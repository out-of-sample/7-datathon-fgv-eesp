---
id: P3-03
title: Monitor do Dólar Digital (daily index + regime flag)
phase: P3
status: done
owner: CS 1
working: -
due: 2026-11-03
depends: P1-02, P2-02
---

## Goal
One script that updates a daily premium index, shows the current regime and flags a possible break: our 'solution' slide. No web app. Plan: `docs/02-dolar-cripto.md` §7.7.

## Subtasks
- [x] S1 — Write the alarm rule, calibration and pass mark (Specification below); commit before the first run. — done: Renzo, 2026-10-31
- [x] S2 — `scripts/p3_03_monitor.py`: rebuild premium and noise band from raw, then daily index, regime level and alarm. — done: Renzo, 2026-10-31
- [x] S3 — Real-time backtest, CUSUM vs the simple rule: delay on 24 Jun and 22 Jul 2026, false alarms per year. — done: Renzo, 2026-10-31
- [x] S4 — `results/figures/P3-03_monitor.png` (pt-BR, last 12 months + "today" box); finding; Handoff; STATUS. — done: Renzo, 2026-10-31

## Specification (S1)
Written 31 Oct 2026 by the agent for Renzo and **committed before the first run** of any monitor code. Plan:
`docs/02-dolar-cripto.md` §7.7. Honesty note: we know the 24 Jun 2026 jump and the 22 Jul fade (F-011). The
threshold is therefore set only on data before 2026, and 2026 is the test.

- **Data.** `premium_bps` from `data/processed/P1-02_premium_daily.csv` (PTAX days, 13 Oct 2020 – 30 Oct 2026) and
  `noise_band_bps` from `data/processed/P2-01_noise_floor_daily.csv` (same calendar date). The script first re-runs
  `scripts/p1_02_premium.py` and `scripts/p2_01_noise.py`, so it starts from raw data.
- **Daily index.** The premium (bps) and its 5-day mean.
- **Regime level.** Mean premium since the current regime began, using days up to yesterday only. The first regime
  starts on the first day; each alarm starts a new one (below).
- **Alarm (CUSUM, past data only).** On day t: `z = (y_t − level_t) / s_t`, with `s_t` = 1.4826 × MAD of the daily
  changes over the previous 60 PTAX days, divided by √2. Using daily changes keeps the scale from jumping after a
  level shift. Two sums: `S+ = max(0, S+ + z − k)`, `S− = max(0, S− − z − k)`, `k = 0.5`. **Alarm** when
  max(S+, S−) > h; its direction is the sign. After an alarm:
  - the new regime starts on the day after the alarming sum was last 0 (the standard CUSUM estimate of when the
    change began);
  - both sums reset;
  - there are no alarms for the next 10 PTAX days (warm-up).
- **Calibration.** Training period: 13 Oct 2020 – 31 Dec 2025, about 5.2 years. h is the smallest value on the
  grid 1, 1.5, …, 30 that gives at most 2 alarms per year in training (≤ 10 alarms). k, the 60-day window and the
  10-day warm-up are fixed and not tuned.
- **Simple rule (baseline).** Alarm when |mean of the last 5 days − mean of the 60 days before them| > c × noise band
  of the previous day, with the same 10-day pause after an alarm. c is the smallest value on the grid 0.5, 0.75, …, 10
  with at most 2 alarms per year in training. Same alarm budget, so the two rules are compared fairly.
- **Test.** 1 Jan – 30 Oct 2026, with the monitor running continuously from 2020.
  - **Targets:** the jump starting 24 Jun 2026 (upward) and the fade starting 22 Jul 2026 (downward), dated by P2-02.
    P2-02 used hindsight and the full sample, so it serves only as the "perfect" benchmark here.
  - **Detected:** the first alarm in the right direction within [−5, +20] PTAX days of the target. Its **delay** is
    that alarm's PTAX-day index minus the target's.
  - **False alarm:** any other test alarm. Rate = count per year of test.
  - **Training:** alarms are listed next to the P2-02 breaks (Jul 2021, Aug 2024, Jul 2025), as a description only.
- **Pass mark.**
  - **Useful:** it detects 24 Jun within 5 PTAX days, with ≤ 2 false alarms in the test.
  - **Beats the simple rule:** it detects 24 Jun sooner, or as soon with fewer false alarms.
  - Either way it is reported as is, including on the slide.
- **Today box.** For the last day (30 Oct 2026): the index and its 5-day mean, the regime level and its start date,
  the CUSUM as a percentage of h, and whether an alarm fired in the last 10 PTAX days.
- **Not done.** No tuning of k, the windows, the warm-up or the grids after seeing the test; any later variant is
  reported as an extra next to this one. No automatic daily download: updating means re-running
  `scripts/p1_01_download.py`, then this script.

## Success criteria
- [x] Script runs end to end from raw data
- [x] results/figures/P3-03_monitor.png ready for a slide
- [x] Rule for the flag written in the script header

## Outputs
- `scripts/p3_03_monitor.py`, `results/figures/P3-03_monitor.png`, `results/tables/P3-03_backtest.csv`,
  `data/processed/P3-03_monitor_daily.csv`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** S1–S4 done and independently reviewed by Jonathan (status `done`, F-014 `confirmed`); all three criteria met. The monitor passes the pass mark fixed in advance (F-014):
  - it flags the 24 Jun jump the same day;
  - it has 2 other alarms in the 2026 test, vs 4 for the simple rule;
  - it caught the fade after 11 PTAX days.
- **Next step:** Ready for P5 deck (slide 11, `results/figures/P3-03_monitor.png`) and P4-02 independent re-check.
- **Open questions:**
  - The upward sum built from 25 May 2026 and was at 92% of the threshold on 23 Jun: did something start in late May? Passed to P2-03 and P1-04.
  - Are the 25 Sep and 30 Oct "false" alarms real falls? Re-run with November data.
  - For the deck (P5): show the 5-day mean, not the lagging regime level, as the main line?
- **How to resume:** update with `python scripts/p1_01_download.py`, then `python scripts/p3_03_monitor.py`.

## Log
- 2026-11-02, agent for Renzo: audit item 5: `last_alarm` guard already applied (Felipe); re-run gives the same backtest table.
- 2026-11-01, Jonathan: reviewed `scripts/p3_03_monitor.py` (confirmed `.shift(1)` on `s` and `band_prev`, MAD scaling `1.4826 / sqrt(2)`, and `.shift(5)` on baseline window — zero lookahead), reproduced `P3-03_backtest.csv` (`h = 24.5`, `c = 7.25`) and `P3-03_monitor.png` matching F-014; status -> done
- 2026-10-31, agent for Renzo: S2–S4 done → review. CUSUM h = 24.5 (budget 10 alarms in 2020–2025): 24 Jun alarm same day, fade +11 days, 2 other test alarms; simple rule c = 7.25: same day, +12, 4 others (F-014). Pre-June build-up from 25 May noted for P2-03/P1-04.
- 2026-10-31, agent for Renzo: S1 specification written and committed before the first run.
- 2026-10-31, agent for Renzo: Renzo takes P3-03; subtasks being written.

## Result
F-014. Backtest in `results/tables/P3-03_backtest.csv`; figure `results/figures/P3-03_monitor.png`.
