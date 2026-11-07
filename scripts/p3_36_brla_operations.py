"""P3-36: read-only BRLA operation investigation; results/P3-36_protocol.md.

Inputs: frozen P3-29_events.csv and P3-29 RPC files; public Forno, Ankr and
Blockscout. New responses are immutable under data/raw/p3_36/ with checksums.
Outputs: results/tables/P3-36_{sample,operations,commands,transfers,provenance}.csv.
Units: integer token base units; BRLA uses 18 decimals; timestamps UTC.
Run: python3 scripts/p3_36_brla_operations.py [--offline] [--smoke]
Offline replay requires both raw bundles. No transaction is sent or signed.
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import re
import urllib.request
from decimal import Decimal
from pathlib import Path

import p3_29_reconcile as base

ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT / 'data/raw/p3_29'
RAW = ROOT / 'data/raw/p3_36'
OUT = ROOT / 'results/tables'
VM = '0xa5e1a81738259256181f9a0e478188553062d340'
IMPL = '0x37f794f3f586a76a643be0be0d107d6b671afa78'
EXEC = '0x24856bc3'
COMPLETE = '0x18643e9c376d4717d245cfdb57ec1bfe08520d98fa387b945b540fcb68c2dfaa'
MAX = 2**256 - 1
PROVENANCE = {}
DOCUMENTS = {
    'fees-and-balances': 'https://integration-guide.avenia.io/docs/Concepts/feesAndBalances/',
    'quote-ticket-faq': 'https://integration-guide.avenia.io/docs/FAQ/faqQuoteAndTicket/',
    'async-reports': 'https://integration-guide.avenia.io/docs/Avenia-Account-Management/asyncReports/',
    'combinations': 'https://integration-guide.avenia.io/docs/Operations/combinations/',
    'pix-stable-usecase': 'https://integration-guide.avenia.io/docs/Usecases/pix2Stable&stable2pix/',
}


def documents(offline):
    rows = []
    for name, url in DOCUMENTS.items():
        p = RAW / 'documents' / (name + '.json')
        if not p.exists():
            if offline:
                raise FileNotFoundError(p)
            req = urllib.request.Request(url, headers={'User-Agent': 'P3-36 read-only research'})
            with urllib.request.urlopen(req, timeout=30) as response:
                html = response.read().decode('utf-8')
                record = {'url': url, 'final_url': response.url, 'http_status': response.status,
                          'retrieved_utc': dt.datetime.now(dt.UTC).isoformat(), 'html': html}
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(record, indent=2))
            with base.SUMS.open('a') as f:
                f.write(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(ROOT)}\n')
        record = json.loads(p.read_text())
        rows.append({'name': name, 'url': url, 'retrieved_utc': record['retrieved_utc'],
                     'path': str(p.relative_to(ROOT)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
    write('documents', rows)


def get(provider, url, body=None):
    name, _ = base.frozen(provider, url, body)
    prior = OLD / provider / f'{name}.json'
    current = RAW / provider / f'{name}.json'
    if prior.exists():
        p = prior
        response = json.loads(p.read_text())['response']
    else:
        response = base.fetch(provider, url, body)
        p = current
    if p.exists():
        PROVENANCE[str(p.relative_to(ROOT))] = {
            'path': str(p.relative_to(ROOT)), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
            'url': url, 'request': json.dumps(body, sort_keys=True),
            'retrieved_utc': json.loads(p.read_text())['retrieved_utc']}
    return response


def rpc(provider, method, *params):
    response = get(provider, base.RPC[provider], base.rpc_body(method, *params))
    if response.get('error') or response.get('result') is None:
        raise ValueError(f'{provider} {method}: {response.get("error", "null result")}')
    return response['result']


def word(data, offset):
    if offset < 0 or offset + 32 > len(data):
        raise ValueError('ABI word outside input')
    return int.from_bytes(data[offset:offset + 32], 'big')


def dynamic(data, offset):
    size = word(data, offset)
    if offset + 32 + size > len(data):
        raise ValueError('ABI bytes outside input')
    return data[offset + 32:offset + 32 + size]


def decode_execute(value):
    if value[:10] != EXEC:
        raise ValueError('not execute(bytes,bytes[])')
    data = bytes.fromhex(value[10:])
    command_start = word(data, 0)
    start = word(data, 32)
    if command_start < 64 or start < 64 or command_start % 32 or start % 32:
        raise ValueError('invalid ABI dynamic offset')
    commands = dynamic(data, command_start)
    n = word(data, start)
    if n != len(commands) or n > len(data) // 32:
        raise ValueError('command/input length mismatch')
    args = [dynamic(data, start + 32 + word(data, start + 32 + i * 32)) for i in range(n)]
    return commands, args


def addr(data, offset):
    x = word(data, offset)
    if x >= 2**160:
        raise ValueError('noncanonical address')
    return '0x' + f'{x:040x}'


def write(name, rows):
    if not rows:
        return
    fields = list(dict.fromkeys(k for r in rows for k in r))
    with (OUT / f'P3-36_{name}.csv').open('w') as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader(); w.writerows(rows)


def select():
    ledger = ROOT / 'data/processed/P3-29_events.csv'
    PROVENANCE[str(ledger.relative_to(ROOT))] = {
        'path': str(ledger.relative_to(ROOT)), 'sha256': hashlib.sha256(ledger.read_bytes()).hexdigest(),
        'url': '', 'request': 'Derived P3-29 ledger; see data/README.md', 'retrieved_utc': ''}
    with ledger.open() as f:
        rows = list(csv.DictReader(f))
    rows = sorted((r for r in rows if '2026-06-19' <= r['day_utc'] <= '2026-06-30'
                   and r['type'] in ('mint', 'burn')), key=lambda r: (int(r['block']), int(r['log_index'])))
    chosen = {}
    first = set()
    for r in rows:
        reasons = []
        if r['cross_check'] == 'large':
            reasons.append('large_burn')
        key = r['day_utc'], r['type']
        if key not in first:
            reasons.append('first_' + r['type'] + '_of_day'); first.add(key)
        if reasons:
            chosen[(r['tx'], r['log_index'])] = dict(r, selection=';'.join(reasons))
    return list(chosen.values())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--offline', action='store_true')
    parser.add_argument('--smoke', action='store_true')
    parser.add_argument('--documents', action='store_true')
    opts = parser.parse_args()
    base.RAW, base.SUMS, base.OFFLINE = RAW, RAW / 'SHA256SUMS', opts.offline
    RAW.mkdir(parents=True, exist_ok=True)
    if opts.documents:
        documents(opts.offline)
        return
    for bad in ('0x', EXEC, EXEC + '00' * 64):
        try:
            decode_execute(bad)
        except ValueError:
            pass
        else:
            raise AssertionError('malformed input accepted')
    sample = select()
    write('sample', sample)
    if opts.smoke:
        sample = [max((r for r in sample if r['type'] == 'burn'), key=lambda r: int(r['amount_base']))]
    source = get('blockscout', base.REST + '/smart-contracts/' + IMPL)
    assert source['name'] == 'MiniVM' and not source['is_partially_verified']
    contracts = {s['file_path']: s['source_code'] for s in source['additional_sources']}
    constants = {int(v, 16): k for k, v in re.findall(r'uint256 constant (\w+) = (0x[0-9A-Fa-f]+);',
                                                    contracts['contracts/libs/Commands.sol'])}
    assert constants[0] == 'MINT' and constants[1] == 'BURN' and constants[3] == 'TRANSFER'
    assert 'onlyRole(OPERATOR_ROLE)' in source['source_code']
    selectors = {s: rpc('forno', 'web3_sha3', '0x' + s.encode().hex())[:10]
                 for s in ('OPERATOR_ROLE()', 'hasRole(bytes32,address)')}
    operations, cmds, transfers = [], [], []
    for tx_hash in dict.fromkeys(r['tx'] for r in sample):
        selected = [r for r in sample if r['tx'] == tx_hash]
        row = {'tx': tx_hash, 'time_utc': selected[0]['time_utc'],
               'selection': ';'.join(r['selection'] for r in selected),
               'selected_mints_base': sum(int(r['amount_base']) for r in selected if r['type'] == 'mint'),
               'selected_burns_base': sum(int(r['amount_base']) for r in selected if r['type'] == 'burn'),
               'economic_purpose': 'unresolved', 'mechanism': 'unresolved'}
        try:
            tx = rpc('ankr', 'eth_getTransactionByHash', tx_hash)
            receipt = rpc('ankr', 'eth_getTransactionReceipt', tx_hash)
            assert tx['hash'] == receipt['transactionHash'] == tx_hash
            assert receipt['blockHash'] == tx['blockHash'] and int(tx['blockNumber'], 16) == int(selected[0]['block'])
            assert receipt['status'] == '0x1' and receipt['to'].lower() == tx['to'].lower() == VM
            block = tx['blockNumber']
            impls = [rpc(p, 'eth_getStorageAt', VM, base.IMPL_SLOT, block) for p in ('forno', 'ankr')]
            assert impls[0] == impls[1] and '0x' + impls[0][-40:] == IMPL
            # Previous-block check prevents using an implementation installed later in this block.
            before = rpc('forno', 'eth_getStorageAt', VM, base.IMPL_SLOT, hex(int(block, 16) - 1))
            assert before == impls[0]
            deployed = rpc('forno', 'eth_getCode', IMPL, block)
            assert deployed.lower() == source['deployed_bytecode'].lower()
            role = rpc('forno', 'eth_call', {'to': VM, 'data': selectors['OPERATOR_ROLE()']}, block)
            role_call = selectors['hasRole(bytes32,address)'] + role[2:] + tx['from'][2:].rjust(64, '0')
            operator = rpc('forno', 'eth_call', {'to': VM, 'data': role_call}, block)
            assert int(operator, 16) == 1
            brla_role_call = selectors['hasRole(bytes32,address)'] + role[2:] + VM[2:].rjust(64, '0')
            token_operator = rpc('forno', 'eth_call', {'to': base.BRLA, 'data': brla_role_call}, block)
            assert int(token_operator, 16) == 1
            commands, inputs = decode_execute(tx['input'])
            logs = sorted(receipt['logs'], key=lambda x: int(x['logIndex'], 16))
            completed = {int(l['topics'][1], 16): int(l['topics'][2], 16)
                         for l in logs if l['address'].lower() == VM and l['topics'][0] == COMPLETE}
            assert len(completed) == len(commands)
            token_logs = []
            for log in logs:
                if log['topics'][0] == base.TRANSFER and len(log['topics']) == 3:
                    tr = {'tx': tx_hash, 'log_index': int(log['logIndex'], 16), 'token': log['address'].lower(),
                          'from': '0x' + log['topics'][1][-40:], 'to': '0x' + log['topics'][2][-40:],
                          'amount_base': int(log['data'], 16)}
                    transfers.append(tr); token_logs.append(tr)
            for r in selected:
                assert any(t['log_index'] == int(r['log_index']) and t['token'] == base.BRLA
                           and t['amount_base'] == int(r['amount_base']) for t in token_logs)
            decoded, prior_completion, cached = [], -1, 0
            for i, (command, data) in enumerate(zip(commands, inputs)):
                kind = constants.get(command & 0x3f, 'UNKNOWN')
                cr = {'tx': tx_hash, 'command_index': i, 'code': hex(command), 'command': kind,
                      'allow_revert': bool(command & 0x80), 'success': completed[i], 'raw_input': '0x' + data.hex()}
                completion_index = next(int(l['logIndex'], 16) for l in logs if l['address'].lower() == VM
                                        and l['topics'][0] == COMPLETE and int(l['topics'][1], 16) == i)
                actual = [t for t in token_logs if prior_completion < t['log_index'] < completion_index]
                cr['receipt_transfers'] = len(actual)
                if kind in ('MINT', 'BURN', 'TRANSFER'):
                    n = 4 if kind == 'TRANSFER' else 3
                    assert len(data) == n * 32
                    token, a = addr(data, 0), addr(data, 32)
                    b = addr(data, 64) if kind == 'TRANSFER' else (a if kind == 'MINT' else base.ZERO)
                    a = base.ZERO if kind == 'MINT' else a
                    amount = word(data, (n - 1) * 32)
                    cr.update(token=token, from_address=a, to_address=b, amount_argument_base=amount)
                    if amount == MAX - 1:
                        amount = cached
                    if amount == MAX:
                        cr['amount_resolution'] = 'whole_balance_not_independently_resolved'
                        raise ValueError('whole-balance sentinel requires a trace')
                    if completed[i]:
                        assert len(actual) == 1 and (actual[0]['token'], actual[0]['from'], actual[0]['to'],
                                                     actual[0]['amount_base']) == (token, a, b, amount)
                        cached = amount
                    cr['resolved_amount_base'] = amount
                    cr['receipt_matches'] = bool(completed[i])
                else:
                    raise ValueError(f'unhandled command {kind}')
                cmds.append(cr); decoded.append(kind); prior_completion = completion_index
            row.update(sender=tx['from'], proxy=VM, implementation=IMPL, historical_implementation_agrees=True,
                       command_sequence=';'.join(decoded), n_commands=len(commands),
                       n_token_transfers=len(token_logs), tokens=';'.join(sorted({x['token'] for x in token_logs})),
                       mechanism='verified_' + '_then_'.join(decoded).lower(), all_commands_success=all(completed.values()),
                       bytecode_matches_explorer=True, sender_has_operator_role=True, vm_has_brla_operator_role=True)
            print(row['time_utc'], row['selection'], row['command_sequence'], flush=True)
        except (ValueError, AssertionError, KeyError) as exc:
            row['error'] = f'{type(exc).__name__}: {exc}'
            print(tx_hash, row['error'], flush=True)
        operations.append(row)
    suffix = '_smoke' if opts.smoke else ''
    write('operations' + suffix, operations); write('commands' + suffix, cmds); write('transfers' + suffix, transfers)
    write('provenance' + suffix, list(PROVENANCE.values()))
    verified = [r for r in operations if r['mechanism'] != 'unresolved']
    summary = []
    for label, group in [('all', operations), ('large_burn', [r for r in operations if 'large_burn' in r['selection']]),
                         ('control_burn', [r for r in operations if 'first_burn_of_day' in r['selection']]),
                         ('control_mint', [r for r in operations if 'first_mint_of_day' in r['selection']])]:
        summary.append({'group': label, 'transactions': len(group),
                        'verified_mechanism': sum(r['mechanism'] != 'unresolved' for r in group),
                        'economic_purpose_supported': sum(r['economic_purpose'] != 'unresolved' for r in group),
                        'selected_burns_brla': str(sum(Decimal(r['selected_burns_base']) for r in group) / 10**18),
                        'selected_mints_brla': str(sum(Decimal(r['selected_mints_base']) for r in group) / 10**18)})
    write('summary' + suffix, summary)
    print(json.dumps({'transactions': len(operations), 'verified_mechanism': len(verified),
                      'verified_economic_purpose': 0,
                      'selected_burns_brla': str(sum(Decimal(r['selected_burns_base']) for r in operations) / 10**18),
                      'selected_mints_brla': str(sum(Decimal(r['selected_mints_base']) for r in operations) / 10**18)}, indent=2))


if __name__ == '__main__':
    main()
