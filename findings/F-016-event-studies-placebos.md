---
id: F-016
title: Before/after event study on all 13 Brazilian events finds only the 23 Jun 2026 BCB notice moved the premium (+93.9 bps, p < 0.005 vs 200 placebos)
status: exploratory
task: P2-03
date: 2026-11-02
checked_by: -
---

## Claim
Testing 20-PTAX-day windows before and after every dated Brazilian regulatory and microstructure event (13 events from P1-04, evaluating both effective and announcement dates) shows that **only one event produced an anomalous shift in the USDT/BRL premium**: the **23 Jun 2026 BCB supervisory ofício** (E-05), which jumped by **+93.9 bps** ($t = 5.80$, Newey-West HAC $SE = 16.2$ bps, parametric $p = 6.44 \times 10^{-9}$).

Against an empirical benchmark of **200 random placebo dates** sampled from clean non-event trading days (matching weekday proportions, seed = 20261102), **no placebo date reached +93.9 bps** (placebo range: -57.5 to +62.7 bps; mean -0.55, std 18.0 bps). The empirical two-sided and one-sided p-values for 23 Jun 2026 are both **$p = 1/201 = 0.004975$ ($p < 0.005$, 100th percentile)**.

All other formal, public regulations (the SPSAV virtual asset framework E-02, the eFX overhaul E-06a, mandatory BCB reporting codes E-04, and the 3.5% crypto IOF proposal E-03) produced changes between -5.3 bps and +7.2 bps, completely indistinguishable from normal trading noise ($p_{\text{placebo}} \ge 0.58$).

## Evidence

### Event Table (Headline Summary)
Computed with 20 PTAX trading days before ($[-20, -1]$) and 20 trading days after ($[+1, +20]$) around $t_0$, omitting event day $t_0$. Newey-West HAC standard errors use a Bartlett kernel with 5 lags. Placebo p-values are based on 200 clean non-event draws:

| Event ID | Date Kind | Event Date | $t_0$ PTAX | Pre Mean (bps) | Post Mean (bps) | Diff (bps) | HAC SE | $t$-stat | $p$ (Param) | $p$ (Placebo 2S) | Placebo Pctile | Naive RMSE | Post RMSE | Description |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **E-05** | **effective** | **2026-06-23** | **2026-06-23** | **15.2** | **109.1** | **+93.9** | **16.2** | **5.80** | **$6.4 \times 10^{-9}$** | **0.0050** | **100.0%** | **103.1** | **42.5** | **BCB supervisory ofício on crypto FX fund structures** |
| E-01 | announcement | 2025-05-22 | 2025-05-22 | 26.9 | 40.1 | +13.2 | 2.0 | 6.75 | $1.4 \times 10^{-11}$ | 0.3731 | 81.0% | 17.0 | 10.8 | Decreto 12.466 (3.5% IOF on official FX) |
| E-01 | effective | 2025-05-23 | 2025-05-23 | 26.2 | 41.7 | +15.4 | 2.2 | 7.09 | $1.4 \times 10^{-12}$ | 0.3134 | 84.0% | 18.1 | 9.4 | Decreto 12.466 effective date |
| E-01b | announcement | 2025-06-27 | 2025-06-27 | 39.9 | 16.0 | -23.9 | 5.5 | -4.31 | $1.6 \times 10^{-5}$ | 0.1990 | 9.0% | 31.1 | 19.9 | Decreto Leg. 176/2025 (suspending IOF hike) |
| E-01b | effective | 2025-07-04 | 2025-07-04 | 37.6 | 12.7 | -24.9 | 4.9 | -5.09 | $3.6 \times 10^{-7}$ | 0.1940 | 8.5% | 29.9 | 16.6 | STF ADC 96 injunction (suspending IOF hike) |
| E-02 | announcement | 2025-11-10 | 2025-11-10 | 13.2 | 9.5 | -3.8 | 3.9 | -0.97 | 0.330 | 0.6716 | 37.5% | 8.6 | 7.7 | Res. BCB 519-521 (SPSAV framework) |
| E-02 | effective | 2026-02-02 | 2026-02-02 | 8.4 | 4.1 | -4.3 | 1.7 | -2.57 | 0.010 | 0.6567 | 36.0% | 6.9 | 5.4 | SPSAV licensing framework takes effect |
| E-03 | announcement | 2026-02-05 | 2026-02-05 | 7.6 | 5.5 | -2.1 | 1.9 | -1.10 | 0.270 | 0.7861 | 43.5% | 6.2 | 5.9 | Draft decree proposal 3.5% crypto IOF |
| E-04 | announcement | 2025-11-10 | 2025-11-10 | 13.2 | 9.5 | -3.8 | 3.9 | -0.97 | 0.330 | 0.6716 | 37.5% | 8.6 | 7.7 | Res. BCB 521 Art. 4 reporting codes |
| E-04 | effective | 2026-05-04 | 2026-05-04 | 4.6 | 11.9 | +7.2 | 2.9 | 2.48 | 0.013 | 0.5771 | 73.5% | 12.1 | 9.7 | BCB crypto FX reporting codes take effect |
| E-06a | announcement | 2026-04-30 | 2026-04-30 | 4.9 | 10.9 | +6.0 | 3.2 | 1.91 | 0.056 | 0.6070 | 72.0% | 11.5 | 9.8 | Res. BCB 561 (eFX overhaul & stablecoin ban) |
| E-06a | effective | 2026-10-01 | 2026-10-01 | 22.8 | 17.5 | -5.3 | 7.2 | -0.74 | 0.460 | 0.6368 | 34.0% | 22.0 | 21.4 | Res. BCB 561 eFX rules take effect |
| E-06b | announcement | 2026-08-07 | 2026-08-07 | 53.3 | 31.3 | -22.0 | 8.0 | -2.74 | 0.006 | 0.2189 | 10.5% | 23.5 | 8.2 | Res. BCB 584 (precautionary hold proposal) |
| E-07 | effective | 2022-06-17 | 2022-06-17 | 53.2 | 48.5 | -4.7 | 7.7 | -0.61 | 0.542 | 0.6468 | 35.0% | 22.6 | 22.1 | Binance abrupt Pix suspension (Capitual) |
| M-01 | effective | 2021-07-26 | 2021-07-26 | 77.9 | 61.0 | -16.9 | 11.1 | -1.52 | 0.128 | 0.2736 | 14.0% | 38.4 | 34.5 | Binance leverage cap & withdrawal limit |
| M-02 | announcement | 2024-08-13 | 2024-08-13 | 55.4 | 42.3 | -13.1 | 18.9 | -0.69 | 0.488 | 0.3731 | 18.0% | 23.2 | 19.2 | CVM Binance settlement approval |
| M-02 | effective | 2024-08-20 | 2024-08-20 | 61.1 | 44.3 | -16.7 | 15.9 | -1.05 | 0.293 | 0.2786 | 14.0% | 24.9 | 18.4 | CVM Binance settlement DOU publication |
| M-03 | announcement | 2025-06-19 | 2025-06-20 | 38.3 | 21.1 | -17.2 | 7.0 | -2.47 | 0.014 | 0.2637 | 13.5% | 27.8 | 21.8 | Binance 10x tick size cut announcement |
| M-03 | effective | 2025-06-27 | 2025-06-27 | 39.9 | 16.0 | -23.9 | 5.5 | -4.31 | $1.6 \times 10^{-5}$ | 0.1990 | 9.0% | 31.1 | 19.9 | Binance 10x tick size cut takes effect |
| M-04 | effective | 2026-07-07 | 2026-07-07 | 70.9 | 60.4 | -10.5 | 28.6 | -0.37 | 0.713 | 0.4527 | 24.0% | 25.7 | 23.4 | Foxbit-NovaDAX migration & order-book adaptation |

*Note: E-03 effective date is N/A (unenacted proposal); E-06b effective date is 2027-01-01 (future date outside sample period).*

### Extended Windows for E-05 (23 Jun 2026)
- **Pre-trend check ($[-40, -21]$ vs $[-20, -1]$):** 24 Apr – 22 May (mean 7.0 bps) vs 25 May – 22 Jun (mean 15.2 bps). Drift $= +8.3$ bps. As shown by the real-time CUSUM monitor (F-014), the premium began building modestly in late May 2026 as BCB supervisory inquiries circulated.
- **Acute spike ($[+1, +20]$):** 24 Jun – 21 Jul 2026 (20 PTAX days): mean **109.1 bps** (jump of **+93.9 bps**).
- **Post-adaptation plateau ($[+21, +60]$):** 22 Jul – 16 Sep 2026 (40 PTAX days): mean **34.5 bps** ($+19.3$ bps vs pre-period mean).
- **Full plateau through sample end ($[+21, +71]$):** 22 Jul – 30 Oct 2026 (71 PTAX days): mean **26.8 bps** ($+11.5$ bps vs pre-period mean).

### Naive Persistence Baseline (S3)
- For E-05, the naive persistence baseline (forecasting zero change, using the pre-period mean of 15.2 bps) yields an RMSE of **103.1 bps** on the 20 post-event days.
- In contrast, modeling the new regime mean (109.1 bps) reduces the residual RMSE to **42.5 bps**, an error reduction of **58.8%**.
- Across null events (e.g., E-02, E-03, E-06a), the naive baseline RMSE is 6–12 bps, identical to the post-regime RMSE (5–10 bps), confirming no regime shift occurred.

### Placebo Benchmark (S2)
- 200 random dates drawn with `seed = 20261102` from 1,068 clean PTAX trading days outside $\pm 20$ trading days of all known events.
- Mean placebo diff: $-0.55$ bps, standard deviation: $18.00$ bps, median: $-0.73$ bps.
- Min placebo: $-57.53$ bps; Max placebo: $+62.66$ bps.
- Counts exceeding E-05 ($+93.9$ bps): $0 / 200$. Absolute counts $\ge 93.9$ bps: $0 / 200$.
- Figure saved to `results/figures/P2-03_placebo_dist.png`.

## Economic Interpretation
Why did only the 23 Jun 2026 supervisory *ofício* move the price of digital dollars, while major formal regulatory frameworks did not?
1. **Binding Arbitrage Channel:** Public regulations (such as Resolução BCB 519/520/521) set governance, reporting, and licensing standards with long implementation timelines (months to years), giving domestic OTC desks and institutional players ample time to adapt without interrupting capital flows.
2. **Immediate Administrative Enforcement:** The 23 Jun 2026 supervisory notice directly instructed commercial banks, foreign exchange brokers, and investment fund administrators to halt virtual-asset import structures that allowed instantaneous fiat-to-stablecoin transfers through offshore fund vehicles. This immediately severed the primary institutional arbitrage pipeline that kept USDT/BRL anchored to PTAX, causing the spread to blow out to +185 bps intraday and averaging +109 bps over the next 20 trading days.
3. **Endogenous Market Adaptation:** Over the following 20–30 days, domestic crypto market makers adapted by rerouting flows through direct OTC brokerage, bank FX settlement (paying standard FX spreads), and expanded domestic order-book integration (exemplified by the 7 Jul Foxbit-NovaDAX user migration and the 6x surge in Foxbit institutional trade size, F-008). Consequently, the acute spike faded into a persistent but smaller plateau of ~27–34 bps.

## Reproduction
```bash
python scripts/p2_03_events.py
```
Outputs: `results/tables/P2-03_event_table.csv`, `results/tables/P2-03_placebo_draws.csv`, `results/figures/P2-03_placebo_dist.png`, `results/agentic/team_estimate.json`.
