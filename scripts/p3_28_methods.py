r"""P3-28 S3-S4: the four methods (B0, B1, B2, A) and the scorer. Spec: tasks/P3-28-agentic-access-map.md;
frozen settings: results/P3-28_protocol.md. Helpers (corpus text, passage check) come from p3_28_access_map.py.

run    .venv/bin/python scripts/p3_28_methods.py run <B0|B1|B2|A> <dev|heldout|CASE_ID[,CASE_ID]> [--repeats N] [--workers W]
       One JSON per run in data/raw/p3_28/runs/<method>/<case>_r<k>.json: method, case, repeat, model, prompt hash,
       corpus hash, start/end UTC, wall time, usage per model, turns, stop reason, raw result, parsed answers.
       Existing runs are never overwritten (a failed or timed-out run stays and is scored as zero answered fields).
score  .venv/bin/python scripts/p3_28_methods.py score <reference.csv> <dev|heldout> [--tag TAG]
       -> results/tables/P3-28_case_scores<TAG>.csv, P3-28_errors<TAG>.csv, P3-28_costs<TAG>.csv; summary printed.
       Offline. The reference CSV has the coding-form columns (case_id, field_id, state, value, unit, source_ids, passages).

Methods (same case text, same permitted documents = the case's provider family + shared rules/issuers/third-party):
  B0  deterministic keyword rules, no model; `unknown` whenever no rule fires.
  B1  fixed keyword retrieval (top chunks per field) -> one model call, no tools.
  B2  same retrieval -> extract call -> verify call (model rechecks each answer against the chunks) -> deterministic
      verbatim filter (answers whose passages are not found word for word become unknown). No adaptive queries.
  A   one tool-using agent (Read, Grep, Glob) in a sandbox holding only the permitted .txt files; it chooses its own
      searches and reads and must verify passages with Grep. Turn ceiling MAX_TURNS.
Model     claude CLI (Claude Code bundled with the VS Code extension), --model MODEL for B1/B2/A, isolated with
          --restricted --strict-mcp-config --no-session-persistence and our own --system-prompt; the CLI also makes a
          small internal Haiku call, logged in usage. Runs on Renzo's existing plan (no API key).
Scoring   field-level; see score() docstring.
"""
import csv
import concurrent.futures as cf
import datetime as dt
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import p3_28_access_map as M  # noqa: E402

ROOT, RAW = M.ROOT, M.RAW
RUNS = RAW / 'runs'
TEXT = RAW / 'text'
CLAUDE = os.environ.get('P3_28_CLAUDE', str(Path.home() / '.vscode/extensions/anthropic.claude-code-2.1.318-linux-x64/'
                                                         'resources/native-binary/claude'))
MODEL = 'claude-sonnet-5-5'
MAX_TURNS = 40
TIMEOUT_S = 900
TOP_K = 8            # chunks per field for B1/B2
CHUNK = 700          # characters per retrieval chunk (overlap 200)
FAMILY_OF_GROUP = {'foxbit': 'foxbit', 'funds-press': 'funds-press', 'avenia': 'avenia', 'binance': 'binance', 'mb': 'mb'}
SHARED = {'shared'}
STATES = ['supported', 'restricted', 'conditional', 'conflicting', 'unknown', 'not_applicable']

# Field keywords (pt/en) used by B0 and by the B1/B2 retrieval; fixed after development.
FIELD_KW = {
    'F01': 'pix depósito deposit reais brl', 'F02': 'terceiros titular titularidade cpf cnpj mesma own name',
    'F03': 'verificação verificar kyc kyb cadastro compliance aprovação verification', 'F04': 'prazo horas dias úteis análise 72h',
    'F05': 'limite limites depósito mensal deposit limit', 'F06': 'autorização autorizada psav banco central 589 pedido protocolou',
    'F07': 'comprar compra stablecoin usdt usdc dólar digital buy', 'F08': 'taxa taker maker ordem mercado ativa fee %',
    'F09': 'stablecoin dólar digital comercial separadamente contrato condições', 'F10': 'saque saques carteira externa wallet withdraw enviar',
    'F11': 'rede redes network trc-20 erc-20 polygon base solana tron', 'F12': 'taxa saque rede fee withdrawal network',
    'F13': 'declaração destino origem travel rule carteira própria autocustódia declarar', 'F14': 'limite saque cripto withdrawal limit personalizado',
    'F15': 'contract address token blockchain rede', 'G01': 'fundos câmbio importação suspensão descontinuidade liberou intermediação',
    'G02': 'alinhamento regulador condição retomar suspensas'}
ASSET_FIELDS = {'F07', 'F10', 'F11', 'F12', 'F15'}  # fields whose retrieval query adds the case asset and network
PROFILE_FIELDS = {'F02', 'F03', 'F04', 'F05', 'F09', 'F14'}  # queries that add the profile's words
PROFILE_KW = {'PJ-BR': 'pj jurídica empresa empresas cnpj corporativo corporate business company',
              'PF-BR': 'pf física cpf pessoa individual', 'FUND-BR': 'fundo fundos'}
B0_RULES = {  # field -> (regex that must match one sentence, state, value)
    'F01': (r'(dep[oó]sit\w*[^.]{0,80}\bpix\b|\bpix\b[^.]{0,80}dep[oó]sit)', 'supported', ''),
    'F02': (r'(dep[oó]sitos? de terceiros|mesma titularidade|same name|own name)', 'supported', 'yes'),
    'F13': (r'(declara\w+ (de )?(origem|destino)|travel rule|regra de viagem)', 'supported', ''),
}

SYSTEM = """You are an evidence analyst. You answer fixed questions about the documented conditions for one case: a
profile (PJ-BR = Brazilian non-financial company; PF-BR = resident individual; FUND-BR = investment fund) acquiring a
stablecoin with reais and withdrawing it to its own self-custodied wallet on a given network, at a given as-of date.
Rules:
- Use ONLY the documents provided (or found with your tools). Never use memory or outside knowledge.
- States: supported (a document states it for this profile/date), restricted (a document says it cannot be done or a rule
  forbids it), conditional (possible only if something the documents do not establish holds), conflicting (documents
  disagree and nothing settles it), unknown (no document answers; missing is not "no"), not_applicable.
- Questions asking WHAT is required (F02, F03, F09, F13): use supported when a document states the requirement, with the
  requirement in value; unknown if no document says.
- Profile matters: a page for individuals does not answer a company question unless it says it applies to all clients.
  Network matters: a fee or status without a named network does not answer a network-specific question (unknown).
  Dates matter: a rule starting after the as-of date is not in force. Advertising is a provider statement.
- Fees/limits: never 0 for a missing value; leave value empty and state unknown. Convert percent to bps (0.50% = 50).
- "Can" questions (F01, F07, F10, F11, F15, G01) are conditional when a document makes the operation depend on an
  approval or review specific to it (e.g. a separate commercial analysis of stablecoin purchases); ordinary account
  verification (F03) and the destination declaration (F13) do not by themselves make F01, F07 or F10 conditional.
- F06: if the provider is only an applicant for authorisation and no document says whether banks may keep serving
  applicants, answer unknown. restricted needs a document applying the ban to this provider; supported needs a document
  saying it is authorised or that banks may keep serving it.
- Every non-unknown answer gives evidence: a list of {source_id, passage}, each passage short (5-40 words) and copied
  EXACTLY, character for character, from that document. An answer whose passage is not found verbatim gets no credit.
- Answer every question listed; one answer per field_id."""

SCHEMA = {'type': 'object', 'properties': {'answers': {'type': 'array', 'items': {'type': 'object', 'properties': {
    'field_id': {'type': 'string'}, 'state': {'type': 'string', 'enum': STATES}, 'value': {'type': 'string'},
    'unit': {'type': 'string'}, 'evidence': {'type': 'array', 'items': {'type': 'object', 'properties': {
        'source_id': {'type': 'string'}, 'passage': {'type': 'string'}}, 'required': ['source_id', 'passage']}},
    'note': {'type': 'string'}}, 'required': ['field_id', 'state', 'value', 'evidence']}}}, 'required': ['answers']}


# ---------- case, documents, retrieval ----------
def cases():
    return {c['case_id']: c for c in M.rows(M.CASES)}


def fields_for(c):
    kind = 'fund' if c['profile_id'] == 'FUND-BR' else 'exchange'
    return [f for f in M.rows(M.FIELDS) if f['applies_to'] == kind]


def permitted(c):
    fam = FAMILY_OF_GROUP[c['group_id']]
    src, snap = M.latest()
    return sorted(i for i, s in src.items() if i in snap and (s['family'] == fam or s['split'] in SHARED))


def doc_text(i):
    return (TEXT / f'{i}.txt').read_text(encoding='utf-8').strip()


def corpus_hash(ids):
    return hashlib.sha256(''.join(hashlib.sha256(doc_text(i).encode()).hexdigest() for i in ids).encode()).hexdigest()


def case_text(c, fs):
    lines = [f"Case {c['case_id']}: {c['operation']}.", f"Profile: {c['profile_id']}. Asset: {c['destination_asset']}. "
             f"Network: {c['chain']}. Amount: {c['amount']} {c['amount_unit']}. As-of date: {c['as_of_utc'][:10]}.",
             '', 'Questions (answer each field_id):']
    lines += [f"- {f['field_id']} [{f['kind']}, answer: {f['answer']}{'; ' + f['unit_hint'] if f['unit_hint'] else ''}]: "
              f"{f['question']}" for f in fs]
    return '\n'.join(lines)


def tokens(s):
    return re.findall(r'[\wà-ú\-]+', s.lower())


def chunks(ids):
    out = []
    for i in ids:
        t = doc_text(i)
        for k in range(0, max(len(t) - 200, 1), CHUNK - 200):
            out.append((i, t[k:k + CHUNK]))
    return out


def retrieve(c, fs, ids):
    """Fixed BM25-style keyword retrieval: top TOP_K chunks per field, deduplicated."""
    ch = chunks(ids)
    toks = [Counter(tokens(t)) for _, t in ch]
    n, avg = len(ch), sum(sum(t.values()) for t in toks) / max(len(ch), 1)
    df = Counter(w for t in toks for w in t)
    picked = []
    for f in fs:
        q = set(tokens(FIELD_KW[f['field_id']] + (' ' + c['destination_asset'] + ' ' + c['chain']
                                                  if f['field_id'] in ASSET_FIELDS else '') +
                       (' ' + PROFILE_KW[c['profile_id']] if f['field_id'] in PROFILE_FIELDS else '')))
        def bm25(t):
            L = sum(t.values())
            return sum(math.log(1 + (n - df[w] + .5) / (df[w] + .5)) * t[w] * 2.2 / (t[w] + 1.2 * (.25 + .75 * L / avg))
                       for w in q if w in t)
        for j in sorted(range(n), key=lambda j: -bm25(toks[j]))[:TOP_K]:
            if j not in picked:
                picked.append(j)
    return [ch[j] for j in sorted(picked)]


def chunk_block(ch):
    return '\n\n'.join(f'[{i}] …{t}…' for i, t in ch)


# ---------- model calls ----------
def claude(prompt, cwd, tools, max_turns=None, system=SYSTEM):
    cmd = [CLAUDE, '-p', prompt, '--restricted', '--strict-mcp-config', '--no-session-persistence',
           '--tools', tools, '--model', MODEL, '--output-format', 'json', '--system-prompt', system,
           '--json-schema', json.dumps(SCHEMA)]
    if max_turns:
        cmd += ['--max-turns', str(max_turns)]
    t0 = dt.datetime.now(dt.timezone.utc)
    try:
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=TIMEOUT_S)
        out = json.loads(p.stdout) if p.stdout.strip().startswith('{') else {'is_error': True, 'result': p.stdout[-2000:],
                                                                             'stderr': p.stderr[-2000:]}
    except subprocess.TimeoutExpired:
        out = {'is_error': True, 'result': 'TIMEOUT', 'subtype': 'timeout'}
    out['_wall_s'] = (dt.datetime.now(dt.timezone.utc) - t0).total_seconds()
    return out


def sid(s):
    """The agent sees files named <source_id>.txt and sometimes cites the file name."""
    return re.sub(r'\.txt$', '', (s or '').strip())


def answers_of(out):
    """Model answers -> internal form with aligned source_ids / passages lists."""
    so = out.get('structured_output')
    if not isinstance(so, dict):
        try:
            so = json.loads(re.search(r'\{.*\}', out.get('result', ''), re.S).group(0))
        except (AttributeError, ValueError, TypeError):
            return []
    res = []
    for a in so.get('answers', []) if isinstance(so.get('answers'), list) else []:
        ev = [e for e in a.get('evidence') or [] if isinstance(e, dict)]
        res.append({**{k: v for k, v in a.items() if k != 'evidence'},
                    'source_ids': [sid(e.get('source_id', '')) for e in ev], 'passages': [e.get('passage', '') for e in ev]})
    return res


def verbatim_filter(ans, ids):
    texts = {i: M.norm(doc_text(i)) for i in ids}
    out = []
    for a in ans:
        ok = a.get('source_ids') and len(a['source_ids']) == len(a.get('passages', [])) and all(
            s in texts and M.norm(p) in texts[s] for s, p in zip(a['source_ids'], a['passages']))
        out.append(a if ok or a.get('state') == 'unknown' else {**a, 'state': 'unknown', 'value': '', 'source_ids': [],
                                                                 'passages': [], 'note': 'dropped: passage not verbatim'})
    return out


def method_B0(c, fs, ids):
    sents = [(i, s.strip()) for i in ids for s in re.split(r'(?<=[.!?])\s+', doc_text(i)) if s.strip()]
    ans = []
    for f in fs:
        rule = B0_RULES.get(f['field_id'])
        hit = next(((i, s) for i, s in sents if rule and re.search(rule[0], s, re.I)), None) if rule else None
        if hit and len(hit[1]) <= 400:
            ans.append(dict(field_id=f['field_id'], state=rule[1], value=rule[2], unit='', source_ids=[hit[0]],
                            passages=[hit[1]], note='B0 rule'))
        elif f['field_id'] == 'F08':
            m = next(((i, mm) for i, s in sents for mm in [re.search(r'(taker|ordem (a )?mercado|ativa)[^.]{0,60}?(\d+,\d+|\d+\.\d+)\s?%', s, re.I)] if mm), None)
            ans.append(dict(field_id='F08', state='', value=str(round(float(m[1].group(3).replace(',', '.')) * 100, 2)) if m else '',
                            unit='bps' if m else '', source_ids=[m[0]] if m else [], passages=[m[1].group(0)] if m else [],
                            note='B0 rule') if m else dict(field_id='F08', state='unknown', value='', unit='', source_ids=[], passages=[]))
        else:
            ans.append(dict(field_id=f['field_id'], state='unknown', value='', unit='', source_ids=[], passages=[]))
    return {'answers': ans, 'calls': []}


def method_B1(c, fs, ids, wd):
    ch = retrieve(c, fs, ids)
    out = claude(case_text(c, fs) + '\n\nDocument excerpts (source_id in brackets):\n\n' + chunk_block(ch), wd, '')
    return {'answers': answers_of(out), 'calls': [out], 'chunks': [[i, t[:80]] for i, t in ch]}


def method_B2(c, fs, ids, wd):
    ch = retrieve(c, fs, ids)
    block = chunk_block(ch)
    o1 = claude(case_text(c, fs) + '\n\nDocument excerpts (source_id in brackets):\n\n' + block, wd, '')
    a1 = answers_of(o1)
    o2 = claude(case_text(c, fs) + '\n\nDocument excerpts (source_id in brackets):\n\n' + block +
                '\n\nDraft answers to VERIFY:\n' + json.dumps({'answers': a1}, ensure_ascii=False) +
                '\n\nCheck every draft answer: (1) each passage appears word for word in the excerpt of the cited source; '
                '(2) it supports the state/value for THIS profile, network and as-of date; (3) nothing in the excerpts '
                'contradicts it. Correct wrong answers; set unsupported ones to unknown with empty value. Return the full '
                'corrected list.', wd, '')
    a2 = answers_of(o2) or a1
    return {'answers': verbatim_filter(a2, ids), 'calls': [o1, o2], 'draft': a1, 'chunks': [[i, t[:80]] for i, t in ch]}


def method_A(c, fs, ids, wd):
    prompt = (case_text(c, fs) + '\n\nThe documents are the .txt files in the current directory, one per source_id '
              '(file name = source_id). Investigate with Glob, Grep and Read: search for each question in Portuguese and '
              'English, read the surrounding text, look for conditions, exceptions, dates and conflicting statements, and '
              'search again when something is missing. Before answering, confirm each passage you cite with Grep on the '
              'exact string in that file. Give your final answers in the required JSON.')
    out = claude(prompt, wd, 'Read,Grep,Glob', max_turns=MAX_TURNS)
    return {'answers': answers_of(out), 'calls': [out]}


def sum_usage(calls):
    """Sum every numeric usage component per model across calls (v1.1; v1 kept only the last call per model)."""
    tot = {}
    for o in calls:
        for m, u in (o.get('modelUsage') or {}).items():
            for k, v in u.items():
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    tot.setdefault(m, {})[k] = tot.get(m, {}).get(k, 0) + v
    return tot


def commit():
    try:
        return subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    except OSError:
        return ''


def config_hash():
    """Hash of every setting that shapes a run: prompts, schema, keywords, retrieval and limit constants, method code."""
    import inspect
    parts = [SYSTEM, json.dumps(SCHEMA), json.dumps(FIELD_KW), json.dumps(sorted(ASSET_FIELDS)), json.dumps(sorted(PROFILE_FIELDS)),
             json.dumps(PROFILE_KW), json.dumps({k: list(v) for k, v in B0_RULES.items()}), MODEL,
             str((MAX_TURNS, TIMEOUT_S, TOP_K, CHUNK))] + [inspect.getsource(f) for f in (
             retrieve, chunks, claude, answers_of, verbatim_filter, method_B0, method_B1, method_B2, method_A)]
    return hashlib.sha256('\n'.join(parts).encode()).hexdigest()


def run_one(method, cid, r):
    c = cases()[cid]
    dest = RUNS / method / f'{cid}_r{r}.json'
    if dest.exists():
        return f'{dest.name} exists'
    fs, ids = fields_for(c), permitted(c)
    wd = tempfile.mkdtemp(prefix=f'p328_{method}_{cid}_')
    try:
        for i in ids:
            shutil.copy(TEXT / f'{i}.txt', wd)
        t0 = dt.datetime.now(dt.timezone.utc)
        res = {'B0': lambda: method_B0(c, fs, ids), 'B1': lambda: method_B1(c, fs, ids, wd),
               'B2': lambda: method_B2(c, fs, ids, wd), 'A': lambda: method_A(c, fs, ids, wd)}[method]()
        t1 = dt.datetime.now(dt.timezone.utc)
    finally:
        shutil.rmtree(wd, ignore_errors=True)
    calls = res.pop('calls')
    rec = dict(method=method, case_id=cid, repeat=r, model=MODEL if method != 'B0' else 'none',
               prompt_hash=hashlib.sha256((SYSTEM + json.dumps(SCHEMA) + json.dumps(FIELD_KW) + case_text(c, fs)).encode()).hexdigest(),
               corpus_hash=corpus_hash(ids), permitted=ids, start_utc=t0.isoformat(), end_utc=t1.isoformat(),
               wall_s=(t1 - t0).total_seconds(), n_calls=len(calls),
               turns=sum(int(o.get('num_turns') or 0) for o in calls),
               errors=[o.get('subtype') or o.get('result', '')[:200] for o in calls if o.get('is_error')],
               stop=[o.get('terminal_reason') or o.get('subtype') for o in calls],
               usage=sum_usage(calls), usage_per_call=[o.get('modelUsage') or {} for o in calls],
               code_commit=commit(), config_hash=config_hash(),
               notional_usd=sum(float(o.get('total_cost_usd') or 0) for o in calls),
               raw_results=[o.get('result') for o in calls], **res)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding='utf-8')
    return f"{dest.name}: {len(rec['answers'])} answers, {rec['turns']} turns, {rec['wall_s']:.0f}s, errors {rec['errors'] or 'none'}"


def run(method, which, repeats=1, workers=3):
    cs = cases()
    ids = [k for k, c in cs.items() if c['split'] == which] if which in ('dev', 'heldout') else which.split(',')
    jobs = [(method, cid, r) for cid in ids for r in range(1, (1 if method == 'B0' else repeats) + 1)]
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        for msg in ex.map(lambda j: run_one(*j), jobs):
            print(method, msg, flush=True)


# ---------- scoring (v1.1: review P3-36 R1-R4, R7) ----------
SCHEDULE = {'B0': 1, 'B1': 3, 'B2': 3, 'A': 3}   # locked run manifest: method -> repeats
if os.environ.get('P3_28_SCHEDULE'):  # development pilots only, e.g. 'B0:1,B1:1,B2:1,A:1'
    SCHEDULE = {k: int(v) for k, v in (x.split(':') for x in os.environ['P3_28_SCHEDULE'].split(','))}
TEXT_FIELDS = {'F03', 'F09', 'G02'}              # requirement text: credit needs a human audit of the value
UNIT = [(r'business|úteis|uteis', 'business_day', 1), (r'\bh\b|hora|hour|\d\s*h\b', 'hour', 1), (r'dia|day', 'hour', 24),
        (r'bps|bp\b|basis', 'bps', 1), (r'%|percent', 'bps', 100), (r'usdt', 'USDT', 1), (r'usdc', 'USDC', 1),
        (r'brla', 'BRLA', 1), (r'brl|r\$|reais', 'BRL', 1)]


def num(s):
    m = re.search(r'-?\d+(?:[.,]\d+)?', re.sub(r'(?<=\d)\.(?=\d{3}\b)', '', s or ''))  # 75.000 -> 75000
    return float(m.group(0).replace(',', '.')) if m else None


def qty(value, unit):
    """(number, canonical unit) from value + unit text; unit None when not stated."""
    x, t = num(value), f'{unit or ""} {value or ""}'.lower()
    for pat, u, k in UNIT:
        if re.search(pat, t):
            return (x * k if x is not None else None), u
    return x, None


def category(s):
    s = (s or '').lower()
    if re.search(r'case|caso|personaliz|individual|custom', s):
        return 'case_by_case'
    if re.search(r'level|nível|nivel|tier', s):
        return 'by_level'
    return 'fixed' if re.search(r'\d', s) else ('' if not s.strip() else 'other')


def correct(f, ref, a):
    """Mechanical field match. state fields: same state. Numeric fields F04, F08, F12: same quantity after unit
    normalisation (hours/days -> hours, business days kept apart, % -> bps, asset units must agree); a stated unit on
    both sides must match. Limit basis F05, F14: same category (fixed also needs the same quantity). F02: state and
    yes/no. F13: state, plus the date when the reference gives one. F03, F09, G02 (requirement text): state (G02: both
    null or both non-null) here, and the value must also pass the human audit before it earns final credit."""
    fid, rs, rv = f['field_id'], ref['state'].strip().lower(), ref['value'].strip()
    ms, mv = (a.get('state') or '').strip().lower(), (a.get('value') or '').strip()
    if fid in ('F04', 'F08', 'F12'):
        (x, ux), (y, uy) = qty(rv, ref.get('unit')), qty(mv, a.get('unit'))
        return x is not None and y is not None and (ux == uy or None in (ux, uy) and fid == 'F08') and \
            abs(x - y) <= 0.01 * max(abs(x), 1e-9)
    if fid in ('F05', 'F14'):
        cr = category(rv)
        return cr == category(mv) and (cr != 'fixed' or qty(rv, ref.get('unit'))[0] == qty(mv, a.get('unit'))[0])
    if fid == 'G02':
        return bool(rv) == bool(mv)
    if rs != ms:
        return False
    if fid == 'F02' and rv:
        return rv.lower()[:2] == mv.lower()[:2]
    if fid == 'F13' and re.search(r'\d{4}-\d{2}-\d{2}', rv):
        return rv[:10] in mv
    return True


def answerable(f, ref):
    if f['answer'] == 'value':
        return bool(ref['value'].strip()) and ref['state'].strip().lower() not in ('unknown', 'not_applicable')
    return ref['state'].strip().lower() not in ('unknown', 'not_applicable', '')


def evidence_ok(a, ids, texts):
    """Every {source_id, passage} pair: permitted source, passage of >= 12 characters found verbatim (normalised).
    Length, not words: table rows such as 'Ethereum 0xA0b8...' are valid evidence. Relevance is for the human audit."""
    s, p = [sid(i) for i in a.get('source_ids') or []], a.get('passages') or []
    return bool(s) and len(s) == len(p) and all(
        i in ids and len(M.norm(x)) >= 12 and M.norm(x) in texts[i] for i, x in zip(s, p))


def audit_key(c, f, a):
    return hashlib.sha256(json.dumps([c, f, (a.get('state') or '').lower(), (a.get('value') or '').strip().lower(),
                                      [sid(x) for x in a.get('source_ids') or []], a.get('passages') or []],
                                     ensure_ascii=False).encode()).hexdigest()[:16]


def score(ref_path, which, tag='', audit_path=None):
    """SAC per case = answerable reference fields with final credit / answerable reference fields. Final credit =
    mechanical match AND valid evidence AND (when an audit file is given) the auditor's `supports = yes` (and, for
    F03/F09/G02, `value_ok = yes`). Without an audit file the result is labelled PROVISIONAL. Cases with no answerable
    field are excluded from SAC (counted). Macro: mean over a case's scheduled repeats, then over cases.
    Locked manifest: every case x SCHEDULE run must exist; a missing or failed run (errors, timeout) earns zero and its
    answers are still checked by the guardrail. Duplicate answers to one field earn zero; a bad positive among them
    counts. Guardrail: availability answers 'supported' where the reference is not 'supported', the evidence is invalid,
    or the auditor marks supports = no; plus notes the auditor flags. Corpus hashes of every run must match the current
    text extracts, else scoring stops."""
    cs = {k: c for k, c in cases().items() if c['split'] == which}
    ref = {(r['case_id'], r['field_id']): r for r in M.rows(ref_path)}
    need = [(cid, f['field_id']) for cid, c in cs.items() for f in fields_for(c)]
    gaps = [k for k in need if k not in ref or not (ref[k]['state'].strip() or ref[k]['value'].strip())]
    if gaps:
        sys.exit(f'reference incomplete: {len(gaps)} of {len(need)} rows missing or blank, e.g. {gaps[:3]}')
    texts = {i: M.norm(doc_text(i)) for i in M.latest()[1]}
    aud = {r['key']: r for r in M.rows(audit_path)} if audit_path else {}
    scores, errs, costs, to_audit, missing = [], [], [], {}, []
    for cid, c in cs.items():
        fs = fields_for(c)
        for method, reps in SCHEDULE.items():
            for r in range(1, reps + 1):
                p = RUNS / method / f'{cid}_r{r}.json'
                run_ = json.loads(p.read_text(encoding='utf-8')) if p.exists() else None
                if run_ is None:
                    missing.append(f'{method}/{cid}_r{r}')
                elif run_['corpus_hash'] != corpus_hash(run_['permitted']):
                    sys.exit(f'corpus mismatch for {p.name} ({method}): the run saw other document versions')
                failed = run_ is None or bool(run_.get('errors'))
                byf = {}
                for a in (run_ or {}).get('answers', []):
                    byf.setdefault(a.get('field_id'), []).append(a)
                n_ans = n_ok = guard = unk_ref = unk_ok = unk_ans = 0
                for f in fs:
                    rf, al = ref[(cid, f['field_id'])], byf.get(f['field_id'], [])
                    a = al[0] if len(al) == 1 else {}
                    ev = evidence_ok(a, (run_ or {}).get('permitted', []), texts)
                    is_unk = (a.get('state') or 'unknown').lower() == 'unknown' and not (a.get('value') or '').strip()
                    mech = answerable(f, rf) and correct(f, rf, a) and ev and not failed
                    k = audit_key(cid, f['field_id'], a) if a else ''
                    ad = aud.get(k, {})
                    fin = mech and (not aud or (ad.get('supports', '').lower() == 'yes' and (
                        f['field_id'] not in TEXT_FIELDS or ad.get('value_ok', '').lower() == 'yes')))
                    bad_pos = any(f['kind'] == 'availability' and (x.get('state') or '').lower() == 'supported' and (
                        rf['state'].strip().lower() != 'supported' or not evidence_ok(x, run_['permitted'], texts) or
                        aud.get(audit_key(cid, f['field_id'], x), {}).get('supports', '').lower() == 'no') for x in al)
                    bad_pos += bool(ad.get('note_claim', '').lower() == 'yes')
                    if a and (mech or (f['kind'] == 'availability' and (a.get('state') or '').lower() == 'supported')
                              or (a.get('note') or '').strip()):
                        to_audit[k] = dict(key=k, case_id=cid, field_id=f['field_id'], question=f['question'],
                                           profile=c['profile_id'], asset=c['destination_asset'], network=c['chain'],
                                           as_of=c['as_of_utc'][:10], state=a.get('state', ''), value=a.get('value', ''),
                                           evidence=' || '.join(f'[{sid(x)}] {y}' for x, y in zip(a.get('source_ids') or [], a.get('passages') or [])),
                                           note=a.get('note', ''), supports='', value_ok='', note_claim='', auditor_comment='')
                    unk_ans += is_unk
                    if answerable(f, rf):
                        n_ans += 1
                        n_ok += fin
                    else:
                        unk_ref += 1
                        unk_ok += is_unk and not failed
                    guard += bool(bad_pos)
                    errs.append(dict(method=method, case_id=cid, repeat=r, field_id=f['field_id'], ref_state=rf['state'],
                                     ref_value=rf['value'], state=a.get('state', ''), value=a.get('value', ''),
                                     n_answers=len(al), evidence_valid=ev, mechanical=mech, final=fin, failed_run=failed,
                                     outcome='correct' if fin else 'correct_unknown' if (not answerable(f, rf) and is_unk)
                                     else 'unsupported_positive' if bad_pos else 'duplicate' if len(al) > 1
                                     else 'failed_run' if failed else 'false_unknown' if is_unk
                                     else 'invalid_evidence' if not ev else 'not_confirmed_by_audit' if mech else 'wrong_answer'))
                scores.append(dict(method=method, case_id=cid, family=c['group_id'], repeat=r, answerable=n_ans,
                                   credited=n_ok, sac=n_ok / n_ans if n_ans else '', unsupported_positive=guard,
                                   ref_unknown=unk_ref, unknown_kept=unk_ok, all_unknown_rate=unk_ans / len(fs),
                                   failed_run=failed, missing_run=run_ is None))
                if run_:
                    u = run_['usage']
                    costs.append(dict(method=method, case_id=cid, repeat=r, model=run_['model'], calls=run_['n_calls'],
                                      turns=run_['turns'], wall_s=round(run_['wall_s'], 1),
                                      output_tokens=sum(v.get('outputTokens', 0) for v in u.values()),
                                      uncached_input=sum(v.get('inputTokens', 0) for v in u.values()),
                                      cache_read=sum(v.get('cacheReadInputTokens', 0) for v in u.values()),
                                      cache_creation=sum(v.get('cacheCreationInputTokens', 0) for v in u.values()),
                                      usage_complete='usage_per_call' in run_ or run_['n_calls'] <= 1,
                                      notional_usd=round(run_['notional_usd'], 4), errors=';'.join(map(str, run_['errors']))))
    for name, data in (('case_scores', scores), ('errors', errs), ('costs', costs)):
        if data:
            with open(ROOT / f'results/tables/P3-28_{name}{tag}.csv', 'w', newline='', encoding='utf-8') as fh:
                w = csv.DictWriter(fh, list(data[0]))
                w.writeheader()
                w.writerows(data)
    if not aud and to_audit:  # blinded audit sheet: no method, run or reference columns; one row per distinct answer
        rows_ = sorted(to_audit.values(), key=lambda x: x['key'])
        with open(RAW / f'reference/audit_sheet{tag}.csv', 'w', newline='', encoding='utf-8') as fh:
            w = csv.DictWriter(fh, list(rows_[0]))
            w.writeheader()
            w.writerows(rows_)
    label = 'FINAL (audited)' if aud else 'PROVISIONAL (mechanical; semantic audit pending)'
    print(f'{which} {label}; missing runs {len(missing)}{" " + str(missing[:4]) if missing else ""}; '
          f'audit sheet rows {len(to_audit)}')
    print('method | cases in SAC (excluded: no answerable field) | SAC | unsupported positives | unknown kept | all-unknown | failed')
    for m in SCHEDULE:
        rs_ = [x for x in scores if x['method'] == m]
        per = {}
        for x in rs_:
            if x['sac'] != '':
                per.setdefault(x['case_id'], []).append(x['sac'])
        excl = len({x['case_id'] for x in rs_}) - len(per)
        sac = sum(sum(v) / SCHEDULE[m] for v in per.values()) / len(per) if per else float('nan')  # missing runs = 0
        print(f"{m} | {len(per)} ({excl}) | {sac:.3f} | {sum(x['unsupported_positive'] for x in rs_)} | "
              f"{sum(x['unknown_kept'] for x in rs_)}/{sum(x['ref_unknown'] for x in rs_)} | "
              f"{sum(x['all_unknown_rate'] for x in rs_) / max(len(rs_), 1):.2f} | {sum(x['failed_run'] for x in rs_)}")


def selftest():
    """The review's synthetic failures (P3-36 C02-C13) must now be rejected; controls must pass."""
    F = lambda fid, kind='term', ans='value': dict(field_id=fid, kind=kind, answer=ans)
    R = lambda st='', v='', u='': dict(state=st, value=v, unit=u)
    assert not correct(F('F04'), R(v='72', u='hours'), dict(value='72', unit='days'))          # C02 units
    assert correct(F('F04'), R(v='72', u='hours'), dict(value='3', unit='days'))               # 3 days = 72 h
    assert not correct(F('F04'), R(v='72', u='hours'), dict(value='3', unit='business days'))  # business days apart
    assert correct(F('F08'), R(v='50', u='bps'), dict(value='0.50%', unit=''))                 # % -> bps
    assert 'F03' in TEXT_FIELDS and 'G02' in TEXT_FIELDS                                      # C03/C04: audit needed
    texts = {'X': M.norm('Depósito via Pix 24/7, todos os dias Grátis')}
    assert not evidence_ok(dict(source_ids=['X'], passages=['']), ['X'], texts)               # C05 empty quote
    assert not evidence_ok(dict(source_ids=['X'], passages=['Grátis']), ['X'], texts)         # under 12 characters
    assert evidence_ok(dict(source_ids=['X.txt'], passages=['via Pix 24/7,']), ['X'], texts)  # control
    assert not evidence_ok(dict(source_ids=['X'], passages=['via Pix 24/7,']), ['Y'], texts)  # not permitted
    u = sum_usage([{'modelUsage': {'m': {'inputTokens': 10}}}, {'modelUsage': {'m': {'inputTokens': 20}}}])
    assert u['m']['inputTokens'] == 30                                                         # C14 usage summed
    print('methods selftest ok')


if __name__ == '__main__':
    a = sys.argv[1:]
    opt = {k: int(a[a.index(k) + 1]) for k in ('--repeats', '--workers') if k in a}
    if a[0] == 'run':
        run(a[1], a[2], opt.get('--repeats', 1), opt.get('--workers', 3))
    elif a[0] == 'selftest':
        selftest()
    elif a[0] == 'score':
        score(a[1], a[2], a[a.index('--tag') + 1] if '--tag' in a else '', a[a.index('--audit') + 1] if '--audit' in a else None)
