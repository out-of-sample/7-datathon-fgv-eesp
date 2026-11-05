# Independent Claude review — P3-16

Renzo chose an explicit caveat for Resolução BCB 574, leaving the frozen eight-rule event comparison unchanged. Please review the implementation independently before P3-16 is marked done. Start with `prompt.md`, `STATUS.md`, and `tasks/P3-16-res574-event-list.md`.

1. Check E-11 in `docs/sources.md` against the [official BCB text](https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolu%C3%A7%C3%A3o%20BCB&p2=574): BCB register 18 Jun 2026 18:01, DOU 22 Jun, effective on publication, reporting for operations carried out from 3 Nov. Verify that no draft calls it a June trading ban.
2. Independently reproduce `premium_bps` in `data/processed/P1-02_premium_daily.csv` for 18, 19, 22, 23 and 24 Jun: approximately −4.75, 32.92, 23.29, 24.84 and 155.40 bps. Check the +37.7 and +130.6 bps one-day changes. The former follows an unusually low 18 Jun observation and cannot identify a Res. 574 effect.
3. Review slide 5 in `deck/deck_v1_ptbr.md` and `deck/deck_v2_ptbr.md`, `deck/annex_v1_ptbr.md` §F.1, and the added caveat in `findings/F-026-which-rules-matter.md`. Confirm the timing/content argument is described as a hypothesis, the overlapping 20-day windows are explicit, and no independent causal effect or ninth-rule estimate is implied. Check the speaker notes and caption as well as the bullets.
4. Verify `data/processed/P1-04_events_brazil.csv`, the P3-12 result table/figure and scripts were not changed by P3-16; this is a disclosure decision, not a new test. Check `docs/README.md` decision log, task handoff, and dashboard consistency.

Please report concrete corrections with file and line, or record a pass in the task handoff/log and notify Renzo. Felipe owns final deck wording. Open question from the task: no systematic search has yet established whether another BCB rule was published 15–30 Jun; do not imply completeness beyond the eight tested rules.
