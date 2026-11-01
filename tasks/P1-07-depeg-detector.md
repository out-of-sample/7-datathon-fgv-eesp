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
- [x] S5 — Review of S1–S4 (see Review below). — done: Renzo, 2026-10-31
- [x] S6 — Fix the review points in a v2 script (`scripts/p1_07_depeg_v2.py`); v1 script and outputs stay untouched. — done: Renzo, 2026-10-31
- [x] S7 — Compare v1 and v2 event by event; new finding for the v2 count; F-012 History updated. — done: Renzo, 2026-10-31

## Success criteria
- [x] Definition written here before the scan (commit order shows it)
- [x] `data/processed/P1-07_depeg_events.csv` with the count of independent events
- [x] `results/figures/P1-07_svb_weekend.png`

## Outputs
- v1 (Nattan): `scripts/p1_07_depeg.py`, `data/processed/P1-07_depeg_events.csv`, `results/figures/P1-07_svb_weekend.png`
- review and v2 (Renzo): `scripts/p1_07_review.py`, `scripts/p1_07_depeg_v2.py`, `data/processed/P1-07_depeg_events_v2.csv`,
  `results/tables/P1-07_v1_vs_v2.csv`, `results/figures/P1-07_svb_weekend_v2.png`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** S1–S7 done and reviewed. Nattan reviewed and approved Renzo's v2 fixes. Both v1 (F-012, 29 events) and v2 (F-013, 24 USD-confirmed, 11 falls below $1) sit side by side; no v1 file was changed. F-012 marked `exploratory` (superseded by v2), F-013 marked `confirmed` (checked by Nattan). New SVB figure `P1-07_svb_weekend_v2.png` (lowest hourly close $0.863, Sunday announcement 22:15 UTC marked, most recovery occurred before US banks reopened).
- **Next step (P3-04 / team):** Decide between a case table of the 11 falls vs widening the universe (more coins/venues like DAI, USDe, or pre-2021 USDT/USD sources). Check USDP delisting date. Sensitivity checks.

## Review (Renzo, 2026-10-31)
Reproduced with `.venv/bin/python scripts/p1_07_depeg.py`: 318 rows (29 USD-confirmed, 16 relative-price
candidates, 273 rejected), Bitstamp 120 rows, low 0.805. The definition commit (57597ab) precedes the script commit
(2a36549). The code implements the frozen definition. All numbers below: `.venv/bin/python scripts/p1_07_review.py`.

The three success criteria are met. The **claim in F-012 is not yet supported** as worded:
1. **16 of the 29 events are prices above $1** (12 below, 1 both ways). A coin at $1.01 is excess demand, closed by
   minting, not by redemption; the chapter asks how a coin *returns to $1 after falling*. Report the two directions
   separately; the chapter count is the events below $1.
2. **USTC (Mar 2023) is not an event.** It is UST after the May 2022 collapse, relisted under a new name; its first
   Binance candle is already $0.022. It double-counts UST's terminal event. The listing-artefact rule only checks
   candles after a >24 h gap, so it misses an episode that starts at a pair's first candle.
3. **Shared moves of USDT on Binance pass the USD check.** On 13 Dec 2023 BUSD/USDT and FDUSD/USDT rise to 1.006 in
   the same hour (closes within 0.0003 of each other) while Coinbase USDT/USD is 0.9995: USDT was cheap on Binance,
   two coins did not depeg together. Multiplying by Coinbase's USDT price cannot remove a Binance-only USDT move.
   "USD-confirmed" is weaker than it sounds; it means "survives Coinbase's USDT price".
4. **6 of the 9 censored events did recover.** Their Binance episodes ended 1–8 days later (BUSD and FDUSD
   13 Dec 2023, FDUSD Feb, Mar 2024 and Apr 2025, USDP Apr 2024). The direct check only looks at
   relative end + 12 h, so recovery after that is coded as "never recovered". This would bias survival curves.
   Real censoring: UST May 2022, USTC (point 2), USDP Sep 2026.
5. **Delistings.** USDP's data stops on 24 Sep 2026 (delisting `[verify]`); its two Sep 2026 events (one censored)
   may be wind-down drift, like BUSD's Dec 2023 event (pair ends 15 Dec 2023). UST's collapse also ends in a delisting,
   so a delisting flag must not drop it automatically.
6. **Reproducibility.** Coinbase USDT/USD is fetched live and not saved, although `data/raw/coinbase/USDT-USD-1h.csv`
   is frozen (P1-01). The Bitstamp file in `data/raw/` is rewritten on every run (raw data should be immutable).
   The pre-specified sensitivity checks (0.3%/1.0% start, 0.05%/0.25% recovery) are not run yet (P3-04 or P4-01).

Consequence: below $1, without USTC and the USDP delisting events, about **10–12 events** remain. The chapter plan
draws Kaplan–Meier curves only with ≥ 12 independent events, so the count decides the chapter's form.

**SVB figure.** Correct data and shading (bank close Fri 21:00 UTC, open Mon 13:30 UTC, after the US clock change).
- $0.805 is an intra-hour low on one venue; the lowest hourly close is **$0.863** (11 Mar 07h UTC), and 3 hours close
  below $0.90. Quote the close, or say "brief low".
- **Most of the recovery happened while banks were closed:** $0.86 → $0.97 over Saturday and Sunday; $0.968 → $0.989 in
  the hour of 22h UTC Sunday 12 Mar, around the US government's deposit guarantee announcement (time `[verify]`); only
  $0.991 → $0.999 at Monday's bank open (13–14h UTC). F-012's "recovering once banking channels reopened" is only
  partly right. For the chapter (redemption vs backing) this matters: news about the backing did most of the work.
- The footnote overlaps the x-axis label.

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
- 2026-11-01, Nattan: reviewed Renzo's v2 fixes; verified logic, directional separation, and shared-move filter; approved; status → done.
- 2026-10-31, agent for Renzo: S6/S7 done: v2 with the review fixes next to v1; 11 falls below $1 (F-013); SVB figure v2 with the 22:15 UTC announcement (D-13). Status review (Nattan or Jonathan).
- 2026-10-31, agent for Renzo: S5 review done (Review section; `scripts/p1_07_review.py`); 233 new raw files added to SHA256SUMS. Nattan asked Renzo to fix the points; S6/S7 added, status doing.
- 2026-10-31, agent for Renzo: Renzo takes the review.
- 2026-10-31, Nattan: status set to review; marked for review by Felipe or Renzo.
- 2026-10-31, Nattan: completed S2, S3, S4. Automated scan produced 318 screened candidates: 29 USD-confirmed independent events, 16 relative-price candidates, and 273 logged quality rejections. Generated SVB-weekend case figure `P1-07_svb_weekend.png` (Bitstamp USDC/USD trough $0.805 on 11 Mar 2023 07:00 UTC). Documented in F-012.
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
v1 (Nattan) below; v2 after the review fixes: F-013 (24 USD-confirmed, 11 below $1, 2 censored). Both kept for comparison.

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
