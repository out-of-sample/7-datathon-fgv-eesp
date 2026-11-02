---
id: F-018
title: The Bitcoin premium jumped by the same +93.8 bps on 24 Jun 2026, as triangular arbitrage on Binance requires; the test cannot tell a stablecoin-specific shock from a crypto-wide one
status: confirmed
task: P3-02
date: 2026-11-02
checked_by: Renzo
---

## Claim
After the 23 Jun 2026 BCB notice (E-05), the Brazilian **Bitcoin premium** rose by the same amount as the USDT premium. This is what triangular arbitrage on Binance requires: BTC/BRL ÷ (BTC/USDT × USDT/BRL) stays within 0.4 bps of 1 (mean 0.36 bps, sd 1.07 in 2025–26). So the premium is a price on entering crypto with reais, carried to every BRL pair. The test cannot say whether the notice hit stablecoins only or all crypto. Only placebo p-values are meaningful (see F-016):
- The **USD-adjusted Bitcoin premium** ($P^{\text{BTC}}_{\text{BRL}} / (P^{\text{BTC}}_{\text{USD}} \times \text{PTAX}) - 1$) jumped by **+93.78 bps** ($t = 5.82$, Newey-West HAC $SE = 16.10$ bps, parametric $p = 5.72 \times 10^{-9}$), rising from a 20-day pre-period mean of **14.96 bps** to an acute post-period mean of **108.74 bps**.
- Against an empirical benchmark of **200 random placebo dates** (matching weekday proportions, `seed = 20261102`), no placebo date reached +93.78 bps (placebo range: -56.31 to +62.83 bps, std 18.06 bps). The empirical two-sided and one-sided p-values are both **$p = 1/201 = 0.004975$ ($p < 0.005$, 100th percentile)**.
- Across the entire 2025–2026 period, the daily arbitrage spread between USDT/BRL and BTC/BRL ($\text{USDT}_{\text{premium}} - \text{BTC}_{\text{premium}}$) remained pinned at **$0.28\text{ to }0.46$ bps** (less than half a basis point). During the acute post-event window, the spread shifted by only **+0.13 bps** (from 0.28 bps to 0.40 bps).
- All other 12 Brazilian regulatory events (including the SPSAV virtual asset framework E-02, reporting codes E-04, and eFX overhaul E-06a) produced null results on BTC ($p_{\text{placebo}} \ge 0.2040$), replicating the exact pattern observed for USDT.

## Evidence

### Headline Comparison: USDT/BRL vs BTC/BRL (E-05, 23 Jun 2026)
Evaluated over a 20-PTAX-day pre-window ($[-20, -1]$) and acute post-window ($[+1, +20]$), alongside extended pre-trend ($[-40, -21]$) and after-spike windows ($[+21, +60]$ and $[+21, +71]$):

| Series | Pre-trend [-40, -21] (bps) | Pre [-20, -1] (bps) | Acute [+1, +20] (bps) | Acute Diff (bps) | HAC SE (bps) | $t$-stat | $p$ (Placebo 2S) | Plateau [+21, +60] (bps) | Full Plateau [+21, end] (bps) |
|---|---|---|---|---|---|---|---|---|---|
| **USDT/BRL Premium (P1-02)** | 6.98 | 15.24 | 109.14 | **+93.91** | 16.18 | 5.80 | **0.0050** | 34.54 (+19.31) | 26.78 (+11.54) |
| **BTC/USD Premium (USD-adj)** | 6.62 | 14.96 | 108.74 | **+93.78** | 16.10 | 5.82 | **0.0050** | 34.08 (+19.12) | 26.46 (+11.50) |
| **BTC/USDT Cross (unadj)** | 5.01 | 7.21 | 100.18 | **+92.97** | 15.48 | 6.01 | **0.0050** | 28.59 (+21.38) | 20.45 (+13.24) |
| **Spread: USDT − BTC (USD-adj)** | **0.36** | **0.28** | **0.40** | **+0.13** | 0.08 | 1.62 | 0.8806 | **0.46** | **0.32** |
| **Spread: USDT − BTC (Cross)** | 1.97 | 8.02 | 8.97 | **+0.94** | 1.12 | 0.84 | 0.7413 | 5.95 | 6.32 |

### Event Study Across All 13 Brazilian Regulatory Events (BTC/USD Premium)
Computed with Newey-West HAC standard errors (5 lags) and empirical p-values against 200 random placebo dates:

| Event ID | Kind | Date | $t_0$ PTAX | Pre Mean (bps) | Post Mean (bps) | Diff (bps) | HAC SE | $t$-stat | $p$ (Param) | $p$ (Placebo 2S) | Placebo Pctile | Naive RMSE | Post RMSE | Description |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **E-05** | **eff** | **2026-06-23** | **2026-06-23** | **14.96** | **108.74** | **+93.78** | **16.10** | **5.82** | **$5.7 \times 10^{-9}$** | **0.0050** | **100.0%** | **102.91** | **42.38** | **BCB supervisory notice on fund crypto FX imports** |
| E-01 | ann | 2025-05-22 | 2025-05-22 | 25.90 | 38.94 | +13.04 | 1.97 | 6.62 | $3.5 \times 10^{-11}$ | 0.3731 | 80.5% | 16.62 | 10.30 | Decreto 12.466 (3.5% IOF on official FX) |
| E-01 | eff | 2025-05-23 | 2025-05-23 | 25.30 | 40.33 | +15.03 | 2.20 | 6.82 | $8.8 \times 10^{-12}$ | 0.3234 | 83.5% | 17.60 | 9.15 | Decreto 12.466 effective date |
| E-01b | ann | 2025-06-27 | 2025-06-27 | 38.62 | 15.30 | -23.31 | 5.59 | -4.17 | $3.0 \times 10^{-5}$ | 0.2040 | 9.5% | 30.70 | 19.97 | Decreto Leg. 176/2025 (suspending IOF hike) |
| E-01b | eff | 2025-07-04 | 2025-07-04 | 36.37 | 12.14 | -24.23 | 4.95 | -4.89 | $9.9 \times 10^{-7}$ | 0.2040 | 9.5% | 29.53 | 16.88 | STF ADC 96 injunction (suspending IOF hike) |
| E-02 | ann | 2025-11-10 | 2025-11-10 | 13.05 | 9.04 | -4.01 | 3.82 | -1.05 | 0.294 | 0.6716 | 37.5% | 8.15 | 7.09 | Res. BCB 519-521 (SPSAV framework) |
| E-02 | eff | 2026-02-02 | 2026-02-02 | 7.63 | 4.67 | -2.96 | 1.93 | -1.54 | 0.125 | 0.7214 | 40.5% | 6.32 | 5.59 | SPSAV licensing framework takes effect |
| E-03 | ann | 2026-02-05 | 2026-02-05 | 7.03 | 6.06 | -0.98 | 1.99 | -0.49 | 0.625 | 0.9005 | 51.0% | 6.06 | 5.98 | Draft decree proposal 3.5% crypto IOF |
| E-04 | ann | 2025-11-10 | 2025-11-10 | 13.05 | 9.04 | -4.01 | 3.82 | -1.05 | 0.294 | 0.6716 | 37.5% | 8.15 | 7.09 | Res. BCB 521 Art. 4 reporting codes |
| E-04 | eff | 2026-05-04 | 2026-05-04 | 4.39 | 11.42 | +7.03 | 2.77 | 2.54 | 0.011 | 0.5721 | 74.0% | 11.73 | 9.39 | BCB crypto FX reporting codes take effect |
| E-06a | ann | 2026-04-30 | 2026-04-30 | 4.64 | 10.43 | +5.79 | 3.05 | 1.90 | 0.058 | 0.6219 | 70.5% | 11.19 | 9.57 | Res. BCB 561 (eFX overhaul & stablecoin ban) |
| E-06a | eff | 2026-10-01 | 2026-10-01 | 22.63 | 17.38 | -5.26 | 7.16 | -0.73 | 0.463 | 0.6269 | 33.0% | 21.98 | 21.35 | Res. BCB 561 eFX rules take effect |
| E-06b | ann | 2026-08-07 | 2026-08-07 | 52.95 | 30.84 | -22.11 | 8.03 | -2.76 | 0.006 | 0.2289 | 11.0% | 23.55 | 8.10 | Res. BCB 584 (precautionary hold proposal) |
| E-07 | eff | 2022-06-17 | 2022-06-17 | 53.21 | 48.09 | -5.12 | 7.49 | -0.68 | 0.494 | 0.6318 | 33.5% | 23.02 | 22.45 | Binance abrupt Pix suspension (Capitual) |
| M-01 | eff | 2021-07-26 | 2021-07-26 | 78.65 | 61.88 | -16.77 | 11.69 | -1.44 | 0.151 | 0.2985 | 14.5% | 39.12 | 35.34 | Binance leverage cap & withdrawal limit |
| M-02 | eff | 2024-08-13 | 2024-08-13 | 55.17 | 41.82 | -13.35 | 19.18 | -0.70 | 0.486 | 0.3682 | 17.5% | 23.74 | 19.63 | CVM Binance settlement approval |
| M-03 | eff | 2025-06-27 | 2025-06-27 | 38.62 | 15.30 | -23.31 | 5.59 | -4.17 | $3.0 \times 10^{-5}$ | 0.2040 | 9.5% | 30.70 | 19.97 | Binance 10x tick size cut takes effect |
| M-04 | eff | 2026-07-07 | 2026-07-07 | 70.65 | 60.13 | -10.52 | 28.47 | -0.37 | 0.712 | 0.4527 | 24.0% | 25.63 | 23.37 | Foxbit takes over NovaDAX clients (M-04) |

### Naive Persistence Baseline
- For E-05 on BTC, the naive pre-period persistence baseline yields an RMSE of **102.91 bps** on the post-event window.
- In contrast, modeling the post-regime mean reduces the RMSE to **42.38 bps**, an error reduction of **58.8%** (identical to the 58.8% reduction observed for USDT in F-016).

## Interpretation
- **What it shows:** the jump is not a quirk of the USDT/BRL order book. Any BRL pair on Binance carries the same premium,
  because arbitrageurs close the BTC–USDT–BRL triangle to within about 0.4 bps.
- **What it cannot show:** whether the shock was specific to stablecoins. Even a stablecoin-only shock would move the BTC
  premium through the triangle. A real heterogeneity test needs a price not tied by that arbitrage, for example BTC on a
  domestic venue against a foreign BTC/USD price. That has not been done.
- For the deck: one sentence ("the same premium appears on bitcoin, as arbitrage requires"), not a separate slide.

## Used in deck
One sentence on the robustness slide ("o mesmo prêmio aparece no bitcoin, como a arbitragem exige"); annex table.

## Reproduction
```bash
python scripts/p3_02_btc.py
```
Outputs:
- `data/processed/P3-02_btc_premium_daily.csv`
- `results/tables/P3-02_btc_events.csv`
- `results/figures/P3-02_btc_vs_usdt_premium.png`

## History
- 2026-11-02, agent for Renzo (review fixes, on Felipe's behalf, agreed by Renzo): title, claim and interpretation rewritten; the lockstep follows from triangular arbitrage and cannot confirm a market-wide restriction; slide suggestion reduced to one sentence
- 2026-11-02, Renzo (review, P3-02): reproduces. The lockstep is implied by triangular arbitrage on Binance (USDT-vs-BTC-cross gap 0.36 bps mean, sd 1.07 in 2025–26), so it cannot confirm "market-wide import restrictions"; reword to "a price on entering crypto with reais". Event table re-run with corrected P1-04 dates (tasks/P3-02 → Handoff)
- 2026-11-02: Initial exploratory finding written by Felipe for task P3-02.
