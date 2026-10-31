---
id: P1-09
title: Remove the Brazil-listing boundary from donor history
phase: P1
status: todo
owner: CS 2
working: -
due: 2026-11-04
depends: P1-05
---

## Goal
Make donor history independent of the USDT/BRL listing clock. This is a historical cleanup;
the P1-05 review found no numerical discrepancy in the planned synthetic-control periods.

## Subtasks
- [ ] S1 — Build the donor USDT/USD adjustment directly from the frozen USDCUSDT/BUSDUSDT candles, or explicitly mask incomplete boundary sessions and document the restricted history.
- [ ] S2 — Re-run P1-05 and its independent review; explain the changed historical dates in F-010 History and the task handoff.

## Success criteria
- [ ] Donor sessions are not silently shortened by missing USDT/BRL timestamps.
- [ ] The historical discrepancy in `results/tables/P1-05_review_differences.csv` is resolved and all affected dates are disclosed.
- [ ] Existing core-period estimates are unchanged within output rounding.

## Outputs
- `scripts/p1_05_donors.py`, existing P1-05 output files and review tables.

## Handoff
- **State:** not started; found during P1-05 independent review. Production code reads its USD adjustment from P1-02's BRL-indexed hourly file.
- **Next step:** S1; inspect `uu` in `scripts/p1_05_donors.py` and `h` in `scripts/p1_02_premium.py`. Keep the original raw files immutable.
- **Open questions:** whether earlier donor history is useful; do not expand the P2-04 analysis window as part of this cleanup.
- **How to resume:** `.venv/bin/python scripts/p1_05_review.py`; see F-010 History for the exact discrepancy. No need to redownload data.

## Log
- 2026-10-31, second agent for Renzo: created from P1-05 review; deferred because it does not affect the core study or F-010's reported years.

## Result
Not started.
