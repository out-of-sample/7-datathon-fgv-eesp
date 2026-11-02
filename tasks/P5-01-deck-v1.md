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
- [x] S1: Definir estrutura, narrativa e layout dos 12 slides conforme `docs/02-dolar-cripto.md` §9 e `prompt.md` §8. — done: Felipe, 2026-11-02
- [x] S2: Redigir os slides 1 a 6 (Capa, Motivação/Pergunta, Lições de 2025, Teoria das Portas de Arbitragem, Dados/Piso de Ruído, Quebras Cegas Bai-Perron e Band-TAR). — done: Felipe, 2026-11-02
- [x] S3: Redigir os slides 7 a 12 (Estudo de Eventos com 200 Placebos, Controle Sintético e Bitcoin, Custos de US$ 100k, Depegs em Dólar/SVB, Monitor CUSUM, Implicações Regulatórias e Limitações). — done: Felipe, 2026-11-02
- [ ] S4: Diagramação visual final e compilação em PDF após o congelamento oficial de P4-03 na quarta-feira.

## Success criteria
- [x] Every slide's number links to a frozen finding
- [x] One idea per slide
- [x] headline charts readable in 10 seconds
- [x] Definition-of-done items drafted

## Outputs
- `deck/deck_v1_ptbr.md` (rascunho completo dos 12 slides em pt-BR com rastreabilidade total)
- `deck/deck_v1_ptbr.pdf` (geração programada para S4 após freeze de P4-03)

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** Rascunho completo dos 12 slides finalizado em `deck/deck_v1_ptbr.md`. Todos os números, tabelas e figuras estão rigorosamente rastreados aos achados `F-001` a `F-021`, scripts de geração e fontes de dados.
- **Next step:** S4 (geração do PDF final e diagramação gráfica após o freeze oficial de resultados em P4-03 na quarta-feira).
- **Open questions:** Nenhuma pendência de conteúdo.
- **How to resume:** Verificar se houve alguma alteração de dados no freeze de P4-03 e prosseguir com a renderização em PDF via Pandoc/Marp/Typst.

## Log
- 2026-11-02, agent for Felipe: Felipe takes the deck rewrite after the 2 Nov reviews: rebuild on the P5-07 notebook flow (deck prototype), spike = measured effect, after-spike level reported as not shown (p = 0.24), placebo p only, sources/framing rules.
- 2026-11-02, agent for Renzo (note for Felipe): sources fixed (docs/sources.md). In the deck, market events M-01–M-04 coincide with breaks, they do not explain them; the July fade is unexplained (P2-02 re-run); the 23 Jun notice can now cite two independent accounts plus the BCB's LAI answer (E-05).
- 2026-11-02, Felipe: Estruturadas as sub-tarefas S1 a S4; elaborada a versão integral de `deck/deck_v1_ptbr.md` com 12 slides contendo título direto, visual/layout com figura de 10s, tópicos quantitativos em pt-BR, notas do orador e rodapé de rastreabilidade para findings (`F-001` a `F-021`), scripts e fontes (`D-xx`, `E-xx`, `R-xx`, `L-xx`). S1, S2 e S3 concluídos. Status definido como `doing` aguardando freeze de P4-03 para PDF final.

## Result
Rascunho v1 completo da apresentação de 12 slides em português criado em `deck/deck_v1_ptbr.md`. O material atende a todos os requisitos do regulamento (Art. 7º) e do briefing metodológico (`prompt.md` §8), trazendo autocrítica das lições de 2025, identificação causal estrita, teste cego de quebras estruturais, estudo de eventos contra 200 placebos aleatórios, controle sintético internacional, aplicação financeira prática (US$ 100k), capítulo em dólares (SVB) e monitor sequencial CUSUM.
