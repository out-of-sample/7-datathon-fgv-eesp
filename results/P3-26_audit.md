# P3-26: Audit of the Binance Security Incident (29–30 Oct 2026) as Confounder for November Readout

**Date:** 2026-11-07  
**Task:** P3-26 (`tasks/P3-26-november-exchange-confounder.md`)  
**Owner:** Economist (Felipe)  
**Related Findings:** F-035 (P3-20 E1 readout), F-014 (P3-03 monitor backtest), F-045  
**Primary Sources Opened:** `docs/sources.md` entries M-11, M-12  

---

## Executive Summary

On 29 October 2026 at 20:05 UTC, Binance experienced a major security incident compromising hot wallets and internal signing infrastructure, triggering an immediate suspension of cryptocurrency withdrawals (sources M-11, M-12; FBI/TRM Labs attributed to TraderTraitor / Lazarus). During the Brazilian PTAX window on 30 October 2026 (13:00–17:00 UTC), the Binance USDT/BRL premium plunged to **−30.3 bps**, while domestic venues remained normal (+18.6 bps on Foxbit, +17.4 bps on Mercado Bitcoin), opening an unprecedented **+49.0 bps** Foxbit − Binance gap.

This audit evaluates the mechanical and statistical consequences of this incident on the P3-20 prospective policy evaluation and the P3-03 CUSUM monitor:

1. **E1 (Res. BCB 574, effective 3 Nov 2026) Primary Statistic S2 is Completely Insulated:**  
   Under the pre-registered P3-20 rule (`9a522e9`), the event day `t0 = 30 Oct` is **excluded** from `S2 = mean(3–4 Nov) − mean(20 PTAX days ending 29 Oct)`. The 20-day pre-window ended at 17:00 UTC on 29 Oct, three hours *before* the 20:05 UTC attack occurred. The post-window (3–4 Nov) started four days later, after withdrawals had reopened and cross-venue parity had fully restored (Binance at +17.6 and +25.0 bps vs Foxbit at +16.6 and +22.0 bps; gaps of −1.0 and −3.0 bps).
2. **E1 Early Reading Statistic S1 was Contaminated (Justifying Pre-Registration Exclusion):**  
   `S1 = p[3 Nov] − p[30 Oct] = +47.9 bps` directly uses the 30 Oct anomaly as its baseline. P3-20 explicitly pre-registered on 3 Nov that S1 was contaminated by the 30 Oct Binance-only dip and could not serve as the verdict statistic.
3. **E2 (Res. BCB 589, effective 6 Nov 2026) Pre-Window Sensitivity is Minor (~2.3 bps):**  
   The 20-day pre-window for E2 (`t0 = 5 Nov`) spans 20 PTAX days ending 4 Nov and includes 30 Oct as 1 of its 20 days. This single anomalous day pulls down the 20-day pre-mean by 2.27 to 2.44 bps (from 18.21/18.38 bps to 15.94 bps). Relative to the pre-registered reference band of ±75 bps (`[-75.5, +59.8] bps`), a ~2.3 bps shift is negligible (~3% of the band) and does not alter the verdict rule, but is disclosed transparently.
4. **P3-03 CUSUM Monitor Silence is a Mechanical Pause Artifact:**  
   The 30 Oct dip triggered a downward CUSUM alarm on 30 Oct (`2026-10-30(-)` in `P3-03_backtest.csv`). By the pre-registered monitor specification, any alarm initiates a mandatory 10-PTAX-day pause (`QUIET = 10`), suppressing all alarms from 3 Nov through 16 Nov 2026. Therefore, the monitor's silence during the November evaluation windows is a mechanical consequence of the 30 Oct pause, **not** an informative non-alarm reading.

---

## 1. Verified Incident Timeline (S1)

From opened Binance official announcements (`M-11`, `M-12`), public blockchain intelligence reports, and the Brazilian market data:

| Timestamp (UTC) | Timestamp (BRT) | Event & Market State | Binance | Foxbit | Mercado Bitcoin | Foxbit − Binance Gap | CUSUM Monitor State |
|---|---|---|---|---|---|---|---|
| **2026-10-29 13:00–17:00** | 10:00–14:00 | Normal PTAX window (pre-incident) | +12.5 bps | +13.4 bps | +11.3 bps | +0.9 bps | Normal monitoring |
| **2026-10-29 20:05** | 17:05 | Attack onset; withdrawals suspended (M-11) | — | — | — | — | After-hours event |
| **2026-10-30 13:00–17:00** | 10:00–14:00 | PTAX window during withdrawal freeze | **−30.3 bps** | **+18.6 bps** | **+17.4 bps** | **+49.0 bps** | **Downward Alarm (sum < -24.5)** |
| **2026-10-31 to 11-01** | Weekend | 98% assets replenished; withdrawals reopen (M-11) | — | — | — | — | Weekend |
| **2026-11-02** | Holiday | Dia de Finados (no PTAX) | — | — | — | — | Holiday |
| **2026-11-03 13:00–17:00** | 10:00–14:00 | Res. 574 effective (E1 post-day 1) | +17.6 bps | +16.6 bps | — | −1.0 bps | Pause day 1/10 |
| **2026-11-04 13:00–17:00** | 10:00–14:00 | E1 post-day 2 (Copom / US midterms) | +25.0 bps | +22.0 bps | — | −3.0 bps | Pause day 2/10 |
| **2026-11-05 13:00–17:00** | 10:00–14:00 | E2 t0 (last day before Res. 589 art. 91) | +21.5 bps | +23.8 bps | — | +2.3 bps | Pause day 3/10 |
| **2026-11-06 13:00–17:00** | 10:00–14:00 | Res. 589 in force; US payrolls | +17.1 bps | +19.2 bps | — | +2.1 bps | Pause day 4/10 |

The table confirms that on 30 October 2026, the USDT/BRL premium on Binance decoupled sharply from both domestic Brazilian exchanges. The Foxbit − Binance gap exploded from +0.9 bps on 29 Oct to **+49.0 bps** on 30 Oct, and the Mercado Bitcoin − Binance gap exploded to **+47.7 bps**. By Tuesday 3 November, the cross-venue gap had completely vanished (−1.0 bps), proving that the price dislocation was transient and tied to the withdrawal freeze.

---

## 2. Methodological Mapping to P3-20 Evaluation (S2)

### A. E1 (Res. BCB 574): S2 is Insulated, S1 is Contaminated

- **Primary Statistic S2 (`mean[3–4 Nov] − mean[1–29 Oct]`):**  
  The pre-registered formula in `scripts/p3_20_live.py` (`stat(..., "S2")`) takes the pre-mean over `[t0-20, t0-1]` and post-mean over `[t0+1, t0+2]`.  
  With `t0 = 30 Oct`, `t0-1 = 29 Oct`.  
  Therefore, the pre-window terminates on 29 Oct at 17:00 UTC, exactly 3 hours and 5 minutes **before** the 20:05 UTC security incident began.  
  The post-window begins on 3 Nov, after withdrawals had reopened and cross-venue parity had normalized.  
  Result: Binance S2 = `21.32 bps − 19.23 bps = +2.09 bps` (`p = 0.897`). The verdict is completely free of the 30 Oct distortion.

- **Early Statistic S1 (`p[3 Nov] − p[30 Oct]`):**  
  `S1 = 17.60 − (−30.35) = +47.95 bps` (`p = 0.12`).  
  This statistic directly benchmarks the normalized 3 Nov price against the trough of the withdrawal panic. P3-20's registration on 3 Nov correctly diagnosed this in advance: *"For E1 it is not used for the verdict: the premium on 30 Oct was −30.3 bps, far below its usual level, so a plain rebound on 3 Nov would show as a rise. S2's pre-window excludes t0"* (`tasks/P3-20-live-predictions.md` line 47).

### B. E2 (Res. BCB 589): Sensitivity Analysis of 20-Day Pre-Window

For E2 (`t0 = 5 Nov`), the pre-window `[t0-20, t0-1]` spans the 20 PTAX days from 6 October 2026 through 4 November 2026, which contains 30 October as one observation.

| Specification | 20-Day Pre-Mean | Post-Mean (Observed / Illustrative) | S2 Statistic | Reference Band | Status |
|---|---|---|---|---|---|
| **Registered Rule (with 30 Oct)** | **15.94 bps** | — | — | −75.5 / +59.8 | **Pre-registered verdict rule** |
| Sensitivity: Exclude 30 Oct (19 days) | 18.38 bps | — | −2.44 bps shift | −75.5 / +59.8 | Diagnostic sensitivity check |
| Sensitivity: Replace 30 Oct with 15.0 bps | 18.21 bps | — | −2.27 bps shift | −75.5 / +59.8 | Diagnostic sensitivity check |

The mechanical downward pull on the pre-mean is **2.27 to 2.44 bps**. Because the two-sided 95% reference band has a half-width of ~75 bps, an adjustment of 2.3 bps cannot alter the statistical significance or falsification verdict. The registered rule is preserved without modification, and this sensitivity is disclosed in the report and slide annex.

---

## 3. Impact on P3-03 CUSUM Monitor (S2)

The CUSUM break detector (`scripts/p3_03_monitor.py`) flagged a downward break on 30 October 2026:
- Negative CUSUM sum crossed the calibrated threshold `h = 24.5` on 30 Oct 2026 (`2026-10-30(-)` in `results/tables/P3-03_backtest.csv`).
- By line 76 of `scripts/p3_03_monitor.py`:  
  ```python
  if max(sp, sm) > h:
      alarm[t] = 1 if sp >= sm else -1
      start = (zero_p if sp >= sm else zero_m) + 1
      sp = sm = 0.0
      resume = t + QUIET + 1  # QUIET = 10 PTAX days
  ```
- The 10 PTAX days following 30 Oct are:  
  1: 3 Nov, 2: 4 Nov, 3: 5 Nov, 4: 6 Nov, 5: 9 Nov, 6: 10 Nov, 7: 11 Nov, 8: 12 Nov, 9: 13 Nov, 10: 16 Nov.
- **Conclusion:** During the entire prospective testing period (3–16 November 2026), the CUSUM monitor is actively paused by design. The lack of an alarm during 3–4 Nov or 6 Nov is a mechanical artifact of the quiet period, **not** an empirical finding that the market had zero cumulative drift.

---

## 4. Teammate Review & Recommended Disclosure Language (S3)

### Recommended Disclosure for Finding F-035 / F-045
> *"Robustness disclosure (Binance security incident, 29–30 Oct 2026): An unauthorized hot-wallet withdrawal incident on Binance at 20:05 UTC on 29 Oct (M-11, M-12) prompted a temporary withdrawal suspension. During the 30 Oct PTAX window, Binance premium dislocated to −30.3 bps (Foxbit − Binance gap +49.0 bps). Under pre-registered P3-20 rule (9a522e9), E1 primary statistic S2 excludes 30 Oct by design (pre-window ended 29 Oct 17:00 UTC, 3 hours before the incident; post-window 3–4 Nov began after parity restored, gap −1.0 bps). S1 (+47.9 bps) directly measured recovery from this dip, justifying its pre-registered exclusion from the verdict. For E2, 30 Oct lowers the 20-day pre-mean by 2.3 bps, well within the ±75 bps reference band. Monitor silence is a mechanical 10-day quiet pause following the 30 Oct alarm."*

### Recommended Slide 10 / Annex Language (Portuguese)
> *"Nota metodológica (Auditoria do incidente Binance de 29–30/out): A suspensão temporária de saques da Binance em 29/out (20:05 UTC) gerou descolamento pontual em 30/out (−30,3 pb na Binance vs +18,6 pb na Foxbit). A métrica primária pré-registrada S2 para a Res. 574 exclui o dia 30/out por construção: a janela prévia encerrou-se 3h antes do ataque e o pós-evento (3–4/nov) iniciou-se após a normalização da paridade (gap Foxbit−Binance de −1,0 pb). Na Res. 589, o dia 30/out reduz a média prévia de 20 dias em apenas 2,3 pb (frente a uma banda de ±75 pb). O monitor CUSUM permaneceu em pausa regulamentar de 10 dias úteis."*
