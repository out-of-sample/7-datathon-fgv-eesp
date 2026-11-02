---
id: F-020
title: Between 37.5% and 53.6% of the 2025 DeFi spread over SOFR was token subsidies, not risk premium
status: exploratory
task: P3-08
date: 2026-11-02
checked_by: -
---

## Claim
Decomposing daily DeFi yields into base borrower interest (`apyBase`) and protocol token incentives (`apyReward`) reveals that **53.6% of Compound V3's spread over SOFR** (and **37.5% of the TVL-weighted Aave/Compound spread**) over the 2023–2025 datathon window was promotional token subsidies (COMP emissions), not structural credit or smart-contract risk premia. In the 2025 test period, Compound V3's organic base spread over SOFR was actually negative (-8.2 bps). Last year's models were predicting promotional marketing subsidies rather than genuine financial risk.

## Evidence
- **Sample Window:** 12 Feb 2023 – 07 Nov 2025 (1,000 calendar days, matching the 2025 Datathon dataset `raw_data/Y.csv`).
  - Train split: 12 Feb 2023 – 21 Apr 2025 (800 days, 80%).
  - Test split: 22 Apr 2025 – 07 Nov 2025 (200 days, 20%).
- **Canonical Pools Analyzed (DeFiLlama Yields API):**
  - **Aave V3 Ethereum USDC:** `aa70268e-4b52-42bf-a116-608b370f9501` (used in the 2025 repo `src/DefiLlama/search.py`, mislabeled as `Aave_V2_USDC`).
  - **Compound V3 Ethereum USDC:** `7da72d09-56ca-4ec5-a45f-59114353e487` (Comet USDC market).
  - **Aave V2 Ethereum USDC (legacy):** `a349fea4-d780-4e16-973e-70ca9b606db2`.
  - **Compound V2 Ethereum USDC (legacy):** `cefa9bb8-c230-459a-a855-3b94e96acd8c`.
- **SOFR Benchmark:** New York Fed Secured Overnight Financing Rate API (`https://markets.newyorkfed.org/api/rates/secured/sofr/search.json`), business-day forward-filled (1,000 days mean: 4.866% / 486.6 bps).

### Headline Numbers (Full 1,000-Day Window: 12 Feb 2023 – 07 Nov 2025)

| Metric | Aave V3 USDC | Compound V3 USDC | Combined V3 (TVL-weighted) | Combined V3 (Equal-weighted) |
|---|---|---|---|---|
| Pool UUID | `aa70268e-...` | `7da72d09-...` | - | - |
| Days with subsidies (`apyReward > 0`) | 0 / 1,000 (0.0%) | 845 / 1,000 (84.5%) | 845 / 1,000 (84.5%) | 845 / 1,000 (84.5%) |
| Mean SOFR rate | 486.6 bps (4.866%) | 486.6 bps (4.866%) | 486.6 bps (4.866%) | 486.6 bps (4.866%) |
| Mean Total APY | 517.9 bps (5.179%) | 576.9 bps (5.769%) | 523.7 bps (5.237%) | 547.4 bps (5.474%) |
| Mean Base APY (`apyBase`) | 517.9 bps (5.179%) | 528.5 bps (5.285%) | 509.8 bps (5.098%) | 523.2 bps (5.232%) |
| Mean Token Subsidy (`apyReward`) | 0.0 bps (0.000%) | **48.4 bps (0.484%)** | **13.9 bps (0.139%)** | **24.2 bps (0.242%)** |
| Mean Nominal Spread (`apy - SOFR`) | +31.3 bps | +90.3 bps | +37.2 bps | +60.8 bps |
| Mean Base Spread (`apyBase - SOFR`) | +31.3 bps | +41.9 bps | +23.2 bps | +36.6 bps |
| Subsidy share of total yield | 0.0% | 8.40% | 2.66% | 4.42% |
| **Subsidy share of spread over SOFR** | **0.0%** | **53.62%** | **37.50%** | **39.81%** |

### Breakdown by Subperiods (Compound V3 USDC)
- **Train Period (12 Feb 2023 – 21 Apr 2025, 800 days):**
  - Subsidized days: 80.6% (645 / 800 days).
  - Mean Total APY: 610.4 bps vs SOFR 500.9 bps (nominal spread = +109.5 bps).
  - Mean Base APY: 555.3 bps (base spread = +54.4 bps).
  - Mean COMP Subsidy: 55.1 bps.
  - **Subsidy share of spread:** **50.29%**.
- **Test Period (22 Apr 2025 – 07 Nov 2025, 200 days):**
  - Subsidized days: **100.0%** (200 / 200 days).
  - Mean Total APY: 442.9 bps vs SOFR 429.2 bps (nominal spread = +13.7 bps).
  - Mean Base APY: 421.0 bps (**base organic spread = -8.2 bps, negative!**).
  - Mean COMP Subsidy: 21.9 bps.
  - **Interpretation:** In the test set, the organic borrower rate was *below* US Treasury SOFR. The positive spread was an illusion created entirely by COMP token subsidies (+21.9 bps turning a -8.2 bps spread into +13.7 bps).
- **Calendar Year 2024:**
  - Subsidized days: 100.0% (366 / 366 days).
  - Mean COMP Subsidy: 67.1 bps out of 284.4 bps total spread (23.58% of spread).
- **Calendar Year 2025 (through 07 Nov):**
  - Subsidized days: 100.0% (311 / 311 days).
  - Mean COMP Subsidy: 23.8 bps out of 48.6 bps total spread (**48.84% of spread**).

### Legacy Pools (V2)
- **Compound V2 cUSDC (`cefa9bb8-...`):** COMP rewards active on 21.8% of days (218 days, exclusively in 2023 before migration to V3). Mean subsidy = 13.3 bps. Overall spread was negative (-72.7 bps).
- **Aave V2 USDC (`a349fea4-...`):** 0% rewards. APY averaged 383.6 bps (-102.9 bps spread over SOFR) as capital fled to V3.

## Reproduction
Run from repository root:
```bash
py scripts/p3_08_subsidy.py
```
Outputs:
- Table: `results/tables/P3-08_subsidy_2025.csv`
- Figure: `results/figures/P3-08_subsidy_share_2025.png`
- Frozen raw data: `data/raw/defillama/{aave_v3_usdc,aave_v2_usdc,compound_v3_usdc,compound_v2_usdc,sofr,pools}.json`

## Interpretation for the "Lições de 2025" Slide
In our 2025 submission (*"Quantificando o Risco DeFi vs RWA: Modelagem e Previsão do Spread"*), we treated the spread between DeFi lending yields and SOFR as a structural risk premium reflecting counterparty, collateral, and smart-contract risks.

However, DeFiLlama's default `apy` mixes organic borrower interest (`apyBase`) with promotional governance token emissions (`apyReward`). Our empirical audit reveals:
1. **Promotional spending disguised as risk premia:** For Compound V3, **53.6%** of the historical spread over SOFR was protocol promotional spending (COMP token dilution), not a market-clearing interest rate paid by borrowers.
2. **False positive spreads:** In the 2025 test set, Compound's organic rate was lower than the US risk-free rate (-8.2 bps). A model predicting the nominal spread was actually predicting protocol marketing policy, not credit risk.
3. **Cross-protocol heterogeneity:** While Compound relied heavily on COMP subsidies (active in 84.5% of days overall, 100% in 2024–2025), Aave V3 on Ethereum operated with 0% token rewards throughout the entire 1,000-day window. Conflating the two into a single pooled DeFi index without separating subsidies contaminated the dependent variable.

### Suggested Slide Bullet (pt-BR)
> **Rendimento orgânico vs. subsídio promocional:** No trabalho de 2025, modelamos o spread DeFi vs SOFR usando o APY bruto como se fosse um prêmio de risco puro. Ao decompor as taxas on-chain, descobrimos que **53,6% do spread do Compound V3** (e **37,5% do spread ponderado por TVL**) correspondia a subsídios temporários em tokens de governança (COMP), e não a juros pagos por tomadores. No período de teste de 2025, o spread orgânico real do Compound era negativo (-8,2 bps). O modelo previa propaganda e incentivos de protocolo, não risco de crédito.

## Sources to register in `docs/sources.md`
Add to `docs/sources.md` under `## Data`:
```markdown
| D-14 | DeFiLlama Yields API | Historical daily APY, base APY (apyBase), reward APY (apyReward), and TVL for canonical lending pools (Aave V3, Aave V2, Compound V3, Compound V2) | `https://yields.llama.fi/pools` and `https://yields.llama.fi/chart/{pool_id}` (frozen in `data/raw/defillama/`) | checked 2 Nov 2026 (P3-08) |
| D-15 | Federal Reserve Bank of New York (NY Fed) Markets API | Secured Overnight Financing Rate (SOFR) daily reference rate (percentRate, volume, percentiles) | `https://markets.newyorkfed.org/api/rates/secured/sofr/search.json?startDate=2023-02-01&endDate=2025-11-10` (frozen in `data/raw/defillama/sofr.json`) | checked 2 Nov 2026 (P3-08) |
```

## Caveats
- Aave V3 offers incentive campaigns via Merkl or secondary contracts on layer 2s (Arbitrum, Optimism, Polygon) and for GHO minting; however, on Ethereum mainnet USDC (pool `aa70268e-4b52-42bf-a116-608b370f9501`), DeFiLlama records zero direct apyReward during 2023–2025.
- The 2025 repo code (`src/DefiLlama/search.py`) labeled `aa70268e-4b52-42bf-a116-608b370f9501` as `Aave_V2_USDC`, though this UUID actually corresponds to Aave V3 Ethereum. The analysis above accounts for both V3 and genuine V2 (`a349fea4-...`).

## Used in deck
Planned: Slide "Lições de 2025: O que mudou em relação ao ano passado" (alongside F-005 naive persistence baseline).

## History
- 2026-11-02, Felipe: created; audited all 4 canonical Ethereum USDC pools and NY Fed SOFR over the 1,000-day 2025 sample window; computed exact subsidy shares across train/test splits and calendar years; status: exploratory.
