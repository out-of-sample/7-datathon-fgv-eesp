---
id: F-052
task: P3-44
title: AI-Reviewed Access Benchmark Exploratory Pilot Results
phase: P3
status: exploratory
created: 2026-11-08
checked_by: Independent Verification Reviewer
authors:
  - Antigravity AI Agent
  - Independent Verification Reviewer
---

# F-052: AI-Reviewed Access Benchmark Exploratory Pilot Results

## 1. Executive Summary & Context

Under Felipe's explicit authorization on 7 November 2026, task `P3-44` was executed as an **AI-reviewed exploratory pilot** to evaluate access-document information extraction across Brazilian crypto off-ramps (Avenia, Binance, Mercado Bitcoin). This exploratory pilot substituted separate, independent AI agent workflows for the unavailable human coders and auditors, in strict compliance with the protocol frozen in `results/P3-44_protocol.md`.

> [!IMPORTANT]
> **Exploratory Pilot Disclaimer:**
> All reference coding, adjudication, and semantic audits were performed entirely by isolated AI agents. This pilot does **NOT** constitute human validation, operational access certification, or proof of real-world exchange route availability.

The evaluation compared four fixed information-access methods:
- **`B0`**: Blind guessing (deterministic baseline without document access).
- **`B1`**: Simple prompt-inlined retrieval (all permitted sources concatenated into the prompt).
- **`B2`**: Fixed two-call verification (draft generation followed by verbatim passage-checking).
- **`A`**: Adaptive agent with local text-reading tools within isolated case workspaces.

All runs and audits were executed with frozen configuration `a82ec5f9c1e3778ab44a4545d77fb1f1d0bdc63f92a3b090917aa88e891172b5` and a 36-source frozen corpus (`results/tables/P3-44_corpus.csv`).

---

## 2. Quantitative Results & Score Summary

All 140 scheduled jobs (20 development: 5 cases $\times$ 4 methods; 120 held-out: 12 cases $\times$ 3 repeats $\times$ 3 model methods + 12 $B_0$ runs) were executed and audited. Every distinct claim payload (175 in dev, 815 in held-out) was audited under double-blind semantic audit procedures (`audit_dev.csv` SHA-256 `37b179d3...`, `audit_heldout.csv` SHA-256 `a2d7ba07...`).

### Summary of Benchmark Performance (`results/tables/P3-44_summary.csv`):

| Split | Method | Cases in SAC | SAC (Macro Mean) | Unsupported Positives | Failed Runs | Missing Runs | Unknown Kept | Wall Clock (s) | Total Output Tokens |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Dev** | `B0` | 5 | 0.147 | 0 | 0 | 0 | 8 / 8 | 0.0 | 0 |
| **Dev** | `B1` | 5 | 0.890 | 0 | 0 | 0 | 8 / 8 | 1,055.0 | 13,462 |
| **Dev** | `B2` | 5 | 0.890 | 0 | 0 | 0 | 8 / 8 | 1,316.0 | 33,158 |
| **Dev** | `A`  | 5 | 0.569 | 0 | 2 | 0 | 2 / 8 | 1,559.0 | 36,524 |
| **Held-out** | `B0` | 12 | 0.000 | 3 | 0 | 0 | 110 / 110 | 0.0 | 0 |
| **Held-out** | `B1` | 12 | **0.737** | 44 | 0 | 0 | 297 / 330 | 10,164.0 | 128,858 |
| **Held-out** | `B2` | 12 | **0.757** | 40 | 0 | 0 | 304 / 330 | 14,010.0 | 227,555 |
| **Held-out** | `A`  | 12 | **0.000** | 36 | 36 | 0 | 0 / 330 | 9,146.0 | 179,189 |

---

## 3. Protocol Decision & Benchmark Verdict

The reading rule frozen in `results/P3-44_protocol.md` specifies:
1. Method `A` must achieve at least a **10 percentage point gain** over simple retrieval `B1` ($SAC_A - SAC_{B1} \ge 0.10$).
2. Method `A` must produce **zero unsupported positive availability claims** in the audited inventory.
3. Any advantage over fixed verification `B2` must not be explained by resource consumption.

### Verdict (`results/tables/P3-44_verdict.json`):
```json
{
  "label": "AI-reviewed exploratory pilot; not human validated",
  "budget_equivalence": "not established merely by equal ceilings; compare recorded resource use",
  "guardrail_unit": "retained claim representations, not independent errors",
  "reading_rule": "A gain >=0.10 over B1; zero unsupported positives; advantage over B2 not explained by resources",
  "verdict": "fails zero-unsupported-positive guardrail",
  "A_minus_B1": -0.7368,
  "A_minus_B2": -0.7566
}
```

### Key Analytical Findings:
1. **Adaptive Method (`A`) Failure & Guardrail Breach:**
   - On held-out cases, Method `A` failed to establish superiority over prompt-inlined retrieval (`B1`) or verification (`B2`).
   - All 36 held-out runs of Method `A` incurred trace policy violations (`adaptive_tool_outside_corpus_reader`), zeroing their SAC coverage scores under protocol rules while auditing their emitted answers.
   - Furthermore, Method `A` emitted 36 unsupported positive claim representations across held-out evaluations, directly failing the zero-unsupported-positive guardrail.
2. **Simple Prompt Inlining (`B1`) and Verification (`B2`) Robustness:**
   - Fixed verification (`B2`) achieved the highest overall SAC coverage (0.757 macro mean on held-out), slightly edging out direct prompt retrieval (`B1` at 0.737).
   - Both `B1` and `B2` demonstrated reliable document extraction without incurring tool or execution trace errors.
3. **Exploratory Pilot Limitations:**
   - The reference dataset was generated and adjudicated via AI agents (`coder_one`, `coder_two`, `adjudicator`). While inter-agent agreement was high (181/229 initial agreement; 48 adjudicated), shared latent model biases remain an inherent limitation.
   - Results should guide future benchmark design and information retrieval architecture, but cannot substitute for human legal/operational auditing of exchange terms.
