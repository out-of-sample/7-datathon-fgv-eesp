---
id: F-029
title: On non-overlapping windows the June change still beats every ordinary window (p = 0.03), and the two days before the 26 Jun meeting add +155 bps (p 0.02-0.04); but the +94 bps month also holds other BCB measures, and Res. 574 coincides with a +38 bps day before the notice
status: exploratory
task: P4-04
date: 2026-11-02
checked_by: -
---

## Claim
**The headline survives honest inference.** The pre-committed statistic (mean premium over the 20 PTAX days after
23 Jun 2026 minus the 20 before, +93.9 bps, F-016) is larger than the same change at every one of 1,073 ordinary dates.
Those 1,073 windows overlap (neighbours share 38 of 40 days), so F-016's p = 0.0009 claims too much precision. Using
only windows that share no days, there are 30 per draw; the June change beats all 30 for every one of the 41 possible
draws: **p = 0.032** (two-sided, as F-016). The windows still are not fully independent, because the premium is
autocorrelated.

**What the +94 bps month contains.** The window 24 Jun – 21 Jul also holds the BCB meeting of 26 Jun (suspension kept,
in-book arbitrage released, a draft 24-hour hold presented; E-05.5, E-12) and Res. BCB 580 (1 Jul, E-10), and a second
peak on 3 Jul (+86.7 bps in a day) with no identified cause. +93.9 bps is the average over "the notice and what
followed", not the notice alone.

**The part before the meeting.** In the two PTAX days before the meeting (24–25 Jun), the premium averaged **+154.6 bps**
over the pre-notice level: beyond all but 2 of 1,073 ordinary dates (p = 0.003), and p = 0.020–0.040 on non-overlapping
windows (49 per draw). The first day alone rose +130.6 bps, the largest daily rise of 2026; since 2023, three other days
rose as much (one spans Carnival and is flagged).

**Res. 574 is not ruled out.** Res. BCB 574 (a reporting rule) is dated 18 Jun 18:01 in the BCB register and was
published in the DOU on 22 Jun. On the next PTAX day after its register date the premium rose **+37.7 bps** (−4.7 →
32.9 bps, 18 → 19 Jun); in 2026 before the notice only one other day rose as much (daily standard deviation 8.1 bps).
Part of it is a rebound from an unusually low 18 Jun (12.4 → −4.7). The premium then eased (23.3, 24.8 bps) before the
+130.6 bps jump on 24 Jun. An event study cannot separate the two rules: every 20-day window after 18 or 22 Jun contains
the 24 Jun jump.

## Evidence
- Reproduce: `python scripts/p4_04_inference.py` → `results/tables/P4-04_nonoverlap.csv` (one row per statistic and
  offset), `results/tables/P4-04_window_events.csv`; specification committed before the script (`f4071ef`). The
  script's clean-date rule reproduces F-016 exactly (1,073 dates, +93.91 bps, largest placebo +65.7, p = 0.0009).

| Statistic | Observed | All 1,073 clean dates | Non-overlapping windows |
|---|---|---|---|
| A: [+1, +20] vs [−20, −1] (headline) | +93.9 bps | k = 0, p = 0.0009, largest abs. placebo 65.7 | n = 30, k = 0 for all 41 offsets, p = 0.032 |
| B: [+1, +2] vs [−20, −1] (before the 26 Jun meeting) | +154.6 bps | k = 2, p = 0.0028, largest abs. placebo 202.8 | n = 49, k = 0–1 over 23 offsets, p = 0.020–0.040 |

- One-day change 23 → 24 Jun: +130.6 bps. Clean one-day changes as large: 9 of 1,092 (6 in 2021, 1 in 2022, 1 in 2024 on 2 Dec, 1 in 2025 on 5 Mar; 5 Aug 2024
  falls inside an event blackout).
  All days by year (excluding 24 Jun): 2023 none; 2024 two (5 Aug +300.2, 2 Dec +132.1); 2025 one (5 Mar +132.2,
  previous PTAX day 28 Feb, flagged `ptax_window_uncertain`); 2026 none (largest +86.7 on 3 Jul).
- Dated items within [−20, +20] PTAX days of 23 Jun (premium on that PTAX day, bps): Res. 574 register 18 Jun (−4.7);
  Res. 574 DOU 22 Jun (23.3); notice 23 Jun (24.8); meeting 26 Jun (75.6); Res. 580 1 Jul (121.1); Foxbit–NovaDAX 7 Jul
  (138.7); Foxbit Infra 18 Jul, a Saturday (20 Jul: 66.9).
- Res. 574 check (not in the script):
  ```bash
  .venv/bin/python -c "
  import pandas as pd
  p=pd.read_csv('data/processed/P1-02_premium_daily.csv',parse_dates=['date_brt']).set_index('date_brt')['premium_bps']
  d1=p.diff(); x=d1.loc['2026-06-19']; pre=d1['2026-01-01':'2026-06-22'].drop(pd.Timestamp('2026-06-19'))
  print(round(x,1), len(pre), (pre>=x).sum(), round(pre.std(),1))"
  ```

## Caveats
- **The statistic B window was chosen after seeing 24–25 Jun.** Its end (+2) is set by the meeting date, not by the
  premium, and the spec disclosed the values; it is secondary to A.
- **Daily data cannot say when Res. 574 became public.** The register time (18 Jun 18:01) may not be the public release
  time; the DOU date is 22 Jun.
- **One day is one day.** The 18 → 19 Jun rise is one observation after an unusual dip; it is not a test of Res. 574.
- Core findings F-016, F-022 and F-026 are unchanged (freeze rule); this finding sets how their numbers are worded.

## Text for the deck (for Felipe, P5-01)
- **Slide 4:** "+93,9 bps no mês seguinte ao ofício: maior que a variação em todas as 1.073 datas comuns; em 30 janelas
  que não se sobrepõem, p = 0,03. Nos dois dias antes da reunião de 26/jun, +155 bps (p entre 0,02 e 0,04)."
- **Slide 4 or 8, footnote:** "A janela de 20 dias inclui a reunião de 26/jun (suspensão mantida, arbitragem em livro
  liberada, minuta da retenção de 24 h) e a Res. 580 (1/jul); um segundo pico em 3/jul não tem causa identificada."
- **Slide 5** (replaces "Só o ofício moveu o preço"): "Das regras com data, só o ofício coincide com um movimento fora da
  faixa das datas comuns. A Res. 574, datada quatro dias antes, coincide com uma alta de 38 bps em um dia (18→19/jun),
  que o teste de evento não separa do ofício."

## Used in deck
Not yet; proposed for slides 4, 5 and 8.

## History
- 2026-11-02, agent for Renzo: created (P4-04). Exploratory values seen before the spec were disclosed in the task file.
