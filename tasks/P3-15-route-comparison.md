---
id: P3-15
title: Why +94 bps and not +350 - which routes are comparable (clarification for the deck)
phase: P3
status: todo
owner: Economist
working: -
due: 2026-11-04
depends: P3-01, P3-10
---

## Goal
The deck sets two numbers next to each other: the premium rose by +94 bps after the 23 Jun 2026 notice (F-016), and the
closed funds' route paid 0% IOF against 3.5% (350 bps) for ordinary transfers abroad (Slide 5, E-05.10, R-02). A juror
will ask why the premium did not rise by 350 bps. This task maps the legally distinct routes and says what each number
measures. It does **not** promise to find the marginal route; "we cannot identify the marginal route" is an allowed
result.

Why the comparison is not direct: +94 bps is a *change in a market price*; 350 bps is the IOF on *one legal kind of bank
transfer abroad*. F-015 already says bank FX and buying USDT in Brazil are not operationally equivalent.

## Subtasks
- [ ] S1 — Route map. One row per route that can bring dollars or USDT into Brazil, before and after 23 Jun 2026: funds'
  FX import (IOF 0%, Decreto 6.306/2007 art. 15-B III; closed 23 Jun); ordinary availability abroad (3.5% from 23 May
  2025); investment remittance (1.1%); goods import (0%; not usable for crypto, Res. BCB 561 / eFX); arbitrage inside
  exchange order books (allowed 26 Jun, E-05.5); a person or firm moving USDT bought abroad to a Brazilian exchange.
  Columns: who can use it, cost (IOF + spread, from F-015 / R-01 / R-02), does it add USDT supply in Brazil (yes / no /
  unknown), status before / after the notice, source ID or `[not opened]`. Every cost from an opened source (`prompt.md` §6).
- [ ] S2 — What the numbers can say. Write before comparing: (a) if exactly one open route's cost over the pre-notice
  premium is close to the spike (+94 bps) and nothing cheaper was open, call it a *candidate* marginal route (compatible,
  not shown); (b) otherwise write "we cannot identify the marginal route". Then apply the rule to the S1 table.
- [ ] S3 — The July-fade bound. Check this statement against F-022 and F-024 and keep it only if it holds: imports stayed
  at about a third of their Jan–May level in Aug–Sep (F-024), so the funds' channel stayed mostly closed, yet the premium
  after 22 Jul is not distinguishable from ordinary drift (+11.5 to +19.3 bps over the pre-notice level, placebo p = 0.24,
  F-022). So after July no route costing ~350 bps can have been the one setting the price: either a cheap route supplied
  USDT, or demand fell. The data do not say which.
- [ ] S4 — Finding (next free F-number) with the S2 outcome and S3, and two pt-BR sentences for Felipe: one for Slide 1
  ("até o custo do próximo canal disponível") and one for Slide 5 (the 0% vs 3.5% line).

## Success criteria
- [ ] `results/tables/P3-15_routes.md` exists; every cost cites an opened source or is marked `[not opened]`
- [ ] The S2 rule is in this file (commit) before S1's costs are compared with +94 bps
- [ ] A finding states outcome (a) or (b) and the S3 bound, with the commands or files that give each number

## Outputs
- `results/tables/P3-15_routes.md` (no script expected: numbers come from F-015, F-016, F-022, F-024)
- `findings/F-0NN-route-comparison.md`

## Handoff
- **State:** not started. Written 2 Nov 2026 after the deck-language review (`docs/deck-notes-2026-11-02.md`).
- **Next step:** S2 first (commit the rule), then S1.
- **Open questions:** whether the order-book arbitrage of 26 Jun adds any USDT to Brazil or only moves it between books
  (Cointelegraph 26 Jun, E-05.5, says it was allowed; it does not say how USDT entered). Felipe owns P3-01's route costs.
- **How to resume:** read F-015 (route table), `docs/sources.md` rows E-05.5, E-05.10, R-01, R-02; F-022; F-024.

## Log
- 2026-11-02, agent for Renzo: created (todo) after the review of the "beyond a period study" proposals

## Result
