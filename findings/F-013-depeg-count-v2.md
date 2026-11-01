---
id: F-013
title: After the review fixes, the depeg screen finds 11 falls below $1 (9 without a likely delisting), short of the 12 the chapter needs for recovery curves
status: exploratory
task: P1-07
date: 2026-10-31
checked_by: -
---

## Claim
We applied Nattan's depeg screen (F-012, "v1") with the six review fixes ("v2"). Of v1's 29 events, 24 pass the
check against the dollar price, but only **11 are falls below $1**. The other 13 are prices above $1, which reflect
excess demand rather than a loss of trust. Two of the 11 (USDP, Sep 2026) are probably drift before a delisting. The
11 are separate shocks: no two start within 48 hours of each other. The chapter plan draws recovery (Kaplan–Meier)
curves only with at least 12 independent events, so with this data the chapter is a case table.

## Evidence
v2 counts below. Columns are v2's verdict, rows are v1's, over the 54 screen candidates:

| v1 \ v2 | USD-confirmed | rejected | relative-price candidate |
|---|---|---|---|
| USD-confirmed | 24 | 5 | 0 |
| rejected | 0 | 9 | 0 |
| relative-price candidate | 0 | 0 | 16 |

- **Rejected by v2:**
  - USTC, Mar 2023: the series starts at its first candle, $0.022, so it is UST relisted rather than a new event.
  - BUSD and FDUSD, 13 Dec 2023: they move together; within 0.1% of each other at the peak hour.
  - BUSD and TUSD on the SVB weekend: the same shared-move rule applies.
- **Ends added:** 4 events that v1 marked as never recovered now have a recovery date: FDUSD Feb and Mar 2024, FDUSD Apr 2025, USDP Apr 2024.
  - FDUSD Apr 2025 recovers on 23 Apr in dollar terms, against 10 Apr on Binance.
  - Censored in v2: UST May 2022 and USDP 23 Sep 2026 only.
- **The 11 falls below $1:**

  | Coin | Episodes | Notes |
  |---|---|---|
  | TUSD | Jan–Feb 2024, Oct–Nov 2024, Nov 2024, Jun–Oct 2025 | low $0.954 in Jan 2024 |
  | UST | Jan 2022; May 2022 | the May collapse ends in delisting and is kept |
  | FDUSD | Mar 2024; Apr 2025 | low $0.965 in Apr 2025 |
  | USDP | SVB weekend Mar 2023 | low $0.974 |
  | USDP | 15–18 Sep 2026; 23 Sep 2026 | both flagged: USDP's data ends 24 Sep |

- **SVB weekend (Bitstamp USDC/USD):** the lowest hourly close is $0.863 (11 Mar 07h UTC); the intra-hour low of
  $0.805 is in the same hour. The price closed at $0.968 at 21h UTC Sunday 12 Mar. It was $0.989 by 23h, after
  the deposit guarantee announcement at 22:15 UTC (D-13). It closed at $0.991 at 12h Monday, before the bank open,
  and $0.999 at 14h. Most of the recovery happened before banks reopened. Figure:
  `results/figures/P1-07_svb_weekend_v2.png`.
- Reproduce: `.venv/bin/python scripts/p1_07_depeg_v2.py` (~3 min, no downloads; needs `scripts/p1_07_depeg.py`
  run once). Outputs:
  - `data/processed/P1-07_depeg_events_v2.csv`;
  - `results/tables/P1-07_v1_vs_v2.csv`;
  - the figure.

  It first checks that v1's rule on the frozen Coinbase file gives v1's 29; it does.

## Caveats
- **Shared-move rule.** We wrote it after seeing the 13 Dec 2023 case, so it is not pre-specified. It also removed
  BUSD and TUSD on the SVB weekend. Two coins at the same price to within 0.1% most likely means USDT moved on Binance,
  but this is a judgement. Without the rule, TUSD's SVB episode (down and up) would make 12 events.
- **Two venues, one band.** Dollar prices multiply Binance stablecoin/USDT by Coinbase USDT/USD. Small differences
  between the two venues can delay a measured recovery inside the 0.1% band; FDUSD in Apr 2025 is 13 days later
  than on Binance alone.
- **Pre-2021 candidates.** The 16 candidates from before May 2021 are not counted: Coinbase USDT/USD starts then.
  Many of them start at the same hour in several pairs, so they are probably USDT moves.
- **Coverage.** One venue (Binance), seven coins. DAI, USDe and other stablecoins without a Binance USDT pair are not
  screened.
- **Not run yet.** The pre-specified sensitivity checks (0.3% / 1.0% start, 0.05% / 0.25% recovery). The USDP
  delisting date is `[verify]`.

## Used in deck
Not yet. P3-04 decides between a case table and recovery curves, and whether more coins or venues are worth adding.

## History
- 2026-10-31, agent for Renzo: created (exploratory) from the P1-07 review fixes; F-012 kept for comparison
