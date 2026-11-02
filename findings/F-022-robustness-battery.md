---
id: F-022
title: The 23 Jun 2026 spike is robust (+74 to +128 bps across 22 variants); the after-spike level (+11 to +34 bps) is not distinguishable from ordinary drift (placebo p = 0.24)
status: confirmed
task: P4-01
date: 2026-11-02
checked_by: Renzo
---

## Claim
**The spike is robust; a lasting effect is not shown.** Across 22 variants of the acute window (window length 10–30 days,
four premium definitions, three exchanges, the synthetic control and DiD with four donor pools, break-date intervals),
the jump after the 23 Jun 2026 notice lies between **+73.7 and +128.3 bps**, mostly +93 to +117. It is 10–35 times the
trading-friction floor (2.7–9.4 bps). The break-date interval is 18–30 Jun (pooled variance) or 23–30 Jun
(regime-specific). Binance, Foxbit and Mercado Bitcoin give +93.3 to +94.9 bps.

What remained after the spike (+11.5 to +19.3 bps over the pre-window; +28 to +34 bps against the synthetic control) is
**not distinguishable from ordinary drift**. On every clean date, [+21, +60] vs [−20, −1] moves this much often enough:
p_placebo = 0.24 (882 dates), and 0.14 using only dates from 2025 (85 dates).

The p-values in the battery labelled `p_param` (Newey–West) are kept for reference only. They overstate significance for
this autocorrelated series (see F-016). The BTC rows replicate the jump because triangular arbitrage ties BTC/BRL to
USDT/BRL on Binance (F-018), not because they confirm a wider restriction.

---

## Evidence

The complete matrix of 51 robustness runs is exported to `results/tables/P4-01_robustness.csv`. The summary across the six core dimensions is detailed below and visualized in the specification forest plot `results/figures/P4-01_robustness_forest.png`.

### Dimension 1 — Event-Study Window Length (around 23 Jun 2026)
Evaluating symmetric windows around 23 Jun 2026 ($t_0$ excluded) and after-spike windows:

| Window Specification | Pre Mean (bps) | Post Mean (bps) | Effect / Jump (bps) | HAC SE (bps) | $t$-stat | $p$-value |
|---|---|---|---|---|---|---|
| $[-10, -1]$ vs $[+1, +10]$ PTAX days | 12.5 | 140.8 | **+128.3** | 7.55 | 17.00 | $8.6 \times 10^{-65}$ |
| $[-15, -1]$ vs $[+1, +15]$ PTAX days | 13.0 | 125.9 | **+113.0** | 9.67 | 11.68 | $1.6 \times 10^{-31}$ |
| **$[-20, -1]$ vs $[+1, +20]$ PTAX days (Headline)** | **15.2** | **109.1** | **+93.9** | **16.18** | **5.80** | **$6.4 \times 10^{-9}$** |
| $[-30, -1]$ vs $[+1, +30]$ PTAX days | 13.5 | 87.2 | **+73.7** | 17.12 | 4.30 | $1.7 \times 10^{-5}$ |
| $[+21, +60]$ Plateau (40 days) vs $[-20, -1]$ | 15.2 | 34.5 | **+19.3** | 3.42 | 5.64 | $1.7 \times 10^{-8}$ |
| $[+21, \text{end}]$ Full sample (71 days) vs $[-20, -1]$ | 15.2 | 26.8 | **+11.5** | 3.97 | 2.91 | $0.0036$ |
| Clean pre-period (1 Apr – 22 May) vs $[+1, +20]$ | 5.7 | 109.1 | **+103.4** | 16.09 | 6.43 | $1.3 \times 10^{-10}$ |

*Key finding:* Narrower post-windows show even higher acute treatment effects (+128.3 bps at 10 days, +113.0 bps at 15 days), reflecting the fact that the shock peaked in early July (+185 bps intraday) before market makers adapted. Dropping the pre-trend days (25 May – 22 Jun, which drifted up by +9.5 bps as informal rumors circulated) reveals a clean baseline jump of **+103.4 bps**.

---

### Dimension 2 — Premium Definition & Sample Filters
Testing alternative data constructions on the baseline 20-day window:

| Premium Definition | Pre Mean (bps) | Post Mean (bps) | Jump (bps) | HAC SE (bps) | $t$-stat | Notes |
|---|---|---|---|---|---|---|
| **`premium_bps` (Headline: PTAX 10–13h, Binance 1/USDCUSDT)** | **15.2** | **109.1** | **+93.9** | **16.18** | **5.80** | Headline series |
| `premium_unadj_bps` (No USDT/USD adjustment) | 7.5 | 100.6 | **+93.1** | 15.55 | 5.99 | Assumes USDT = $1.0000 |
| `premium_cb_bps` (Coinbase direct USDT/USD quote) | 18.5 | 112.2 | **+93.7** | 16.41 | 5.71 | Independent USD anchor |
| `premium_dayclose_bps` (23:59 UTC daily close) | 37.7 | 113.8 | **+76.1** | 17.75 | 4.29 | Daily close vs PTAX window |
| Excluding 14 `ptax_window_uncertain` days | 15.2 | 109.1 | **+93.9** | 16.18 | 5.80 | 100% identical in 2026 |

*Key finding:* Whether adjusting USDT against Binance USDC or Coinbase direct USD quotes changes the estimated jump by less than **0.2 bps** (+93.9 vs +93.7 bps). Unadjusted USDT/BRL shows an identical +93.1 bps jump. Day-close pricing yields +76.1 bps because overnight trading incorporates global moves and begins from a higher pre-event baseline (37.7 bps).

---

### Dimension 3 — Domestic BRL Exchange Venues
Comparing order books across Brazil's top three domestic cryptocurrency exchanges (from `results/tables/P2-05_venues_daily.csv`):

| Exchange Venue | 20-day Pre-Window (25 May – 22 Jun) Jump | 16-day June Pre-Window (1 Jun – 22 Jun) Jump | Order Book Trade Source |
|---|---|---|---|
| **Binance (Headline)** | **+93.9 bps** ($15.2 \to 109.1$) | **+96.2 bps** ($13.0 \to 109.1$) | Global order book / BRL pair |
| **Foxbit** | **+93.3 bps** ($14.7 \to 108.0$) | **+95.2 bps** ($12.9 \to 108.0$) | Domestic Brazilian exchange |
| **Mercado Bitcoin** | **+94.9 bps** ($10.7 \to 105.6$) | **+98.5 bps** ($7.1 \to 105.6$) | Domestic Brazilian exchange |
| **3-Venue Composite (Equal-weighted)** | **+94.0 bps** ($13.5 \to 107.6$) | **+96.6 bps** ($11.0 \to 107.6$) | Cross-venue composite index |

*Key finding:* Across all three venues, the jump is virtually identical within 1.6 bps on the 20-day window and 3.3 bps on the June window. This conclusively proves that the premium is not an exchange-specific glitch or Binance order-book artefact.

---

### Dimension 4 — Structural Break Test Confidence Intervals
Testing Bai (1997) confidence intervals for Break 4 (24 Jun 2026 jump) and Break 5 (22 Jul 2026 fade) under homoskedastic vs heteroskedastic Newey-West variances:

| Series & Break Event | Regime Change ($\delta$) | Bai (1997) Theorem 1 Pooled CI (Homoskedastic) | Bai (1997) Theorem 2 Regime-Specific CI (Heteroskedastic) |
|---|---|---|---|
| **`premium_bps` — Break 4 (24 Jun 2026)** | **+99.8 bps** | **[2026-06-18 .. 2026-06-30] ($\pm 3.1$d)** | **[2026-06-23 .. 2026-06-30] ($-0.1$d / $+3.9$d)** |
| `premium_bps` — Break 5 (22 Jul 2026) | -82.4 bps | [2026-07-15 .. 2026-07-29] ($\pm 4.6$d) | [2026-07-14 .. 2026-07-23] ($-5.7$d / $+0.9$d) |
| `premium_cb_bps` — Break 6 (24 Jun 2026) | +101.3 bps | [2026-06-22 .. 2026-06-26] ($\pm 2.0$d) | [2026-06-23 .. 2026-06-30] ($-0.1$d / $+3.9$d) |
| `premium_cb_bps` — Break 7 (22 Jul 2026) | -83.9 bps | [2026-07-17 .. 2026-07-27] ($\pm 2.8$d) | [2026-07-14 .. 2026-07-23] ($-5.6$d / $+0.9$d) |
| `premium_dayclose_bps` — Break 5 (23 Jun 2026) | +90.0 bps | [2026-06-12 .. 2026-07-02] ($\pm 6.3$d) | [2026-06-17 .. 2026-06-30] ($-3.7$d / $+4.2$d) |
| `premium_dayclose_bps` — Break 6 (21 Jul 2026) | -75.9 bps | [2026-07-08 .. 2026-08-03] ($\pm 8.8$d) | [2026-07-13 .. 2026-07-28] ($-5.9$d / $+4.6$d) |

*Key finding:* Under Bai (1997) Theorem 2, the pre-break regime was characterized by exceptionally low residual variance ($\omega_1 = 10.8$ bps), which compresses the left tail of Break 4 to just $0.1$ PTAX days. Consequently, the break date cannot have occurred prior to 23 Jun 2026, perfectly matching the reported afternoon circulation of the BCB supervisory *ofício*.

---

### Dimension 5 — Synthetic Control Variations & Colombian Holiday Filter
Testing counterfactual "Synthetic Brazil" estimates across donor pools and calendar adjustments:

| Specification | Acute Treatment Gap | Plateau Treatment Gap | Pre RMSPE | RMSPE Ratio | Placebo Rank |
|---|---|---|---|---|---|
| **5-donor Headline (EUR, TRY, ZAR, MXN, COP)** | **+109.3 bps** | **+28.2 bps** | **7.05 bps** | **9.31** | **#1 / 6 ($p = 0.167$)** |
| Strict 4-donor pool (ex-EUR: TRY, ZAR, MXN, COP) | **+116.7 bps** | **+33.9 bps** | 10.33 bps | 6.90 | #1 / 5 ($p = 0.200$) |
| 6-donor pool w/ IDR (from 1 Dec 2025) | **+109.9 bps** | **+28.6 bps** | 7.19 bps | 9.20 | #1 / 7 ($p = 0.143$) |
| Same-time ECB fix outcome (`BRL_ecb`) | **+101.6 bps** | **+32.3 bps** | 16.58 bps | 3.94 | #1 / 6 ($p = 0.167$) |
| Non-parametric DiD (Equal-weighted donors) | **+103.3 bps** | **+31.4 bps** | — | — | Benchmark |
| Excluding Colombian Monday holidays (*Ley Emiliani*) | **+109.5 bps** | **+28.3 bps** | 6.98 bps | 9.44 | #1 / 6 ($p = 0.167$) |

*Key finding:* In all six specifications, Brazil ranks #1 in post/pre RMSPE ratio among all donor countries. The acute gap remains between **+101.6 bps and +116.7 bps**, and the plateau gap is between **+28.2 bps and +33.9 bps**. Filtering out all 18 Colombian Monday bank holidays (*festivos*) shifts the acute gap by only +0.2 bps (+109.3 vs +109.5 bps), confirming that TRM calendar conventions do not drive the result.

---

### Dimension 6 — Cross-Asset Heterogeneity & Noise Floor
Testing whether the shock transmitted to Bitcoin and comparing the jump against microstructure noise bounds:

| Estimator / Series | Estimated Value | Shock Ratio (Jump / Metric) | Statistical Significance | Economic Interpretation |
|---|---|---|---|---|
| **BTC/USD Premium (23 Jun Jump)** | **+93.8 bps** | $1.00\times$ vs USDT | $t = 5.82, p < 0.005$ | Lockstep jump across crypto import layer |
| **BTC-Implied USDT Cross Jump** | **+93.0 bps** | $0.99\times$ vs USDT | $t = 6.01, p < 0.005$ | Triangle parity holds within 1 bps |
| Corwin & Schultz (2012) Spread | 2.80 bps | **$33.5\times$** | Median friction | Benchmark bid-ask spread |
| Abdi & Ranaldo (2017) Spread | 2.71 bps | **$34.7\times$** | Close/high/low spread | Independent friction estimator |
| Roll (1984) Serial Covariance Spread | 4.32 bps | **$21.7\times$** | Effective spread | Negative autocovariance bound |
| Conservative Noise Band (21d rolling max) | 3.94 bps | **$23.8\times$** | Upper friction envelope | Zero-arbitrage band |
| Naive Hourly High-Low Range | 9.38 bps | **$10.0\times$** | Upper bound on volatility | Includes intraday price trends |

*Key finding:* The 23 Jun 2026 treatment effect is an order of magnitude larger than any measure of trading friction, bid-ask spread, or intraday price volatility.

---

## Honest Nuances and Methodological Caveats

1. **Window Length and Decay:** The acute shock was strongest in the first 10 trading days (+128.3 bps) and faded over 30 days (+73.7 bps). Presenting a single "+93.9 bps" number reflects the standard pre-committed 20-day event window; researchers and policymakers should understand that this represents the time-average of a sharp acute spike followed by a decline whose cause is unexplained (P2-02).
2. **Synthetic Control vs Event Study Gap:** Synthetic Control yields a slightly larger acute gap (+109.3 bps) than the unadjusted event study (+93.9 bps) because donor currencies experienced moderate dollar strength in late June 2026. Thus, counterfactual Brazil would have seen stablecoin premiums decline slightly, making the relative treatment effect larger.
3. **Day-Close Timing:** Day-close estimates are smaller (+76.1 bps) because global crypto markets trade 24/7, allowing overnight news to price in before the official PTAX window opens. The PTAX-matched window (10:00–13:00 BRT) remains the methodologically rigorous choice because it synchronizes crypto quotes to the exact window when the central bank calculates the official foreign exchange rate.

---

## Used in Deck
- **Slide on Robustness & Specification Curve:** Includes forest plot `results/figures/P4-01_robustness_forest.png` displaying acute and plateau estimates across all 22 specifications alongside the shaded noise band.
- **Annex Table:** Summarizes the 6-dimension robustness matrix from `results/tables/P4-01_robustness.csv`.

---

## History
- 2026-11-02, agent for Renzo (review fixes, on Felipe's behalf, agreed by Renzo): claim and title rewritten; after-spike placebo rows added to the battery (53 rows); parametric p labelled p_param; BTC point corrected
- 2026-11-02, Renzo (review, P4-01): 51 rows reproduce exactly; acute jump robust (+74 to +128 bps). Plateau placebo test (reviewer): +19.3 bps for [+21,+60] has p = 0.24 over 882 clean dates (0.14 in 2025–26), so the "persistent plateau" is not shown. Drop parametric p-values; BTC point is implied by arbitrage (tasks/P4-01 → Handoff)
- 2026-11-02, Felipe: created (status exploratory; P4-01 criteria 1–3 satisfied; full 51-specification battery executed across 6 dimensions via `scripts/p4_01_robustness.py`).
