---
id: P5-05
title: Annex: sources, event table, AI-use disclosure
phase: P5
status: doing
owner: Economist
working: -
due: 2026-11-07
depends: P5-01
---

## Goal
Annex slides: source register, event table with links, robustness tables, and a plain description of how AI agents were used (including extension A/B if done).

## Subtasks
- [x] S1: Elaborar o Anexo A com a tabela consolidada dos 13 eventos brasileiros (`results/tables/P2-03_event_table.csv` e `results/tables/P3-12_rule_attributes.csv`), exibindo exclusivamente $p$-valores de placebos (1.073 datas limpas e 200 sorteios), datas corrigidas (`M-02` 2024-08-13, `M-03` 2025-06-27), enquadramento "coincide com" para `M-01`–`M-04` e links primários abertos. — done: Felipe, 2026-11-02
- [x] S2: Elaborar o Anexo B com a bateria completa de robustez (`P4-01_robustness.csv`, incluindo as linhas pós-pico com $p_{\text{placebo}} = 0,239$ e $0,140$, 3 corretoras em 20d e 16d, ICs homocedásticos e heterocedásticos de Bai 1997, 6 especificações do controle sintético, **Anexo B.5 com a tabela completa de 17 linhas de `P3-01_route_costs.csv` + `P3-11`/`P3-13` para a Opção A**, **Anexo B.6 com os 12 casos de depeg com fontes `DP-01`–`DP-10` + Band-TAR** e **Anexo B.7 com a síntese quantitativa do plano *"So what?"* `P3-10`–`P3-14`**). — done: Felipe, 2026-11-02
- [x] S3: Elaborar o Anexo C com o registro auditado de dados (`D-01`–`D-17`), legislação e tarifas (`E-05.1`–`E-05.10`, `E-10`, `R-01`, `R-01b`, `R-02`–`R-07`, `M-05`), casos de depeg (`DP-01`–`DP-10`) e literatura (`L-01`–`L-08`), com URLs testadas (HTTP 200) e zero tags `[verify]`. — done: Felipe, 2026-11-02
- [x] S4: Elaborar o Anexo D (mapa `.py` $\to$ `.txt` incluindo `p3_10`–`p3_14` e matriz de rastreabilidade entre os 14 slides de `deck_v1_ptbr.md` e as 15 seções de `notebooks/p5_07_story.ipynb`) e Anexo E (declaração transparente sobre uso de agentes de IA e auditoria cruzada). — done: Felipe, 2026-11-02

## Success criteria
- [x] Source register complete (no [verify] left in anything cited)
- [x] AI-use disclosure slide written

## Outputs
- `deck/annex_v1_ptbr.md` (documento suplementar oficial com Anexos A, B, C, D e E)

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** `deck/annex_v1_ptbr.md` atualizado integralmente para refletir as revisões de 02/nov e os 5 achados confirmados do plano *"So what?"* (`F-023` a `F-027`):
  - **Anexo A:** sincronizado com `results/tables/P2-03_event_table.csv` e `results/tables/P3-12_rule_attributes.csv` (`F-026`, modo de emissão e dias de aviso prévio; `E-10` Res. BCB 580/2026; 10 fontes abertas `E-05.1`–`E-05.10` em `F-023`).
  - **Anexo B:** inclui B.1–B.4, **B.5 (tabela completa de 17 linhas de `P3-01` + agregados de `P3-11` / `F-025` e decomposição de 9,1 bps de `P3-13` / `F-027`)**, **B.6 (12 casos de depeg com fontes `DP-01`–`DP-10` + Band-TAR)** e **B.7 (síntese quantitativa do plano *"So what?"*: `P3-10` a `P3-14`, `F-023` a `F-027`)**.
  - **Anexo C:** todas as URLs verificadas (incluindo `D-16` BCB Setor Externo, `D-17` SGS 432 Selic, `E-05.1`–`E-05.10` com art. 15-B, III do Decreto 6.306/2007 aberto no Planalto, `E-10` Res. BCB 580/2026, `R-01`–`R-07`, `M-05` e `DP-01`–`DP-10`; zero tags `[verify]`).
  - **Anexo D e E:** mapa `.py` $\to$ `.txt` expandido para incluir `p3_10`–`p3_14`, matriz de rastreabilidade dos 14 slides / 15 seções do notebook e divulgação transparente de IA atualizada.
- **Next step:** Aguardar freeze oficial de resultados em `P4-03` para consolidação conjunta no PDF final com `P5-01`.
- **Open questions:** Nenhuma.
- **How to resume:** Utilizar `deck/annex_v1_ptbr.md` como apêndice formal no material da submissão final.

## Log
- 2026-11-02, agent for Renzo (P5-01 S5): added Anexo F (material moved off the slides: F-029 inference and window contents, Res. 574 note, method note with L-09, countries, SVB, monitor, Lições de 2025, hypothesis scoreboard, routes) and rewrote the D.2 matrix for the 10-slide deck; C.5 gains L-09. See `docs/deck-changes-2026-11-02.md`.
- 2026-11-02, Felipe: Integrados `F-023` a `F-027` (`P3-10` a `P3-14`) nos Anexos A, B.5, B.7, C (`D-16`, `D-17`, `E-05.1`–`E-05.10`, `E-10`), D e E de `deck/annex_v1_ptbr.md`; verificado art. 15-B, III do Decreto 6.306/2007 no Planalto (zero tags `[verify]` em `docs/sources.md`). `working: -`.
- 2026-11-02, Felipe: Atualizado `deck/annex_v1_ptbr.md` (Anexos A–E) com $p$-valores de placebos apenas, datas corrigidas de `P2-03`, tabela completa de `P3-01` (Anexo B.5, Opção A), tabela completa de depegs com fontes `DP-01`–`DP-10` (Anexo B.6) e URLs auditadas (Anexo C). `working: Felipe`.
- 2026-11-02, agent for Felipe: Felipe takes the annex update to match revised F-015…F-022 and the fixed sources.
- 2026-11-02, agent for Renzo: correction: the M-03 row's p = 0.014 is the parametric p (placebo p 0.26). Show only placebo p-values in the annex (P2-03 review).
- 2026-11-02, agent for Renzo: four broken event links in `deck/annex_v1_ptbr.md` replaced with the opened sources (docs/sources.md M-01–M-04). Event-study rows for M-02 (20 Aug) and M-03 (20 Jun announcement) rest on unsourced dates; update after the P2-03 re-run. Use "coincide com" rather than "explica" for M-01–M-04.
- 2026-11-02, Felipe: Criada a primeira versão de `deck/annex_v1_ptbr.md`.

## Result
Documento de anexos (`deck/annex_v1_ptbr.md`) sincronizado com todos os achados (`F-001` a `F-027`), tabelas de `results/tables/` e fontes primárias abertas em `docs/sources.md`.
