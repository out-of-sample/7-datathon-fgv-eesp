# Extension audit: the project improved, but the progress summary overstates several results

Date: 7 November 2026, Brasília. Reviewed checkout: `b161a85` after an authorized pull from `d281bff`. Local audit; no push.

## Executive assessment

The extensions add a useful treasury illustration, a documented duration experiment, prospective policy measurements and a much stronger on-chain accounting appendix. They do not jointly prove that every digital-dollar cost originates at a banking gate, that recovery duration is inherently unpredictable, or that every holder should sell immediately.

The submitted deck is generally more careful than the progress summary supplied in chat. Use the checked-in findings and scripts as the numerical authority.

## What changed since the previous work

- P3-30 expanded from the initial Brazil feasibility failure to a ten-currency pool and a penalized discrete-time survival experiment.
- P3-31 now includes buyer and seller cases and an idealized FX-hedge comparison.
- P3-26/F-045 quantify the October incident's relation to November windows; F-035 includes E2's first-day measurement.
- P3-28 adds an evidence-backed access card, while P3-29 adds historical Celo accounting and additional-case checks.
- P3-34 supplies cost-stack and market-composition exhibits.
- Commits `8df8f50` and `d281bff` record Felipe's P3-29 S6 interpretation review and Annex B.10.2 integration. S6 completion is distinct from independent pipeline reproduction.
- The pull added `b161a85`: P3-35 is an active, separately owned investigation of the economic function of the BRLA burns. Its protocol is registered; its result is pending. Do not describe that economic attribution as completed.

## 1. Duration: replace the supplied summary

Current F-038 and its script use a shock exceeding three robust standard deviations above the preceding 60-observation median, with recovery requiring five consecutive observations inside the frozen one-sigma band. They do not use a primary 50-bp/three-day definition.

The current census contains **10,875 currency-observations**, on native calendars, and **61 episodes** at the primary threshold. These are not 13,849 Brazilian PTAX days or nine independent global shocks.

The fitted comparison is **one penalized discrete-time logistic hazard model versus Kaplan–Meier**, not Cox PH, AFT and random survival forests. At the primary ten-day horizon, validation Brier is model **0.346** versus baseline **0.330**; test is **0.175** versus **0.188**, with eight test episodes and a paired difference interval **−0.112 to +0.073**. Threshold variants lose to the baseline. A narrow test improvement is inconclusive.

The **20-day median is a training-pool Kaplan–Meier estimate**. Brazil's 2026 episode begins **25 May** and remains unrecovered through 30 October after **111 PTAX days** under this definition. The one-month June acute price spike and recovery to the frozen pre-May band are different objects. The chat's Brazil “21-day recovery” is contradicted by current F-038.

The current onset features show no evident peak-price look-ahead: initial excess is measured at onset and training current-premium features are lagged. Cutoff extraction is chronological. However, cross-currency shocks may share causes; three test episodes are Indonesian, and the bootstrap resamples individual episodes rather than global-event clusters. Treat its interval and generalization as exploratory.

**Approved interpretation:** this model and small evaluation sample do not establish reliable predictive improvement. Neither a nonsignificant coefficient nor an inconclusive Brier comparison proves that duration cannot be predicted.

## 2. November: arithmetic supported, causal certainty overstated

Independent calculation from the saved P3-20 daily CSV reproduces E1's pre-mean **19.23185 bps**, post-mean **21.324 bps**, and S2 **+2.09215 bps**. The excluded 30 October observation cannot directly enter that pre-mean. This supports the registered calculation, not “100% uncontaminated”: residual effects on later liquidity or both venues are not excluded by a small cross-venue gap.

E2's saved 5 November levels are Binance **22.190**, Foxbit **23.429**; 6 November levels are **16.764** and **16.899**. Independent differences reproduce **−5.426 bps**, **−6.530 bps**, gap change **−1.104 bps**, and terminal gap **+0.135 bps**. These agree with F-035's rounded first-day reading.

**E2's primary two-day S2 verdict requires 9 November**, after the submission deadline. Its first-day reading cannot confirm the primary prediction or establish that announced deadlines generally lack effects. Branch C was two-sided with no directional prediction.

F-045 and its generated report contain stale/hard-coded 5–6 November levels (for example 21.5/23.8 and 17.1/19.2), whereas F-035 matches the saved CSV. Reconcile the report templates with calculated values before using them as evidence. Its hypothetical-prewindow interpretation also hard-codes a p-value inconsistent with the surrounding table. The E1 headline arithmetic itself reproduces.

The source register describes phased withdrawal restoration as a **plan**, not verified USDT restoration at a particular time. Do not turn parity normalization into proof of completed operational restoration.

Historical placebo bands are reference distributions, not confidence bounds that exclude all smaller/larger causal effects. Report “not unusual relative to the reference distribution,” rather than “proved zero effect.” The documented CUSUM quiet pause also makes a non-alarm during that interval uninformative.

## 3. Treasury and fee exhibits: the summary includes a withdrawn assumption

The current holder implementation correctly prices a long-USD forward using CIP. F-039 explicitly withdrew the former standalone **2.5 bps/day carry charge**: adding that charge while also accumulating BRL cash would double-count carry under its ideal assumptions. The chat summary should not reuse it.

Slide 10's “aposta pura no prêmio local” is still too strong. The comparison includes USD interest, USDT/USD movements and residual hedge exposure. Use: **“O hedge reduz a exposição ao USD/BRL; o resultado também depende do preço USDT/USD, do rendimento USD e do residual do hedge.”** Current illustrative assumptions include a net 10% BRL return, 5% USD return and 0.22-bp hedge fee; WDO spread and margin funding are omitted. Actual institutional access and achievable net returns matter.

The seller loss is a retrospective result from one starting date and one episode, under specified rates and fees. It does not establish that an institution should always sell immediately. Qualify it with **“neste episódio, sob este cenário”**.

F-040's **470–939×** arithmetic compares the incremental 93.9-bp premium shock with a listed 0.1–0.2-bp network fee. It is not the ratio of total banking-route cost to total blockchain-route cost. The pool comparison similarly divides 111 bps by a 5-bp pool fee; other costs remain. Label the numerator and denominator prominently. The all-in table is a constructed proxy using current fee schedules, not measured historical execution.

Replace F-040's causal “provando” with an observed-price statement or “compatível com”. The linked BRLA route strengthens evidence of price breadth but is not independent identification of the banking mechanism.

## 4. Ledger and access evidence: useful, with distinct completion gates

The independent agent confirms that F-041/F-042/F-044 remain exploratory and P3-29 S7 independent reproduction remains pending. S6 economist review and annex integration are completed. Add the pending-reproduction caveat next to Annex B.10.2 results, rather than relying on readers finding it in the task file.

The ledger and annex carefully distinguish mint from fiat subscription, burn from redemption, and address from owner. They surface pre-notice burns and do not establish a cross-chain migration or BCB causality. The unmatched provider supply point is a discrepancy, not proven provider error. Preserve those distinctions in the main thesis.

F-043 is one retrospective access-card development case, with a second-reader check of 23 rows. It preserves bank-leg access as unknown and historical fee/depth fields as null. It does not demonstrate a usable institutional route or a causal effect of Res. 589. P3-35's new investigation appropriately seeks the economic function that the ledger alone cannot identify.

## 5. Repository and review integrity

STATUS.md has committed conflict markers at the top, Next actions and Recent activity. These are not a live Git merge: the checkout pulled cleanly. They make the dashboard contradictory and should be resolved with the owners, preserving both activity histories and regenerating the board. This review does not choose between disputed task records.

P3-29 still has status `review`; completed economist interpretation is not a substitute for the remaining independent reproduction. Its original planning paragraph and parts of its handoff are stale relative to completed S6. P3-35 is currently owned by Renzo and must remain separate.

## Checks performed

- Authorized Git pull: fast-forward to `b161a85`.
- `scripts/p3_30_duration.py --test`: **14 checks passed**.
- `scripts/p3_31_holder.py --test`: **13 checks passed**.
- Independent arithmetic on saved P3-20 daily observations, as reported above.
- Three bounded independent agent reviews assigned to duration, treasury/costs, and ledger/access evidence.
- All three agent reviews completed; their actionable findings are incorporated above. They inspected code and evidence without changing source files.

These checks do not constitute an end-to-end rerun of all raw-data downloads, the ledger or the final PDF. Passing arithmetic tests does not validate economic assumptions.

## Sources and reproducibility

Primary repository evidence: [F-038](../findings/F-038-shock-duration-feasibility.md), [F-039](../findings/F-039-holder-decisions.md), [F-035](../findings/F-035-e1-res574-readout.md), [F-045](../findings/F-045-november-binance-incident-audit.md), [P3-29](../tasks/P3-29-on-chain-reconciliation.md), [P3-35](../tasks/P3-35-brla-economic-function.md), and [source register M-11/M-12](sources.md).

On this machine run Python using `C:/Users/Felipe/AppData/Local/Programs/Python/Python314/python.exe`; scripts are relative to the repository root. The review read existing frozen sources rather than conducting a fresh external-source verification.

## Suggested thesis for the jury

> Neste episódio, o encarecimento do dólar digital apareceu em várias corretoras e também em uma rota on-chain. Uma transferência barata na blockchain não garante conversão barata entre reais e dólares. Os resultados são compatíveis com fricções no acesso aos canais de conversão; não identificamos integralmente o canal marginal nem o mecanismo da recuperação.

This preserves the useful lesson while distinguishing measured price breadth from the interpretation of banking access. The ledger supports a statement about token accounting; it cannot independently establish the cause of the price spike or the purpose of a fiat transaction.

## Priority before submission

**Correction follow-through (7 November, authorized by Felipe):** the wording fixes below were applied to the findings, deck variants and supporting annex; incident report generation now reads computed daily values; cost-chart labels now identify the marginal-fee denominator. STATUS conflict markers were reconciled, both activity histories preserved, and the board regenerated. Duration and holder checks pass (14 + 13). Remaining independent ledger reproduction and E2's 9 November verdict cannot be replaced by editorial corrections. Earlier sections record the audit-time defects, not the corrected file state. No PDF export was regenerated in this correction pass.

1. Replace the chat's duration/model numbers with current F-038; retain the small-sample and dependence qualifications.
2. Remove the withdrawn carry charge, universal sell-now claim and “pure premium” interpretation.
3. Present E2 only as an early reading; its verdict is unavailable before submission. Soften complete incident insulation and reconcile hard-coded F-045 report values.
4. Mark ledger/access findings as exploratory and obtain the remaining independent reproduction where feasible.
5. Coordinate resolution of committed STATUS conflict markers; no deck or frozen finding was changed by this audit.
