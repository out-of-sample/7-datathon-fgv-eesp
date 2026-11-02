---
id: P5-01
title: Deck v1 (pt-BR)
phase: P5
status: doing
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
- **State:** `deck/deck_v1_ptbr.md` reconstruído em 14 slides seguindo diretamente o fluxo de 15 seções de `notebooks/p5_07_story.ipynb` (`P5-07`) e incorporando integralmente as revisões de 02/nov **e os 5 achados do plano *"So what?"* (`F-023` a `F-027`, confirmados após revisão por pares de `P3-10` a `P3-14`)**:
  1. **Slide 5 (`F-023`, `F-024`):** 10 fontes abertas sobre o ofício de 23/jun (`E-05.1`–`E-05.10`, incluindo Cointelegraph Brasil 24/jun, Exame 25/jun e resposta LAI do BCB), confirmação das cotações da imprensa (+56 e +69 bps no mesmo dia) e queda de **−78%** nas compras externas líquidas de criptoativos/stablecoins no BCB em julho/2026 (de US$ 2.542 mi para US$ 572 mi; $p = 0,022$, permanecendo em 32% em ago–set, figura `P3-10_imports.png`).
  2. **Slide 6 (`F-026`):** das 8 normas brasileiras datadas, apenas o ofício reservado e imediato de 23/jun (+93,9 bps) moveu o prêmio fora da banda de 95% de datas comuns ($[-35,0; +37,6]$ bps), enquanto todas as 7 normas publicadas com 1 a 175 dias de vacatio legis ficaram dentro do ruído (figura `P3-12_rules.png`).
  3. **Slide 10 (`F-015`, `F-025`):** além do custo unitário de R$ 5.052 por US$ 100 mil (+93,9 bps), incorpora o volume financeiro agregado movido nas 4 semanas do pico (**R$ 106,1 milhões** na Binance sobre US$ 2,10 bi; **R$ 145,3 milhões** nas 3 corretoras sobre US$ 2,88 bi; equivalente tarifário de 94,9 bps; $p_{\text{placebo}} = 0,005$), mantendo **ambas as opções de apresentação da comparação institucional abertas para decisão da equipe** (Opção C no Slide 10 vs Opção A no Anexo B.5).
  4. **Slide 12 (`F-027`):** previsão datada e registrada em git (`393a14a`, 02/nov/2026) para a retenção cautelar de 24h da Res. BCB 584 em 01/jan/2027 (~9,1 bps de custo para quem já detém USDT em transferência de saída; variação prevista dentro de $[-35,0; +37,6]$ bps em 04/jan/2027).
- **Next step:** Decisão conjunta da equipe entre Opção C e Opção A no Slide 10 (e entre destacar R$ 106,1 mi Binance ou R$ 145,3 mi 3 corretoras); após o freeze de `P4-03`, executar S4 (diagramação final e exportação em PDF).
- **Open questions:** Escolha da equipe entre Opção C e Opção A para o Slide 10.
- **How to resume:** Revisar o Slide 10 de `deck/deck_v1_ptbr.md` com o time antes do freeze de quarta-feira (04/nov).

## Log
- 2026-11-02, Felipe: Integrados os achados confirmados `F-023` a `F-027` (`P3-10` a `P3-14`) nos Slides 5, 6, 10 e 12 de `deck/deck_v1_ptbr.md` (`P3-10_imports.png`, `P3-12_rules.png`, R$ 106,1 mi / R$ 145,3 mi movidos no pico, e previsão datada `393a14a` para a Res. BCB 584 em 01/jan/2027). `working: -`.
- 2026-11-02, Felipe: Reconstruído `deck/deck_v1_ptbr.md` (14 slides mapeados às 15 seções de `notebooks/p5_07_story.ipynb`) incorporando todas as revisões de 02/nov: pico de 1 mês como único efeito medido, pós-pico não significativo ($p_{\text{placebo}} = 0,24$), $p$-valores de placebo apenas, enquadramento neutro (`docs/02-dolar-cripto.md` §10), fontes abertas para depegs (`DP-01`–`DP-10`) e tarifas (`R-01`–`R-07`), e Opções C e A abertas no Slide 10. `working: Felipe`.
- 2026-11-02, agent for Felipe: Felipe takes the deck rewrite after the 2 Nov reviews: rebuild on the P5-07 notebook flow (deck prototype), spike = measured effect, after-spike level reported as not shown (p = 0.24), placebo p only, sources/framing rules.
- 2026-11-02, agent for Renzo (note for Felipe): sources fixed (docs/sources.md). In the deck, market events M-01–M-04 coincide with breaks, they do not explain them; the July fade is unexplained (P2-02 re-run); the 23 Jun notice can now cite two independent accounts plus the BCB's LAI answer (E-05).
- 2026-11-02, Felipe: Estruturadas as sub-tarefas S1 a S4; elaborada a primeira versão de `deck/deck_v1_ptbr.md`.

## Result
Apresentação completa em português (`deck/deck_v1_ptbr.md`, 14 slides) alinhada ao protótipo `notebooks/p5_07_story.ipynb` (`P5-07`), às regras de enquadramento e fontes abertas (`prompt.md` §5–§6, `docs/02-dolar-cripto.md` §10) e a todos os achados (`F-001` a `F-027`).
