"""P3-38: reproduce comparison-review findings with synthetic inputs, offline.

Run: python3 scripts/p3_38_comparison_audit.py [--from-git]
Inputs: results/tables/P3-38_inputs.csv and its frozen files in data/raw/p3_38/.
Outputs: results/tables/P3-38_audit_checks.csv and P3-38_inventory.csv.
Missing snapshots are read from the reviewed Git commit and hash-checked;
--from-git exercises that reproduction path without using local raw copies.
No model calls, human labels, real run outputs or P3-28 output files are used.
The reviewed functions are extracted from the hashed snapshot with Python's AST.
Their temporary files stay in a temporary directory. A successful command means
the audit completed, not that the reviewed scorer passed the contract checks.
"""
import ast
import argparse
import contextlib
import csv
import datetime as dt
import hashlib
import html
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'results/tables/P3-38_inputs.csv'
OUTPUT = ROOT / 'results/tables/P3-38_audit_checks.csv'
REVIEWED_COMMIT = 'c63aa7092352640ebd17b2228e7f1b86ed9f9c92'


def rows(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def frozen(from_git=False):
    files = {}
    for row in rows(MANIFEST):
        snapshot = ROOT / row['snapshot_path']
        if snapshot.exists() and not from_git:
            data = snapshot.read_bytes()
        else:
            data = subprocess.run(['git', 'show', REVIEWED_COMMIT + ':' + row['source_path']],
                                  cwd=ROOT, check=True, capture_output=True).stdout
        if hashlib.sha256(data).hexdigest() != row['sha256']:
            raise ValueError('Snapshot hash mismatch: ' + row['source_path'])
        files[row['source_path']] = data.decode('utf-8')
    return files


def load_functions(source, names, env):
    tree = ast.parse(source)
    selected = [node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name in names]
    if {node.name for node in selected} != set(names):
        raise ValueError('The snapshot does not contain all required functions')
    exec(compile(ast.Module(body=selected, type_ignores=[]), '<reviewed-snapshot>', 'exec'), env)


def environment(files):
    env = dict(re=re, html=html, csv=csv, json=json, hashlib=hashlib, dt=dt,
               tempfile=tempfile, shutil=shutil)
    load_functions(files['scripts/p3_28_access_map.py'], ['norm'], env)
    env['M'] = SimpleNamespace(norm=env['norm'], rows=rows, latest=lambda: ({}, {'S': {}}))
    load_functions(files['scripts/p3_28_methods.py'],
                   ['num', 'category', 'correct', 'answerable', 'sid', 'evidence_ok', 'score', 'run_one'], env)
    return env


def field(fid='F01', answer='state', kind='availability'):
    return dict(field_id=fid, answer=answer, kind=kind)


def reference(fid='F01', state='supported', value='', unit='', case='C'):
    return dict(case_id=case, field_id=fid, state=state, value=value, unit=unit)


def answer(fid='F01', state='supported', value='', unit='', passage='Pix deposits are accepted.', **extra):
    return dict(field_id=fid, state=state, value=value, unit=unit,
                source_ids=['S'], passages=[passage], **extra)


def record(case, answers, errors=None):
    return dict(method='A', case_id=case, repeat=1, answers=answers, permitted=['S'],
                errors=errors or [], model='synthetic', n_calls=1, turns=1,
                wall_s=1, usage={}, notional_usd=0)


def score_fixture(files, fields, refs, runs, cases=None):
    env = environment(files)
    cases = cases or sorted({r['case_id'] for r in refs})
    with tempfile.TemporaryDirectory(prefix='p338_score_') as tmp:
        root = Path(tmp)
        (root / 'results/tables').mkdir(parents=True)
        run_dir = root / 'runs/A'
        run_dir.mkdir(parents=True)
        for index, run in enumerate(runs):
            (run_dir / f'{index}.json').write_text(json.dumps(run))
        ref_file = root / 'reference.csv'
        with ref_file.open('w', newline='') as f:
            writer = csv.DictWriter(f, refs[0])
            writer.writeheader()
            writer.writerows(refs)
        env.update(ROOT=root, RUNS=root / 'runs',
                   cases=lambda: {cid: dict(case_id=cid, split='dev', group_id='synthetic') for cid in cases},
                   fields_for=lambda c: fields, doc_text=lambda i: 'Pix deposits are accepted. Contact support.')
        printed = io.StringIO()
        with contextlib.redirect_stdout(printed):
            env['score'](ref_file, 'dev')
        return rows(root / 'results/tables/P3-28_case_scores.csv'), printed.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--from-git', action='store_true')
    args = parser.parse_args()
    files = frozen(args.from_git)
    env = environment(files)
    checks = []

    def check(cid, finding, description, expected, observed):
        checks.append(dict(check_id=cid, finding=finding, synthetic_case=description,
                           expected=json.dumps(expected), observed=json.dumps(observed),
                           contract_pass=observed == expected))

    check('C01', 'control', 'Correct number and unit', True,
          env['correct'](field('F04', 'value', 'term'), reference('F04', value='72', unit='hours'),
                         answer('F04', value='72', unit='hours')))
    check('C02', 'R1', 'Same number, wrong unit: 72 hours versus 72 days', False,
          env['correct'](field('F04', 'value', 'term'), reference('F04', value='72', unit='hours'),
                         answer('F04', value='72', unit='days')))
    check('C03', 'R1', 'G02 wrong nonempty resumption condition', False,
          env['correct'](field('G02', 'value', 'term'), reference('G02', value='regulatory alignment'),
                         answer('G02', value='no approval is required')))
    check('C04', 'R1', 'F03 correct state but opposite requirement', False,
          env['correct'](field('F03', 'state+value'), reference('F03', value='company verification required'),
                         answer('F03', value='no company verification required')))
    check('C05', 'R2', 'Empty quotation should not count as evidence', False,
          env['evidence_ok'](answer(passage=''), ['S'], {'S': 'Pix deposits are accepted.'}))
    check('C06', 'control', 'Quotation from an unpermitted source is rejected', False,
          env['evidence_ok'](answer(), [], {'S': 'Pix deposits are accepted.'}))
    check('C07', 'R2', 'Matching state with a real but irrelevant quotation earns no coverage', 0.0,
          float(score_fixture(files, [field()], [reference()],
                              [record('C', [answer(passage='Contact support.')])])[0][0]['sac']))
    check('C08', 'R3', 'Failed run with a retained draft must score zero', 0.0,
          float(score_fixture(files, [field()], [reference()],
                              [record('C', [answer()], errors=['timeout'])])[0][0]['sac']))
    missing, _ = score_fixture(files, [field()], [reference(), reference(case='MISSING')],
                               [record('C', [answer()])], cases=['C', 'MISSING'])
    check('C09', 'R3', 'Scheduled case with no run file remains in the result', 2, len(missing))
    try:
        score_fixture(files, [field(), field('F07')], [reference()], [record('C', [answer()])])
        rejects_incomplete = False
    except (ValueError, KeyError, AssertionError):
        rejects_incomplete = True
    check('C10', 'R3', 'Missing reference row stops scoring instead of shrinking denominator', True, rejects_incomplete)
    _, summary = score_fixture(files, [field()], [reference(), reference(state='unknown', case='U')],
                                [record('C', [answer()]), record('U', [answer(state='unknown', passage='')])])
    macro = float(next(line for line in summary.splitlines() if line.startswith('A |')).split('|')[2])
    check('C11', 'R3', 'A case with zero answerable fields is excluded from SAC macro-average', 1.0, macro)
    note_run = record('C', [answer(state='unknown', passage='', note='The complete route is available without restrictions.')])
    note_score, _ = score_fixture(files, [field()], [reference(state='unknown')], [note_run])
    check('C12', 'R4', 'Unsupported route assertion in free text is detected', True,
          int(note_score[0]['unsupported_positive']) > 0)
    duplicate_run = record('C', [answer(), answer(state='unknown', passage='')])
    dup_score, _ = score_fixture(files, [field()], [reference(state='unknown')], [duplicate_run])
    check('C13', 'R4', 'Duplicate field cannot hide an earlier unsupported positive', True,
          int(dup_score[0]['unsupported_positive']) > 0)

    # Exercise the real run-record writer with fake model calls. No CLI is invoked.
    with tempfile.TemporaryDirectory(prefix='p338_usage_') as tmp:
        root = Path(tmp)
        (root / 'text').mkdir()
        calls = [dict(modelUsage={'same-model': {'inputTokens': n}}, total_cost_usd=0)
                 for n in (10, 20)]
        env.update(RUNS=root / 'runs', TEXT=root / 'text', MODEL='synthetic', SYSTEM='', SCHEMA={}, FIELD_KW={},
                   cases=lambda: {'C': {}}, fields_for=lambda c: [], permitted=lambda c: [],
                   case_text=lambda c, fs: '', corpus_hash=lambda ids: 'synthetic',
                   method_B2=lambda c, fs, ids, wd: dict(answers=[], calls=calls))
        env['run_one']('B2', 'C', 1)
        saved = json.loads((root / 'runs/B2/C_r1.json').read_text())
    check('C14', 'R5', 'Token use sums both calls to the same model', 30,
          saved['usage']['same-model']['inputTokens'])

    stale = record('C', [answer()])
    stale['corpus_hash'] = 'intentionally-not-the-current-corpus-hash'
    try:
        score_fixture(files, [field()], [reference()], [stale])
        rejects_stale = False
    except (ValueError, KeyError, AssertionError):
        rejects_stale = True
    check('C15', 'R7', 'Run from a different corpus is rejected before scoring', True, rejects_stale)

    with OUTPUT.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, checks[0], lineterminator='\n')
        writer.writeheader()
        writer.writerows(checks)
    cases = list(csv.DictReader(io.StringIO(files['results/tables/P3-28_cases.csv'])))
    corpus = list(csv.DictReader(io.StringIO(files['results/tables/P3-28_corpus.csv'])))
    inventory = []
    for split, family in sorted({(c['split'], c['group_id']) for c in cases}):
        inventory.append(dict(split=split, family=family,
                              cases=sum(c['split'] == split and c['group_id'] == family for c in cases),
                              provider_family_documents=sum(s['family'] == family for s in corpus),
                              shared_documents=sum(s['split'] == 'shared' for s in corpus)))
    inventory_path = ROOT / 'results/tables/P3-38_inventory.csv'
    with inventory_path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, inventory[0], lineterminator='\n')
        writer.writeheader()
        writer.writerows(inventory)
    failed = sum(not c['contract_pass'] for c in checks)
    print(f'Audit completed: {len(checks)} synthetic checks; {failed} contract violations; '
          f'{len(checks) - failed} controls passed. No model performance was measured.')
    print(OUTPUT.relative_to(ROOT))
    print(inventory_path.relative_to(ROOT))


if __name__ == '__main__':
    main()
