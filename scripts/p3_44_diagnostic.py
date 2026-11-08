"""Post-hoc saved-answer sensitivity; no inference, no changes to frozen records.

Run: python scripts/p3_44_diagnostic.py
Requires the ignored v4 raw bundle. Original scoring is reproduced first. Only a
failed read of the exact erroneous dispatch folder can be waived, in memory,
after its saved error response confirms no file was returned. This is not a
protocol score, a repaired execution, or a new benchmark winner.
"""
import contextlib
import copy
import io
import json
import shutil
from pathlib import Path

import p3_44_evaluate as E

P, pilot = E.P, E.pilot
ROOT = E.ROOT


def normalized(value):
    return str(value).replace('\\', '/').lower()


def eligible(cid, repeat, run):
    """Fail closed unless all offending calls are dispatched missing-file reads."""
    if run.get('errors') != ['adaptive_tool_outside_corpus_reader']:
        return 0
    stem = f'A_{cid}_r{repeat}'
    cwd = pilot.WORK / stem
    prompt = pilot.FREEZE / 'prompts' / f'{stem}.txt'
    wrong = pilot.FREEZE / 'workspaces_v4' / stem
    trace = pilot.RUNS / 'A' / f'{cid}_r{repeat}_call1.jsonl'
    events = pilot.extract_events(trace.read_text(encoding='utf-8'))
    cleaned = copy.deepcopy(events)
    count = 0
    dispatch = '\n'.join(e.get('content', '') for e in events if e.get('type') == 'SYSTEM_MESSAGE')
    if normalized(wrong) not in normalized(dispatch):
        return 0
    for i, event in enumerate(events):
        if event.get('type') != 'PLANNER_RESPONSE':
            continue
        kept = []
        calls = event.get('tool_calls') or []
        for call in calls:
            single = [{'type': 'PLANNER_RESPONSE', 'tool_calls': [call]}]
            if not pilot.trace_violations(single, 'A', cwd, prompt):
                kept.append(call)
                continue
            args = call.get('args') or {}
            target = Path(args.get('AbsolutePath') or args.get('Path') or '')
            if (call.get('name') != 'view_file' or target.parent.resolve() != wrong.resolve()
                    or target.name not in {sid + '.txt' for sid in run['permitted']}
                    or target.exists() or len(calls) != 1):
                return 0
            response = events[i + 1] if i + 1 < len(events) else {}
            error = response.get('error', '')
            if (response.get('status') != 'ERROR' or normalized(target) not in normalized(error)
                    or 'cannot find the path specified' not in error.lower()):
                return 0
            count += 1
        cleaned[i]['tool_calls'] = kept
    if pilot.trace_violations(cleaned, 'A', cwd, prompt):
        return 0
    return count


def run():
    frozen = sorted(pilot.RUNS.glob('*/*')) + sorted(E.REF.glob('*.csv'))
    originals = sorted(E.TABLES.glob('P3-44_*.csv')) + [E.TABLES / 'P3-44_verdict.json']
    originals = [p for p in originals if not p.name.startswith('P3-44_diagnostic_')]
    before = {p: pilot.digest(p.read_bytes()) for p in frozen + originals if p.is_file()}
    summary, waivers = [], []
    preflight = P.audit_preflight
    old_root = P.ROOT
    for split in ('dev', 'heldout'):
        cases = E.configure(split)
        E.validate_reference(E.REF / 'reference.csv')
        audit = E.REF / f'audit_{split}.csv'
        _, _, saved = preflight(cases, '_' + split, audit)
        selected = {}
        for (cid, method, repeat), record in saved.items():
            if record and method == 'A':
                n = eligible(cid, repeat, record)
                if n:
                    selected[(cid, method, repeat)] = n
                    waivers.append(dict(split=split, case_id=cid, repeat=repeat, failed_reads=n,
                        reason='dispatch supplied wrong folder; saved response is missing-path error',
                        run_sha256=pilot.digest((pilot.RUNS / method / f'{cid}_r{repeat}.json').read_bytes()),
                        trace_sha256=pilot.digest((pilot.RUNS / method / f'{cid}_r{repeat}_call1.jsonl').read_bytes())))
        outroot = ROOT / 'scratch/p3_44_diagnostic' / split
        (outroot / 'results/tables').mkdir(parents=True, exist_ok=True)
        P.ROOT = outroot
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                P.score(E.REF / 'reference.csv', split, '_strict', audit)
            for name in ('case_scores', 'errors', 'costs'):
                strict = outroot / 'results/tables' / f'P3-28_{name}_strict.csv'
                original = E.TABLES / f'P3-44_{name}_{split}.csv'
                if P.M.rows(strict) != P.M.rows(original):
                    raise ValueError(f'Original score reproduction differs: {original.name}')

            def diagnostic_preflight(*args, **kwargs):
                aud, required, runs = preflight(*args, **kwargs)
                runs = copy.deepcopy(runs)
                for key in selected:
                    runs[key]['errors'] = []
                return aud, required, runs

            P.audit_preflight = diagnostic_preflight
            with contextlib.redirect_stdout(io.StringIO()):
                P.score(E.REF / 'reference.csv', split, '_diagnostic', audit)
        finally:
            P.audit_preflight = preflight
            P.ROOT = old_root
        src = outroot / 'results/tables/P3-28_case_scores_diagnostic.csv'
        rows = P.M.rows(src)
        shutil.copyfile(src, E.TABLES / f'P3-44_diagnostic_case_scores_{split}.csv')
        strict_rows = P.M.rows(E.TABLES / f'P3-44_case_scores_{split}.csv')
        for method in pilot.METHODS:
            mr = [r for r in rows if r['method'] == method]
            groups = {}
            for row in mr:
                if row['sac'] != '':
                    groups.setdefault(row['case_id'], []).append(float(row['sac']))
            means = [sum(v)/len(v) for v in groups.values()]
            guard = sum(int(r['unsupported_positive']) for r in mr)
            assert guard == sum(int(r['unsupported_positive']) for r in strict_rows if r['method'] == method)
            if method != 'A':
                assert mr == [r for r in strict_rows if r['method'] == method]
            summary.append(dict(split=split, method=method, label='post-hoc diagnostic, not protocol result',
                sac_macro=sum(means)/len(means), waived_runs=sum(k[1] == method for k in selected),
                failed_runs=sum(r['failed_run'] == 'True' for r in mr),
                unsupported_claim_representations=guard))
    assert all(pilot.digest(p.read_bytes()) == digest for p, digest in before.items()), 'Frozen inputs/original outputs changed'
    E.write_csv(E.TABLES / 'P3-44_diagnostic_summary.csv', summary)
    if waivers:
        E.write_csv(E.TABLES / 'P3-44_diagnostic_waivers.csv', waivers)
    receipt = dict(label='post-hoc saved-answer diagnostic; not a protocol amendment or new execution',
        original_scores_reproduced=True, original_inputs_outputs_unchanged=True,
        reference_sha256=pilot.digest((E.REF / 'reference.csv').read_bytes()),
        audits={s: pilot.digest((E.REF / f'audit_{s}.csv').read_bytes()) for s in ('dev', 'heldout')},
        config_sha256=pilot.digest((pilot.FREEZE / 'config.json').read_bytes()),
        waived_runs=len(waivers), inference_calls=0,
        limitations='Same AI reference and semantic audit retained; real dispatch error and resource differences remain. No superiority claim.')
    receipt['output_sha256'] = {p.name: pilot.digest(p.read_bytes()) for p in
        E.TABLES.glob('P3-44_diagnostic_*.csv')}
    receipt['script_sha256'] = pilot.digest(Path(__file__).read_bytes())
    (E.TABLES / 'P3-44_diagnostic_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    run()
