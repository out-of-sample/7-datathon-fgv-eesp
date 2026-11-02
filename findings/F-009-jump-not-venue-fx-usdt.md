---
id: F-009
title: The 24 Jun 2026 jump appears on three exchanges by the same amount and is not explained by the real, USDT/USD or a Binance event
status: confirmed
task: P2-05
date: 2026-10-31
checked_by: Jonathan
---

## Claim
The premium jump after 23 Jun 2026 is not a Binance artefact: on Binance, Foxbit and Mercado Bitcoin it rose by
93–95 bps (20-day averages before vs after). It is not a move in the real: the 24 Jun PTAX change (+0.68%) was
ordinary, and on comparable days the premium usually falls slightly. It is not USDT's own dollar price (unchanged
within 1 bps). No exchange-specific event was found. What remains is a Brazil-wide change in the USDT/BRL price
starting on the afternoon of 23 Jun, consistent with, but not proof of, the reported BCB notice (P1-04, P2-03, P2-04).

## Evidence
- **Three venues (S1).** Mean window premium, 20 PTAX days before (25 May – 22 Jun) vs after (24 Jun – 21 Jul):
  Binance 15.2 → 109.1 (+93.9 bps), Foxbit 14.7 → 108.0 (+93.3), Mercado Bitcoin 10.7 → 105.6 (+94.9). Daily values
  agree within a few bps (24 Jun: 155 / 152 / 148; 25 Jun: 184 / 185 / 156).
- **The real (S2).** PTAX +0.68% on 24 Jun: 34% of PTAX days since Oct 2020 moved more. On the 246 earlier days when
  PTAX rose at least that much, the premium changed by −18.7 bps on the day (−2.7 after 5 days, −2.8 after 20) on
  average; on 24 Jun it rose +130.6 (+96.2 after 5 days, +23.5 after 20). PTAX volatility over the previous 20 days
  was 0.77% per day, close to the 0.71% median since 2020. The larger PTAX move of 18 Jun (+1.9%) left the premium at −5 bps.
- **USDT/USD (S2).** Mean in the PTAX window before / after: Binance-based −7.7 / −8.5 bps, Coinbase −11.0 / −11.5 bps.
- **Exchange events (S3).** Searched news for Binance BRL deposit/withdrawal problems in Jun–Jul 2026: none found
  (the documented suspension is Jun–Jul 2022). A Binance-only event could not move Foxbit and Mercado Bitcoin anyway.
- **Data error.** Three independent price sources agree; the move lasts weeks, so a one-day PTAX error cannot cause it.
- **Timing (S4).** Premium against the last published PTAX: in the 23 Jun PTAX window it was at its earlier level
  (window premium 25 / 26 / 19 bps, vs 20-day means of 15 / 15 / 11); against the 23 Jun PTAX it was 42–63 bps at
  16–20h UTC (13–17h Brasília), 74–86 bps at 21–23h UTC and 69–92 bps overnight, then 207–246 bps on the 24 Jun open
  (12–15h UTC, which includes that morning's move in the real) and 107–144 bps against the new PTAX.
- Reproduce: `python scripts/p2_05_checks.py` (prints all of the above; `results/tables/P2-05_venues_daily.csv`,
  `results/figures/P2-05_hourly_22_26_jun.png`).

## Caveats
- The hourly view compares crypto prices with the last official fix; between fixes it also contains the real's own
  moves. We have no intraday official rate, so "started on the afternoon of 23 Jun" is approximate.
- The three venues share arbitrageurs; their agreement rules out a venue artefact, not a common crypto-market cause.
  The synthetic control (P2-04) with other countries addresses that.
- No independent rate (e.g. FRED DEXBZUS) was used to cross-check PTAX: FRED blocks our script. A manual browser download
  would close this.
- The news search for exchange events is not exhaustive (Binance's own announcement pages were not searched directly).

## Used in deck
Not yet (candidate: one robustness line "same jump on 3 exchanges", and the hourly figure in the annex).

## History
- 2026-10-31, agent for Renzo: created (status confirmed: P2-05 criteria pass; not yet re-run by a teammate)
