---
id: P1-07
title: Depeg detector and SVB-weekend figure (chapter)
phase: P1
status: doing
owner: Nattan
working: Nattan
due: 2026-11-01
depends: P1-01
---

## Goal
Count independent stablecoin depeg events and draft the SVB-weekend figure for the dollar-side chapter.
Plan: `docs/01-depeg-recovery.md` (chapter scope at the top, definition in §6.1).

## Subtasks
- [x] S1 — Freeze the event definition (§6.1) in this file **before** scanning all pairs. — done: Nattan, 2026-10-31
- [ ] S2 — Scan Binance stablecoin pairs; handle the numeraire problem (USDC/USDT is a relative price). — doing: Nattan
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
- **State:** S1 is frozen; S2 is in progress.
- **Next step:** inspect frozen stablecoin price files and implement the detector.
- **Open questions:** none
- **How to resume:** use the definition below, then run `scripts/p1_07_depeg.py` once created.

## Frozen event definition (S1)

This definition is fixed before the automated scan:

- **Price and numeraire:** screen Binance stablecoin/USDT pairs as relative prices. For a USD-level claim or the
  SVB figure, use a direct USD pair; do not treat an isolated stablecoin/USDT move as proof that the numerator
  depegged. Flag it as `relative-price candidate` when a direct USD reference is unavailable.
- **Start:** first observation with `abs(price - 1) > 0.005` (0.5%) that remains outside the band for at least
  30 consecutive minutes. For hourly data, require two consecutive hourly observations; the time resolution is
  recorded and does not imply minute precision.
- **End (recovery):** first observation inside `abs(price - 1) < 0.001` (0.1%) that remains inside for six
  consecutive hours. The event duration runs from start to that first recovery observation.
- **Independent event:** merge episodes whose gap is under 24 hours. If the recovery condition is never observed,
  censor the event at the last valid observation or delisting.
- **Quality rule:** reject bad ticks—isolated one-observation spikes, impossible/zero prices, or listing/relisting
  artefacts—and record every rejection and its reason. This task does not claim cross-venue confirmation where
  only one venue is frozen.
- **Pre-specified sensitivity checks:** start thresholds 0.3% and 1.0%; recovery bands 0.05% and 0.25%.

## Log
- 2026-10-31, Nattan: froze the event definition before S2; direct USD prices are required for USD-level claims.
- 2026-10-31, Nattan: claimed task; S1 in progress.
- 2026-10-31, agent for Renzo (note from P1-01, nobody working here yet): Binance has **no USDCUSDT data from
  2022-09-26 03h to 2023-03-11 13h UTC**. The pair restarts at 2023-03-11 14:00 UTC, mid-SVB weekend (first
  candle open 1.0000 = listing artefact, low 0.882). The Friday-to-Saturday-morning part of the depeg is not in
  Binance; S4 needs the Kraken reference or another venue for it. Details: P1-01 → Result.
- 2026-10-31, agent for Renzo (note from F-006): Bitstamp USDC/USD 1h covers all 120 hours of 10–14 Mar 2023,
  including the bottom (low 0.805 at 11 Mar 07:00 UTC) that Binance misses; USDT/USD itself reached 1.027 that
  night (Coinbase), so USDC/USDT understates USDC's fall. API calls are in `scripts/p1_02_probe_usdtusd.py`.

## Result
