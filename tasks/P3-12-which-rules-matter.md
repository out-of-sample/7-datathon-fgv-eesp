---
id: P3-12
title: So what (2) - which rules moved the premium (published rules vs the confidential notice)
phase: P3
status: review
owner: Economist
working: -
due: 2026-11-03
depends: P2-03
---

## Goal
One chart and one slide from the P2-03 event table, no new estimation: every dated rule, how it was issued
(decree, published resolution with notice period, confidential notice), the channel it touched, and its
before/after change against the placebo band. The point for regulators: the premium shows which channel
arbitrageurs actually use; only the notice that closed the funds' import route moved it. Plan: `docs/06-so-what.md`,
answer 2.

## Subtasks
- [x] S1 — Add to the event table (or a small side table) how each rule was issued and how much notice the market
  had, each with its source from `docs/sources.md`. — done: Renzo, 2 Nov (`results/tables/P3-12_rules.csv`)
- [x] S2 — Figure `results/figures/P3-12_rules.png`: one row per rule, the change in bps, the 95% placebo band,
  the detection limit (~25–37 bps) marked. — done: Renzo, 2 Nov (band = 2.5–97.5% of the 200 placebo draws, −35 to +38 bps)
- [x] S3 — Slide text (pt-BR) with the two caveats: content and form differ together, so the chart cannot say
  which mattered; "no effect" means "no effect above the detection limit". — done: Renzo, 2 Nov (Result)

## Success criteria
- [x] Every row's issuance type has a source
- [x] Figure uses only numbers from `results/tables/P2-03_event_table.csv`
- [x] Both caveats on the slide

## Outputs
- `scripts/p3_12_rules.py`, `results/tables/P3-12_rules.csv`, `results/figures/P3-12_rules.png`, F-026

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** done, in review (F-026). Eight rules, one row each; only E-05 (confidential, immediate) is outside the
  ordinary-date range; the seven published rules (1–175 days of notice) are inside it. Both caveats are on the figure.
- **Next step:** Felipe (deck owner) checks the figure and the slide text in Result.
- **Open questions:** none.
- **How to resume:** `python scripts/p3_12_rules.py`.

## Log
- 2026-11-02, agent for Renzo: S1–S3 done; F-026; status review.
- 2026-11-02, agent for Renzo: Renzo takes P3-12 (owner Economist; asked by Renzo). Scope: the 8 rules (E-01 to E-06b); market events (E-07, M-01 to M-04) are not rules and stay out. Band = 2.5–97.5% of the 200 P2-03 placebo draws.
- 2026-11-02, agent for Renzo: created (plan `docs/06-so-what.md`).

## Result
Only the confidential, immediate notice moved the premium detectably; the seven published rules stayed within the range of
ordinary dates (F-026, `results/figures/P3-12_rules.png`). Slide text (pt-BR):
Título: "Só o ofício sigiloso moveu o prêmio de forma detectável."
"Testamos as oito regras brasileiras com data. O decreto do IOF, sua suspensão e quatro resoluções do BCB, todas públicas e
quase todas com semanas ou meses de antecedência, ficaram dentro da faixa das datas comuns. Só o ofício de 23/06/2026,
sigiloso e de efeito imediato, saiu dela: +94 pb. O prêmio revela qual regra fechou o canal que os arbitradores de fato
usavam. Ressalvas: forma e conteúdo mudam juntos (o ofício foi também a única regra que fechou o canal dos fundos), e
'sem efeito' quer dizer 'sem efeito acima de ~35 pb'."
