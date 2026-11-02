# Prior Knowledge & Memory Test: Brazilian Crypto FX Event (23 June 2026)

**Project:** 7º Datathon de Moedas Digitais FGV EESP (2026) — Team Out of Sample  
**Task:** P3-05 Subtask S3  
**Status:** Pre-registered template ready for live execution  
**Date:** 2026-11-02  
**Tester:** Renzo / Jonathan  

---

## 1. Objective and Protocol

To verify that the AI coding agents do not possess pre-existing memorized conclusions or data leakage about the 23 June 2026 event (Notice 42,084 / BCB crypto monitoring and foreign exchange regulatory clarifications), we query each model family in a clean session **with web search and external retrieval strictly disabled**.

### The Exact Memory Prompt:
> *"What changes or regulatory notices occurred regarding Brazilian stablecoins and crypto foreign exchange on 23 June 2026?"*

### Evaluation Criteria:
1. **Unaware / Cutoff:** Model states it has no knowledge of events on 23 June 2026 or that its training cutoff precedes mid-2026. (Ideal: zero-shot prior is uninformative).
2. **Hallucination:** Model invents fictional regulations or dates.
3. **Specific Knowledge:** Model describes BCB Notice 42,084 or specific stablecoin tax/monitoring rules. (If observed, must be noted as a prior).

---

## 2. Model Family Test Results

### Family 1: Anthropic Claude (Claude 3.7 Sonnet / Claude 3.5 Sonnet)

| Parameter | Value |
|---|---|
| **Interface / CLI** | Claude Code / Claude Chat |
| **Model Version** | `claude-3-7-sonnet-20250219` (or `claude-3-5-sonnet-20241022`) |
| **Web Search** | Disabled |
| **Timestamp** | *[Fill on execution]* |
| **Knowledge Assessment** | *[Unaware / Hallucination / Specific]* |

#### Verbatim Model Response:
```text
[Paste verbatim response from Claude here]
```

---

### Family 2: OpenAI (GPT-4o / o3-mini)

| Parameter | Value |
|---|---|
| **Interface / CLI** | Codex CLI / ChatGPT |
| **Model Version** | `gpt-4o` / `o3-mini` |
| **Web Search** | Disabled |
| **Timestamp** | *[Fill on execution]* |
| **Knowledge Assessment** | *[Unaware / Hallucination / Specific]* |

#### Verbatim Model Response:
```text
[Paste verbatim response from OpenAI here]
```

---

### Family 3: Google (Gemini 2.0 Flash / Pro)

| Parameter | Value |
|---|---|
| **Interface / CLI** | Gemini CLI / Gemini Web |
| **Model Version** | `gemini-2.0-flash` / `gemini-2.0-pro` |
| **Web Search** | Disabled |
| **Timestamp** | *[Fill on execution]* |
| **Knowledge Assessment** | *[Unaware / Hallucination / Specific]* |

#### Verbatim Model Response:
```text
[Paste verbatim response from Gemini here]
```

---

## 3. Summary & Synthesis

| Family | Model | Pre-existing Knowledge of 23 Jun 2026? | Risk of Contamination |
|---|---|---|---|
| Claude | | [ ] Yes / [ ] No | Low / Med / High |
| OpenAI | | [ ] Yes / [ ] No | Low / Med / High |
| Gemini | | [ ] Yes / [ ] No | Low / Med / High |

### Conclusion for the Jury:
*(To be completed after recording verbatim responses. Confirms that agents deduced the rise in the USDT premium empirically from the provided kline data rather than recalling pre-existing news or commentary).*
