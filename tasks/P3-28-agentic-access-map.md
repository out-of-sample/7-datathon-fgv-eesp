---
id: P3-28
title: Build and evaluate a source-backed agentic map of digital-dollar access
phase: P3
status: paused
owner: Team
working: -
due: 2026-11-07
depends: P3-27
---

## Goal
Build a dated, source-backed map of the conditions under which a specified user can access a digital-dollar route, and test whether an agentic investigation improves evidence coverage over simpler workflows. Connect the project's measured acquisition-cost episode to a separately evaluated tool for investigating access conditions.

**Planning status:** formalized at Renzo's request on 6 Nov 2026; no implementation or experiment has started. `owner: Team` means assignment is pending, not that every member is working on it. The due date is the **feasibility/readiness checkpoint**, not a promise of a complete study before submission. Suggested roles: CS implementation owner, economist for the coding rubric, and a different teammate for the final review. Follow `prompt.md` §7 when claiming work.

## Questions and hypotheses

**Primary research question:** With the same source corpus, model and resource ceiling, does an agent that iteratively retrieves and checks evidence answer more access-condition questions correctly than a fixed retrieval-and-answer workflow, without making unsupported availability claims?

| ID | Question / hypothesis | Evidence needed | What would weaken or reject it |
|---|---|---|---|
| H1 — primary | Iterative investigation increases supported answer coverage on previously unseen cases. | A frozen human-adjudicated reference set, paired baseline/agent outputs and evidence-linked scoring. | No material coverage gain; gain disappears under equal budgets; or the workflow fails the availability-error guardrail. |
| H2 — secondary | The workflow reduces unsupported availability assertions, especially with missing or conflicting information. | Cases containing missing dates, eligibility conditions, service restrictions and genuine source conflicts. | It turns missing evidence into availability, resolves contradictions without grounds, or merely abstains on every case. |
| Q3 — descriptive | Which required conditions are publicly documented, and which remain unknown, for the sampled routes? | A route/condition inventory with an explicit search perimeter. | The public corpus cannot establish the condition; preserve unknown rather than completing the map by inference. |
| Q4 — exploratory | Do nominally different routes share documented operational dependencies? | Explicit evidence linking providers to issuers, networks, bridges or other infrastructure. | Shared dependencies cannot be verified. Co-moving prices alone do not identify a common bank or supplier. |

H1 concerns tool performance. Q3/Q4 concern the sampled infrastructure. Neither estimates the causal effect of a rule, predicts prices, identifies the marginal supplier, or establishes that a payment would succeed.

## Connection to the current project

- F-009/F-016: the local premium rose across the observed venues. The map must distinguish an observed price from the conditions for acquiring and withdrawing the asset.
- F-018 and exploratory F-037: the observed BTC pair and BRLA/USDC pool also reflected the episode. A new token or interface is not evidence of an independent or cheaper access channel.
- F-028/F-030: route availability and reopening remain unresolved. These are **known development cases**, not held-out discoveries or a basis for declaring that all alternative routes were closed.
- F-024 and exploratory F-036: price normalization coexists with different recorded net acquisitions and venue composition. This motivates investigating access, without identifying the cause of those changes.
- F-014 can supply a dated question for investigation. It detects an observed condition; it is not a forecast, and its mandatory alarm pause must remain visible.

**Incremental contribution required:** a new, reproducible conditions dataset plus measured performance on held-out questions. Reformatting `P3-15_routes.md`, summarizing the existing findings, or adding a chat interface is insufficient.

## Deliverable and scope

The minimum product is a script that accepts a case definition and returns (1) a structured evidence table, (2) a route/dependency graph generated from that table, and (3) a concise explanation of documented conditions, restrictions and unknowns. A Markdown/CSV output and a static figure are sufficient for the PDF; a website is optional future work.

**Unit of analysis:** one route × user profile × operation × requested date. Start with a Brazilian legal entity seeking to acquire a specified token and withdraw it to its own wallet. Account eligibility, completed onboarding and source of funds are explicit scenario assumptions unless independently documented; an assumed condition is never scored as a verified fact. A later profile can cover an individual or an issuer redemption operation.

**Initial scope:** Brazil, USDT/USDC access through the three existing exchange candidates and the BRLA-to-USDC candidate. These are candidate routes, not assertions of usable end-to-end access. Split the route into its actual legs: BRL funding, acquisition, withdrawal/network transfer and destination receipt. Add issuer redemption only when it is part of the defined operation. Fix amount and network for every case, or mark them `unspecified` and prevent claims about capacity at a particular size.

**Time modes:**

1. **Retrospective investigation:** documents available now may explain a historical question, but each claim distinguishes publication time, asserted effective time and retrieval time. This does not simulate knowledge available in June.
2. **As-of investigation:** only source versions demonstrably published by the case cutoff enter the corpus. Missing archives produce `historical_evidence_unavailable`. Model memory is not admissible evidence, and access controls do not prove the model has never seen the event.

Use retrospective mode for the initial study. An as-of claim requires its own validated source-version audit.

## Evidence schema and decision rules

Freeze these fields before evaluation:

| Record | Required fields |
|---|---|
| Case | `case_id`, `route_id`, `profile_id`, `operation`, origin/destination asset, chain, amount/unit, `as_of_utc`, mode, scenario assumptions, split/group IDs |
| Source | `source_id`, exact URL, publisher, document/version family, publication/effective dates or explicit unknown, retrieval UTC, immutable raw-file path, SHA-256, section/page locator |
| Condition | `case_id`, leg, actor, predicate, value/unit, exceptions, evidence state, source IDs and short supporting passage, validity interval, assumptions, contradiction IDs |
| Dependency | route/leg, dependency type, named entity or chain/contract identifier, source IDs, validity interval, evidence state |
| Run | method, exact model/version, prompt/config hash, corpus hash, tools called, stop reason, token/tool counts where available, wall time, human interventions, output hash |

Condition states are `supported`, `restricted`, `conditional`, `conflicting`, and `unknown`. Use them for the **particular predicate**, such as documented withdrawal support on a given network. Separate fields identify whether the evidence is an official rule, provider statement, third-party report, measured quote or observed execution. Do not promote provider advertising to an execution observation or a legal determination.

Deterministic aggregation rules:

- A verified restriction on a required leg flags that leg as restricted for the specified profile/date; describe the source's scope.
- Missing evidence on a required leg prevents an end-to-end positive availability statement. Failed retrieval is a technical failure, not evidence of a restriction.
- A conditional source remains conditional until the relevant condition is established; an assumption stays visibly separate.
- Conflicting sources remain conflicting unless dated supersession or a documented scope difference resolves them. Do not use majority voting among repeated articles.
- A fully documented set of conditions is labelled **documented conditions satisfied under the stated assumptions**. It is still not proof of account access, current liquidity or payment execution.
- Missing fee/limit fields are null, never zero. A current document cannot fill a historical gap without evidence that its terms applied then.
- Shared issuer/network/dependency edges require sources. Report observed shared-dependency counts, not nationwide concentration or predicted losses from an outage.

The graph and route status are generated by code from accepted records. The LLM cannot directly overwrite them.

## Data and reference set

**Existing inputs, read-only:** `results/tables/P3-15_routes.md`, `results/tables/P3-17_candidates.md`, `data/processed/P1-04_events_brazil.csv`, relevant F-028/F-030/F-037 passages, and the source register. Existing findings are context for the human designer; they are not gold answers shown to an evaluated agent.

**Sources to collect after the task is claimed:** original provider terms/help pages/status notices, issuer documentation and applicable official texts. Start from already opened source-register URLs; verify any new exact URL and register it. Secondary reporting can identify leads or confidential-document excerpts, with provenance preserved. It cannot silently stand in for an unavailable primary source.

Freeze a local corpus under `data/raw/p3_28/`. Keep raw pages, source passages, raw model traces and reference annotations out of git. Commit manifests/checksums and permitted derived summaries; follow the latest data policy in `docs/README.md`. Respect access limits; do not assume a paid data service or account is available.

**Reference construction:** two human readers independently code the required fields and evidence state, then adjudicate disagreements with the economist's input on scope. Record original disagreements. The reference is what the frozen documents support, not a certification of real operational access. An LLM judge cannot be the sole reference. If two readers are unavailable, label the exercise a single-annotator pilot and do not make the full H1 claim.

**Planned evaluation size:** target 12 development cases and at least 24 held-out cases across at least four document/provider families. These are design targets, not a power calculation. The exact manifest, counts and any smaller pilot must be committed before final runs. A smaller study reports case results and limitations, not a broad reliability claim.

Group amendments and near-duplicate documents together; never randomly split paragraphs. Keep at least two provider/document families entirely out of development where the source inventory permits. Shared background legislation is flagged as shared context, not counted as independent evidence. Select cases from the source inventory before model outputs: ordinary access conditions, conditional access, explicit restrictions, unresolved contradictions and missing evidence. Do not manufacture real-world restrictions to balance classes; any constructed stress cases get separate synthetic labels and scores.

## Methods, metrics and reading rule

**Primary evaluation uses a closed, frozen corpus.** This makes information access comparable and citations reproducible. A later live-web demonstration is reported separately, because changing pages and search results introduce another treatment.

| Method | Procedure | Purpose |
|---|---|---|
| B0 | Deterministic keyword/date retrieval and conservative extraction rules; unknown when no rule applies. | Simple non-LLM baseline. |
| B1 | One retrieval pass followed by one structured LLM response. | Main baseline for H1. |
| B2 | Fixed retrieve → extract → verify workflow with no adaptive choice of next query. | Distinguish agentic iteration from extra verification/compute. |
| A | One tool-using agent selects subsequent searches or document reads, checks missing/conflicting conditions and returns structured records. | Proposed method. |

All automated methods see the same case and permitted sources. B1/B2/A use the same actual model/version and the same maximum context/output, tool-call and elapsed-time budgets, fixed after development. Log actual consumption; a ceiling is not evidence of equal cost. No need for multiple agents or model-family voting. A uses read-only retrieval and schema/checking tools; retrieved text is data, not instructions. Evaluate one fixed configuration on every case, with three scheduled repeats for B1/B2/A if quotas permit; never select the best run. If repeats are reduced, freeze that change before final runs.

**Primary metric: supported answer coverage (SAC).** For each case, divide the number of answerable reference fields correctly answered **with valid supporting evidence** by the number of answerable reference fields. Macro-average across cases, then across scheduled repeats. A wrong value/date/profile, unsupported citation, or unresolved contradiction presented as settled receives no credit. Score fields atomically so a long answer cannot earn extra points. Cases with no answerable fields are excluded from SAC with their count shown, and remain in the unknown/error evaluation.

**Mandatory guardrail:** count every unsupported positive claim that a required leg or end-to-end route is available. The prototype passes this guardrail only with **zero observed instances** in the locked benchmark, including free-text output. This is a finite-sample result, not an estimated zero deployment risk. Unsupported extra claims also enter a separate claim-error denominator.

Secondary measures: correctness of unknown/conflicting states; field-level precision/recall; source/date accuracy; end-to-end state accuracy; human correction minutes; latency and actual model/tool usage. Report all-unknown frequency so abstention cannot masquerade as successful coverage. Human review time is measured with outputs anonymized and assignment counterbalanced to limit familiarity effects.

**Predeclared prototype reading rule:** H1 receives preliminary support if A improves SAC by at least **10 percentage points over B1**, passes the guardrail, and the result is not explained solely by a larger resource budget. Ten points is a project decision threshold, not a literature standard. B2 is mandatory: if A fails to improve on B2 at comparable quality/cost, conclude that verification helps but agentic adaptation is not established. Report paired differences and per-family results; with few source families, uncertainty remains descriptive. Repeats and multiple fields are not independent economic events. Negative or mixed outcomes complete the study when properly reported.

## Procedure and checkpoints

1. **S1 — Feasibility and case contract.** Name implementer/reviewers; inventory sources and legal/operational ambiguities; freeze one profile, operation, date mode and schema. Retrieve one source-backed development case end to end before building a larger pipeline. Output: feasibility note, one evidence card and the candidate source/case inventory. Stop expansion if source versions or reviewer capacity cannot support evaluation.
2. **S2 — Corpus and human reference.** Snapshot sources, hash them, create the grouped split and independently adjudicated labels. Ensure development cases include F-028/F-030 examples; keep evaluation labels inaccessible to the implementer/agent until scoring. Output: source manifest, reference manifest/hash and coding rubric. **Checkpoint G1:** two readers can apply the rubric and critical unknowns remain explicit.
3. **S3 — Baselines and agent pilot.** Implement B0/B1/B2/A on development cases only, with deterministic route aggregation. Exercise missing source, wrong date, contradictory statement, missing fee and irrelevant/instruction-like document text. Choose and freeze model/configuration, budgets and case list. Output: development results plus a committed `P3-28_protocol.md`. No test-set tuning.
4. **S4 — Locked evaluation.** Run every scheduled case/method/repeat, including failures/timeouts. A timeout is a failed run with zero answered fields and remains in the denominator. Preserve transcripts; identify infrastructure-wide outages separately without silently rerunning poor answers. Any correction after opening test scores creates a new version and a fresh test set for a new claim. Output: paired scores, errors and cost table. **Checkpoint G2:** reference and output audit by a teammate who did not build the workflow.
5. **S5 — Research application and integration.** Apply the frozen workflow to the declared route inventory. Produce a dated graph, evidence cards and an unknowns table. Present Q3/Q4 as sample descriptions, separately from H1 results. P3-29 may supply verified contract/flow records through the interface below; its absence must not block this task. Output: one result figure and a proposed deck/annex paragraph, with evidence labels.
6. **S6 — Reproduction and handoff.** Re-score saved outputs offline, verify corpus/prompt hashes and denominators, and have an independent teammate reproduce the tables and inspect every positive route claim. Write a new finding using the next free ID. Update source/data registers, task Handoff and board. Live model regeneration is documented as potentially nondeterministic; scoring and graph construction must reproduce.

Each step is a separate work session; split further if it exceeds one focused session. Do not build all infrastructure before the first evidence card. Use G1/G2 as checks of the listed criteria, not as invented external permission requirements.

## Subtasks
- [x] S1 — Confirm case contract, source access and reviewers; complete one development evidence card. — done: Renzo's agent, 7 Nov (scope: S1 only; second coder Felipe; G2 auditor not named)
- [ ] S2 — Freeze the corpus, grouped case split and independently adjudicated reference; pass G1. — agent part done 7 Nov (corpus v1: 31 sources; 17 cases, 229 field rows; rubric; blank sheets). Pending: Renzo's manual saves of Binance/MB (A-25–A-41) → corpus v2; coding by **Felipe and Jonathan**; adjudication
- [x] S3 — Build and pilot B0/B1/B2/A; commit the final protocol before held-out runs. — done: Renzo's agent, 7 Nov (protocol v1 `c63aa70`; v1.1 scoring fixes `08939b9` after review P3-36; F-047)
- [ ] S4 — Complete the locked evaluation and independent claim/error audit; pass G2. — Avenia runs done (40, hashed before any label); Binance/MB runs wait for corpus v2; blinded audit by **Nattan**
- [ ] S5 — Produce the dated access map and a measured integration proposal for the project.
- [ ] S6 — Independently reproduce outputs, write the finding and finish the handoff.

## Success criteria
- [ ] Profile, operation, date mode, source hierarchy, evidence states and deterministic aggregation rules are frozen.
- [x] A working evidence card separates observed prices, documented conditions, assumptions and unknowns. (D-01, `results/tables/P3-28_access_cards.md`, 7 Nov)
- [ ] Reference labels, grouped split, model/configuration and resource limits predate held-out runs; departures are disclosed.
- [ ] All four methods and all scheduled runs are reported with SAC, unsupported-availability counts, unknown handling and costs.
- [ ] The conclusion follows the H1 reading rule and B2 comparison; failure or inconclusive performance is permitted.
- [ ] New conditions/dependency evidence is distinguished from existing results; no unsupported execution, causal or savings claims appear.
- [ ] An independent teammate reproduces scores/graph and checks evidence before any main-deck use.

## Outputs

Planned files; **none is implemented by this task specification**:

- `scripts/p3_28_access_map.py` — case loading, local evidence tools, method adapters, deterministic map generation and scoring; header documents inputs, units and commands.
- `results/P3-28_protocol.md` — frozen rubric, case selection, split, prompts/configuration, budgets, thresholds and amendment history.
- `data/raw/p3_28/` — immutable source snapshots, restricted reference labels and raw run transcripts; hashes and retrieval manifest.
- `data/processed/P3-28_conditions.csv`, `P3-28_dependencies.csv` — derived records; fields defined above.
- `results/tables/P3-28_case_scores.csv`, `P3-28_errors.csv`, `P3-28_costs.csv`, `P3-28_access_cards.md`.
- `results/figures/P3-28_access_map.png`, `P3-28_evaluation.png` — graph and paired performance/coverage figure.
- New `findings/F-NNN-agentic-access-map.md` using the next free ID; proposed integration text in the finding, not an automatic deck edit.

Proposed command interface, to implement in S3: `.venv/bin/python scripts/p3_28_access_map.py {pilot,evaluate,report,reproduce} --protocol results/P3-28_protocol.md`. `reproduce` must use frozen data/outputs and make no network/model calls. Record actual final commands in the finding; do not claim these commands work before implementation.

## Integration and claim limits

**Narrative:** measured acquisition-cost episode → breadth across observed venues → unresolved access conditions after price normalization → evaluated evidence-gathering tool. Proposed English conclusion: “The study measures the local premium; the access map shows which route conditions the available evidence can establish, and which require further verification.”

P3-29 supplies records keyed by token/chain/contract and time, with source/block references, evidence state and caveats. Import only reviewed records; a balanced supply ledger does not prove redemption access. Neither task depends on the other being completed. Avoid counting one supporting document or transaction several times as independent evidence.

For the ten-slide PDF, propose at most one combined solution/evaluation slide, with detailed cases in the annex, only after S6 review and the deck owner's integration. Preserve frozen findings and the exploratory labels of F-036/F-037. A June walkthrough alone is a demonstration. If no held-out benefit is established, retain the conditions dataset as a descriptive contribution and state that agentic superiority was not shown.

**Expansion after a successful pilot:** additional providers, individual-user profiles, issuers and countries using the same schema and separately validated local source rules. This task does not forecast FX, automate transactions, provide a legal-access certification or claim that a substitute route would have avoided June's premium.

## Risks, fallback and open questions

- Missing archives: use retrospective mode and label historical gaps; do not fabricate as-of knowledge.
- Too few independent source families: report a pilot with counts; do not inflate sample size with near-duplicate pages.
- Unsupported availability or no advantage over B2: preserve the failure result; prefer the simpler workflow for any product recommendation.
- Usage limits: use existing authorized plans where practical, log actual models, and stop at the fixed budget. Paid services require the existing project authorization process.
- No mature benchmark by 8 Nov: the PDF may include only a clearly labelled prototype or omit the extension; later results cannot be represented as part of the submitted evidence.
- Assignment questions: who implements, who creates the hidden reference, who independently reviews, and what reduced pilot is feasible? These are recorded at S1 rather than assumed to be solved here.

## Sources and reading order

Read `prompt.md`, `STATUS.md`, P3-27 and its 6 Nov log entries, then F-028/F-030/F-037 and the existing route/candidate tables. Source-register T-02 (*AgenticFinBench*) is a precedent for claim/evidence evaluation; T-01 warns against treating model agreement as truth. T-06/R-11 provide current issuer terms only. This task's design choices and thresholds are proposed here, not results established by those sources.

## Handoff
- **State (7 Nov, 03:15 Brasília, Renzo's agent):** Renzo asked to proceed with the study (it continues; results reach
  the PDF only after review). Felipe's commit `a5a6974` had set "post-submission"; Renzo's instruction stands, and the
  conflict was reported to him. Done: corpus v1 (`results/tables/P3-28_corpus.csv`, hash `8ae612dc…`), 17 cases (5 dev,
  12 held-out in 3 families), 15+2 fields, rubric, blank sheets; methods B0/B1/B2/A and scorer
  (`scripts/p3_28_methods.py`); protocol frozen (`results/P3-28_protocol.md`, v1 + v1.1); development pilot (F-047:
  A 0.87, B2 0.85, B1 0.75, B0 0.15 provisional, implementer's labels); **held-out Avenia runs done** (40, hashes in
  `results/tables/P3-28_heldout_run_hashes.csv`).
- **Next steps, in order:**
  1. **Renzo** saves the 17 Binance/Mercado Bitcoin pages (list: `results/tables/P3-28_sources.csv`, `fetch=manual`) in
     his normal browser as `data/raw/p3_28/manual/<ID>.pdf` (Print → Save as PDF; or `<ID>.html`). For A-33, A-39 and
     A-40 he finds the page and adds `<ID>,<url>` to `data/raw/p3_28/manual/urls.csv`. Then
     `.venv/bin/python scripts/p3_28_access_map.py snapshot && .venv/bin/python scripts/p3_28_access_map.py corpus`,
     and adds one quoted line per page to `docs/sources.md` (A-25–A-41 row).
  2. **Renzo** sends the new corpus zip (`data/raw/p3_28/P3-28_corpus_<hash>.zip`) and the blank sheets
     (`data/raw/p3_28/reference/form_{felipe,jonathan}.csv`) to **Felipe** and **Jonathan**, separately. They code
     blind per `results/P3-28_rubric.md`, return them privately, and the sheets stay **outside the repo** until step 3
     is done.
  3. An agent runs the Binance/MB held-out cases: `run B0 H-05,…,H-12`; `run B1|B2|A H-05,…,H-12 --repeats 3
     --workers 2`; then appends `sha256sum data/raw/p3_28/runs/*/H-*.json` to the hash file and commits it.
  4. Sheets go into `data/raw/p3_28/reference/`; `adjudicate` (prints counts only); Felipe and Jonathan settle
     `disagreements.csv`. The adjudicated reference is hashed and committed.
  5. `score <reference> heldout` writes the blinded `audit_sheet.csv`; **Nattan** fills it; `score … --audit` gives
     the final SAC; G2 check by Nattan; S5/S6.
- **Open questions:** whether coders and auditor have time before 8 Nov (if not, the held-out result is post-submission
  and the PDF keeps only Felipe's annex card B.10); turn counting (`num_turns` 28–58 above `--max-turns 40`, protocol
  §8); B2 token under-recording in existing runs (§11).
- **How to resume:** read `results/P3-28_protocol.md` first. Never edit run files; never open filled sheets before
  step 3 is committed. Scoring without `--audit` is PROVISIONAL. Other sessions share this checkout: commit only P3-28
  files (memory note on parallel sessions).

## Log
- 2026-11-07 — agent for Renzo: S2 agent part, S3 done, S4 Avenia runs → paused for human inputs. Corpus v1 (31 sources), 17 cases, fields, rubric (two rules added in development), blank sheets for Felipe and Jonathan; methods B0/B1/B2/A; isolation test passed; protocol v1 frozen (`c63aa70`) before held-out runs, v1.1 scoring fixes after independent review P3-36 (`08939b9`); dev pilot F-047; Avenia held-out 40 runs hashed before any label. Binance/MB blocked to scripts (no headless workaround): manual saves by Renzo. Reported to Renzo: conflict with Felipe's 'post-submission' handoff.
- 2026-11-07 — agent for Renzo: Renzo asks to proceed with the study; agent takes S2 (corpus, grouped split, rubric, blank coding forms). Reference labels must come from two human readers; results enter the PDF only after S6 review.
- 2026-11-07 — Felipe (Economist): Second-coder verification of S1 / D-01 complete. All 23 condition rows, units and verbatim passages verified. Rubric §5 item 2 resolved (L2-02 conditional under lex specialis); L1-08 (unknown) and L3-04 (null) confirmed. Option (a) adopted for annex integration (Anexo B.10).
- 2026-11-07 — agent for Renzo: S1 done → paused. Case contract, source-access tests (Foxbit, BCB, Tether 200; Binance 202; MB 403; Wayback June copies only for terms/fee pages), `scripts/p3_28_access_map.py` (snapshot/card/selftest; deterministic aggregation; verbatim passage check), D-01 card: route not established on L1 (Res. 589 since 6 Nov vs Foxbit applicant status). A-01–A-11 registered. F-043 exploratory. Shared working tree with a parallel P3-29 session: only P3-28 files and lines committed.
- 2026-11-07 — agent for Renzo: Renzo takes S1 only (scope decision: S1, then the team chooses annex-only descriptive table or post-submission study; full H1 evaluation not attempted before 8 Nov). Second coder: Felipe.
- 2026-11-06 — Codex for Renzo: formalized from the P3-27 discussion at Renzo's request. Documentation only; no experiment launched or team member assigned.

## Result
S1 (feasibility) only, 7 Nov: a script can freeze, date and verify an access card for current Foxbit documents. On D-01 the documents do not establish the route (L1 unknown since Res. BCB 589's 6 Nov ban). No method was evaluated; H1, Q3 at scale and Q4 remain untested (F-043, exploratory).
