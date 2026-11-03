---
id: P3-16
title: Res. BCB 574 (published 22 Jun 2026, one day before the notice) is missing from the event list
phase: P3
status: todo
owner: Economist
working: -
due: 2026-11-04
depends: P1-04, P3-12
---

## Goal
While opening sources for P3-15, Renzo's agent found Resolução BCB nº 574/2026 (E-11). It was published in the DOU on
22 Jun 2026, one PTAX day before the 23 Jun notice, and is not in `data/processed/P1-04_events_brazil.csv`. It is a
reporting rule: FX-authorised institutions must report virtual-asset operations carried out from 3 Nov 2026. A juror
who knows it will ask whether it, not the notice, moved the premium. F-026 says "of eight dated rules"; with Res. 574
there are nine.

What is already known (description, not a test): the daily premium (`premium_bps`) was 23.3 bps on 22 Jun, 24.8 bps on
23 Jun and 155.4 bps on 24 Jun 2026. The jump came the day after the notice, not on the day Res. 574 was published.
The break interval under Bai's Theorem 2 starts on 23 Jun (F-022). Res. 574 is dated 18 Jun 2026 18:01 in the BCB
register (E-11); the premium was 32.9 bps on 19 Jun. This favours the notice but does **not** prove Res. 574 had no
effect. Reproduce:
`.venv/bin/python -c "import pandas as pd; d=pd.read_csv('data/processed/P1-02_premium_daily.csv',index_col='date_brt'); print(d.loc['2026-06-19':'2026-06-25','premium_bps'].round(1))"`

## Subtasks
- [ ] S1 — Decide with the team how Res. 574 enters: a row in the event list and F-026's table (as a published rule, 0
  days to publication, 134 days to the reporting start), or a caveat line. Core findings F-001..F-027 stay unchanged
  until the team re-decides the freeze (decision log, 2 Nov); a re-run goes into a new finding or the History of F-026
  after that decision.
- [ ] S2 — If added: note that a [−20, −1] vs [+1, +20] window around 22 Jun contains the 24 Jun jump, so the event
  study cannot separate 22 Jun from 23 Jun; the separation comes from the daily timing above and the break interval.
  Write the separation rule before any re-run.
- [x] S3 — done: Renzo, 2 Nov (draft; Felipe decides) — One line for the deck or annex. Draft (pt-BR, annex):
  "A Resolução BCB nº 574 (datada de 18/jun no registro do BCB, publicada no DOU em 22/jun) cria a obrigação de
  reportar operações com ativos virtuais realizadas a partir de 3/nov/2026; não restringe operações de junho. No dia
  seguinte à data de registro, o prêmio subiu 38 bps (de −4,7 para 32,9 bps, 18→19/jun; em 2026, antes do ofício, só um
  outro dia subiu tanto), recuou para 23,3 e 24,8 bps em 22 e 23/jun e saltou +131 bps em 24/jun, dia seguinte ao
  ofício. O conteúdo (só reporte) e a diferença de tamanho apontam o ofício como a explicação principal do salto de
  24/jun; a Res. 574 pode ter movido o prêmio em dezenas de bps, e o teste de evento não separa as duas datas."
  (Corrected 2 Nov: the first draft said the premium "não se moveu entre 19 e 23/jun", which left out 18 → 19 Jun; F-029.)

## Success criteria
- [ ] Res. 574 appears in the event list or as an explicit caveat, with source E-11
- [ ] The deck or annex says why the 24 Jun jump is attributed to the 23 Jun notice and not to Res. 574

## Outputs
- `data/processed/P1-04_events_brazil.csv` row or a caveat in F-026 / the annex

## Handoff
- **State:** S3 drafted (annex sentence above, content + timing, not "ruled out"). S1 (event list or caveat) and S2
  wait for the team. Source opened and registered (E-11 in `docs/sources.md`, 2 Nov 2026).
- **Next step:** S1 (team call).
- **Open questions:** whether any other rule was published between 15 and 30 Jun 2026; nobody has searched the BCB
  register for that window systematically.
- **How to resume:** read E-11 and E-05.10 in `docs/sources.md`; F-026; F-022 (break intervals).

## Log
- 2026-11-02, agent for Renzo: S3 draft corrected: +37.7 bps on 18 → 19 Jun (F-029) added; the first draft started the window a day late
- 2026-11-02, agent for Renzo: S3 drafted (caveat by content and timing, after a second agent's review)
- 2026-11-02, agent for Renzo: created (todo) from P3-15

## Result
