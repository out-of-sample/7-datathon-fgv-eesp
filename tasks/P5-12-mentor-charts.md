---
id: P5-12
title: Mentor feedback 1 and 2 - historical PTAX premium and currency comparisons
phase: P5
status: review
owner: Economist
working: -
due: 2026-11-08
depends: P1-02, P1-05, P3-46
---

## Goal
Deliver large chart images matching deck v4, without editing the supplied deck. Felipe explicitly requested feedback 1 first, plus candidates for feedback 2.

## Subtasks
- [x] S1 — Inspect deck and frozen series, verify coverage and negative premiums — done: Codex for Felipe, 8 Nov
- [x] S2 — Historical premium since 2020, with full daily range and a literal unadjusted PTAX companion — done: Codex for Felipe, 8 Nov
- [x] S3 — Euro and Mexican peso time-series comparison and before/after bars; preserve descriptive limits — done: Codex for Felipe, 8 Nov
- [x] S4 — Inspect images, record reproducible finding and handoff — done: Codex for Felipe, 8 Nov

## Success criteria
- [x] Historical plots include daily extremes and zero, with dates and percent units.
- [x] Cross-country figures identify own official FX benchmarks and reproduce F-053.
- [x] PNGs rendered and inspected; source CSVs and script retained.

## Handoff
- **State:** Four final chart pairs (PNG/SVG), data tables and F-057 ready. Existing staged STATUS.md and untracked work preserved. Pull --rebase refused because index is dirty.
- **Next step:** Felipe chooses historical definition (deck-adjusted recommended) and comparison graphic for slides 2/5. Independent teammate review before asserting new descriptive results as reviewed.
- **Open questions:** No slide editing performed. "Never below PTAX" is false; do not add it. Historical maximum is not the June 2026 event.
- **How to resume:** `python scripts/p5_12_mentor_charts.py` with pandas/numpy/matplotlib. Read F-057; figures under results/figures/P5-12_*.

## Log
- 2026-11-08 — Codex for Felipe: charts generated and inspected, labels corrected, arithmetic and F-053 reproduced; ready for review.
- 2026-11-08 — Codex for Felipe: registered scope; reviewed deck XML and existing datasets. Claim push deferred to avoid mixing staged work.

## Result
Four chart options match the supplied deck palette and retain honest axes and negative values. F-057 documents coverage, arithmetic and limits. Original PPTX unchanged.
