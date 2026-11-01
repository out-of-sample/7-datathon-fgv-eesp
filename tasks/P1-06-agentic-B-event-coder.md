---
id: P1-06
title: Extension B - AI event coder for the comparison currencies
phase: P1
status: done
owner: CS 3
working: -
due: 2026-11-01
depends: P1-04
---

## Goal
Use an AI agent with web search to list rule changes in each comparison country, check it against human
coding, and remove contaminated countries from the synthetic control. Plan: `docs/05-agentic-robustness.md` §B.

## Subtasks
- [ ] S1 — Write the agent prompt (countries, window 1 Nov 2025 - 30 Sep 2026, output columns as in P1-04). Save it
   in `data/raw/agentic_B/prompt.md` with the model name and date.
- [ ] S2 — Run the agent; save its raw output unchanged in `data/raw/agentic_B/`.
- [ ] S3 — Human check: open every source the agent gives for events between 1 Jun and 31 Jul 2026; mark real /
   wrong date / not supported.
- [ ] S4 — Accuracy: precision and recall against the P1-04 Brazil list and two comparison countries coded by hand
   by a teammate; Cohen's kappa on the event type.
- [x] S5 — Propose donor exclusions with reasons.
- [x] S6 — If not finished by the Sun 1 Nov gate: a human screens the donors manually and we say so.

## Success criteria
- [x] Every event used has a human-checked source
- [ ] `results/tables/P1-06_coder_accuracy.csv` (precision, recall, kappa, counts)
- [x] Donor exclusion list with reasons in the Result section
- [x] Any paid tool used was approved (decision log)

## Outputs
- `data/raw/agentic_B/`, `data/processed/P1-06_events_donors.csv`, `results/tables/P1-06_coder_accuracy.csv`

## Handoff
- **State:** done via S6 manual screening fallback (completed by Jonathan on 1 Nov).
- **Next step:** P2-04 synthetic control uses the clean donor pool (`EUR, TRY, ZAR, MXN, COP`; with `EUR` flagged for optional leave-one-out check due to March 2025 MiCA regime).
- **Open questions:** none.
- **How to resume:** `data/processed/P1-06_events_donors.csv` contains the manual event screen table.

## Log
- 2026-11-01, Jonathan: triggered S6 manual screening fallback at the Sun 1 Nov gate; screened surviving P1-05 donors (EUR, TRY, ZAR, MXN, COP) for 1 Jun – 31 Jul 2026 shocks; generated P1-06_events_donors.csv; status -> done
- 2026-10-31, agent for Renzo (note from P1-05): rule 2 of the donor exclusion rule (P1-05 Result) needs this task's screen for EUR, TRY, ZAR, MXN, COP, IDR, window 1 Jun – 30 Sep 2026 (earlier events listed for robustness). ARS and UAH are already out (capital controls; UAH easing package 11 Aug 2026, ARS cepo changes Jun 2026). Check for EUR: MiCA restrictions on USDT for EEA users from ~31 Mar 2025 `[verify]`.

## Result
**Manual screening triggered under S6 (`status: done`).**

Following P1-05, four currencies were already eliminated by Rules 1 and 3 (`ARS` and `UAH` for active capital controls/cepo; `IDR` and `PLN` for failing pre/post fixing coverage). 

Manual human screening of the five surviving candidates (`EUR, TRY, ZAR, MXN, COP`) over the critical window **1 Jun – 31 Jul 2026** (Rule 2) found **no discrete regulatory, tax, or capital-control shock** in any of the five jurisdictions during June–July 2026:
- **TRY, ZAR, MXN, COP:** Clean comparison currencies; no central bank FX intervention or crypto ban in June–July 2026.
- **EUR:** ESMA/MiCA restrictions on USDT for EEA users took effect around 31 Mar 2025, well before the 1 Nov 2025 pre-period start, and `EURUSDT` maintained full liquidity ($667M/month) and 100% coverage in P1-05. Retained under Rule 2 (no shock in Jun–Jul 2026), with a recommendation to check leave-one-out sensitivity without EUR in P2-04.

**Final clean donor pool for P2-04:** `EUR, TRY, ZAR, MXN, COP` (5 donors; meets the >= 4 criterion).