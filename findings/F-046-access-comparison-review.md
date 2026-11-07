---
id: F-046
title: Synthetic checks show that P3-28 comparison scores need correction and evidence review before an H1 claim
status: exploratory
task: P3-38
date: 2026-11-07
checked_by: -
---

## Claim
At revision `c63aa7092352640ebd17b2228e7f1b86ed9f9c92`, 13 of 15 deliberately constructed synthetic checks expose violations of the intended scoring/accounting contract; two control checks pass. The checks concern the evaluation machinery, not model performance, and are not an estimate of a real-world error rate. The automated comparison is not ready to establish P3-28 H1 without the corrections and human evidence checks in the independent review.

## Evidence
- Review: `results/P3-38_comparison_review.md` (R1–R7); exact inputs and SHA-256 hashes: `results/tables/P3-38_inputs.csv`.
- Code and design snapshot: 7 Nov 2026, `05:56:40.952054+00:00`. All eight captured files match the pinned revision. Raw copies are outside Git; replay can read the same bytes from Git.
- Reproduce offline, without a model or human labels:
  ```bash
  python3 scripts/p3_38_comparison_audit.py --from-git
  ```
  Writes `results/tables/P3-38_audit_checks.csv` and `results/tables/P3-38_inventory.csv`. The script checks input hashes, extracts the reviewed functions and supplies artificial records. It never calls the model CLI.
- Synthetic observations:
  - **C02–C04:** the answer matcher accepts 72 days for 72 hours, an unrelated nonempty G02 condition, and an opposite F03 requirement with the same state.
  - **C05/C07:** an empty quotation passes the presence check; an irrelevant quotation with a matching answer state receives SAC = 1.0 in a synthetic one-field case.
  - **C08–C11:** a failed run retaining a correct answer receives SAC = 1.0; a scheduled case without a run file disappears; a missing reference field is skipped; a zero-answerable case lowers a synthetic macro-average from the intended 1.0 to 0.5.
  - **C12/C13:** an unsupported positive in free text and an earlier duplicate-field positive are not counted by the structured guardrail.
  - **C14:** two simulated calls using 10 and 20 input tokens record 20, not 30. Earlier same-model usage is overwritten. The notional-cost field is separately summed; this check makes no claim about its accuracy.
  - **C15:** a deliberately incompatible corpus hash is accepted by scoring.
  - **C01/C06 controls:** a correct numeric answer matches; an unpermitted source is rejected.
- Static resource observation (R6): the reviewed `TIMEOUT_S` is 900 seconds per call. B2 has two calls, allowing up to 1,800 seconds of model-call time, while B1 and A have one call/session each. A has a 40-turn ceiling; the reviewed code does not enforce one shared aggregate token/output ceiling. These are configured limits, not observed runtimes.
- Manifest inventory: 31 documents; five development cases across Foxbit (three cases, 11 family documents) and funds' press reports (two cases, four family documents); 12 held-out cases across Avenia, Binance and Mercado Bitcoin (four each). Avenia has 11 family documents; Binance and Mercado Bitcoin have zero each in this corpus version. Five shared documents are available to each case. Thus eight held-out cases have only shared documents; their actual field answerability remains for human coding.
- The original P3-28 reading rule requires a 10-percentage-point gain over B1, the guardrail and a comparison with B2. This review does not change that threshold or measure such a gain.

## Caveats
- The synthetic failures are selected counterexamples. Several exercise the same underlying defect. Do not report “13 bugs,” a 13/15 model error rate, or any conclusion about which model method wins.
- `P3-28_protocol.md` already includes a manual semantic audit at G2. Some automatic-score errors can be caught there, but final scores must incorporate the decisions and cover all score-bearing fields.
- Independent code review is not the required independent human reference or a completed G2 audit. No human held-out labels or held-out outputs were inspected, and no method was rerun.
- Findings apply to the pinned revision. Later fixes require checking their own revision; this file should retain the earlier result and add a dated history note rather than erase it.
- No current legal or operational conclusion is made about a provider. Missing provider documents do not prove that its services are unavailable.

## Used in deck
Not used. This is a method-readiness review, not a comparative performance result or a new economic estimate.

## History
- 2026-11-07 — Renzo's independent review agent created this exploratory finding under P3-38. Replayed the synthetic checks from both local snapshots and the pinned Git revision. Peer reproduction remains pending.
