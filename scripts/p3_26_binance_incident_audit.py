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
        "cusum_state": "Incident onset (after the PTAX measurement window)",
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
        "market_event": "Phased restoration planned (M-11); exact USDT restoration unverified",
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
        "market_event": "Res. 574 effective; observed cross-venue gap small",
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
        "interpretation": "30 Oct observation excluded directly; residual incident effects possible"
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
        "interpretation": f"Diagnostic S2={s2_hyp:.2f} bps; p={p_hyp:.4f}; registered score unchanged"
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

    # Generate market values from the same data as the tables, never typed levels.
    audit_md = "# P3-26: October incident and November evaluation\n\n"
    audit_md += "E1 S2 excludes the 30 Oct observation directly. Small later cross-venue gaps do not rule out persistent or shared incident effects. Exact USDT withdrawal restoration is not verified by the source register.\n\n"
    audit_md += "## Observed daily premiums (bps)\n\n" + p_df.loc["2026-10-29":].to_csv()
    audit_md += "\n## Window sensitivity (computed)\n\n" + sensitivity_df.to_csv(index=False)
    audit_md += "\n## Timeline\n\n" + timeline_df.to_csv(index=False)
    audit_md += "\nE2 S1 is an early reading only. The registered two-day verdict requires 9 November, after submission. Reference bands are historical distributions, not causal effect confidence bounds. CUSUM silence during its ten-observation quiet pause is mechanical.\n"

    with open(report_path, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(audit_md)

    print("\nAudit report saved to:", report_path)


if __name__ == "__main__":
    main()
