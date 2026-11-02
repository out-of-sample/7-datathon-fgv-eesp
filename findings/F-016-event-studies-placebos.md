---
id: F-016
title: Of 13 dated Brazilian events, only the 23 Jun 2026 BCB notice moved the premium (+93.9 bps; beyond all 1,073 placebo dates, p ≈ 0.001)
status: confirmed
task: P2-03
date: 2026-11-02
checked_by: Renzo
---

## Claim
We compared the premium in the 20 PTAX days before and after every dated Brazilian event in P1-04 (13 events, effective
and announcement dates). **Only the 23 Jun 2026 BCB notice (E-05) stands out: +93.9 bps** (15.2 → 109.1 bps). No random
"placebo" date comes close. Against 200 random clean dates, p = 0.005, the smallest possible with 200. Against all 1,073
clean dates, p = 0.0009, with the largest placebo move at +65.7 bps. Every other event, including the formal regulations
(E-02 SPSAV framework, E-04 reporting codes, E-06a eFX, E-03 the 3.5% crypto IOF proposal) and the May 2025 IOF increase,
moved the premium by −25 to +15 bps, well inside ordinary variation (placebo p ≥ 0.15).

## Evidence
Window: 20 PTAX days before ([−20, −1]) vs after ([+1, +20]) the first PTAX day on or after each date, that day excluded.
Placebos: clean PTAX days, outside ±20 days of every event date. "p (200)" uses 200 random clean dates with weekday
quotas taken from the event dates (seed 20261102); "p (all)" uses every clean date. Both are two-sided, (k+1)/(n+1).

| Event | Date kind | Date | Pre (bps) | Post (bps) | Change (bps) | p (200) | p (all clean) |
|---|---|---|---|---|---|---|---|
| E-01 | announcement | 2025-05-22 | 26.9 | 40.1 | +13.2 | 0.403 | 0.3845 |
| E-01 | effective | 2025-05-23 | 26.2 | 41.6 | +15.4 | 0.338 | 0.3147 |
| E-01b | announcement | 2025-06-27 | 39.9 | 16.0 | -23.9 | 0.194 | 0.1648 |
| E-01b | effective | 2025-07-04 | 37.6 | 12.7 | -24.9 | 0.184 | 0.1527 |
| E-02 | announcement | 2025-11-10 | 13.2 | 9.5 | -3.8 | 0.721 | 0.7477 |
| E-02 | effective | 2026-02-02 | 8.4 | 4.1 | -4.3 | 0.697 | 0.7225 |
| E-03 | announcement | 2026-02-05 | 7.6 | 5.5 | -2.1 | 0.846 | 0.8408 |
| E-04 | announcement | 2025-11-10 | 13.2 | 9.5 | -3.8 | 0.721 | 0.7477 |
| E-04 | effective | 2026-05-04 | 4.7 | 11.9 | +7.2 | 0.612 | 0.6145 |
| E-05 | effective | 2026-06-23 | 15.2 | 109.1 | +93.9 | 0.005 | 0.0009 |
| E-06a | announcement | 2026-04-30 | 4.9 | 10.9 | +6.0 | 0.622 | 0.6471 |
| E-06a | effective | 2026-10-01 | 22.8 | 17.5 | -5.3 | 0.662 | 0.6778 |
| E-06b | announcement | 2026-08-07 | 53.3 | 31.3 | -22.0 | 0.219 | 0.1872 |
| E-07 | effective | 2022-06-17 | 53.2 | 48.5 | -4.7 | 0.687 | 0.7039 |
| M-01 | effective | 2021-07-26 | 77.9 | 61.0 | -16.9 | 0.298 | 0.2700 |
| M-02 | effective | 2024-08-13 | 55.4 | 42.3 | -13.1 | 0.403 | 0.3855 |
| M-03 | effective | 2025-06-27 | 39.9 | 16.0 | -23.9 | 0.194 | 0.1648 |
| M-04 | effective | 2026-07-07 | 71.0 | 60.4 | -10.5 | 0.488 | 0.4888 |

E-03 has no effective date (unenacted proposal); E-06b takes effect on 1 Jan 2027, outside the sample.

- **Why no parametric p-values.** The Newey–West test (5 lags, 20 + 20 days) calls almost every event significant: for
  example E-01 has p = 10⁻¹¹ but a placebo p of 0.38. The premium is strongly autocorrelated, so 20-day means drift on
  ordinary days. The script still writes `p_param` to the table, but it is not used.
- **Before the notice.** Over [−40, −21] (24 Apr – 22 May) the premium averaged 7.0 bps, and over [−20, −1] (25 May – 22 Jun)
  15.2 bps, a +8.3 bps drift. The real-time monitor shows the same build-up from 25 May (F-014). Its cause is unknown.
- **After the spike.** [+21, +60] (22 Jul – 16 Sep) averages 34.5 bps (+19.3 vs the pre-window); [+21, end] (to 30 Oct)
  26.8 bps (+11.5). The placebo test in P4-01 does not separate this from ordinary drift (p = 0.24), so only the spike is
  a measured effect.
- **Baseline.** The pre-window mean is the no-change forecast. The +93.9 bps *is* the comparison with that baseline.

## Interpretation (hypotheses, not tested here)
1. Formal rules with long lead times (E-02, E-04, E-06a) may leave time to adjust, while a supervisory notice with
   immediate effect (E-05) does not.
2. The reported content of the notice (FX operations by funds to import virtual assets declared irregular; D-sources
   in E-05) fits a closed arbitrage channel, which is the project's thesis. We have not observed the channel's volumes.
3. Why the spike faded after about a month is unexplained (P2-02 finds no event within ±5 days of the 22 Jul break).

## Reproduction
```bash
python scripts/p2_03_events.py
```
Outputs: `results/tables/P2-03_event_table.csv`, `results/tables/P2-03_placebo_draws.csv`, `results/figures/P2-03_placebo_dist.png`, `results/agentic/team_estimate.json`.

## History
- 2026-11-02, agent for Renzo (review fixes, on Felipe's behalf, agreed by Renzo): table re-run with corrected P1-04 dates and placebo-only p-values; all-clean-dates p added; unsourced "BCB inquiries circulated" removed; RMSE "baseline" replaced; interpretation marked as hypotheses; title updated
- 2026-11-02, Renzo (review, P2-03): numbers reproduced; headline holds; text changes requested (tasks/P2-03 → Handoff)
- 2026-11-02, Felipe: created
