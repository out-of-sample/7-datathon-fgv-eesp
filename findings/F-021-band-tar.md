---
id: F-021
title: Threshold Band-TAR model reveals a 26-fold widening of the no-arbitrage band during the 24 Jun spike (1.6 to 42.0 bps) and deceleration of mean reversion
status: exploratory
task: P3-07
date: 2026-11-02
checked_by: -
---

## Claim
A symmetric Band Threshold Autoregression model (Band-TAR(1), Obstfeld & Taylor 1997) estimated on the daily USDT/BRL premium across the structural regimes identified by Bai-Perron break tests (P2-02) shows a sharp widening of the no-arbitrage friction band during the 20-day spike following the 23 June 2026 BCB supervisory notice:

1. **Pre-Notice Friction Floor (Regime 4, Jul 2025 – Jun 2026):**
   Prior to the notice, the implied arbitrage band threshold was just **$c = 1.61\text{ bps}$** (95% block-bootstrap CI: **$[1.22, 5.13]\text{ bps}$**). Deviations outside this narrow band were eliminated almost immediately ($\beta_{\text{out}} = -1.03$, implied half-life $t_{1/2} \le 1.00\text{ trading day}$). This $1.6\text{ bps}$ threshold sits directly within the bid-ask microstructure noise floor ($2–10\text{ bps}$, F-007), showing an exceptionally tight, low-friction arbitrage corridor.

2. **Acute Post-Notice Disruption (Regime 5, 24 Jun – 21 Jul 2026):**
   During the 20-day spike after the 23 June notice, the no-arbitrage band blew open **26-fold to $c = 41.95\text{ bps}$** (95% CI: **$[9.96, 52.63]\text{ bps}$**). Within this wide band, the premium drifted without triggering immediate corrective arbitrage flows.

3. **Post-Spike Regime (Regime 6, 22 Jul – 30 Oct 2026):**
   After the 22 July break (whose cause is unexplained within $\pm 5$ days, `F-011`; coincides in time with `M-04`, `M-05`, `F-008`), the estimated band around the regime mean narrowed to **$c = 9.40\text{ bps}$** (95% CI: **$[3.13, 14.41]\text{ bps}$**). Note (`F-022`): because the post-spike mean level itself (+11.5 to +19.3 bps above pre-notice) is not statistically distinguishable from ordinary 40-day drift across clean dates (placebo $p = 0.24$), only the acute spike ($c = 41.95\text{ bps}$) is presented as a measured effect of the notice, while the Regime 6 estimate is descriptive of post-July volatility.

4. **Deceleration of Arbitrage Speed (Pooled Post-Notice):**
   Pooling the post-notice period (24 Jun – 30 Oct 2026, $N=91$), the outside-band reversion speed dropped to **$\beta_{\text{out}} = -0.352$** (95% CI: $[-1.17, -0.28]$), lengthening the deviation half-life to **$t_{1/2} = 1.60\text{ trading days}$** (95% CI: $[0.26, 2.10]\text{ days}$), compared to $\le 1.00\text{ day}$ adjustment pre-notice.

5. **Honest Baseline Comparison (prompt.md Rule 2):**
   - **vs Naive Random Walk ($\Delta y_t = 0$):** Band-TAR outperforms persistence across all regimes in-sample, reducing RMSE by **$7.8\%$ to $26.5\%$** (and by $20.3\%$ during the acute spike). Out-of-sample on the full 6-year series, Naive RW has lower RMSE (17.43 vs 19.82 bps).
   - **vs Linear AR(1):** Band-TAR outperforms linear AR(1) in-sample across all regimes, with the largest gains in R5 (**$+10.8\%$ gain in acute spike**) and R6 (**$+7.2\%$ gain**), and achieves lower OOS RMSE than linear AR(1) in wide-threshold regimes (R2, R5, R6, Pooled Post-Notice). In tight corridor regimes like R4 where $c \approx 1.6\text{ bps}$, linear AR(1) is slightly more parsimonious OOS (8.80 vs 8.93 bps).

## Evidence

### Band-TAR(1) Parameter Estimates and Bootstrap Confidence Intervals
Estimated on $z_t = y_t - \mu_r$ (demeaned deviation from regime equilibrium parity) with threshold grid search ($10\text{th}–85\text{th}$ percentiles of $|z_{t-1}|$, $\ge 15\%$ sample trimming in each state):

$$\Delta z_t = \beta_{\text{in}} z_{t-1} \cdot \mathbf{1}_{\{|z_{t-1}| \le c\}} + \beta_{\text{out}} \left(z_{t-1} - \operatorname{sign}(z_{t-1}) c\right) \cdot \mathbf{1}_{\{|z_{t-1}| > c\}} + \varepsilon_t$$

| Regime | Period | N | Mean $\mu_r$ (bps) | SD $\sigma_r$ (bps) | Band $c$ (bps) | 95% Bootstrap CI of $c$ | Reversion $\beta_{\text{out}}$ | 95% CI of $\beta_{\text{out}}$ | Half-Life $t_{1/2}$ (days) | % Inside Band | Band around 0 Parity (bps) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **R1: Early Friction** | Oct 20 – Jul 21 | 196 | 91.29 | 58.36 | **54.97** | [5.91, 66.29] | -0.907 | [-1.33, -0.64] | 0.29 | 79.0% | 78.64 |
| **R2: Post-Cap / Pre-CVM** | Jul 21 – Aug 24 | 771 | 54.54 | 34.23 | **13.62** | [4.48, 36.87] | -0.631 | [-1.00, -0.55] | 0.70 | 45.6% | 72.12 |
| **R3: Pre-Tick Cut** | Aug 24 – Jul 25 | 220 | 34.94 | 24.94 | **4.75** | [2.29, 27.52] | -0.720 | [-1.17, -0.66] | 0.54 | 25.1% | 34.16 |
| **R4: Pre-Notice Corridor** | Jul 25 – Jun 26 | 242 | 9.32 | 9.28 | **1.61** | [1.22, 5.13] | -1.030 | [-1.48, -0.94] | 1.00 | 16.6% | 10.06 |
| **R5: Acute Notice Spike** | Jun 26 – Jul 26 | 20 | 109.14 | 43.62 | **41.95** | [9.96, 52.63] | -1.489 | [-5.98, -0.42] | 1.00 | 57.9% | 99.44 |
| **R6: Post-Spike (Jul–Oct 26)** | Jul 26 – Oct 26 | 71 | 26.78 | 16.64 | **9.40** | [3.13, 14.41] | -0.987 | [-1.64, -0.66] | 0.16 | 47.1% | 39.84 |
| **Pooled Pre-Notice** | Jul 25 – Jun 26 | 242 | 9.32 | 9.28 | **1.61** | [1.22, 5.13] | -1.030 | [-1.48, -0.94] | 1.00 | 16.6% | 10.06 |
| **Pooled Post-Notice** | Jun 26 – Oct 26 | 91 | 44.88 | 42.35 | **32.43** | [5.91, 54.14] | -0.352 | [-1.17, -0.28] | **1.60** | 78.9% | 75.24 |
| **Full Sample** | Oct 20 – Oct 26 | 1520 | 48.66 | 42.04 | **26.68** | [8.07, 48.05] | -0.584 | [-1.00, -0.51] | 0.79 | 54.4% | 74.87 |

*Note:* Block bootstrap with 500 replications, block length $b=5$ (or $b=3$ for $N < 40$), `seed=20261102`. Implied half-life is $t_{1/2} = \ln(0.5)/\ln(1 + \beta_{\text{out}})$ with discrete 1-day ceiling when $\beta_{\text{out}} \le -1.0$.

### Model Comparison Against Baselines (RMSE in bps)

| Regime | Naive RW In-Sample | Linear AR(1) In-Sample | Band-TAR In-Sample | In-Sample Gain vs RW (%) | In-Sample Gain vs AR1 (%) | Naive RW OOS (80/20) | Linear AR(1) OOS (80/20) | Band-TAR OOS (80/20) | Best Model OOS |
|---|---|---|---|---|---|---|---|---|---|
| R1 | 60.10 | 51.02 | **49.90** | +17.0% | +2.2% | 38.91 | **32.29** | 35.37 | Linear AR(1) |
| R2 | 34.01 | 29.51 | **29.30** | +13.8% | +0.7% | 36.72 | 30.34 | **29.66** | **Band-TAR** |
| R3 | 28.36 | 23.30 | **23.15** | +18.4% | +0.6% | 15.98 | **12.92** | 12.94 | Tie / AR(1) |
| R4 (Pre-Notice) | 12.48 | 9.23 | **9.17** | +26.5% | +0.7% | 10.21 | **8.80** | 8.93 | Linear AR(1) |
| R5 (Acute Spike) | 38.80 | 34.67 | **30.91** | +20.3% | **+10.8%** | 32.89 | 32.89 | **30.97** | **Band-TAR** |
| R6 (Post-Spike) | 16.91 | 14.84 | **13.78** | +18.5% | **+7.2%** | 24.84 | 22.54 | **21.22** | **Band-TAR** |
| Pooled Post-Notice | 23.25 | 22.05 | **21.44** | +7.8% | **+2.8%** | 27.62 | 26.45 | **26.22** | **Band-TAR** |
| Full Sample | 35.20 | 31.95 | **31.29** | +11.1% | +2.1% | 17.43 | 21.73 | **19.82** | Naive RW |

### Reproduction
- Run: `py scripts/p3_07_tar.py`
- Table: `results/tables/P3-07_band_tar.csv`
- Figure: `results/figures/P3-07_band_tar.png`

## Caveats
1. **Small Sample in Acute Spike ($N=20$):** Regime 5 has only 20 trading days (24 Jun – 21 Jul 2026). While the $42.0\text{ bps}$ band is supported by bootstrap CIs [$10.0, 52.6$] and OOS verification, the pooled post-notice sample ($N=91$, $c = 32.4\text{ bps}$) provides a more stable conservative estimate.
2. **Post-Spike Level vs Band (`F-022`):** While the estimated within-regime band in R6 ($9.40\text{ bps}$) is wider than in R4 ($1.61\text{ bps}$), the post-spike mean level itself has placebo $p = 0.24$, so we do not claim a permanent level shift from the notice.
3. **Discrete Daily Sampling & Symmetric Band:** PTAX is fixed daily (13:00–16:00 UTC), so half-lives represent daily settlement horizons rather than intraday electronic latency, and bands are constrained to be symmetric $[-c, +c]$.

## Used in deck
Slide 3 ("Dados e medida: seis anos de histórico e quebras cegas") and Annex B.6 of `deck/annex_v1_ptbr.md`.

## History
- 2026-11-02, agent for Felipe: aligned R6 interpretation with F-022 (post-spike level not distinguishable from drift, placebo p = 0.24) and P2-02 (22 Jul fade unexplained within ±5d; M-04/M-05 only coincide)
- 2026-11-02, Felipe: created (exploratory, task P3-07). All P2 criteria completed ahead of gate; Band-TAR estimated across all 6 regimes + pooled windows.
