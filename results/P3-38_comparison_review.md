# P3-38 — Independent review of simple retrieval versus agentic investigation

Written in English for Renzo on 7 Nov 2026. Scope: option 3 in the discussion of P3-28. This is an independent investigation in new files, as Renzo requested because another session owns the implementation. The implementing session's files and decisions have not been changed.

**What this change does:** P3-28 compares a fixed document search with an AI that chooses further searches after reading evidence. This review tests whether the comparison's scoring and accounting can support its conclusions, and specifies how to make the experiment interpretable.

**Finding:** the idea remains testable, but the reviewed automated scores are provisional. Synthetic checks expose errors in answer validation, evidence checks, failure accounting and cost accounting. The existing protocol's human audit could address some errors, but those corrections must enter the final scores. There is no held-out performance finding or H1 verdict in this review.

## 1. Evidence and scope

- Reviewed revision: `c63aa7092352640ebd17b2228e7f1b86ed9f9c92`.
- Snapshot captured at `2026-11-07T05:56:40.952054+00:00`, while implementation was still being completed. Every captured file subsequently matched that revision byte for byte.
- Input hashes: [`tables/P3-38_inputs.csv`](tables/P3-38_inputs.csv). Raw copies remain outside Git under `data/raw/p3_38/bf915594278a62c5/`.
- Reproduction: `python3 scripts/p3_38_comparison_audit.py --from-git`. The command reads the pinned revision and verifies every file hash, so another teammate does not need the raw copies. It makes no network or model calls.
- Outputs: [`tables/P3-38_audit_checks.csv`](tables/P3-38_audit_checks.csv), [`tables/P3-38_inventory.csv`](tables/P3-38_inventory.csv), and [F-046](../findings/F-046-access-comparison-review.md).
- The audit executes the reviewed functions on synthetic records in a temporary directory. It does not inspect human reference sheets or held-out model answers. Development summaries were encountered during the initial inspection; none is used as evidence for H1.
- Expected workload: the declared small research pilot, with saved outputs and offline scoring. This is not a production service audit.

There are 15 synthetic checks: 13 violate the stated or required scoring contract and two controls pass. These are deliberately selected examples, not a random sample, an error rate or 13 independent bugs. They support the concrete findings below.

## 2. What the experiment should establish

The useful question is: **when a document answer is incomplete or conditional, does choosing what to inspect next produce more correct, supported answers at comparable cost?**

There are separate possible benefits:

| Benefit | What must change in the comparison | What would not establish it |
|---|---|---|
| Better retrieval | More of the relevant evidence reaches the answerer | A higher score produced by a more permissive scorer |
| Better verification | Unsupported or mis-scoped answers are corrected | Matching a real quotation that does not support the claim |
| Adaptive investigation | The next read/search depends usefully on what was found | Spending much more time or reading much more text than the fixed workflow |
| Practical usefulness | More supported answers, fewer corrections, acceptable time and resource use | A convincing demonstration on a case used to design the system |

An access-condition answer describes what the specified documents establish for a profile, operation, amount, network and date. It does not certify a completed payment or identify the cause of June's price premium. The economic connection remains the distinction between an observed price and the conditions for using a route.

## 3. Must fix before treating automatic scores as final

Line references below are to `scripts/p3_28_methods.py` at the reviewed revision. Corrections are recommendations to its owner, not edits made by this review.

### R1 — The answer matcher accepts wrong units and wrong requirements

- **What this is:** `correct()` at line 335 decides whether a field earns credit.
- **Problem:** C02 accepts 72 days against a reference of 72 hours. C03 accepts an unrelated nonempty answer for G02 because it compares only whether text exists. C04 accepts the opposite company-verification requirement for F03 because its state matches. These examples test the matcher directly.
- **Fix:** Normalize numeric values together with their units; retain the distinction between calendar and business days. For requirement text, use human-reviewed accepted meanings or a blinded field-level decision. Matching the state alone cannot establish that the value is correct.
- **If we skip it:** A method can gain coverage by giving an incorrect condition, and the ranking can reflect scoring shortcuts rather than useful answers.

### R2 — Quotation presence is only a mechanical check

- **What this is:** `evidence_ok()` at line 362 checks whether the quoted string occurs in a permitted document.
- **Problem:** C05 accepts an empty quotation. In C07, an answer about Pix cites only “Contact support.” and receives SAC = 1.0 for that synthetic case. The source string exists, but it does not support the answer. The current protocol already calls for manual semantic checking at G2; the automatic score cannot replace that check.
- **Fix:** Reject empty quotations, validate source/quotation pairs, and have blinded reviewers assess whether each score-bearing answer follows from the cited passage for the case's profile, date and network. Store those decisions and incorporate them into the final score. Audit non-availability fields too, including fees and requirements.
- **If we skip it:** “Supported answer coverage” measures quotation presence plus a loose answer match. It does not yet measure evidence-supported correctness.

### R3 — Failures, missing records and empty denominators change the score incorrectly

- **What this is:** `score()` at line 368 walks the run files and reference rows that happen to exist, then computes a macro-average.
- **Problem:** C08 gives a failed run SAC = 1.0 when a valid draft remains in its answers. C09 omits a scheduled case with no run file. C10 accepts an incomplete reference and silently skips the missing field. C11 includes a case with no answerable fields as zero in the macro-average: the synthetic example becomes 0.5 instead of 1.0. The original specification excludes such cases from SAC while retaining them for unknown/error measures.
- **Fix:** Score against a locked case × method × repeat manifest. Require a complete reference before scoring. Refuse to finalize an incomplete run matrix, or represent planned failed runs explicitly under the declared failure rule. Apply zero credit to failed runs as promised, and exclude zero-answerable cases from the SAC average while reporting their number and unknown handling.
- **If we skip it:** Missing and failed runs can make a method look better, and cases without answerable fields can make it look worse for the wrong reason. Different methods may be compared on different denominators.

### R4 — The automatic guardrail does not cover all emitted claims

- **What this is:** the guardrail counts some structured `supported` values. The task specification requires checking unsupported positive availability claims in the complete output, including free text.
- **Problem:** C12 puts an unsupported end-to-end availability assertion in an answer's `note`; the counter remains zero. C13 gives the same field an unsupported positive followed by `unknown`; the dictionary at line 384 keeps only the latter. Neither test claims this occurred in a real model run.
- **Fix:** Require exactly one answer for every expected field and reject duplicates or extra fields. Inspect retained notes and other emitted prose under the same claim rubric, or make the displayed product strictly structured and still audit the benchmark output under the original rule. Keep raw and filtered output so a filter cannot silently erase a safety failure.
- **If we skip it:** A zero counter can be reported even though the response contains an unsupported route claim. The protocol's narrower structured-state rule must not silently replace the original requirement.

### R5 — Token accounting drops earlier calls to the same model

- **What this is:** the `usage` dictionary comprehension in `run_one()` at line 303 stores model usage under a model-name key.
- **Problem:** C14 runs the real record writer with two synthetic calls reporting 10 and 20 input tokens for the same model. It records 20 instead of 30. A later call overwrites the earlier entry. `notional_usd` is summed separately, so this check does not establish the same error in that field.
- **Fix:** Sum each numeric usage component across calls and retain the per-call records. Report uncached input, cache reads, cache creation and output separately, together with total elapsed time and the CLI's notional cost estimate.
- **If we skip it:** The fixed verification workflow can appear to use fewer tokens than it actually used, invalidating a comparison of quality and resources.

### R6 — The reviewed limits do not implement the same overall resource ceiling

- **What this is:** the methods are meant to be compared under the same model, source corpus and resource ceiling.
- **Problem:** `TIMEOUT_S = 900` applies to each call. B2 has two calls, so its potential model-call time is 1,800 seconds, whereas B1 and A each have one 900-second call/session. A additionally has a 40-turn limit. No shared aggregate token/output budget is enforced in this code. B1/B2 receive retrieved chunks; A can read full permitted files. This is a code/protocol observation, not a measured runtime result.
- **Fix:** Define and enforce a total per-case budget across all calls, with actual use recorded. Keep the retrieval allowances explicit. Before the held-out run, select limits using development cases and test B2 against A under the same total allowance; document any runtime limitation that prevents enforcement.
- **If we skip it:** A quality difference cannot be attributed specifically to adaptive investigation. The comparison is of differently resourced workflows, which is still descriptive if labelled that way.

### R7 — The scorer does not enforce the run's frozen evidence version

- **What this is:** run records contain `corpus_hash`, but scoring reads the latest text extracts and does not validate that hash.
- **Problem:** C15 supplies a deliberately incompatible corpus hash and scoring proceeds. Thus a quotation check could use a different document version from the one the method saw. The recorded `prompt_hash` also omits the complete method-specific prompt and several retrieval/limit settings; the revision and exact prompt record are needed to reconstruct them.
- **Fix:** Verify the source manifest, text hashes, case/field/rubric versions, model configuration and run manifest before scoring. Store the complete prompts/tool traces or their immutable references, with an explicit hash of the full configuration. A mismatch should stop final scoring, not silently select current files.
- **If we skip it:** A source update or configuration change can alter the evaluation without changing the run identity.

## 4. What the source inventory can support

This inventory is reproduced from the frozen case and corpus manifests, without reading held-out source bodies or labels:

| Split / family | Cases | Family-specific documents | Shared documents available to each case |
|---|---:|---:|---:|
| Development / Foxbit | 3 | 11 | 5 |
| Development / funds' press reports | 2 | 4 | 5 |
| Held-out / Avenia | 4 | 11 | 5 |
| Held-out / Binance | 4 | 0 | 5 |
| Held-out / Mercado Bitcoin | 4 | 0 | 5 |

The 31-document corpus is real, but the nominal three-family held-out sample contains provider-specific documents for only Avenia in this version. Eight held-out cases receive shared material only. That does not make every field unanswerable: an issuer document may answer a network question. Actual answerability must come from the human reference.

Missing-document cases are useful for checking whether a method preserves uncertainty. They cannot by themselves establish broad performance in extracting provider conditions. The protocol plans manual collection for the missing providers and a new corpus version. Complete that collection before freezing, or explicitly narrow the study and show answerable-field counts by family. Do not drop a difficult provider after seeing model scores.

The planned pilot has fewer cases than the original design target. Grouping by provider is a useful safeguard, but several profiles and assets using the same documents are not independent provider replications. Report per-family paired differences and descriptive uncertainty; do not inflate the effective sample size using fields or repeated runs.

## 5. Recommended comparison design

### Methods and purpose

| Method | Procedure | What its comparison tells us |
|---|---|---|
| B0 | Fixed extraction rules, with `unknown` when no rule applies | A transparent floor for mechanical extraction; its limited field coverage must be disclosed |
| B1 | A fixed retrieval plan followed by one model answer | Whether the agent adds value over a practical simple baseline |
| B2 | The fixed retrieval plan, extraction and a prescribed verification step | Whether adaptive investigation adds value beyond extra checking |
| A | A model chooses subsequent searches/reads based on missing or conflicting evidence | The proposed adaptive method |

Keep the same underlying model, case questions, source corpus, output schema, scoring rubric and human audit across model methods. Shared mechanical validation should not selectively advantage one method. If B2's deterministic quotation filter remains part of its distinct workflow, disclose it and preserve both pre-filter claims and final answers for the guardrail.

B2 must be a credible comparator. Ensure its fixed retrieval supplies surrounding context and the document metadata needed for dates, profiles and exceptions. The current B2 verifies the same excerpts it first received, so it cannot recover evidence absent from those excerpts. Any stronger fixed retrieval plan must be developed and frozen before held-out evaluation; it must not be chosen after seeing which questions A answers correctly.

### Resource controls

Use a budget for the complete case, not for each model call separately. The owner should freeze total elapsed time, total model-token allowance, output allowance, retrieval operations and the amount of evidence delivered to the model. Log consumption as well as ceilings. Distinguish repeated cached input from new input; token traffic and a pricing estimate are different measures.

Equal ceilings alone do not demonstrate equal cost. Predeclare a matched-budget B2-versus-A comparison using development-calibrated limits. If A consumes more resources, report its quality/cost tradeoff. Do not infer that additional computation is the causal mechanism, or that adaptation is the mechanism, from an observational cost difference. A small second budget level can test sensitivity if the existing quota supports it; it is optional and must be fixed before final runs.

No numeric token budget is adopted by this review: current cost accounting must be repaired and measured on development cases first. The existing 10-percentage-point H1 threshold remains the task's proposed reading rule, not a threshold selected by this review.

### Reference and scoring

Two human readers should independently code from the same frozen documents, resolve disagreements and preserve both original sheets. Neither should see model identities or outputs before the reference is finalized. The implementer must not tune against the held-out reference.

The reviewed protocol proposes running models before the human reference exists and says this is “the same or stronger” protection. That equivalence is not established. Output-first evaluation can be defensible if the cases, corpus, rubric, scoring rules and run schedule were fixed first, outputs are immutable, coders remain blind, and no decisions change after inspection. It does not substitute for checking that humans can apply the rubric. Prefer completing G1 before the final run. If the owner retains the changed order, register it as an amendment with the remaining limitations; do not label G1 passed early.

For each case and scheduled repeat, the final score is the number of answerable fields correctly answered **and supported in meaning by the evidence**, divided by the reference's answerable fields. Average across repeats within a case, then across eligible cases. Show the same paired cases for every method. Keep all-unknown cases in unknown handling and the claim audit, even though they are excluded from SAC.

The final review table should contain: method, case, family, repeat, answerable fields, supported correct fields, SAC, unsupported availability assertions, unknown/conflict handling, failure status, human correction time, total latency and resource use. Freeze acceptable equivalences and unit conversions before scoring; human decisions resolving new edge cases should be blinded, logged and applied symmetrically.

### What conclusions would be justified

| Observed result after independent evaluation | Permitted interpretation |
|---|---|
| A clears the planned gain over B1, passes the complete guardrail, and improves over B2 at comparable resources | Preliminary support for adaptive investigation on this pilot's sampled families |
| A beats B1 but adds little over B2 | The simpler fixed verification workflow is sufficient at the measured quality/cost; adaptive advantage is not established |
| A gives more supported answers but fails the guardrail | The prototype fails the task's acceptance rule despite its coverage gain |
| Most potentially informative answers remain unavailable in the corpus | Evidence of documentation gaps and uncertainty handling; limited evidence about retrieval superiority |
| A costs more and no matched-budget test is available | A workflow quality/cost tradeoff, with the source of the gain unresolved |
| Human reference, complete runs or evidence audit are missing | A development demonstration; no H1 verdict |

## 6. Execution sequence for the implementing owner

1. **Resolve scoring before expansion.** Address R1–R5 and R7. Use the synthetic checks as concrete regression requirements, preserving the old development results as superseded/provisional rather than silently replacing their meaning.
2. **Finish the source and reference contract.** Complete or explicitly narrow the missing-provider corpus; freeze the cases, rubric and field meanings. Have the two readers establish G1 independently of model outcomes.
3. **Calibrate the comparison on development cases.** Strengthen fixed retrieval where needed, enforce the total budgets, and log complete per-call use. Select the configuration once.
4. **Register the final protocol and schedule.** Hash the corpus, full configuration, reference or approved reference procedure, and the full case × method × repeat manifest. A final run must not begin under a changing version.
5. **Run and review all scheduled outputs.** Keep failures, apply the complete claim audit and semantic support checks, and calculate paired scores and costs. If execution or scoring is incomplete, report that explicitly.
6. **Apply the reading rule and reproduce offline.** An independent teammate should regenerate the tables and check the claims before any deck result. The existing descriptive access card can remain useful while the comparative claim is pending.

This sequence can be shortened to a labelled development pilot if the deadline or human review capacity prevents final evaluation. The scientific acceptance rule should not be lowered to produce a favourable slide.

## 7. Decisions and provenance

| ID | Type | Decision / recommendation | Authority or evidence |
|---|---|---|---|
| D1 | User instruction, adopted | Continue exploring option 3 and record the work in English | Renzo's request in this conversation |
| D2 | User instruction, adopted | Work independently in new files because P3-28 is active elsewhere | Renzo's explicit reply to the coordination question |
| D3 | Administrative, applied | Use P3-38 after concurrent synchronization exposed collisions with P3-35, P3-36 and P3-37 | Other sessions' economic-function and post-extension-audit tasks; publish this task from a clean temporary checkout to preserve shared edits |
| D4 | Review conclusion | Automatic scores from the reviewed version require corrections/audit before supporting H1 | C02–C15 and R6; this does not retract any frozen economic result |
| D5 | Recommendation to P3-28 owner | Repair scoring/accounting, then compare A with a credible B2 at matched total budgets | R1–R7 and the original task question |
| D6 | Recommendation to team | Keep the result descriptive until human reference, complete runs and final evidence audit exist | Original P3-28 G1/G2 and scientific claim limits |
| D7 | Scope limit, applied | No model evaluation, hidden-label inspection, source collection, legal determination or deck edit in this review | Independent-analysis scope and separation from active implementation |
| D8 | Protocol exception, recorded | Shared STATUS, decision log and board updates are supplied as handoff text in a new file | User's new-files-only instruction; pre-existing STATUS conflicts; see protocol handoff |

These are review recommendations unless explicitly marked applied or adopted. This report does not adopt a new P3-28 protocol, change its hypotheses, approve a gate, or assign human work on the team's behalf.

**Verdict: fix R1–R7 and complete the independent reference/evidence checks before using the comparison as an H1 result.**

**Not checked:** actual provider access, legal correctness, the model CLI's isolation guarantees, hidden human labels, held-out performance, or changes after the pinned revision. No external literature or current regulation was researched for this code-and-design review.
