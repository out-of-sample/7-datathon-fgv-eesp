---
id: F-025
title: In the four weeks after the notice, buyers of USDT/BRL paid about R$ 106 mn more on Binance (R$ 145 mn on three exchanges) than at the pre-notice premium; no ordinary month comes close
status: frozen
task: P3-11
date: 2026-11-02
checked_by: Felipe
---

## Claim
From 24 Jun to 21 Jul 2026, R$ 11.2 bn of USDT changed hands on Binance's USDT/BRL market (R$ 15.8 bn on Binance,
Foxbit and Mercado Bitcoin). Buyers paid on average 95 bps above the pre-notice premium, so about **R$ 106 mn** went
from buyers to sellers on Binance alone (**R$ 145 mn** on the three exchanges). The notice worked like a tariff of
about 0.95% on buying digital dollars, collected by whoever could still supply them, not by the government. None of
194 ordinary placebo months moved more than R$ 35 mn (p = 0.005).

## Evidence
Spike window 24 Jun – 21 Jul 2026 (PTAX days [+1, +20], 28 calendar days); pre-notice level 15.2 bps.

| Variant | Binance: R$ mn (tariff equivalent, bps) | 3 exchanges: R$ mn (bps) |
|---|---|---|
| **Headline: excess over the 20-day pre-notice mean** | **106.1 (94.9)** | **145.3 (92.2)** |
| Pre window 10 days | 109.2 (97.6) | 149.6 (94.9) |
| Pre window 40 days | 110.7 (99.0) | 151.8 (96.3) |
| Synthetic-control gap +109.31 bps (F-017) | 122.2 (109.3) | 172.3 (109.3) |
| After window [+21, +60] (description only) | 30.9 (19.2) | 49.7 (19.3) |

Per exchange (headline): Binance R$ 106.1 mn on R$ 11.18 bn; Foxbit R$ 37.4 mn on R$ 4.40 bn; Mercado Bitcoin
R$ 1.8 mn on R$ 0.18 bn.

Placebo (Binance, 194 P2-03 placebo dates with full data): tariff equivalent 5% / 50% / 95% = −24.1 / 0.1 / 35.5 bps;
transfer −6.1 / 0.0 / 11.3 R$ mn; largest R$ 35.5 mn. None reaches |94.9| bps: k = 0, p = 1/195 = 0.005.

Reproduce: `python scripts/p3_11_money.py` → `results/tables/P3-11_transfer.csv`, `results/tables/P3-11_placebo.csv`.
Specification committed before the script (`91f9c25`).

## Caveats
- **A transfer, not a welfare loss.** Each real above the old premium paid by a buyer was received by a seller; the
  loss to the economy (trades that did not happen, costlier routes) is not measured.
- **Gross, partial market.** Exchange-reported volume on three venues; OTC desks, other exchanges and P2P are missing,
  so the market-wide figure is larger. Arbitrageurs can be on both sides of the same volume.
- **Foxbit's volume** has open questions (F-008); the headline uses Binance alone for that reason.
- **Who received it is inferred, not measured.** Sellers at the higher price were those who could still bring USDT in
  (F-024: purchases abroad −US$ 2.0 bn in July). We do not see their identity.
- The after window (+R$ 31 mn on Binance, 19 bps) is shown for completeness: F-022 found that level not distinguishable
  from ordinary drift (placebo p = 0.24), so it is not claimed as an effect.
- Context, not a test: the route the notice closed paid zero IOF-Câmbio against 3.5% on the ordinary route (E-05.10,
  decree not opened). The 95 bps tariff equivalent is about a quarter of that 350 bps gap.

## Used in deck
Slide 10 (`deck/deck_v1_ptbr.md`) & Anexo B.5 (`deck/annex_v1_ptbr.md`).

## History
- 2026-11-04, agent for Renzo (P4-03, Renzo's decision): status confirmed -> frozen (tag `results-frozen`); from now on only bug fixes, each disclosed here
- 2026-11-02, agent for Renzo: created (P3-11).
