---
id: F-017
title: Synthetic control estimates a +109 bps acute treatment gap for the 23 Jun 2026 shock (Brazil ranks #1 of 6, ratio 9.31) fading to a +28 bps plateau
status: confirmed
task: P2-04
date: 2026-11-02
checked_by: Renzo
---

## Claim
A convex Synthetic Control estimator (Abadie, Diamond & Hainmueller 2010) constructed from international fiat-to-USDT currencies without the Brazilian shock (pre-period: 1 Nov 2025 – 22 Jun 2026; post-period: 24 Jun – 30 Sep 2026) reveals that **Brazil's USDT premium diverged sharply from synthetic counterfactuals immediately following the 23 June 2026 BCB supervisory ofício**.

In the **headline 5-donor specification** (EUR, TRY, ZAR, MXN, COP):
1. **Pre-treatment Fit:** Pre-period RMSPE is **7.05 bps** across 140 common trading days, demonstrating that Synthetic Brazil tightly tracks Brazil's pre-shock premium. The synthetic weights place **63.6% on EUR, 17.9% on MXN, 13.4% on TRY, 4.5% on ZAR, and 0.7% on COP**.
2. **Acute Treatment Gap:** Over 24 Jun – 21 Jul 2026 (17 days with data for Brazil and every donor), Brazil's premium exceeded Synthetic Brazil by **+109.3 bps** on average. The non-parametric Difference-in-Differences (DiD) baseline against an equal-weighted donor mean yields **+103.3 bps**.
3. **After the spike:** over 22 Jul – 30 Sep 2026 (48 common days) the gap narrowed to **+28.2 bps** (DiD: **+31.4 bps**). The placebo test in P4-01 does not separate the after-spike level from ordinary drift (p = 0.24), so only the spike is a measured effect.
4. **In-Space Placebo Inference:** Brazil ranks **#1 of 6** in post-to-pre RMSPE ratio (**9.31** vs donor placebos ranging from 0.78 to 1.22), #1 of 6 in acute treatment gap (+109.3 bps vs donor placebos between -16.6 and +67.8 bps), and #1 of 6 in acute RMSPE (117.95). The permutation p-value is **$p = 1/6 = 0.167$**, exactly at the discrete sample lower bound.

## Evidence

### Headline Results Across Specifications
All specifications evaluate the acute window ($24\text{ Jun} - 21\text{ Jul}$) and plateau window ($22\text{ Jul} - 30\text{ Sep}$):

| Specification | Outcome Series | Pre Period | Pre RMSPE (bps) | Post/Pre Ratio | Acute Gap (SC, bps) | Plateau Gap (SC, bps) | DiD Acute Gap (bps) | DiD Plateau Gap (bps) | Placebo Rank | Permutation $p$ | Weights Summary |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **5-donor (Headline)** | **BRL_ptax** | **Nov 25 – Jun 26** | **7.05** | **9.31** | **+109.3** | **+28.2** | **+103.3** | **+31.4** | **1/6** | **0.167** | **EUR: 63.6%, MXN: 17.9%, TRY: 13.4%, ZAR: 4.5%, COP: 0.7%** |
| 5-donor (BRL_ecb check) | BRL_ecb | Nov 25 – Jun 26 | 16.58 | 3.94 | +101.6 | +32.3 | +96.8 | +35.4 | 1/6 | 0.167 | EUR: 60.5%, MXN: 30.7%, ZAR: 4.6%, COP: 4.3% |
| Strict 4-donor (ex-EUR) | BRL_ptax | Nov 25 – Jun 26 | 10.33 | 6.90 | +116.7 | +33.9 | +102.9 | +33.4 | 1/5 | 0.200 | TRY: 54.6%, MXN: 42.7%, ZAR: 2.6% |
| Strict 4-donor [BRL_ecb] | BRL_ecb | Nov 25 – Jun 26 | 18.25 | 3.85 | +108.5 | +37.7 | +96.4 | +37.4 | 1/5 | 0.200 | MXN: 55.9%, TRY: 38.1%, COP: 3.6%, ZAR: 2.5% |
| 6-donor (with IDR) | BRL_ptax | Dec 25 – Jun 26 | 7.19 | 9.20 | +109.9 | +28.6 | +104.7 | +35.7 | 1/7 | 0.143 | EUR: 58.0%, MXN: 21.7%, TRY: 15.4%, ZAR: 4.1%, COP: 0.5% |
| 6-donor [BRL_ecb] | BRL_ecb | Dec 25 – Jun 26 | 16.90 | 3.88 | +102.1 | +32.6 | +98.2 | +39.7 | 1/7 | 0.143 | EUR: 52.3%, MXN: 39.1%, COP: 4.4%, ZAR: 3.4%, TRY: 0.7% |

### In-Space Placebo Breakdown (Headline 5-Donor Specification)
Each donor is treated in turn, estimating optimal synthetic weights on the remaining 4 donors:

| Unit | Role | Pre RMSPE (bps) | Post RMSPE (bps) | RMSPE Ratio | Acute Gap (bps) | Acute RMSPE (bps) | Rank (Ratio) | Rank (Acute Gap) |
|---|---|---|---|---|---|---|---|---|
| **Brazil (BRL_ptax)** | **Treated** | **7.05** | **65.71** | **9.31** | **+109.3** | **117.95** | **1 of 6** | **1 of 6** |
| Turkey (TRY) | Donor Placebo | 15.39 | 18.81 | 1.22 | -16.6 | 20.60 | 2 of 6 | 6 of 6 |
| Eurozone (EUR) | Donor Placebo | 12.05 | 12.02 | 1.00 | +9.7 | 12.86 | 3 of 6 | 4 of 6 |
| Colombia (COP) | Donor Placebo | 62.27 | 56.98 | 0.92 | +32.8 | 61.91 | 4 of 6 | 3 of 6 |
| South Africa (ZAR) | Donor Placebo | 70.81 | 64.40 | 0.91 | +67.8 | 70.62 | 5 of 6 | 2 of 6 |
| Mexico (MXN) | Donor Placebo | 16.56 | 12.96 | 0.78 | -12.1 | 15.79 | 6 of 6 | 5 of 6 |

### Robustness & Sensitivity Checks
1. **Donor Pool Composition:**
   - Removing EUR (under the conservative hypothesis that European MiCA CASP regulations might confound the donor pool) yields an acute gap of **+116.7 bps** and plateau gap of **+33.9 bps** (Brazil ranks 1/5, ratio 6.90).
   - Adding IDR (starting the pre-period on 1 Dec 2025 to achieve 100% data coverage) yields an acute gap of **+109.9 bps** and plateau gap of **+28.6 bps** (Brazil ranks 1/7, ratio 9.20).
2. **Fix Timing Alignment (`BRL_ecb`):**
   - Evaluating Brazil using the ECB 14:00 Frankfurt reference rate snapshot (identical timestamp to the ECB donors) yields an acute gap of **+101.6 bps** and plateau gap of **+32.3 bps** (Brazil ranks 1/6).
3. **Model Dependence:**
   - The non-parametric Difference-in-Differences baseline (equal-weighted donor mean) requires no optimization or convex hull assumptions and produces an acute gap of **+103.3 bps** (vs +109.3 bps SC) and plateau gap of **+31.4 bps** (vs +28.2 bps SC).

## Methodological Nuance: Permutation Inference Floor
With $J = 5$ donor currencies, the non-parametric permutation p-value has a theoretical floor of $1 / (J + 1) = 1/6 \approx 0.167$ ($1/7 \approx 0.143$ with IDR; $1/5 = 0.200$ without EUR). As agreed at the Economist Gate (2026-11-01), the Datathon plan's standard guideline of "$p < 0.10$ for causal falsification" cannot be reached by cross-sectional permutation alone given global Binance fiat coverage. 

Therefore, our inference structure combines two complementary strategies:
1. **Statistical Significance:** Established via the **within-Brazil 200-date placebo distribution** (P2-03, F-016), where $p = 1/201 = 0.0050$ ($p < 0.005$).
2. **Comparison with other currencies:** the synthetic control and the DiD (P2-04) show that no comparison currency moved like Brazil. Over the spike their changes were −15.6 to +23.7 bps (EUR −1.3, TRY −11.9, ZAR +7.3, MXN −15.6, COP +23.7), against +103 to +109 for Brazil. A global crypto or emerging-market shock is therefore an unlikely explanation. With 5 donors this is supporting evidence (permutation p = 0.17), not a significance test.

## Reproduction
```bash
python scripts/p2_04_synth.py
```
Outputs: `results/tables/P2-04_synth_results.csv`, `results/tables/P2-04_synth_weights.csv`, `results/figures/P2-04_synthetic_control.png`.

## History
- 2026-11-02, agent for Renzo (review fixes, on Felipe's behalf, agreed by Renzo): day counts stated (17 acute, 48 plateau common days); "as domestic order books and OTC channels adapted" removed (no evidence; July fade unexplained); "causal attribution" softened to comparison with donors (p = 0.17); figure: neutral labels, no overlap, placebos with pre-fit > 5× Brazil's (COP, ZAR) left out of panel B and named in the legend (Abadie et al. 2010)
- 2026-11-02, Renzo (review, P2-04): tables reproduce exactly; independent donor-average DiD matches (tasks/P2-04 → Handoff)
- 2026-11-02, Felipe: created
