r"""P3-29: reconcile BRLA supply with on-chain records. S1 = feasibility smoke test (Celo only).
Specification: tasks/P3-29-on-chain-reconciliation.md (S1). No event is classified here; S2 freezes the protocol first.

What S1 checks, before any bulk collection, on two public read-only providers (no keys):
  chain ID; historical block headers; historical contract code, EIP-1967 proxy slots and state (totalSupply, decimals)
  at an opening and a closing block; event logs (range limits) and one receipt; contract metadata from Blockscout.
  Then sets the opening/closing totalSupply next to DefiLlama's Celo series (Flash bundle).
Contract  BRLA on Celo 0xfecb3f7c54e2caae9dc6ac9060a822d47e053760 (CoinGecko D-20, Avenia terms T-06, DefiLlama adapter)
Snapshot  T0 = 2026-06-19 00:00 UTC, T1 = 2026-07-01 00:00 UTC (the task's initial 19-30 Jun case; S2 freezes the final
          boundaries). Block "at" T = last block with timestamp <= T. Event interval would be (b0, b1].
Units     integer base units; BRLA = base / 10**decimals (decimals read on-chain), exact Decimal, presentation only. UTC.
Providers forno = https://forno.celo.org (Celo Foundation JSON-RPC); blockscout = https://celo.blockscout.com/api/eth-rpc
          (+ REST v2, explorer's own index); ankr = https://rpc.ankr.com/celo. Probe-only (historical eth_call at b0, one
          receipt): 1rpc, stakely, drpc.
Inputs    the endpoints above; data/raw/flash-mentor-leads/brla/raw_defillama_brla_supply.json (restore: data/README.md)
Outputs   data/raw/p3_29/<provider>/*.json  request, URL, retrieval UTC, HTTP status, response (immutable; checksums
          appended to data/raw/SHA256SUMS). Only HTTP-200 answers are frozen, so throttled calls are retried on a re-run.
          data/processed/P3-29_snapshots.csv, results/tables/P3-29_coverage.csv
Run       .venv/bin/python scripts/p3_29_reconcile.py smoke
          P3_29_OFFLINE=1 .venv/bin/python scripts/p3_29_reconcile.py smoke   (frozen responses only; stops on a miss)
"""
import csv
import datetime as dt
import hashlib
import json
import os
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
SPACING = {'blockscout': 2.0}  # seconds between live calls (its free tier answers 429 to bursts)
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


def fetch(provider, url, body=None):
    """JSON-RPC POST (body) or REST GET (body None). HTTP-200 answers are frozen and reused; failed calls are frozen
    under failed/ as evidence (replayed offline, never reused live, so a live re-run retries them)."""
    key = hashlib.sha256((url + json.dumps(body, sort_keys=True)).encode()).hexdigest()[:20]
    name = f"{body['method'] if body else 'GET'}_{key}"
    f = RAW / provider / f'{name}.json'
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
            if status not in (429, 502, 503, 504):
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
    r = fetch(provider, url or RPC[provider], {'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': list(params)})
    return r.get('result'), r.get('error')


def must(provider, method, *params):
    res, err = rpc(provider, method, *params)
    if err or res is None:
        raise RuntimeError(f'{provider} {method} {params}: {err or "null result"}')
    return res


def header(n, provider='forno'):
    return must(provider, 'eth_getBlockByNumber', hex(n), False)


def block_at(t, head):
    """Last block with timestamp <= t (binary search on headers)."""
    lo, hi = 1, head
    assert int(header(lo)['timestamp'], 16) <= t < int(header(hi)['timestamp'], 16)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        lo, hi = (mid, hi) if int(header(mid)['timestamp'], 16) <= t else (lo, mid)
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


def defillama_celo():
    d = json.loads(DEFILLAMA.read_text())
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
    for path, data in [(ROOT / 'data/processed/P3-29_snapshots.csv', rows),
                       (ROOT / 'results/tables/P3-29_coverage.csv', coverage)]:
        with open(path, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(data[0]))
            w.writeheader()
            w.writerows(data)
    for c in coverage:
        print(f"{c['status']:4} {c['capability']:40} {c['provider']:18} {c['detail']}")
    for r in rows:
        print(r['label'], r['provider'], r['block'], r['time_utc'], r['total_supply_brla'], 'DefiLlama',
              r['defillama_circulating'], 'diff', r['diff_defillama_minus_onchain_brla'])


if __name__ == '__main__':
    if sys.argv[1:] != ['smoke']:
        sys.exit(__doc__)
    smoke()
