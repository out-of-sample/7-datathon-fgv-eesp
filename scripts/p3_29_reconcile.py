r"""P3-29: reconcile BRLA supply with on-chain records, Celo only. Spec: tasks/P3-29-on-chain-reconciliation.md.

smoke   S1 feasibility (F-041): chain ID, historical headers, code, EIP-1967 slots and state at 19 Jun and 1 Jul 2026
        00:00 UTC, log range limits, one receipt, Blockscout metadata, on several public providers; next to DefiLlama.
ledger  S3 under results/P3-29_protocol.md (committed before collection): totalSupply at the 14 daily boundaries
        19 Jun - 2 Jul 00:00 UTC (Forno + Ankr); every log of the proxy in between (Forno, 5,000-block chunks); decoded
        mints (Transfer from 0x0) and burns (Transfer to 0x0); stock residual per UTC day and for the development
        interval 19 Jun -> 1 Jul (tolerance 0 base units); DefiLlama v1 (Flash, 4 Nov) and v2 (fresh) against the
        on-chain path of each UTC day (+-1 BRLA); receipts for every event >= 1% of gross volume and 30 seeded others.
Contract  BRLA on Celo 0xfecb3f7c54e2caae9dc6ac9060a822d47e053760 (proxy; implementation BRLAV1_1 0xe6a5...ddfb)
Units     integer base units; BRLA = base / 10**18 (decimals read on-chain), exact Decimal, presentation only. UTC.
          Block "at" T = last block with timestamp <= T; a day's events are in (b_d, b_d+1].
Providers forno = https://forno.celo.org; ankr = https://rpc.ankr.com/celo; blockscout = https://celo.blockscout.com
          (eth-rpc + REST v2); probes 1rpc, stakely, drpc; DefiLlama https://stablecoins.llama.fi/stablecoin/365.
          Event and function hashes come from web3_sha3 on Forno and Ankr (no local Keccak installed).
Inputs    the endpoints above; data/raw/flash-mentor-leads/brla/raw_defillama_brla_supply.json (restore: data/README.md)
Outputs   data/raw/p3_29/<provider>/*.json  request, URL, retrieval UTC, HTTP status, response (immutable; checksums
          appended to data/raw/SHA256SUMS); failed calls under failed/ (replayed offline, retried live).
          smoke:  data/processed/P3-29_s1_snapshots.csv, results/tables/P3-29_s1_coverage.csv
          ledger: data/processed/P3-29_{snapshots,events,reconciliation}.csv, results/tables/P3-29_coverage.csv,
                  results/tables/P3-29_case_audit.md
Run       .venv/bin/python scripts/p3_29_reconcile.py {smoke,ledger}
          P3_29_OFFLINE=1 .venv/bin/python scripts/p3_29_reconcile.py {smoke,ledger}   (frozen answers only)
"""
import csv
import datetime as dt
import hashlib
import json
import os
import random
import statistics
import sys
import time
import urllib.error
import urllib.request
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data/raw/p3_29'
SUMS = ROOT / 'data/raw/SHA256SUMS'
DEFILLAMA = ROOT / 'data/raw/flash-mentor-leads/brla/raw_defillama_brla_supply.json'
OFFLINE = os.environ.get('P3_29_OFFLINE') == '1'

RPC = {'forno': 'https://forno.celo.org', 'blockscout': 'https://celo.blockscout.com/api/eth-rpc',
       'ankr': 'https://rpc.ankr.com/celo'}
PROBE = {'1rpc': 'https://1rpc.io/celo', 'stakely': 'https://celo-json-rpc.stakely.io', 'drpc': 'https://celo.drpc.org'}
# S4 (other listed BRLA contracts): two archive providers per chain found by probing on 7 Nov (F-041 style)
CHAINS = {'polygon': {'id': 137, 'token': '0xe6a537a407488807f0bbeb0038b79004f19dddfb', 'llama': 'Polygon',
                      'rpcs': {'polygon_drpc': 'https://polygon.drpc.org',
                               'polygon_tenderly': 'https://polygon.gateway.tenderly.co'}},
          'gnosis': {'id': 100, 'token': '0xfecb3f7c54e2caae9dc6ac9060a822d47e053760', 'llama': 'Gnosis',
                     'rpcs': {'gnosis_official': 'https://rpc.gnosischain.com',
                              'gnosis_gatewayfm': 'https://rpc.gnosis.gateway.fm'}},
          'moonbeam': {'id': 1284, 'token': '0xfeb25f3fddad13f82c4d6dbc1481516f62236429', 'llama': 'Moonbeam',
                       'rpcs': {'moonbeam_drpc': 'https://moonbeam.drpc.org',
                                'moonbeam_onfinality': 'https://moonbeam.api.onfinality.io/public'}}}
URLS = {**RPC, **PROBE, **{p: u for c in CHAINS.values() for p, u in c['rpcs'].items()}}
SPACING = {'blockscout': 2.0, **{p: 0.2 for c in CHAINS.values() for p in c['rpcs']}}  # seconds between live calls
last_call = {}
REST = 'https://celo.blockscout.com/api/v2'
CHAIN_ID = 42220
BRLA = '0xfecb3f7c54e2caae9dc6ac9060a822d47e053760'
ZERO = '0x' + '0' * 40
IMPL_SLOT = '0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc'   # EIP-1967 implementation
ADMIN_SLOT = '0xb53127684a568b3173ae13b9f8a6016e243e63b6e8ee1178d6a717850b5d6103'  # EIP-1967 admin
TRANSFER = '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
UPGRADED = '0xbc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b'
SEL = {'totalSupply': '0x18160ddd', 'decimals': '0x313ce567'}
SNAPS = {'open': '2026-06-19T00:00:00+00:00', 'close': '2026-07-01T00:00:00+00:00'}
LOG_SPANS = [1_000, 10_000, 100_000]  # blocks after b0 (Celo L2: ~1 s per block)

coverage = []


def note(capability, provider, ok, detail=''):
    coverage.append({'capability': capability, 'provider': provider, 'status': 'ok' if ok else 'fail',
                     'detail': str(detail)[:300]})


def freeze(f, url, body, status, resp):
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps({'url': url, 'request': body, 'retrieved_utc': dt.datetime.now(dt.UTC).isoformat(),
                             'http_status': status, 'response': resp}, indent=1))
    with open(SUMS, 'a') as s:
        s.write(f'{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.relative_to(ROOT)}\n')


def frozen(provider, url, body=None):
    """Name and path of the frozen answer for one request (the cache key)."""
    key = hashlib.sha256((url + json.dumps(body, sort_keys=True)).encode()).hexdigest()[:20]
    name = f"{body['method'] if body else 'GET'}_{key}"
    return name, RAW / provider / f'{name}.json'


def rpc_body(method, *params):
    return {'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': list(params)}


def fetch(provider, url, body=None):
    """JSON-RPC POST (body) or REST GET (body None). HTTP-200 answers are frozen and reused; failed calls are frozen
    under failed/ as evidence (replayed offline, never reused live, so a live re-run retries them)."""
    name, f = frozen(provider, url, body)
    if f.exists():
        return json.loads(f.read_text())['response']
    if OFFLINE:
        failed = sorted((RAW / provider / 'failed').glob(f'{name}_*.json'))
        if failed:
            return json.loads(failed[-1].read_text())['response']
        sys.exit(f'offline: no frozen response for {provider} {url} {body}')
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body else None, headers={
        'Content-Type': 'application/json', 'User-Agent': 'p3-29-reconcile/1 (read-only research script)'})
    for attempt in range(4):
        time.sleep(max(0, SPACING.get(provider, 0) - (time.time() - last_call.get(provider, 0))))
        last_call[provider] = time.time()
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                status, text = r.status, r.read().decode()
            break
        except urllib.error.HTTPError as e:
            status, text = e.code, e.read().decode(errors='replace')
            if status not in (408, 429, 502, 503, 504):
                break
        except Exception as e:  # transport failure: not frozen, a re-run retries
            status, text = None, repr(e)
        time.sleep(5 * 2 ** attempt)
    try:
        resp = json.loads(text) if status == 200 else None
    except ValueError:
        resp = None
    if resp is None:
        resp = {'error': {'http': status, 'body': text[:300]}}
        freeze(RAW / provider / 'failed' / f"{name}_{dt.datetime.now(dt.UTC):%Y%m%dT%H%M%S}.json", url, body, status, resp)
        return resp
    freeze(f, url, body, status, resp)
    return resp


def rpc(provider, method, *params, url=None):
    r = fetch(provider, url or URLS[provider], rpc_body(method, *params))
    return r.get('result'), r.get('error')


def must(provider, method, *params):
    res, err = rpc(provider, method, *params)
    if err or res is None:
        raise RuntimeError(f'{provider} {method} {params}: {err or "null result"}')
    return res


def header(n, provider='forno'):
    return must(provider, 'eth_getBlockByNumber', hex(n), False)


def block_at(t, head, guess=None):
    """Last block with timestamp <= t: the guess if its header and the next one bracket t, else binary search."""
    if guess and int(header(guess)['timestamp'], 16) <= t < int(header(guess + 1)['timestamp'], 16):
        return guess
    lo, hi = 1, head
    assert int(header(lo)['timestamp'], 16) <= t < int(header(hi)['timestamp'], 16)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        lo, hi = (mid, hi) if int(header(mid)['timestamp'], 16) <= t else (lo, mid)
    return lo


def block_at_search(p, t, lo, hi):
    """Last block <= t on provider p within [lo, hi] (ts(lo) <= t < ts(hi)): interpolation, bisection when it stalls."""
    ts = lambda n: int(header(n, p)['timestamp'], 16)
    tlo, thi, step = ts(lo), ts(hi), 0
    assert tlo <= t < thi, (p, t, lo, hi)
    while hi - lo > 1:
        step += 1
        g = (lo + hi) // 2 if step % 3 == 0 else lo + int((t - tlo) * (hi - lo) / max(thi - tlo, 1))
        g = min(max(g, lo + 1), hi - 1)
        tg = ts(g)
        lo, tlo, hi, thi = (g, tg, hi, thi) if tg <= t else (lo, tlo, g, tg)
    return lo


def word_addr(hexword):
    return '0x' + hexword[-40:].lower()


def sha(hexcode):
    return hashlib.sha256(bytes.fromhex(hexcode[2:])).hexdigest()


def state(provider, b):
    """Proxy code, EIP-1967 slots, implementation code, totalSupply and decimals at block b."""
    tag = hex(b)
    impl = word_addr(must(provider, 'eth_getStorageAt', BRLA, IMPL_SLOT, tag))
    return {'proxy_code_sha256': sha(must(provider, 'eth_getCode', BRLA, tag)),
            'implementation': impl,
            'admin': word_addr(must(provider, 'eth_getStorageAt', BRLA, ADMIN_SLOT, tag)),
            'impl_code_sha256': sha(must(provider, 'eth_getCode', impl, tag)),
            'total_supply_base': int(must(provider, 'eth_call', {'to': BRLA, 'data': SEL['totalSupply']}, tag), 16),
            'decimals': int(must(provider, 'eth_call', {'to': BRLA, 'data': SEL['decimals']}, tag), 16)}


def defillama_celo(d=None):
    d = d or json.loads(DEFILLAMA.read_text())
    return {dt.datetime.fromtimestamp(r['date'], dt.UTC).date().isoformat(): r['circulating']['peggedREAL']
            for r in d['chainBalances']['Celo']['tokens']}


def smoke():
    # 1. chain identity
    for p in RPC:
        res, err = rpc(p, 'eth_chainId')
        note('chain_id', p, res and int(res, 16) == CHAIN_ID, res or err)
    head = int(must('forno', 'eth_blockNumber'), 16)
    fin = rpc('forno', 'eth_getBlockByNumber', 'finalized', False)[0]

    # 2. snapshot blocks, header agreement across providers
    blocks = {}
    for lab, iso in SNAPS.items():
        b = block_at(int(dt.datetime.fromisoformat(iso).timestamp()), head)
        h = header(b)
        other, err = rpc('blockscout', 'eth_getBlockByNumber', hex(b), False)
        note(f'header_{lab}', 'blockscout', other and other['hash'] == h['hash'], other['hash'] if other else err)
        blocks[lab] = {'block': b, 'hash': h['hash'],
                       'time_utc': dt.datetime.fromtimestamp(int(h['timestamp'], 16), dt.UTC).isoformat(),
                       'next_time_utc': dt.datetime.fromtimestamp(int(header(b + 1)['timestamp'], 16), dt.UTC).isoformat()}
    note('finalized_tag', 'forno', fin and int(fin['number'], 16) > blocks['close']['block'],
         f"finalized {int(fin['number'], 16) if fin else None} > close {blocks['close']['block']}")

    # 3. historical state on both providers
    rows, dl = [], defillama_celo()
    for lab, bk in blocks.items():
        for p in RPC:
            try:
                s = state(p, bk['block'])
                note(f'historical_state_{lab}', p, True, f"totalSupply {s['total_supply_base']}")
            except RuntimeError as e:
                note(f'historical_state_{lab}', p, False, e)
                continue
            brla = Decimal(s['total_supply_base']) / Decimal(10) ** s['decimals']
            llama = dl.get(SNAPS[lab][:10])
            rows.append({'contract_key': f'celo:{BRLA}', 'label': lab, 'target_utc': SNAPS[lab], **bk, 'provider': p,
                         **s, 'total_supply_brla': f'{brla:f}', 'defillama_date_label': SNAPS[lab][:10],
                         'defillama_circulating': llama,
                         'diff_defillama_minus_onchain_brla': None if llama is None else f'{Decimal(str(llama)) - brla:f}',
                         'alignment_status': 'time_alignment_unknown'})
    for p, url in PROBE.items():
        res, err = rpc(p, 'eth_call', {'to': BRLA, 'data': SEL['totalSupply']}, hex(blocks['open']['block']), url=url)
        note('historical_state_open', p, res is not None, f'totalSupply {int(res, 16)}' if res else err)

    # 4. logs: range limits from b0, cross-provider equality on the smallest span, Upgraded events in (b0, b1]
    b0, b1 = blocks['open']['block'], blocks['close']['block']
    logs = {}
    for p in RPC:
        for span in LOG_SPANS:
            res, err = rpc(p, 'eth_getLogs', {'address': BRLA, 'topics': [TRANSFER],
                                              'fromBlock': hex(b0 + 1), 'toBlock': hex(b0 + span)})
            note(f'logs_transfer_{span}_blocks', p, res is not None, f'{len(res)} logs' if res is not None else err)
            if res is not None:
                logs[(p, span)] = res
        res, err = rpc(p, 'eth_getLogs', {'address': BRLA, 'topics': [UPGRADED],
                                          'fromBlock': hex(b0 + 1), 'toBlock': hex(b1)})
        note('logs_upgraded_open_to_close', p, res is not None, f'{len(res)} Upgraded events' if res is not None else err)
    ids = {p: {(l['blockHash'], l['transactionHash'], l['logIndex']) for l in logs.get((p, LOG_SPANS[0]), [])}
           for p in RPC}
    for p in [q for q in RPC if q != 'forno']:
        note('logs_equal_to_forno', p, (p, LOG_SPANS[0]) in logs and ids[p] == ids['forno'],
             f"{len(ids[p])} vs {len(ids['forno'])} logs in ({b0}, {b0 + LOG_SPANS[0]}]")
    sample = logs.get(('forno', LOG_SPANS[0])) or logs.get(('forno', LOG_SPANS[1])) or []
    zero_moves = sum(1 for l in sample if ZERO[2:] in (l['topics'][1][-40:], l['topics'][2][-40:]))
    note('logs_zero_address_transfers_in_sample', 'forno', True, f'{zero_moves} of {len(sample)} (not classified)')

    # 5. one receipt: by hash on every provider (+ dRPC), by block on Forno (no tx-hash index needed)
    if sample:
        tx, bn = sample[0]['transactionHash'], sample[0]['blockNumber']
        rec = {p: rpc(p, 'eth_getTransactionReceipt', tx) for p in RPC}
        rec['drpc'] = rpc('drpc', 'eth_getTransactionReceipt', tx, url=PROBE['drpc'])
        known = rpc('forno', 'eth_getTransactionByHash', tx)[0] is not None
        for p, (res, err) in rec.items():
            note('receipt_by_hash', p, res is not None,
                 f"status {res['status']}, {len(res['logs'])} logs" if res else
                 err or f'null result (transaction known to forno: {known}); not a failure label (T-07)')
        blk = rpc('forno', 'eth_getBlockReceipts', bn)[0] or []
        mine = next((r for r in blk if r['transactionHash'] == tx), None)
        ref = next((res for res, _ in rec.values() if res), None)
        note('receipt_by_block', 'forno', mine is not None and ref is not None and mine['blockHash'] == ref['blockHash']
             and mine['status'] == ref['status'] and mine['logs'] == ref['logs'],
             f"{tx} in block {int(bn, 16)}: matches the by-hash receipt (status, block hash, logs)")

    # 6. contract metadata (Blockscout REST): creation, implementations, verified source
    addr = fetch('blockscout', f'{REST}/addresses/{BRLA}')
    note('rest_address', 'blockscout', 'error' not in addr,
         {k: addr.get(k) for k in ('creation_transaction_hash', 'is_verified', 'proxy_type', 'implementations')})
    impl = rows[0]['implementation'] if rows else None
    if impl:
        sc = fetch('blockscout', f'{REST}/smart-contracts/{impl}')
        note('rest_impl_source', 'blockscout', sc.get('is_verified') is True,
             {k: sc.get(k) for k in ('name', 'compiler_version', 'is_verified', 'verified_at')})
    ctx = addr.get('creation_transaction_hash') if isinstance(addr, dict) else None
    if ctx:
        r = rpc('forno', 'eth_getTransactionReceipt', ctx)[0]
        if r:
            t = dt.datetime.fromtimestamp(int(header(int(r['blockNumber'], 16))['timestamp'], 16), dt.UTC)
            note('deployment', 'forno', r['contractAddress'] == BRLA, f"block {int(r['blockNumber'], 16)} at {t.isoformat()}")
    tok = fetch('blockscout', f'{REST}/tokens/{BRLA}')
    note('rest_token', 'blockscout', 'error' not in tok, {k: tok.get(k) for k in ('name', 'symbol', 'decimals', 'type')})

    # outputs
    write_csv(ROOT / 'data/processed/P3-29_s1_snapshots.csv', rows)
    write_csv(ROOT / 'results/tables/P3-29_s1_coverage.csv', coverage)
    for c in coverage:
        print(f"{c['status']:4} {c['capability']:40} {c['provider']:18} {c['detail']}")
    for r in rows:
        print(r['label'], r['provider'], r['block'], r['time_utc'], r['total_supply_brla'], 'DefiLlama',
              r['defillama_circulating'], 'diff', r['diff_defillama_minus_onchain_brla'])


def write_csv(path, data):
    fields = list(dict.fromkeys(k for row in data for k in row))
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(data)


# ---------------------------------------------------------------- S4: other listed contracts (protocol amendment 10)
def chains():
    v1 = json.loads(DEFILLAMA.read_text())['chainBalances']
    day = lambda k: DAY0 + dt.timedelta(days=k)
    celo = {r['label']: int(r['total_supply_base']) for r in csv.DictReader(open(ROOT / 'data/processed/P3-29_snapshots.csv'))
            if r['provider'] == 'forno'}
    rows, cap, pred = [], [], []
    for name, c in CHAINS.items():
        (pa, pb), tok = c['rpcs'], c['token']
        llama = {dt.datetime.fromtimestamp(r['date'], dt.UTC).date().isoformat(): r['circulating']['peggedREAL']
                 for r in v1[c['llama']]['tokens']}
        for p in (pa, pb):
            res, err = rpc(p, 'eth_chainId')
            cap.append({'chain': name, 'provider': p, 'capability': 'chain_id', 'ok': bool(res) and int(res, 16) == c['id'],
                        'detail': res or err})
        head = int(must(pa, 'eth_blockNumber'), 16)
        supply = lambda p, b: (lambda r: int(r[0], 16) if r[0] else None)(rpc(p, 'eth_call', {'to': tok, 'data': SEL['totalSupply']}, hex(b)))
        lo, bounds = 1, []
        for k in range(N_BOUND):
            b = block_at_search(pa, int(day(k).timestamp()), lo, head)
            lo = b
            sa, sb = supply(pa, b), supply(pb, b)
            meta = {}
            for p in (pb, pa):  # code and implementation slot from whichever provider serves them
                code, e1 = rpc(p, 'eth_getCode', tok, hex(b))
                impl, e2 = rpc(p, 'eth_getStorageAt', tok, IMPL_SLOT, hex(b))
                if code and impl:
                    meta = {'code_sha256': sha(code), 'implementation': word_addr(impl), 'meta_provider': p}
                    break
            dec = rpc(pa, 'eth_call', {'to': tok, 'data': SEL['decimals']}, hex(b))[0]
            rep_v = llama.get(day(k).date().isoformat())
            bounds.append({'chain': name, 'label': day(k).date().isoformat(), 'block': b,
                           'time_utc': dt.datetime.fromtimestamp(int(header(b, pa)['timestamp'], 16), dt.UTC).isoformat(),
                           'supply_base': sa, 'supply_brla': brla(sa), 'second_provider_equal': sa is not None and sa == sb,
                           'decimals': int(dec, 16) if dec else None, **meta, 'defillama_v1': rep_v,
                           'r_at_0000_brla': '' if rep_v is None or sa is None else f'{Decimal(str(rep_v)) - Decimal(sa) / UNIT:f}'})
        for k in range(N_BOUND - 1):
            bounds[k]['delta_next_day_brla'] = brla(bounds[k + 1]['supply_base'] - bounds[k]['supply_base'])
        rows += bounds
        cap.append({'chain': name, 'provider': f'{pa}+{pb}', 'capability': 'historical_supply_all_boundaries',
                    'ok': all(r['supply_base'] is not None for r in bounds),
                    'detail': f"second provider equal at {sum(r['second_provider_equal'] for r in bounds)} of {N_BOUND}"})
        cap.append({'chain': name, 'provider': bounds[0].get('meta_provider'), 'capability': 'code_and_implementation',
                    'ok': bool(bounds[0].get('code_sha256')),
                    'detail': f"implementations {sorted({r.get('implementation') for r in bounds})}, "
                              f"code hashes {len({r.get('code_sha256') for r in bounds})}, decimals {sorted({r['decimals'] for r in bounds}, key=str)}"})
        # prediction P-0045: equal 00:44/00:48 endpoint supplies -> DefiLlama equals supply within 1 BRLA.
        # Legacy flat_window column tests endpoints only; no claim about intervening mint/burn events.
        for k in range(DEV_END + 1):
            t44 = int((day(k) + dt.timedelta(minutes=44)).timestamp())
            b44 = block_at_search(pa, t44, bounds[k]['block'], head)
            b48 = block_at_search(pa, t44 + 240, b44, head)
            s44, s48, rep_v = supply(pa, b44), supply(pa, b48), llama.get(day(k).date().isoformat())
            flat = s44 is not None and s44 == s48
            verdict = 'not_tested' if not flat or rep_v is None else (
                'match' if abs(int(Decimal(str(rep_v)) * UNIT) - s44) <= UNIT else 'miss')
            pred.append({'chain': name, 'label': day(k).date().isoformat(), 'block_0044': b44, 'block_0048': b48,
                         'supply_0044_brla': brla(s44), 'supply_0048_brla': brla(s48), 'flat_window': flat,
                         'defillama_v1': rep_v, 'verdict': verdict,  # post hoc split, description only:
                         'informative': verdict == 'match' and abs(int(Decimal(str(rep_v)) * UNIT) - bounds[k]['supply_base']) > UNIT})
    # offset screen and consolidated view
    other = lambda lab: sum(r['supply_base'] for r in rows if r['label'] == lab)
    labels = [day(k).date().isoformat() for k in range(N_BOUND)]
    screen = []
    for a, b in zip(labels, labels[1:]):
        dc, do = celo[b] - celo[a], other(b) - other(a)
        screen.append({'day_utc': a, 'celo_change_brla': brla(dc), 'other_chains_change_brla': brla(do),
                       'offset': dc < 0 and do > 0 and 2 * do >= -dc})
    dc, do = celo[labels[-1]] - celo[labels[0]], other(labels[-1]) - other(labels[0])
    screen.append({'day_utc': f'cumulative {labels[0]} to {labels[-1]}', 'celo_change_brla': brla(dc),
                   'other_chains_change_brla': brla(do), 'offset': dc < 0 and do > 0 and 2 * do >= -dc})
    llama_total = lambda lab: sum(Decimal(str(t['circulating']['peggedREAL'])) for ch in v1.values() for t in ch['tokens']
                                  if dt.datetime.fromtimestamp(t['date'], dt.UTC).date().isoformat() == lab)
    consolidated = [{'label': lab, 'onchain_four_contracts_brla': brla(celo[lab] + other(lab)),
                     'defillama_v1_sum_brla': f'{llama_total(lab):f}'} for lab in labels]
    write_csv(ROOT / 'data/processed/P3-29_chains.csv', rows)
    write_csv(ROOT / 'results/tables/P3-29_chains_prediction.csv', pred)
    L = ['# P3-29 S4: other listed BRLA contracts (generated by scripts/p3_29_reconcile.py chains)', '',
         'Protocol amendment 10 (registered before any value was read). totalSupply at 00:00 UTC boundaries only; no logs, '
         'so no within-day check and no transaction-level link. Amounts in BRLA.', '', '## Capabilities and identity', '',
         '| Chain | Provider | Capability | OK | Detail |', '|---|---|---|---|---|']
    L += [f"| {c['chain']} | {c['provider']} | {c['capability']} | {c['ok']} | {c['detail']} |" for c in cap]
    L += ['', '## Supply at 00:00 UTC (mn BRLA) and DefiLlama v1 minus on-chain (BRLA)', '',
          '| Label | ' + ' | '.join(f'{n} supply | {n} r' for n in CHAINS) + ' |', '|---|' + '---:|---:|' * len(CHAINS)]
    for lab in labels:
        cells = []
        for n in CHAINS:
            r = next(x for x in rows if x['chain'] == n and x['label'] == lab)
            cells += [f"{float(r['supply_brla']) / 1e6:,.3f}" if r['supply_brla'] else '-',
                      f"{float(r['r_at_0000_brla']):,.0f}" if r['r_at_0000_brla'] else '-']
        L.append(f'| {lab} | ' + ' | '.join(cells) + ' |')
    L += ['', '## Prediction P-0045 (held out from Celo): DefiLlama = equal endpoint supply at 00:44/00:48 UTC, +-1 BRLA (intervening changes not checked)', '']
    for n in CHAINS:
        v = [x['verdict'] for x in pred if x['chain'] == n]
        inf = sum(x['informative'] for x in pred if x['chain'] == n)
        L.append(f"- {n}: {v.count('match')} match, {v.count('miss')} miss, {v.count('not_tested')} not tested (unequal endpoints "
                 f"or no value); informative matches (00:44 value differs from 00:00 by more than 1 BRLA, post hoc): {inf}")
    L += [f"- misses: {[(x['chain'], x['label'], x['defillama_v1'], x['supply_0044_brla']) for x in pred if x['verdict'] == 'miss']}",
          '', '## Offset screen (Celo daily change vs the three other contracts combined; accounting, not linking)', '',
          '| Day (UTC) | Celo change | Other chains change | Offset (opposite sign, >= half) |', '|---|---:|---:|---|']
    L += [f"| {x['day_utc']} | {float(x['celo_change_brla']):,.0f} | {float(x['other_chains_change_brla']):,.0f} | {x['offset']} |"
          for x in screen]
    L += ['', '## Consolidated: sum of the four contracts at 00:00 UTC vs the sum of DefiLlama v1 chain values', '',
          '| Label | On-chain, four contracts | DefiLlama v1 sum |', '|---|---:|---:|']
    L += [f"| {x['label']} | {float(x['onchain_four_contracts_brla']):,.0f} | {float(x['defillama_v1_sum_brla']):,.0f} |"
          for x in consolidated]
    (ROOT / 'results/tables/P3-29_chains_audit.md').write_text('\n'.join(L) + '\n')
    print('\n'.join(L))


# ---------------------------------------------------------------- S3: Celo ledger (results/P3-29_protocol.md)
EVENTS = ['Transfer(address,address,uint256)', 'Approval(address,address,uint256)', 'Upgraded(address)',
          'AdminChanged(address,address)', 'BeaconUpgraded(address)', 'Initialized(uint8)', 'Paused(address)',
          'Unpaused(address)', 'RoleGranted(bytes32,address,address)', 'RoleRevoked(bytes32,address,address)',
          'RoleAdminChanged(bytes32,bytes32,bytes32)']  # every event declared in the verified BRLAV1_1 source (T-19)
FUNCS = ['mint(address,uint256)', 'burn(uint256)', 'burnFrom(address,uint256)', 'transfer(address,uint256)',
         'transferFrom(address,address,uint256)',
         'burnFromWithPermit(address,address,uint256,uint256,uint8,bytes32,bytes32)',
         'execute(bytes,bytes[])']  # last one added post hoc: the selector of the large burns' transactions
STOP_EVENTS = {'Upgraded', 'AdminChanged', 'BeaconUpgraded', 'Initialized'}
# 19 Jun .. 3 Jul (3 Jul added post hoc to test the 2 Jul label); development interval = boundaries 0..12
DAY0, B0, N_BOUND, DEV_END = dt.datetime(2026, 6, 19, tzinfo=dt.UTC), 69_926_442, 15, 12
CHUNK, MIN_CHUNK, UNIT, SEED, N_SAMPLE = 5_000, 500, 10 ** 18, 20261107, 30
DEFILLAMA_V2 = 'https://stablecoins.llama.fi/stablecoin/365'


def keccak(text):
    """Keccak-256 via the nodes' web3_sha3 (no local implementation installed); Forno and Ankr must agree."""
    h = must('forno', 'web3_sha3', '0x' + text.encode().hex())
    assert h == must('ankr', 'web3_sha3', '0x' + text.encode().hex()), text
    return h


def brla(base):
    return f'{Decimal(base) / UNIT:f}' if base is not None else ''


def get_logs(lo, hi, chunks):
    """All logs of the proxy in [lo, hi] from Forno; halves on error; a range still failing at MIN_CHUNK is a gap."""
    body = {'address': BRLA, 'fromBlock': hex(lo), 'toBlock': hex(hi)}
    res, err = rpc('forno', 'eth_getLogs', body)
    if res is not None:
        raw = str(frozen('forno', RPC['forno'], rpc_body('eth_getLogs', body))[1].relative_to(ROOT))
        chunks.append({'check': 'log_chunk', 'from_block': lo, 'to_block': hi, 'status': 'ok', 'n': len(res), 'detail': raw})
        return [dict(l, _raw=raw) for l in res]
    if hi - lo + 1 <= MIN_CHUNK:
        chunks.append({'check': 'log_chunk', 'from_block': lo, 'to_block': hi, 'status': 'gap', 'n': '', 'detail': err})
        return []
    mid = (lo + hi) // 2
    return get_logs(lo, mid, chunks) + get_logs(mid + 1, hi, chunks)


def receipt_check(e):
    """Is the log in a successful receipt from a second source (Ankr by hash; else Forno by block, same provider)?"""
    rec, err = rpc('ankr', 'eth_getTransactionReceipt', e['tx'])
    source = 'ankr'
    if rec is None:
        blk = rpc('forno', 'eth_getBlockReceipts', hex(e['block']))[0] or []
        rec, source = next((r for r in blk if r['transactionHash'] == e['tx']), None), 'forno_block (same provider)'
    ok = bool(rec) and rec['status'] == '0x1' and any(
        int(l['logIndex'], 16) == e['log_index'] and l['topics'] == e['topics'] and l['data'] == e['data']
        and l['blockHash'] == e['block_hash'] for l in rec['logs'])
    return ok, source if rec else f'no receipt: {err}'


def collect(day0, n_bound, head, topic):
    """Boundaries day0 + k days (k < n_bound) on Forno and Ankr; every proxy log between the first and last; decoded."""
    checks, bounds = [], []
    for k in range(n_bound):
        t = day0 + dt.timedelta(days=k)
        b = block_at(int(t.timestamp()), head, guess=B0 + int((t - DAY0).total_seconds()))
        h = header(b)
        call = ({'to': BRLA, 'data': SEL['totalSupply']}, hex(b))
        bounds.append({'k': k, 'label': t.date().isoformat(), 'block': b, 'hash': h['hash'],
                       'time_utc': dt.datetime.fromtimestamp(int(h['timestamp'], 16), dt.UTC).isoformat(),
                       'forno': int(must('forno', 'eth_call', *call), 16),
                       'ankr': (lambda r: int(r, 16) if r else None)(rpc('ankr', 'eth_call', *call)[0]),
                       'decimals': int(must('forno', 'eth_call', {'to': BRLA, 'data': SEL['decimals']}, hex(b)), 16),
                       'impl': word_addr(must('forno', 'eth_getStorageAt', BRLA, IMPL_SLOT, hex(b)))})
    one_second = all(bounds[k + 1]['block'] - bounds[k]['block'] == 86_400 for k in range(n_bound - 1))
    checks.append({'check': 'one_second_blocks', 'status': 'ok' if one_second else 'fail',
                   'detail': 'every UTC day has exactly 86,400 blocks, so block time = boundary time + offset'})

    # logs, deduplicated and decoded
    chunks, logs, lo = [], [], bounds[0]['block'] + 1
    while lo <= bounds[-1]['block']:
        hi = min(lo + CHUNK - 1, bounds[-1]['block'])
        logs += get_logs(lo, hi, chunks)
        lo = hi + 1
    tiled = sorted((c['from_block'], c['to_block']) for c in chunks)
    tiles_ok = tiled[0][0] == bounds[0]['block'] + 1 and tiled[-1][1] == bounds[-1]['block'] and all(
        a[1] + 1 == b[0] for a, b in zip(tiled, tiled[1:]))
    checks.append({'check': 'chunks_tile_interval', 'status': 'ok' if tiles_ok else 'fail',
                   'detail': f"{len(chunks)} chunks, {sum(c['status'] == 'gap' for c in chunks)} gaps"})
    seen, events, dup, removed, hashes = set(), [], 0, 0, {}
    for l in logs:
        key = (l['blockHash'], l['transactionHash'], l['logIndex'])
        if key in seen:
            dup += 1
            continue
        seen.add(key)
        removed += bool(l.get('removed'))
        n = int(l['blockNumber'], 16)
        hashes.setdefault(n, set()).add(l['blockHash'])
        k = next(i for i in range(n_bound - 1) if bounds[i]['block'] < n <= bounds[i + 1]['block'])
        e = {'day_utc': bounds[k]['label'], 'block': n, 'log_index': int(l['logIndex'], 16), 'tx': l['transactionHash'],
             'block_hash': l['blockHash'], 'event': topic.get(l['topics'][0], 'unknown'), 'topic0': l['topics'][0],
             'time_utc': (dt.datetime.fromisoformat(bounds[k]['time_utc']) + dt.timedelta(seconds=n - bounds[k]['block'])
                          ).isoformat() if one_second else '',
             'raw_file': l['_raw'], 'topics': l['topics'], 'data': l['data'], 'k': k}
        if 'blockTimestamp' in l and one_second:
            assert int(l['blockTimestamp'], 16) == int(dt.datetime.fromisoformat(e['time_utc']).timestamp()), e
        if e['event'] == 'Transfer':
            frm, to = '0x' + l['topics'][1][-40:], '0x' + l['topics'][2][-40:]
            e['type'] = 'mint' if frm == ZERO else 'burn' if to == ZERO else 'transfer'
            e['counterparty'] = to if e['type'] == 'mint' else frm if e['type'] == 'burn' else ''
            e['amount_base'] = int(l['data'], 16)
        else:
            e['type'] = 'other'
        events.append(e)
    events.sort(key=lambda e: (e['block'], e['log_index']))
    for b in bounds:  # boundary blocks that carry logs: their hash must equal the header hash
        if b['block'] in hashes:
            assert hashes[b['block']] == {b['hash']}, b
    checks += [{'check': 'duplicate_logs', 'status': 'ok', 'n': dup, 'detail': 'dropped on (blockHash, tx, logIndex)'},
               {'check': 'removed_logs', 'status': 'ok' if removed == 0 else 'fail', 'n': removed},
               {'check': 'one_hash_per_block', 'status': 'ok' if all(len(v) == 1 for v in hashes.values()) else 'fail',
                'n': len(hashes)},
               {'check': 'unknown_topics', 'status': 'ok' if all(e['event'] != 'unknown' for e in events) else 'fail',
                'n': sum(e['event'] == 'unknown' for e in events)}]
    return bounds, events, chunks, checks


def bridge(bounds, events, chunks, k0, k1, label):
    """Stock identity between boundaries k0 and k1: supply change minus (mints - burns), in base units."""
    ev = [e for e in events if k0 <= e['k'] < k1]
    mint = [e['amount_base'] for e in ev if e['type'] == 'mint']
    burn = [e['amount_base'] for e in ev if e['type'] == 'burn']
    gap = any(c['status'] != 'ok' and c['from_block'] <= bounds[k1]['block'] and c['to_block'] > bounds[k0]['block']
              for c in chunks)
    stop = [e['event'] for e in ev if e['event'] in STOP_EVENTS]
    ds = bounds[k1]['forno'] - bounds[k0]['forno']
    r = None if gap else ds - (sum(mint) - sum(burn))
    return {'interval': label, 'start_block': bounds[k0]['block'], 'end_block': bounds[k1]['block'],
            'start_supply_brla': brla(bounds[k0]['forno']), 'end_supply_brla': brla(bounds[k1]['forno']),
            'delta_supply_brla': brla(ds), 'gross_mints_brla': brla(sum(mint)), 'gross_burns_brla': brla(sum(burn)),
            'n_mints': len(mint), 'n_burns': len(burn), 'n_transfers': sum(e['type'] == 'transfer' for e in ev),
            'other_events': ';'.join(sorted({e['event'] for e in ev if e['type'] == 'other'})),
            'r_stock_base': '' if r is None else r, 'coverage_complete': not gap,
            'ankr_equal_at_ends': bounds[k0]['ankr'] == bounds[k0]['forno'] and bounds[k1]['ankr'] == bounds[k1]['forno'],
            'implementation_same': bounds[k0]['impl'] == bounds[k1]['impl'], 'stop_events': ';'.join(stop),
            'decimals_18': bounds[k0]['decimals'] == bounds[k1]['decimals'] == 18}


def label_checks(bounds, events, recon, v1, v2):
    """Raw residual at 00:00 UTC and the within-day consistency rule (+-1 BRLA) for each boundary's label."""
    snaps = []
    for b in bounds:
        day_ok = b['k'] < len(bounds) - 1 and recon[b['k']]['r_stock_base'] == 0
        path = [(b['time_utc'], b['forno'])]
        if day_ok:
            s = b['forno']
            for blk_events in group_by_block([e for e in events if e['k'] == b['k'] and e['type'] in ('mint', 'burn')]):
                s += sum(e['amount_base'] if e['type'] == 'mint' else -e['amount_base'] for e in blk_events)
                path.append((blk_events[0]['time_utc'], s))
        for p, val in (('forno', b['forno']), ('ankr', b['ankr'])):
            row = {'label': b['label'], 'block': b['block'], 'hash': b['hash'], 'time_utc': b['time_utc'], 'provider': p,
                   'total_supply_base': val, 'total_supply_brla': brla(val), 'decimals': b['decimals'],
                   'implementation': b['impl']}
            if p == 'forno':
                rep1, rep2 = v1.get(b['label']), v2.get(b['label'])
                rep_base = None if rep1 is None else int(Decimal(str(rep1)) * UNIT)
                status = 'no_reported_value' if rep1 is None else 'not_tested' if not day_ok else 'outside_day_range'
                match = [t for t, s in path if rep_base is not None and abs(rep_base - s) <= UNIT]
                if match and day_ok:
                    status = 'consistent_within_day'
                row.update({'defillama_v1': rep1, 'defillama_v2': rep2, 'revised_v2_vs_v1': rep2 is not None and rep1 != rep2,
                            'r_at_0000_brla': '' if rep_base is None else brla(rep_base - val),
                            'day_path_min_brla': brla(min(s for _, s in path)) if day_ok else '',
                            'day_path_max_brla': brla(max(s for _, s in path)) if day_ok else '',
                            'day_path_points': len(path) if day_ok else '', 'provider_check': status,
                            'first_match_utc': match[0] if match else '', 'last_match_utc': match[-1] if match else '',
                            'alignment_status': 'time_alignment_unknown'})
            snaps.append(row)
    return snaps


def cross_check(mb, n_sample, selector):
    """Receipts (second source) for every mint/burn >= 1% of gross volume and a seeded sample of the rest."""
    gross = sum(e['amount_base'] for e in mb)
    large = [e for e in mb if e['amount_base'] * 100 >= gross]
    big = {id(e) for e in large}
    sample = random.Random(SEED).sample([e for e in mb if id(e) not in big], min(n_sample, len(mb) - len(large)))
    for e in large + sample:
        ok, source = receipt_check(e)
        e.update({'cross_check': ('large' if id(e) in big else 'sample'), 'receipt_ok': ok, 'receipt_source': source})
        if id(e) in big:
            tx = rpc('ankr', 'eth_getTransactionByHash', e['tx'])[0] or rpc('forno', 'eth_getTransactionByHash', e['tx'])[0]
            e.update({'tx_from': tx['from'], 'tx_to': tx['to'], 'selector': tx['input'][:10],
                      'function': selector.get(tx['input'][:10], 'unknown'),
                      'block_hash_matches_header': header(e['block'])['hash'] == e['block_hash']})
    check = {'check': 'receipts_large_and_sample', 'n': len(large) + len(sample),
             'status': 'ok' if all(e['receipt_ok'] for e in large + sample) else 'fail',
             'detail': f"{len(large)} events >= 1% of gross {brla(gross)} BRLA + {len(sample)} sampled (seed {SEED})"}
    return large, sample, gross, check


def setup():
    head = int(must('forno', 'eth_blockNumber'), 16)
    topic = {keccak(s): s.split('(')[0] for s in EVENTS}
    assert topic.get(TRANSFER) == 'Transfer' and topic.get(UPGRADED) == 'Upgraded'
    selector = {keccak(s)[:10]: s.split('(')[0] for s in FUNCS}
    v2_raw = fetch('defillama', DEFILLAMA_V2)
    return head, topic, selector, defillama_celo(), defillama_celo(v2_raw) if 'chainBalances' in v2_raw else {}


def ledger():
    head, topic, selector, v1, v2 = setup()
    bounds, events, chunks, checks = collect(DAY0, N_BOUND, head, topic)
    recon = [bridge(bounds, events, chunks, k, k + 1, f"day {bounds[k]['label']}") for k in range(N_BOUND - 1)]
    dev = bridge(bounds, events, chunks, 0, DEV_END, f"development {bounds[0]['label']} to {bounds[DEV_END]['label']} 00:00 UTC")
    snaps = label_checks(bounds, events, recon, v1, v2)
    rep0, rep1 = v1.get(bounds[0]['label']), v1.get(bounds[DEV_END]['label'])
    d_rep = Decimal(str(rep1)) - Decimal(str(rep0))
    r_prov = d_rep - Decimal(bounds[DEV_END]['forno'] - bounds[0]['forno']) / UNIT
    dev.update({'defillama_delta_brla': f'{d_rep:f}', 'r_provider_brla': f'{r_prov:f}',
                'r_provider_relative': f'{abs(r_prov) / max(abs(d_rep), Decimal(1)):.6f} (denominator |delta reported|)'})
    dev_mb = [e for e in events if e['k'] < DEV_END and e['type'] in ('mint', 'burn')]
    large, sample, gross, check = cross_check(dev_mb, N_SAMPLE, selector)
    checks.append(check)

    # post hoc: Blockscout metadata of every minter/burner and every contract the large events' transactions called
    addrs = sorted({e['counterparty'] for e in dev_mb} | {e['tx_to'].lower() for e in large})
    meta = []
    for a in addrs:
        m = fetch('blockscout', f'{REST}/addresses/{a}')
        meta.append({'address': a, 'is_contract': m.get('is_contract'), 'name': m.get('name'),
                     'is_verified': m.get('is_verified'), 'implementations': [i.get('name') for i in m.get('implementations') or []],
                     'creator': m.get('creator_address_hash'), 'public_tags': m.get('public_tags'),
                     'error': m.get('error')})

    # outputs
    keep = ['day_utc', 'time_utc', 'block', 'log_index', 'tx', 'event', 'type', 'counterparty', 'amount_base',
            'cross_check', 'receipt_ok', 'receipt_source', 'tx_from', 'tx_to', 'selector', 'function',
            'block_hash_matches_header', 'interpretation', 'raw_file']
    out = [dict({c: e.get(c, '') for c in keep}, amount_brla=brla(e.get('amount_base')), interpretation='unresolved')
           for e in events if e['type'] != 'transfer']
    write_csv(ROOT / 'data/processed/P3-29_events.csv', out)
    write_csv(ROOT / 'data/processed/P3-29_snapshots.csv', snaps)
    write_csv(ROOT / 'data/processed/P3-29_reconciliation.csv', recon + [dev])
    write_csv(ROOT / 'results/tables/P3-29_coverage.csv', checks + chunks)
    audit(dev, recon, snaps, large, sample, dev_mb, gross, checks, events, meta)


# ---------------------------------------------------------------- S5: frozen additional cases (protocol 8, 11)
S5_MANIFEST = ROOT / 'results/tables/P3-29_s5_manifest.csv'


def manifest():
    """Selection from DefiLlama v1 alone (no on-chain data): 6 large and 6 ordinary daily changes outside June."""
    v1, date = defillama_celo(), dt.date.fromisoformat
    inv = [(d, Decimal(str(v1[d])) - Decimal(str(v1[(date(d) - dt.timedelta(days=1)).isoformat()])))
           for d in sorted(v1) if '2026-03-25' <= d <= '2026-10-30' and not '2026-06-18' <= d <= '2026-07-02'
           and (date(d) - dt.timedelta(days=1)).isoformat() in v1]
    far = lambda d, kept: all(abs((date(d) - date(k)).days) >= 7 for k, _ in kept)
    large = []
    for d, x in sorted(inv, key=lambda r: -abs(r[1])):
        if len(large) < 6 and far(d, large):
            large.append((d, x))
    q1, _, q3 = statistics.quantiles([abs(x) for _, x in inv], n=4, method='inclusive')
    eligible = [(d, x) for d, x in inv if q1 <= abs(x) <= q3 and far(d, large)]
    ordinary = sorted(random.Random(SEED).sample(eligible, 6))
    rows = [{'case': f'{kind}{i + 1}', 'kind': kind, 'label': d, 'delta_reported_v1_brla': f'{x:f}',
             'inventory_days': len(inv), 'abs_q1_brla': f'{q1:f}', 'abs_q3_brla': f'{q3:f}', 'eligible_ordinary': len(eligible)}
            for kind, sel in (('L', large), ('O', ordinary)) for i, (d, x) in enumerate(sel)]
    write_csv(S5_MANIFEST, rows)
    for r in rows:
        print(r)


def cases():
    if not S5_MANIFEST.exists():
        manifest()
        sys.exit(f'{S5_MANIFEST.relative_to(ROOT)} written: commit it, then run `cases` again to collect')
    head, topic, selector, v1, v2 = setup()
    summary, details = [], []
    for c in csv.DictReader(open(S5_MANIFEST)):
        day0 = dt.datetime.fromisoformat(c['label']).replace(tzinfo=dt.UTC) - dt.timedelta(days=1)
        bounds, events, chunks, checks = collect(day0, 3, head, topic)
        recon = [bridge(bounds, events, chunks, k, k + 1, f"day {bounds[k]['label']}") for k in range(2)]
        snaps = {s['label']: s for s in label_checks(bounds, events, recon, v1, v2) if s['provider'] == 'forno'}
        mb = [e for e in events if e['type'] in ('mint', 'burn')]
        large, sample, gross, check = cross_check(mb, 5, selector)
        vol = {}
        for e in mb:
            vol[e['counterparty']] = vol.get(e['counterparty'], 0) + e['amount_base']
        top = max(vol.items(), key=lambda x: x[1]) if vol else ('', 0)
        prev = bounds[0]['label']
        summary.append({
            'case': c['case'], 'kind': c['kind'], 'label': c['label'], 'delta_reported_v1_brla': c['delta_reported_v1_brla'],
            'onchain_change_two_days_brla': brla(bounds[2]['forno'] - bounds[0]['forno']),
            'gross_mints_brla': brla(sum(e['amount_base'] for e in mb if e['type'] == 'mint')),
            'gross_burns_brla': brla(sum(e['amount_base'] for e in mb if e['type'] == 'burn')),
            'n_mint_burn': len(mb), 'stock_residual_base_day1': recon[0]['r_stock_base'],
            'stock_residual_base_day2': recon[1]['r_stock_base'],
            'integrity_ok': all(x['status'] == 'ok' for x in checks) and all(r['coverage_complete'] and r['ankr_equal_at_ends']
                                                                            and r['implementation_same'] and not r['stop_events'] for r in recon),
            'provider_prev_label': snaps[prev]['provider_check'], 'provider_label': snaps[c['label']]['provider_check'],
            'match_time_prev_utc': snaps[prev]['first_match_utc'][11:19], 'match_time_label_utc': snaps[c['label']]['first_match_utc'][11:19],
            'r_at_0000_label_brla': snaps[c['label']]['r_at_0000_brla'],
            'receipts': f"{sum(e['receipt_ok'] for e in large + sample)}/{len(large) + len(sample)}",
            'top_counterparty': top[0], 'top_share': f'{100 * top[1] / sum(vol.values()):.1f}%' if vol else '',
            'n_counterparties': len(vol), 'large_functions': ';'.join(sorted({e['function'] for e in large}))})
        details += [dict(r, case=c['case']) for r in recon]
    write_csv(ROOT / 'results/tables/P3-29_s5_cases.csv', summary)
    write_csv(ROOT / 'data/processed/P3-29_s5_days.csv', details)
    for r in summary:
        print({k: r[k] for k in ('case', 'label', 'delta_reported_v1_brla', 'stock_residual_base_day1', 'stock_residual_base_day2',
                                 'integrity_ok', 'provider_prev_label', 'provider_label', 'match_time_label_utc', 'receipts',
                                 'top_share', 'n_counterparties')})


def group_by_block(evs):
    out = []
    for e in evs:
        if out and out[-1][0]['block'] == e['block']:
            out[-1].append(e)
        else:
            out.append([e])
    return out


def audit(dev, recon, snaps, large, sample, dev_mb, gross, checks, events, meta):
    """results/tables/P3-29_case_audit.md: what an independent reader needs to follow every number."""
    L = ['# P3-29 case audit: BRLA on Celo, 19-30 Jun 2026 (generated by scripts/p3_29_reconcile.py ledger)', '',
         'Protocol: results/P3-29_protocol.md. Amounts in BRLA (base units / 10^18). Interpretation of every event: '
         'unresolved (on-chain records do not say why anyone minted or burned).', '', '## Development interval', '']
    L += [f'- {k}: {v}' for k, v in dev.items()]
    L += ['', '## Daily stock identity (UTC days)', '',
          '| Day | Supply start | Supply end | Mints (n) | Burns (n) | Residual (base units) | Coverage | Ankr = Forno |',
          '|---|---:|---:|---:|---:|---:|---|---|']
    L += [f"| {r['interval'][4:]} | {float(r['start_supply_brla']):,.2f} | {float(r['end_supply_brla']):,.2f} | "
          f"{float(r['gross_mints_brla']):,.2f} ({r['n_mints']}) | {float(r['gross_burns_brla']):,.2f} ({r['n_burns']}) | "
          f"{r['r_stock_base']} | {r['coverage_complete']} | {r['ankr_equal_at_ends']} |" for r in recon]
    L += ['', '## DefiLlama labels (v1 = Flash 4 Nov; v2 = fresh pull)', '',
          '| Label | Reported v1 | v2 revised? | v1 minus on-chain at 00:00 UTC | Day path min-max | Check | First / last match (description only) |',
          '|---|---:|---|---:|---|---|---|']
    for s in snaps:
        if s['provider'] != 'forno':
            continue
        rng = f"{float(s['day_path_min_brla']):,.0f} - {float(s['day_path_max_brla']):,.0f}" if s['day_path_min_brla'] else ''
        L.append(f"| {s['label']} | {s['defillama_v1']} | {s['revised_v2_vs_v1']} | "
                 f"{float(s['r_at_0000_brla']):,.2f} | {rng} | {s['provider_check']} | "
                 f"{s['first_match_utc'][11:19]} / {s['last_match_utc'][11:19]} |" if s['r_at_0000_brla'] != '' else
                 f"| {s['label']} | - | - | - | {rng} | {s['provider_check']} | |")
    L += ['', f'## Events of at least 1% of gross supply-changing volume ({float(Decimal(gross) / UNIT):,.2f} BRLA)', '',
          '| Time UTC | Type | Amount | Counterparty | Tx to | Function | Receipt | Header hash |', '|---|---|---:|---|---|---|---|---|']
    L += [f"| {e['time_utc'][:19]} | {e['type']} | {float(Decimal(e['amount_base']) / UNIT):,.2f} | `{e['counterparty']}` | "
          f"`{e['tx_to']}` | {e['function']} | {e['receipt_ok']} ({e['receipt_source']}) | {e['block_hash_matches_header']} |"
          for e in large]
    L += ['', f"Sampled smaller events: {len(sample)}, receipts confirmed {sum(e['receipt_ok'] for e in sample)} "
          f"(sources: {sorted({e['receipt_source'] for e in sample})}).", '', '## Counterparty concentration (addresses, not owners)', '']
    for typ in ('mint', 'burn'):
        vol = {}
        for e in dev_mb:
            if e['type'] == typ:
                vol[e['counterparty']] = vol.get(e['counterparty'], 0) + e['amount_base']
        tot = sum(vol.values())
        L += [f'**{typ}s:** {len(vol)} addresses, total {float(Decimal(tot) / UNIT):,.2f} BRLA', '',
              '| Address | BRLA | Share |', '|---|---:|---:|']
        L += [f'| `{a}` | {float(Decimal(v) / UNIT):,.2f} | {100 * v / tot:.1f}% |'
              for a, v in sorted(vol.items(), key=lambda x: -x[1])[:10]]
        L.append('')
    by_brt = {}
    for e in dev_mb:
        d = (dt.datetime.fromisoformat(e['time_utc']) - dt.timedelta(hours=3)).date().isoformat()
        m, b = by_brt.get(d, (0, 0))
        by_brt[d] = (m + e['amount_base'], b) if e['type'] == 'mint' else (m, b + e['amount_base'])
    L += ['## Sensitivity: mints and burns by Brasília day (description only)', '', '| Day (UTC-3) | Mints | Burns |', '|---|---:|---:|']
    L += [f'| {d} | {float(Decimal(m) / UNIT):,.2f} | {float(Decimal(b) / UNIT):,.2f} |' for d, (m, b) in sorted(by_brt.items())]
    L += ['', '## Addresses (Blockscout metadata, post hoc; describes the account, not its owner)', '',
          '| Address | Contract | Name / implementation | Verified | Creator | Public tags |', '|---|---|---|---|---|---|']
    L += [f"| `{m['address']}` | {m['is_contract']} | {m['name'] or ''} {m['implementations'] or ''} | {m['is_verified']} | "
          f"`{m['creator'] or ''}` | {m['public_tags'] or m['error'] or ''} |" for m in meta]
    L += ['', '## Checks', ''] + [f"- {c['check']}: {c['status']} {c.get('n', '')} {c.get('detail', '')}" for c in checks]
    L += [f"- other events in the collected interval: "
          f"{sorted({(e['event'], e['day_utc']) for e in events if e['type'] == 'other'})}"]
    (ROOT / 'results/tables/P3-29_case_audit.md').write_text('\n'.join(L) + '\n')
    print('\n'.join(L))


# ---------------------------------------------------------------- S6 candidate figure (reads S3 outputs only)
def figure():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.dates as mdates
    import matplotlib.pyplot as plt
    ink, ink2, grid, surf, blue, orange = '#0b0b0b', '#52514e', '#e4e3df', '#fcfcfb', '#2a78d6', '#eb6834'
    snaps = [r for r in csv.DictReader(open(ROOT / 'data/processed/P3-29_snapshots.csv')) if r['provider'] == 'forno']
    ev = [r for r in csv.DictReader(open(ROOT / 'data/processed/P3-29_events.csv')) if r['type'] in ('mint', 'burn')]
    t = lambda x: dt.datetime.fromisoformat(x)
    s0 = int(snaps[0]['total_supply_base'])
    path_t, path_s, s = [t(snaps[0]['time_utc'])], [s0 / UNIT / 1e6], s0
    for blk in group_by_block([dict(e, block=int(e['block'])) for e in ev]):
        s += sum(int(e['amount_base']) * (1 if e['type'] == 'mint' else -1) for e in blk)
        path_t.append(t(blk[0]['time_utc']))
        path_s.append(s / UNIT / 1e6)
    fig, (a, b) = plt.subplots(2, 1, figsize=(10, 7.2), sharex=True, gridspec_kw={'height_ratios': [3, 2]}, facecolor=surf)
    for ax in (a, b):
        ax.set_facecolor(surf)
        ax.grid(axis='y', color=grid, lw=0.8)
        ax.set_axisbelow(True)
        ax.tick_params(colors=ink2, labelsize=9)
        for side in ('top', 'right'):
            ax.spines[side].set_visible(False)
        for side in ('left', 'bottom'):
            ax.spines[side].set_color(ink2)
        ax.axvline(dt.datetime(2026, 7, 1, tzinfo=dt.UTC), color=ink2, lw=1, ls=(0, (3, 3)))
    a.step(path_t, path_s, where='post', color=blue, lw=1.6, label='Oferta on-chain (totalSupply, após cada bloco com emissão/queima)')
    ok = [r for r in snaps if r['provider_check'] == 'consistent_within_day']
    bad = [r for r in snaps if r['provider_check'] == 'outside_day_range']
    a.plot([t(r['first_match_utc']) for r in ok], [float(r['defillama_v1']) / 1e6 for r in ok], 'o', ms=6, color=ink,
           markeredgecolor=surf, markeredgewidth=1.2, label='DefiLlama, valor diário (igual à oferta on-chain em algum bloco do dia)', zorder=3)
    a.plot([t(r['time_utc']) for r in bad], [float(r['defillama_v1']) / 1e6 for r in bad], 'o', ms=7, mfc=surf, mec=ink, mew=1.6,
           label='DefiLlama, 26/06 e 02/07: 59,28 mi, sem correspondência on-chain', zorder=3)
    big = max((e for e in ev if e['type'] == 'burn'), key=lambda e: int(e['amount_base']))
    bt = t(big['time_utc'])
    a.annotate(f"queima de {float(Decimal(big['amount_base']) / UNIT) / 1e6:,.1f} mi\n{bt:%d/%m %H:%M} UTC".replace(',', 'X').replace('.', ',').replace('X', '.'),
               xy=(bt, 96), xytext=(bt + dt.timedelta(hours=20), 70), fontsize=8.5, color=ink2,
               arrowprops={'arrowstyle': '-', 'color': ink2, 'lw': 0.8})
    a.set_ylabel('milhões de BRLA', color=ink2, fontsize=9)
    a.set_ylim(40, 300)
    a.legend(loc='upper left', bbox_to_anchor=(0.17, 1.0), fontsize=8, frameon=False, labelcolor=ink)
    a.set_title('Oferta de BRLA na Celo e valores diários do DefiLlama', loc='left', fontsize=11, color=ink)
    days = sorted({e['day_utc'] for e in ev})
    x = [dt.datetime.fromisoformat(d).replace(tzinfo=dt.UTC) + dt.timedelta(hours=12) for d in days]
    vol = lambda d, typ: sum(int(e['amount_base']) for e in ev if e['day_utc'] == d and e['type'] == typ) / UNIT / 1e6
    mints, burns = [vol(d, 'mint') for d in days], [vol(d, 'burn') for d in days]
    w = dt.timedelta(hours=16)
    b.bar(x, mints, width=w, color=blue, label='Emissões (mints)')
    b.bar(x, [-v for v in burns], width=w, color=orange, label='Queimas (burns)')
    b.plot(x, [m - q for m, q in zip(mints, burns)], 'D', ms=5, color=ink, markeredgecolor=surf, label='Variação líquida da oferta')
    b.axhline(0, color=ink2, lw=0.8)
    b.set_ylabel('milhões de BRLA por dia', color=ink2, fontsize=9)
    b.legend(loc='upper center', bbox_to_anchor=(0.5, 1.0), fontsize=8, frameon=False, ncol=3, labelcolor=ink)
    b.set_title('Emissões e queimas por dia (UTC): o saldo líquido é pequeno perto dos fluxos brutos', loc='left', fontsize=11, color=ink)
    b.text(dt.datetime(2026, 7, 1, 2, tzinfo=dt.UTC), max(mints) * 0.9, 'fora do caso\n(1–2/07)', fontsize=8, color=ink2)
    b.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))
    b.set_xlim(dt.datetime(2026, 6, 19, tzinfo=dt.UTC), dt.datetime(2026, 7, 3, tzinfo=dt.UTC))
    fig.text(0.01, 0.005, 'Fontes: Celo JSON-RPC (Forno; conferido na Ankr), contrato 0xfecb…3760; DefiLlama, stablecoin 365 (versão de 4/11/2026).\n'
             'A identidade de estoque fecha com resíduo zero em todos os dias. Emissão não é entrada de reais; queima não é resgate.',
             fontsize=7, color=ink2)
    fig.tight_layout(rect=(0, 0.035, 1, 1))
    out = ROOT / 'results/figures/P3-29_supply_bridge.png'
    fig.savefig(out, dpi=200, facecolor=surf)
    print(out.relative_to(ROOT))


if __name__ == '__main__':
    if sys.argv[1:] not in (['smoke'], ['ledger'], ['chains'], ['cases'], ['figure']):
        sys.exit(__doc__)
    {'smoke': smoke, 'ledger': ledger, 'chains': chains, 'cases': cases, 'figure': figure}[sys.argv[1]]()
