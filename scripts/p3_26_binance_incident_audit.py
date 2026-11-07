r"""P3-26: Audit of Binance Security Incident (29-30 Oct 2026) as Confounder for November Readout.

Purpose:
  Map the chronological timeline of the 29-30 Oct 2026 Binance security incident (M-11, M-12)
  against the P3-20 prospective prediction windows (E1: Res. 574, E2: Res. 589) and the P3-03
  CUSUM monitor state. Explicitly evaluate the insulation of the pre-registered E1 primary
  statistic S2 versus the contamination of S1, quantify the pre-window sensitivity for E2,
  and explain why CUSUM monitor silence during 3-16 Nov is a mechanical pause artifact.

Inputs:
  - data/processed/P1-02_premium_daily.csv
  - data/processed/P3-20_premium_daily.csv
  - results/tables/P3-03_backtest.csv
  - results/tables/P3-20_reference.csv
  - results/tables/P3-20_reference_values.csv
  - docs/sources.md (M-11, M-12)

Outputs:
  - results/tables/P3-26_incident_timeline.csv
  - results/tables/P3-26_window_sensitivity.csv
  - results/P3-26_audit.md

Run:
  py scripts/p3_26_binance_incident_audit.py
"""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
PROC = ROOT / "data/processed"
TAB = ROOT / "results/tables"
RES = ROOT / "results"


def build_timeline(p_df):
    """Construct exact chronological timeline across the incident and evaluation windows."""
    rows = []
    # 1. 29 Oct PTAX window
    row_29 = p_df.loc[pd.Timestamp("2026-10-29")] if pd.Timestamp("2026-10-29") in p_df.index else None
    rows.append({
        "timestamp_utc": "2026-10-29 13:00-17:00",
        "timestamp_brt": "2026-10-29 10:00-14:00",
        "market_event": "Pre-incident normal trading (PTAX window)",
        "binance_premium_bps": round(row_29["Binance"], 1) if row_29 is not None else np.nan,
        "foxbit_premium_bps": round(row_29["Foxbit"], 1) if row_29 is not None else np.nan,
        "mb_premium_bps": round(row_29["Mercado Bitcoin"], 1) if row_29 is not None and not np.isnan(row_29["Mercado Bitcoin"]) else np.nan,
        "gap_foxbit_binance_bps": round(row_29["gap_foxbit"], 1) if row_29 is not None else np.nan,
        "gap_mb_binance_bps": round(row_29["gap_mb"], 1) if row_29 is not None and not np.isnan(row_29["gap_mb"]) else np.nan,
        "cusum_state": "Normal (cumulative monitoring)",
        "p3_20_window_role": "E1 pre-window final day (t0-1); clean pre-baseline"
    })

    # 2. 29 Oct Attack onset
    rows.append({
        "timestamp_utc": "2026-10-29 20:05",
        "timestamp_brt": "2026-10-29 17:05",
        "market_event": "Binance hot-wallet compromise & withdrawal freeze (M-11, M-12)",
        "binance_premium_bps": np.nan,
        "foxbit_premium_bps": np.nan,
        "mb_premium_bps": np.nan,
        "gap_foxbit_binance_bps": np.nan,
        "gap_mb_binance_bps": np.nan,
        "cusum_state": "Incident onset (after market close)",
        "p3_20_window_role": "Occurred 3h after 29 Oct PTAX window closed"
    })

    # 3. 30 Oct PTAX window
    row_30 = p_df.loc[pd.Timestamp("2026-10-30")] if pd.Timestamp("2026-10-30") in p_df.index else None
    rows.append({
        "timestamp_utc": "2026-10-30 13:00-17:00",
        "timestamp_brt": "2026-10-30 10:00-14:00",
        "market_event": "PTAX window during withdrawal suspension (sharp Binance-only dip)",
        "binance_premium_bps": round(row_30["Binance"], 1) if row_30 is not None else np.nan,
        "foxbit_premium_bps": round(row_30["Foxbit"], 1) if row_30 is not None else np.nan,
        "mb_premium_bps": round(row_30["Mercado Bitcoin"], 1) if row_30 is not None and not np.isnan(row_30["Mercado Bitcoin"]) else np.nan,
        "gap_foxbit_binance_bps": round(row_30["gap_foxbit"], 1) if row_30 is not None else np.nan,
        "gap_mb_binance_bps": round(row_30["gap_mb"], 1) if row_30 is not None else np.nan,
        "cusum_state": "Alarm triggered: Downward alarm 2026-10-30(-)",
        "p3_20_window_role": "E1 t0 (EXCLUDED from S2 pre-mean; contaminates S1 baseline)"
    })

    # 4. 31 Oct - 1 Nov Weekend restoration
    rows.append({
        "timestamp_utc": "2026-10-31 to 2026-11-01",
        "timestamp_brt": "2026-10-31 to 2026-11-01",
        "market_event": "Withdrawals progressively restored; 98% assets replenished (M-11)",
        "binance_premium_bps": np.nan,
        "foxbit_premium_bps": np.nan,
        "mb_premium_bps": np.nan,
        "gap_foxbit_binance_bps": np.nan,
        "gap_mb_binance_bps": np.nan,
        "cusum_state": "Mandatory quiet pause day 0 (weekend)",
        "p3_20_window_role": "Weekend (no PTAX window)"
    })

    # 5. 2 Nov Holiday
    rows.append({
        "timestamp_utc": "2026-11-02",
        "timestamp_brt": "2026-11-02",
        "market_event": "Dia de Finados bank holiday in Brazil",
        "binance_premium_bps": np.nan,
        "foxbit_premium_bps": np.nan,
        "mb_premium_bps": np.nan,
        "gap_foxbit_binance_bps": np.nan,
        "gap_mb_binance_bps": np.nan,
        "cusum_state": "Mandatory quiet pause day 0 (holiday)",
        "p3_20_window_role": "Holiday (no PTAX window)"
    })

    # 6. 3 Nov E1 post-day 1
    row_03 = p_df.loc[pd.Timestamp("2026-11-03")] if pd.Timestamp("2026-11-03") in p_df.index else None
    rows.append({
        "timestamp_utc": "2026-11-03 13:00-17:00",
        "timestamp_brt": "2026-11-03 10:00-14:00",
        "market_event": "Res. 574 effective; cross-venue parity restored",
        "binance_premium_bps": round(row_03["Binance"], 1) if row_03 is not None else np.nan,
        "foxbit_premium_bps": round(row_03["Foxbit"], 1) if row_03 is not None else np.nan,
        "mb_premium_bps": round(row_03["Mercado Bitcoin"], 1) if row_03 is not None and not np.isnan(row_03["Mercado Bitcoin"]) else np.nan,
        "gap_foxbit_binance_bps": round(row_03["gap_foxbit"], 1) if row_03 is not None else np.nan,
        "gap_mb_binance_bps": round(row_03["gap_mb"], 1) if row_03 is not None and not np.isnan(row_03["gap_mb"]) else np.nan,
        "cusum_state": "Pause day 1/10 (QUIET=10 active)",
        "p3_20_window_role": "E1 post-day 1 (t0+1); S1 reading (+47.9 bps vs 30 Oct)"
    })

    # 7. 4 Nov E1 post-day 2
    row_04 = p_df.loc[pd.Timestamp("2026-11-04")] if pd.Timestamp("2026-11-04") in p_df.index else None
    rows.append({
        "timestamp_utc": "2026-11-04 13:00-17:00",
        "timestamp_brt": "2026-11-04 10:00-14:00",
        "market_event": "E1 post-day 2; Copom decision evening; US midterms",
        "binance_premium_bps": round(row_04["Binance"], 1) if row_04 is not None else np.nan,
        "foxbit_premium_bps": round(row_04["Foxbit"], 1) if row_04 is not None else np.nan,
        "mb_premium_bps": round(row_04["Mercado Bitcoin"], 1) if row_04 is not None and not np.isnan(row_04["Mercado Bitcoin"]) else np.nan,
        "gap_foxbit_binance_bps": round(row_04["gap_foxbit"], 1) if row_04 is not None else np.nan,
        "gap_mb_binance_bps": round(row_04["gap_mb"], 1) if row_04 is not None and not np.isnan(row_04["gap_mb"]) else np.nan,
        "cusum_state": "Pause day 2/10 (QUIET=10 active)",
        "p3_20_window_role": "E1 post-day 2 (t0+2); S2 evaluation window completes"
    })

    # 8. 5 Nov E2 t0
    row_05 = p_df.loc[pd.Timestamp("2026-11-05")] if pd.Timestamp("2026-11-05") in p_df.index else None
    rows.append({
        "timestamp_utc": "2026-11-05 13:00-17:00",
        "timestamp_brt": "2026-11-05 10:00-14:00",
        "market_event": "Last PTAX day before Res. 589 art. 91 ban (E2 t0)",
        "binance_premium_bps": round(row_05["Binance"], 1) if row_05 is not None else np.nan,
        "foxbit_premium_bps": round(row_05["Foxbit"], 1) if row_05 is not None else np.nan,
        "mb_premium_bps": round(row_05["Mercado Bitcoin"], 1) if row_05 is not None and not np.isnan(row_05["Mercado Bitcoin"]) else np.nan,
        "gap_foxbit_binance_bps": round(row_05["gap_foxbit"], 1) if row_05 is not None else np.nan,
        "gap_mb_binance_bps": round(row_05["gap_mb"], 1) if row_05 is not None and not np.isnan(row_05["gap_mb"]) else np.nan,
        "cusum_state": "Pause day 3/10 (QUIET=10 active)",
        "p3_20_window_role": "E2 t0 (pre-window ending on 4 Nov contains 30 Oct)"
    })

    # 9. 6 Nov E2 post-day 1
    row_06 = p_df.loc[pd.Timestamp("2026-11-06")] if pd.Timestamp("2026-11-06") in p_df.index else None
    rows.append({
        "timestamp_utc": "2026-11-06 13:00-17:00",
        "timestamp_brt": "2026-11-06 10:00-14:00",
        "market_event": "Res. 589 art. 91 ban in force; US payrolls (10:30 BRT)",
        "binance_premium_bps": round(row_06["Binance"], 1) if row_06 is not None else np.nan,
        "foxbit_premium_bps": round(row_06["Foxbit"], 1) if row_06 is not None else np.nan,
        "mb_premium_bps": round(row_06["Mercado Bitcoin"], 1) if row_06 is not None and not np.isnan(row_06["Mercado Bitcoin"]) else np.nan,
        "gap_foxbit_binance_bps": round(row_06["gap_foxbit"], 1) if row_06 is not None else np.nan,
        "gap_mb_binance_bps": round(row_06["gap_mb"], 1) if row_06 is not None and not np.isnan(row_06["gap_mb"]) else np.nan,
        "cusum_state": "Pause day 4/10 (QUIET=10 active through 16 Nov)",
        "p3_20_window_role": "E2 post-day 1 (t0+1); S1 early reading window"
    })

    return pd.DataFrame(rows)


def compute_sensitivity(p_df, ref_vals):
    """Compute pre-mean and S2 sensitivity with/without 30 Oct for E1 and E2."""
    rows = []
    bin_vals = ref_vals[(ref_vals.series == "Binance") & (ref_vals.statistic == "S2")].value_bps.to_numpy()

    # --- E1: Res. 574 (t0 = 2026-10-30) ---
    i_e1 = p_df.index.get_loc(pd.Timestamp("2026-10-30"))
    pre_e1_reg = p_df.iloc[i_e1-20:i_e1]["Binance"]  # 20 days ending 29 Oct
    post_e1 = p_df.iloc[i_e1+1:i_e1+3]["Binance"]     # 3 Nov, 4 Nov

    pre_m_reg = pre_e1_reg.mean()
    post_m = post_e1.mean()
    s2_reg = post_m - pre_m_reg
    k_reg = int((np.abs(bin_vals) >= abs(s2_reg)).sum())
    p_reg = (k_reg + 1) / (len(bin_vals) + 1)

    rows.append({
        "event": "E1 (Res. 574)",
        "specification": "Registered P3-20 rule (excludes 30 Oct from pre-mean)",
        "pre_window_dates": f"{pre_e1_reg.index[0].date()}..{pre_e1_reg.index[-1].date()}",
        "pre_mean_bps": round(pre_m_reg, 2),
        "post_window_dates": f"{post_e1.index[0].date()}..{post_e1.index[-1].date()}",
        "post_mean_bps": round(post_m, 2),
        "s2_bps": round(s2_reg, 2),
        "s2_reference_band_bps": "-75.5 / +59.8",
        "p_two_sided": round(p_reg, 4),
        "status": "registered_verdict",
        "interpretation": "Insulated from 30 Oct dip; pre-window ended 3h before hack"
    })

    # E1 hypothetical variant: 20 days ending on 30 Oct (including 30 Oct)
    pre_e1_hyp = p_df.iloc[i_e1-19:i_e1+1]["Binance"]
    pre_m_hyp = pre_e1_hyp.mean()
    s2_hyp = post_m - pre_m_hyp
    k_hyp = int((np.abs(bin_vals) >= abs(s2_hyp)).sum())
    p_hyp = (k_hyp + 1) / (len(bin_vals) + 1)

    rows.append({
        "event": "E1 (Res. 574)",
        "specification": "Diagnostic check (including 30 Oct in 20d pre-window)",
        "pre_window_dates": f"{pre_e1_hyp.index[0].date()}..{pre_e1_hyp.index[-1].date()}",
        "pre_mean_bps": round(pre_m_hyp, 2),
        "post_window_dates": f"{post_e1.index[0].date()}..{post_e1.index[-1].date()}",
        "post_mean_bps": round(post_m, 2),
        "s2_bps": round(s2_hyp, 2),
        "s2_reference_band_bps": "-75.5 / +59.8",
        "p_two_sided": round(p_hyp, 4),
        "status": "diagnostic_sensitivity_only",
        "interpretation": "30 Oct dip lowers pre-mean by 1.75 bps, raising S2 to +3.8 bps; still p=0.74 (well within band)"
    })

    # --- E2: Res. 589 (t0 = 2026-11-05) ---
    pre_e2_reg = p_df.loc[:pd.Timestamp("2026-11-04")].tail(20)["Binance"]
    pre_m_e2_reg = pre_e2_reg.mean()

    # Pre-window without 30 Oct (19 days)
    pre_e2_no30 = pre_e2_reg.drop(pd.Timestamp("2026-10-30"))
    pre_m_e2_no30 = pre_e2_no30.mean()

    # Pre-window replacing 30 Oct with neutral ~15.0 bps
    pre_e2_replaced = pre_e2_reg.copy()
    pre_e2_replaced.loc[pd.Timestamp("2026-10-30")] = 15.0
    pre_m_e2_replaced = pre_e2_replaced.mean()

    rows.append({
        "event": "E2 (Res. 589)",
        "specification": "Registered P3-20 rule (20d pre-window ending 4 Nov, contains 30 Oct)",
        "pre_window_dates": f"{pre_e2_reg.index[0].date()}..{pre_e2_reg.index[-1].date()}",
        "pre_mean_bps": round(pre_m_e2_reg, 2),
        "post_window_dates": "pending (6 Nov / 9 Nov)",
        "post_mean_bps": np.nan,
        "s2_bps": np.nan,
        "s2_reference_band_bps": "-75.5 / +59.8",
        "p_two_sided": np.nan,
        "status": "registered_baseline",
        "interpretation": "30 Oct (-30.3 bps) pulls down 20d pre-mean by ~2.4 bps vs 19d unweighted mean"
    })

    rows.append({
        "event": "E2 (Res. 589)",
        "specification": "Diagnostic check (excluding 30 Oct from pre-window, 19 days)",
        "pre_window_dates": f"{pre_e2_no30.index[0].date()}..{pre_e2_no30.index[-1].date()} (excl 30 Oct)",
        "pre_mean_bps": round(pre_m_e2_no30, 2),
        "post_window_dates": "pending (6 Nov / 9 Nov)",
        "post_mean_bps": np.nan,
        "s2_bps": np.nan,
        "s2_reference_band_bps": "-75.5 / +59.8",
        "p_two_sided": np.nan,
        "status": "diagnostic_sensitivity_only",
        "interpretation": "Pre-mean rises from 15.94 to 18.38 bps (+2.44 bps shift). Small relative to +-75 bps band"
    })

    rows.append({
        "event": "E2 (Res. 589)",
        "specification": "Diagnostic check (replacing 30 Oct with neutral 15.0 bps baseline)",
        "pre_window_dates": f"{pre_e2_reg.index[0].date()}..{pre_e2_reg.index[-1].date()} (30 Oct=15 bps)",
        "pre_mean_bps": round(pre_m_e2_replaced, 2),
        "post_window_dates": "pending (6 Nov / 9 Nov)",
        "post_mean_bps": np.nan,
        "s2_bps": np.nan,
        "s2_reference_band_bps": "-75.5 / +59.8",
        "p_two_sided": np.nan,
        "status": "diagnostic_sensitivity_only",
        "interpretation": "Pre-mean rises by +2.27 bps to 18.21 bps. Pre-registered score remains unchanged"
    })

    return pd.DataFrame(rows)


def main():
    p_df = pd.read_csv(PROC / "P3-20_premium_daily.csv", parse_dates=["date_brt"], index_col="date_brt").sort_index()
    ref_vals = pd.read_csv(TAB / "P3-20_reference_values.csv", parse_dates=["t0"])

    timeline_df = build_timeline(p_df)
    sensitivity_df = compute_sensitivity(p_df, ref_vals)

    TAB.mkdir(parents=True, exist_ok=True)
    timeline_path = TAB / "P3-26_incident_timeline.csv"
    sensitivity_path = TAB / "P3-26_window_sensitivity.csv"
    report_path = RES / "P3-26_audit.md"

    # Write CSVs with CRLF
    timeline_df.to_csv(timeline_path, index=False, lineterminator="\r\n")
    sensitivity_df.to_csv(sensitivity_path, index=False, lineterminator="\r\n")

    print("Timeline saved to:", timeline_path)
    print(timeline_df.to_string(index=False))

    print("\nSensitivity saved to:", sensitivity_path)
    print(sensitivity_df.to_string(index=False))

    # Generate comprehensive audit report
    audit_md = f"""# P3-26: Audit of the Binance Security Incident (29–30 Oct 2026) as Confounder for November Readout

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
"""

    with open(report_path, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(audit_md)

    print("\nAudit report saved to:", report_path)


if __name__ == "__main__":
    main()
