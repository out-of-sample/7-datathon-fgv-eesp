---
id: F-052
task: P3-44
title: AI-reviewed access pilot finds no demonstrated adaptive advantage
phase: P3
status: exploratory
created: 2026-11-08
checked_by: Independent Verification Reviewer; Codex diagnostic reviewer
authors:
  - Antigravity AI Agent
  - Codex for Felipe
---

# F-052 — AI-reviewed access pilot

The saved experiment does not establish an advantage for the adaptive agent over simpler document verification. Its original zero coverage score mainly reflects a folder setup error. A separate diagnostic removes that penalty and still finds no coverage advantage. All methods also made unsupported claims. This supports using the output as research assistance requiring verification, not as certification that a treasury route works.

Felipe authorized replacing human coding and auditing with separate AI agents on 7 November. This is an **AI-reviewed exploratory pilot**, with no human validation. Two source-only coders, a third adjudicator and separate method-masked answer audits are recorded. Method masking does not establish a fully double-blind study. Shared AI errors remain possible.

## What was compared

The frozen corpus has 36 public sources. There are 17 cases and 229 reference fields; 48 fields required adjudication. All 140 scheduled jobs have saved records: 20 development and 120 held-out jobs. The audits contain 175 distinct complete payloads in development and 815 in held-out cases. Repeated identical payloads share a decision; differing comments remain distinct.

- **B0:** deterministic rules that search the permitted documents, without model inference.
- **B1:** one model call using fixed retrieved excerpts in its prompt.
- **B2:** a draft followed by a fixed verification call.
- **A:** adaptive local document reading.

The model methods used the replacement Antigravity runner labeled `gemini-flash-antigravity`. This label does not independently verify the exact service model build. Historical Claude and interrupted Codex batches are excluded. The switch from the written v3 protocol to v4 native tools, including dispatch restrictions, was not fully documented before execution; the retrospective disclosure is in `results/P3-44_protocol.md`.

## Results

Coverage is the mean across cases of the share of answerable fields with a correct, evidence-supported and audit-approved final answer. Failed runs earn zero under the original rule.

| Held-out method | Original coverage | Post-hoc diagnostic coverage | Unsupported claim representations | Original failed runs |
|---|---:|---:|---:|---:|
| B0 | 0.0% | 0.0% | 3 | 0 |
| B1 | 73.7% | 73.7% | 44 | 0 |
| B2 | 75.7% | 75.7% | 40 | 0 |
| A | 0.0% | 72.9% | 36 | 36 |

Original scores and verdict are preserved. Each held-out adaptive trace has one attempted read in the wrong folder supplied by its dispatch message. Each saved response confirms the path was missing and returned no file. Subsequent allowed reads do not cancel the original violation. The diagnostic waives only those 36 failures, in memory, retaining every answer, reference judgment and semantic audit decision. It changes no development run; the two development failures remain.

Even in this diagnostic, A trails B1 by 0.8 percentage points and B2 by 2.8 points. It does not reach the planned ten-point gain over B1, and its unsupported-positive guardrail still fails. These are descriptive differences, not evidence of statistical equivalence or a clean ranking of research ability.

Unsupported counts include final answers, drafts and retained raw prose, sometimes repeating the same underlying mistake. They are not counts of independent errors or error rates. The guardrail also covers unsupported requirements, dates and evidence failures; not every counted item asserts an available trading route.

## Evidence recheck and limits

The follow-up source check supports several substantive concerns: Binance's A-30 fee table does not establish the case's BRL purchase route; E-06b explicitly starts on 1 January 2027 and cannot establish a requirement already in force on the case date; Mercado Bitcoin's A-34 direct Pix purchase offer does not expressly establish funding a reais account balance. These observations concern the frozen documents and benchmark rubric, not current legal advice.

Other flags are interpretation-sensitive. A-41 discusses USDT/TRC20 and says Mercado Bitcoin supports major networks, but does not unambiguously map each case asset to its withdrawal network. Preserve the conservative reference and the auditor's differing judgments; do not call every such disagreement an invented claim. No reference or audit decision was changed in this diagnostic, which is not a complete new semantic audit.

Resource equivalence is unestablished. The dispatch added a twelve-read instruction in the inspected held-out setup while the general tool ceiling was forty; fixed retrieval also limits what B1/B2 see. Antigravity visible output-token totals are estimates apportioned from output plus thinking, not directly measured visible-token counts. Money costs remain unavailable. These limits and the real execution failures preclude an unqualified superiority conclusion.

## Reproduction and review

With the ignored frozen raw bundle available, run `python scripts/p3_44_diagnostic.py`. It first reproduces all original case, error and cost tables, then writes only separately named `P3-44_diagnostic_*` tables and a hash receipt. It checks that original outputs and saved inputs remain unchanged. No inference is called.

Six diagnostic boundary tests and the existing 15 audit and 12 pipeline tests pass. A separate agent independently checked all 41 adaptive records and the source examples, finding no blocking diagnostic defect. Task P3-44 remains in review; the original experimental limitations remain visible.

## History

- 8 Nov — Antigravity completed v4 records, audits and original scoring.
- 8 Nov — Codex reviewed completion, corrected baseline/protocol claims, reproduced original scores and added the separately labeled saved-answer diagnostic at Felipe's request. Original artifacts retained.
