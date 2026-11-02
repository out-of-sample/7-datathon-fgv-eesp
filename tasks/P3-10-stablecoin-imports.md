---
id: P3-10
title: Mechanism - did stablecoin imports fall when the premium jumped, and recover when it faded?
phase: P3
status: doing
owner: CS 1
working: Renzo
due: 2026-11-03
depends: P1-02, P2-02
---

## Goal
Measure the channel the 23 Jun notice reportedly closed. If the notice shut the route arbitrage funds used to
bring stablecoins into Brazil, the BCB's monthly statistics should show stablecoin purchases abroad falling in
July 2026 while the premium rose (price up, quantity down = a supply channel closing). The premium fell back from
22 Jul (F-011); if another route opened, purchases should recover in Aug–Sep. Plan: `docs/06-so-what.md`, answer 3.

## Specification (written 2 Nov 2026, before downloading; known at this point: only the press figures
US$ 2,540 mn for Jun and US$ 572 mn for Jul 2026, InvestNews 28 Aug. Aug and Sep 2026 not seen)

- **Series:** BCB external-sector statistics, monthly, stablecoins ("criptoativos com passivo correspondente"),
  purchases by residents abroad, US$ million, as far back as published. Use the series that reproduces the press
  figures for Jun and Jul 2026 (within rounding). If none does: stop and report (stop rule in `docs/06`).
- **T1, the drop:** log change Jun → Jul 2026, ranked against every other month-over-month log change in the
  series. Empirical p = (k+1)/(n+1), k = other months with a fall at least as large. Robustness (June may be
  inflated by a rush): log(Jul / mean of the five months before Jun), ranked against the same statistic for
  every other month. Prediction: p ≤ 0.10. If p > 0.10, the mechanism stays "reported, not measured".
- **T2, the fade:** R = mean(Aug, Sep 2026) / mean(Jan–May 2026). R ≥ 0.5: imports recovered, consistent with
  a new route explaining the fade. R < 0.25: not recovered, the fade is not explained by imports. In between:
  partial, reported as inconclusive. If Sep 2026 is not published yet, use Aug alone and say so.
- **T3, description only:** monthly purchases next to the monthly mean premium (P1-02), 2024 – Sep 2026, one
  figure. Correlation reported, no causal claim.
- **S3, on exchanges:** windows in PTAX days around 23 Jun: before [−20, −1], spike [+1, +20], after [+21, +60].
  Per venue (Binance, Foxbit, Mercado Bitcoin): daily volume (USDT), trades per day, average trade size,
  buyer-initiated share (Binance kline column 9; Foxbit `taker_buy_volume_usdt`, definition `[verify]`; Mercado
  Bitcoin has none). Description; the Binance volume change is ranked against the P2-03 placebo dates.

## Subtasks
- [ ] S1 — Locate the BCB file or series, download it to `data/raw/bcb/`, add its checksum to
  `data/raw/SHA256SUMS` and a D-row to `docs/sources.md`; check it reproduces the press figures. — doing: Renzo
- [ ] S2 — `scripts/p3_10_imports.py`: T1, T2, T3; figure `results/figures/P3-10_imports.png`; table
  `results/tables/P3-10_imports.csv`.
- [ ] S3 — On-exchange volume and order flow (same script), table `results/tables/P3-10_order_flow.csv`.
- [ ] S4 — Finding with the results whichever way they go.

## Success criteria
- [ ] Raw file frozen with checksum and source row; press figures reproduced (or the mismatch reported)
- [ ] T1, T2 and T3 run exactly as specified above; deviations written in the log with the reason
- [ ] Finding written with the command that reproduces every number

## Outputs
- `data/raw/bcb/<file>`, `scripts/p3_10_imports.py`, `data/processed/P3-10_imports_monthly.csv`,
  `results/figures/P3-10_imports.png`, `results/tables/P3-10_imports.csv`, `results/tables/P3-10_order_flow.csv`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** specification written and committed before any download.
- **Next step:** S1 — find the BCB series (external-sector statistics page or SGS).
- **Open questions:** none
- **How to resume:** read the specification above; do not change it after seeing Aug–Sep data without a log line.

## Log
- 2026-11-02, agent for Renzo: created with the specification (plan `docs/06-so-what.md`); Renzo takes S1.

## Result
