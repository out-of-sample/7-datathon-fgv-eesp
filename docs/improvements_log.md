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
