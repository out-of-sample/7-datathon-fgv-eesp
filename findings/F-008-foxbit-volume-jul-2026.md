---
id: F-008
title: Foxbit's USDT/BRL volume rose about sixfold from July 2026, through bigger trades, not more trades
status: exploratory
task: P1-03
date: 2026-10-31
checked_by: -
---

## Claim
On Foxbit, a Brazilian exchange, USDT/BRL volume went from 100–190 million USDT a month (Jan–Jun 2026) to
0.9–1.1 billion a month (Jul–Oct 2026), right after the 23–24 Jun premium jump. The number of trades did not rise;
the average trade grew about fivefold. The same months show no such rise on Mercado Bitcoin, and a much smaller
one on Binance. Why this happened is not known.

## Evidence
Monthly traded volume (million USDT) and Foxbit trade counts, 2026:

| Month | Foxbit | Mercado Bitcoin | Binance | Foxbit trades (thousand) | Foxbit average trade (USDT) |
|---|---|---|---|---|---|
| Jan | 109 | 47 | 1,173 | 94 | 1,158 |
| Feb | 141 | 37 | 1,208 | 112 | 1,265 |
| Mar | 134 | 51 | 1,512 | 149 | 899 |
| Apr | 100 | 58 | 1,383 | 110 | 905 |
| May | 124 | 46 | 1,535 | 92 | 1,346 |
| Jun | 189 | 32 | 1,926 | 218 | 869 |
| Jul | 1,085 | 40 | 2,207 | 173 | 6,262 |
| Aug | 902 | 37 | 1,624 | 146 | 6,198 |
| Sep | 1,019 | 56 | 1,844 | 155 | 6,556 |
| Oct (to 30) | 1,091 | 67 | 2,059 | 201 | 5,424 |

Reproduce: `python scripts/p1_03_second_venue.py` (last printed table; data frozen by P1-01 and P1-03).

## Caveats
- Exchange-reported volume. A market-making programme, fee promotion, wash trading or a reporting change at Foxbit
  would look the same. Nothing here tells those apart from real new demand.
- Timing alone is not a cause. "Large players moved to a domestic venue after the June notice" fits the
  limits-to-arbitrage story but is untested `[verify]`: look for Foxbit announcements (fees, institutional or OTC
  desk, market makers) in June–July 2026 (P2-05 S3).
- Mercado Bitcoin, the larger domestic venue in 2025, shows no rise, which argues for something Foxbit-specific.

## Used in deck
Not used.

## History
- 2026-10-31, agent for Renzo: created from the P1-03 audit (status exploratory)
