---
id: F-007
title: Trading friction on USDT/BRL is 2–10 bps; the premium is 4–11 times that every year, but only ~2 times it from Aug 2025 to Jun 2026
status: frozen
task: P2-01
date: 2026-10-31
checked_by: Jonathan
---

## Claim
The typical bid-ask spread on Binance USDT/BRL, i.e. the cost of buying and selling straight back, fell from about
10 bps (0.10%) in 2020–21 to about 2.5 bps in 2026. In every year the median premium over PTAX was 4 to 11 times
that spread, so it is not trading friction. The exception is the quiet period from 1 Aug 2025 to 22 Jun 2026:
there the premium (median 8.4 bps) was only about twice the spread and sat inside the noise band on 17% of days.
After 24 Jun 2026 it was about 20 times the spread (median 81 bps) and never inside the band.

## Evidence
Yearly medians of daily values, bps (spread = full proportional spread (ask − bid) / mid):

| Year | Corwin–Schultz | Abdi–Ranaldo | Naive: hourly range | One price tick | Median premium | Premium ÷ band | Days inside band |
|---|---|---|---|---|---|---|---|
| 2020 (from 13 Oct) | 9.1 | 12.6 | 24.0 | 1.8 | 96.0 | 7.3 | 2% |
| 2021 | 10.3 | 8.7 | 29.1 | 1.8 | 83.2 | 7.4 | 3% |
| 2022 | 7.9 | 5.3 | 18.7 | 1.9 | 53.2 | 6.1 | 6% |
| 2023 | 4.5 | 2.9 | 12.2 | 2.0 | 59.6 | 11.4 | 1% |
| 2024 | 4.0 | 3.5 | 12.0 | 1.8 | 51.1 | 10.1 | 3% |
| 2025 | 3.5 | 3.5 | 11.0 | 0.2 | 18.2 | 4.3 | 5% |
| 2026 (to 30 Oct) | 2.5 | 2.2 | 7.6 | 0.2 | 13.1 | 3.6 | 14% |

- Band = ± the 21-day rolling median of the larger of the two daily estimates. "Inside" = |premium| ≤ band.
- 1 Aug 2025 – 22 Jun 2026: median premium 8.4 bps, median band 3.9 bps, 17% of days inside.
  24 Jun – 31 Jul 2026: median premium 80.9 bps, median band 3.8 bps, 0% inside.
- Naive baseline: the probe's median hourly range (F-001) is reproduced exactly; it is about 3 times the estimators,
  because it also contains price moves within the hour.
- Binance cut the USDT/BRL price step from 0.001 to 0.0001 BRL on about 27 Jun 2025 (first finer price in our data:
  27 Jun 2025 05:00 UTC; Binance announcement verified in M-03; literature formulas L-01/L-02 verified). Before that, no quoted spread could be below ~1.9 bps.
- Live check (Binance public market data, Sat 31 Oct 2026 16:43 UTC, one snapshot): bid 5.3800, ask 5.3804 = 0.74 bps.
- Reproduce: `python scripts/p2_01_noise.py` → printed tables, `data/processed/P2-01_noise_floor_daily.csv`,
  `results/figures/P2-01_premium_noise_band.png`, `results/figures/P2-01_spread_estimators.png`.

## Caveats
- Both estimators were designed for daily bars; on hourly bars with tiny spreads they are noisy. Abdi–Ranaldo hits
  0 in several months (below the one-tick minimum, so it under-reads); Corwin–Schultz stays at or above one tick
  until the tick change. Both are above the live quoted spread, so the band is probably too wide, not too narrow:
  it makes it harder, not easier, to call a premium real.
- The band covers the exchange spread only. Trading fees, the bank's FX spread and IOF are left out; P3-01 adds them.
- One venue. The second venue (P1-03) may have a wider spread.

## Used in deck
Not yet (planned: the shaded band on headline chart 1).

## History
- 2026-11-04, agent for Renzo (P4-03, Renzo's decision): status confirmed -> frozen (tag `results-frozen`); from now on only bug fixes, each disclosed here
- 2026-10-31, Jonathan: reviewed and verified (independent clean run reproduces table, noise band CSV and figures); confirmed.
- 2026-10-31, agent for Renzo: created (status confirmed: P2-01 criteria pass; not yet re-run by a teammate)
