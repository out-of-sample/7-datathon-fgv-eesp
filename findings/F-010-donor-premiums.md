---
id: F-010
title: Where residents cannot buy dollars freely (ARS, UAH) USDT costs 4-7% more than the official dollar; in open markets 0-1%
status: exploratory
task: P1-05
date: 2026-10-31
checked_by: -
---

## Claim
We built the same USDT premium as for Brazil for nine other currencies (the donor pool of the synthetic control).
Where the official dollar is rationed by capital controls, the premium is large: in 2025 and up to 22 Jun 2026,
Argentina 5.5–7.2% and Ukraine 4.1–4.9%. Where it is not, it is small: euro, Turkish lira, Mexican peso, Polish zloty,
Indonesian rupiah and Colombian peso within ±0.7%, South African rand about 0.7–1.0%, Brazil 0.1–0.2%. This fits
the project's thread (a closed arbitrage channel lets the market price drift from the official one), but two
controlled currencies are a description, not a test.

## Evidence
Mean premium, bps (price of USDT in local currency / (official rate x USDT/USD) - 1), up to 22 Jun 2026:

| Currency | Official rate | 2024 | 2025 | 2026 (to 22 Jun) | Binance volume, M USD/month (Nov 2025 - Jun 2026) |
|---|---|---|---|---|---|
| BRL (PTAX, P1-02) | PTAX | 49 | 22 | 8 | 1,462 |
| BRL (ECB, check) | ECB | 56 | 25 | 12 | same |
| EUR | ECB | 7 | 1 | 1 | 667 |
| TRY | ECB | 51 | 1 | −7 | 1,182 |
| ZAR | ECB | 196 | 97 | 68 | 19 |
| MXN | ECB | 72 | 36 | 17 | 40 |
| PLN | ECB | 36 | 9 | 12 | 10 |
| IDR | ECB | – | 33 | 19 | 107 |
| COP | TRM | −217 | −69 | 22 | 15 |
| UAH | NBU | 853 | 490 | 412 | – |
| ARS | BCRA A 3500 | 3,037 | 721 | 548 | – |

- **Method check on Brazil.** Brazil measured the donor way (ECB rate at ~14:10 CET, Binance at 14:00 Frankfurt) vs the
  P1-02 PTAX premium: 1,510 common days, correlation 0.79, mean difference +3.9 bps, median absolute difference 16.5 bps.
  It finds the 23 Jun 2026 jump: +82.5 bps vs +93.9 with PTAX (20 days after minus 20 days before).
- **TRM dating.** Dating each TRM to the trades of the previous weekday gives a calmer COP premium (sd of daily change
  52.4 bps) than same-day dating (77.0 bps), Jul 2024 – 22 Jun 2026. We use the previous weekday.
- **Coverage, 1 Nov 2025 – 30 Sep 2026** (share of the currency's own fix days with a premium, pre / post 23 Jun):
  EUR, TRY, ZAR, MXN, COP, ARS 100% / 100%; UAH 100% / 96% (Binance pair ends 28 Sep 2026); IDR 87.5% / 100% (Binance
  pair starts 29 Nov 2025); PLN 100% / 7% (pair ends 1 Jul 2026).
- Reproduce: `python scripts/p1_05_donors.py` (prints the coverage table, the TRM test and the Brazil check; yearly
  means: `pd.read_csv("data/processed/P1-05_donor_premiums_daily.csv", parse_dates=["date"], index_col="date")[:"2026-06-22"]`
  grouped by year). Volumes: Binance column 5 (base volume) summed per month, EURUSDT converted with the close.

## Caveats
- Each currency is measured at its own fix time (ECB currencies ~14:10 CET; COP, UAH, ARS as a mean over local trading
  hours, which are `[verify]`). Single-instant measurement adds noise: on Brazil, 16.5 bps median gap between the two ways.
- ZAR, MXN, COP and PLN trade 10–40 million USD a month on Binance, so their premiums are noisier (ZAR sd 49 bps,
  COP sd 66 bps in the pre-period, vs 5 bps for EUR).
- The negative COP premium in 2024 (−217 bps) is not explained. The pair was listed in Jun 2024 and is thin.
- "Controlled" vs "open" is our classification from secondary sources (P1-05 Result, `[verify]`), with two controlled
  currencies. No causal claim.

## Used in deck
Not yet (candidate: one slide or annex table "the same mechanism across countries"; the donor data feeds P2-04).

## History
- 2026-10-31, agent for Renzo: created (exploratory)
