---
id: P2-01
title: Noise floor (how big a premium is just trading friction)
phase: P2
status: done
owner: CS 1
working: -
due: 2026-11-01
depends: P1-02
---

## Goal
Estimate the typical bid-ask spread of USDT/BRL so that any premium inside that band is treated as noise,
not evidence.

## Subtasks
- [x] S1 — Spread estimators from hourly high/low/close: Corwin-Schultz and Abdi-Ranaldo; daily median. — done: Renzo, 31 Oct
- [x] S2 — Compare with the probe's median hourly range (F-001). — done: Renzo, 31 Oct
- [x] S3 — Add the band to the premium chart. — done: Renzo, 31 Oct

## Success criteria
- [x] `data/processed/P2-01_noise_floor_daily.csv`
- [x] Finding written: typical spread in bps by year, and how the premium compares
- [x] Naive comparison shown: raw hourly range vs the estimators

## Outputs
- `scripts/p2_01_noise.py`, `data/processed/P2-01_noise_floor_daily.csv`, finding file

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** done (reviewed and verified by Jonathan). Finding F-007 reproduced; figures and noise floor daily CSV verified.
- **Next step (reviewer):** `python scripts/p1_02_premium.py && python scripts/p2_01_noise.py`; the printed table
  must match F-007; look at the two `results/figures/P2-01_*.png`. Then set `status: done`.
- **Open questions:** (1) Binance's tick change (~27 Jun 2025) needs its announcement (`[verify]`); it matters for the
  Jul 2025 step (note left in P2-02). (2) The two papers are cited from memory (L-01, L-02 `[verify]`).
- **How to resume / reuse:** the band for other charts is `noise_band_bps` in
  `data/processed/P2-01_noise_floor_daily.csv` (index `date_utc`, which equals the PTAX date for the 13–16h UTC window).

## Log
- 2026-10-31, Jonathan: review complete; scripts/p2_01_noise.py executed cleanly; tables, F-007 probe assertions and figures verified; status -> done
- 2026-10-31, agent for Renzo: S1–S3 done; F-007; tick change found (27 Jun 2025); status → review
- 2026-10-31, agent for Renzo: Renzo takes P2-01 (P1-02 in review)

## Result
The typical USDT/BRL spread fell from ~10 bps (2020–21) to ~2.5 bps (2026). The premium was 4–11 times that in
every year, so it is not trading friction, except in the quiet period Aug 2025 – Jun 2026, when it was only about
twice the spread (17% of days inside the band). Details and the yearly table: **F-007**.

Choices: both estimators on hourly bars, aggregated per UTC day with each paper's convention (CS: negative pair
estimates set to 0, then the mean; AR: mean of the products, then the square root of the positive part). Band =
± the 21-day rolling median of the larger of the two daily estimates (conservative, because AR under-reads).

**Column dictionary — `P2-01_noise_floor_daily.csv`** (one row per UTC day with USDT/BRL trades)

| Column | Meaning | Unit |
|---|---|---|
| `date_utc` | UTC calendar day (index) | date |
| `hours` | hourly candles present that day | count |
| `spread_cs_bps`, `spread_ar_bps` | Corwin–Schultz and Abdi–Ranaldo full spread estimates | bps |
| `range_median_bps` | naive baseline: median hourly (high − low) / close | bps |
| `tick_bps` | one price step (0.001 BRL until 26 Jun 2025, then 0.0001 BRL) relative to the day's median price | bps |
| `noise_band_bps` | band half-width: 21-day rolling median of max(CS, AR); empty for the first 9 days | bps |
