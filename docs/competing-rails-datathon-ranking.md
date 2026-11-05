# Competing-rails hypotheses: datathon ranking and investigation plans

**Date:** 4 November 2026 (Brasília)  
**Prepared by:** Codex for Renzo, P3-23  
**Status:** Checked recommendation, not adopted scope or new empirical findings.  
**Read first:** [Full English research agenda](competing-rails-research-agenda.md)

## Recommendation

Prioritize **H2: the already registered prediction**, then **H1: recovery and market composition**. Add **H3: a narrowly defined cost sensitivity analysis** if it materially improves the economic interpretation. Reuse the existing user illustrations under H5. Qualify H4 before any BRLA price test. Keep H6 as a subsequent research project unless a credible identification design and the required data become available.

This ranks incremental contribution to this datathon, not long-run scientific value or ease of coding. The main criteria are connection to the primary question, information beyond existing findings, whether the required quantity can actually be observed, and whether the evidence supports a clear PDF exhibit. No numerical scoring system is presented as objective evidence.

| Rank | Original hypothesis | Datathon-sized investigation | What it could establish | Main limitation |
|---|---|---|---|---|
| **1** | H2: which gate changes the premium? | Complete P3-20 E1 as registered; preserve E2 branch and early-reading protocol | A prospective check of a specific prediction | One event; broad reference variation; no general proof that reporting rules have zero effect |
| **2** | H1: why did the premium recover? | Test whether price normalization accompanied persistent changes in observed trading composition; review competing mechanisms | A documented change in market organization accompanying recovery | No dealer identities, inventories or gross international flows |
| **3** | H3: cost, size and reliability | Matched-endpoint cost accounting and break-even sensitivity to missing fees/size | Conditions under which an illustrative route advantage survives or reverses | No historical executable-depth, failure or delivery-time panel |
| **4** | H5: who bore the burden? | Use and carefully extend P3-21's fixed user scenarios | Transparent incidence illustrations on the observed premium path | No observed customer population, cancellations or welfare identification |
| **5** | H4: BRL stablecoin architecture | Qualify an independent BRL peg and FX-conversion comparison, then test only if data pass | A narrow comparison of two conversion margins | No BRLA/BRZ historical dataset in the inspected inventory; a USD pool alone does not identify a BRL depeg |
| **6** | H6: spillovers into conventional FX | Specify a future exposure-based design | Currently a research question, not a new datathon result | Missing funding/exposure data and a credible way to separate direct policy effects |

## What was checked

Repository inspection started at `a090a28`; syncing brought in `7204a38`, Felipe's [research/conclusions memo](plan-research-and-conclusions.md). The assessment reads that memo alongside the findings, rather than treating proposed conclusions as established facts.

- Read `prompt.md`, `STATUS.md`, `docs/README.md`, `docs/phases.md`, the source register and relevant task specifications.
- Examined the actual code in `scripts/p3_20_live.py` and `scripts/p3_01_costs.py`, rather than assuming named commands or endpoint comparisons were implemented.
- Inspected CSV schemas and existing outputs for premium, noise estimates, Foxbit/MB candles, P3-17 flows, P3-19 response tests, P3-20 references and P3-21 illustrations.
- Inspected the data manifest and searched data paths for BRLA/BRZ, order books/depth, conventional-FX funding, customer records and quotes. No such research datasets were located. A filename search is not proof that the data cannot be obtained elsewhere.
- Reopened the official FGV event page and BIS literature pages. The FGV regulation PDF was not accessible through the web tool in this session; its detailed submission-format requirements are taken from the repository's previously checked regulation summary.
- No November outcome data was downloaded or inspected. No new hypothesis test, price estimate or change to a registered specification was made.

### Calendar and deliverable constraints

The [FGV event page](https://eesp.fgv.br/evento/7o-desafio-de-dados-datathon-de-moedas-digitais-da-fgv-eesp) confirms submission on **8 November at 23:59 Brasília**, finalist announcement on 12 November and the final on 16 November. The ten-slide cap is a **team rule**, not a claim about the official regulation. Core findings remain protected while the team decides extension inclusion; see the “Research continues” decision in `docs/README.md`.

Calendar matters for observation, not just available labor: P3-20 E2's second post-event PTAX day is 9 November. Its registered two-day primary verdict therefore cannot appear in the 8 November PDF. Its 6 November one-day reading is explicitly preliminary. E1's 3–4 November two-day window can be evaluated before submission, subject to data availability and review. The January 2027 prediction cannot resolve during this competition.

## Rank 1 — H2: complete the prospective test, without expanding its claim

**Question for the PDF:** Did the registered prediction for the November reporting rule survive its specified test?

**Existing work.** [P3-20](../tasks/P3-20-live-predictions.md) contains the specification, registration commits, comparison venues, overlap screen and reference distribution. This is genuinely additional information relative to fitting explanations to the known June episode. International qualification is separately planned in [P3-22](../tasks/P3-22-other-countries-qualify.md); it is not equivalent to a prospective test.

**Code validation.** At the inspected revision, `scripts/p3_20_live.py` dispatches only `reference`. Its docstring explicitly says `readout` remains to be added. Running that script alone does not evaluate E1. The next worker must implement the registered download/readout steps, not invent a replacement design.

**How to do it, in the existing task owner's workstream:**

1. Preserve the registration and frozen reference outputs. Implement isolated downloads to new raw filenames and an extended premium table; verify every overlapping frozen row reproduces.
2. Compute the registered primary statistic S2 for E1: mean on 3–4 November minus the specified twenty-PTAX-day pre-window. Keep the registered exclusion of t0 and missingness rules.
3. Evaluate the registered empirical p-value rule using the stored reference observations; also report the non-overlapping comparison requested by the specification. Report all venues and missingness, without selecting the most favorable venue.
4. State the observed statistic, reference variability, verdict and concurrent developments. Compare with the simple no-change expectation; do not call this general forecasting skill from one event.
5. Preserve E2's separate source-based branch selection before its outcome window and score it as registered. A conceptual critique of the branch belongs alongside the prediction, not in a silent rewrite.

**Checked inference caveats:**

- The stored Binance **S2** ordinary-date quantiles are **−75.5 to +59.8 bps**. **−35.4 to +37.7 bps** belongs to **S20**, a different statistic. These values were read directly from `results/tables/P3-20_reference.csv`; they were not newly estimated here.
- A reference quantile band is not automatically a confidence interval for the event's causal effect. “Not unusually large relative to these placebo dates” is defensible; “rules out every effect larger than the band” is not established by non-rejection. Formal equivalence would require an appropriate interval/test and a justified margin, separately identified from the registered verdict.
- The registered absolute-value empirical p-value remains the verdict rule; do not substitute membership of an asymmetric quantile interval for that calculation.
- Restricting buyers' bank deposits does not theoretically guarantee a price increase. E2 branch B needs this conceptual limitation disclosed even while the original registered prediction remains intact.
- A correct no-detectable-move prediction for an anticipated reporting rule does not isolate transparency from content, adaptation or weak power. A changed premium also need not be caused by that rule, given overlapping developments.

**Output:** one compact prediction-versus-observation exhibit and a reproducible finding, plus an annex with the full specification and limitations.

**Success/failure rule:** report the registered result regardless of sign or significance. If the readout cannot be verified, label it pending. Do not select inclusion based on whether the prediction “wins.”

## Rank 2 — H1: did price recover while trading composition remained different?

**Question for the PDF:** Is recovery in the premium also recovery in the observable organization of trading?

**Already known.** [F-031](../findings/F-031-who-traded-the-fade.md) reports changes in Foxbit's share, trade size, business-hour trading and initiation imbalance. [F-032](../findings/F-032-supply-response.md) relates initiation to the premium, with weak within-day evidence. Simply replotting those results is synthesis, not new confirmation of replacement supply.

**Incremental test:** make the distinction between price recovery and composition recovery explicit, check it on a consistent sample, and test how dependent the pattern is on the selected dates and venue coverage.

**How to do it:**

1. Write a retrospective specification before computing new comparisons. Retain the already used pre-event, acute and post-spike periods, clearly disclosing that they were selected with knowledge of the episode. Do not optimize the recovery date again.
2. Use **Foxbit's share of the three observed venues' USDT volume** as the primary composition measure. Define it from summed volume, not an accidental mix of daily-share averages and volume-weighted shares. Compute on common coverage and report missing/zero-trade hours.
3. Compare its post-spike level with the pre-event level, alongside the premium. As secondary descriptions, show trade size and the business-hour share. MB has volume but lacks the trade-count and taker-side columns present in Foxbit's file; do not manufacture equivalent MB measures.
4. Match calendar composition and use contiguous historical placebo windows and block uncertainty to describe whether the change is unusual. This remains one episode: daily rows are not independent policy shocks, and placebo unusualness does not identify the cause.
5. Audit possible venue migration, coverage changes and recorded corporate events. The onset of the selling wave predates the announced NovaDAX partnership and Foxbit Infra relaunch; that constrains a simple announcement-caused-onset story without excluding earlier private activity.
6. Present a competing-explanations table: rerouting, inventory use, demand retreat and reporting-perimeter changes. Mark which observable facts each explains and which required data are absent. Do not assign causal weights from fit to the same episode.

**Output:** an aligned price/composition figure and a short mechanism evidence matrix. A defensible result would be “the premium normalized while observed trading composition remained changed,” if the comparison survives. It would not establish who supplied the dollars or who caused the recovery.

**Failure condition:** if the composition result disappears on common coverage or calendar balancing, report that. If it survives but mechanisms remain observationally equivalent, retain an unresolved mechanism verdict. The dropped on-chain attribution task P3-18 should not be reopened by assigning unverified exchange wallets.

**Value:** adds an observable consequence of the shock beyond the price spike. This is the best datathon subset of H1; the full inventory-and-rerouting research requires additional records.

## Rank 3 — H3: establish the conditions under which an apparent cost advantage survives

**Question for the PDF/annex:** How sensitive is the economic comparison to endpoint, fees, transaction size and unobserved execution costs?

**Validation finding.** `scripts/p3_01_costs.py` prices a USDT purchase plus exchange/network charges and compares it with bank-route scenarios. It does not include a complete foreign fiat redemption leg, historical execution slippage, or a delivery/failure panel. Its corporate spread input is not validated for every retail transaction size. Therefore it cannot be relabeled as a measured fiat-to-fiat payment frontier.

**How to do the narrower study:**

1. Define one user, direction and endpoint. Either retain acquisition of USDT and label the different bank asset explicitly, or add the missing exit leg to a genuine matched fiat-to-fiat comparison. Do not equate bank deposits and USDT without disclosing their different claims and access conditions.
2. Separate observed premium, documented fee assumptions, dated tax/purpose assumptions, and genuinely unknown costs. Existing route-law eligibility remains unresolved in [F-028](../findings/F-028-route-comparison.md).
3. Derive the break-even omitted cost: if a benchmark route costs `B` bps and the observed/assumed stablecoin components sum to `S` bps, the apparent advantage survives only if additional costs are less than `B − S`. A negative margin already reverses that scenario. This is an accounting sensitivity, not estimated execution performance.
4. Keep fixed charges in currency units before converting to bps: `10,000 × fixed fee / transaction value`. Use fee schedules valid for the chosen size and user; do not scale a corporate FX spread down to a small retail transfer without evidence. Apply fees multiplicatively or on their documented bases when calculating exact receipts; additive bps are an approximation.
5. Compare the pre-shock, acute and recovered premium paths under the same assumptions. Show conditions under which the scenario ordering reverses; do not pick one convenient fee case as the winner.

**Output:** one sensitivity exhibit or annex table, with unknown legs visibly marked. Full capacity/delivery claims require repeated executable quotes, depth, completed payments and failures, as proposed in H3's long-run agenda.

**Failure condition:** unmatched endpoints or unknown tax eligibility prevent a provider ranking. Report the break-even conditions without a “cheapest route” verdict. Price candles and high-low spread estimators cannot supply the missing slippage curve.

**Why only third:** potentially useful economics, but much of the basic accounting is already P3-01 and the paper literature. The contribution is clarifying robustness of the comparison, not claiming a new global payment benchmark.

## Rank 4 — H5: retain the user illustrations; do not call them a welfare study

[P3-21](../tasks/P3-21-who-paid.md) and [F-033](../findings/F-033-who-paid.md) already implement fixed purchase/holding scenarios and disclose counterfactual sensitivity. The highest-value next step is review and clear use of this work, rather than creating more hypothetical personas.

If extending it, fix transaction schedules and counterfactuals first, add documented execution-fee sensitivity, separate purchases after the event from earlier purchases, and keep held-position revaluation distinct from realized cash transfers. Do not infer actual savers' losses from a hypothetical account.

**Output:** a reader-friendly incidence illustration linked to the existing reproducible table. **Claim ceiling:** consequences for specified transactions on the observed path. The actual H5 hypothesis—persistent exclusion or costs for particular customer groups—cannot be tested with these aggregate prices. It requires client-level outcomes including failed and canceled requests.

The gross-turnover result in F-025 does not identify sellers' residence, market-maker profit, total tax receipts or social loss. A claim that all extra spending went to offshore incumbents, or generated zero public revenue anywhere along the route, is not established.

## Rank 5 — H4: qualify a BRLA test before treating it as evidence

**Go/no-go checks, before an outcome plot:**

1. Verify issuer, token contract, chain, decimals, relevant pool and historical existence. Avoid confusing similarly named tokens or selecting the pool with the desired move.
2. Establish pre-event and event coverage, stale-price frequency, liquidity, and an independent BRL valuation or documented executable redemption source. The required historical dataset was not found in the inspected repo.
3. Define the two margins separately: BRL token versus BRL, and BRL token versus dollar stablecoin. Account for dollar-stablecoin deviations and synchronize the conventional FX benchmark.
4. If only a BRLA/USDT pool is available, specify an **FX-conversion-gap** study. That pool alone cannot show whether BRLA, USDT access, or pool liquidity generated the move.
5. Lock the window, missingness and liquidity criteria, then run all qualified series. Report no move and failed qualification as outcomes, without converting either into evidence that the channel was unaffected.

**Output if qualified:** a narrow two-margin case study, likely annex material. **Failure condition:** no independent peg measurement or credible liquidity leaves the proposed depeg test unidentifiable. A BRLA depeg is neither necessary nor sufficient to prove the June mechanism. This is the principal reason for its rank, rather than the amount of coding required.

## Rank 6 — H6: defer the causal FX-spillover claim

The current PTAX and crypto series are insufficient to isolate transmission through intermediaries. Adding spot or futures correlations does not solve direct policy effects, common macro news or endogenous flows. BIS Working Paper 1340 already addresses the broader spillover question.

To advance this branch, first obtain synchronized FX/funding and intermediary-exposure data and state a credible source of identifying variation. Distinguish a stablecoin demand shock from a supply interruption. Then specify outcomes and alternative direct channels before estimation. The notice is not automatically a valid instrument for flows because it also concerns banks and FX operations directly.

**Datathon output now:** a precise future-research question. **Promotion condition:** a defensible identifying design and data, not merely a statistically significant regression. A CS network simulation can illustrate assumptions, but fitting it to this episode would not establish the transmission mechanism.

## Where the new strategy memo exceeds the evidence

These are review comments on [Felipe's memo](plan-research-and-conclusions.md), not edits to his document or claims about what the mentor personally established.

| Proposed statement | Evidence check / correction |
|---|---|
| The recovery mechanism has already been solved by Foxbit selling | F-031/F-032 explicitly leave trader identity, external supply and causation open |
| The BC never reopened the channel | F-030 found no verified public reopening; an unsuccessful search is not proof of no operational accommodation |
| BRLA should depeg if the dollar-access channel is blocked | A stable BRL peg can coexist with a higher BRLA-to-dollar conversion price |
| R$106–145m is private offshore profit or social loss with zero tax revenue | F-025 measures extra buyer expenditure relative to a benchmark over observed turnover; ownership, costs and tax incidence are unmeasured |
| Public rules had zero impact, proving the benefit of transparency | Non-rejection is not zero; announcement, content, anticipation and power differ; F-029 also qualifies the “only notice” comparison |
| E1 uses the −35/+38 bps band and is ready to run | That is S20; S2 is −75.5/+59.8 bps in the stored Binance table, and the readout code is not implemented yet |
| A null E1 is automatically a strong out-of-sample success | Report its registered verdict, but compare with no-change and disclose low discrimination; no causal equivalence claim follows |
| A fitted 35 bps threshold identifies replacement-route costs | F-032's trade-initiation statistic does not measure the costs or capacity of suppliers |
| Stablecoin net acquisitions measure import supply; high turnover proves inelastic demand | Net acquisitions, gross inflows, stock, trading turnover and final-use demand are different quantities |
| An exchange exit proves the notice caused consolidation | Verify the event, timing and alternative causes first; observed exchange shares do not identify supplier concentration or a causal exit mechanism |

No exchange-exit event or causal attribution was independently established in this task. This assessment does not endorse that lead as a result.

## Recommended sequence and materials for the submission

1. **P3-20 owner:** complete and independently review E1, following its existing specification; retain E2's early/full-result distinction.
2. **Recovery work:** use the existing P3-17/P3-19 ownership and review process; adopt a separately recorded retrospective specification for any new composition comparisons. Do not duplicate the completed price-response regression.
3. **Cost work:** identify the endpoint and genuinely missing components before any new scenario calculation. Review the matched comparison with the economist.
4. **Deck owner:** consider one prediction exhibit, one recovery/composition exhibit and the existing user illustration. Supporting sensitivities and rejected mechanisms belong in the annex. The ten-slide cap remains.

These are proposed work packages, not assignments to teammates or authorization to modify their active tasks. Core findings and the headline are unchanged by this document. A new analysis should have its own recorded specification, script/output paths, finding and independent review before deck adoption.

## Reproducible inspection notes

This task validates prerequisites and interpretation, not the empirical truth of the proposed hypotheses. Existing findings carry their own reproduction commands and review status.

The following read-only check reproduces the central schema and reference checks without touching November outcomes or overwriting outputs:

```bash
.venv/bin/python - <<'PY'
from pathlib import Path
import pandas as pd
paths = [
    'data/processed/P1-02_premium_daily.csv',
    'data/processed/P2-01_noise_floor_daily.csv',
    'data/raw/foxbit/USDTBRL-1h.csv',
    'data/raw/mercadobitcoin/USDT-BRL-1h.csv',
    'results/tables/P3-17_daily_flow.csv',
    'results/tables/P3-19_daily.csv',
    'results/tables/P3-21_who_paid.csv',
]
for name in paths:
    d = pd.read_csv(name)
    print(name, list(d.columns))
    if 'date_brt' in d:
        print('coverage:', d.date_brt.min(), d.date_brt.max())
r = pd.read_csv('results/tables/P3-20_reference.csv')
print(r.loc[r.series.eq('Binance'),
            ['statistic', 'band_lo_bps', 'band_hi_bps']].to_string(index=False))
for term in ['brla', 'brz', 'orderbook', 'depth', 'b3', 'swap', 'customer', 'quote']:
    print(term, [str(p) for p in Path('data').rglob('*')
                 if p.is_file() and term in str(p).lower()])
PY
rg -n 'readout|reference|__main__' scripts/p3_20_live.py
```

Checked premises: existing frozen data support price, volume and some trade-initiation descriptions; no inspected input identifies customer incidence or historical full-route execution; E1 can supply a prospective check after implementation; E2's primary window falls after submission. The ranking is a judgment conditional on those premises, not a forecast of which hypotheses will be supported.
