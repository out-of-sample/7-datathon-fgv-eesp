---
id: F-039
title: A holder needs 37.9 bps appreciation over 10 PTAX days to offset a hypothetical 10% annual BRL return
status: exploratory
task: P3-31
date: 2026-11-06
checked_by: -
---

## Claim
For an institution holding 100,000 idle USDT, a hypothetical 10% effective annual net BRL return implies required gross USDT/BRL appreciation of 18.9, 37.9 and 75.9 basis points over 5, 10 and 20 PTAX publication days, with symmetric proportional conversion costs and immediate settlement. This is an accounting threshold, not a predicted return or an accessible investment quote.

In the June retrospective illustration (signal 24 June, initial indicative window price 25 June), waiting produced R$4,697, R$11,594 and R$21,704 less than converting initially and earning that hypothetical return by 2 July, 9 July and 23 July respectively. These are indicative historical comparisons, not executable gains or causal effects.

## Evidence
- Input: `data/processed/P1-02_premium_daily.csv`; source lineage in P1-02 and `docs/sources.md`. Reused existing repository data; no new external source or current market-rate claim.
- Equation: `N=Q*P*(1-c)-f`; future break-even price `(N_now*A+f_later)/(Q*(1-c_later))`, where `A=(1+r)^(days/252)`.
- Initial gross price R$5.278475 per USDT; initial net proceeds at hypothetical 10 bp cost R$527,319.6525. Base cost is a scenario, not a venue fee quote.
- At 10 days, required gross price R$5.298476784; sell-now accumulation R$529,317.830843 versus delayed indicative net proceeds R$517,724.257500.
- Fixed FX and USDT/USD comparison isolates the premium path: waiting minus converting initially equals -R$5,407.53, -R$6,167.17, -R$11,171.53 at the same horizons and 10% scenario. Actual-path differences also reflect exchange rates and USDT/USD, multiplicatively decomposed in the output.
- Rates 0/5/10/15/20% effective annual net; four cost cases; FX changes -5/-2/0/+2/+5% and four premium endpoints are retained without selecting a profitable variant.
- Reproduce: `python scripts/p3_31_holder.py`; on this Windows machine use `& C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe scripts/p3_31_holder.py`.
- Outputs: `results/tables/P3-31_thresholds.csv`, `P3-31_historical_comparison.csv`, `P3-31_historical_inputs.csv`, `P3-31_sensitivity.csv`, `P3-31_audit.json`; figures `results/figures/P3-31_thresholds.png` and `P3-31_historical.png`.
- Six boundary tests pass: unchanged price/zero interest, premium compression/FX appreciation, unequal costs, missing prices, late settlement, fixed-cost accumulation ordering. Selected 21-row window has no missing required price fields; price identity reconciles.

## Caveats
- One known historical shock, with scenarios specified retrospectively; no strategy validation, forecast or optimal trading date claimed.
- Uses observed PTAX publication dates as a Brazilian business-day proxy, not a verified institution-specific settlement/investment calendar. No absent dates are filled. For operational use supply the actual calendar and cutoff rules.
- Assumes same-day settlement; a sale at the obligation date with positive settlement lag is rejected. Earlier settlement of the initial sale reduces investment days correctly.
- Market-window prices are not institutional executable bids. Depth, slippage, access, institution-specific taxes and withdrawal delays are not observed. Scenario fees and net yields do not remedy this evidence gap.
- All-in return matters. Premium normalization alone cannot determine the decision, and a rising dollar can reverse the illustrated advantage.
- Historic entry price is sunk for this incremental comparison unless taxes or binding mandate/accounting constraints make it relevant; such constraints are not modelled here.

## Used in deck
Not inserted. Candidate for one practical-conclusion slide after teammate review; pair thresholds with scenario qualifications.

## History
- 2026-11-06 — Codex for Felipe: specification first, engine and figures run locally, six tests pass; independent review requested. No frozen finding modified.
