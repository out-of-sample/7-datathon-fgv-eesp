---
id: P1-09
title: Remove the Brazil-listing boundary from donor history
phase: P1
status: review
owner: CS 2
working: -
due: 2026-11-04
depends: P1-05
---

## Goal
Make donor history independent of the USDT/BRL listing clock. This is a historical cleanup;
the P1-05 review found no numerical discrepancy in the planned synthetic-control periods.

## Subtasks
- [x] S1 — Build the donor USDT/USD adjustment directly from the frozen USDCUSDT/BUSDUSDT candles, or explicitly mask incomplete boundary sessions and document the restricted history. — done: Felipe, 2 Nov
- [x] S2 — Re-run P1-05 and its independent review; explain the changed historical dates in F-010 History and the task handoff. — done: Felipe, 2 Nov

## Success criteria
- [x] Donor sessions are not silently shortened by missing USDT/BRL timestamps.
- [x] The historical discrepancy in `results/tables/P1-05_review_differences.csv` is resolved and all affected dates are disclosed.
- [x] Existing core-period estimates are unchanged within output rounding.

## Outputs
- `scripts/p1_05_donors.py`, `scripts/p1_05_review.py`
- `data/processed/P1-05_donor_premiums_daily.csv`
- `results/tables/P1-05_donor_coverage.csv`
- `results/tables/P1-05_review.csv`, `results/tables/P1-05_review_yearly.csv`, `results/tables/P1-05_review_differences.csv`

## Handoff
- **State:** complete, awaiting teammate review.
- **Next step:** none; P1-09 is in review.
- **Open questions:** none; core-period donor history and P2-04 synthetic control results are completely unchanged.
- **How to resume:** run `py scripts/p1_05_donors.py` and `py scripts/p1_05_review.py`.

## Log
- 2026-10-31, second agent for Renzo: created from P1-05 review; deferred because it does not affect the core study or F-010's reported years.
- 2026-11-02, Felipe: rebuilt `uu` in `scripts/p1_05_donors.py` directly from raw `USDCUSDT`/`BUSDUSDT` candles from 2020-01-01 onward; resolved the single 13 Oct 2020 UAH boundary discrepancy (now 11.25 bps vs 11.248862 bps independent review); verified `results/tables/P1-05_review_differences.csv` now has 0 discrepancies; confirmed all 2021–2026 donor yearly means and P2-04 synthetic control estimates are 100% unchanged; updated F-010 History; set status to review.

## Result
Rebuilt the USDT/USD reference series `uu` directly from the immutable raw Binance candles (`USDCUSDT` with `BUSDUSDT` gap filler) in `scripts/p1_05_donors.py`, making donor history independent of the `USDTBRL` listing time (10:00 UTC on 13 Oct 2020). On 13 Oct 2020, UAH now includes all 7 specified hours (10:00–16:00 Kyiv), yielding 11.25 bps (11.248862 bps), matching the independent raw reconstruction in `scripts/p1_05_review.py`. `results/tables/P1-05_review_differences.csv` now contains 0 discrepancies. All donor numbers in the core analysis window (1 Nov 2025 – 30 Sep 2026) and yearly means across 2021–2026 remain 100.0% unchanged.
