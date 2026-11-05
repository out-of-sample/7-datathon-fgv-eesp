---
id: F-014
title: A real-time alarm calibrated on 2020–2025 flags the 24 Jun 2026 jump on the same day, with fewer false alarms than a simple rule
status: frozen
task: P3-03
date: 2026-10-31
checked_by: Jonathan
---

## Claim
The "Monitor do Dólar Digital" alarm uses only data available on each day. Its threshold was set on 2020–2025, at
most 2 alarms per year. In the 2026 test:
- it fired on **24 Jun 2026, the day of the jump** (delay 0);
- it caught the fade 11 PTAX days after 22 Jul;
- it raised 2 other alarms in 10 months.

A simple rule with the same alarm budget also fired on 24 Jun, but raised 4 other alarms. The monitor meets the
pass mark fixed before the run (tasks/P3-03 → Specification).

## Evidence
Alarm budget: 10 in training (13 Oct 2020 – 31 Dec 2025, ≤ 2 per year). Test: 1 Jan – 30 Oct 2026.

| Rule | Parameter | Training alarms | 24 Jun jump | 22 Jul fade | Other test alarms (per year) |
|---|---|---|---|---|---|
| CUSUM | h = 24.5 | 9 | 24 Jun (0 days) | 6 Aug (11 days) | 2 (2.4): 25 Sep ↓, 30 Oct ↓ |
| Simple: 5-day vs 60-day mean > c × noise band | c = 7.25 | 10 | 24 Jun (0 days) | 7 Aug (12 days) | 4 (4.8): 9 Jul ↑, 24 Aug ↓, 9 Sep ↓, 24 Sep ↓ |

- **Before the jump.** The upward sum started building on 25 May 2026, the estimated start of the new regime. On
  23 Jun it was at 92% of the threshold (22.6 of 24.5): the premium was 23–25 bps on 22–23 Jun against a regime level
  of 9.6.
  - Weekly averages: 10–22 bps from mid-May, vs 5.8 bps in Jan–Apr 2026.
  - On 24 Jun the premium was 155 bps and the sum 62.
- **Today (30 Oct 2026).**
  - Premium: −30 bps; 5-day mean: −5 bps.
  - Level of the regime since 21 Aug: 22 bps.
  - A downward alarm fired that day.
- **Training.** The 9 alarms cut the slow 2021–2025 decline into steps (dates in the script output). Two are within
  10 PTAX days of a P2-02 break: 6 Aug 2024 (an upward alarm, while the P2-02 break is a fall) and 22 Jul 2025.
- **Reproduce:** `.venv/bin/python scripts/p3_03_monitor.py` (about 5 s; it rebuilds P1-02 and P2-01 from raw data
  first). It produces:
  - `results/tables/P3-03_backtest.csv`;
  - `data/processed/P3-03_monitor_daily.csv`;
  - `results/figures/P3-03_monitor.png`.

## Caveats
- **The 24 Jun jump is an easy target.** The premium went up about 10-fold in a day. The fade is a fairer test of
  speed, and both rules took about 11–12 PTAX days on it.
- **"False" alarms may be real.** The two other CUSUM alarms (25 Sep, 30 Oct) are falls toward and below the
  pre-June level. The rule counts them as false because P2-02 found no break there, but P2-02 cannot place a break in
  the last 20 days of the sample. The 30 Oct alarm rests on the last data point; new data will tell.
- **The regime level lags.** It is a running average since the regime began, so it lags: it reached about 60 bps
  only as the spike faded. On the slide the 5-day mean carries the message.
- **The 23 Jun timing.** The monitor uses one daily series (Binance, PTAX window). Hourly data showed the rise
  starting on the afternoon of 23 Jun (P2-05); a daily monitor sees it on 24 Jun.
- **Venue coverage:** Uses P1-02's primary premium series (Binance USDT/USD-adjusted); re-checked and verified by Jonathan (1 Nov 2026).
- **The pre-June build-up is a question, not a finding.** Did something start in late May 2026? It goes to P2-03
  (pre-trend before the event) and P1-04 (events in May–Jun 2026).

## Used in deck
Not yet (candidate: slide 11, "Monitor do Dólar Digital", figure `P3-03_monitor.png`).

## History
- 2026-11-04, agent for Renzo (P4-03, Renzo's decision): status confirmed -> frozen (tag `results-frozen`); from now on only bug fixes, each disclosed here
- 2026-11-01, Jonathan: reproduced script, backtest table (`P3-03_backtest.csv`) and figure (`P3-03_monitor.png`); audited past-data-only shifts (`.shift(1)` on `s_t` and noise band); status -> confirmed
- 2026-10-31, agent for Renzo: created (exploratory); specification committed before the run (commit 827adcb)
