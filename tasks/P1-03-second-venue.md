---
id: P1-03
title: Find and download a second BRL venue for USDT
phase: P1
status: done
owner: CS 2
working: -
due: 2026-10-31
depends: -
---

## Goal
Check that the premium (and the 24 Jun 2026 jump) is not a Binance-only artefact by getting USDT/BRL prices
from a second exchange.

## Subtasks
- [x] S1 — Look for public historical USDT/BRL data (Mercado Bitcoin, Foxbit, or another Brazilian venue); hourly if
   possible, daily at minimum, covering at least 1 Jan - 30 Sep 2026. — done: Renzo, 31 Oct
- [x] S2 — Record the endpoint, limits and terms in `docs/sources.md` (row D-04). — done: Renzo, 31 Oct
- [x] S3 — Download to `data/raw/<venue>/` and add checksums and a manifest row. — done: Renzo, 31 Oct

## Success criteria
- [x] A second venue with coverage of Jan-Sep 2026, or a written explanation of why none is available
- [x] Source row D-04 updated to checked

## Outputs
- `scripts/p1_03_second_venue.py`, `data/raw/foxbit/USDTBRL-1h.csv`, `data/raw/mercadobitcoin/USDT-BRL-1h.csv`,
  `results/tables/P1-03_venue_coverage.csv`

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
-  **State:** done (reviewed and verified by Jonathan). Two Brazilian venues frozen (hourly, 30 Oct
  2026 cutoff), checksums added to `data/raw/SHA256SUMS`, manifest and D-04 filled.
- **Next step:** None for P1-03. Downstream tasks (P2-05) use frozen venue data.
- **Open questions:** (1) Mercado Bitcoin's general terms were read (D-04: no clause on research use of public
  prices; databases owned by MB, so we never share the raw file and we cite MB). The API terms
  (https://www.mercadobitcoin.com.br/politicas-termo-api) were read on 31 Oct: non-commercial research use is fine (D-04). Closed. (2) Why Foxbit's
  volume rose ~6× in July 2026 (see Result) is unknown; relevant to the economist's interpretation.
- **How to resume / reuse:** drop Foxbit rows with `volume_usdt == 0` (no trade); Foxbit `open` = previous close,
  so use closes (or Mercado Bitcoin's `o`, a true first trade) when matching the PTAX window.

## Log
- 2026-10-31, Jonathan: review complete; scripts/p1_03_second_venue.py executed cleanly; coverage and volume tables match Result exactly; SHA256SUMS passed; status -> done
- 2026-10-31, agent for Renzo: S1–S3 done: Foxbit + Mercado Bitcoin frozen; re-download byte-identical; status → review
- 2026-10-31, agent for Renzo: Renzo takes P1-03 (planned for Nattan in STATUS, unclaimed; Renzo to tell him)

## Result
Two Brazilian exchanges cover Jan–Sep 2026 hourly: **Foxbit** (trades from 7 Apr 2021) and **Mercado Bitcoin**
(from 11 Mar 2023). Both are frozen at 30 Oct 2026. Their prices track Binance closely: the median hourly gap is
5.5 bps for Mercado Bitcoin and 9.7 bps for Foxbit, which is on average 12.5 bps cheaper than Binance. Command:
`python scripts/p1_03_second_venue.py` (table also in `results/tables/P1-03_venue_coverage.csv`).

| Venue | Hours with trades | First trade hour (UTC) | Share of hours with trades | Longest no-trade stretch | Median \|close − Binance\| | Mean close − Binance |
|---|---|---|---|---|---|---|
| Foxbit | 45,789 | 2021-04-07 03h | 0.90 (2021), 0.84 (2022), ≥ 0.93 from 2023 | 9 h (2022-05-24) | 9.7 bps | −12.5 bps |
| Mercado Bitcoin | 30,889 | 2023-03-11 22h | 0.89 (2023), ≥ 0.99 from 2024 | 22 h (19–20 Apr 2026) | 5.5 bps | −0.6 bps |

No duplicate hours and no price row with the close outside high/low (after dropping Foxbit's zero-filled hours).

Venues checked and not used: OKX USDT-BRL (history from ~2024 only, 100 candles per call, international like
Binance), Bitso (`usdt_brl` exists; candles not checked), Bybit (blocks requests from this country), NovaDAX (API
host does not resolve).

**Volume (million USDT)**, from the same script:

| Year | Foxbit | Mercado Bitcoin | Binance |
|---|---|---|---|
| 2021 | 9 | – | 6,184 |
| 2022 | 18 | – | 5,345 |
| 2023 | 74 | 20 | 3,127 |
| 2024 | 356 | 209 | 6,741 |
| 2025 | 417 | 788 | 14,079 |
| 2026 (to 30 Oct) | 4,894 | 469 | 16,471 |

Foxbit traded 100–190 million USDT a month in Jan–Jun 2026 and **0.9–1.1 billion a month from July 2026**. The
number of trades did not rise (92–218 thousand a month before, 146–201 thousand after); the average trade grew from
0.9–1.3 thousand USDT (Jan–Jun) to 5.4–6.6 thousand (Jul–Oct). It starts right
after the 23–24 Jun jump. Larger players moving to a domestic venue, or a market-making or reporting change at
Foxbit, are both possible; nothing here tells them apart `[verify]`. Recorded as **F-008**.
