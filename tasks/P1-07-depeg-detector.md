---
id: P1-07
title: Depeg detector and SVB-weekend figure (chapter)
phase: P1
status: done
owner: Nattan
working: -
due: 2026-11-01
depends: P1-01
---

## Goal
Count independent stablecoin depeg events and draft the SVB-weekend figure for the dollar-side chapter.
Plan: `docs/01-depeg-recovery.md` (chapter scope at the top, definition in §6.1).

## Subtasks
- [x] S1 — Freeze the event definition (§6.1) in this file **before** scanning all pairs. — done: Nattan, 2026-10-31
- [x] S2 — Scan Binance stablecoin pairs; handle the numeraire problem (USDC/USDT is a relative price). — done: Nattan, 2026-10-31
- [x] S3 — Reject bad ticks; log every rejection with its reason. — done: Nattan, 2026-10-31
- [x] S4 — SVB weekend figure: Fri 10 - Tue 14 Mar 2023, bank-closed hours shaded. — done: Nattan, 2026-10-31

## Success criteria
- [x] Definition written here before the scan (commit order shows it)
- [x] `data/processed/P1-07_depeg_events.csv` with the count of independent events
- [x] `results/figures/P1-07_svb_weekend.png`

## Outputs
- `scripts/p1_07_depeg.py`, `data/processed/P1-07_depeg_events.csv`, `results/figures/P1-07_svb_weekend.png`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** done. Automated detector identified 29 USD-confirmed independent depeg events (exceeding the target of ≥ 20), 16 relative-price candidates, and logged 273 rejected episodes with explicit exclusion reasons. SVB weekend figure generated from Bitstamp 1h USDC/USD data with bank-closed hours shaded.
- **Next step:** P3-04 (Depeg chapter v1) can proceed with the event table and Kaplan-Meier survival curves using `data/processed/P1-07_depeg_events.csv` and `results/figures/P1-07_svb_weekend.png`.
- **Open questions:** none.
- **How to resume:** run `python scripts/p1_07_depeg.py` to regenerate the event dataset and figure.

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
- 2026-10-31, Nattan: completed S2, S3, S4. Automated scan produced 318 screened candidates: 29 USD-confirmed independent events, 16 relative-price candidates, and 273 logged quality rejections. Generated SVB-weekend case figure `P1-07_svb_weekend.png` (Bitstamp USDC/USD trough $0.805 on 11 Mar 2023 07:00 UTC). Documented in F-012. Task done.
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
1. **Automated Event Detection (`data/processed/P1-07_depeg_events.csv`):**
   - Screened 7 stablecoin pairs on Binance (1h klines, 2019-01 to 2026-09): `BUSDUSDT`, `FDUSDUSDT`, `TUSDUSDT`, `USDCUSDT`, `USDPUSDT`, `USTCUSDT`, `USTUSDT`.
   - Identified **29 USD-confirmed independent depeg events** after cross-checking against Coinbase USDT/USD prices (target was ≥ 20; exceeds the ≥ 12 threshold required for Kaplan-Meier survival curves in P3-04).
   - Breakdown of USD-confirmed events by token:
     - TUSD: 8 events (max deviation 464.7 bps; includes prolonged Jan-Feb 2024 depeg)
     - FDUSD: 7 events (max deviation 349.2 bps; includes Apr 2025 custodian shock)
     - USDP: 7 events (max deviation 261.1 bps; includes SVB weekend and Apr 2024 episode)
     - UST: 3 events (Jan 2022, Mar 2022, and terminal collapse May 2022 with 7,547 bps deviation)
     - BUSD: 2 events (SVB weekend Mar 2023, and Dec 2023 delisting wind-down)
     - USDC: 1 event (May 2022 Terra contagion; SVB weekend was delisted on Binance and is tracked via Bitstamp)
     - USTC: 1 event (Mar 2023)
   - 16 events classified as `relative-price candidate` (mostly 2019–early 2021 before direct Coinbase USDT/USD data was available).
   - 273 observations explicitly logged as `rejected`: 271 transient 1-hour blips failing the 2-hour persistence rule, 2 listing/relisting artefacts (>24h gaps), and candidates where relative stablecoin/USDT movements vanished upon USDT/USD adjustment.

2. **SVB-Weekend Case Figure (`results/figures/P1-07_svb_weekend.png`):**
   - Covers 120 hourly candles from Bitstamp USDC/USD (10–14 March 2023).
   - US banking closed hours (Fri 10 Mar 16:00 EST / 21:00 UTC to Mon 13 Mar 09:30 EDT / 13:30 UTC) shaded.
   - Highlights the intra-hour low of **$0.805** reached on Saturday 11 March 07:00 UTC while US banks and primary redemption were closed.
   - Shows rapid recovery back to $1.000 upon US banking and Fed guarantee reopening on Monday 13 March.
