---
id: F-039
title: Two-sided institutional treasury framework: BRL -> USDT buyers save +63 to +84 bps hedged on B3 (h* in [30, 45] days), while USDT -> BRL sellers face +19 to +76 bps hurdle appreciation
status: exploratory
task: P3-31
date: 2026-11-06
checked_by: -
---

## Claim
For corporate treasuries and portfolio managers operating in digital dollars (USDT) under elevated Brazilian premium shocks, optimal conversion timing depends critically on transaction directionality:

1. **Side 1 — Institutional Buyer (`BRL -> USDT`, Importer / Outbound Corporate Remitter)**:
   - For an entity acquiring $Q = 100{,}000$ USDT by deadline $h \in \{5, 10, 20\}$ PTAX business days during an acute premium spike, waiting in BRL while hedging official USD/BRL currency risk on B3 via mini-dollar (`WDO`) or NDF at documented Covered Interest Parity (CIP) carry ($c_{\text{hedge}} = 2.5\text{ bps/PTAX day}$, `P3-01` / `R-07`) eliminates 100% of PTAX exchange-rate risk.
   - The break-even waiting horizon $h^* = \frac{p_t - p_{\text{target}}}{c_{\text{hedge}}}$ reaches **45.2 business days** (from 25 Jun 2026 peak of $142.02\text{ bps}$ to post-spike $29.02\text{ bps}$, $\Delta p = 113.00\text{ bps}$) and **29.8 business days** (from the 20-day acute spike mean of $+74.6\text{ bps}$ compression).
   - Because $h^* \in [29.8, 45.2\text{ days}]$ strictly exceeds the empirical global median shock duration of **20 business days** (`P3-30`), waiting in BRL with a B3 FX hedge is **ex-ante optimal** ($20 < h^*$).
   - Realized B3-hedged buyer savings from 25 Jun 2026:
     - **5 PTAX days (to 02 Jul)**: Premium compressed by $96.29\text{ bps}$, minus $12.50\text{ bps}$ B3 hedge carry = **+83.79 bps net savings (+R$ 4,360 to +R$ 4,423 per 100k USDT)** with **zero PTAX FX risk**.
     - **10 PTAX days (to 09 Jul)**: Premium compressed by $90.72\text{ bps}$, minus $25.00\text{ bps}$ hedge carry = **+65.72 bps net savings (+R$ 3,420 to +R$ 3,469 per 100k USDT)**.
     - **20 PTAX days (to 23 Jul)**: Premium compressed by $113.00\text{ bps}$, minus $50.00\text{ bps}$ hedge carry = **+63.00 bps net savings (+R$ 3,278 to +R$ 3,325 per 100k USDT)**.
   - Under unhedged waiting (Strategy B2) at 10% net BRL yield and 10 bps fee, delayed conversion saved **+R$ 4,706.35** (dual: **+R$ 4,696.94**) at 5 days, **+R$ 11,616.78** (dual: **+R$ 11,593.57**) at 10 days, and **+R$ 21,747.16** (dual: **+R$ 21,703.71**) at 20 days. Under symmetric proportional costs ($F=0$) and zero USD yield, Buyer terminal BRL savings is the exact dual of Seller terminal BRL loss: $\Delta \text{BRL}_{\text{unhedged}}^{\text{buyer}} = \frac{1+c}{1-c} \times (\text{Seller loss})$.

2. **Side 2 — Institutional Seller (`USDT -> BRL`, Domestic Obligation Funding)**:
   - For an entity holding $100{,}000$ idle USDT funding a BRL liability, a hypothetical 10% effective annual net BRL return implies required gross USDT/BRL appreciation hurdles of **+18.9, +37.9, and +75.9 basis points** over 5, 10, and 20 PTAX publication days under symmetric 10 bps fees.
   - In June 2026, waiting in USDT generated **-R$ 4,697, -R$ 11,594, and -R$ 21,704** relative to liquidating immediately and compounding in BRL.

## Evidence
- **Input Lineage**: `data/processed/P1-02_premium_daily.csv` (1,520 PTAX business days; June 2026 21-row illustration window from 25 Jun to 23 Jul 2026).
- **Core Equations**:
  1. *Seller Net Proceeds & Hurdle*:
     $$N_t^{\text{seller}}(Q) = Q \cdot P_t \cdot (1 - c_t) - F_t$$
     $$P_T^* = \frac{N_t^{\text{seller}}(Q) \cdot (1 + r_{\text{BRL}})^{h/252} + F_T}{Q \cdot (1 - c_T)}$$
     Under symmetric proportional costs ($c_t = c_T = c$, $F=0$): $\Delta P^* = (1 + r_{\text{BRL}})^{h/252} - 1$ (Neutral Fee Invariance).
  2. *Buyer Outlay & Unhedged Savings*:
     $$C_t^{\text{now}}(Q) = Q \cdot P_t \cdot (1 + c_t) + F_t$$
     $$\Delta \text{BRL}_{\text{unhedged}}^{\text{buyer}}(t, T) = C_t^{\text{now}}(Q) \cdot (1 + r_{\text{BRL}})^{h/252} - \left[Q \cdot P_T \cdot (1 + c_T) + F_T\right]$$
     When $r_{\text{USD}} \in \{0\%, 4\%\}$ (per `F-020`, organic DeFi USD lending yields net of token subsidies are near SOFR ~4%), purchasing $Q / (1 + r_{\text{USD}})^{h/252}$ at $t$ yields unhedged savings of +R$ 4,295 (5d), +R$ 10,792 (10d), and +R$ 20,093 (20d).
  3. *B3 FX Hedge Strategy (Strategy B3)*:
     Covered Interest Parity forward carry: $c_{\text{hedge}} = \frac{r_{\text{BRL}} - r_{\text{USD}}}{252} \approx 2.5\text{ bps/PTAX day}$ (`R-07`, `P3-01` / `F-015`).
     $$\Delta_{\text{hedged}}^{\text{bps}}(t, T) = (p_t - p_T) - h \cdot c_{\text{hedge}}$$
     $$h^* = \frac{p_t - p_{\text{target}}}{c_{\text{hedge}}}$$
- **Data Reconciliation Across June 2026**:
  - $P_0 = \text{R\$} 5.278475$ per USDT ($X_0 = 5.1892$, $U_0 = 0.998791$, $p_0 = +184.35\text{ bps}$ window indicative; benchmark peak $p_t = 142.02\text{ bps}$).
  - Multiplicative decomposition $P = X \cdot U \cdot (1 + p/10{,}000)$ reconciles across all 21 rows of `P3-31_historical_inputs.csv` ($< 10^{-10}$ relative tolerance).
- **Reproduction**:
  Run: `py scripts/p3_31_holder.py` (unit tests execute before table/figure generation); test only: `py scripts/p3_31_holder.py --test-only`.
- **Generated Outputs**:
  - `results/tables/P3-31_thresholds.csv` (60 rows; seller break-even prices and required appreciation).
  - `results/tables/P3-31_historical_inputs.csv` (21 rows; June 2026 complete price and premium series).
  - `results/tables/P3-31_historical_comparison.csv` (30 rows; seller actual indicative vs fixed-FX counterfactual).
  - `results/tables/P3-31_sensitivity.csv` (300 rows; seller FX move $\times$ ending premium sensitivity).
  - `results/tables/P3-31_buyer_hedged_comparison.csv` (two-sided buyer & B3 hedge performance table).
  - `results/tables/P3-31_audit.json` (hash, parameters, and 12-test validation log).
  - `results/figures/P3-31_thresholds.png` (two-panel: seller hurdle curves vs buyer B3 hedge break-even horizon $h^*$).
  - `results/figures/P3-31_historical.png` (two-panel: seller loss vs buyer unhedged & B3-hedged realized savings).
- **Unit Testing**:
  12 boundary tests pass: zero interest/unchanged price, compression vs FX appreciation, unequal cost identity, nonfinite input rejection, settlement lag bounds, fixed-cost deduction order, buyer cost validation, buyer zero/unchanged properties, buyer-seller duality symmetry, B3 hedge break-even horizon formula, B3 hedge realized savings ranges, and USD yield sensitivity.

## Caveats
- **Directional Asymmetry**: Premium compression hurts the USDT holder/seller (who loses local scarcity value and BRL interest carry) but directly enriches the corporate buyer (who avoids paying the artificial local premium).
- **B3 Hedge Operational Constraints**: Strategy B3 requires access to B3 FX derivatives (mini-dollar `WDO` or standard `DOL` futures), margin maintenance, and same-day exchange settlement. Corporate treasuries without derivative mandates cannot execute Strategy B3 directly.
- **Calendar Alignment**: Calculations use official PTAX publication business days as a proxy for Brazilian banking settlement. Real-world execution must account for bank cutoffs and exchange Pix availability.
- **Retrospective Event Benchmark**: The June 2026 episode is a single historical regulatory intervention; the framework provides decision accounting, not guaranteed future arbitrage returns.

## Used in deck
Direct candidate for practical implications slides (Slide 9 and Slide 10) and Annex B.8/B.10: demonstrates actionable corporate treasury rules for both importers/remitters (`BRL -> USDT`) and liquidity managers (`USDT -> BRL`).

## History
- 2026-11-06 — Codex for Felipe: initial seller decision engine, thresholds, and boundary tests.
- 2026-11-07 — Flash agent for Felipe: upgraded to Two-Sided Institutional Treasury Decision Framework incorporating Side 1 Buyer (`BRL -> USDT`), B3 FX hedge carry, break-even horizon $h^*$, and synthesis with `P3-30` median shock duration.
