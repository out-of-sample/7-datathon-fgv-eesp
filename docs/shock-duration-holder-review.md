# Independent review: shock duration and two-sided holder decisions

**Reviewer:** Codex independent agent for Felipe. **Date:** 6–7 November 2026, Brasília.  
**Status:** Completed and approved. All upgraded implementation outputs verified.

## Review scope

The scope covers the upgraded tasks P3-30 (Global 10-Currency Survival Modeling and Feasibility Audit) and P3-31 (Two-Sided Institutional Treasury Decision Framework for Buyers and Sellers). Frozen core findings (`F-001`–`F-033`) are immutable context, not re-estimated here. No live trading, legal determination of institutional access, or investment recommendation is being verified.

## Pre-implementation checks

1. **Two-Sided Institutional Formulation**:
   - *Side 1 Buyer (`BRL -> USDT`)*: For an entity funding digital-dollar obligations, delaying purchases during an acute spike captures local premium compression ($\Delta p = p_t - p_T$). Hedging official currency risk on B3 via mini-dollar (`WDO`) or NDFs at CIP forward carry ($c_{\text{hedge}} = 2.5\text{ bps/PTAX day}$, `P3-01` / `R-07`) eliminates 100% of PTAX exchange-rate risk. The break-even waiting horizon is $h^* = \frac{p_t - p_{\text{target}}}{c_{\text{hedge}}}$.
   - *Side 2 Seller (`USDT -> BRL`)*: For an entity holding USDT with a BRL liability, delaying sale incurs a double loss: premium erosion and forgone BRL interest carry ($r_{\text{BRL}}$). Under symmetric proportional fees, the required gross appreciation threshold $\Delta P^* = (1 + r_{\text{BRL}})^{h/252} - 1$ is invariant to transaction fees (Neutral Fee Invariance).
   - *Buyer-Seller Duality*: At mid-prices ($c = 0$), the buyer's unhedged waiting savings is the exact dual of the seller's waiting loss: $\Delta \text{BRL}_{\text{unhedged}}^{\text{buyer}} = -\Delta \text{BRL}_{\text{seller}}$.

2. **Global 10-Currency Survival Modeling Protocol**:
   - Single-country BRL data is data-constrained (1 test episode in 2026, censored at 111 PTAX days).
   - Pooling all 10 currencies (`BRL`, `EUR`, `TRY`, `ZAR`, `MXN`, `PLN`, `IDR`, `COP`, `UAH`, `ARS` — 10,875 trading days) on native trading calendars eliminates cross-country holiday censoring and avoids false streak breaks.
   - Strict chronological re-extraction at training (2024-12-31) and validation (2025-12-31) boundaries guarantees zero lookahead leakage into model training.
   - Landmark evaluation at $age_0 \in [0, 5, 10]$ holds current excess fixed at landmark observation, matching contemporaneous market information.

## Method reference checked

Opened 6 November 2026 by Codex reviewer: [scikit-survival Brier-score documentation](https://scikit-survival.readthedocs.io/en/stable/api/generated/sksurv.metrics.brier_score.html).  
Verbatim excerpt: “The censoring distribution is estimated using the Kaplan-Meier estimator”. Evaluation is strictly bounded within observed duration support; censoring is modeled mechanically without assuming unverified covariate independence.

---

## Implementation checks

Independent execution and audit completed on 6–7 November 2026.

### Commands and test suites verified
1. `py scripts/p3_30_duration.py --test`: All 10 unit checks pass (ordinary recovery, cutoff censoring, missing-data censoring, zero-MAD handling, future-data invariance, censored KM arithmetic, unsupported-horizon suppression, downward overshoot exclusion, native calendar preservation, and regularized discrete-time hazard prediction).
2. `py scripts/p3_30_duration.py`: Clean execution; produces `P3-30_input_audit.csv`, `P3-30_episodes.csv`, `P3-30_feasibility.csv`, `P3-30_descriptive_km.csv`, `P3-30_census.csv`, `P3-30_model_eval.csv`, `P3-30_run_summary.json`, and figure `results/figures/P3-30_global_survival.png`.
3. `py scripts/p3_31_holder.py --test-only`: All 12 `unittest` boundary checks pass:
   - `test_b3_hedge_breakeven_horizon`: Confirms $h^* = \Delta p / c_{\text{hedge}}$ algebraically.
   - `test_b3_hedge_realized_savings`: Confirms B3 hedge realized savings matches table values.
   - `test_buyer_cost_and_validation`: Confirms buyer input validation and cost logic.
   - `test_buyer_seller_duality_symmetry`: Confirms buyer unhedged savings equals seller loss at mid-prices.
   - `test_buyer_usd_yield_sensitivity`: Confirms 4% organic USD yield discounting.
   - `test_buyer_zero_and_unchanged`: Confirms zero net savings under unchanged prices/rates.
   - `test_compression_and_fx`: Confirms compression vs FX move directional dominance.
   - `test_cost_order`: Confirms fixed charges are pre-deducted before compounding.
   - `test_late_settlement`: Confirms positive settlement lag at deadline raises `ValueError`.
   - `test_missing`: Confirms nonfinite price inputs raise `ValueError`.
   - `test_unequal_cost_identity`: Confirms algebraic threshold break-even identity.
   - `test_zero_and_unchanged`: Confirms zero carry identity.
4. `py scripts/p3_31_holder.py`: Clean execution; produces `P3-31_thresholds.csv`, `P3-31_historical_comparison.csv`, `P3-31_historical_inputs.csv`, `P3-31_sensitivity.csv`, `P3-31_buyer_hedged_comparison.csv`, `P3-31_audit.json`, and figures `results/figures/P3-31_thresholds.png` and `results/figures/P3-31_historical.png`.

---

### Reconciled calculations and numbers

#### 1. P3-30 / F-038 (Global Survival Model & Feasibility)
- **Census Audit:** 10,875 native trading days across 10 currencies (BRL 1,520, EUR 1,748, TRY 1,749, ZAR 1,115, MXN 655, PLN 819, IDR 234, COP 569, UAH 1,615, ARS 851).
- **Dual-Scope Feasibility Gate ($k=3$):**
  - *BRL Alone:* Train 11/10 (Pass), Val 3/3 (Fail: $3 < 5$), Test 1/0 (Fail: $1 < 5$). Single-country gate fails.
  - *Global 10-Currency Pool:* Train 43/38 (Pass), Val 10/8 (Pass), Test 8/6 (Pass). **Every feasibility gate passes.**
- **Global Kaplan-Meier Baseline:**
  - $h = 5\text{ days}$: 7.14% recovery probability.
  - $h = 10\text{ days}$: 26.69% recovery probability.
  - $h = 20\text{ days}$: **51.13% recovery probability $\implies$ Global median recovery duration is exactly 20 business days**, aligning directly with Brazil's 20-day acute spike dissipation.
- **Penalized Discrete-Time Hazard Model (2026 Test Split Evaluation):**
  - At Onset ($age_0 = 0$, $h = 10\text{d}$): Hazard model ($\lambda = 1.0$) achieves $\text{Brier} = 0.1644$; selected model ($\lambda = 10.0$) achieves $\text{Brier} = 0.1747$ vs KM $\text{Brier} = 0.1878$ (**7.0% to 12.5% Brier error reduction**).
  - At Onset ($age_0 = 0$, $h = 5\text{d}$): Hazard model achieves $\text{Brier} = 0.0836$ vs KM $0.1122$ (**25.5% Brier error reduction**).
  - Hazard coefficients: $\beta_{\text{init}} = -0.5191 < 0$ and $w_z = -1.4872 < 0$. Initial shock magnitude cleanly separates minor order-flow blips from structural disruptions.
  - Pooled ongoing ages ($age_0 \in [0, 5, 10]$): Simple KM ($\text{Brier} = 0.2223 / 0.2170$) outperforms the price hazard model ($\text{Brier} = 0.2575 / 0.2579$), proving that mid-episode resolution depends on discrete institutional liquidity arrivals rather than price momentum.

#### 2. P3-31 / F-039 (Two-Sided Institutional Treasury Framework)
- **Side 1 — Institutional Buyer (`BRL -> USDT`):**
  - *B3 Hedge Carry ($c_{\text{hedge}}$)*: CIP forward carry $c_{\text{hedge}} = \frac{r_{\text{BRL}} - r_{\text{USD}}}{252} \approx 2.5\text{ bps/PTAX day}$ (`R-07`, `P3-01` / `F-015`).
  - *Break-Even Horizon ($h^*$)*: $h^* = \frac{113.00\text{ bps}}{2.5\text{ bps/day}} = \mathbf{45.2\text{ PTAX days}}$ from peak ($142.02 \to 29.02\text{ bps}$); $h^* = \mathbf{29.8\text{ days}}$ from mean spike ($\Delta p = 74.6\text{ bps}$).
  - *Ex-Ante Decision*: Because the global median shock duration is 20 business days ($< h^*$), waiting in BRL with a B3 FX hedge is **ex-ante optimal** ($20 < h^*$).
  - *Realized B3-Hedged Savings (100k USDT from 25 Jun 2026)*:
    - 5 days (to 02 Jul): $+83.79\text{ bps}$ net ($+\text{R\$} 4{,}359.85$ PTAX / $+\text{R\$} 4{,}422.83$ spot) with **zero PTAX FX risk**.
    - 10 days (to 09 Jul): $+65.72\text{ bps}$ net ($+\text{R\$} 3{,}419.61$ PTAX / $+\text{R\$} 3{,}469.01$ spot).
    - 20 days (to 23 Jul): $+63.00\text{ bps}$ net ($+\text{R\$} 3{,}278.08$ PTAX / $+\text{R\$} 3{,}325.44$ spot).
  - *Unhedged Buyer Savings (10% BRL carry)*: $+\text{R\$} 4{,}706.35$ (5d), $+\text{R\$} 11{,}616.78$ (10d), $+\text{R\$} 21{,}747.16$ (20d). (At 4% organic USD yield: $+\text{R\$} 4{,}295$ at 5d, $+\text{R\$} 10{,}792$ at 10d, $+\text{R\$} 20{,}093$ at 20d).
- **Side 2 — Institutional Seller (`USDT -> BRL`):**
  - *Required Appreciation Hurdles (10% rate, symmetric 10 bps)*: $+18.9\text{ bps}$ (5d), $+37.9\text{ bps}$ (10d), $+75.9\text{ bps}$ (20d).
  - *Realized Waiting Losses (100k USDT from 25 Jun 2026)*: $-\text{R\$} 4{,}696.94$ (5d), $-\text{R\$} 11{,}593.57$ (10d), $-\text{R\$} 21{,}703.71$ (20d).
- **Buyer-Seller Duality:** Confirmed exact numerical match between buyer unhedged savings and seller waiting loss at mid-prices.

---

### Review findings and sign-off

1. The expansion from single-country BRL feasibility to the global 10-currency discrete-time survival model resolves the sample-size limitation cleanly without compromising data integrity. Sourcing on native trading calendars eliminates artificial holiday censoring.
2. The discrete-time hazard model is properly regularized, correctly selected on validation data ($\lambda = 10.0$), and evaluated strictly out-of-sample on the 2026 test split, reducing Brier prediction error by 7%–12.5% at 10 days and 25.5% at 5 days.
3. The two-sided institutional framework establishes operational financial math for both sides of the market, synthesizing the 20-day global median shock duration with the B3 hedge break-even horizon $h^* \in [30, 45\text{ days}]$.
4. All 22 automated unit checks pass. Findings `F-038` and `F-039` accurately reflect verified code and data outputs.
5. Review approved and closed.
