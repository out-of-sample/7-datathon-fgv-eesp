"""P3-31: conditional holder comparison, not an executable trading backtest.
Input: frozen data/processed/P1-02_premium_daily.csv. Outputs: P3-31 tables/figures.
Run: python scripts/p3_31_holder.py (tests run first); --test-only for tests.
Net annual effective return and fees are hypothetical scenarios, not quoted products.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
import unittest
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / 'data/processed/P1-02_premium_daily.csv'
TABLE = ROOT / 'results/tables'
FIG = ROOT / 'results/figures'
Q = 100_000
HORIZONS = (5, 10, 20)
RATES = (0., .05, .10, .15, .20)


def net(q, price, fee=0., fixed=0.):
    if not all(math.isfinite(x) for x in (q, price, fee, fixed)):
        raise ValueError('Nonfinite quantity, price or cost')
    if q <= 0 or price <= 0 or not 0 <= fee < 1 or fixed < 0:
        raise ValueError('Invalid quantity, price or cost')
    value = q * price * (1-fee) - fixed
    if value <= 0:
        raise ValueError('Net proceeds must be positive')
    return value


def accumulation(rate, days):
    if not math.isfinite(rate) or rate <= -1 or days < 0:
        raise ValueError('Invalid net annual effective rate or days')
    return (1+rate)**(days/252)


def threshold(q, price, rate, days, fee_now=.001, fixed_now=0.,
              fee_later=.001, fixed_later=0.):
    # Validate future cost parameters as well as initial net proceeds.
    net(q, price, fee_later, fixed_later)
    return (net(q, price, fee_now, fixed_now)*accumulation(rate, days)
            + fixed_later)/(q*(1-fee_later))


def compare(q, p0, p1, rate, horizon, fee_now=.001, fixed_now=0.,
            fee_later=.001, fixed_later=0., settlement_now=0, settlement_later=0):
    if not all(isinstance(x, int) and x >= 0 for x in
               (horizon, settlement_now, settlement_later)):
        raise ValueError('Horizon and settlement lags must be nonnegative integers')
    # Later sale is at deadline by definition. Do not silently shift its execution.
    if settlement_now > horizon or settlement_later > 0:
        raise ValueError('Proceeds settle after the payment deadline')
    now = net(q, p0, fee_now, fixed_now)*accumulation(rate, horizon-settlement_now)
    later = net(q, p1, fee_later, fixed_later)
    return now, later, later-now


def require_prices(frame):
    cols = ['ptax_sell_brl_per_usd', 'usdtbrl_window_brl', 'usdtusd_window_usd', 'premium_bps']
    if frame.index.has_duplicates or not frame.index.is_monotonic_increasing:
        raise ValueError('Duplicate or unordered dates')
    if not np.isfinite(frame[cols].to_numpy()).all():
        raise ValueError('Missing/nonfinite selected price; no filling permitted')
    if (frame[cols[:3]] <= 0).any().any():
        raise ValueError('Nonpositive prices')
    recovered = frame[cols[0]] * frame[cols[2]] * (1+frame.premium_bps/10000)
    if not np.allclose(recovered, frame.usdtbrl_window_brl, rtol=1e-10):
        raise ValueError('Price decomposition does not reconcile')


class BoundaryTests(unittest.TestCase):
    def test_zero_and_unchanged(self):
        self.assertAlmostEqual(compare(Q, 5, 5, 0, 10)[2], 0)
        self.assertLess(compare(Q, 5, 5, .1, 10)[2], 0)

    def test_compression_and_fx(self):
        p0 = 5*1.02
        self.assertLess(compare(Q, p0, 5, .1, 10)[2], 0)
        self.assertGreater(compare(Q, p0, 5*1.04, .1, 10)[2], 0)

    def test_unequal_cost_identity(self):
        p1 = threshold(Q, 5, .15, 20, .001, 50, .004, 100)
        self.assertAlmostEqual(compare(Q, 5, p1, .15, 20, .001, 50, .004, 100)[2], 0, places=7)

    def test_missing(self):
        with self.assertRaises(ValueError):
            net(Q, float('nan'))

    def test_late_settlement(self):
        with self.assertRaises(ValueError):
            compare(Q, 5, 5, .1, 10, settlement_later=1)
        with self.assertRaises(ValueError):
            compare(Q, 5, 5, .1, 10, settlement_now=11)
        self.assertAlmostEqual(compare(Q, 5, 5, .1, 10, settlement_now=10)[2], 0)

    def test_cost_order(self):
        # Fixed charge is deducted before investing, not at the end.
        a, _, _ = compare(Q, 5, 5, .1, 10, fixed_now=100)
        self.assertAlmostEqual(a, (Q*5*.999-100)*1.1**(10/252))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test-only', action='store_true')
    args = parser.parse_args()
    tested = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(BoundaryTests))
    if not tested.wasSuccessful():
        raise SystemExit(1)
    if args.test_only:
        return
    TABLE.mkdir(parents=True, exist_ok=True)
    FIG.mkdir(parents=True, exist_ok=True)
    d = pd.read_csv(INPUT, parse_dates=['date_brt']).set_index('date_brt')
    signal = pd.Timestamp('2026-06-24')
    start = d.index.get_loc(signal)+1
    window = d.iloc[start:start+21].copy()
    require_prices(window)
    if len(window) != 21 or window.index[0] != pd.Timestamp('2026-06-25'):
        raise ValueError('Required complete June illustration window unavailable')
    # PTAX-observed calendar, not a bank settlement calendar. No filling or skipping null rows.
    window.to_csv(TABLE / 'P3-31_historical_inputs.csv')
    p0 = window.usdtbrl_window_brl.iloc[0]
    x0 = window.ptax_sell_brl_per_usd.iloc[0]
    u0 = window.usdtusd_window_usd.iloc[0]
    b0 = window.premium_bps.iloc[0]
    rows, history, sensitivity = [], [], []
    cost_cases = [('symmetric_10bps', .001, 0., .001, 0.),
                  ('zero_cost', 0., 0., 0., 0.),
                  ('later_30bps_fixed100', .001, 0., .003, 100.),
                  ('now_30bps_fixed100', .003, 100., .001, 0.)]
    for h in HORIZONS:
        for r in RATES:
            for case, c0, f0, c1, f1 in cost_cases:
                required = threshold(Q, p0, r, h, c0, f0, c1, f1)
                rows.append(dict(horizon_ptax_days=h, net_annual_effective_rate=r,
                                 cost_case=case, quantity_usdt=Q, initial_price_brl=p0,
                                 fee_now=c0, fixed_now_brl=f0, fee_later=c1, fixed_later_brl=f1,
                                 required_price_brl=required, required_appreciation_bps=(required/p0-1)*1e4))
            last = window.iloc[h]
            for path, p1 in [('actual_indicative', last.usdtbrl_window_brl),
                             ('fixed_fx_and_usdtusd', x0*u0*(1+last.premium_bps/1e4))]:
                now, later, difference = compare(Q, p0, p1, r, h)
                history.append(dict(signal_date=str(signal.date()), initial_sale_date=str(window.index[0].date()),
                                    deadline=str(window.index[h].date()), horizon_ptax_days=h,
                                    net_annual_effective_rate=r, path=path, quantity_usdt=Q,
                                    initial_price_brl=p0, final_price_brl=p1,
                                    sell_now_accumulated_brl=now, wait_proceeds_brl=later,
                                    wait_minus_sell_now_brl=difference,
                                    fx_factor=last.ptax_sell_brl_per_usd/x0 if path=='actual_indicative' else 1.,
                                    usdtusd_factor=last.usdtusd_window_usd/u0 if path=='actual_indicative' else 1.,
                                    premium_factor=(1+last.premium_bps/1e4)/(1+b0/1e4)))
            for fx_move in (-.05, -.02, 0., .02, .05):
                for end_premium in (0., b0/2, b0, b0*1.5):
                    p1=x0*(1+fx_move)*u0*(1+end_premium/1e4)
                    a,b,delta=compare(Q,p0,p1,r,h)
                    sensitivity.append(dict(horizon_ptax_days=h, net_annual_effective_rate=r,
                                            fx_change=fx_move, final_premium_bps=end_premium,
                                            wait_minus_sell_now_brl=delta))
    thresholds=pd.DataFrame(rows); hist=pd.DataFrame(history)
    thresholds.to_csv(TABLE/'P3-31_thresholds.csv', index=False)
    hist.to_csv(TABLE/'P3-31_historical_comparison.csv', index=False)
    pd.DataFrame(sensitivity).to_csv(TABLE/'P3-31_sensitivity.csv', index=False)
    plt.rcParams.update({'font.size':11, 'axes.spines.top':False, 'axes.spines.right':False})
    fig,ax=plt.subplots(figsize=(9,5.8))
    maincase=thresholds[thresholds.cost_case=='symmetric_10bps']
    for r, marker in zip(RATES, ('o','s','^','D','v')):
        z=maincase[maincase.net_annual_effective_rate==r]
        ax.plot(z.horizon_ptax_days,z.required_appreciation_bps,marker=marker,label=f'{r:.0%} a.a. líquido (cenário)')
    ax.set(xlabel='Prazo em dias de publicação da PTAX', ylabel='Alta necessária do preço USDT/BRL (pb)',
           title='Quanto o USDT precisa subir para compensar a espera?')
    ax.set_xticks(HORIZONS); ax.set_ylim(bottom=0); ax.grid(alpha=.2); ax.legend(fontsize=9)
    fig.text(.1,.025,'100 mil USDT; taxa efetiva / 252 dias; custos simétricos de 10 pb; liquidação imediata.\nCenários hipotéticos, não retornos de produtos disponíveis.',fontsize=9)
    fig.tight_layout(rect=(0,.09,1,1)); fig.savefig(FIG/'P3-31_thresholds.png',dpi=180); plt.close(fig)
    fig,ax=plt.subplots(figsize=(9,5.8))
    chosen=hist[hist.net_annual_effective_rate==.10]
    for path,label,marker in [('actual_indicative','Preços históricos indicativos','o'),
                              ('fixed_fx_and_usdtusd','Câmbio e USDT/USD fixos; só prêmio varia','s')]:
        z=chosen[chosen.path==path]
        ax.plot(z.horizon_ptax_days,z.wait_minus_sell_now_brl/1000,marker=marker,label=label)
    ax.axhline(0,color='black',linewidth=.8)
    ax.set(xlabel='Prazo em dias de publicação da PTAX',ylabel='Esperar menos converter agora (R$ mil)',
           title='Junho de 2026: comparação retrospectiva de um detentor')
    ax.set_xticks(HORIZONS); ax.legend(fontsize=9); ax.grid(alpha=.2)
    fig.text(.1,.025,'Sinal: 24/6; preço inicial: 25/6. 100 mil USDT; rendimento BRL hipotético de 10% a.a. líquido.\nCustos simétricos de 10 pb; liquidação imediata. Não é lucro executável nem teste de estratégia.',fontsize=9)
    fig.tight_layout(rect=(0,.09,1,1)); fig.savefig(FIG/'P3-31_historical.png',dpi=180); plt.close(fig)
    audit={'input':str(INPUT.relative_to(ROOT)), 'sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),
           'rows_full_input':len(d), 'rows_selected':len(window), 'selected_missing_prices':0,
           'selected_start':str(window.index[0].date()), 'selected_end':str(window.index[-1].date()),
           'calendar':'Observed PTAX publication dates, not verified bank settlement days',
           'initial_sale_after_signal':bool(window.index[0]>signal), 'tests_passed':tested.testsRun,
           'annual_rate_status':'hypothetical effective net BRL returns, not CDI/SOFR or accessible products',
           'cost_status':'hypothetical; bid/depth and institution-specific taxes unavailable',
           'settlement':'same-day assumed; waiting at deadline with any positive lag rejected',
           'claim':'retrospective indicative comparison, not strategy performance'}
    (TABLE/'P3-31_audit.json').write_text(json.dumps(audit,indent=2),encoding='utf-8')
    print(maincase.to_string(index=False))
    print(chosen.to_string(index=False))


if __name__=='__main__':
    main()
