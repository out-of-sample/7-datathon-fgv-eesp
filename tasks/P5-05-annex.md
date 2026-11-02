---
id: P5-05
title: Annex: sources, event table, AI-use disclosure
phase: P5
status: doing
owner: Economist
working: Felipe
due: 2026-11-07
depends: P5-01
---

## Goal
Annex slides: source register, event table with links, robustness tables, and a plain description of how AI agents were used (including extension A/B if done).

## Subtasks
- [x] S1: Elaborar o Anexo A com a tabela consolidada de todos os 13 eventos regulatórios brasileiros, janelas de estudo de eventos, erros HAC, p-valores de 200 placebos e fontes primárias/secundárias. — done: Felipe, 2026-11-02
- [x] S2: Elaborar o Anexo B com a bateria completa de robustez (sensibilidade a janelas $\pm 5$ a $\pm 40$ dias, confirmação nas 3 corretoras nacionais, teste de Bai-Perron com métricas alternativas e controle sintético). — done: Felipe, 2026-11-02
- [x] S3: Elaborar o Anexo C com o registro auditado de dados, legislação, tarifas bancárias e literatura, sem nenhuma tag `[verify]` pendente. — done: Felipe, 2026-11-02
- [x] S4: Elaborar o Anexo D (reprodutibilidade e mapa `.py` $\to$ `.txt` com matriz de rastreabilidade ponta a ponta) e Anexo E (declaração transparente e ética sobre governança e uso de agentes de IA). — done: Felipe, 2026-11-02

## Success criteria
- [x] Source register complete (no [verify] left in anything cited)
- [x] AI-use disclosure slide written

## Outputs
- `deck/annex_v1_ptbr.md` (documento suplementar oficial com Anexos A, B, C, D e E)

## Handoff
<!-- Overwrite at the end of every session, finished or not, so anyone can continue from here. -->
- **State:** Documento suplementar completo redigido em `deck/annex_v1_ptbr.md`, contendo Anexo A (eventos e placebos), Anexo B (robustez), Anexo C (fontes auditadas sem pendências), Anexo D (mapa de reprodutibilidade e rastreabilidade) e Anexo E (declaração ética de uso de IA).
- **Next step:** Aguardar freeze oficial de resultados em P4-03 para consolidação conjunta no PDF final com `P5-01`.
- **Open questions:** Nenhuma.
- **How to resume:** Utilizar os anexos como apêndice formal no material da submissão final.

## Log
- 2026-11-02, agent for Felipe: Felipe takes the annex update to match revised F-015…F-022 and the fixed sources.
- 2026-11-02, agent for Renzo: correction: the M-03 row's p = 0.014 is the parametric p (placebo p 0.26). Show only placebo p-values in the annex (P2-03 review).
- 2026-11-02, agent for Renzo: four broken event links in `deck/annex_v1_ptbr.md` replaced with the opened sources (docs/sources.md M-01–M-04). Event-study rows for M-02 (20 Aug) and M-03 (20 Jun announcement) rest on unsourced dates; update after the P2-03 re-run. Use "coincide com" rather than "explica" for M-01–M-04.
- 2026-11-02, Felipe: Estruturadas as sub-tarefas S1 a S4; criado `deck/annex_v1_ptbr.md` cobrindo detalhadamente os Anexos A, B, C, D e E com rastreabilidade total, links normativos, parâmetros tarifários e governança do uso de IA. Todos os critérios de sucesso atendidos. Status definido como `doing` até o congelamento oficial de P4-03 e compilação do PDF final.

## Result
Documento de anexos finalizado em `deck/annex_v1_ptbr.md`. Fornece transparência metodológica completa, auditabilidade dos scripts, conferência dos eventos regulatórios contra placebos e conformidade com as diretrizes do regulamento do Datathon FGV.
