# Proposal for team approval: contribution, recovery, and presentation

> **Estado na entrega (8 nov 2026): PROPOSTA HISTÓRICA / NÃO ADOTADA INTEGRALMENTE — não tratar como compromisso de execução.** Veja [estado final](estado-final.md).

**Status:** proposed; no team approval recorded.  
**Requested by:** Renzo. **Prepared:** 2 Nov 2026.  
**Decision requested:** approve a bounded investigation of three improvements, followed by a separate decision on what enters the submission. Approval of the investigation is not approval of its hypotheses or a replacement title.  
**Discussion history:** [improvements log](improvements_log.md). **Constraints:** [project brief](../prompt.md), [phases and freeze](phases.md).  
**Second view (added 2 Nov):** §7 gives a different answer to the same concerns, from a second agent, and compares it with §§1–6. The team chooses one backbone at the gate in §8.

## 1. Purpose and expected improvement

The concern is that a technically robust project may still read as a sequence of analyses confirming an observed spike, with a motivation constructed afterward. We propose testing whether a more explicit contribution, a careful investigation of recovery, and a question-led PDF can address that concern.

| Workstream | Question to investigate | Proposed improvement | What would count as failure |
|---|---|---|---|
| A — Contribution | What does our evidence add beyond reporting and existing research? | A specific economic question, honest discovery history, and a bounded contribution | The proposed novelty is already established elsewhere, or our evidence cannot answer the question |
| B — Recovery | What can we establish about adjustment after the premium increased? | Additional understanding of market adjustment, with competing explanations assessed | Only another correlation is found, measurement is unreliable, or mechanisms remain observationally indistinguishable |
| C — Presentation | Can unfamiliar readers identify our question, finding, and limits from the PDF? | A clearer standalone argument within ten slides | Readers still cannot identify the contribution, or the revised story encourages stronger claims than the evidence permits |

These are expected benefits to test, not evidence that the project will win. A rigorous descriptive case study remains a valid fallback. A causal explanation, identified supplier, new product, or general theory is not required for this proposal to succeed.

## 2. Starting evidence and limits

This proposal is based on repository evidence reviewed on 2 Nov; it does not report a new empirical test. Each finding below remains subject to its recorded review status.

- The cross-venue spike and robustness work already exist: [F-009](../findings/F-009-jump-not-venue-fx-usdt.md), [F-022](../findings/F-022-robustness-battery.md). Failure to distinguish the post-spike residual from ordinary variation is not proof of zero persistence.
- The one-month headline includes multiple institutional developments. Review [F-029](../findings/F-029-headline-inference.md) and the pending event-list work before attributing it to one notice.
- [F-024](../findings/F-024-stablecoin-imports.md) uses aggregate net foreign acquisitions, not fund-specific gross supply. [F-030](../findings/F-030-no-verified-reopening.md) does not identify a verified reopening date.
- [F-031](../findings/F-031-who-traded-the-fade.md) now distinguishes seller-initiated trading from new supply. [F-032](../findings/F-032-supply-response.md) already tests association with the premium and the cross-venue gap; the daily association is stronger than the within-day evidence. It is exploratory and awaits independent review.
- [P3-18](../tasks/P3-18-onchain-foxbit-source.md) was dropped for lack of citable wallet identification. This proposal does not reopen it.
- The current deck already has ten slides. Workstream C compares against that version, not the earlier fourteen-slide deck. Its owner retains control of integration.

External context is registered in [sources](sources.md): contemporaneous reporting E-05, literature L-10/L-11, BCB methodology and data D-16/D-18, and general maker/taker terminology R-08. Reviewers must open the relevant sources themselves before adopting claims; an abstract is not a full-paper review.

## 3. Workstream A — Test the contribution

### Proposed question and metric

Candidate question for evaluation:

> Quanto o dólar digital encareceu no episódio de junho de 2026, quanto tempo esse encarecimento durou e o que os dados permitem dizer sobre o ajuste posterior?

Keep the existing time-matched, USDT/USD-adjusted premium in basis points as the primary outcome. Retain the current headline estimator and baseline while reviewing its interpretation; do not switch estimators to make the new story stronger. Recovery and trading measures are secondary. Define “duration” using the existing recovery analysis, with uncertainty and sensitivity, rather than choosing a visually attractive return date.

### Investigation

1. **Audit prior knowledge.** Read the relevant event reporting and literature, including the full BIS paper if accessible within the time budget. Build a table with source/date, exact claim, geography/episode, method, and whether our proposed contribution duplicates or extends it. Mark inaccessible sources. Do not claim “first study” from a limited search.
2. **Reconstruct discovery honestly.** Use the probe, dated commits, task specifications and findings to record what was observed first, which questions followed, and which rules were fixed before later calculations. Distinguish an algorithm that did not receive event dates from researchers who had already seen the episode.
3. **Build a claim-to-evidence table.** For magnitude, persistence and recovery, list the supporting finding, reproduction command, benchmark, alternative explanation, reviewer, and permissible wording. Separate measured, consistent with, illustrative, and not identified.
4. **Draft a short contribution paragraph in Portuguese.** It must state the prior knowledge, what we measured beyond it, and what remains unresolved. Prepare a descriptive fallback if the recovery mechanism cannot be established.
5. **Independent challenge.** A teammate who did not write the paragraph must answer: “What did this add beyond the news?”, “Why is it economically relevant?”, and “Which sentence would we have to remove if recovery evidence fails?” Record objections and revisions.

### Deliverables and adoption gate

Deliver a one-page contribution memo, source comparison, discovery timeline, and claim-to-evidence table. Adopt the framing only when every factual clause has evidence, the added contribution is distinguishable from prior reporting, and the question is answerable without pretending causal identification. If those conditions fail, narrow the claim; do not compensate with a stronger title.

**Why this helps:** it makes the contribution assessable and gives the motivation an honest origin. It can improve relevance and clarity without adding statistical complexity.

## 4. Workstream B — Test what recovery can teach us

### B1. Validate the measurements before interpreting them

- Verify Foxbit candle field definitions against accessible official documentation or a documented provider response. Reconcile sample candles with available underlying trade records if feasible. Check units, duplicates, missing hours, time zones and whether taker-buy volume is bounded by total volume. Arithmetic consistency alone does not establish field meaning.
- Verify BCB net-acquisition coverage, reporting population, revisions and any classification changes. Write explicitly which transactions and institutions cannot be separated.
- Review PTAX timing and benchmark limitations. A reference rate is not necessarily an executable funding rate; hourly prices against a morning reference may incorporate later FX movement.
- If a critical definition cannot be verified, exclude that variable from a mechanism claim. The premium trajectory can still be presented separately.

### B2. Review existing results rather than repeat their discovery

A teammate other than the original analyst reproduces P3-17 and P3-19 from frozen inputs, recording input checksums, commands, environment, row counts and discrepancies. Read script output paths before running; use a temporary checkout/output directory or preserve existing outputs so comparison does not silently overwrite the reference evidence.

Review these interpretation issues explicitly:

1. Does the daily premium association survive accounting for the common episode timing? The weak within-day result already limits a price-response interpretation.
2. The cross-venue coefficient's uncertainty includes zero. That does not prove that cross-venue arbitrage is absent; limited variation may make the comparison inconclusive.
3. A fitted hinge location is not automatically the point where predicted imbalance crosses zero. Recompute those separately if used. Neither is an identified marginal route cost or a cost bound without additional assumptions about participants, inventory and execution.
4. A pre-run rule written after observing related data remains exploratory. Passing that rule does not make this an independent confirmation.
5. Positive trade-initiation imbalance cannot establish trader identity, deposits, imports, or the cause of declining prices.

Preserve the original reported results and rules. Any additional specification must be labelled a new sensitivity check, not a replacement selected for significance.

### B3. Bounded sensitivity checks, specified before execution

Retain the original P3-19 model as the reference. Before running any added checks, the reviewer fixes a short specification sheet and commits it under the normal team protocol:

- Add calendar-week effects to the daily association as a check on common episode timing. Report lost identifying variation and wider uncertainty rather than interpreting an imprecise estimate as proof of no relationship.
- Compare absolute initiation imbalance with imbalance divided by total volume over the same window; exclude and count zero-volume windows. This asks whether the pattern is mainly scale or also trade composition.
- Re-estimate uncertainty using blocks of 3 and 10 PTAX days alongside the existing 5-day blocks. Keep all results.
- Report leave-one-calendar-week-out estimates as an influence diagnostic, not independent experiments.
- Reuse existing recovery-window sensitivity from F-022. Add no new recovery dates solely to improve fit.

These checks are proposed, not performed. Do not add model families or continue searching after seeing an unfavorable result. If the time budget is exhausted, report which checks were not run and keep the claim descriptive.

### B4. Compare explanations and construct the exhibit

| Explanation | Evidence that would help distinguish it | What the existing proxies cannot establish |
|---|---|---|
| Original channel reopened | Dated, verifiable operational authorization/resumption evidence | Absence of a public announcement does not establish continued closure |
| Other intermediaries or inventories supported adjustment | Participant, inventory or traceable flow evidence; reliable institutional chronology | Trade initiation cannot identify foreign sourcing or new entrants |
| Demand weakened | Independent demand indicators with documented coverage | Turnover alone does not separate demand and supply |
| Trading/reporting coverage changed | Provider methodology, exchange migration/partnership timing, reporting changes | A venue's volume increase need not represent a market-wide increase |
| Common conditions changed both prices and trading | Timing controls and transparent sensitivity comparisons | Temporal order alone does not remove common causes |

Create a common-calendar exhibit covering January–September 2026, with a clearly labelled June–July inset if useful. Separate panels show premium by venue, validated trading measures, and monthly BCB net acquisitions. Do not interpolate monthly data into daily observations, sum exchange imbalances into “national supply,” or place incompatible units on a misleading shared scale. Annotate externally dated events and coverage gaps. Treat exchange partnerships as alternative explanations, not established causes.

### Deliverables and adoption gate

Deliver a measurement note, independent reproduction report, complete sensitivity table, competing-explanations matrix, and one reproducible figure with a Portuguese caption. Each new empirical result gets a finding file and exact command.

Three possible outcomes are acceptable:

- **Descriptive recovery:** reliable trajectory, mechanisms unresolved. Use the chart and say what is unknown.
- **Robust association:** verified fields and stable descriptive relationships. Use “associated with” or carefully bounded “consistent with”; retain rival explanations.
- **Mechanism discrimination:** only if independent evidence actually separates alternatives. The team must document the identifying assumptions before strengthening language.

**Stop conditions:** no verified variable meaning, no usable discriminating data, or the pre-freeze time budget is exhausted. No paid data, deposits, outreach, new independent-event study, or wallet reconstruction is included. A separate episode may be future work; it is not necessary to complete this proposal.

**Why this helps:** it tests whether recovery supplies new economic understanding beyond the spike, while preventing another correlated series from being presented as an explanation.

## 5. Workstream C — Test the PDF's argument

### Prepare a controlled alternative

Archive the current ten-slide PDF or render it from the current deck and record its commit. Produce a text storyboard first. Keep the evidence and numerical claims identical in the initial comparison, so a clearer presentation is not confused with adding stronger-looking results. Add recovery evidence only after workstream B's gate.

Proposed ten-slide allocation, subject to the deck owner's review:

| Slide | Question answered |
|---|---|
| 1 | Why does local dollar access through stablecoins matter, and what is our question? |
| 2 | What intermediation mechanism could generate a premium? |
| 3 | What is measured, against which benchmark, and how was the episode discovered? |
| 4 | How large and broad was the acute increase? |
| 5 | Which alternatives and overlapping institutional events limit attribution? |
| 6 | How did the premium evolve afterward? |
| 7 | What does validated recovery evidence establish, and what remains unresolved? |
| 8 | What does the magnitude mean for a transparent transaction-size illustration? |
| 9 | What did we learn from 2025, and how do the baseline and robustness checks constrain today's claims? |
| 10 | What is the contribution, practical implication, and main limitation? |

Keep source citations and essential caveats beside the claim. Detailed specifications go to the annex. Gross-turnover premium calculations must not be labelled consumer loss, welfare loss or causal regulatory cost. The required “Lições de 2025” content is retained. Moving the depeg chapter, monitor, or agent extension to the annex requires explicit team agreement; this proposal does not silently remove adopted material.

### Reader test and scoring

Recruit four unfamiliar readers if available; two is the minimum for a diagnostic review. Prefer at least one with economics/finance familiarity. Recruitment/outreach is for the team; no messages are authorized by this document.

Give readers the PDF without a presentation. Before showing either version, freeze the questions and scoring key:

1. What economic problem is being studied?
2. What does the project add beyond the reported event?
3. What is the main finding and its time horizon?
4. What does the evidence fail to identify?
5. What practical implication follows, and under what assumptions?

Score each answer 0 (wrong/missing), 1 (partly correct), or 2 (correct with necessary qualification). Also ask readers to flag any sentence implying a proven regulatory cause, identified importer, measured welfare loss, or established permanent effect.

Where feasible, split first exposure evenly between current and proposed PDFs. A later crossover can collect preferences but is contaminated by learning; report first-exposure answers separately. With this small sample, report individual answers and scores, not statistical significance or a population estimate of jury preference.

Proposed practical acceptance rule: at least three of four readers score at least 8/10 on the candidate, and none leaves with a central unsupported causal claim. With only two readers, require both to meet that rule and label confidence limited. These are team-chosen quality targets, not validated scientific thresholds. If both versions pass equally well, prefer the smaller revision. If the candidate creates misunderstandings, revise once and retest with a new reader where possible; otherwise retain the clearer current version.

### Deliverables and adoption gate

Deliver a storyboard, candidate PDF, source/claim checklist, anonymized reader responses and scores, and a slide-by-slide change recommendation. Felipe and the team approve integration. Reader preference cannot override factual accuracy or the ten-slide constraint.

**Why this helps:** it tests whether the PDF communicates the contribution without a presenter, rather than assuming a more attractive narrative is better.

## 6. People, effort, dependencies and schedule

Assignments below are suggestions, not claims on anyone's tasks. Owners must accept them and respect existing workloads. Research estimates are planning caps, not measured execution times.

| Work package | Suggested lead / reviewer | Cap | Dependency |
|---|---|---|---|
| A: contribution and discovery audit | Felipe + Renzo / independent teammate | 3 person-hours | Existing sources and findings |
| B1–B3: measurement and reproduction/sensitivity | Jonathan or Nattan, whichever did not author the tested work / other available reviewer | 6 person-hours | Verified inputs; coordinate P3-17/P3-19 reviews |
| B4: recovery exhibit and explanation matrix | Renzo / Felipe | 3 person-hours | Measurement gate |
| C: storyboard and PDF candidate | Felipe + Renzo / teammate | 3 person-hours | A; B determines strength of recovery slide |
| C: reader checks and final recommendation | Available teammate / Felipe | 2 person-hours, excluding reader availability | Candidate PDF |

**Total cap: 17 person-hours**, with no new spending. If the team cannot allocate this, prioritize A, measurement/interpretation review, and a text storyboard; omit extra B sensitivity checks and use descriptive recovery language.

- **3 Nov:** approve scope/owners; complete A and B measurement/reproduction review; draft storyboard in parallel only where it does not depend on pending evidence.
- **By the existing 4 Nov freeze:** finish or stop B, record all null/failed/unavailable checks, and decide which claims can enter the deck. No moving the freeze implicitly.
- **5 Nov:** candidate PDF using frozen evidence.
- **6 Nov:** reader check within the existing red-team work; integrate approved presentation changes.
- **7–8 Nov:** preserve script export and submission checks. If approval arrives late, reduce scope rather than displace them.

Use existing P3-17/P3-19 review, P4-02/P4-03 validation/freeze, and P5-01/P5-03 deck/red-team tasks where their owners agree. Create separate task files with the next available IDs only for genuinely new approved work. Do not reassign another person's subtasks. Prospective outputs receive task-prefixed names when tasks are allocated.

## 7. Second view: an alternative backbone, compared with §§1–6

**Added 2 Nov 2026 by a second agent for Renzo, at Renzo's request, after reading §§1–6 and the
[improvements log](improvements_log.md).** Status: proposed, not approved. §§1–6 are unchanged. This section answers the
same two concerns differently and compares the two answers, so the team can choose at one gate. No deck file or finding
changed. The only checks run are the ones named below, each with its command or source.

### 7.1 The two concerns, judged directly

| Concern (Renzo) | Verdict | Why |
|---|---|---|
| "It looks like we found the anomaly and ran tests to confirm it" | True as history | The 30 Oct probe showed the jump before the hypotheses were written (`docs/02-dolar-cripto.md` §3); slide 3 discloses it. This cannot be argued away. What can change is the jump's role in the story: from premise to result |
| "It reads as a data-analysis routine" | Partly true, mostly a deck problem | The design is causal within its limits: a date from outside sources, a break test that never saw the date (F-011), 1,073 placebo dates (F-016), a synthetic control (F-017). But 4 of the 10 slides (4, 5, 6, 8) argue "is it real", the hypotheses on slide 3 read as a checklist, and no economic claim that the data could have refuted is stated up front |

Two facts already in the repo turn the jump from premise into result:

- **It was news before we saw it.** Cointelegraph Brasil (24 Jun) reported the spread going "de cerca de 0,1 acima do
  mercado para 0,7 após a notificação e chegou a ficar acima de 1% e até 2% ao longo do dia" (E-05.6). Exame (25 Jun)
  reported that the notice made crypto up to 2% dearer (E-05.2).
- **We tested every dated rule the same way, and only one moved** (F-026). Those null results are the best answer to
  "you built the question backward from one date".

### 7.2 The alternative question and its motivation

> **O que move o preço do dólar digital no Brasil?** On slide 1: "Entre as regras de 2025–2026, quais moveram o preço do
> dólar digital?"

This question exists without June 2026. Its motivation, with each fact's level:

| Fact | Source | Level |
|---|---|---|
| May 2025: IOF on ordinary FX purchases rose to 3.5%; Congress and the STF suspended it, then it was reinstated | E-01, E-01b | Sourced |
| Feb 2026: the government proposed IOF on crypto and stablecoin purchases (never enacted) | E-03 | Sourced |
| The rationale, as a Forbes Brasil column describes it: "Se a compra de dólar paga IOF, a conversão de reais para stablecoins também deveria pagar. Do ponto de vista fiscal, a lógica é simples: evitar arbitragem tributária e ampliar arrecadação." The same column: "Segundo dados da Receita Federal, brasileiros declararam cerca de R$ 388 bilhões em criptoativos nos três primeiros trimestres de 2025. Mais de 70% desse valor estava em stablecoins." | URL already listed under E-03. Re-opened 2 Nov 2026 by Renzo's agent (curl; `datePublished` 2026-02-12; author field "Redação", not confirmed). A column describing the government's view, not the government's text. **The quotes are not yet in `sources.md`** | Context only |
| Residents' net acquisitions of cryptoassets abroad (BCB SGS 29644, mostly stablecoins): US$ 2,428 mn a month, Jan–May 2026 | D-16, F-024 | Measured: the route is large |

**Correction to what this agent told Renzo in chat on 2 Nov.** It said net acquisitions "roughly doubled after the May
2025 IOF rise" (US$ 952 mn → 2,428 mn a month). The arithmetic is right, but the comparison is misleading:

- **The starting point was a dip.** Jan–May 2025 (952) was below both halves of 2024 (1,134 and 1,255). Aug–Dec 2025 is
  +49% over Aug–Dec 2024.
- **The premium was already falling before the IOF change:** 59.2 bps (Jan–May 2024), 41.6 (Aug–Dec 2024), 32.5 (Jan–May
  2025), 10.8 (Aug–Dec 2025), 6.8 (Jan–May 2026).
- **Three other changes hit the same weeks:** the Binance tick cut (27 Jun 2025; M-03, F-007), the STF injunction (4 Jul
  2025; E-01b) and the July 2025 break (−25.6 bps; F-011).

The 2025 numbers therefore show size and a long trend. They do **not** show substitution caused by the IOF. Use them as
motivation only.

Command (reads the frozen P3-10 table; no download), with its output:

```
.venv/bin/python -c "import pandas as pd; d=pd.read_csv('data/processed/P3-10_imports_monthly.csv',parse_dates=['month']).set_index('month'); [print(a,b,round(d.loc[a:b].imports_usd_mn.mean()),round(d.loc[a:b].premium_mean_bps.mean(),1)) for a,b in [('2024-01','2024-05'),('2024-08','2024-12'),('2025-01','2025-05'),('2025-08','2025-12'),('2026-01','2026-05')]]"
```

| Months | Net acquisitions, US$ mn/month | Premium, bps |
|---|---|---|
| Jan–May 2024 | 1,134 | 59.2 |
| Aug–Dec 2024 | 1,255 | 41.6 |
| Jan–May 2025 | 952 | 32.5 |
| Aug–Dec 2025 | 1,866 | 10.8 |
| Jan–May 2026 | 2,428 | 6.8 |

If the team adopts §7, these numbers go into a descriptive finding before any slide uses them.

### 7.3 The answer: one idea, five predictions, scored

The idea: **the premium is set by the cheapest channel that is still open, not by the headline tax.** The principle is
not new (limits to arbitrage; L-11 studies stablecoin–fiat parity gaps across countries). What is ours is a contrast
inside one market, measured with one test, 13 months apart:

- a 240 bps IOF rise on the bank route (May 2025) moved the premium +13.2 bps, inside the range of ordinary dates
  (p = 0.38; F-026);
- a confidential notice that closed the funds' 0% route (Jun 2026) moved it +93.9 bps, beyond every ordinary date, while
  net acquisitions fell 78% (F-016, F-024).

| # | Prediction | Evidence | Result | Level |
|---|---|---|---|---|
| 1 | A tax on a route that is not the cheapest does not move the price | IOF decree +13.2 bps (p = 0.38); its suspension −23.9 (p = 0.16) (F-026) | Holds. The test only rules out moves beyond about ±35 bps | Measured (null) |
| 2 | Closing the cheapest route raises the price and lowers the quantity | +93.9 bps (F-016); net acquisitions −78% in July (F-024) | Holds | Measured. The quantity is one monthly observation, and Res. 580 falls in the same month |
| 3 | Rules that leave the current supply channel open do not move it (licensing, reporting, eFX, an unenacted proposal, a hold starting in 2027) | Five other published rules: −22.0 to +7.2 bps (F-026) | Holds, except Res. 574: +37.7 bps on 18→19 Jun, not tested (F-029, P3-16) | Measured (nulls) |
| 4 | The rise is capped by the next route's cost | Highest day +170.7 bps over the pre-notice level; never near 350 (F-028) | Not testable: the next route is not identified | Not shown |
| 5 | If supply finds another way, the price returns while the closed channel stays shut | Fade from 22 Jul (F-011); acquisitions at 32% of the Jan–May level in Aug–Sep (F-024); no reopening found (F-030); Foxbit seller-initiated trading rose with the premium (F-031, F-032) | Consistent; rerouting and lower demand not separated | Consistent with; F-030 to F-032 exploratory |

The same results answer concern 1 once they score an idea instead of being listed as checks.

**Creative angle (true as stated):** the notice was not published in the DOU (E-05). The premium moved the next PTAX
day, the press reported it on 24–25 Jun, and the real-time monitor flagged it the same day (F-014). The market priced an
unpublished rule. Wording: "não publicada", not "que ninguém leu"; 13 banks received it (E-05.2).

### 7.4 Where §7 agrees with §§1–6

- Tell the discovery history honestly (§3, A.2).
- Narrow the novelty claim. Prior knowledge includes L-11, M-06 and E-05 (§3, A.1). Under §7 the claim is the
  within-market contrast, not the principle.
- Build a claim-to-evidence table with the four language levels (§3, A.3). Either backbone needs it.
- F-031 measures who initiated trades, not supply, deposits or imports (§4, B2; log correction). §7 uses it only as
  "consistent with".
- R$ 106 mn is a transfer computed on gross turnover, not a welfare loss (slide 9 already says so).
- Test the PDF on readers without a presenter (§5). It is the only direct check of concern 2.
- Approving an investigation is not adopting its result; the 4 Nov freeze stays binding.

### 7.5 Where they differ, and which this agent would pick

| Topic | §§1–6 | §7 | Recommendation and reason |
|---|---|---|---|
| Central question | Size, duration and adjustment of the June episode (§3) | Which rules move the price | **§7.** The §3 question starts from the episode, so it does not answer "how did you find this?". It also puts the weakest evidence at the centre: every recovery finding (F-030, F-031, F-032) is exploratory, and §4 lists "descriptive recovery, mechanisms unresolved" as an acceptable outcome. The §7 question rests on confirmed findings (F-016, F-024, F-026) |
| Recovery | Two slides (§5, slides 6–7) and up to 9 person-hours (B1–B4) | One slide: prediction 5, "consistent with; not separated" | **§7 before the freeze.** B2 (independent review of P3-17/P3-19) is owed anyway. B1 only for the Foxbit fields, and only if F-031/F-032 reach a slide. B3 sensitivity checks on exploratory results: after the freeze, or not at all |
| Rules comparison (F-026) and dated 2027 prediction (F-027) | Not named in the §5 slide plan; the log says the prediction "can be assessed" | Central: slides 4 and 10 | **Keep both.** F-026 is the systematic evaluation that answers concern 2. F-027 is the deck's only forward-looking claim that can be proved wrong |
| "Lições de 2025" | Slide 9 | Strip on the method slide | **Method slide.** Decision log, 2 Nov (Renzo): "not a standalone slide", "the method slide as a short strip". §5's slide 9 conflicts with that decision |
| Title | *Um choque no dólar digital: prêmio e ajuste de liquidez no Brasil* (log) | *O que move o preço do dólar digital no Brasil?*, with a subtitle that gives the answer | **§7.** "Choque" asserts the cause. "Ajuste de liquidez" promises a mechanism we do not identify |
| Reader test | Two PDFs, 2–4 readers, 5 questions, split first exposure | Same, plus one question | **Add Q6:** "Por que os autores estudaram isso, e como encontraram o episódio?" It tests concern 2 directly. If readers are scarce, test only the candidate |
| Effort | 17 person-hours | About 11 (§7.7) | **§7.** The freeze is Wed 4 Nov, and P5-02, P5-04 and rehearsals still need people |

### 7.6 Weak points of §7

1. **Prediction 1 is one null result.** The test only rules out moves beyond about ±35 bps, so the slide must say "não
   moveu de forma detectável".
2. **The argument is partly circular.** We call the funds' route the cheapest partly because closing it moved the price.
   Independent support:
   - its 0% IOF (Decreto 6.306, art. 15-B, III);
   - ABToken's description of the channel (E-05.2);
   - the quantity fall (F-024).

   The wording stays "compatível com"; F-028 does not identify the marginal route.
3. **The question promises generality.** "O que move o preço" draws on one market and one shock that moved it, so the
   answer on slide 1 must say "entre as oito regras testadas, 2025–2026".
4. **Legal tone.** "0% contra 3,5%" next to "substituto" can read as tax avoidance. Use the BCB's own words and
   "diferença de alíquota", never "brecha".
5. **What no framing fixes:**
   - one shock;
   - the letter's form vs its content;
   - the cause of the fade;
   - the marginal route;
   - the letter's full text, which is not public.

### 7.7 Combined plan, if the team agrees

| Step | What | Cap (planning, not measured) | Suggested lead (must accept) |
|---|---|---|---|
| 1 | Gate: choose the backbone (§3 or §7); approve the reduced scope | 0.5 h | Team |
| 2 | A.1–A.3 as written in §3, against the chosen question | 3 h | Felipe + Renzo |
| 3 | Register the Forbes quotes under E-03 in `sources.md`; descriptive finding for the 2024–26 table in §7.2 | 1 h | Renzo |
| 4 | B2 independent review of P3-17/P3-19 (already owed); B1 Foxbit fields only if F-031/F-032 go on a slide | 2–3 h | Jonathan or Nattan |
| 5 | Text storyboard and candidate deck, with the same numbers as now | 3 h | Felipe + Renzo |
| 6 | Reader check with six questions | 1.5 h plus reader time | A teammate |

About 11 person-hours in total. B3, B4 and a second episode come after the freeze, or not at all.

Storyboard under §7 (10 slides, nothing dropped, only reordered):

| Slide | Content | Evidence |
|---|---|---|
| 1 | The question; the contrast as the answer (IOF +13 bps vs notice +94 bps) | F-026, F-016 |
| 2 | Why it matters: the route is large (US$ 2.4 bn a month) and the government's own argument; how reais, dollars and USDT connect | D-16, E-03, E-05 |
| 3 | The idea and its five predictions; data and method strip; probe disclosure; "Lições de 2025" strip | §7.3; F-005 |
| 4 | Predictions 1 and 3: the eight rules | F-026, F-029 (Res. 574) |
| 5 | Prediction 2, price: the jump (break test, three exchanges); "not the real, not USDT, not other countries" in one line | F-011, F-009, F-017 |
| 6 | Prediction 2, quantity: net acquisitions | F-024 |
| 7 | Cost: R$ 106 mn transfer, tariff equivalent 95 bps | F-025, F-015 |
| 8 | Prediction 4: why +94 and not +350 | F-028 |
| 9 | Prediction 5: the return, the robustness range, what we do not show | F-022, F-030–F-032 |
| 10 | Scorecard, implications, dated 2027 prediction, limits | F-027 |

Whether either backbone wins is unknown. The regulation scores quality, relevance and creativity (Art. 8, item 19); no
source says how this jury weighs them.

## 8. Team approval record

The team may approve each workstream independently. Leave blank until a decision is actually made.

| Decision | Approve / revise / decline | Owner accepted | Reviewer | Date / rationale |
|---|---|---|---|---|
| Backbone: §3 question (episode and adjustment) or §7 question (which rules move the price) | Pending | — | — | — |
| A: contribution audit and candidate question | Pending | — | — | — |
| B: bounded recovery review and checks | Pending | — | — | — |
| C: candidate PDF and reader test | Pending | — | — | — |
| Effort cap and protection of freeze/submission schedule | Pending | — | — | — |
| Moving existing chapters/extensions to annex, if needed | Pending | — | — | — |

Approval authorizes investigation only. At completion, record a separate **adopt / narrow / reject** verdict for each proposed change, links to evidence, dissent or unresolved limitations, and the final wording approved by the team. Update the decision log and task handoffs then. Until that gate, the current project and deck remain the baseline.
