---
id: F-045
title: Audit of Binance 29–30 Oct 2026 security incident confirms E1 S2 directly excludes the 30 Oct observation; E2 pre-mean shift is minor (~2.3 bps); CUSUM monitor silence during 3–16 Nov is a mechanical quiet pause
status: exploratory
task: P3-26
date: 2026-11-07
checked_by: -
---

## Claim
An audit of Binance's 29 Oct 2026 security incident (M-11, M-12; hot-wallet compromise at 20:05 UTC) and resulting withdrawal suspension shows that the registered E1 S2 calculation excludes the 30 Oct dip directly; it does not exclude subsequent or shared incident effects. Under the pre-registered P3-20 rule (`9a522e9`), the event day `t0 = 30 Oct` is **excluded** from primary statistic S2: the 20-day pre-window ended on 29 Oct at 17:00 UTC (3 hours before the attack), and the post-window (3–4 Nov) began with small observed cross-venue gaps; exact USDT withdrawal restoration is not verified (gap −1.0 bps vs Foxbit). By contrast, S1 (+47.9 bps) directly measured recovery from the −30.3 bps Binance-only dip, justifying its pre-registered exclusion from the verdict. For E2 (Res. 589), the 30 Oct dip lowers the 20-day pre-mean by ~2.3 bps (a minor shift relative to the ±75 bps reference band). Finally, CUSUM monitor silence from 3 to 16 Nov is a mechanical 10-PTAX-day pause (`QUIET = 10`) triggered by the 30 Oct alarm, not an informative non-alarm reading.

## Evidence
Reproduce: `py scripts/p3_26_binance_incident_audit.py` → `results/tables/P3-26_incident_timeline.csv`, `results/tables/P3-26_window_sensitivity.csv`, `results/P3-26_audit.md`.

- **Chronology & Cross-Venue Dislocation:**
  - 29 Oct 2026 PTAX window (13:00–17:00 UTC): Binance +12.5 bps, Foxbit +13.4 bps, Mercado Bitcoin +11.3 bps (Foxbit − Binance gap +0.9 bps). Clean pre-incident baseline.
  - 29 Oct 2026 20:05 UTC: Attack onset and withdrawal freeze (M-11, M-12), 3 hours after window close.
  - 30 Oct 2026 PTAX window (E1 t0): Binance premium collapsed to **−30.3 bps**, while Foxbit remained at **+18.6 bps** and Mercado Bitcoin at **+17.4 bps**. The Foxbit − Binance gap expanded to **+49.0 bps** (+47.8 bps for MB − Binance).
  - 31 Oct – 1 Nov 2026: source M-11 describes planned phased restoration; exact USDT restoration is not established. 2 Nov: Dia de Finados bank holiday.
  - 3 Nov 2026 (E1 post-day 1): Binance +17.6 bps, Foxbit +16.6 bps (gap −1.0 bps). Cross-venue parity restored.
  - 4 Nov 2026 (E1 post-day 2): Binance +25.0 bps, Foxbit +22.0 bps (gap −3.0 bps).

- **E1 S2 Insulation vs S1 Contamination:**
  - Pre-registered S2 (`mean[3–4 Nov] − mean[1–29 Oct]`): `21.32 − 19.23 = +2.09 bps` (`p = 0.897`, non-overlapping `0.920`). The 30 Oct observation is excluded directly; residual effects remain possible.
  - S1 (`p[3 Nov] − p[30 Oct]`): `17.60 − (−30.35) = +47.95 bps` (`p = 0.12`). Contaminated by the 30 Oct trough.
  - Hypothetical S2 if 30 Oct were included in pre-window: `21.32 − 17.48 = +3.84 bps` (`p = 0.820`). Null verdict holds across all specifications.

- **E2 Pre-Mean Sensitivity:**
  - Registered 20-day pre-window (ending 4 Nov, contains 30 Oct): mean = 15.94 bps.
  - Sensitivity excluding 30 Oct (19 days): mean = 18.38 bps (+2.44 bps shift).
  - Sensitivity replacing 30 Oct with neutral 15.0 bps: mean = 18.21 bps (+2.27 bps shift).
  - Shifts of ~2.3 bps represent only ~3% of the ±75 bps reference band (`[−75.5, +59.8] bps`).

- **CUSUM Monitor Mechanical Pause:**
  - 30 Oct dip triggered downward CUSUM alarm (`2026-10-30(-)` in `results/tables/P3-03_backtest.csv`).
  - By line 76 of `scripts/p3_03_monitor.py`, alarm initiates mandatory 10-PTAX-day pause (`QUIET = 10`), covering 3 Nov through 16 Nov. Monitor silence is a mechanical artifact.

## Caveats
- While S2 excludes 30 Oct, general market sentiment or liquidity friction in the days following the attack could theoretically have persisted into 3–4 Nov; however, the cross-venue gap with Foxbit (−1.0 bps on 3 Nov, −3.0 bps on 4 Nov) indicates that venue-specific friction had normalized.
- Mercado Bitcoin data for 3–4 Nov is missing due to Cloudflare challenge on their API endpoint.

## Used in deck
Annex / Slide 10 methodological note and caveat disclosure for P3-20/P5-08.

## History
- 2026-11-07, Economist (Felipe): created from P3-26 audit.

- 2026-11-07 — Codex for Felipe (P3-36): audit corrections applied; claim limits clarified; original estimates retained. Independent reproduction status is unchanged.
