---
id: P2-02
title: Blind structural-break test on the premium
phase: P2
status: review
owner: CS 2
working: -
due: 2026-11-01
depends: P1-02, P1-04
---

## Goal
Let an algorithm find the dates where the premium changed regime **without telling it the policy dates**,
then check which breaks match known events. If it finds 24 Jun 2026 on its own, that is our headline chart.

## Subtasks
- [x] S1 — **Before running**, write the specification here: method (Bai-Perron via R `strucchange`, or Python
   `ruptures`), minimum segment = 20 trading days, maximum breaks = 8, number of breaks chosen by BIC. — done: Renzo, 31 Oct (Specification below)
- [x] S2 — Run on the daily premium (P1-02). Report break dates with confidence intervals. — done: Renzo, 31 Oct
- [x] S3 — Match breaks to the P1-04 events (within +/-5 trading days). List unmatched breaks as "unexplained". — done: Felipe, 2 Nov
- [x] S4 — Robustness: the alternative time-matching variant of the premium. — done: Renzo, 31 Oct (also Coinbase USDT/USD)

## Success criteria
- [x] Specification committed before the first run
- [x] `results/tables/P2-02_breaks.csv` (date, CI, matched event or "unexplained")
- [x] `results/figures/P2-02_premium_breaks.png` (premium, noise band, breaks, event markers)
- [x] Finding written

## Outputs
- `scripts/p2_02_breaks.py` (or `.R`), table, figure, finding

## Specification (S1)
Written 31 Oct 2026 by the agent for Renzo and **committed before the first run** of any break test on the premium.
Main choices (method, 20-day minimum, BIC) come from `docs/02-dolar-cripto.md` §7.2 (30 Oct, before the v2 series
existed). Honesty note: the team has already seen the premium chart and knows about the 24 Jun 2026 jump; "blind"
means the algorithm is given no event dates, and every choice below is fixed before it runs.

- **Data.** `premium_bps` from `data/processed/P1-02_premium_daily.csv`: every PTAX day, 13 Oct 2020 – 30 Oct 2026
  (1,520 days, no gaps; the 14 `ptax_window_uncertain` days are kept, as in P1-02). One observation = one PTAX day.
- **Model.** Pure mean-shift model (Bai–Perron with a constant only): the premium is a constant plus noise within each
  regime. Break dates estimated by least squares with dynamic programming (`ruptures.Dynp`, cost `l2`, exact global
  optimum for each number of breaks), minimum segment 20 PTAX days, 0 to 8 breaks.
- **Number of breaks.** Primary: BIC as in Bai–Perron, `ln(SSR_m / T) + p ln(T) / T` with `p = 2m + 1` (m break dates
  plus m+1 means). Also reported: LWZ (Liu, Wu & Zidek 1997), `ln(SSR_m / (T − p)) + (p · 0.299 / T) (ln T)^2.1`.
  **Pre-committed rule:** BIC is known to over-select breaks when errors are serially correlated (here AR(1) ≈ 0.65).
  If BIC picks the maximum (8), we treat that as over-selection and the headline count is LWZ's; otherwise BIC's.
- **Confidence intervals.** Bai (1997) for a mean shift: 95% CI = break ± 11.03 · ω² / δ² PTAX days, where δ is the
  change in mean at the break and ω² the long-run variance of the residuals of the chosen model (Newey–West, Bartlett
  kernel, lag floor(4 (T/100)^(2/9)) = 7). Constants `[verify]` against Bai (1997) (L-03). Intervals reported in PTAX days
  and mapped to dates.
- **What counts as "found 24 Jun 2026".** A headline break whose 95% CI contains 23 or 24 Jun 2026, or whose date is
  within ±5 PTAX days of 23 Jun 2026 (the S3 matching window).
- **Matching (S3, after P1-04).** A break matches an event if the event date is within ±5 PTAX days of the break date;
  we also report whether the event lies inside the 95% CI. Breaks with no event are reported as "unexplained". Known
  non-rule candidates to list beside the rules: Binance tick cut (~27 Jun 2025, F-007), Binance Pix suspension
  (Jun–Jul 2022, E-07), FTX collapse (Nov 2022), SVB weekend (Mar 2023).
- **Robustness (S4), same specification:** (a) `premium_dayclose_bps` (other timing); (b) `premium_cb_bps` (Coinbase
  USDT/USD, from May 2021); (c) both BIC and LWZ counts shown for every series.
- **Figure.** Premium, P2-01 noise band, regime means, break dates with 95% CIs; event markers added in S3.
- **Not done:** no tuning of the minimum segment, the maximum or the penalty after seeing the output; any later variant
  is reported as an extra, next to this one.

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** S1–S4 complete (`status: review`). S3 matching re-run on 2 Nov after P1-04 source fixes so every break follows the strict ±5-day rule (`F-011`).
- **Next step:** Teammate (Nattan / Jonathan) reviews `results/tables/P2-02_breaks.csv` and `findings/F-011-blind-breaks.md` and marks `done`.
- **Open questions:** Break 5 (22 Jul 2026, fade from 109.1 to 26.8 bps) has no verified event within ±5 trading days and is reported as `unexplained` (M-04 on 7 Jul is −11 trading days away; M-05 Foxbit Infra on 18 Jul is a market rebrand/claim, not a rule).
- **How to resume:** `py scripts/p2_02_breaks.py`

## Log
- 2026-11-02, agent for Renzo: S3 re-run after the P1-04 source fixes. Removed the date-keyed overrides (Break 3, July fade) and the hand-written labels/markers so every break follows the ±5-day rule and labels come from the event table. Main series: Breaks 1–4 coincide with M-01 (0d), M-02 (−5d, was 0d with the unsourced 20 Aug date), E-01b (−2d), E-05 (−1d); Break 5 unexplained. The committed table had come from an older script version (Coinbase break 1 19 Jul 2021 vs 1 Jun 2021 now and on 31 Oct). F-011 updated.
- 2026-11-02, Felipe: S3 matching completed using P1-04 verified events + non-rules; results/tables/P2-02_breaks.csv updated; script handles both local full data and table-based matching; status -> review
- 2026-10-31, agent for Renzo: S2 and S4 run (F-011): 24 Jun 2026 found blind (CI 18–30 Jun, +99.8 bps) in all three series; partial reversal from 22 Jul. Status → blocked (S3 needs P1-04)
- 2026-10-31, agent for Renzo: S1 specification written and committed before any break-test run
- 2026-10-31, agent for Renzo: Renzo takes P2-02 (CS 2 task; Renzo covers CS 2 work and tells Nattan). S1–S2 and S4 now; S3 waits for P1-04
- 2026-10-31, agent for Renzo (note from P2-01, nobody working here yet): Binance cut the USDT/BRL price tick
  tenfold on ~27 Jun 2025 (0.001 → 0.0001 BRL; F-007). The premium steps down around Jul 2025 (P1-02 figures).
  If the break test finds a break there, the tick change is a candidate explanation besides any rule.

## Result
S3 complete. Breaks found blind (headline: LWZ, because BIC hit the cap of 8; F-011):

| Break | First day of new regime | 95% CI | Mean before → after (bps) | Matched event (±5 PTAX days) |
|---|---|---|---|---|
| 1 | 26 Jul 2021 | 22 Jun – 27 Aug 2021 | 91.3 → 54.5 | Coincides with M-01: 26 Jul 2021 Binance 20× leverage cap (0 trading days, in 95% CI) |
| 2 | 20 Aug 2024 | 24 Apr – 16 Dec 2024 | 54.5 → 34.9 | Coincides with M-02: 13 Aug 2024 CVM–Binance settlement (−5 trading days, in 95% CI) |
| 3 | 8 Jul 2025 | 29 Apr – 12 Sep 2025 | 34.9 → 9.3 | Coincides with E-01b: 4 Jul 2025 STF IOF injunction (−2 trading days, in 95% CI; M-03 tick cut 27 Jun is −7d, in 95% CI) |
| 4 | **24 Jun 2026** | **18 – 30 Jun 2026** | 9.3 → 109.1 | **Coincides with E-05: 23 Jun 2026 BCB supervisory ofício (−1 trading day, in 95% CI)** |
| 5 | 22 Jul 2026 | 15 – 29 Jul 2026 | 109.1 → 26.8 | **unexplained** (no event within ±5 trading days; M-04 on 7 Jul is −11d) |

24 Jun 2026 is found in all three series (day-close 23 Jun; Coinbase USDT/USD 24 Jun), and so is the reversal around
21–22 Jul. Command: `py scripts/p2_02_breaks.py`. Figure: `results/figures/P2-02_premium_breaks.png`.
