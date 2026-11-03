---
id: P5-01
title: Deck v1 (pt-BR)
phase: P5
status: paused
owner: Economist
working: -
due: 2026-11-05
depends: P4-03
---

## Goal
Full deck draft following `docs/02-dolar-cripto.md` §9 and the definition of done in `prompt.md` §8, including the 'Lições de 2025' slide.

## Subtasks
- [x] S1: Definir estrutura, narrativa e layout dos slides conforme `docs/02-dolar-cripto.md` §9, `prompt.md` §8 e o protótipo `notebooks/p5_07_story.ipynb` (`P5-07`). — done: Felipe, 2026-11-02
- [x] S2: Redigir os slides 1 a 7 (Capa/Pergunta, Quatro Hipóteses $H_0$–$H_3$, Dados e Piso de Ruído, Seis Anos e 5 Quebras Cegas, Salto em 3 Corretoras + BTC + Queda de −78% nas Importações de Cripto, O Ofício de 23/jun com 10 Fontes Abertas + 8 Normas por Aviso Prévio, 13 Eventos vs 1.073 Datas Limpas). — done: Felipe, 2026-11-02
- [x] S3: Redigir os slides 8 a 14 (Controle Sintético e Países com Controle Cambial, Pico de 1 Mês vs Pós-Pico Não Significativo $p = 0,24$, Custo em R$ por US$ 100k + R$ 106,1 mi / R$ 145,3 mi Movidos mantendo Opções C e A abertas para a equipe, Fim de Semana do SVB e 11 Quedas com Fontes `DP-01`–`DP-10`, Monitor CUSUM + Previsão Datada para Res. BCB 584 em 01/jan/2027, Lições de 2025, Placar de Hipóteses e Limites). — done: Felipe, 2026-11-02
- [x] S5: Cortar para 10 slides conforme `docs/deck-plan-10-slides.md`; material movido para o Anexo F; registro em `docs/deck-changes-2026-11-02.md`. — done: Renzo (agent), 2026-11-02
- [ ] S4: Diagramação visual final e compilação em PDF após o congelamento oficial de P4-03 na quarta-feira.

## Success criteria
- [x] Every slide's number links to a frozen finding
- [x] One idea per slide
- [x] headline charts readable in 10 seconds
- [x] Definition-of-done items drafted

## Outputs
- `deck/deck_v1_ptbr.md` (10 slides em pt-BR, 2/nov; a versão de 14 slides está em `1bce097`)
- `deck/qa_ptbr.md` (perguntas difíceis para o ensaio); `docs/deck-changes-2026-11-02.md` (registro das mudanças)
- `deck/deck_v1_ptbr.pdf` (geração programada para S4 após freeze de P4-03)

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** `deck/deck_v1_ptbr.md` now has **10 slides** (S5, Renzo's agent, 2 Nov, at Renzo's request), built from
  `docs/deck-plan-10-slides.md`. Every change, the two deviations from the plan (slide 5 title "entre as oito regras
  testadas"; no p-value on the money slide) and the moved material are listed in `docs/deck-changes-2026-11-02.md`.
  The annex has a new Anexo F (moved material, F-029 inference, Res. 574 note) and a 10-slide D.2 matrix.
  `deck/deck_apresentacao.html` rebuilt (10 slides). Rehearsal sheet: `deck/qa_ptbr.md`. The 14-slide version:
  `git show 1bce097:deck/deck_v1_ptbr.md`.
- **Next step:** Felipe reviews the 10 slides against `docs/deck-changes-2026-11-02.md` and accepts or reverses each
  change; the team confirms Option A (bank-route table in Annex B.5) and decides P3-16 S1 (Res. 574).
- **Open questions:** F-015 (R$ 5,052, slides 1 and 9) and F-029 (slides 4 and 5) are still `exploratory`; four
  figures are to be drawn in P5-02 (slides 2, 3, 4, 9; list in the change doc).
- **How to resume:** edit `deck/deck_v1_ptbr.md` (keep the `<!-- SLIDE N -->`, `## Slide N — `, `- **Legenda (10
  segundos):**`, `- **Notas:**` markers the build reads; table separators without `:`), then run
  `.venv/bin/python scripts/build_deck_html.py`. S4 (layout and PDF) after the freeze (P4-03).

## Log
- 2026-11-02, agent for Renzo: Renzo takes S5 ("update the slides yourself, apply the plan, keep a doc"): deck cut to 10 slides, Anexo F, Q&A sheet, P3-12 figure title reworded, HTML rebuilt; change record `docs/deck-changes-2026-11-02.md`; status paused for Felipe's review. `working: -`.
- 2026-11-02, Felipe: Integrados os achados confirmados `F-023` a `F-027` (`P3-10` a `P3-14`) nos Slides 5, 6, 10 e 12 de `deck/deck_v1_ptbr.md` (`P3-10_imports.png`, `P3-12_rules.png`, R$ 106,1 mi / R$ 145,3 mi movidos no pico, e previsão datada `393a14a` para a Res. BCB 584 em 01/jan/2027). `working: -`.
- 2026-11-02, Felipe: Reconstruído `deck/deck_v1_ptbr.md` (14 slides mapeados às 15 seções de `notebooks/p5_07_story.ipynb`) incorporando todas as revisões de 02/nov: pico de 1 mês como único efeito medido, pós-pico não significativo ($p_{\text{placebo}} = 0,24$), $p$-valores de placebo apenas, enquadramento neutro (`docs/02-dolar-cripto.md` §10), fontes abertas para depegs (`DP-01`–`DP-10`) e tarifas (`R-01`–`R-07`), e Opções C e A abertas no Slide 10. `working: Felipe`.
- 2026-11-02, agent for Felipe: Felipe takes the deck rewrite after the 2 Nov reviews: rebuild on the P5-07 notebook flow (deck prototype), spike = measured effect, after-spike level reported as not shown (p = 0.24), placebo p only, sources/framing rules.
- 2026-11-02, agent for Renzo (note for Felipe): sources fixed (docs/sources.md). In the deck, market events M-01–M-04 coincide with breaks, they do not explain them; the July fade is unexplained (P2-02 re-run); the 23 Jun notice can now cite two independent accounts plus the BCB's LAI answer (E-05).
- 2026-11-02, Felipe: Estruturadas as sub-tarefas S1 a S4; elaborada a primeira versão de `deck/deck_v1_ptbr.md`.
- 2026-11-03, agent for Renzo: deck v2 generated next to v1 (`deck/deck_v2_ptbr.md`, `deck/deck_v2_apresentacao.html`) from `docs/deck-proposal-2026-11-03.md` (slides 1, 9, 10; slide 8 line not applied); v1 untouched except its HTML rebuilt after two builder fixes (R$/US$ read as math; no bold/code in table cells). Felipe chooses v1 or v2.

## Result
2/nov (Renzo's agent): deck cortado para 10 slides (`docs/deck-changes-2026-11-02.md`). Antes: apresentação completa em português (`deck/deck_v1_ptbr.md`, 14 slides) alinhada ao protótipo `notebooks/p5_07_story.ipynb` (`P5-07`), às regras de enquadramento e fontes abertas (`prompt.md` §5–§6, `docs/02-dolar-cripto.md` §10) e a todos os achados (`F-001` a `F-027`).
