---
id: P5-01
title: Deck v1 (pt-BR)
phase: P5
status: doing
owner: Economist
working: Felipe
due: 2026-11-05
depends: P4-03
---

## Goal
Full deck draft following `docs/02-dolar-cripto.md` §9 and the definition of done in `prompt.md` §8, including the 'Lições de 2025' slide.

## Subtasks
- [x] S1: Definir estrutura, narrativa e layout dos slides conforme `docs/02-dolar-cripto.md` §9, `prompt.md` §8 e o protótipo `notebooks/p5_07_story.ipynb` (`P5-07`). — done: Felipe, 2026-11-02
- [x] S2: Redigir os slides 1 a 7 (Capa/Pergunta, Quatro Hipóteses $H_0$–$H_3$, Dados e Piso de Ruído, Seis Anos e 5 Quebras Cegas, Salto em 3 Corretoras + BTC, O Ofício de 23/jun com 3 fontes independentes, 13 Eventos vs 1.073 Datas Limpas). — done: Felipe, 2026-11-02
- [x] S3: Redigir os slides 8 a 14 (Controle Sintético e Países com Controle Cambial, Pico de 1 Mês vs Pós-Pico Não Significativo $p = 0,24$, Custo em R$ por US$ 100k mantendo Opções C e A abertas para a equipe, Fim de Semana do SVB e 11 Quedas com Fontes `DP-01`–`DP-10`, Monitor CUSUM, Lições de 2025, Placar de Hipóteses e Limites). — done: Felipe, 2026-11-02
- [ ] S4: Diagramação visual final e compilação em PDF após o congelamento oficial de P4-03 na quarta-feira.

## Success criteria
- [x] Every slide's number links to a frozen finding
- [x] One idea per slide
- [x] headline charts readable in 10 seconds
- [x] Definition-of-done items drafted

## Outputs
- `deck/deck_v1_ptbr.md` (rascunho completo dos 14 slides em pt-BR mapeados às 15 seções de `notebooks/p5_07_story.ipynb`)
- `deck/deck_v1_ptbr.pdf` (geração programada para S4 após freeze de P4-03)

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** `deck/deck_v1_ptbr.md` reconstruído em 14 slides seguindo diretamente o fluxo de 15 seções de `notebooks/p5_07_story.ipynb` (`P5-07`) e incorporando integralmente as correções de revisão de 02/nov:
  1. O pico agudo de 1 mês (+93,9 bps = R$ 5.052 por US$ 100 mil; +73,7 a +128,3 bps em 22 variantes) é apresentado como o único efeito medido, enquanto o nível pós-22/jul (+11,5 a +19,3 bps; $p_{\text{placebo}} = 0,24$) é reportado honestamente no Slide 9 como não distinguível de oscilação ordinária.
  2. O arrefecimento de 22/jul é apresentado como **não explicado** (sem evento em $\pm 5$ dias úteis), os eventos `M-01`–`M-04` **coincidem com** quebras sem provar causa, e o aumento de 6× no volume da Foxbit (`F-008`) permanece com causa em aberto (citando tanto a parceria NovaDAX `M-04` quanto o relançamento institucional Foxbit Infra `M-05`).
  3. No Slide 10 (`P3-01`), o destaque principal é o custo do ofício (R$ 5.052 por US$ 100k no pico), e **ambas as opções de apresentação da comparação institucional foram mantidas prontas para decisão da equipe** (Opção C: bloco compacto neutro no próprio Slide 10 com parâmetros validados `R-01`–`R-07` e 4 ressalvas de não-equivalência; Opção A: manter apenas o custo do ofício no slide e remeter a tabela completa para o Anexo B.5).
- **Next step:** Decisão conjunta da equipe entre Opção C e Opção A no Slide 10; após o freeze de `P4-03`, executar S4 (diagramação final e exportação em PDF).
- **Open questions:** Escolha da equipe entre Opção C e Opção A para o Slide 10.
- **How to resume:** Revisar o Slide 10 de `deck/deck_v1_ptbr.md` com o time antes do freeze de quarta-feira (04/nov).

## Log
- 2026-11-02, Felipe: Reconstruído `deck/deck_v1_ptbr.md` (14 slides mapeados às 15 seções de `notebooks/p5_07_story.ipynb`) incorporando todas as revisões de 02/nov: pico de 1 mês como único efeito medido, pós-pico não significativo ($p_{\text{placebo}} = 0,24$), $p$-valores de placebo apenas, enquadramento neutro (`docs/02-dolar-cripto.md` §10), fontes abertas para depegs (`DP-01`–`DP-10`) e tarifas (`R-01`–`R-07`), e Opções C e A abertas no Slide 10. `working: Felipe`.
- 2026-11-02, agent for Felipe: Felipe takes the deck rewrite after the 2 Nov reviews: rebuild on the P5-07 notebook flow (deck prototype), spike = measured effect, after-spike level reported as not shown (p = 0.24), placebo p only, sources/framing rules.
- 2026-11-02, agent for Renzo (note for Felipe): sources fixed (docs/sources.md). In the deck, market events M-01–M-04 coincide with breaks, they do not explain them; the July fade is unexplained (P2-02 re-run); the 23 Jun notice can now cite two independent accounts plus the BCB's LAI answer (E-05).
- 2026-11-02, Felipe: Estruturadas as sub-tarefas S1 a S4; elaborada a primeira versão de `deck/deck_v1_ptbr.md`.

## Result
Apresentação completa em português (`deck/deck_v1_ptbr.md`, 14 slides) alinhada ao protótipo `notebooks/p5_07_story.ipynb` (`P5-07`), às regras de enquadramento e fontes abertas (`prompt.md` §5–§6, `docs/02-dolar-cripto.md` §10) e aos achados revisados (`F-001` a `F-022`).
