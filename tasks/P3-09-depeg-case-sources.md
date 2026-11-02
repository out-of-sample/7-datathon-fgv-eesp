---
id: P3-09
title: Open sources for the depeg case causes (restore them in the case table)
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-04
depends: P3-04
---

## Goal
The P3-04 review marked every cause in the 11-case depeg table as unsourced. Find an opened, quoted source for each
cause (and for the USDP end-of-data on Binance), so the deck can say why each stablecoin left $1 without guessing.

## Subtasks
- [x] S1 — Open and quote a source for each case cause, starting with FDUSD Apr 2025, TUSD Jan 2024, UST May 2022, and the USDP delisting — done: Felipe, 2 Nov
- [x] S2 — Restore the sourced causes in `results/tables/P3-04_depeg_case_table.csv` (via `scripts/p3_04_depeg_chapter.py`) and add the sources to `docs/sources.md`; leave "Causa não verificada" where nothing was found — done: Felipe, 2 Nov

## Success criteria
- [x] Every cause in the case table is either sourced (opened, one line quoted) or marked "não verificada"
- [x] F-019 History notes what changed

## Outputs
- `results/tables/P3-04_depeg_case_table.csv`, `docs/sources.md`

## Handoff
- **State:** Complete, in `review`. All 11 downward depeg cases from P1-07 v2 + the USDC SVB benchmark + the USDP Binance delisting (24 Sep 2026, announced 10 Sep 2026) now have opened, verbatim-quoted sources in `docs/sources.md` (`DP-01`..`DP-10`, `D-13`). Sourced causes restored in `results/tables/P3-04_depeg_case_table.csv` and `results/figures/P3-04_depeg_cases.png` via `scripts/p3_04_depeg_chapter.py`.
- **Next step:** Teammate (Renzo / Jonathan) checks `DP-01`..`DP-10` in `docs/sources.md` and marks `done`.
- **Open questions:** -
- **How to resume:** `py scripts/p3_04_depeg_chapter.py`

## Log
- 2026-11-02, agent for Felipe: S1–S2 completed (`status: review`). Added `DP-01`..`DP-10` to `docs/sources.md` (every URL opened with HTTP 200 and one verbatim quote); re-ran `scripts/p3_04_depeg_chapter.py` and updated `findings/F-019-depeg-chapter.md`.
- 2026-11-02, agent for Felipe: created from the P3-04 review's open item; Felipe takes it.

## Result
Opened and quoted primary/press sources for all 11 downward depeg events and the Binance USDP delisting (`DP-01`..`DP-10` in `docs/sources.md`), including Richmond Fed Economic Brief EB 22-24 for UST May 2022 (`DP-09`), SEC Release 2024-145 for TUSD Oct 2024 (`DP-05`), Protos for TUSD Jan 2024 (`DP-03`), Decrypt for FDUSD Apr 2025 (`DP-07`), USDP Signature Bank exposure (`DP-01`), UST Frog Nation (`DP-02`), TUSD Nov 2024 (`DP-06`), Livemint/Bloomberg for FDUSD Mar 2024 (`DP-04`), S&P Global Ratings via Nasdaq for TUSD Jun 2025 (`DP-08`), and Livecoins for Binance's 10 Sep 2026 USDP removal announcement (`DP-10`). Restored the sourced mechanisms in `results/tables/P3-04_depeg_case_table.csv` and updated `findings/F-019-depeg-chapter.md`.
