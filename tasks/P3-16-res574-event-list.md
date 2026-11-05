---
id: P3-16
title: Res. BCB 574 (published 22 Jun 2026, one day before the notice) is missing from the event list
phase: P3
status: review
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
- [x] S1 — Decide with the team how Res. 574 enters: a row in the event list and F-026's table (as a published rule, 0
  days to publication, 134 days to the reporting start), or a caveat line. Core findings F-001..F-027 stay unchanged
  until the team re-decides the freeze (decision log, 2 Nov); a re-run goes into a new finding or the History of F-026
  after that decision. — done: Renzo, 2026-11-05 (explicit caveat, no ninth event row)
- [x] S2 — If added: note that a [−20, −1] vs [+1, +20] window around 22 Jun contains the 24 Jun jump, so the event
  study cannot separate 22 Jun from 23 Jun; the separation comes from the daily timing above and the break interval.
  Write the separation rule before any re-run. — not applicable: Renzo chose the caveat path, 2026-11-05; no re-run
- [x] S3 — done: Renzo, 2 Nov (draft; Felipe decides) — One line for the deck or annex. Draft (pt-BR, annex):
  "A Resolução BCB nº 574 (datada de 18/jun no registro do BCB, publicada no DOU em 22/jun) cria a obrigação de
  reportar operações com ativos virtuais realizadas a partir de 3/nov/2026; não restringe operações de junho. No dia
  seguinte à data de registro, o prêmio subiu 38 bps (de −4,7 para 32,9 bps, 18→19/jun; em 2026, antes do ofício, só um
  outro dia subiu tanto), recuou para 23,3 e 24,8 bps em 22 e 23/jun e saltou +131 bps em 24/jun, dia seguinte ao
  ofício. O conteúdo (só reporte) e a diferença de tamanho apontam o ofício como a explicação principal do salto de
  24/jun; a Res. 574 pode ter movido o prêmio em dezenas de bps, e o teste de evento não separa as duas datas."
  (Corrected 2 Nov: the first draft said the premium "não se moveu entre 19 e 23/jun", which left out 18 → 19 Jun; F-029.)
- [x] S4 — Verify E-11 and the price dates, then make the deck/annex caveat explicit and prepare independent Claude review. — done: Codex for Renzo, 2026-11-05

## Success criteria
- [x] Res. 574 appears as an explicit caveat, with source E-11
- [x] The deck and annex explain why the notice is the better hypothesis for the 24 Jun jump while neither rule's separate causal effect is identified

## Outputs
- Caveat in `findings/F-026-which-rules-matter.md`, `deck/annex_v1_ptbr.md`, and slide 5 of both deck drafts; no event row or re-estimation
- Independent review instructions: `docs/agent-prompt-P3-16-review.md`

## Handoff
- **State:** Caveat route implemented; official E-11 and price dates checked. Frozen eight-rule results unchanged. Awaiting independent Claude review before done.
- **Next step:** Claude reviews `docs/agent-prompt-P3-16-review.md`; Felipe checks final slide wording as deck owner.
- **Open questions:** whether any other rule was published between 15 and 30 Jun 2026; nobody has searched the BCB
  register for that window systematically.
- **How to resume:** read E-11 and E-05.10 in `docs/sources.md`; F-026; F-022 (break intervals).

## Log
- 2026-11-05 01:25 (Brasília), agent for Renzo (Claude, independent review per `docs/agent-prompt-P3-16-review.md`): **pass.**
  E-11 matches the BCB text (register 18/6/2026 18:01; "realizadas a partir de 3 de novembro de 2026"; "entra em vigor na
  data de sua publicação"); no draft calls it a June ban. Premium 18, 19, 22, 23, 24 Jun = −4.75, 32.92, 23.29, 24.84,
  155.40 bps; one-day changes +37.7 and +130.6 reproduce. Slide 5 (both drafts), annex F.1 and F-026 word the notice as
  the better hypothesis, state the overlapping windows, and claim no ninth estimate; `ce3ad79` changed no event list,
  P3-12 output or script. F-026 is frozen and the change is a disclosed caveat in its History: acceptable. Note: the BRLA
  route (F-037) also rose on 18→19 Jun (+46 bps), so that day's move was not Binance-only. Felipe owns the final wording.
- 2026-11-05, Codex for Renzo: checked E-11 against the official BCB text and the daily premium (18 Jun −4.75; 19 Jun 32.92; 22 Jun 23.29; 23 Jun 24.84; 24 Jun 155.40 bps). Added explicit caveats to F-026, annex, and both deck drafts; no event row, script change, or estimate. Sent to Claude review through the task handoff.
- 2026-11-05, Renzo + Codex: Renzo chose the caveat path for P3-16; Codex takes S4 and will request an independent Claude review. The frozen eight-rule calculation is retained.
- 2026-11-02, agent for Renzo: S3 draft corrected: +37.7 bps on 18 → 19 Jun (F-029) added; the first draft started the window a day late
- 2026-11-02, agent for Renzo: S3 drafted (caveat by content and timing, after a second agent's review)
- 2026-11-02, agent for Renzo: created (todo) from P3-15

## Result
Res. 574 is a reporting obligation for operations from 3 Nov, registered 18 Jun and published 22 Jun. The 18→19 Jun rise was 37.7 bps, but is not an identified effect. The 23→24 Jun jump was 130.6 bps; its timing and the different content favor the notice as a hypothesis. The event windows overlap, so individual causal effects are not identified. Renzo chose explicit caveats while preserving the frozen eight-rule calculation.
