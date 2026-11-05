---
id: F-028
title: We cannot identify which route set the price after the 23 Jun notice; the ordinary 3.5% route did not set it (the premium rose at most +171 bps, and raising that route's IOF in May 2025 moved it +13 bps)
status: frozen
task: P3-15
date: 2026-11-02
checked_by: -
---

## Claim
**Why +94 bps and not +350.** The two numbers measure different things. +93.9 bps is the change in a market price
(F-016). 350 bps is the IOF difference between the closed funds' route (0%) and an ordinary purchase of foreign
currency (3.5%): a tax rate on one kind of FX transaction, not a price. Two observations say the ordinary 3.5% route
was not the one setting the USDT price:
1. after the notice the premium stayed far below +350 bps on every day: the highest daily premium was 185.9 bps on
   3 Jul 2026, **+170.7 bps** over the pre-notice level of 15.2 bps;
2. when that route's IOF itself rose by 240 bps (1.1% → 3.5%, decree of 22 May 2025), the premium moved **+13.2 bps**,
   inside the range of ordinary dates (placebo p = 0.38, F-026).

We cannot tell whether cheaper supply remained available, buyers bought less, or both. We do **not** call the 3.5%
route a ceiling: a route caps the premium only if it can supply USDT legally and at scale, and no opened source shows
that (route 3 in the table: "unknown").

**Which route set the price: not identified** (outcome (b) of the rule committed in `6393330` before the comparison).
Of six routes, one has an excess cost inside the spike's range: a remittance abroad "com finalidade de investimento"
at 1.10% IOF, 110 bps over the closed route (range +73.7 to +128.3 bps; synthetic control +109.3). This is a
**coincidence of magnitude we cannot interpret**. No opened source says that category can carry virtual assets, and
cheaper routes of unknown status stayed open: funds investing on their own account and arbitraging inside exchange order
books (0% IOF; on 26 Jun the BCB "'liberou'" that arbitrage, E-05.5), goods-import FX (0%), and USDT already abroad.

**After July (S3, kept with corrections).** In Aug–Sep 2026 residents' stablecoin purchases abroad stayed at 32% of their
Jan–May level (F-024, T2 = 0.32), consistent with the funds' channel staying closed. The BCB series counts all
residents' purchases, not only funds'. Yet from 22 Jul to 30 Oct the premium never rose more than **+52.1 bps** above
its pre-notice level, and its average level is not distinguishable from ordinary drift (+11.5 to +19.3 bps, placebo
p = 0.24, F-022). So after July neither the 1.1% nor the 3.5% route (110 and 350 bps over the closed route) was setting the price:
either cheaper supply reached the market or demand fell. The data do not say which.

## Evidence
- Route map, sources and the rule applied condition by condition: `results/tables/P3-15_routes.md`. Costs from F-015
  (`results/tables/P3-01_route_costs.csv`; R-01, R-01b, R-02); statuses from E-05.1, E-05.2, E-05.5, E-05.6, E-05.10
  (new quotes opened 2 Nov 2026 by Renzo's agent, listed in the table's notes).

| Route | IOF | Excess over closed route $e_r$, bps | Adds USDT supply? | After 23 Jun |
|---|---|---|---|---|
| 1. Funds' import with intermediation | 0% | 0 (reference) | yes (E-05.2) | closed (E-05.1, E-05.5) |
| 2. Funds' own account / in-book arbitrage | 0% | 0 | unknown | unknown |
| 3. Ordinary purchase of foreign currency | 3.5% | 350 | unknown | open |
| 4. Remittance "com finalidade de investimento" | 1.10% | **110** (in range) | unknown | open as a tax category |
| 5. Goods-import FX | 0% | 0 | unknown | open as a category |
| 6. USDT already abroad, moved on-chain | – | not measured | unknown | unknown |

- Rule outcome: condition 1 holds (route 4 only); condition 2 fails (route 4: supply unknown); condition 3 fails
  (routes 2 and 5 are cheaper with unknown status or supply; route 6 not measured); condition 4 holds. Outcome (b).
- Bound check, `premium_bps` from `data/processed/P1-02_premium_daily.csv`:

| Window | Days | Highest daily premium | On | Minus 15.2 bps |
|---|---|---|---|---|
| 24 Jun – 30 Oct 2026 | 91 | 185.9 bps | 3 Jul 2026 | +170.7 bps |
| 22 Jul – 30 Oct 2026 | 71 | 67.3 bps | 5 Oct 2026 | +52.1 bps |

- Reproduce the bound check:
  ```bash
  .venv/bin/python -c "
  import pandas as pd
  p = pd.read_csv('data/processed/P1-02_premium_daily.csv', parse_dates=['date_brt']).set_index('date_brt')['premium_bps']
  for a, b in [('2026-06-24', '2026-10-30'), ('2026-07-22', '2026-10-30')]:
      s = p[a:b]; print(a, b, 'n =', len(s), 'max =', round(s.max(), 1), 'on', s.idxmax().date(), 'max - 15.2 =', round(s.max() - 15.2, 1))
  "
  ```
- Other numbers: +93.9 bps and 15.2 bps (F-016, F-022 `scripts/p4_01_robustness.py`), range +73.7 to +128.3 (F-022),
  route costs 22.5 / 132.5 / 372.5 bps (F-015 `scripts/p3_01_costs.py`), T2 = 0.32 (F-024 `scripts/p3_10_imports.py`).

## Caveats
- **Not a legal opinion.** "Unknown" means no opened source answers the question. It does not mean a route is lawful
  or unlawful for virtual assets. Framing rule (`docs/02-dolar-cripto.md` §10): we measure frictions and recommend no route.
- **The rule was written knowing the numbers** (spike, range and F-015 totals). It fixed how they would be read before
  the comparison. It was not blind.
- **May 2025 is not a clean test either.** The next day Dec. 12.467 kept 1.1% for investment remittances; Congress and
  the STF suspended and then restored the decree (E-01b, −23.9 bps, p = 0.16). The funds' 0% route was untouched, so
  the null fits a cheaper route setting the price then too.
- **"Did not set the price" is not "could not supply".** Whether the 3.5% route can carry virtual assets is unknown
  (Brotto, E-05.10, opinion, compares the funds' 0% with it: "vantagem de até 3,5%").
- **Inciso number:** R-02 cites art. 15-B, XXI for the 3.5% rate and Brotto cites XXIV. The rate agrees. Planalto blocks
  automated requests; Felipe can check it in a browser.
- Daily maxima are single days at the PTAX window. The +170.7 bps peak is description, not a test.

## Text for the deck (for Felipe, P5-01; level "not shown" for the marginal route)
- **Slide 1** (replaces "o prêmio descola da paridade até o custo do próximo canal disponível"): "Quando uma regra fecha
  a porta mais barata, o prêmio pode subir até o custo do próximo canal disponível; em 2026 ele subiu +94 bps, bem
  menos que a diferença de alíquota de 3,5 pontos, e não identificamos qual canal passou a definir o preço."
- **Slide 5** (the 0% vs 3,5% line): "Os fundos pagavam IOF-Câmbio zero, contra 3,5% na compra comum de moeda
  estrangeira; o prêmio subiu bem menos que essa diferença (no pior dia, 3/jul, 171 bps acima do nível anterior), e
  quando a alíquota da compra comum subiu de 1,1% para 3,5% em maio de 2025 o prêmio não se moveu (+13 bps): o canal
  bancário comum não era o que definia o preço, e não sabemos se foi oferta mais barata ou menor demanda que o conteve."

## Used in deck
Not yet. Proposed for Slides 1 and 5 (text above) and the annex (route table).

## History
- 2026-11-04, agent for Renzo (P4-03, Renzo's decision): status confirmed -> frozen (tag `results-frozen`); from now on only bug fixes, each disclosed here
- 2026-11-02, agent for Renzo (after a second agent's review): "ceiling" removed (route 3's supply is unknown, so
  it is not an established upper bound); May 2025 IOF evidence (F-026) added; deck sentences rewritten
- 2026-11-02, agent for Renzo: created (P3-15); rule committed first (`6393330`).
