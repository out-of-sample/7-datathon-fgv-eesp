# Project conversation log

This file records evolving research questions, reflections, and decisions from strategy discussions with Renzo. It is the continuity record for this conversation; append new dated entries rather than replacing earlier ones.

## How to use this log

- Label each item **reflection**, **hypothesis**, **proposal**, or **decision**.
- Mark a proposal as **proposed** until Renzo or the team explicitly adopts it. A research design becomes **pre-registered** only when it is fixed and committed before the relevant outcome data are examined; calling an idea a hypothesis here does not make it confirmatory.
- Include the evidence, limits, and relevant finding or source links. Register new external sources in [`sources.md`](sources.md) under the project’s source-opening rule in `prompt.md` §6.
- Keep entries dated and append subsequent updates, so the team can see how the question and its evidence changed.

## 2026-11-02 — Sharpening the project's story

### Reflection — The analysis is stronger than the current contribution statement

The study does more than notice two correlated series: it constructs a time-matched USDT/BRL premium, checks the dollar value of USDT, examines other exchanges and currencies, tests for breaks, and compares the June episode with ordinary dates. The headline arithmetic reproduces: the 20-day before/after difference is 93.9 bps, and the Binance gross-turnover calculation is R$106.1 million (`F-016`, `F-025`; scripts `p4_04_inference.py` and `p3_11_money.py`). These checks make the episode measurable and harder to dismiss as one venue’s data error.

They still describe one policy episode. Multiple venues and specifications strengthen measurement of that episode; they do not provide independent policy shocks. The present contribution needs to say what a reader learns about price adjustment and liquidity beyond “a local premium rose.”

### Reflection — Discovery and motivation are different parts of the account

The project’s own record says the 30 October probe revealed the jump before the hypotheses were written (`docs/README.md`, `docs/02-dolar-cripto.md`). Preserve that chronology. A candid research account is that the team explored the price series, noticed an unusual episode, found contemporary reporting that suggested a possible institutional explanation, and then tested its size and competing explanations. Exploratory discovery is legitimate; it must not be retold as a prior prediction.

The motivation can be stated without pretending it was the discovery method: Brazilians can obtain dollar exposure through several financial channels, and token prices may depend on the institutions that connect those channels. The economic question is what happens to the price and market liquidity when access for one set of intermediaries changes.

### Reflection — Narrow the novelty claim

The general connection between stablecoin/fiat price gaps and constrained arbitrage is already in the literature. The BIS Working Paper 1340 studies parity gaps across stablecoins, currencies, and exchanges (`L-11`). Contemporary Brazilian reporting also discussed the June notice, local price increases, and a supply-shock interpretation (`E-05.1`, `E-05.2`). An October commentary connected the episode to foreign stablecoin acquisitions and Brazil’s evolving FX rules (`M-06`). The project should claim a careful local measurement and diagnosis of this episode, not discovery of the general principle.

PTAX is a widely used Brazilian FX reference, but the premium over PTAX is a benchmark-relative price gap, not by itself the price every buyer could execute (`D-18`). Explain the measure in those terms and avoid implying that every positive premium is an anomaly.

### Reflection — The recovery may be the more informative story

The acute premium increase is robust, but the post-spike level is not distinguishable from ordinary variation (`F-022`). The question of how the market adjusted as the premium narrowed may therefore be more informative than treating persistence as the assumed result.

An exploratory, post-hoc analysis found that during the decline in late June and July, aggressive sellers crossed the Foxbit order book to sell about 362 million USDT net, mostly during Brazilian business hours (`F-031`). This is consistent with large-scale supply reaching the market through an observable route while the premium fell. It does not identify the seller, establish where the USDT came from, or show that the selling caused the price decline. Keep it explicitly exploratory unless independently reviewed.

The separate search for a public date when funds’ restricted FX import channel resumed found none. Its result is unresolved, and the available order-flow evidence is mixed (`F-030`). A new on-chain source check is blocked until Foxbit wallet addresses can be obtained from a citable source (`P3-18`). Do not turn the missing restoration date into evidence that the channel did not resume privately.

### Working question and title proposal — not yet a team decision

**Question proposal:** After a change disrupted one route used to supply Brazil’s USDT market, how large was the price dislocation, and what observable flows accompanied its narrowing?

**Title proposal:** *Um choque no dólar digital: prêmio e ajuste de liquidez no Brasil*.

This wording puts the measured price movement and the adjustment process in view while leaving the precise cause of the fade open. It should be revised if the team’s review of `F-031` or later evidence changes what can be claimed. The R$106.1 million result should be described as a benchmark-relative amount applied to gross Binance turnover, not as identified consumer losses, seller profits, or a welfare loss (`F-025`).

### Proposed next research focus — not yet a registered test

Assess whether a clear, independently reviewed timeline of the premium and the Foxbit seller-initiated flow would make a useful central exhibit. Keep the timing evidence separate from causal attribution; write a test specification before inspecting any new outcomes. The status of this proposal is **open**.

## 2026-11-02 — What the three improvements would require

**Status: explanation and proposals for discussion.** Renzo asked what the three improvements mean, what work could implement them, and why they could strengthen the project. No new project title, research design, or deck structure has been adopted in this conversation.

### State update and interpretation correction

- The log is now named `improvements_log.md`; links in the project index and primary plan follow that name.
- [P3-18](../tasks/P3-18-onchain-foxbit-source.md) is now **dropped**, superseding the earlier entry's blocked status. The task records unsuccessful searches for citable Foxbit Tron wallet labels. The explanation below does not depend on obtaining those addresses.
- The previous response's initial title candidate was *Um dólar, dois preços — O prêmio do USDT no episódio regulatório de junho de 2026*. The first log entry introduced another candidate, *Um choque no dólar digital*. Both are proposals, not decisions.
- **Correction to the earlier interpretation of F-031:** the code computes total traded volume minus twice buyer-initiated volume, which equals seller-initiated minus buyer-initiated trading volume. That statistic describes which side initiated trades. It cannot establish a single new supplier, an identified group accumulating or disposing of assets, new deposits, or net imports into Brazil. The earlier entry's language about supply reaching the market was too strong without this distinction.
- The approximately 362 million USDT arithmetic was rechecked from the frozen Foxbit hourly file on this turn; the result agrees with F-031. This verifies a calculation under the file's field definitions, not the economic inference. Foxbit's API documentation could not be opened through the web tool on this turn; the field mapping still merits direct source verification. Coinbase's official explanation of maker/taker orders was opened as a general definition (R-08), not evidence about Foxbit's particular schema.
- Counterexample (logical illustration, not empirical result): a trader can buy passively on one venue and sell aggressively on another. Only the aggressive leg appears as seller-initiated volume in this statistic. Summing signed trading volume across venues therefore does not identify net new asset supply. Similarly, business-hours activity does not identify how many traders participated or whether they were new entrants.
- The BCB source D-16 measures residents' **net acquisitions** of cryptoassets with corresponding liabilities, mostly stablecoins. Lower recorded net acquisitions cannot establish a fall in every gross supply channel or identify the affected funds.

### Improvement 1 — Define the economic contribution

**Problem.** The existing headline overlaps contemporary press accounts and prior research. The project must specify the extra knowledge supplied by its measurement. Rigor is necessary, but a list of methods leaves that contribution implicit.

**Concrete work proposed.**

1. Write a one-page comparison of prior knowledge, this project's measurement, and unresolved questions. Use E-05.1/E-05.2 and M-06 for existing Brazilian coverage, L-11 for the broader research, and F-009/F-022/F-024/F-029 for this study's evidence.
2. Set one central question: *How large and persistent was the Brazilian USDT price dislocation around June 2026, and how much of its adjustment can the observed evidence explain?* This is a framing proposal based on known results, not a newly pre-registered hypothesis.
3. State the contribution in plain language: comparable measurement across venues and reference prices; a distinction between the acute episode and the unestablished lasting effect; and an assessment of competing explanations of the adjustment.
4. Place unresolved causal attribution, trading-flow interpretation, and the gross-turnover nature of F-025 next to the relevant claims.

**Why it could help.** This gives an economist a reason to care beyond the existence of a price jump. An acute adjustment and a persistent price wedge have different economic interpretations. It also answers the motivation concern without inventing a different discovery history.

**Deliverable and check.** A contribution paragraph and a short claim/evidence table. Every proposed claim must map to evidence; any claim relying on an unobserved actor or route remains a hypothesis. Competition performance cannot be inferred from this exercise.

### Improvement 2 — Investigate recovery through competing explanations

**Problem.** The premium receded while recorded net foreign acquisitions stayed below the earlier level (F-024). This challenges a simple one-channel explanation, but does not identify the cause of recovery.

| Candidate explanation | Evidence that could distinguish it | Current constraint |
|---|---|---|
| The original activity resumed | A dated operational or regulatory record identifying the same activity | F-030 found no verifiable restoration date; private resumption remains possible |
| Different intermediaries or existing inventories supplied trades | Participant records, defensibly attributed asset flows, or inventory evidence | F-031 documents trade initiation, not identity or asset origin; P3-18 was dropped |
| Demand weakened | Evidence about buying intentions, client orders, or demand shifts alongside price | Trading turnover alone cannot separate demand from supply; failure of a volume threshold does not rule out a demand explanation |
| The recorded flow changed because of reporting coverage or classification | BCB compilation methodology, reporting population and treatment of transactions across the episode | F-024 explicitly leaves compilation details unverified |

**Concrete work proposed, in order.**

1. Verify what the BCB series includes and what the Foxbit candle fields mean. Record coverage changes and any details that remain unavailable.
2. Independently review F-031 and correct its interpretation before making it central to the deck. A descriptive finding about unusual selling pressure may survive even when a new-supplier claim does not.
3. Make a common-calendar figure for the full period before, during and after the episode, with separate panels for the premium, seller-initiated imbalance/trade size, and monthly net foreign acquisitions. Distinguish the daily and monthly frequencies; annotate externally dated events. A timing diagram makes competing explanations inspectable but does not establish causality.
4. Check whether descriptive patterns survive reasonable fixed alternative windows and consistent time zones. Existing known data remain exploratory; specifying a rerun now does not turn them into an untouched test.
5. If the team wants a general claim about arbitrage-channel disruptions, consider a separately selected episode with usable evidence. A further independent episode would address generality more directly than additional specifications of June, but feasibility must be checked before adding it to scope.

**Stop rule proposed.** If identity, source, or a restoration date cannot be observed, retain a bounded result: an acute premium episode followed by narrowing, accompanied by changes in trading behavior. Do not relabel ambiguous proxies as proof of substitution or restoration.

**Why it could help.** This could add economic explanation beyond the already reported jump and give the project a substantive adjustment question. Even a discriminating null result can clarify which popular explanation the data do not support. The gain depends on evidence that separates explanations, not simply another correlation.

### Improvement 3 — Organize the PDF around the argument

**Problem.** The current deck has dedicated blocks for methods and robustness, while the economic contribution and the recovery question are less prominent. A reader can remember the procedures without understanding what the study adds.

**Proposed ten-slide structure, for discussion only:**

| Slide | Reader's question | Main content |
|---|---|---|
| 1 | Why investigate this? | Dollar access through stablecoins and the June episode; central question |
| 2 | How could the price gap arise? | Diagram of the channels linking reais, dollars and USDT; relevant institutional change |
| 3 | What exactly is measured? | Premium definition, benchmark limitation, timing and data coverage; honest discovery chronology |
| 4 | What happened? | Acute premium increase, consistent measurement across venues |
| 5 | Could common alternatives explain it? | USDT/USD and FX adjustment plus currency comparison, with their limits |
| 6 | What happened afterward? | Complete rise-and-decline path; distinguish an observed decline from proof of no lasting effect |
| 7 | What can explain the adjustment? | Competing explanations and defensible trading/net-acquisition evidence; do not claim an identified supplier |
| 8 | Why does the magnitude matter? | Transparent transaction-size illustration; explicit assumptions and limits of aggregate turnover calculations |
| 9 | How much should we trust the conclusion? | Compact robustness evidence and unresolved identification issues |
| 10 | What did we learn? | One contribution statement, bounded implications, and the evidence needed to resolve the mechanism |

**Concrete work proposed.** Produce a text storyboard first, then the central chronological figure. Keep one main claim per slide, attach limitations where they matter, and put detailed specifications in the annex. The monitor and future prediction can be assessed against whether they strengthen this same argument.

**Comprehension check proposed.** Give the draft PDF to readers who were not involved in the analysis. Ask them to identify the problem, the added finding, and what remains unproven. If their answers reduce to “you ran several models,” revise the storyboard. This is a proposed check; it has not been performed.

**Why it could help.** The PDF must communicate without a presenter. A coherent order makes relevance, contribution and evidential boundaries easier to understand. It also makes overclaims more visible before submission.

### Suggested order — proposal

Contribution paragraph → verify measurement/interpretation → recovery exhibit and comparison of explanations → storyboard → reader comprehension check. The paragraph and storyboard can begin immediately; the strength of the recovery claim depends on what the measurement review establishes.

## 2026-11-02 — Team-review proposal requested

Renzo requested a complete proposal to investigate improvements 1, 2 and 3, including what to do and how each could improve the project. The resulting [team-review proposal](improvements-proposal.md) is **proposed, not approved**.

It defines a contribution/prior-knowledge audit, measurement verification and independent recovery review, bounded sensitivity checks, a competing-explanations exhibit, and a ten-slide storyboard tested with unfamiliar readers. Each workstream has deliverables, adoption criteria, failure outcomes and a stop rule. Suggested owners have not been assigned. The proposed effort cap is 17 person-hours; the existing 4 Nov results freeze remains binding.

New context since the earlier discussion: P3-19/F-032 already investigates whether Foxbit trade initiation tracked the premium or the cross-venue gap. The proposal reuses that work and requests independent review, including its weak within-day evidence, rather than repeating the original exploration. F-031's trade-initiation wording has now been corrected. The proposed threshold review distinguishes a fitted hinge from a zero crossing and from an identified route cost; this is a review question, not a new empirical finding.

Approval of an investigation will not establish its hypothesis or authorize a new title or conclusion. A second team gate determines which changes are adopted, narrowed or rejected. No new analysis, deck rewrite, reader recruitment or external communication was performed for this proposal.

## 2026-11-02 — Second agent's view added to the proposal

**Status: proposal, not a decision.** Renzo raised two concerns with a second agent: the project reads as a data-analysis routine, and the motivation looks built after the anomaly was seen. Renzo asked it to record its answer next to the existing proposal and compare the two. It is now §7 of the [proposal](improvements-proposal.md); §§1–6 are unchanged.

- **Reflection.** Concern 2 is true as history: the probe came first. The fix is to change the jump's role from premise to result. Two facts support that: the press reported the move on 24–25 Jun (E-05.2, E-05.6), and all eight dated rules got the same test, with one mover (F-026).
- **Proposal.** Central question: "O que move o preço do dólar digital no Brasil?" One idea: the premium is set by the cheapest channel still open. Five predictions are scored against existing findings. Three hold (two of them only as nulls, which rule out moves beyond about ±35 bps), one cannot be tested, and one is consistent but not separated from lower demand. The contrast inside one market is the claimed contribution: IOF 2025 +13.2 bps (p = 0.38) vs the notice +93.9 bps with −78% net acquisitions. The principle itself is not new (L-11).
- **Disagreements with §§1–6.**
  - It does not centre the story on recovery: every recovery finding is exploratory.
  - It keeps F-026 and F-027 on slides.
  - "Lições de 2025" goes on the method slide, per the 2 Nov decision.
  - It changes the title, adds a sixth reader question on how the episode was found, and caps effort at about 11 person-hours instead of 17.
- **Correction.** In chat, the agent said net acquisitions "roughly doubled after the May 2025 IOF rise". The base (Jan–May 2025) was a dip below 2024, and the premium had been falling since 2024 (59 → 42 → 32 → 11 → 7 bps). Three other changes fall in the same weeks: the tick cut, the STF injunction and the July 2025 break. The 2025 numbers are motivation, not substitution evidence; the command and table are in §7.2.
- **Source.** The Forbes Brasil column under E-03 was re-opened on 2 Nov via curl. Its quotes on the government's tax-arbitrage rationale and on the Receita figure (R$ 388 bn, over 70% in stablecoins) are in §7.2 but not yet in `sources.md`. The author is unconfirmed.

A team gate (§8, first row) chooses the backbone.

## 2026-11-02 — Review of proposed Ukraine / Argentina / EEA extension

**Status: critique and revised recommendation only; no P3-20 created, predictions committed, or event outcomes examined.** Renzo requested analysis of a proposal to test channel opening/closing outside Brazil. Relevant source checks are X-01–X-03 in the source register; F-010, P1-05, P1-06 and the current decision log were read. Firecrawl CLI remains unavailable; the web tool was used.

Recommendation: support a staged international extension, but do not call the current three-case design three clean independent confirmations. First qualify the mechanism and observable outcome of each event, then lock the analysis protocol, then run all eligible cases and report all exclusions and outcomes.

- **Ukraine:** secondary reporting describes individual FX-access easing, making it a plausible candidate; primary instrument and exact channel still unverified. Ordinary-date placebos benchmark unusualness under comparability assumptions; they cannot remove a coincident war shock or endogenous policy timing. Secondary reporting also dates another bank FX-position change to 1 Sep, inside the proposed four-week window. Specify announcement/implementation dates and overlapping measures before running. Earlier-ending windows change the estimand and must be selected on institutional timing, not outcomes. Delisting announcement timing was not independently verified here.
- **Argentina:** BCRA's 11 Apr announcement bundles access changes, exchange-rate bands and financing. Decomposing the premium into USDT/local-price, official-FX and USDT/USD legs explains arithmetic, not causal attribution. Wholesale-rate limitations cannot be solved by a footnote if the claim is about households' executable costs. Use a retail benchmark if verified or narrow the estimand to the official-reference gap. The latest team decision already reopens international research; the older future-work restriction is superseded, while the freeze choice remains pending.
- **EEA:** Binance's primary announcement is 3 Mar, with spot implementation 31 Mar at 23:59 UTC and intermediate changes. A pre-window around implementation is already exposed to the announcement. Global EUR quotes do not identify the cost faced by EEA residents excluded from spot access. An equivalence test with a prespecified economically justified margin is necessary to support a small-effect claim; nonsignificance alone is inconclusive. Substitutes remaining available does not logically imply exactly zero global price response.
- **Design discipline:** signs alone are insufficient. Lock selection/exclusions, mechanism, outcome and benchmark, announcement/effective dates, windows, calendar alignment, overlap screen, missingness/liquidity rules, inference, smallest meaningful effect, multiplicity policy and interpretation categories. Report rejected candidates with reasons; do not force an unsuitable event through identical code.
- **Prior exposure:** F-010 already reports EUR volatility and ARS/UAH means; the donor-event screen already names these events. Ask about plots, tables, model fits and agent outputs, not just plots. Describe an unseen-window analysis as a retrospectively specified extension conditional on prior knowledge, not a prospective forecast or untouched holdout without evidence.
- **Feasibility:** existing data reduces acquisition work but not exposure, benchmark or identification problems. P2-03's script is Brazil/PTAX-specific and writes core outputs; use isolated extension outputs. One person-day is an unvalidated estimate. Preferred sequence: qualify Ukraine and Argentina, treat EEA as a separate market-access boundary case, then authorize eligible event tests. Retain Brazil as the centre; international evidence supports the broader interpretation only to the extent each case permits.

No findings or adopted conclusions were changed by this review. The main gain would be testing where the proposed mechanism applies and where it does not, rather than counting three favorable signs.

## 2026-11-03 — Response to the review of the cross-country extension

**Status: plan, not a team decision.** Renzo asked the first agent to check the 2 Nov review above and propose a plan.

- **Accepted, checked against the repo and sources:**
  - Ukraine's 1 Sep bank FX-position change falls inside a four-week window. The first agent had seen it in search results and not handled it.
  - "More noise means less power, not bias" was wrong as stated: policy timing and war news can coincide with the event, and placebos cannot remove that.
  - Decomposing Argentina's premium is accounting, not identification.
  - The "future work only" line for Argentina is superseded by the "Research continues" row of the decision log.
  - The EEA restriction was announced 3 Mar, four weeks before it took effect; its pre-window is exposed to the announcement, and a global quote is not EEA residents' access.
  - A null result needs a stated bound.
  - Calling past episodes "predictions" was wrong: only rules not yet in force allow true predictions.
  - The prior-exposure check must cover tables, model fits and agent outputs. P1-06 already screened the EEA event.
  - Core scripts write their outputs when run, so extension code must not import them.
- **Applied to the first agent's own plan, P3-20** (predictions for 3 and 6 Nov), before registration:
  - a screen of overlapping events: Copom meeting 3–4 Nov, US midterms 3 Nov, US jobs report 6 Nov at 10:30 Brasília (inside the PTAX window);
  - null results stated as "no move larger than the band", never "no effect";
  - code isolation, with an assert that the frozen rows reproduce;
  - each venue and event reported on its own.
- **Where the first agent differs:**
  - The staged plan is right in shape but does not weigh the calendar. Five days remain before submission, with the deck, figures, scripts-as-.txt and rehearsal still open. Realistically only stage 1 (qualification) fits before 8 Nov; stages 2–3 are oral-final material at best.
  - The same standard applies to the Brazil nulls (F-026) and to F-027. Their wording should state the bound ("não detectável acima de ~35 bps") at the freeze.
- **Plan:**
  1. P3-20: Renzo reviews; push before 10:00 Brasília on 3 Nov.
  2. P3-21: who paid and who gained.
  3. P3-22: stage 1 only, capped at 4 hours, no outcomes computed; the team gate decides each case.

## 2026-11-04 — Competing-rails agenda recorded and datathon directions ranked

**Status: documentation requested by Renzo; investigation recommendations, not adopted conclusions.** Renzo asked to preserve the preceding brainstorm in English for the team and its agents, then rank the hypotheses within datathon scope and validate the assessment. Task: P3-23.

- The [research agenda](competing-rails-research-agenda.md) records six directions: recovery mechanisms, channel-specific predictions, executable-payment performance, BRL stablecoin architecture, user incidence, and conventional-FX spillovers. It preserves the original request not to constrain the long-run agenda by time or feasibility.
- The separate [datathon ranking](competing-rails-datathon-ranking.md) recommends H2, H1, H3, H5, H4, H6, based on incremental information and what available observations identify. It gives procedures, outputs and failure conditions for each. No new extension outcomes were computed or downloaded.
- Checks covered current tasks, actual CSV schemas and frozen output tables, the implemented P3-20 command dispatcher, cost-accounting endpoints, and opened official/literature sources. The IMF sandwich paper remains indexed-abstract-only; its landing page returned 403. This is prerequisite/design validation, not empirical confirmation of the hypotheses.
- Sync brought in Felipe's research/conclusions memo (`7204a38`). Its proposals are cross-referenced rather than overwritten. Review notes address unresolved Foxbit attribution, net versus gross acquisitions, BRLA peg logic, profit/welfare and tax claims, and form-versus-content identification.
- Important P3-20 checks: only `reference` is implemented; E1 readout must still be built under the existing task; S2's Binance reference quantiles are −75.5/+59.8 bps, not S20's −35.4/+37.7; E2's primary two-day verdict requires 9 Nov, after PDF submission. These numbers are existing registered outputs, not new estimates. No November prices were inspected.
- Inference refinement to earlier discussion: a non-significant result inside ordinary-date quantiles does not itself establish a bound on a causal effect. Report the registered p-value and reference variability; formal equivalence requires a separate justified design. Preserve the registered prediction, including its failures and conceptual limitations.

The two documents are linked from `docs/README.md` and STATUS. Core findings, active task specifications, the deck, and Felipe's memo were not changed. Next: team review of the ranking, and separate task/specification records for any adopted analysis.

## 2026-11-04 — Felipe: a useful conclusion without a forecasting claim

**Status: strategic discussion for P5-08, not an adopted conclusion or a new empirical result.** Felipe asked for a practical "so what", including alternatives outside the mentor's leads. Reviewed mentor notes, corrected Flash dossier, competing-rails plans and existing findings; one Luna agent challenged the proposed interpretation. A successful pull to `82f5494` added F-035 before this note was written (the initial unprivileged pull had failed).

- Recommended backbone: **the cost of access to the digital dollar can rise materially even without a dollar-peg failure**. F-009/F-015 establish the local premium and transaction-scale consequence. F-018 shows that switching to the observed BTC/BRL pair did not remove the premium; triangular arbitrage means this is not independent identification of the original shock's scope.
- Concrete proposed use: replay the observed acquisition-cost path against a specified operator's funding commitments and margin, as a historical stress scenario. This does not estimate event probability, an optimal reserve, profitable arbitrage, or savings from an unobserved alternative route. Route redundancy is an operational hypothesis to evaluate, not a demonstrated remedy. No new calculator or simulation was built.
- Policy implication: assess local acquisition costs alongside recorded net external purchases; price normalization alone does not establish restoration of the previous flow pattern. F-024's net purchases are not gross supply, and their persistence does not prove continuing impairment. P3-25 could add observed venue-composition evidence; its owner continues that work.
- An index can describe current conditions. F-014 detects the jump after it is present, and the simple baseline detects it too. The pre-event accumulation is not validated foresight. A trading signal needs independent events, executable prices and a baseline; renaming the premium does not supply them.
- Flash: BRLA is possible corroboration within the same event, not a second shock or an identified BRL depeg. EWZ's stale observation and Coinext's separately attributed closure cannot support macro spillovers or notice-caused exit. The turnover-weighted money estimate is neither welfare loss nor identified supplier profit.
- Latest F-035 is an exploratory prospective no-unusual-move result awaiting independent review. It agrees with the no-change baseline. Its ordinary-date quantile band is not a confidence bound on the causal effect; avoid the finding's "rules out" wording in Slide 10. This discussion does not independently reproduce its calculation.

Suggested next step: choose one named user and decision for Slide 10; lead with measured local access cost, use a historical stress illustration if the team adopts it, and keep the registered prediction as a discipline check. Mentor questions are useful leads, not requirements to demonstrate equities or FX spillovers. Existing frozen findings and deck remain unchanged.


## 2026-11-05 — Critical discussion of the lessons-and-solution proposal

**Status: review and proposals, not adopted scope, deck text or new empirical findings.** Renzo requested candid evaluation of `proposal-2026-11-05-lessons-and-solution.md`. Read the brief, status, decision log, phases, mentor synthesis, competing-rails ranking, conclusions memo, relevant findings and the v3 conclusion. Read monitor and turnover-accounting code; checked existing CSV outputs. The initial pull was blocked by pre-existing changes to STATUS/README and the untracked proposal; those changes were preserved. Firecrawl CLI is unavailable; external checks used the web tool.

**Recommended direction.** Keep a reproducible diagnostic of digital-dollar access costs, with the June episode as an observed stress scenario. Do not promise the causal cost of each regulation on the following day or validated forecasts of future rule costs. Separate measurement (premium), unusualness detection (alarm), event attribution (design and competing explanations), and prospective prediction scoring. PTAX is a benchmark, not every customer's executable alternative. A rule can change costs other than the premium, and policy benefits are outside this study.

**What the review verified.** Read-only recomputation from `P1-02_premium_daily.csv` reproduces F-016's before/after means and difference. F-035/F-036/F-037 values match their stored tables; that inspection is not an independent raw-data rerun or teammate sign-off. Existing results retain their current statuses. `scripts/p3_03_monitor.py` sets `QUIET=10` and resumes at `t + QUIET + 1`; its stored last row has a 30 Oct downward alarm. The proposal's 6 Nov "sem alarme" demonstration would occur during the mandatory pause. Show "alarm paused" separately from current premium if used.

**A newly located competing event.** Opened Binance's official incident update and follow-up (M-11/M-12): incident on 29 Oct UTC and a withdrawal suspension. The searched project docs/findings/P3-20 did not record it. This could matter for the Binance-only 30 Oct dip, the monitor alarm, and the November baseline/comparison. It is not established as their cause and does not invalidate the June episode. P3-26 records a bounded, unassigned follow-up: establish token-specific restoration and disclose overlap while preserving P3-20's registered scoring rule. Do not advertise November as clean policy validation before this audit.

**Claims to tighten before adopting the proposal:**

- Lesson 1: use "nas quatro semanas após o ofício". F-029 explicitly says the month includes the meeting and Res. 580. One immediate restriction versus heterogeneous public rules does not identify the benefit of advance notice. Keep this qualification in visible wording; first-round readers cannot depend on speaker notes.
- The headline change is a difference in premium, not the final all-in route price. F-025 is benchmark-relative gross-turnover accounting, using daily premiums and carried-forward PTAX-day values; it does not measure net household loss, market-maker profit, or welfare. Avoid an unqualified "regulatory bill".
- Lesson 2: prefer "o prêmio também apareceu na rota on-chain observada". F-037 measures one thin BRLA/USDC pool, with par BRLA/BRL assumed and no historical full-size executable quote. Similar increases do not establish equality of costs or independent confirmation from another shock. A stable BRLA/BRZ relative price is not proof both held their fiat peg.
- Lesson 3: keep the distinction between price recovery and observed composition, with "aquisições líquidas registradas" for F-024 and "nas três corretoras observadas" for F-036. Neither lower net acquisitions nor changed venue shares proves ongoing impairment, national concentration or rerouting caused by the notice.
- E1: the observed change was ordinary under the registered comparison, and agrees with the no-change baseline. This is discipline, not demonstrated forecasting skill. Ordinary-date quantiles are not confidence bounds on the causal effect; the proposal's "no effect above ~35 bps" and F-035's "rules out" language are not justified by non-rejection. E2's primary verdict needs 9 Nov; the PDF can only report the registered preliminary reading. Its branch C has no directional prediction.
- Cost stack A: optional illustration, not the priority empirical contribution. R-04's fee remains unverified; the newly opened FAQ R-12 confirms fees can vary, not the 1 USDT value. Specify transfer size, network, dated fee assumption and endpoint. A withdrawal fee is not interchangeable with a generic chain gas estimate. Current fees plotted against historical premiums are a scenario, not observed historical total costs. Do not use a huge fee ratio as evidence of causal identification.
- Scale B: retain the warning that only part of the market is observable. Reject an estimated share of Avenia business from pool turnover divided by a company's unmatched peak monthly payment flow. Dates, gross/net accounting, assets and perimeter differ; a residual is not identified off-pool mint/redemption volume.
- Ladder C: omit from the conclusion. Cross-country official benchmarks and periods differ; "one door versus several" implies an unestimated dose-response. D/E and AI analyst runs do not address the current claim/review gaps; preserve deferrals unless the team changes scope.

**Novelty check.** BIS L-11 and L-12 landing pages were reopened. Local parity gaps, limits to arbitrage, and conversion/intermediary costs beyond chain fees already appear in the literature. The defensible contribution is a carefully measured Brazilian episode, tracing its magnitude, breadth, recovery and limits, with reproducible diagnostics. The exact privately supplied Polygon PDF was not read, so its report-wide sourcing and volume claims are not independently verified here.

**Suggested practical use.** A payment operator can evaluate the observed premium and replay the June acquisition-cost shock against a specified dollar obligation. That supports a historical stress calculation, not an optimal reserve, probability forecast or proof a substitute route will work. A regulator can use the joint price/flow/venue evidence to flag episodes requiring investigation, not to read causal costs or net welfare directly from a gauge. Keep one user and decision prominent in the ten-slide PDF.

**Priority recommendation.** Resolve claim limits and the November competing event; obtain the already-required teammate reviews of new findings; simplify Slide 10 to one lesson, a few supporting facts and a concrete use. An optional cost illustration comes after those. No new pool downloads, model runs, deck edits or frozen-result edits were performed in this review.

## 2026-11-06 — Agentic AI, blockchain and operational prediction: options that add capability

**Status: requested exploration, not adopted scope or empirical results. Task P3-27.** Renzo asks to take fashionable technology seriously as a competitive consideration, while preserving rigor and avoiding forecasts of exchange rates, interest rates or the market response to regulation. He reports that the opening highlighted AI agents and blockchain; this is attributed to his firsthand account, not independently verified as a scoring preference. He explicitly wants alternatives that expand the project's scope. Firecrawl CLI is unavailable; sources T-01 to T-12 were opened with the web tool.

**Correction to the previous recommendation.** Renzo objected that the historical cost/stress worksheet repackages existing work. F-033 already contains illustrative user cost cases: that suggestion is not a new research contribution. A new extension must add a new outcome, a new dataset, a tested intervention or a demonstrably useful capability. P3-05 has a bundle/protocol/harness, but live memory/isolation tests and pilots remain unchecked; P3-06 is not started. P1-06 was completed by the manual fallback, with agent validation waived. Neither is an already-validated AI result.

**1. Agent-assisted payment completion under constraints (largest product expansion).** User: a Brazilian business or its software agent paying a specified digital service. Hypothesis: a workflow that retrieves provider conditions, checks quote freshness and network compatibility, and repairs a failed plan completes more valid payments at acceptable total cost than fixed-route automation. Deliverable: a small executable laboratory with specified origin/destination assets, amounts, deadlines and budgets, source-backed route records, a deterministic constraint/optimization layer, and x402 testnet payment receipts. The agent chooses the next information/tool step; it is not asked to predict prices. BRL funding would remain explicitly simulated until a real eligible provider integration is available.

Compare fixed route, greedy cheapest quote, a deterministic constrained planner and the agent-assisted planner, with equal information access, budgets and scenarios. Isolate the agent contribution by keeping the optimizer the same. Use held-out provider formats and scenarios including unavailable withdrawals, stale quotes, incompatible networks, insufficient depth and conflicting documents. Count correct completions, violations, appropriate abstentions, interventions and total costs including failures, inference and fees. Testnet establishes protocol/constraint behavior, not live-market savings. Real quotes establish quoted costs, not execution. x402 already exists (T-03); conventional routing already exists (T-04/T-05). The contribution would be tested resilience for specified Brazilian funding constraints. If an ordinary workflow performs equally well for less, agent superiority fails. A simulator showing only the June premium replay would repeat F-033.

**2. Agent-assisted reconciliation of BRL stablecoins across chains (strongest new empirical branch).** User: researchers, payment operators and risk teams interpreting supply/liquidity dashboards. Hypothesis: some apparent supply contractions reflect chain migration, treasury classification or aggregation differences, and a reproducible reconciliation can distinguish documented accounting movements from unexplained changes. Start with F-037's unresolved BRLA Celo supply movement as a known development case; broaden to additional preselected dates and, if feasible, BRZ/BRL1 contracts. Deliverable: supply/flow ledger by chain, verified mint/burn/bridge events, reproducible transaction references and an unresolved-balance report. Add a dependency graph only where issuer/bridge/venue links are documented; address concentration is not owner concentration.

The agent locates contracts and ABIs, selects investigative queries, reconciles documentation and proposes explanations. Deterministic code checks balances and events; no LLM supplies the accounting arithmetic. Compare with a rules-only reconciliation and manually audited cases held out by token/date, measuring supported classifications, unsupported claims, unexplained residuals, analyst time and retrieval cost. Match source snapshots to block times and handle wrapped assets/bridge double counting. Synthetic accounting faults may supplement real cases, separately labelled. Avenia's current terms list contracts (T-06), but historical log/state access remains untested and F-037 reports explorer access trouble. A burn is not proof of fiat redemption; bank settlement and reserve claims need separate evidence. If the unresolved movements cannot be classified, report that rather than inventing a mechanism. This adds issuance/migration/infrastructure outcomes instead of another premium chart.

**3. Source-backed map of access conditions and shared dependencies (best small agentic pilot).** User: an operator evaluating a payment route or researcher screening events across jurisdictions. Hypothesis: tool-using document investigation reduces extraction/update work while maintaining a lower rate of unsupported route-availability claims than a single retrieval-and-answer call. Deliverable: a dated graph of actors, permitted/advertised operations, eligibility, effective dates, limits and source passages, with explicit unknowns. It can expose several advertised routes sharing one issuer, bridge or banking dependency, but only if that relationship is documented. Rule text and advertised terms do not establish practical account access or executable capacity.

Freeze a source corpus and a human-labelled benchmark (ideally two independent readers with adjudication). Hold out entire documents, amendments and providers, not random chunks. Measure date/actor/operation correctness, unsupported 'available' classifications, coverage at a fixed error tolerance, time and cost against manual review, keyword rules and a single LLM using the same corpus. Remove verification or tool iteration to test their contribution at matched compute budgets. A graph of only our already-coded June rules is mostly organization; expansion to operational conditions and genuinely held-out sources is the new capability. Retrospective documents must never be presented as information available in June. T-02 is recent precedent for claim-level grounding evaluation, not a validation of our design.

**4. Tabular foundation model for operational failures/delays (plausible prediction, missing labels).** Candidate: TabPFN-3.5 (T-08/T-09), compared with recent-rate/median rules, logistic regression, gradient boosting, and relevant deterministic preflight checks. Predict a precisely defined failure or settlement-deadline outcome for submitted transactions, using only information available at submission. Deliverable: calibrated probabilities that a payment planner can use; utility is fewer missed obligations at comparable cost. Time-split and group by incident/provider; report calibration, rare-event precision/recall, coverage and downstream costs. Do not train a failure predictor from successful-transfer logs only, or infer waiting time from block timestamps alone. Null receipts are not failed transactions (T-07). The repository's candles and supply snapshots do not provide this labelled dataset. A small-data model does not create independent incidents. This is a data-collection branch, not a credible ready-to-run result for the PDF.

**5. RL for liquidity placement and replenishment (ambitious operational expansion).** User: a payment operator serving exogenous obligations. State: balances per rail, queued invoices, transfer lead times and observed fees; actions: rebalance, replenish or defer within a deadline. Hypothesis: a sequential policy improves the tradeoff between idle capital, transfer cost and missed payments. Deliverable: controller plus transparent simulation benchmark, with hard budget/access constraints outside the learned policy. Compare fixed buffers, threshold replenishment, and optimization/control with identical information; use held-out demand regimes, outages and cost assumptions, not only fresh random seeds of the training simulator. Include a fixed-exchange-rate version to show the contribution is payment operations. T-10/T-11 establish methodological precedent. Our single June episode cannot identify the distribution of future interruptions, customer demand or counterfactual fills. Without operational data, conclusions are restricted to the stated simulator. Lower short-term priority than 1–3; static route selection alone does not justify RL.

**6. Upgrade the planned analyst experiment into an error-detection benchmark (most reuse, narrower expansion).** P3-05/P3-06 remain optional and unexecuted. The existing protocol can study analytical variation; any intervention/audit arm must be separately specified before new runs. Add known data defects (timestamp units, stale quotes, denominator mismatches), clean negative controls and independently checked reference calculations. Compare ordinary analysis with tool-assisted verification, measuring undetected defects, false alarms and reproducibility, not closeness to our preferred estimate. Separate different estimands/windows from coding errors. Use known synthetic truth only in labelled synthetic cases. T-01 cautions that convergence can reflect imitation. Multiple runs/model families remain correlated; they do not create multiple economic shocks. Pin actual available model IDs and validate isolation before claiming it.

**Recommendation for discussion.** For broader product ambition, prioritize 1; for an empirical addition grounded in this project's open questions, prioritize 2; for a bounded agentic pilot with existing documents, prioritize 3. Choose at most one new empirical branch for the current deck. Option 6 has the most prepared infrastructure but still needs live setup and adds less scope. Options 4–5 are plausible follow-on research, contingent on new data and a validated operational environment. For the 8 Nov PDF, require one bounded evaluated capability and a result readable without a live demo; implementation plans alone are not results. No ranking predicts jury preferences or a win.

**Ideas not recommended at this stage.** A chatbot summarizing our charts; registering report hashes on-chain without a demonstrated multi-party verification need; training a large neural model on one regulatory event; LLM trader personas; RL with profits from the already-seen shock as its reward. ERC-8004 is a current draft about agent identity/reputation/validation, not proof that an agent is correct or a payment standard (T-12). x402 transaction counts do not by themselves identify AI-agent activity.

No agent runs, model training, bulk downloads, paid services, transactions, deck edits or finding changes were performed. Technical precedents and design prerequisites were checked; the proposed hypotheses remain untested. The current Avenia contract table is a new primary source, not a reconstruction of June history. Team selection and a separately scoped task/specification are the next steps if an option is adopted.

### 6 Nov follow-up — How the current findings connect to those solutions

Renzo asks for an integrated narrative, not another list of technologies. **Proposed framing, not an adopted deck:** the usefulness of a stablecoin depends on access conditions as well as its dollar peg. The existing study measures a Brazilian access-cost episode; a new tool must then be evaluated on whether it improves investigation or payment operations. The June result establishes neither the effectiveness of an agent nor savings from rerouting.

**Evidence-to-design links:** F-009/F-016 establish a premium increase across observed exchanges after adjusting for fiat FX and USDT/USD, motivating monitoring local acquisition costs. F-018 and exploratory F-037 show that the observed BTC pair and BRLA/USDC pool also reflected the episode: a different asset or interface did not establish insulation. The BRLA calculation assumes parity to reais and is not a completed-payment cost. F-024 records net foreign stablecoin acquisitions, not gross supply; together with exploratory F-036 it shows that price normalization coexisted with different recorded flows and a different venue mix. This does not establish persistent impairment or identify the recovery mechanism. F-028/F-030 leave the marginal supply route and reopening unresolved; lack of public evidence must remain unknown. F-014 provides a detection component, not prediction or a continuously available November alarm during its mandatory pause.

| Proposed extension | Role for existing findings | What must be added and tested |
|---|---|---|
| Payment-completion agent | Motivating case and requirements: include local acquisition cost, verify eligibility/capacity, account for shared price stress | Actual or explicitly simulated route conditions, quotes and operation records; independently evaluate completed obligations, failures and costs. No claim that an agent would have avoided June's common premium. |
| On-chain investigator | F-037's unresolved supply changes are a known development case; F-024/F-036 motivate distinguishing economic flow from trading or accounting movements | Reconcile contract events and chain balances; test other token/date cases. No inference of fiat redemption, trader nationality or the source of Foxbit selling from anonymous transfers alone. |
| Access/dependency map | F-028/F-030 demonstrate missing access information and the distinction between an advertised category and a usable route | New dated conditions/dependencies, source-linked unknowns and held-out extraction tests. Reformatting the current route table alone adds no evidence. |
| Operational prediction | General motivation to evaluate payment reliability | A separate labelled dataset of attempts and timing; existing premium observations are not labels for operational failure. |
| RL liquidity control | June supplies a disclosed historical price-stress scenario | Operational demand, inventories, transfer delays and a justified environment. One episode cannot calibrate disruption probabilities or establish optimal reserves. |
| AI analyst/error benchmark | Raw data and measurement challenges are direct inputs | Evaluate reproducibility/error detection; keep this as method evidence, not the economic mechanism or independent causal confirmation. |

**Two coherent stories, with different continuity.** (A) *From access costs to verifiable access conditions*: measure the episode, establish its breadth, show that normalization does not identify the mechanism, then evaluate an investigative agent on new source-backed cases. A bounded access-map or reconciliation pilot is the strongest narrative continuation. The loop is existing measurement → evidence retrieval → deterministic checks → supported conclusion or explicit unknown, with every result separated by provenance. A retrospective June walkthrough is demonstration/development; generalization requires held-out cases. The illustrative output can correctly say a route's price is observed while withdrawal access and executable size remain unverified. That is useful only if evaluation demonstrates better coverage, reliability or effort beyond the manual work already done.

(B) *From access costs to payment resilience*: an operator has a fixed obligation, the study documents that acquiring the required digital dollars can become more expensive, and a new payment agent is tested under operational constraints. This has larger product scope but needs a substantial new evidence layer. It must be able to refuse an infeasible budget and acknowledge stress shared by all routes. A single LLM converting a cost table into prose, or a June replay with no new decisions/outcomes, remains repackaging. Deep learning and RL would be later modules only if they improve a separately measured operational target.

**Recommendation refinement:** option 1 remains the broadest product idea, but options 2/3 have stronger continuity with the evidence currently available. Prefer one evaluated capability for the datathon. A proposed ten-slide arc would allocate seven slides to problem, measurement, June result, breadth, normalization/composition and the resulting information gap; three to the bounded solution, its held-out evaluation, and conclusions/limits. F-036/F-037 retain exploratory status and review requirements. No deck or frozen finding was changed.
