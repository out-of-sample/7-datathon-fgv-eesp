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
one on Binance. The surge coincides with Foxbit taking over clients of NovaDAX, which closed its Brazilian operations (M-04, announced
7 Jul 2026), during a wider wave of exchange exits. A client migration would more naturally add trades than enlarge
them, so M-04 does not obviously explain the pattern of bigger trades; the cause is open.

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
  limits-to-arbitrage story, but so does a Foxbit-specific cause such as the NovaDAX client migration (M-04).
- Mercado Bitcoin, the larger domestic venue in 2025, shows no rise, which argues for something Foxbit-specific.

## Used in deck
Not used.

## History
- 2026-11-02, agent for Renzo: M-04 wording "matched … adaptation following Res. BCB 580 and IN RFB 2.291" replaced by "coincides with"; the M-04 source names neither rule (docs/sources.md). Noted that a client migration fits "more trades" better than "bigger trades"
- 2026-11-01, Felipe: P1-04 matched the surge to M-04 (7 Jul 2026 Foxbit–NovaDAX user-migration partnership following NovaDAX exit, Res. BCB 580 and IN RFB 2.291/2025 entry into force), consolidating domestic order-book liquidity and explaining the July volume rise.
- 2026-10-31, agent for Renzo: news search (P2-05 S3) found no explanation. One unopened lead: a startupi.com.br
  article dated 10 Sep 2026 on a R$ 110 million investment in Foxbit, whose snippet mentions strengthening its OTC desk
  (https://startupi.com.br/foxbit-recebe-investimento-de-r-110-milhoes/) `[verify]`.
- 2026-10-31, agent for Renzo: created from the P1-03 audit (status exploratory)
