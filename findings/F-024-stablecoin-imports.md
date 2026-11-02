---
id: F-024
title: In July 2026 stablecoin purchases abroad fell 78% (BCB) while the premium rose; they stayed at about a third of their earlier level through September while the premium fell back
status: confirmed
task: P3-10
date: 2026-11-02
checked_by: Felipe
---

## Claim
The month after the 23 Jun notice, Brazilian residents' net purchases of stablecoins abroad fell from US$ 2,542 mn
(June) to US$ 572 mn (July 2026), −78%. That is beyond the normal range of monthly changes in the BCB series
(empirical p = 0.02; robustness p = 0.05), and the largest percentage fall since the series passed US$ 100 mn a month
in 2021. In the same months the premium rose (monthly mean 11 → 43 → 81 bps, May–Jul). A higher price with a lower
quantity is what a closed supply channel produces. In Aug–Sep purchases stayed at 32% of their Jan–May 2026 level
(US$ 702 mn and 843 mn) while the premium fell back to 33 and 23 bps, so the fade is **not** explained by this import
channel reopening (pre-set rule: 0.25 ≤ R < 0.5, "partial, inconclusive").

## Evidence
- Series: BCB external-sector statistics, Tabela 11, "dos quais: criptoativos com passivo correspondente" = SGS 29644,
  US$ mn per month, Jan 2019 – Sep 2026 (93 months), frozen 2 Nov 2026 (D-16). Reproduces the press figures for Jun and
  Jul 2026 (InvestNews 28 Aug) and the BCB note's US$ 1.4 bn for Jul 2025.

| Month (2026) | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep |
|---|---|---|---|---|---|---|---|---|---|
| Purchases, US$ mn | 2,375 | 2,140 | 2,282 | 2,709 | 2,632 | 2,542 | 572 | 702 | 843 |
| Premium, monthly mean, bps | 8 | 5 | 5 | 5 | 11 | 43 | 81 | 33 | 23 |

- Tests (specification in `tasks/P3-10-stablecoin-imports.md`, committed before the download, `c6a1c1b`):

| Test | Value | Comparison | Result |
|---|---|---|---|
| T1 log change Jun → Jul 2026 | −1.49 (−78%) | 91 other monthly changes; 1 as large (Apr 2020, US$ 19.5 mn → 0.2 mn) | p = 0.022, beyond normal range |
| T1b Jul vs mean of Jan–May 2026 | −1.45 (−76%) | 86 other months; 3 as large (Apr 2020, May 2020, Sep 2019, all below US$ 20 mn a month) | p = 0.046, beyond normal range |
| T2 fade: mean(Aug, Sep) / mean(Jan–May 2026) | 0.32 | rule: ≥ 0.5 recovered, < 0.25 not recovered | partial (inconclusive) |
| T3 correlation, monthly purchases vs premium, Jan 2024 – Sep 2026 | −0.62 | 33 months | description only |

- On exchanges, PTAX-day windows around 23 Jun (`results/tables/P3-10_order_flow.csv`):

| Venue | Measure | Before [−20,−1] | Spike [+1,+20] | After [+21,+60] |
|---|---|---|---|---|
| Binance | volume, M USDT/day | 58.4 | 77.6 | 55.2 |
| Binance | buyer-initiated share | 0.52 | 0.49 | 0.51 |
| Foxbit | volume, M USDT/day | 4.3 | 30.7 | 31.6 |
| Foxbit | average trade, USDT | 730 | 4,687 | 6,297 |
| Foxbit | buyer-initiated share | 0.62 | 0.30 | 0.60 |
| Mercado Bitcoin | volume, M USDT/day | 0.95 | 1.25 | 1.38 |

  The Binance volume rise (+33%) is not unusual: 68 of 200 P2-03 placebo dates show a change at least as large
  (two-sided p = 0.34).
- Reproduce: `python scripts/p3_10_imports.py` → `data/processed/P3-10_imports_monthly.csv`,
  `results/tables/P3-10_imports.csv`, `results/tables/P3-10_order_flow.csv`, `results/figures/P3-10_imports.png`.

## Caveats
- **Other July causes.** The BCB statistician attributes the fall to "reorganização do mercado de ativos virtuais num
  contexto de intensificação da regulação e da supervisão de conduta" (D-16), which fits the notice but does not name
  it. Res. BCB 580 (1 Jul 2026, E-10) also falls in July; its prudential rules apply only from 1 Jan 2027. Monthly data
  cannot separate the two.
- The line counts all residents' net stablecoin purchases abroad recorded by the BCB, not only funds' imports. How the
  BCB compiles it (which transactions it sees) is not documented here `[verify]`.
- June includes 24–30 Jun, after the notice; June (2,542) is close to the Jan–May mean (2,428), so no rush or early drop
  is visible.
- The BCB note of 27 Aug gave June as US$ 2.6 bn; SGS today gives 2,542 (possibly revised). It does not change T1.
- T3 is mostly two opposite trends (purchases grew and the premium fell over 2024–2026); it is not evidence of the
  mechanism.
- Foxbit's volume rise (F-008) may have causes unrelated to the notice; its buyer-side definition is `[verify]`.
- Deviation from the specification: the Aug and Sep 2026 values were printed while identifying the series, after the
  specification was committed (`c6a1c1b`) and before the script ran. Thresholds and tests were not changed.

## Used in deck
Slide 5 (`deck/deck_v1_ptbr.md`) & Anexo B.7 (`deck/annex_v1_ptbr.md`).

## History
- 2026-11-02, agent for Renzo: created (P3-10).
