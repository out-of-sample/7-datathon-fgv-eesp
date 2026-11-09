# From shock analysis to institutional decisions: an exploratory research brief

> **Estado na entrega (8 nov 2026): USO PARCIAL — ideias de espera entraram como ilustração; o plano preditivo completo não foi concluído.** Veja [estado final](estado-final.md).

**Prepared for:** Felipe and subsequent research-model review  
**Date:** 6 November 2026, Brasília time  
**Status:** Idea compilation and research framing; no feasibility assessment or adoption decision  
**Origin:** Felipe's notes and clarification in conversation  
**Repository handling:** Local document only. No commit or push authorized.

## 1. Purpose and how to read this document

This brief organizes a possible expansion of the digital-dollar project: moving from a retrospective account of a premium shock toward information that helps institutional participants decide what to do while a shock is unfolding.

Felipe's motivation is that the current evidence, in his assessment, does not yet support a sufficiently strong practical conclusion. A thorough explanation of what happened can still leave the audience asking, “So what should someone do with this information?” He wants to explore a new contribution that connects the existing research to institutional decisions, rather than simply attach a broad concluding statement to the existing results.

The intended next reader is a stronger research model or human collaborator who can challenge and develop the possibilities. This is an expansive brief, not an implementation specification, an adopted research agenda, or a claim that the proposed product can be built with the available data. It deliberately preserves several directions.

Throughout the document:

- **Main direction** means Felipe explicitly identified it as a priority.
- **Retained possibility** means an option remains relevant even though it is not the first priority.
- **Open question** means the conversation has not resolved the issue.
- **Candidate formulation** means the document supplies language or structure for later discussion; it is not a decision Felipe has already made.

Priorities should guide the discussion without being used to discard the remaining options. No ranking of feasibility, expected performance, novelty, or likely competition value has been undertaken here. Questions about validation are recorded for subsequent investigation, not answered in advance.

## 2. The original ideas

Felipe's initial notes contained the following ideas, translated and organized here without removing their exploratory character:

1. Price a fair level of “Brazil risk.”
2. Understand how a discretionary regulatory, judicial, or administrative intervention—a *canetada*—affects multiple markets and locations.
3. Understand when it makes economic sense to leave money in USDT instead of converting it, considering interest forgone, the premium paid when entering, and the duration of the disruption.
4. Explore whether SOFR and on-chain protocol spreads can help evaluate that holding decision.
5. Consider a model of the duration of shocks more generally.
6. Consider learning from global on-chain shocks to predict how long a new shock may last.

These ideas can form a connected research program, but they do not have to become one model. The brief keeps open whether the eventual contribution is an index, a collection of linked estimates, a decision framework, or a combination.

## 3. Central ambition

### 3.1 Main direction

Create information that helps affected holders, especially institutions, understand a shock and evaluate whether to sell USDT now or continue holding it.

The framework would ideally connect:

- The size of the current premium.
- A benchmark for what premium might be considered ordinary or fair under stated conditions.
- The expected time until the premium returns to its previous range.
- The interest forgone while capital remains in idle USDT.
- The economic consequences of selling now versus waiting.
- An explanation of the shock when evidence about its cause becomes available.

It must be possible to begin assessing the shock without knowing its cause in advance. Cause identification is a potentially valuable additional capability, not a prerequisite for the initial assessment.

### 3.2 Candidate overarching question

> During a disruption in digital-dollar markets, what information can help an institutional USDT holder judge whether to convert now or wait, and how much does the expected duration of the disruption matter for that decision?

This is a proposed organizing question. It has not been selected as the project's final primary research question.

### 3.3 Candidate supporting questions

- How unusual is the current premium relative to an appropriate benchmark?
- What recovery patterns recur across shocks?
- Can the framework estimate recovery probabilities at several horizons as the episode unfolds?
- What is the opportunity cost of waiting under the holder's actual alternatives?
- Does a shock reach different exchanges, on-chain pools, assets, countries, and conversion routes in similar ways?
- Can information about the cause improve an assessment initially based on observable market conditions?

## 4. Priorities and alternatives preserved

| Dimension | Main direction selected by Felipe | Retained possibilities or unresolved scope |
|---|---|---|
| Audience | Everyone affected, primarily institutions | Individual holders and other participants remain relevant |
| Decision | Selling USDT into reais or USD | Buying USDT, choosing venues/routes, and earning yield while waiting |
| Cost | Interest forgone while holding idle USDT | Premium erosion, elevated acquisition cost, and missed further appreciation |
| Duration | Time until the premium returns to its previous range | Time until conversion becomes worthwhile; probabilities over several horizons |
| Cause | Assessment should work without knowing the cause beforehand | Identify and quantify causes as information arrives |
| Brazil risk | Benchmark premium against which the observed premium can be compared | Vulnerability score and required compensation for risk |
| Global evidence | Learn common recovery patterns | Study transmission and global conditions affecting local recovery |
| Format | Expansive research brief for stronger models | Index, decision framework, dashboard, and explanatory report remain candidate outputs |
| Feasibility | Deferred to subsequent review | No direction is rejected in this compilation |

## 5. Intended users and decisions

### 5.1 Main audience: institutions

The main audience is institutional participants exposed to digital-dollar shocks. The exact institutional profile remains open. Candidate users include portfolio managers, crypto funds, treasury teams, trading desks, and institutions managing liquidity or dollar exposure.

These are possible profiles, not an agreed list of users with identical objectives. A later specification should describe which institution is making which decision, with what assets, liabilities, restrictions, and investment alternatives.

### 5.2 Main decision: sell USDT into reais or USD

Felipe's original holding question concerned selling USDT into reais or USD. These two destinations should remain explicit in the brief because the destination affects the comparison being made.

The conversation has not established whether the institution must preserve dollar exposure, whether it can take real exposure, or whether it is choosing the destination as part of the decision. The brief should not silently assume any of these answers.

Candidate decision statements include:

- “I hold USDT. Should I sell it now or wait?”
- “Should I convert USDT into USD and invest the proceeds?”
- “Should I realize the current BRL premium and invest in reais?”
- “How long can I wait before forgone interest materially changes the comparison?”

### 5.3 Other decisions to retain

- Whether to buy USDT during a premium spike.
- Which exchange, pool, or conversion route to use.
- Whether to earn yield while maintaining USDT exposure.
- Whether to convert part of a position rather than all of it.
- Whether the answer changes with an institution's liquidity deadline or mandate.

The final two items are candidate elaborations for later review, not choices already made by Felipe.

## 6. The holding question and the meaning of money left on the table

### 6.1 Main component: forgone interest

The primary financial consequence Felipe wants to study is interest forgone while holding idle USDT. The central comparison is between remaining in the current position and converting into an accessible alternative that earns a return.

Felipe explicitly separates this from something uniquely Brazilian: the alternative rate could be CDI in Brazil, SOFR in the United States, SONIA in the United Kingdom, or another relevant benchmark. These are reference points named in the discussion; the brief does not assume a holder can directly earn a published benchmark rate.

Later work should establish what return the particular institution can actually receive, in which currency, over which horizon, and after which costs. The relationship between that achievable return and a reference rate remains an empirical and scenario-definition question.

### 6.2 Premium-related consequences retained

Other financial consequences remain available as separate components:

- A premium that may disappear before the holder sells.
- A high premium paid when acquiring USDT.
- A further increase in the premium that could be missed by selling immediately.
- Differences across conversion destinations or routes.
- The possibility of earning yield without first converting out of USDT.

These components should not be collapsed into one number before the transaction and comparison are defined. The brief preserves them as possible parts of a decision analysis.

### 6.3 Original purchase premium: an unresolved part of Felipe's reasoning

Felipe mentioned justifying continued holding based on the premium paid when entering. The conversation has not yet established the intended example or the precise role of that purchase premium.

Possible interpretations to ask about include:

- A holder evaluating its total return since acquisition.
- A holder deciding what to do from the present moment onward.
- A holder explaining an accounting or mandate constraint.
- A holder deciding whether waiting could recover an earlier acquisition cost.

These are interpretations to clarify, not judgments about the reasoning. A subsequent reviewer should first reconstruct the intended transaction with a concrete example, then distinguish the relevant calculations.

### 6.4 Candidate comparison structure

For each scenario, later work could describe three paths:

| Path | Questions to specify |
|---|---|
| Sell now | Into which currency, through which route, at what executable price, and into which subsequent investment? |
| Hold idle USDT | For how long, with what liquidity needs, and with what possible exit price? |
| Hold USDT while earning yield | Through which instrument, with what access conditions, costs, liquidity, and additional exposures? |

No path is assumed superior. This structure simply makes the user's alternatives concrete.

## 7. Duration as the main predictive object

### 7.1 Main target: return to the previous range

Felipe's first duration target is the time until the premium returns to its previous range. This connects the study of shock recovery to the length of time a holder may remain exposed to an unusual market condition.

The exact meaning of “previous range” remains open. Candidate definitions include an immediate pre-shock range, a longer historical range, or a time-varying estimated benchmark. A return could also require persistence rather than a single brief observation inside the range. None has been selected.

### 7.2 Retained target: time until conversion becomes worthwhile

A second target is the time until selling or converting becomes economically worthwhile for a specified holder. This need not be the same as market normalization: the decision depends on the holder's alternatives and horizon as well as the premium.

The eventual brief or model could therefore carry two separate clocks: a market-recovery clock and a holder-decision clock. This is a candidate formulation for discussion.

### 7.3 Retained output: probabilities at multiple horizons

Felipe also expressed interest in probabilities of outcomes across different horizons. Rather than requiring one predicted recovery date, a candidate output could report the estimated probability of returning to the reference range by several future dates.

No horizons have been chosen. The user may care about days, weeks, months, or horizons linked to institutional obligations. A later specification should ask whether the output is the total expected episode duration, the remaining duration conditional on the shock's current age, or both.

### 7.4 Unresolved episode definitions

- What observation starts a shock?
- How large must a deviation be to count?
- How are ordinary fluctuations distinguished from shocks?
- What happens if the premium reaches a different persistent range?
- How are repeated spikes within one disruption treated?
- What happens when observation ends before recovery?
- Are upward and downward deviations part of the same research question?

These questions are preserved for later design. No detection rule or duration model is implemented by this document.

## 8. Learning from global shocks

### 8.1 Main direction: common recovery patterns

Felipe's main interest in global on-chain shocks is learning whether recovery patterns observed elsewhere can inform an assessment of a new episode. The intended contribution is broader than explaining the Brazilian episode after the fact.

The candidate question is:

> What features of past disruptions help describe how long an ongoing disruption may remain outside its ordinary range?

This leaves open which episodes belong in the comparison set and whether they should be modeled jointly or in separate groups.

### 8.2 Candidate episode families

The following possibilities should remain visible until scope is decided:

- Brazilian crypto-dollar premium shocks.
- Crypto-dollar premium shocks in other countries.
- Stablecoin deviations from their dollar peg.
- On-chain liquidity or conversion disruptions.
- Exchange-specific outages or withdrawal restrictions.
- Regulatory or judicial interventions affecting market access.
- Traditional-market disruptions used as possible comparisons.

The inclusion of traditional-market episodes is an unresolved possibility raised in clarification, not a priority selected by Felipe. The document does not assert that all these events share a recovery process.

### 8.3 Other global directions retained

- How a shock spreads across assets, venues, routes, and countries.
- Whether global funding or liquidity conditions help explain local recovery.
- Whether on-chain protocol spreads provide information about opportunity cost or stress.
- Whether knowledge of the cause improves estimates after an initial cause-agnostic assessment.

## 9. Fair Brazil risk

### 9.1 Meaning intended by Felipe

Felipe uses “Brazil risk” broadly, by analogy with risks affecting Brazilian equities: a judicial, regulatory, or administrative decision can change the conditions under which an asset is held or traded. The idea should not be narrowed prematurely to one regulation or one conversion bottleneck.

The phrase “fair risk” is not yet a formal asset-pricing definition. The proposed research would need to clarify what output the term represents.

### 9.2 Main candidate output: a benchmark premium

If only one Brazil-risk output were pursued, Felipe prefers a benchmark against which the observed premium can be assessed as relatively high or low.

Open interpretations include an ordinary premium conditional on market conditions, an estimate of compensation associated with specified exposures, or a benchmark combining measurable costs and risk components. The brief does not choose among these or assume that a historical average is economically fair.

### 9.3 Additional outputs retained

- A score describing vulnerability to discretionary intervention.
- An estimate of compensation investors might demand for specified risks.
- A decomposition separating ordinary costs, unusual stress, and unresolved components.
- Comparison across jurisdictions under a common framework.

The decomposition and jurisdiction comparison are candidate elaborations for later review.

### 9.4 Dollar movement: explicitly unresolved mechanism

Felipe does not yet see clearly how difficulty moving dollars into and out of Brazil affects the proposed framework. He explicitly requested that it remain in the plan with a note.

**Open mechanism:** Investigate whether, and through what channel, restrictions or costs on cross-border dollar movement affect premiums, recovery, or the holder's executable alternatives. Do not treat this mechanism as already understood or accepted merely because it appears in the current project narrative.

## 10. One intervention, multiple markets

Felipe wants to retain a broad investigation of how a *canetada* affects multiple places. He has not selected the main comparison dimension.

| Dimension | Candidate question |
|---|---|
| Exchanges | Does the premium appear, grow, and recover similarly across venues? |
| On-chain pools | Does the disruption reach routes outside exchange order books? |
| Assets | Do USDT, other stablecoins, and other cryptoassets exhibit related changes? |
| Countries | Is the disturbance local, transmitted abroad, or linked to wider conditions? |
| Financial routes | Do conversion, funding, withdrawal, and redemption routes respond differently? |

Possible objects of comparison include magnitude, onset, duration, liquidity, transaction cost, and the practical availability of an exit. These are candidate dimensions, not an adopted measurement list.

This direction may help explain an ongoing shock or supply features for a duration assessment. It may also remain a distinct explanatory workstream. The relationship is unresolved.

## 11. A cause-agnostic initial assessment

Felipe explicitly wants the framework to operate before the cause is known. An initial assessment could be based on observable market conditions, with subsequent updates as explanatory evidence arrives.

Candidate input families for later review include premium level, episode age, recent movement, cross-venue differences, trading activity, liquidity indicators, reference rates, and on-chain yield conditions. These are suggestions for investigation, not claims that the inputs are available or predictive.

A possible product sequence is:

1. Observe an unusual condition.
2. Describe its magnitude and breadth with information available at that time.
3. Estimate recovery outcomes and the holder's waiting cost under explicit assumptions.
4. Add evidence about the cause when it becomes available.
5. Update the assessment without rewriting what was known earlier.

The project may eventually distinguish detecting a shock, predicting recovery, explaining a cause, and comparing decisions. The current brief keeps these capabilities connected while leaving their implementation separate and open.

## 12. Candidate outputs

### 12.1 Index

An index is the product idea Felipe initially described. Its central meaning remains unresolved: it could summarize premium abnormality, expected persistence, the cost of waiting, or several outputs together. A later specification should make clear what a change in the index means to the user.

### 12.2 Decision framework

A framework could present the alternatives for a specified institution, estimated outcomes over its horizon, forgone interest, and the assumptions under which waiting or converting looks preferable.

The conversation has not determined whether the system should issue a direct action recommendation or provide estimates that a portfolio manager interprets.

### 12.3 Shock report or dashboard

A report or dashboard could combine observed conditions, recovery probabilities, scenario comparisons, and newly identified explanatory evidence. The interface has not been chosen. A dashboard is a possible presentation format, not an instruction to build a website.

### 12.4 Research output

Even if the final product takes another form, the research could contribute a documented episode collection, a recovery comparison, a benchmark-premium analysis, and a transparent holder-cost calculation. These are candidate deliverables for later assessment.

## 13. Relationship to the existing project

The existing project provides context on a Brazilian digital-dollar premium episode and its manifestation across observed markets. That motivates the new questions; it does not by itself establish recovery predictability or a validated institutional decision rule.

The proposed extension asks how the existing retrospective evidence could become useful while a future episode is unfolding. It could connect the description of a shock to expected persistence and the economic cost of waiting.

Existing research and task files should be consulted during later planning, including the primary project, the monitor, the illustrative holder analysis, the BRLA work, and the recent access-map and reconciliation proposals. These are neighboring inputs, not automatically dependencies or adopted components of this brief.

In particular, the newer proposals in P3-28 and P3-29 address access evidence and on-chain accounting. This brief records a distinct interest in recovery prediction and holder decisions. Their scopes should not be silently merged, and constraints belonging to another task should not be treated as Felipe having rejected the possibilities recorded here.

## 14. Questions deliberately left open

### 14.1 Holder and transaction

1. Which institutional profile should anchor the first scenario?
2. Did it acquire USDT before the shock or during an elevated premium?
3. What concrete example explains the role of the original purchase premium?
4. Must it preserve dollar exposure?
5. Are BRL and USD exits separate cases or competing choices?
6. What is its liquidity deadline, transaction size, and investment mandate?

### 14.2 Opportunity cost and alternatives

1. Does idle USDT mean a position earning zero yield?
2. Which alternative instruments can the institution actually access?
3. Should on-chain yield be a main comparison or an optional extension?
4. Which costs and additional exposures belong in the comparison?
5. Should the calculation describe total performance since acquisition, the decision from today onward, or both separately?

### 14.3 Shock and recovery

1. Which episode family is primary?
2. What starts and ends an episode?
3. What defines the previous range?
4. How should persistent changes in the benchmark be represented?
5. Which prediction horizons matter to users?
6. Should outputs describe remaining duration, total duration, or both?

### 14.4 Product and ambition

1. Is the core experience an index, a forecast report, or a decision comparison?
2. Should it recommend an action or supply interpretable estimates?
3. Which multiple outputs are essential, and which can remain separate research branches?
4. What belongs in a submission-oriented version versus a longer-term research agenda?
5. What resources and time should later feasibility work assume?

These are unresolved questions, not requests that must all be answered before a reviewer can use the brief.

## 15. Instructions for a subsequent research-model review

The next reviewer should use this document as a record of intent and preferences. Preserve the distinction between Felipe's main choices and the alternatives he asked to retain.

Suggested review sequence:

1. Restate the intended user problem and identify any interpretation that needs clarification.
2. Formulate several coherent research directions without prematurely combining every output into one model.
3. Explain how each direction connects retrospective shock evidence to a decision or an incremental research contribution.
4. Identify the data, definitions, and assumptions each direction would require.
5. Only then assess feasibility, including what can be investigated with the available project time and what belongs to a longer horizon.
6. Propose ways to evaluate recovery estimates and holder comparisons against simple alternatives.
7. Keep unsupported mechanisms and unavailable information visible.
8. Retain unsuccessful or deferred directions in the record rather than erasing them.

Future evaluation questions may include whether there are enough distinct episodes, whether comparisons across episode families are meaningful, whether predictions use only contemporaneously available information, and whether the output adds value beyond a simple historical-duration or no-model comparison. These are questions for the later review; this document provides no verdict.

## 16. Candidate narrative to develop

The following paragraph captures the ambition without claiming a result:

> Our current research describes how a disruption changed the price of the digital dollar. We now want to investigate what that evidence can offer an institution facing an ongoing shock: how unusual the premium is, how long it may remain outside its ordinary range, and what holding idle USDT costs relative to conversion and investment alternatives. Global episodes may help reveal common recovery patterns, while information about regulatory actions and market access may improve the explanation as it becomes available. The intended contribution is a decision framework grounded in observable conditions and explicit uncertainty.

This is candidate research framing, not a finished conclusion for the deck. A later conclusion must follow the evidence actually produced.

## 17. Handoff

**Completed:** Felipe's notes and subsequent answers have been organized into a detailed English brief. Main priorities, additional possibilities, candidate formulations, and unanswered questions are distinguished.

**Not performed:** Feasibility assessment, external-source research, new analysis, model selection, implementation, task adoption, deck revision, or changes to existing findings.

**Next use:** Give this document to the intended research models or collaborators for challenge and development. Resolve the transaction example and institutional alternatives when useful, then develop candidate plans and evaluate them in the order Felipe chooses.

**Authorization:** Do not infer permission to commit, push, run experiments, or adopt a workstream from the existence of this document. Felipe's instruction for the current session is not to push anything.
