---
id: P3-08
title: 2025 subsidy share for the 'Lições de 2025' slide
phase: P3
status: done
owner: CS 3
working: -
due: 2026-11-03
depends: -
---

## Goal
Measure how much of last year's 'risk spread' was token rewards (DeFiLlama apyReward vs apyBase) for the pools used in 2025. One number for one slide. Plan: `docs/03-incentives.md` §3.

## Subtasks
- [x] S1: Query DeFiLlama Yields API and NY Fed SOFR API; freeze data in `data/raw/defillama/` for offline reproducibility — done: Felipe, 2 Nov
- [x] S2: Implement yield decomposition (`apyBase` vs `apyReward`) and spread calculations across pools and subperiods in `scripts/p3_08_subsidy.py`; generate `results/tables/P3-08_subsidy_2025.csv` and `results/figures/P3-08_subsidy_share_2025.png` — done: Felipe, 2 Nov
- [x] S3: Synthesize economic findings in `findings/F-020-subsidy-share-2025.md` with slide text and exact source register lines — done: Felipe, 2 Nov

## Success criteria
- [x] Reward share of the 2025 spread computed from DeFiLlama with pool IDs listed — done: Felipe, 2 Nov
- [x] Finding written — done: Felipe, 2 Nov

## Outputs
- `scripts/p3_08_subsidy.py`
- `data/raw/defillama/aave_v3_usdc.json`
- `data/raw/defillama/aave_v2_usdc.json`
- `data/raw/defillama/compound_v3_usdc.json`
- `data/raw/defillama/compound_v2_usdc.json`
- `data/raw/defillama/sofr.json`
- `data/raw/defillama/pools.json`
- `results/tables/P3-08_subsidy_2025.csv`
- `results/figures/P3-08_subsidy_share_2025.png`
- `findings/F-020-subsidy-share-2025.md`

## Handoff
- **State:** Completed and verified against 2025 Datathon sample window. All scripts, tables, figures, and findings generated and reviewed.
- **Next step:** Teammate review; integrate finding bullet and figure into the "Lições de 2025" slide in the presentation deck.
- **Open questions:** none
- **How to resume:** Run `py scripts/p3_08_subsidy.py` to regenerate outputs. Read `findings/F-020-subsidy-share-2025.md` for complete narrative.

## Log
- 2026-11-03, Jonathan: independent re-run verified; status -> done.
- 2026-11-02, Felipe: Started task P3-08. Identified canonical pools in DeFiLlama and 2025 repo. Downloaded and froze pool charts and NY Fed SOFR rate in `data/raw/defillama/`.
- 2026-11-02, Felipe: Wrote `scripts/p3_08_subsidy.py`, generated `results/tables/P3-08_subsidy_2025.csv` and 4-panel publication figure `results/figures/P3-08_subsidy_share_2025.png`. Documented complete findings in `findings/F-020-subsidy-share-2025.md`. Status moved to `review`.

## Result
Portuguese bullet for the "Lições de 2025" slide:
> **Rendimento orgânico vs. subsídio promocional:** No trabalho de 2025, modelamos o spread DeFi vs SOFR usando o APY bruto como se fosse um prêmio de risco estrutural. Ao decompor as taxas on-chain, descobrimos que **53,6% do spread do Compound V3** (e **37,5% do spread ponderado por TVL**) correspondia a subsídios temporários em tokens de governança (COMP), e não a juros pagos por tomadores. No período de teste de 2025, o spread orgânico real do Compound era inclusive negativo (-8,2 bps). O modelo previa propaganda e incentivos de protocolo, não risco de crédito.
