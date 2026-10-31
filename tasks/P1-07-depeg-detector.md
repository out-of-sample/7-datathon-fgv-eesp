---
id: P1-07
title: Depeg detector and SVB-weekend figure (chapter)
phase: P1
status: todo
owner: CS 3
working: -
due: 2026-11-01
depends: P1-01
---

## Goal
Count independent stablecoin depeg events and draft the SVB-weekend figure for the dollar-side chapter.
Plan: `docs/01-depeg-recovery.md` (chapter scope at the top, definition in §6.1).

## Subtasks
- [ ] S1 — Freeze the event definition (§6.1) in this file **before** scanning all pairs.
- [ ] S2 — Scan Binance stablecoin pairs; handle the numeraire problem (USDC/USDT is a relative price).
- [ ] S3 — Reject bad ticks; log every rejection with its reason.
- [ ] S4 — SVB weekend figure: Fri 10 - Tue 14 Mar 2023, bank-closed hours shaded.

## Success criteria
- [ ] Definition written here before the scan (commit order shows it)
- [ ] `data/processed/P1-07_depeg_events.csv` with the count of independent events
- [ ] `results/figures/P1-07_svb_weekend.png`

## Outputs
- `scripts/p1_07_depeg.py`, `data/processed/P1-07_depeg_events.csv`, `results/figures/P1-07_svb_weekend.png`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** not started
- **Next step:** S1
- **Open questions:** none
- **How to resume:** -

## Log
- 2026-10-31, agent for Renzo (note from P1-01, nobody working here yet): Binance has **no USDCUSDT data from
  2022-09-26 03h to 2023-03-11 13h UTC**. The pair restarts at 2023-03-11 14:00 UTC, mid-SVB weekend (first
  candle open 1.0000 = listing artefact, low 0.882). The Friday-to-Saturday-morning part of the depeg is not in
  Binance; S4 needs the Kraken reference or another venue for it. Details: P1-01 → Result.

## Result
