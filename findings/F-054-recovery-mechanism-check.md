---
id: F-054
title: Foxbit flow does not distinguish the July recovery mechanism from a common episode trend
status: exploratory
task: P3-47
date: 2026-11-08
checked_by: -
---

## Claim
In the single June–September 2026 episode, seller-initiated Foxbit trading and the premium moved together, but the evidence does **not** show that this trading drove the premium back down. Comparing days within the same calendar week, the premium–flow slope is +0.0406 million USDT per basis point, with a week-bootstrap 95% interval of −0.0050 to +0.1948. Afternoon net selling does not predict the next PTAX-day premium change after controlling for the current premium and Foxbit–Binance gap: −0.129 bps per million USDT (interval −0.706 to +0.420); with week effects, +0.148 (−0.404 to +0.695). The apparent price response in F-032 may reflect the shared episode trend. This is a sensitivity result, not proof that selling had no effect.

## Evidence
The fixed specification was committed as `d497233` before this script ran. Reproduce from the frozen raw file:
`.venv/bin/python scripts/p3_47_recovery_check.py` → `results/tables/P3-47_recovery_checks.csv` and `results/tables/P3-47_coverage.csv`.

The Foxbit raw SHA-256 matches `data/raw/SHA256SUMS`: `b761de3a2a52b6fd111009d57631076cc34615c7ddec52fc2aeb7671d4755a73`. The analysis has 70 PTAX days in 15 Monday–Sunday weeks, 24 June–30 September 2026. All 350 expected 13:00–18:00 Brasília Foxbit hours are present, with no zero-volume hours or days. Median afternoon volume is 16.68 million USDT/day (range 3.95–31.74 million). Rebuilt net flow differs from the rounded P3-19 daily table by at most 0.000049 million USDT.

| Check | Estimate | 95% interval, week bootstrap | Reading |
|---|---:|---:|---|
| Original daily slope, premium → net seller-initiated flow | +0.0512 million USDT/bp | −0.0187 to +0.1236 | Same point estimate as F-032, but interval now includes zero when whole weeks are resampled instead of five-day moving blocks. |
| Within-calendar-week slope | +0.0406 million USDT/bp | −0.0050 to +0.1948 | The association is imprecise after removing each week's average. |
| Within-week normalized imbalance slope | +0.00164 share/bp | −0.00100 to +0.01256 | No clear association in the imbalance as a fraction of afternoon volume. |
| Afternoon net flow → next PTAX-day premium change | −0.129 bp/million USDT | −0.706 to +0.420 | Direction fits price pressure, but interval includes zero. |
| Same forward check with week effects | +0.148 bp/million USDT | −0.404 to +0.695 | Direction reverses; interval includes zero. |

The no-flow baseline (current premium and Foxbit–Binance gap) explains 10.62% of the next-day change's *in-sample* variation without week effects; adding flow lifts this to 10.76% (+0.14 percentage points). Within weeks, 49.26% becomes 49.35% (+0.09 points). These are in-sample fits, **not** forecast performance. The forward sample has 69 PTAX-day pairs.

**Threshold audit.** Re-fitting F-032's hinge on the same 70 days gives a 35 bp *kink*, −0.08355 million USDT fitted flow below it, and a +0.05376 million USDT/bp slope above it. The fitted zero crossing is 36.55 bp. Thus F-032's “near 35 bp” language is numerically close, but the kink and zero crossing are distinct, and neither identifies an arbitrage route cost.

## What remains possible
- **Supply adjustment via another intermediary or existing inventory:** large, business-hours trades and Foxbit's higher venue share fit this, but trade initiation cannot identify deposits, net imports or traders (F-031, F-036). The new within-week and forward tests do not establish price pressure.
- **Reduced demand or a change in who trades:** BCB-measured net purchases abroad stayed low (F-024). Those monthly net purchases are not the same quantity as exchange turnover; the three-venue data do not separate a demand shift from more active supply.
- **Venue-specific activity:** Foxbit's B2B desk relaunch and client-transfer partnerships overlap the period (F-008, F-036). Exchange-reported volume can also change with market making or reporting. The observed share is not a national market share.
- **The original fund channel resumed for some institutions:** no public resumption was found (F-030), but institution-by-institution alignment could be confidential. This cannot be ruled out from the public record.

## Caveats
- The question arose after seeing F-031/F-032; this is one episode, and 70 days are not 70 independent policy events.
- Calendar-week effects remove broad timing but do not remove shared within-week shocks. Fifteen weeks give wide bootstrap intervals; intervals containing zero do not establish zero economic effect.
- The 5-day block and whole-week bootstrap answer different dependence assumptions. The loss of interval exclusion is a sensitivity warning, not an independent refutation of F-032's point estimate.
- Morning premium precedes afternoon flow; the next-day change follows it. That order reduces mechanical simultaneity but does not eliminate unobserved common drivers or passive orders.
- The forward regressions are descriptive, in-sample. Their R² values are not out-of-sample prediction scores or causal effect sizes.
- Foxbit's candle field meaning was checked in F-031 against its API documentation, but these aggregated candles do not identify accounts, wallets, OTC/P2P flow or trades executed through a particular route.

## Used in deck
Not used. Independent teammate reproduction and Felipe's deck decision are pending. Safe Portuguese sentence if reviewed: “O prêmio caiu enquanto havia vendas agressivas na Foxbit, mas, ao comparar dias da mesma semana, essa associação ficou imprecisa; o fluxo também não antecipou uma queda detectável no dia útil seguinte. A causa da recuperação permanece aberta.”

## History
- 2026-11-08, Codex for Renzo: created after the registered P3-47 sensitivity and forward checks; all stated results came from the script above.
