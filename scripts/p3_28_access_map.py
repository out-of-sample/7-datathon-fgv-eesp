r"""P3-28: source-backed access map, S1 tools. Spec: tasks/P3-28-agentic-access-map.md; note: results/P3-28_feasibility.md.

snapshot  Download every source with snapshot=yes in results/tables/P3-28_sources.csv that has no successful snapshot
          yet. Raw bytes go to data/raw/p3_28/<source_id>_<UTC>.<ext> (never overwritten; refusals to failed/), one row
          per request in data/raw/p3_28/manifest.csv, checksums appended to data/raw/SHA256SUMS.
card      Offline. Builds results/tables/P3-28_access_cards.md from the case, condition and dependency records:
          (1) every quoted passage must appear verbatim in the latest snapshot of its source (else exit 1);
          (2) leg and route status come from the deterministic rules below, never from a model or a hand edit.
corpus    Offline. Text extract of the latest snapshot of every source -> data/raw/p3_28/text/<id>.txt; hashes and document
          dates -> results/tables/P3-28_corpus.csv (committed); corpus hash = SHA-256 of the sorted per-source text hashes;
          zip for the human coders -> data/raw/p3_28/P3-28_corpus_<hash8>.zip. The closed corpus every method will see.
forms     Blank coding sheets, one per coder: data/raw/p3_28/reference/form_<coder>.csv (cases x applicable fields).
adjudicate  Compares the two filled sheets; writes disagreements to data/raw/p3_28/reference/disagreements.csv and
          prints COUNTS ONLY, so the implementer (agent) never sees reference labels before scoring.
selftest  Asserts the aggregation rules on toy records.

Manual sources (fetch=manual: pages that refuse scripts). A person saves the page in an ordinary browser as
data/raw/p3_28/manual/<source_id>.html (or .pdf), optionally with the final URL in data/raw/p3_28/manual/urls.csv
(source_id,url); `snapshot` then freezes it like a download (retrieval time = file time, saved_by = that person).

Rules (task file, 'Deterministic aggregation rules'). Only `availability` rows in force at the case's as-of date count.
  leg:   any restricted -> restricted; else any conflicting -> conflicting; else any unknown or no rows -> unknown;
         else any conditional whose assumption is not declared by the case -> conditional;
         else any conditional -> satisfied under assumptions; else supported.
  route: restricted if any required leg is; not established if any is unknown or conflicting; conditional if any is;
         otherwise "documented conditions satisfied (under the stated assumptions)". Never "available".
  `term` rows (fees, limits, times) are reported, never aggregated; an unknown term is null, not zero.
Units     amounts in the unit column; dates UTC (valid_from inclusive, valid_to exclusive).
Inputs    results/tables/P3-28_{sources,cases}.csv, data/processed/P3-28_{conditions,dependencies}.csv,
          data/processed/P3-20_premium_daily.csv (observed price, read-only)
Run       .venv/bin/python scripts/p3_28_access_map.py {snapshot,card,selftest}
"""
import csv
import datetime as dt
import hashlib
import html
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / 'results/tables/P3-28_sources.csv'
CASES = ROOT / 'results/tables/P3-28_cases.csv'
CONDS = ROOT / 'data/processed/P3-28_conditions.csv'
DEPS = ROOT / 'data/processed/P3-28_dependencies.csv'
RAW = ROOT / 'data/raw/p3_28'
MANIFEST = RAW / 'manifest.csv'
SUMS = ROOT / 'data/raw/SHA256SUMS'
CARDS = ROOT / 'results/tables/P3-28_access_cards.md'
PREMIUM = ROOT / 'data/processed/P3-20_premium_daily.csv'
LEGS = {'L1': 'BRL funding', 'L2': 'acquisition', 'L3': 'withdrawal / network transfer', 'L4': 'destination receipt'}
EXT = {'html': 'html', 'json': 'json', 'zendesk': 'json', 'bcb': 'json', 'pdf': 'pdf'}
MFIELDS = ['source_id', 'fetch_url', 'retrieved_utc', 'http_status', 'bytes', 'sha256', 'raw_path',
           'doc_created_utc', 'doc_updated_utc', 'fetch', 'saved_by']
UA = 'p3-28-access-map/1 (read-only research script)'
FIELDS = ROOT / 'results/tables/P3-28_fields.csv'
CORPUS = ROOT / 'results/tables/P3-28_corpus.csv'
REF = RAW / 'reference'
CODERS = ('felipe', 'jonathan')
MANUAL_SAVER = 'Renzo (manual browser save)'


def rows(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def split(s, sep=';'):
    return [x.strip() for x in (s or '').split(sep) if x.strip()]


# ---------- snapshot ----------
def doc_dates(kind, body):
    """Publication/update dates the document itself states (blank = explicit unknown)."""
    try:
        d = json.loads(body)
    except ValueError:
        return '', ''
    if kind == 'zendesk':
        return d['article']['created_at'], d['article']['updated_at']
    if kind == 'bcb':
        return d['conteudo'][0]['Data'], ''
    if kind == 'json' and 'lastUpdateTimestamp' in d:
        t = dt.datetime.fromtimestamp(d['lastUpdateTimestamp'] / 1000, dt.timezone.utc)
        return '', t.strftime('%Y-%m-%dT%H:%M:%SZ')
    return '', ''


def snapshot():
    RAW.mkdir(parents=True, exist_ok=True)
    (RAW / 'failed').mkdir(exist_ok=True)
    old = rows(MANIFEST) if MANIFEST.exists() else []
    if old and set(MFIELDS) - set(old[0]):  # add the new columns once; rows keep their values
        with open(MANIFEST, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, MFIELDS, restval='')
            w.writeheader()
            w.writerows([{**m, 'fetch': m.get('fetch') or 'script'} for m in old])
    done = {m['source_id'] for m in old if m['http_status'] == '200'}
    new = not MANIFEST.exists()
    murls = {r['source_id']: r['url'] for r in rows(RAW / 'manual/urls.csv')} if (RAW / 'manual/urls.csv').exists() else {}
    with open(MANIFEST, 'a', newline='', encoding='utf-8') as mf, open(SUMS, 'a', encoding='utf-8') as sf:
        w = csv.DictWriter(mf, MFIELDS)
        if new:
            w.writeheader()
        for s in rows(SOURCES):
            if s['snapshot'] != 'yes' or s['source_id'] in done:
                continue
            if s['fetch'] == 'manual':
                f = next((RAW / 'manual' / f"{s['source_id']}.{e}" for e in ('html', 'pdf')
                          if (RAW / 'manual' / f"{s['source_id']}.{e}").exists()), None)
                if f is None:
                    print(s['source_id'], 'manual save missing:', s['fetch_url'] or s['title'])
                    continue
                body = f.read_bytes()
                now = dt.datetime.fromtimestamp(f.stat().st_mtime, dt.timezone.utc)
                path = RAW / f"{s['source_id']}_{now:%Y%m%dT%H%M%SZ}{f.suffix}"
                path.write_bytes(body)
                sha, rel = hashlib.sha256(body).hexdigest(), path.relative_to(ROOT).as_posix()
                w.writerow(dict(source_id=s['source_id'], fetch_url=murls.get(s['source_id'], s['fetch_url']),
                                retrieved_utc=now.strftime('%Y-%m-%dT%H:%M:%SZ'), http_status=200, bytes=len(body),
                                sha256=sha, raw_path=rel, fetch='manual', saved_by=MANUAL_SAVER))
                sf.write(f'{sha}  {rel}\n')
                print(s['source_id'], 'manual', len(body), rel)
                continue
            now = dt.datetime.now(dt.timezone.utc)
            req = urllib.request.Request(s['fetch_url'], headers={'User-Agent': UA})
            try:
                with urllib.request.urlopen(req, timeout=40) as r:
                    status, body = r.status, r.read()
            except urllib.error.HTTPError as e:
                status, body = e.code, e.read()
            except (urllib.error.URLError, TimeoutError) as e:
                status, body = 0, repr(e).encode()
            name = f"{s['source_id']}_{now:%Y%m%dT%H%M%SZ}.{EXT[s['kind']]}"
            path = RAW / name if status == 200 else RAW / 'failed' / name
            path.write_bytes(body)  # new name per request: raw files are never overwritten
            sha = hashlib.sha256(body).hexdigest()
            created, updated = doc_dates(s['kind'], body.decode('utf-8', 'replace')) if status == 200 else ('', '')
            rel = path.relative_to(ROOT).as_posix()
            w.writerow(dict(source_id=s['source_id'], fetch_url=s['fetch_url'],
                            retrieved_utc=now.strftime('%Y-%m-%dT%H:%M:%SZ'), http_status=status, bytes=len(body),
                            sha256=sha, raw_path=rel, doc_created_utc=created, doc_updated_utc=updated, fetch='script'))
            sf.write(f'{sha}  {rel}\n')
            print(s['source_id'], status, len(body), rel)


# ---------- card ----------
def norm(s):
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


def text_of(path, kind):
    """Plain text a reader sees; passages are checked against this."""
    if kind == 'pdf':
        import subprocess
        return norm(subprocess.run(['pdftotext', '-q', str(path), '-'], capture_output=True, text=True,
                                   check=True).stdout)
    raw = Path(path).read_bytes().decode('utf-8', 'replace')
    if kind == 'json':
        return norm(json.dumps(json.loads(raw), ensure_ascii=False))
    if kind == 'zendesk':
        a = json.loads(raw)['article']
        raw = a['title'] + ' ' + (a['body'] or '')
    elif kind == 'bcb':
        c = json.loads(raw)['conteudo'][0]
        raw = c['Titulo'] + ' ' + c['Texto']
    raw = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', raw)
    return norm(re.sub(r'<[^>]+>', ' ', raw))


def kind_of(s, m):
    """A manual save may be HTML or a browser 'Save as PDF'; the file extension decides."""
    return 'pdf' if m['raw_path'].endswith('.pdf') else s['kind']


def in_force(r, day):
    return (not r['valid_from'] or r['valid_from'] <= day) and (not r['valid_to'] or day < r['valid_to'])


def leg_status(conds, day, declared):
    st = [r for r in conds if r['kind'] == 'availability' and in_force(r, day)]
    states = {r['state'] for r in st}
    for s in ('restricted', 'conflicting'):
        if s in states:
            return s
    if not st or 'unknown' in states:
        return 'unknown'
    cond = [r for r in st if r['state'] == 'conditional']
    if any(not set(split(r['assumption_ids'])) <= declared or not r['assumption_ids'] for r in cond):
        return 'conditional'
    return 'satisfied under assumptions' if cond else 'supported'


def route_status(legs):
    v = legs.values()
    if 'restricted' in v:
        return 'restricted on ' + ', '.join(k for k, s in legs.items() if s == 'restricted')
    bad = [k for k, s in legs.items() if s in ('unknown', 'conflicting')]
    if bad:
        return 'not established: missing or conflicting evidence on ' + ', '.join(bad)
    if 'conditional' in v:
        return 'conditional on ' + ', '.join(k for k, s in legs.items() if s == 'conditional')
    if 'satisfied under assumptions' in v:
        return 'documented conditions satisfied under the stated assumptions'
    return 'documented conditions satisfied'


def card():
    src = {s['source_id']: s for s in rows(SOURCES)}
    snap = {}
    for m in rows(MANIFEST):
        if m['http_status'] == '200':
            snap[m['source_id']] = m  # manifest is chronological: keep the latest
    texts = {k: text_of(ROOT / m['raw_path'], kind_of(src[k], m)) for k, m in snap.items()}
    conds, deps = rows(CONDS), rows(DEPS)
    fails, out = [], ['# P3-28 access cards', '',
                      'Generated by `scripts/p3_28_access_map.py card` from `results/tables/P3-28_cases.csv`, '
                      '`data/processed/P3-28_conditions.csv` and `P3-28_dependencies.csv`. Do not edit by hand. '
                      'Development cases coded by one reader: **not** reference labels. '
                      'A status describes what the frozen documents support; it is not proof of account access, '
                      'liquidity or a completed payment.', '']

    def check(r):
        ids, ps = split(r['source_ids']), split(r['passages'], '||')
        if len(ids) != len(ps):
            fails.append(f"{r.get('cond_id', r.get('entity'))}: {len(ids)} sources, {len(ps)} passages")
            return '✗'
        for i, p in zip(ids, ps):
            if i not in texts or norm(p) not in texts[i]:
                fails.append(f"{r.get('cond_id', r.get('entity'))}: passage not found in {i}")
                return '✗'
        return '✓' if ids else '–'

    for c in rows(CASES):
        day = c['as_of_utc'][:10]
        declared = {a.split('=')[0] for a in split(c['assumptions'], '|')}
        cc = [r for r in conds if r['case_id'] == c['case_id']]
        if not cc:
            continue
        legs = {l: leg_status([r for r in cc if r['leg'] == l], day, declared) for l in split(c['required_legs'])}
        out += [f"## {c['case_id']} — {c['route_id']} · {c['profile_id']} · as of {c['as_of_utc']} ({c['mode']})", '',
                f"**Operation.** {c['operation']}. Amount {int(float(c['amount'])):,} {c['amount_unit']}; "
                f"chain {c['chain']}.", '',
                f"**Route status (generated): {route_status(legs)}.**", '',
                '| Leg | Status |', '|---|---|']
        out += [f'| {l} {LEGS[l]} | {s} |' for l, s in legs.items()]
        out += ['', '**Assumptions (scenario, never scored as facts)**', '']
        out += [f'- {a.replace("=", ": ", 1)}' for a in split(c['assumptions'], '|')]
        out += ['', '**Documented conditions and unknowns**', '',
                '| ID | Leg | Predicate | Kind | State | Value | Evidence | Sources | In force on as-of | Assumption | Passage check |',
                '|---|---|---|---|---|---|---|---|---|---|---|']
        for r in cc:
            val = f"{r['value']} {r['unit']}".strip() if r['value'] else ('null' if r['kind'] == 'term' else '')
            out.append(f"| {r['cond_id']} | {r['leg']} | {r['predicate']} | {r['kind']} | {r['state']} | {val} | "
                       f"{r['evidence_type'].replace(';', ', ')} | {r['source_ids'].replace(';', ', ')} | "
                       f"{'yes' if in_force(r, day) else 'no (from ' + r['valid_from'] + ')'} | "
                       f"{r['assumption_ids']} | {check(r)} |")
        notes = [r for r in cc if r['exceptions']]
        if notes:
            out += ['', '**Exceptions and scope notes**', '']
            out += [f"- {r['cond_id']}: {r['exceptions']}" for r in notes]
        out += ['', '**Documented dependencies**', '', '| Leg | Type | Entity | Identifier | Sources | Note | Passage check |',
                '|---|---|---|---|---|---|---|']
        out += [f"| {d['leg']} | {d['dependency_type']} | {d['entity']} | {d['identifier']} | {d['source_ids']} | "
                f"{d['note']} | {check(d)} |" for d in deps if d['case_id'] == c['case_id']]
        if c['route_id'] == 'FOX' and PREMIUM.exists():  # observed price: a measured quote, not a condition
            p = [r for r in rows(PREMIUM) if r['Foxbit'] and r['date_brt'] <= day][-1]
            out += ['', '**Observed price (measured; not a condition and not evidence of access)**', '',
                    f"Foxbit USDT/BRL premium over PTAX on {p['date_brt']} (latest PTAX window on or before the "
                    f"as-of date): {float(p['Foxbit']):.1f} bps (`data/processed/P3-20_premium_daily.csv`, F-035). "
                    'In June 2026 it rose +93.3 bps on Foxbit after the 23 Jun notice (F-009).']
        used = sorted({i for r in cc for i in split(r['source_ids'])} | {i for d in deps for i in split(d['source_ids'])})
        out += ['', '**Sources (frozen snapshots)**', '',
                '| ID | Publisher | Document | Doc. created | Doc. updated | Retrieved | SHA-256 (first 12) |',
                '|---|---|---|---|---|---|---|']
        for i in used:
            m = snap.get(i, {})
            out.append(f"| {i} | {src[i]['publisher']} | {src[i]['title']} | {m.get('doc_created_utc') or 'unknown'} | "
                       f"{m.get('doc_updated_utc') or 'unknown'} | {m.get('retrieved_utc', 'NOT SNAPSHOTTED')} | "
                       f"{m.get('sha256', '')[:12]} |")
        out.append('')
    CARDS.write_text('\n'.join(out) + '\n', encoding='utf-8')
    print('wrote', CARDS.relative_to(ROOT))
    if fails:
        print('PASSAGE CHECK FAILED:', *fails, sep='\n  ')
        sys.exit(1)


def latest():
    src = {s['source_id']: s for s in rows(SOURCES)}
    snap = {}
    for m in rows(MANIFEST):
        if m['http_status'] == '200' and m['source_id'] in src:
            snap[m['source_id']] = m
    return src, snap


def corpus():
    import zipfile
    src, snap = latest()
    (RAW / 'text').mkdir(parents=True, exist_ok=True)
    out = []
    for i, m in sorted(snap.items()):
        t = text_of(ROOT / m['raw_path'], kind_of(src[i], m))
        (RAW / 'text' / f'{i}.txt').write_text(t + '\n', encoding='utf-8')
        out.append(dict(source_id=i, family=src[i]['family'], split=src[i]['split'], publisher=src[i]['publisher'],
                        title=src[i]['title'], url=m['fetch_url'], retrieved_utc=m['retrieved_utc'],
                        doc_created_utc=m['doc_created_utc'], doc_updated_utc=m['doc_updated_utc'],
                        fetch=m.get('fetch', 'script'), raw_sha256=m['sha256'], chars=len(t),
                        text_sha256=hashlib.sha256((t + '\n').encode()).hexdigest()))
    h = hashlib.sha256(''.join(o['text_sha256'] for o in out).encode()).hexdigest()
    with open(CORPUS, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, list(out[0]))
        w.writeheader()
        w.writerows(out)
    z = RAW / f'P3-28_corpus_{h[:8]}.zip'
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(CORPUS, 'P3-28_corpus.csv')
        for i in snap:
            zf.write(RAW / 'text' / f'{i}.txt', f'text/{i}.txt')
        for p in (CASES, FIELDS, ROOT / 'results/P3-28_rubric.md'):
            zf.write(p, p.name)
    missing = [s['source_id'] for s in src.values() if s['snapshot'] == 'yes' and s['source_id'] not in snap]
    print(f'corpus: {len(out)} sources, hash {h}, zip {z.relative_to(ROOT)}; missing: {missing or "none"}')


def form_rows():
    fields = rows(FIELDS)
    for c in rows(CASES):
        kind = 'fund' if c['profile_id'] == 'FUND-BR' else 'exchange'
        for f in fields:
            if f['applies_to'] == kind:
                yield dict(case_id=c['case_id'], field_id=f['field_id'], leg=f['leg'], kind=f['kind'],
                           provider=c['route_id'], profile=c['profile_id'], asset=c['destination_asset'],
                           network=c['chain'], as_of=c['as_of_utc'][:10], question=f['question'],
                           answer_type=f['answer'], unit_hint=f['unit_hint'], state='', value='', unit='',
                           source_ids='', passages='', notes='')


def forms():
    REF.mkdir(parents=True, exist_ok=True)
    rs = list(form_rows())
    for c in CODERS:
        p = REF / f'form_{c}.csv'
        if p.exists():
            print('exists, not overwritten:', p.relative_to(ROOT))
            continue
        with open(p, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, list(rs[0]))
            w.writeheader()
            w.writerows(rs)
        print(f'{p.relative_to(ROOT)}: {len(rs)} rows')


def adjudicate():
    """Counts only: the agent must not see reference labels before scoring."""
    src, snap = latest()
    texts = {i: (RAW / 'text' / f'{i}.txt').read_text(encoding='utf-8') for i in snap
             if (RAW / 'text' / f'{i}.txt').exists()}
    a, b = ({(r['case_id'], r['field_id']): r for r in rows(REF / f'form_{c}.csv')} for c in CODERS)
    def v(r):
        return (r['state'].strip().lower(), re.sub(r'\s+', ' ', r['value'].strip().lower()))
    dis, blank, badp = [], 0, 0
    for k in a:
        for r in (a[k], b.get(k, {})):
            if not r.get('state') and not r.get('value'):
                blank += 1
            for i, p in zip(split(r.get('source_ids')), split(r.get('passages'), '||')):
                if i not in texts or norm(p) not in texts[i]:
                    badp += 1
        if k not in b or v(a[k]) != v(b[k]):
            dis.append({'case_id': k[0], 'field_id': k[1],
                        **{f'{c}_{x}': r.get(x, '') for c, r in zip(CODERS, (a[k], b.get(k, {})))
                           for x in ('state', 'value', 'source_ids', 'passages', 'notes')}, 'adjudicated_state': '',
                        'adjudicated_value': '', 'adjudication_note': ''})
    if dis:
        with open(REF / 'disagreements.csv', 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, list(dis[0]))
            w.writeheader()
            w.writerows(dis)
    print(f'fields {len(a)}; disagreements {len(dis)} ({len(dis) / len(a):.0%}); blank answers {blank}; '
          f'passages not found verbatim {badp}. Details for the coders only: data/raw/p3_28/reference/disagreements.csv')


def selftest():
    def r(state, kind='availability', a='', vf=''):
        return dict(kind=kind, state=state, assumption_ids=a, valid_from=vf, valid_to='')
    d = '2026-11-07'
    assert leg_status([r('supported'), r('restricted')], d, set()) == 'restricted'
    assert leg_status([r('supported'), r('unknown')], d, set()) == 'unknown'
    assert leg_status([], d, set()) == 'unknown'                                  # no evidence is not availability
    assert leg_status([r('supported', kind='term'), r('unknown', kind='term')], d, set()) == 'unknown'
    assert leg_status([r('conditional', a='A1')], d, {'A1'}) == 'satisfied under assumptions'
    assert leg_status([r('conditional', a='A1')], d, set()) == 'conditional'
    assert leg_status([r('conditional')], d, {'A1'}) == 'conditional'            # no assumption named
    assert leg_status([r('supported'), r('restricted', vf='2027-01-01')], d, set()) == 'supported'  # not yet in force
    assert route_status({'L1': 'supported', 'L2': 'unknown'}).startswith('not established')
    assert route_status({'L1': 'restricted', 'L2': 'unknown'}) == 'restricted on L1'
    assert route_status({'L1': 'supported', 'L2': 'satisfied under assumptions'}).endswith('stated assumptions')
    assert 'available' not in route_status({'L1': 'supported'})
    print('selftest ok')


if __name__ == '__main__':
    {'snapshot': snapshot, 'card': card, 'corpus': corpus, 'forms': forms, 'adjudicate': adjudicate,
     'selftest': selftest}[sys.argv[1]]()
