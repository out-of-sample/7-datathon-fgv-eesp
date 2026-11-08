"""P3-31: Two-Sided Institutional Treasury Decision Framework.
Side 1: Institutional Buyer (BRL -> USDT) acquiring Q=100k USDT by deadline h in {5, 10, 20} PTAX days
        - Strategy B1: Buy Now at t, hold in USD yield instrument (r_USD in {0%, 4%})
        - Strategy B2: Wait in BRL at r_BRL Unhedged, Buy at T
        - Strategy B3: Wait in BRL + buy USD/BRL forward (B3 WDO/DOL or NDF) priced at covered interest parity
          (review fix 6 Nov: the BRL deposit interest pays the forward points, so waiting has no 2.5 bps/day cost)
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
     Linux/macOS: .venv/bin/python scripts/p3_31_holder.py
Review 6 Nov 2026 (Renzo's agent): premiums are read from P1-02 (the first version typed in 142.02/45.73/51.30/29.02,
which match no series); B3 accounting credits BRL interest; the break-even horizon h* was removed (it charged the
forward points without crediting the interest that pays them).
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
R_BRL = .10            # hypothetical net BRL rate, same as the seller scenarios (not CDI)
R_USD_FWD = .05        # USD rate in the forward's CIP pricing (R-07: SOFR ~5.00%)
HEDGE_FEE_BPS = .22    # one-off exchange fee on the hedge notional (R-07: ~2.5 - 2.28 bps on a DOL contract);
                       # ponytail: lower bound, no WDO bid-ask or margin funding; sensitivity in the table


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


def b3_hedged_buyer(q, x0, u0, p0_bps, x1, u1, p1_bps, horizon, rate_brl=R_BRL,
                    rate_usd_fwd=R_USD_FWD, fee=.001, hedge_fee_bps=HEDGE_FEE_BPS, rate_usd_held=0.):
    """Strategy B1 (buy now) vs B3 (keep BRL at rate_brl, buy USD forward at t, buy USDT at T).

    Forward at covered interest parity: F = X_t * A_BRL / A_USD. Hedge notional N fixed at t as the USD
    value of the planned outlay, N = q * U_t * (1 + p_t) * (1 + fee). Terminal BRL (T-reais):
      B1 = buyer_cost(q / A_USDheld, P_t) * A_BRL
      B3 = buyer_cost(q, P_T) - N * (X_T - F) + N * X_t * hedge_fee
    With rate_usd_held = 0 the saving splits exactly into
      usd_carry  = N * X_t * A_BRL * (1 - 1 / A_USD)          (forward is cheaper than spot by the USD rate)
      premium    = q * (1 + fee) * X_T * [U_t (1 + p_t) - U_T (1 + p_T)]   (premium and USDT/USD change)
      hedge_fee  = - N * X_t * hedge_fee
    There is no carry cost: the BRL deposit interest pays the forward points.
    """
    if not all(math.isfinite(v) for v in (x0, u0, p0_bps, x1, u1, p1_bps)):
        raise ValueError('Nonfinite price input')
    a_brl, a_usd = accumulation(rate_brl, horizon), accumulation(rate_usd_fwd, horizon)
    p0 = x0 * u0 * (1 + p0_bps / 1e4)
    p1 = x1 * u1 * (1 + p1_bps / 1e4)
    b1 = buyer_cost(q / accumulation(rate_usd_held, horizon), p0, fee) * a_brl
    fwd = x0 * a_brl / a_usd
    notional = q * u0 * (1 + p0_bps / 1e4) * (1 + fee)
    fee_brl = notional * x0 * hedge_fee_bps / 1e4
    b3 = buyer_cost(q, p1, fee) - notional * (x1 - fwd) + fee_brl
    return dict(b1_terminal_brl=b1, b3_terminal_brl=b3, savings_brl=b1 - b3,
                savings_bps=(b1 - b3) / b1 * 1e4,
                usd_carry_brl=notional * x0 * a_brl * (1 - 1 / a_usd),
                premium_part_brl=q * (1 + fee) * x1 * (u0 * (1 + p0_bps / 1e4) - u1 * (1 + p1_bps / 1e4)),
                hedge_fee_brl=-fee_brl, forward_brl_per_usd=fwd)


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

    def test_b3_hedge_removes_fx(self):
        # Premium and USDT/USD unchanged, zero rates and fees: any FX move nets to zero
        for x1 in (4.5, 5.0, 5.5):
            r = b3_hedged_buyer(Q, 5.0, 1.0, 50., x1, 1.0, 50., 10, rate_brl=0., rate_usd_fwd=0., fee=0., hedge_fee_bps=0.)
            self.assertAlmostEqual(r['savings_brl'], 0., places=6)

    def test_b3_hedge_no_carry_cost(self):
        # Nothing moves and the USDT bought now earns the forward's USD rate: waiting is worth exactly zero,
        # whatever the BRL rate (the BRL interest pays the forward points)
        for rb in (0., .10, .15):
            r = b3_hedged_buyer(Q, 5.0, 1.0, 50., 5.0, 1.0, 50., 20, rate_brl=rb, rate_usd_fwd=.05, fee=0.,
                                hedge_fee_bps=0., rate_usd_held=.05)
            self.assertAlmostEqual(r['savings_brl'], 0., places=6)
        # CIP forward is above spot when BRL rate > USD rate, yet waiting still costs nothing but the USD carry
        r = b3_hedged_buyer(Q, 5.0, 1.0, 50., 5.0, 1.0, 50., 20, rate_brl=.15, rate_usd_fwd=0., fee=0., hedge_fee_bps=0.)
        self.assertGreater(r['forward_brl_per_usd'], 5.0)
        self.assertAlmostEqual(r['savings_brl'], 0., places=6)

    def test_b3_hedge_decomposition(self):
        r = b3_hedged_buyer(Q, 5.19, .9988, 184.35, 5.08, .9991, 45.92, 20)
        self.assertAlmostEqual(r['savings_brl'], r['usd_carry_brl'] + r['premium_part_brl'] + r['hedge_fee_brl'], places=6)
        # Premium compression of ~138 bps, no FX/rates: saving ~ 138 / (1 + p0) bps
        z = b3_hedged_buyer(Q, 5.0, 1.0, 184.35, 5.0, 1.0, 45.92, 5, rate_brl=0., rate_usd_fwd=0., fee=0., hedge_fee_bps=0.)
        self.assertAlmostEqual(z['savings_bps'], (184.35 - 45.92) / (1 + 184.35 / 1e4), places=6)

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

    # 2. Side 1 Buyer: every PTAX day of the window, prices read from P1-02 (review fix)
    buyer_rows = []
    for h in range(1, len(window)):
        last = window.iloc[h]
        args = (Q, x0, u0, b0, last.ptax_sell_brl_per_usd, last.usdtusd_window_usd, last.premium_bps, h)
        b3 = b3_hedged_buyer(*args)
        b3_fee5 = b3_hedged_buyer(*args, hedge_fee_bps=5.)
        b3_usd4 = b3_hedged_buyer(*args, rate_usd_held=.04)
        _, _, b2 = buyer_compare_unhedged(Q, p0, last.usdtbrl_window_brl, R_BRL, h, fee_now=.001, fee_later=.001)
        _, _, b2_usd4 = buyer_compare_unhedged(Q, p0, last.usdtbrl_window_brl, R_BRL, h, fee_now=.001, fee_later=.001, rate_usd=.04)
        _, _, seller = compare(Q, p0, last.usdtbrl_window_brl, R_BRL, h, fee_now=.001, fee_later=.001)
        buyer_rows.append(dict(
            horizon_ptax_days=h, initial_date=str(window.index[0].date()), deadline=str(window.index[h].date()),
            initial_premium_bps=round(b0, 2), final_premium_bps=round(last.premium_bps, 2),
            premium_change_bps=round(b0 - last.premium_bps, 2),
            ptax_change_pct=round((last.ptax_sell_brl_per_usd / x0 - 1) * 100, 3),
            hedged_savings_bps=round(b3['savings_bps'], 2), hedged_savings_brl=round(b3['savings_brl'], 2),
            hedged_premium_part_brl=round(b3['premium_part_brl'], 2), hedged_usd_carry_brl=round(b3['usd_carry_brl'], 2),
            hedged_fee_brl=round(b3['hedge_fee_brl'], 2),
            hedged_savings_brl_fee5bps=round(b3_fee5['savings_brl'], 2),
            hedged_savings_brl_usdt_earns4pct=round(b3_usd4['savings_brl'], 2),
            unhedged_savings_brl=round(b2, 2), unhedged_savings_brl_usdt_earns4pct=round(b2_usd4, 2),
            unhedged_minus_hedged_brl=round(b2 - b3['savings_brl'], 2),
            seller_wait_minus_sell_now_brl=round(seller, 2),
        ))
    buyer_df = pd.DataFrame(buyer_rows)
    buyer_df.to_csv(TABLE / 'P3-31_buyer_hedged_comparison.csv', index=False)
    headline = buyer_df[buyer_df.horizon_ptax_days.isin(HORIZONS)]

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

    # Panel B (review fix): hedged buyer's realised outcome for every possible deadline, not a break-even h*
    ax2.bar(buyer_df.horizon_ptax_days, buyer_df.hedged_savings_bps,
            color=['#2ca02c' if v >= 0 else '#d62728' for v in buyer_df.hedged_savings_bps])
    ax2.axhline(0, color='black', linewidth=0.8)
    ax2.set(xlabel='Prazo em dias úteis PTAX (h), início 25/jun/2026',
            ylabel='Economia de esperar com hedge (pb)',
            title='(B) Comprador (BRL -> USDT) com hedge: resultado realizado por prazo')
    ax2.set_xticks([1, 5, 10, 15, 20])
    ax2.grid(alpha=0.2, axis='y')

    fig.text(0.08, 0.02,
             '100k USDT; custos simétricos de 10 pb; BRL 10% a.a. (cenário). (B): termo a paridade coberta (USD 5%), taxa B3 0,22 pb.\n'
             'Retrospectivo: mostra o que teria acontecido em cada prazo, não uma regra que se pudesse aplicar em 25/jun.',
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

    # Panel B: Buyer realised savings at the three headline horizons (review fix: values from data)
    ax2.plot(headline.horizon_ptax_days, headline.unhedged_savings_brl / 1000, marker='o', color='#2ca02c', lw=2,
             label='B2: esperar sem hedge (inclui a valorização do real)')
    ax2.plot(headline.horizon_ptax_days, headline.hedged_savings_brl / 1000, marker='s', color='#1f77b4', lw=2,
             label='B3: esperar com termo ideal; USDT/USD e residual permanecem')
    ax2.axhline(0, color='black', linewidth=0.8)
    for _, r in headline.iterrows():
        ax2.annotate(f"{r.hedged_savings_bps:+.0f} pb", xy=(r.horizon_ptax_days, r.hedged_savings_brl / 1000),
                     xytext=(0, -14), textcoords='offset points', ha='center', fontsize=8, color='#1f77b4')
    ax2.set(xlabel='Prazo em dias de publicação da PTAX',
            ylabel='Economia ao adiar compra (R$ mil)',
            title='(B) Comprador (BRL -> USDT): resultado realizado ao adiar')
    ax2.set_xticks(HORIZONS)
    ax2.legend(fontsize=8.5, loc='upper left')
    ax2.grid(alpha=0.2)

    fig.text(0.08, 0.02,
             'Início: 25/jun/2026 (primeiro dia útil após o salto de 24/jun). 100k USDT; BRL 10% a.a. (cenário); taxa 10 pb.\n'
             'Retrospectivo: o prêmio subiu de novo em 3/jul; ninguém sabia em 25/jun que ele cairia.',
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
        'b3_hedge_pricing': f'covered interest parity, BRL {R_BRL:.0%} (scenario), USD {R_USD_FWD:.0%} (R-07 SOFR); one-off fee {HEDGE_FEE_BPS} bps (R-07)',
        'review_6nov_renzo_agent': 'h* break-even and typed-in premiums removed; B3 credits BRL interest; all values below computed',
        'initial_premium_bps': round(float(b0), 2),
        'headline_horizons': headline[['horizon_ptax_days', 'deadline', 'final_premium_bps', 'hedged_savings_bps',
                                       'hedged_savings_brl', 'unhedged_savings_brl',
                                       'seller_wait_minus_sell_now_brl']].to_dict('records'),
        'hedged_days_with_loss': buyer_df.loc[buyer_df.hedged_savings_bps < 0, 'deadline'].tolist(),
        'duality_symmetry_factor': 1.001 / .999,
    }
    (TABLE / 'P3-31_audit.json').write_text(json.dumps(audit, indent=2), encoding='utf-8')

    print("=== SELLER THRESHOLDS (Symmetric 10 bps fee) ===")
    print(maincase.to_string(index=False))
    print("\n=== HISTORICAL SELLER COMPARISON (10% BRL rate) ===")
    print(chosen.to_string(index=False))
    print("\n=== TWO-SIDED BUYER & B3 HEDGE COMPARISON ===")
    print(buyer_df.to_string(index=False))
    print(json.dumps(audit, indent=2, default=str))


if __name__ == '__main__':
    main()
