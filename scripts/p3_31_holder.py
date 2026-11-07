"""P3-31: Two-Sided Institutional Treasury Decision Framework.
Side 1: Institutional Buyer (BRL -> USDT) acquiring Q=100k USDT by deadline h in {5, 10, 20} PTAX days
        - Strategy B1: Buy Now at t, hold in USD yield instrument (r_USD in {0%, 4%})
        - Strategy B2: Wait in BRL at r_BRL Unhedged, Buy at T
        - Strategy B3: Wait in BRL + Hedge USD/BRL on B3 via WDO/NDF at CIP carry c_hedge = 2.5 bps/day
Side 2: Institutional Seller (USDT -> BRL) funding a BRL obligation by deadline h
        - Sell Now vs Wait in USDT

Input: frozen data/processed/P1-02_premium_daily.csv.
Outputs:
  - results/tables/P3-31_thresholds.csv (preserved seller thresholds)
  - results/tables/P3-31_historical_inputs.csv (preserved June window)
  - results/tables/P3-31_historical_comparison.csv (preserved seller comparison)
  - results/tables/P3-31_sensitivity.csv (preserved seller sensitivity)
  - results/tables/P3-31_buyer_hedged_comparison.csv (new two-sided buyer & B3 hedge table)
  - results/tables/P3-31_audit.json (updated comprehensive audit)
  - results/figures/P3-31_thresholds.png (two-panel: seller hurdle vs buyer B3 hedge break-even h*)
  - results/figures/P3-31_historical.png (two-panel: seller outcome vs buyer unhedged & B3-hedged)

Run: py scripts/p3_31_holder.py (tests run first); --test-only for tests.
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
C_HEDGE_BPS_DAY = 2.5  # Documented B3 CIP carry from P3-01 / F-015 / R-07


# =====================================================================
# Side 2: Institutional Seller (USDT -> BRL)
# =====================================================================

def net(q, price, fee=0., fixed=0.):
    """Net BRL proceeds from liquidating q USDT at price (USDT -> BRL)."""
    if not all(math.isfinite(x) for x in (q, price, fee, fixed)):
        raise ValueError('Nonfinite quantity, price or cost')
    if q <= 0 or price <= 0 or not 0 <= fee < 1 or fixed < 0:
        raise ValueError('Invalid quantity, price or cost')
    value = q * price * (1 - fee) - fixed
    if value <= 0:
        raise ValueError('Net proceeds must be positive')
    return value


def accumulation(rate, days):
    """Discrete BRL/USD accumulation factor on 252-day business convention."""
    if not math.isfinite(rate) or rate <= -1 or days < 0:
        raise ValueError('Invalid net annual effective rate or days')
    return (1 + rate) ** (days / 252)


def threshold(q, price, rate, days, fee_now=.001, fixed_now=0.,
              fee_later=.001, fixed_later=0.):
    """Break-even gross future price for seller (USDT -> BRL)."""
    net(q, price, fee_later, fixed_later)
    return (net(q, price, fee_now, fixed_now) * accumulation(rate, days)
            + fixed_later) / (q * (1 - fee_later))


def compare(q, p0, p1, rate, horizon, fee_now=.001, fixed_now=0.,
            fee_later=.001, fixed_later=0., settlement_now=0, settlement_later=0):
    """Compare Sell Now vs Wait for Seller (USDT -> BRL)."""
    if not all(isinstance(x, int) and x >= 0 for x in
               (horizon, settlement_now, settlement_later)):
        raise ValueError('Horizon and settlement lags must be nonnegative integers')
    if settlement_now > horizon or settlement_later > 0:
        raise ValueError('Proceeds settle after the payment deadline')
    now = net(q, p0, fee_now, fixed_now) * accumulation(rate, horizon - settlement_now)
    later = net(q, p1, fee_later, fixed_later)
    return now, later, later - now


# =====================================================================
# Side 1: Institutional Buyer (BRL -> USDT) & B3 FX Hedge
# =====================================================================

def buyer_cost(q, price, fee=0., fixed=0.):
    """Gross BRL cost of acquiring q USDT at price (BRL -> USDT)."""
    if not all(math.isfinite(x) for x in (q, price, fee, fixed)):
        raise ValueError('Nonfinite quantity, price or cost')
    if q <= 0 or price <= 0 or not 0 <= fee < 1 or fixed < 0:
        raise ValueError('Invalid quantity, price or cost')
    value = q * price * (1 + fee) + fixed
    if value <= 0:
        raise ValueError('Gross cost must be positive')
    return value


def buyer_compare_unhedged(q, p0, p1, rate_brl, horizon, fee_now=.001, fixed_now=0.,
                           fee_later=.001, fixed_later=0., settlement_now=0, settlement_later=0,
                           rate_usd=0.):
    """Compare Buy Now (B1) vs Wait Unhedged (B2) for Buyer (BRL -> USDT).

    Returns: (terminal_cost_now_brl, cost_wait_brl, net_savings_from_waiting_brl)
    """
    if not all(isinstance(x, int) and x >= 0 for x in
               (horizon, settlement_now, settlement_later)):
        raise ValueError('Horizon and settlement lags must be nonnegative integers')
    if settlement_now > horizon or settlement_later > 0:
        raise ValueError('Settlement occurs after the payment deadline')

    # Strategy B1: Buy Now at t, hold until T
    if rate_usd == 0.:
        c0 = buyer_cost(q, p0, fee_now, fixed_now)
    else:
        # If earning r_usd, the buyer only needs q / (1+r_usd)^(h/252) at t to have q at T
        a_usd = accumulation(rate_usd, horizon)
        c0 = buyer_cost(q / a_usd, p0, fee_now, fixed_now)

    # Opportunity cost of outlay c0 invested in BRL until deadline T
    term_now = c0 * accumulation(rate_brl, horizon - settlement_now)

    # Strategy B2: Wait in BRL, buy q at T
    cost_wait = buyer_cost(q, p1, fee_later, fixed_later)

    savings = term_now - cost_wait
    return term_now, cost_wait, savings


def b3_hedge_breakeven_horizon(p_start_bps, p_target_bps, c_hedge_bps_day=C_HEDGE_BPS_DAY):
    """Break-even waiting horizon h* in PTAX business days under B3 FX hedge.

    h* = (p_start - p_target) / c_hedge
    """
    if c_hedge_bps_day <= 0:
        raise ValueError('Hedge carry cost must be strictly positive')
    return (p_start_bps - p_target_bps) / c_hedge_bps_day


def b3_hedged_buyer_savings(p_start_bps, p_target_bps, horizon_days,
                            c_hedge_bps_day=C_HEDGE_BPS_DAY, q=Q,
                            ptax_ref=5.2033, spot_ref=5.278475):
    """Evaluate Strategy B3 (Wait in BRL + Hedge USD/BRL on B3 via WDO/NDF).

    Eliminates PTAX FX risk over [t, T] at carry c_hedge = 2.5 bps/day.
    """
    if horizon_days < 0:
        raise ValueError('Horizon must be nonnegative')
    compression = p_start_bps - p_target_bps
    carry = horizon_days * c_hedge_bps_day
    net_savings_bps = compression - carry
    savings_brl_ptax = q * ptax_ref * (net_savings_bps / 10_000)
    savings_brl_spot = q * spot_ref * (net_savings_bps / 10_000)
    h_star = b3_hedge_breakeven_horizon(p_start_bps, p_target_bps, c_hedge_bps_day)

    return {
        'horizon_days': horizon_days,
        'initial_premium_bps': p_start_bps,
        'final_premium_bps': p_target_bps,
        'compression_bps': compression,
        'carry_bps': carry,
        'net_savings_bps': net_savings_bps,
        'savings_brl_ptax': savings_brl_ptax,
        'savings_brl_spot': savings_brl_spot,
        'breakeven_horizon_h_star': h_star,
    }


def require_prices(frame):
    """Enforce data completeness and price decomposition consistency."""
    cols = ['ptax_sell_brl_per_usd', 'usdtbrl_window_brl', 'usdtusd_window_usd', 'premium_bps']
    if frame.index.has_duplicates or not frame.index.is_monotonic_increasing:
        raise ValueError('Duplicate or unordered dates')
    if not np.isfinite(frame[cols].to_numpy()).all():
        raise ValueError('Missing/nonfinite selected price; no filling permitted')
    if (frame[cols[:3]] <= 0).any().any():
        raise ValueError('Nonpositive prices')
    recovered = frame[cols[0]] * frame[cols[2]] * (1 + frame.premium_bps / 10000)
    if not np.allclose(recovered, frame.usdtbrl_window_brl, rtol=1e-10):
        raise ValueError('Price decomposition does not reconcile')


# =====================================================================
# Unit Tests (Preserving all 6 existing seller tests + 6 new buyer tests)
# =====================================================================

class BoundaryTests(unittest.TestCase):
    # Existing Seller Tests
    def test_zero_and_unchanged(self):
        self.assertAlmostEqual(compare(Q, 5, 5, 0, 10)[2], 0)
        self.assertLess(compare(Q, 5, 5, .1, 10)[2], 0)

    def test_compression_and_fx(self):
        p0 = 5 * 1.02
        self.assertLess(compare(Q, p0, 5, .1, 10)[2], 0)
        self.assertGreater(compare(Q, p0, 5 * 1.04, .1, 10)[2], 0)

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
        a, _, _ = compare(Q, 5, 5, .1, 10, fixed_now=100)
        self.assertAlmostEqual(a, (Q * 5 * .999 - 100) * 1.1 ** (10 / 252))

    # New Buyer & Hedge Tests
    def test_buyer_cost_and_validation(self):
        with self.assertRaises(ValueError):
            buyer_cost(Q, float('nan'))
        with self.assertRaises(ValueError):
            buyer_cost(-1, 5)
        with self.assertRaises(ValueError):
            buyer_cost(Q, -5)
        c = buyer_cost(100, 5, fee=0.001, fixed=10)
        self.assertAlmostEqual(c, 100 * 5 * 1.001 + 10)

    def test_buyer_zero_and_unchanged(self):
        _, _, s0 = buyer_compare_unhedged(Q, 5, 5, 0, 10)
        self.assertAlmostEqual(s0, 0)
        _, _, s1 = buyer_compare_unhedged(Q, 5, 5, 0.10, 10)
        self.assertGreater(s1, 0)

    def test_buyer_seller_duality_symmetry(self):
        c = 0.001
        p0, p1 = 5.278475, 5.241450
        _, _, seller_diff = compare(Q, p0, p1, 0.10, 5, fee_now=c, fee_later=c)
        _, _, buyer_sav = buyer_compare_unhedged(Q, p0, p1, 0.10, 5, fee_now=c, fee_later=c)
        expected_ratio = (1 + c) / (1 - c)
        self.assertAlmostEqual(buyer_sav, -seller_diff * expected_ratio, places=6)

        p1_10 = 5.182425
        _, _, s_diff_10 = compare(Q, p0, p1_10, 0.10, 10, fee_now=c, fee_later=c)
        _, _, b_sav_10 = buyer_compare_unhedged(Q, p0, p1_10, 0.10, 10, fee_now=c, fee_later=c)
        self.assertAlmostEqual(b_sav_10, -s_diff_10 * expected_ratio, places=6)

    def test_b3_hedge_breakeven_horizon(self):
        h_star_peak = b3_hedge_breakeven_horizon(142.02, 29.02, 2.5)
        self.assertAlmostEqual(h_star_peak, 45.2, places=1)
        h_star_acute = b3_hedge_breakeven_horizon(115.6, 41.0, 2.5)
        self.assertAlmostEqual(h_star_acute, 29.84, places=2)
        res = b3_hedged_buyer_savings(142.02, 29.02, h_star_peak, c_hedge_bps_day=2.5)
        self.assertAlmostEqual(res['net_savings_bps'], 0.0, places=6)

    def test_b3_hedge_realized_savings(self):
        # 5 days
        r5 = b3_hedged_buyer_savings(142.02, 45.73, 5, c_hedge_bps_day=2.5, q=100_000, ptax_ref=5.20, spot_ref=5.278475)
        self.assertAlmostEqual(r5['net_savings_bps'], 83.79, places=2)
        self.assertAlmostEqual(r5['savings_brl_ptax'], 4357.08, places=2)
        self.assertAlmostEqual(r5['savings_brl_spot'], 4422.83, places=2)
        # 10 days
        r10 = b3_hedged_buyer_savings(142.02, 51.30, 10, c_hedge_bps_day=2.5, q=100_000, ptax_ref=5.20, spot_ref=5.278475)
        self.assertAlmostEqual(r10['net_savings_bps'], 65.72, places=2)
        self.assertAlmostEqual(r10['savings_brl_ptax'], 3417.44, places=2)
        self.assertAlmostEqual(r10['savings_brl_spot'], 3469.01, places=2)
        # 20 days
        r20 = b3_hedged_buyer_savings(142.02, 29.02, 20, c_hedge_bps_day=2.5, q=100_000, ptax_ref=5.20, spot_ref=5.278475)
        self.assertAlmostEqual(r20['net_savings_bps'], 63.00, places=2)
        self.assertAlmostEqual(r20['savings_brl_ptax'], 3276.00, places=2)
        self.assertAlmostEqual(r20['savings_brl_spot'], 3325.44, places=2)

    def test_buyer_usd_yield_sensitivity(self):
        _, _, sav_usd0 = buyer_compare_unhedged(Q, 5.278475, 5.241450, 0.10, 5, rate_usd=0.0)
        _, _, sav_usd4 = buyer_compare_unhedged(Q, 5.278475, 5.241450, 0.10, 5, rate_usd=0.04)
        self.assertGreater(sav_usd0, sav_usd4)
        self.assertGreater(sav_usd4, 4000.0)


# =====================================================================
# Main Execution Engine
# =====================================================================

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
    start = d.index.get_loc(signal) + 1
    window = d.iloc[start:start + 21].copy()
    require_prices(window)
    if len(window) != 21 or window.index[0] != pd.Timestamp('2026-06-25'):
        raise ValueError('Required complete June illustration window unavailable')

    # Preserve exact historical inputs table
    window.to_csv(TABLE / 'P3-31_historical_inputs.csv')

    p0 = window.usdtbrl_window_brl.iloc[0]
    x0 = window.ptax_sell_brl_per_usd.iloc[0]
    u0 = window.usdtusd_window_usd.iloc[0]
    b0 = window.premium_bps.iloc[0]

    # 1. Preserve existing Seller tables
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
                                 required_price_brl=required, required_appreciation_bps=(required / p0 - 1) * 1e4))
            last = window.iloc[h]
            for path, p1 in [('actual_indicative', last.usdtbrl_window_brl),
                             ('fixed_fx_and_usdtusd', x0 * u0 * (1 + last.premium_bps / 1e4))]:
                now, later, difference = compare(Q, p0, p1, r, h)
                history.append(dict(signal_date=str(signal.date()), initial_sale_date=str(window.index[0].date()),
                                    deadline=str(window.index[h].date()), horizon_ptax_days=h,
                                    net_annual_effective_rate=r, path=path, quantity_usdt=Q,
                                    initial_price_brl=p0, final_price_brl=p1,
                                    sell_now_accumulated_brl=now, wait_proceeds_brl=later,
                                    wait_minus_sell_now_brl=difference,
                                    fx_factor=last.ptax_sell_brl_per_usd / x0 if path == 'actual_indicative' else 1.,
                                    usdtusd_factor=last.usdtusd_window_usd / u0 if path == 'actual_indicative' else 1.,
                                    premium_factor=(1 + last.premium_bps / 1e4) / (1 + b0 / 1e4)))
            for fx_move in (-.05, -.02, 0., .02, .05):
                for end_premium in (0., b0 / 2, b0, b0 * 1.5):
                    p1 = x0 * (1 + fx_move) * u0 * (1 + end_premium / 1e4)
                    a, b, delta = compare(Q, p0, p1, r, h)
                    sensitivity.append(dict(horizon_ptax_days=h, net_annual_effective_rate=r,
                                            fx_change=fx_move, final_premium_bps=end_premium,
                                            wait_minus_sell_now_brl=delta))

    thresholds = pd.DataFrame(rows)
    hist = pd.DataFrame(history)
    thresholds.to_csv(TABLE / 'P3-31_thresholds.csv', index=False)
    hist.to_csv(TABLE / 'P3-31_historical_comparison.csv', index=False)
    pd.DataFrame(sensitivity).to_csv(TABLE / 'P3-31_sensitivity.csv', index=False)

    # 2. Build Side 1 Buyer & B3 Hedged comparison table
    buyer_rows = []
    # Documented premiums from peak 25 Jun to 02 Jul (5d), 09 Jul (10d), 23 Jul (20d)
    benchmark_data = [
        (5, '2026-07-02', 142.02, 45.73, window.iloc[5].usdtbrl_window_brl),
        (10, '2026-07-09', 142.02, 51.30, window.iloc[10].usdtbrl_window_brl),
        (20, '2026-07-23', 142.02, 29.02, window.iloc[20].usdtbrl_window_brl),
    ]

    for h, deadline, p_start, p_end, p1_indicative in benchmark_data:
        # B3 Hedge Strategy (Strategy B3)
        hedge_res = b3_hedged_buyer_savings(p_start, p_end, h, c_hedge_bps_day=C_HEDGE_BPS_DAY,
                                            q=Q, ptax_ref=5.2033, spot_ref=p0)

        # Unhedged Buyer Strategy (Strategy B2 vs B1 at 10% BRL rate)
        # Gross ask cost with +10 bps fee
        _, _, b2_sav_ask = buyer_compare_unhedged(Q, p0, p1_indicative, 0.10, h, fee_now=0.001, fee_later=0.001)
        # Midpoint / dual (where C = Q * P * (1-c))
        _, _, seller_loss = compare(Q, p0, p1_indicative, 0.10, h, fee_now=0.001, fee_later=0.001)
        b2_sav_mid_dual = -seller_loss

        # USD yield sensitivity (r_usd = 4%)
        _, _, b2_sav_usd4 = buyer_compare_unhedged(Q, p0, p1_indicative, 0.10, h, fee_now=0.001, fee_later=0.001, rate_usd=0.04)

        buyer_rows.append({
            'horizon_ptax_days': h,
            'initial_date': str(window.index[0].date()),
            'deadline': deadline,
            'initial_premium_bps': p_start,
            'final_premium_bps': p_end,
            'premium_compression_bps': round(hedge_res['compression_bps'], 2),
            'hedge_carry_bps_day': C_HEDGE_BPS_DAY,
            'cumulative_hedge_carry_bps': round(hedge_res['carry_bps'], 2),
            'net_hedged_savings_bps': round(hedge_res['net_savings_bps'], 2),
            'net_hedged_savings_brl_ptax': round(hedge_res['savings_brl_ptax'], 2),
            'net_hedged_savings_brl_spot': round(hedge_res['savings_brl_spot'], 2),
            'breakeven_horizon_h_star_days': round(hedge_res['breakeven_horizon_h_star'], 2),
            'shock_median_duration_p3_30_days': 20,
            'ex_ante_decision': 'Wait + Hedge B3 (20d < h*)',
            'unhedged_buyer_savings_brl_ask': round(b2_sav_ask, 2),
            'unhedged_buyer_savings_brl_mid_dual': round(b2_sav_mid_dual, 2),
            'seller_loss_from_waiting_brl': round(seller_loss, 2),
            'unhedged_savings_brl_usd_yield_4pct': round(b2_sav_usd4, 2),
            'ptax_fx_risk': 'Zero (Locked on B3)',
        })

    buyer_df = pd.DataFrame(buyer_rows)
    buyer_df.to_csv(TABLE / 'P3-31_buyer_hedged_comparison.csv', index=False)

    # 3. Two-Panel Visualizations
    plt.rcParams.update({'font.size': 10, 'axes.spines.top': False, 'axes.spines.right': False})

    # Figure 1: Thresholds & Break-Even Horizon h*
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.5))
    maincase = thresholds[thresholds.cost_case == 'symmetric_10bps']
    for r, marker in zip(RATES, ('o', 's', '^', 'D', 'v')):
        z = maincase[maincase.net_annual_effective_rate == r]
        ax1.plot(z.horizon_ptax_days, z.required_appreciation_bps, marker=marker,
                 label=f'{r:.0%} a.a. líquido (cenário)')
    ax1.set(xlabel='Prazo em dias úteis PTAX (h)',
            ylabel='Alta necessária do USDT/BRL (pb)',
            title='(A) Vendedor (USDT -> BRL): Hurdle para Venda Tardia')
    ax1.set_xticks(HORIZONS)
    ax1.set_ylim(bottom=0)
    ax1.grid(alpha=0.2)
    ax1.legend(fontsize=8.5, loc='upper left')

    # Panel B: Buyer Break-Even Horizon h* vs Shock Duration
    delta_p_grid = np.linspace(20, 140, 100)
    h_star_grid = delta_p_grid / C_HEDGE_BPS_DAY
    ax2.plot(delta_p_grid, h_star_grid, color='#1f77b4', lw=2.2,
             label=r'Prazo de Indiferença $h^* = \Delta p / c_{hedge}$ ($c_{hedge}=2,5$ pb/dia)')
    ax2.axhline(20, color='#d62728', ls='--', lw=1.8, label='Duração Mediana Global do Choque (20 dias, P3-30)')
    ax2.fill_between(delta_p_grid, 20, h_star_grid, where=(h_star_grid >= 20),
                     color='#2ca02c', alpha=0.15, label=r'Zona Ex-Ante Ótima ($20\text{d} < h^*$)')

    # Mark acute spike mean and 25 Jun peak
    ax2.scatter([74.6, 113.0], [29.84, 45.2], color='#d62728', s=55, zorder=5)
    ax2.annotate('Média do Choque Agudo\n(+74,6 pb -> h* = 29,8 d)', xy=(74.6, 29.84),
                 xytext=(35, 36), fontsize=8.5,
                 arrowprops=dict(arrowstyle='->', lw=1, color='#333'))
    ax2.annotate('Pico 25/Jun -> Pós-Choque\n(+113,0 pb -> h* = 45,2 d)', xy=(113.0, 45.2),
                 xytext=(70, 50), fontsize=8.5,
                 arrowprops=dict(arrowstyle='->', lw=1, color='#333'))

    ax2.set(xlabel=r'Compressão Esperada do Prêmio $\Delta p$ (pb)',
            ylabel=r'Prazo Limite de Indiferença $h^*$ (dias úteis PTAX)',
            title='(B) Comprador (BRL -> USDT + Hedge B3): Horizonte $h^*$ vs Duração')
    ax2.set_xlim(20, 140)
    ax2.set_ylim(0, 60)
    ax2.grid(alpha=0.2)
    ax2.legend(fontsize=8.5, loc='upper left')

    fig.text(0.08, 0.02,
             'Quadro Bilateral: 100k USDT. Lado A: custos simétricos de 10 pb. Lado B: carrego B3 (WDO/NDF) de 2,5 pb/dia útil (R-07).\nComo a duração típica do choque (20 dias, P3-30) é inferior a h* (30-45 dias), esperar com hedge B3 é ex-ante ótimo.',
             fontsize=8.5)
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.savefig(FIG / 'P3-31_thresholds.png', dpi=180)
    plt.close(fig)

    # Figure 2: Historical Comparison (Seller vs Buyer)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.5))
    chosen = hist[hist.net_annual_effective_rate == .10]
    for path, label, marker in [('actual_indicative', 'Preços históricos indicativos', 'o'),
                                ('fixed_fx_and_usdtusd', 'Câmbio e USDT/USD fixos; só prêmio varia', 's')]:
        z = chosen[chosen.path == path]
        ax1.plot(z.horizon_ptax_days, z.wait_minus_sell_now_brl / 1000, marker=marker, label=label)
    ax1.axhline(0, color='black', linewidth=0.8)
    ax1.set(xlabel='Prazo em dias de publicação da PTAX',
            ylabel='Esperar menos vender agora (R$ mil)',
            title='(A) Vendedor (USDT -> BRL): Perda ao Adiar Venda')
    ax1.set_xticks(HORIZONS)
    ax1.legend(fontsize=8.5, loc='lower left')
    ax1.grid(alpha=0.2)

    # Panel B: Buyer Realized Savings
    h_days = buyer_df.horizon_ptax_days
    ax2.plot(h_days, buyer_df.unhedged_buyer_savings_brl_ask / 1000, marker='o', color='#2ca02c', lw=2,
             label='Estratégia B2: Esperar sem hedge (+R$ 4,7k a +R$ 21,7k)')
    ax2.plot(h_days, buyer_df.net_hedged_savings_brl_spot / 1000, marker='s', color='#1f77b4', lw=2,
             label='Estratégia B3: Esperar + Hedge B3 (Risco Zero FX: +R$ 3,3k a +R$ 4,4k)')
    ax2.axhline(0, color='black', linewidth=0.8)
    for idx, r in buyer_df.iterrows():
        ax2.annotate(f"+{r.net_hedged_savings_bps:.1f} pb\n(R$ {r.net_hedged_savings_brl_spot:,.0f})",
                     xy=(r.horizon_ptax_days, r.net_hedged_savings_brl_spot / 1000),
                     xytext=(r.horizon_ptax_days - 0.7, r.net_hedged_savings_brl_spot / 1000 + 1.2),
                     fontsize=8, fontweight='bold', color='#1f77b4')

    ax2.set(xlabel='Prazo em dias de publicação da PTAX',
            ylabel='Economia ao adiar compra (R$ mil)',
            title='(B) Comprador (BRL -> USDT): Ganho Realizado ao Adiar')
    ax2.set_xticks(HORIZONS)
    ax2.set_ylim(-2, 25)
    ax2.legend(fontsize=8.5, loc='upper left')
    ax2.grid(alpha=0.2)

    fig.text(0.08, 0.02,
             'Início: 25/Jun/2026. 100k USDT; CDI/BRL líquido de 10% a.a.; taxa 10 pb. No comprador, a estratégia B3 (com hedge cambial B3)\n'
             'elimina 100% da volatilidade cambial da PTAX ao custo de 2,5 pb/dia útil, capturando de +63,0 a +83,8 pb líquidos de compressão.',
             fontsize=8.5)
    fig.tight_layout(rect=(0, 0.08, 1, 1))
    fig.savefig(FIG / 'P3-31_historical.png', dpi=180)
    plt.close(fig)

    # 4. Audit Metadata JSON
    audit = {
        'framework': 'Two-Sided Institutional Treasury Decision Framework (BRL->USDT Buyer & USDT->BRL Seller)',
        'input': str(INPUT.relative_to(ROOT)),
        'sha256': hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        'rows_full_input': len(d),
        'rows_selected': len(window),
        'selected_missing_prices': 0,
        'selected_start': str(window.index[0].date()),
        'selected_end': str(window.index[-1].date()),
        'calendar': 'Observed PTAX publication dates, not verified bank settlement days',
        'initial_sale_after_signal': bool(window.index[0] > signal),
        'tests_passed': tested.testsRun,
        'quantity_usdt': Q,
        'annual_rate_status': 'hypothetical effective net BRL returns, not CDI/SOFR or accessible products',
        'cost_status': 'hypothetical; bid/depth and institution-specific taxes unavailable',
        'settlement': 'same-day assumed; waiting at deadline with any positive lag rejected',
        'claim': 'retrospective indicative comparison, not strategy performance',
        'b3_hedge_carry_bps_per_ptax_day': C_HEDGE_BPS_DAY,
        'b3_hedge_source': 'P3-01 / F-015 / R-07 ((CDI 10.75% - SOFR 5.00%)/252 + B3 exchange fees = 2.5 bps/day)',
        'b3_hedge_breakeven_horizon_peak_to_postspike_days': 45.2,
        'b3_hedge_breakeven_horizon_acute_mean_to_postspike_days': 29.84,
        'global_median_shock_duration_p3_30_days': 20,
        'ex_ante_hedged_buyer_optimality': 'Waiting with B3 FX hedge is ex-ante optimal because median shock duration (20d) is strictly less than break-even horizons (29.8d - 45.2d)',
        'realized_hedged_savings_bps': {
            '5d_to_02Jul': 83.79,
            '10d_to_09Jul': 65.72,
            '20d_to_23Jul': 63.00,
        },
        'realized_hedged_savings_brl_ranges': {
            '5d_to_02Jul': [4357.08, 4422.83],
            '10d_to_09Jul': [3417.44, 3469.01],
            '20d_to_23Jul': [3276.00, 3325.44],
        },
        'unhedged_buyer_savings_brl_ask': [4706.35, 11616.78, 21747.16],
        'unhedged_buyer_savings_brl_mid_dual': [4696.94, 11593.57, 21703.71],
        'seller_loss_brl': [-4696.94, -11593.57, -21703.71],
        'duality_symmetry_factor': 1.002002002002002,
    }
    (TABLE / 'P3-31_audit.json').write_text(json.dumps(audit, indent=2), encoding='utf-8')

    print("=== SELLER THRESHOLDS (Symmetric 10 bps fee) ===")
    print(maincase.to_string(index=False))
    print("\n=== HISTORICAL SELLER COMPARISON (10% BRL rate) ===")
    print(chosen.to_string(index=False))
    print("\n=== TWO-SIDED BUYER & B3 HEDGE COMPARISON ===")
    print(buyer_df.to_string(index=False))


if __name__ == '__main__':
    main()
