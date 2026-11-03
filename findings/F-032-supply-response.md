---
id: F-032
title: After the notice, seller-initiated trading on Foxbit rose with the premium over the official dollar, not with the Foxbit–Binance gap, and turned net positive above about 35 bps; the hour-by-hour evidence is weak
status: exploratory
task: P3-19
date: 2026-11-02
checked_by: -
---

## Claim
Rule fixed before the run (`tasks/P3-19-supply-response.md`, commit `c032614`); the question itself arose after seeing F-031,
so this is a post-hoc test with a pre-committed rule. **Verdict under the rule: responds to the premium**, with a weak
within-day leg.

From 24 Jun to 30 Sep 2026, on days when the premium over the official dollar (measured 10:00–13:00 Brasília) was higher,
seller-initiated trading on Foxbit exceeded buyer-initiated trading by more that same afternoon (13:00–18:00):
**+0.051 mn USDT per bp of premium (95% CI +0.011 to +0.148; 70 PTAX days)**. At a premium of 100 bps instead of 20 bps that
is about 4 mn USDT more per afternoon. The gap between Foxbit's and Binance's prices did not explain it (+0.71 mn USDT per bp,
CI −0.20 to +1.63). This is what arbitrage that brings USDT into Brazil would do (it looks at the premium over the official
dollar), and not what arbitrage between the two exchanges would do (it looks at the gap). Before the notice the same relation
was small and not significant (+0.019, CI −0.011 to +0.046; 116 days, premium range −10 to 46 bps).

**Threshold.** Seller-initiated trading turned net positive when the premium was above **k = 35 bps (CI 20 to 55)**. The
premium settled near that level (August 33.3 bps, September 23.3 bps, both inside the interval; May–June about 11 bps).
Because passive selling (limit orders) does not show in this statistic, 35 bps is at most an upper bound on what these sellers
needed, not a measured route cost.

**The weak leg.** Within each day, a higher premium in one hour did not clearly predict more seller-initiated trading in the
next (+0.006, CI −0.011 to +0.025; 350 hours on 70 days). The rule asked only for a positive point estimate here, and it is
positive, but the interval includes zero. So the daily relation may partly reflect *when* the heavy selling happened (the
weeks of high premium) rather than hour-to-hour reaction to price. The hourly premium is measured against a morning PTAX, so
intraday FX moves add noise that pulls this estimate toward zero.

**Language for the deck: "consistent with".** Safe sentence: seller-initiated trading on Foxbit rose with the premium over
the official dollar, as arbitrage that brings USDT into Brazil would, and stopped being net positive around 35 bps, close to
where the premium settled. Not: "new suppliers", "imports", "caused the fall".

## Evidence
Reproduce: `python scripts/p3_19_supply_response.py` → `results/tables/P3-19_results.csv`, `results/tables/P3-19_daily.csv`.

| Test (sample) | Premium over PTAX, mn USDT per bp [95% CI] | Foxbit − Binance gap, mn USDT per bp [95% CI] | n |
|---|---|---|---|
| Daily, 24 Jun – 30 Sep 2026 | **+0.0512 [+0.0109, +0.1483]** | +0.7064 [−0.1965, +1.6311] | 70 days |
| Daily placebo, 2 Jan – 22 Jun 2026 | +0.0190 [−0.0110, +0.0459] | +0.0677 [−0.0262, +0.1970] | 116 days |
| Within day (day fixed effects), 24 Jun – 30 Sep | +0.0061 [−0.0110, +0.0254] | +0.0293 [−0.0299, +0.0986] | 350 hours, 70 days |
| Threshold k (hinge) | 35 bps [20, 55]; slope above k +0.0538 | – | 70 days |

- Outcome: Foxbit volume − 2 × taker-buy volume (seller-initiated minus buyer-initiated, mn USDT), hourly candles.
- CIs: moving-block bootstrap over days (block 5, 2,000 draws, seed 17); within-day bootstrap over whole days.
- **Deviation from the spec (disclosed):** the spec named `P2-05_venues_daily.csv` for the Foxbit − Binance gap; it ends on
  31 Jul, so the script rebuilds the gap the same way (opens of the 13–16h UTC window candles). On the 49 overlapping days
  the two agree (mean absolute difference 0.01 bps, correlation 1.000; script line "x2 check").

## Caveats
- **One episode, post hoc question.** The rule was fixed before the run, but the idea came from looking at F-031's data.
- **The statistic is trade initiation, not supply.** It cannot show who traded, whether it was one trader or many, or that
  USDT entered Brazil (F-031, corrected). The test only asks which price the imbalance followed.
- **Daily relation and timing.** With a weak within-day leg, "the sellers reacted to price" cannot be fully separated from
  "they were active in the high-premium weeks for other reasons".
- **Small gap variation.** The Foxbit − Binance gap moves little (standard deviation 2.1 bps a day), so the test has less
  power to detect a response to it; "not explained by the gap" is not "the gap does not matter".
- Simultaneity is reduced, not removed: the outcome (afternoon) comes after the premium (morning), but both can respond to
  the same news.

## Used in deck
Not used (Felipe decides). pt-BR draft: "Depois do ofício, as vendas agressivas de USDT na Foxbit aumentaram nos dias de
prêmio maior sobre o dólar oficial, e não com a diferença entre Foxbit e Binance, como faria uma arbitragem que traz USDT de
fora; deixaram de predominar quando o prêmio caiu abaixo de cerca de 35 pb, perto de onde ele se estabilizou. É uma
associação, não uma prova de causa."

## History
- 2026-11-02, agent for Renzo: created (P3-19), status exploratory
