---
id: P3-22
title: Other countries, stage 1 - qualify each case before any test (Ukraine Aug 2026, Argentina Apr 2025, EEA Mar 2025; Russia, Nigeria listed)
phase: P3
status: todo
owner: CS 2
working: -
due: 2026-11-05
depends: P1-05, P1-06
---

## Goal
Decide which foreign episodes can answer a meaningful question about channels opening or closing, **before any outcome is
computed**. This is stage 1 of the staged extension recommended in the improvements log (2 Nov review): qualify cases →
lock a protocol → run and review. It shows where the idea applies and where it does not; it is not a hunt for three
favourable signs. Brazil stays the centre of the project.

## Rules
- No premium value, plot or model around a candidate date is computed or viewed in this task. No download.
- Stages 2–3 are retrospective specifications. They are never called "predictions"; only P3-20 is prospective.
- Every date and rule comes from an opened source registered in `docs/sources.md` (X-01–X-03 already opened). A case
  whose primary instrument cannot be opened is "not qualified for now".
- Report every case's disposition, exclusions included.
- Cap: 4 hours. P5 tasks (deck, figures, scripts as .txt, submission) take priority.

## Eligibility card (one per case)
1. Instrument and publisher; primary text opened (quote, link).
2. Announcement date and time; implementation date(s); intermediate steps.
3. Who is affected (individuals, firms, banks, exchange users by residence).
4. Which channel changes: easier bank dollars as a **substitute** for buying USDT, easier **supply** of USDT, or both.
5. Observable outcome and benchmark; what they cannot show (for example, a global quote is not the cost for a resident
   who lost access; a wholesale reference is not a household's executable price).
6. Overlapping developments within ±25 business days, screened from sources, not from prices.
7. Data coverage and liquidity (coverage only, from file listings and F-010 coverage tables).
8. **Prior exposure inventory**: every table, figure, model fit, notebook and agent output in the repo that touches this
   currency or date (F-010 yearly means and volatility, P1-05 tables, P1-06 event screen, P2-04 donor pool, story
   notebook). Class: outcome not examined / summaries seen / examined.
9. The question the case can answer: reopening test, policy-package exploratory case, or market-resilience boundary case.

## Starting dispositions (proposal for the gate, not decided)

| Case | Likely question | Main open issues |
|---|---|---|
| Ukraine, NBU Res. 90 (10 Aug 2026, in force 11 Aug) | Did easier access to bank dollars for individuals narrow the USDT premium? | NBU primary text not opened (Interfax-Ukraine 11 Aug was opened by the agent for Renzo, 3 Nov; X-03 is secondary); separate bank FX-position change on 1 Sep inside a four-week window; war news; Binance delisted USDT/UAH on 28 Sep (announced around 23 Sep, secondary); policy timing may respond to market conditions |
| Argentina, BCRA Phase 3 (announced 11 Apr 2025, X-01) | Exploratory: what happened to the gap against the official reference after a liberalisation package | A package (bands, financing), not one access change; the denominator moves, and decomposing the legs is accounting, not identification; wholesale vs retail benchmark; yearly means already seen (F-010). The 2 Nov "future work only" line is superseded by the "Research continues" row |
| EEA, Binance (announced 3 Mar 2025, spot restriction 31 Mar 23:59 UTC, X-02) | Boundary case: did the global EUR/USDT market show a meaningful price disruption? Needs an equivalence margin fixed in advance | Anticipation (announced four weeks ahead, intermediate steps 25 and 27 Mar); a global quote ≠ EEA residents' access; already in the P1-06 event screen (with the ESMA homepage as source, which fails our rule) |
| Russia (Binance USDT/RUB, Dec 2019 – Jan 2024) | – | 2022 controls came with the invasion and sanctions; no data downloaded; no dated source opened. Likely excluded now |
| Nigeria (Binance USDT/NGN, Sep 2020 – Mar 2024) | – | Exchange-rate unification moves the denominator, as in Argentina; no data downloaded; no dated source opened. Likely excluded now |

## Subtasks
- [ ] S1 — Eligibility cards for Ukraine, Argentina and the EEA, with opened primary sources
- [ ] S2 — Prior-exposure inventory for all five cases
- [ ] S3 — Short dispositions for Russia and Nigeria (why excluded now, or what would qualify them)
- [ ] S4 — Team gate: for each case, go to stage 2 (protocol lock), exploratory only, boundary case, or excluded. Recorded
  in the decision log with the reason. The freeze decision (P4-03) also says whether stages 2–3 may run before submission

## Success criteria
- [ ] One card per qualified candidate, every date and rule with an opened source
- [ ] Prior exposure classified for every case
- [ ] Every case has a recorded disposition, exclusions included

## Outputs
- `results/tables/P3-22_eligibility.md` (cards, inventory, dispositions); new rows in `docs/sources.md`

## Handoff
- **State:** task created 3 Nov from the second agent's review (improvements log, 2 Nov) and the agent's response (3 Nov
  entry). Nothing done.
- **Next step:** S1 for Ukraine: open the NBU text of Resolution No. 90 (10 Aug 2026) and the 1 Sep bank FX-position rule.
- **Open questions:** team: owner; whether stages 2–3 may run before the submission at all.
- **How to resume:** read the improvements log entries of 2 Nov ("Review of proposed Ukraine / Argentina / EEA
  extension") and 3 Nov; sources X-01–X-03.

## Log
- 2026-11-03, agent for Renzo: created (stage 1 only), at Renzo's request after the second agent's review.

## Result
<!-- fill when done -->
