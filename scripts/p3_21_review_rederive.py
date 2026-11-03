r"""P3-21 review (A): independent re-derivation of U1-U4 with the stdlib only; never imports scripts/p3_21_who_paid.py.
Written by Codex for Renzo (review, 3 Nov 2026), copied from its scratch folder so teammates can re-run it.
Inputs   data/processed/P1-02_premium_daily.csv, results/tables/P3-21_who_paid.csv, results/tables/P3-11_transfer.csv
Output   printed only (windows, monthly values, table comparison, U2 split by purchase date, cover conversions)
Run      python scripts/p3_21_review_rederive.py
Change   3 Nov 2026 (agent for Renzo): registers its own U2 split under the row names the author's CSV now uses
"""
import csv
import hashlib
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean

root = Path(__file__).resolve().parent.parent
source = root / 'data/processed/P1-02_premium_daily.csv'
raw = list(csv.DictReader(source.open()))
assert [r['date_brt'] for r in raw] == sorted(set(r['date_brt'] for r in raw))
data = [(r['date_brt'], float(r['premium_bps']), float(r['ptax_sell_brl_per_usd'])) for r in raw if r['date_brt'] <= '2026-10-30']
assert all(math.isfinite(p) and math.isfinite(f) and f > 0 for _, p, f in data)
t0 = '2026-06-23'
pre = [r for r in data if r[0] < t0][-20:]
spike = [r for r in data if r[0] > t0][:20]
post = [r for r in data if '2026-07-22' <= r[0] <= '2026-10-30']
refs = {'pre-notice (20 days)': mean(r[1] for r in pre), 'post-spike (22 Jul-30 Oct)': mean(r[1] for r in post)}
lookup = {r[0]: r for r in data}
months = defaultdict(list)
for r in data:
    if '2026-01-01' <= r[0] <= '2026-10-30':
        months[r[0][:7]].append(r)
def money(r, usd, reference):
    return usd * r[2] * (r[1] - reference) / 10000
print('sha256', hashlib.sha256(source.read_bytes()).hexdigest())
print('DATA', len(data), data[0][0], data[-1][0])
for name, w in [('pre', pre), ('spike', spike), ('post', post)]:
    print('WINDOW', name, len(w), w[0][0], w[-1][0], 'premium', mean(r[1] for r in w), 'FX', mean(r[2] for r in w))
print('MONTH_PTAX_COUNTS', {m: len(v) for m, v in months.items()})
print('MONTH_DAILY_ALLOCATION', {m: (10000/len(v), sum(10000/len(v) for _ in v)) for m,v in months.items()})
calc = {}
for name, reference in refs.items():
    amounts = [money(r, 100000, reference) for r in spike]
    for stat, value in [('mean', mean(amounts)), ('min', min(amounts)), ('max', max(amounts))]:
        calc['U1', stat, name] = value
    for rule in ['first PTAX day', 'last PTAX day', 'every PTAX day']:
        all_trades = []
        for month, rows in months.items():
            trades = [(rows[0], 10000)] if rule.startswith('first') else [(rows[-1], 10000)] if rule.startswith('last') else [(r, 10000/len(rows)) for r in rows]
            all_trades.extend(trades)
            value = sum(money(r, usd, reference) for r, usd in trades)
            calc['U2', rule + ' ' + month, name] = value
        calc['U2', rule + ' total', name] = sum(money(r, usd, reference) for r, usd in all_trades)
        before = sum(money(r, usd, reference) for r, usd in all_trades if r[0] <= t0)
        after = sum(money(r, usd, reference) for r, usd in all_trades if r[0] > t0)
        print('U2_SPLIT', name, rule, 'through_t0', before, 'after_t0', after, 'total', before+after)
        # added 3 Nov (agent for Renzo): compare the split rows that p3_21_who_paid.py now exports after the review
        calc['U2', rule + ' purchases up to t0', name], calc['U2', rule + ' purchases after t0', name] = before, after
for date, label in [('2026-06-24', 't0+1 (24 Jun)'), ('2026-06-30', 't0+5 (30 Jun)'), ('2026-07-21', 't0+20 (21 Jul)'), ('2026-10-30', '30 Oct (30 Oct)')]:
    calc['U3', 'sells '+label, 'none (vs premium at t0)'] = money(lookup[date], 100000, lookup[t0][1])
for date, label in [('2026-07-21', 't0+20 (21 Jul)'), ('2026-10-30', '30 Oct (30 Oct)')]:
    calc['U4', 'value at '+label, 'none (vs premium at t0+1)'] = money(lookup[date], 100000, lookup['2026-06-24'][1])
for key, value in calc.items():
    print('INDEPENDENT', *key, f'{value:.6f}', 'rounded', round(value), sep=' | ')
stored = list(csv.DictReader((root/'results/tables/P3-21_who_paid.csv').open()))
errors = [abs(calc[r['user'][:2], r['case'], r['counterfactual']] - float(r['brl'])) for r in stored]
assert max(errors) <= 1
print('CSV_COMPARE', len(stored), 'max_abs_error', max(errors), 'rounded_mismatches', sum(round(calc[r['user'][:2], r['case'], r['counterfactual']]) != int(r['brl']) for r in stored))
expected = {'U1': [4842,1895,8824,4249,1308,8227], 'U2': [492,345,402,-104,-251,-192], 'U3':[6802,5487,1407,-2992], 'U4':[-5223,-10070]}
actual = {'U1':[calc['U1', stat, name] for name in refs for stat in ['mean','min','max']], 'U2':[calc['U2', rule+' total',name] for name in refs for rule in ['first PTAX day','last PTAX day','every PTAX day']], 'U3':[v for k,v in calc.items() if k[0]=='U3'], 'U4':[v for k,v in calc.items() if k[0]=='U4']}
for user in expected:
    assert all(abs(x-y)<=1 for x,y in zip(actual[user], expected[user], strict=True))
    print('F033_COMPARE', user, [round(x) for x in actual[user]], 'all_pass')
gap = mean(r[1] for r in spike) - refs['pre-notice (20 days)']
fx = mean(r[2] for r in spike)
daily = calc['U1','mean','pre-notice (20 days)']
fixed = gap*10*5.38
print('COVER', 'gap_bps',gap,'fixed_5.38',fixed,'meanFX_full_gap',gap*10*fx,'rounded_gap_93.9',93.9*10*fx,'daily',daily,'covariance_BRL',daily-gap*10*fx,'gap_percent',100*(daily/fixed-1))
postgap = refs['post-spike (22 Jul-30 Oct)'] - refs['pre-notice (20 days)']
print('AFTER', 'fixed',postgap*10*5.38,'meanFX',postgap*10*mean(r[2] for r in post),'daily',mean(money(r,100000,refs['pre-notice (20 days)']) for r in post))
print('BUY_DAY_PREMIUMS',t0,lookup[t0][1],'2026-06-24',lookup['2026-06-24'][1])
print('U1_extrema',[(r[0], money(r,100000,refs['pre-notice (20 days)'])) for r in spike if money(r,100000,refs['pre-notice (20 days)']) in [min(money(s,100000,refs['pre-notice (20 days)']) for s in spike), max(money(s,100000,refs['pre-notice (20 days)']) for s in spike)]])
print('U5_CITATION',[(r['venue'],r['transfer_brl_mn']) for r in csv.DictReader((root/'results/tables/P3-11_transfer.csv').open()) if r['variant']=='headline: spike, pre 20 days' and r['venue'] in ['Binance','3 venues']])
