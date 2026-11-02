r"""P3-07: Threshold model of the no-arbitrage band (Band-TAR) across regimes.

Purpose:
  Estimates symmetric Band-TAR(1) models (Obstfeld & Taylor 1997) of the USDT/BRL premium
  over PTAX across structural regimes identified by Bai-Perron / LWZ break tests (P2-02).
  Within each regime r with equilibrium parity \mu_r, arbitrageurs only act when deviations
  |z_{t-1}| exceed transaction and friction costs c:
      \Delta z_t = \beta_in * z_{t-1} * 1{|z_{t-1}| <= c}
                 + \beta_out * (z_{t-1} - sign(z_{t-1}) * c) * 1{|z_{t-1}| > c} + \varepsilon_t
  Measures:
    1. Implied arbitrage band half-width c (in bps) around regime mean and around 0 parity.
    2. Outside-band reversion speed \beta_out and implied half-life t_{1/2} = ln(0.5)/ln(1 + \beta_out).
    3. Inside-band persistence \beta_in (and comparison with restricted \beta_in = 0).
    4. Moving block-bootstrap 95% confidence intervals (500 reps, seed=20261102).
    5. In-sample and out-of-sample (80/20 split) RMSE comparison against naive persistence
       (\Delta y_t = 0) and linear AR(1) without threshold (prompt.md Rule 2).

Inputs:
  data/processed/P1-02_premium_daily.csv
  results/tables/P2-02_breaks.csv

Outputs:
  results/tables/P3-07_band_tar.csv
  results/figures/P3-07_band_tar.png

How to run:
  python scripts/p3_07_tar.py
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
PROC = ROOT / "data/processed"
TABLES = ROOT / "results/tables"
FIGURES = ROOT / "results/figures"

TABLES.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)

# 1. Load data
df = pd.read_csv(PROC / "P1-02_premium_daily.csv", parse_dates=["date_brt"], index_col="date_brt")
series = df["premium_bps"].dropna()

breaks_df = pd.read_csv(TABLES / "P2-02_breaks.csv")
prem_breaks = breaks_df[breaks_df["series"] == "premium_bps"]["first_day_new_regime"].tolist()

# Define regimes from P2-02 breaks
# Breaks: '2021-07-26', '2024-08-20', '2025-07-08', '2026-06-24', '2026-07-22'
regimes = [
    {
        "id": "R1",
        "name": "Regime 1: Early crypto friction (Oct 2020 – Jul 2021)",
        "short_name": "R1: Early Friction",
        "start": "2020-10-13",
        "end": "2021-07-23",
    },
    {
        "id": "R2",
        "name": "Regime 2: Binance leverage cap to CVM settlement (Jul 2021 – Aug 2024)",
        "short_name": "R2: Post-Cap / Pre-CVM",
        "start": "2021-07-26",
        "end": "2024-08-19",
    },
    {
        "id": "R3",
        "name": "Regime 3: Post-settlement to tick cut (Aug 2024 – Jul 2025)",
        "short_name": "R3: Pre-Tick Cut",
        "start": "2024-08-20",
        "end": "2025-07-07",
    },
    {
        "id": "R4",
        "name": "Regime 4: Pre-notice corridor (Jul 2025 – Jun 2026)",
        "short_name": "R4: Pre-Notice",
        "start": "2025-07-08",
        "end": "2026-06-23",
    },
    {
        "id": "R5",
        "name": "Regime 5: Acute post-notice spike (Jun 2026 – Jul 2026)",
        "short_name": "R5: Acute Spike",
        "start": "2026-06-24",
        "end": "2026-07-21",
    },
    {
        "id": "R6",
        "name": "Regime 6: Post-adaptation plateau (Jul 2026 – Oct 2026)",
        "short_name": "R6: Adaptation Plateau",
        "start": "2026-07-22",
        "end": "2026-10-30",
    },
    {
        "id": "Pooled_Pre",
        "name": "Pooled Pre-Notice Corridor (Jul 2025 – Jun 2026)",
        "short_name": "Pooled Pre-Notice",
        "start": "2025-07-08",
        "end": "2026-06-23",
    },
    {
        "id": "Pooled_Post",
        "name": "Pooled Post-Notice (Acute + Plateau, Jun 2026 – Oct 2026)",
        "short_name": "Pooled Post-Notice",
        "start": "2026-06-24",
        "end": "2026-10-30",
    },
    {
        "id": "Full",
        "name": "Full Sample (Oct 2020 – Oct 2026)",
        "short_name": "Full Sample",
        "start": "2020-10-13",
        "end": "2026-10-30",
    },
]


def fit_band_tar(y_series, estimate_beta_in=True, n_grid=150, min_pct=0.15):
    """Grid search over threshold c for symmetric Band-TAR(1)."""
    y = np.asarray(y_series, dtype=float)
    dz = np.diff(y)
    z_lag = y[:-1]
    abs_z_lag = np.abs(z_lag)
    n = len(dz)
    if n < 10:
        return None

    p_low, p_high = np.percentile(abs_z_lag, 10), np.percentile(abs_z_lag, 85)
    if p_high <= p_low:
        return None

    candidates = np.linspace(p_low, p_high, n_grid)
    best_ssr = np.inf
    best_fit = None

    for c in candidates:
        inside = abs_z_lag <= c
        outside = ~inside
        n_in = int(np.sum(inside))
        n_out = int(np.sum(outside))
        if n_in < min_pct * n or n_out < min_pct * n:
            continue

        x_out = (z_lag - np.sign(z_lag) * c) * outside
        if estimate_beta_in:
            x_in = z_lag * inside
            X = np.column_stack([x_in, x_out])
            try:
                beta = np.linalg.solve(X.T @ X, X.T @ dz)
                pred = X @ beta
                ssr = float(np.sum((dz - pred) ** 2))
                b_in, b_out = float(beta[0]), float(beta[1])
            except Exception:
                continue
        else:
            X = x_out[:, None]
            try:
                beta = np.linalg.solve(X.T @ X, X.T @ dz)
                pred = X @ beta
                ssr = float(np.sum((dz - pred) ** 2))
                b_in, b_out = 0.0, float(beta[0])
            except Exception:
                continue

        if ssr < best_ssr:
            best_ssr = ssr
            best_fit = {
                "c": float(c),
                "beta_in": b_in,
                "beta_out": b_out,
                "ssr": ssr,
                "rmse": float(np.sqrt(ssr / n)),
                "n_in": n_in,
                "n_out": n_out,
                "pct_in": float(n_in / n),
                "pct_out": float(n_out / n),
                "pred": pred,
            }
    return best_fit


def calc_half_life(beta_out):
    """Implied half-life in trading days: ln(0.5) / ln(1 + beta_out)."""
    if beta_out <= -1.0:
        return 1.0  # complete adjustment or overshoot within 1 trading day
    elif beta_out < 0.0 and (1.0 + beta_out) > 0.0:
        return float(np.log(0.5) / np.log(1.0 + beta_out))
    else:
        return np.nan


def block_bootstrap(y_series, n_reps=500, seed=20261102):
    """Moving block bootstrap for 95% confidence intervals of Band-TAR parameters."""
    rng = np.random.default_rng(seed)
    y = np.asarray(y_series, dtype=float)
    n = len(y)
    b_len = 5 if n >= 40 else 3
    n_blocks = int(np.ceil(n / b_len))

    boot_c, boot_bout, boot_bin, boot_hl = [], [], [], []

    for _ in range(n_reps):
        starts = rng.integers(0, n - b_len + 1, size=n_blocks)
        sample = np.concatenate([y[st : st + b_len] for st in starts])[:n]
        res = fit_band_tar(sample, estimate_beta_in=True, n_grid=60)
        if res is not None:
            boot_c.append(res["c"])
            boot_bin.append(res["beta_in"])
            boot_bout.append(res["beta_out"])
            hl = calc_half_life(res["beta_out"])
            boot_hl.append(hl)

    def ci(arr):
        valid = [x for x in arr if not np.isnan(x)]
        if len(valid) >= 50:
            return float(np.percentile(valid, 2.5)), float(np.percentile(valid, 97.5))
        return np.nan, np.nan

    return {
        "c_ci": ci(boot_c),
        "beta_in_ci": ci(boot_bin),
        "beta_out_ci": ci(boot_bout),
        "hl_ci": ci(boot_hl),
        "n_valid": len(boot_c),
    }


# 2. Main estimation loop
records = []
regime_fits = {}

print("Fitting Band-TAR models across regimes...\n")

for reg in regimes:
    sub = series.loc[reg["start"] : reg["end"]].dropna()
    n_obs = len(sub)
    mean_val = float(sub.mean())
    sd_val = float(sub.std())

    # Demeaned series z_t = y_t - \mu_r
    z_demeaned = sub - mean_val
    # Raw series around zero parity
    z_zero = sub

    # Fit unrestricted Band-TAR (around \mu_r)
    fit_unres = fit_band_tar(z_demeaned, estimate_beta_in=True)
    # Fit restricted Band-TAR (\beta_in = 0)
    fit_res = fit_band_tar(z_demeaned, estimate_beta_in=False)
    # Fit Band-TAR around 0 parity
    fit_0 = fit_band_tar(z_zero, estimate_beta_in=True)

    if fit_unres is None:
        print(f"Skipping {reg['id']}: insufficient observations.")
        continue

    # Implied half-life
    hl = calc_half_life(fit_unres["beta_out"])

    # Linear AR(1) baseline without threshold: \Delta z_t = \beta z_{t-1} + \varepsilon_t
    dz = np.diff(z_demeaned.values)
    z_lag = z_demeaned.values[:-1]
    n_diff = len(dz)

    b_ar = float(np.linalg.lstsq(z_lag[:, None], dz, rcond=None)[0][0])
    pred_ar = z_lag * b_ar
    rmse_ar_in = float(np.sqrt(np.mean((dz - pred_ar) ** 2)))

    # Naive RW persistence baseline: \Delta y_t = 0
    rmse_rw_in = float(np.sqrt(np.mean(dz ** 2)))
    rmse_tar_in = fit_unres["rmse"]

    # Out-of-sample evaluation (chronological 80/20 train/test split)
    n_train = int(np.floor(n_obs * 0.80))
    if n_train >= 15 and (n_obs - n_train) >= 4:
        train_y = z_demeaned.values[:n_train]
        test_y = z_demeaned.values[n_train:]

        fit_train = fit_band_tar(train_y, estimate_beta_in=True, n_grid=100)
        dz_tr = np.diff(train_y)
        z_lag_tr = train_y[:-1]
        b_ar_tr = float(np.linalg.lstsq(z_lag_tr[:, None], dz_tr, rcond=None)[0][0])

        test_z_lag = z_demeaned.values[n_train - 1 : -1]
        test_dz = np.diff(z_demeaned.values[n_train - 1 :])

        # OOS RW
        rmse_rw_oos = float(np.sqrt(np.mean(test_dz ** 2)))
        # OOS AR(1)
        rmse_ar_oos = float(np.sqrt(np.mean((test_dz - test_z_lag * b_ar_tr) ** 2)))

        # OOS Band-TAR
        if fit_train is not None:
            c_tr, bi_tr, bo_tr = fit_train["c"], fit_train["beta_in"], fit_train["beta_out"]
            in_test = np.abs(test_z_lag) <= c_tr
            tar_pred_oos = np.where(in_test, bi_tr * test_z_lag, bo_tr * (test_z_lag - np.sign(test_z_lag) * c_tr))
            rmse_tar_oos = float(np.sqrt(np.mean((test_dz - tar_pred_oos) ** 2)))
        else:
            rmse_tar_oos = np.nan
    else:
        rmse_rw_oos, rmse_ar_oos, rmse_tar_oos = np.nan, np.nan, np.nan

    # Block bootstrap CIs
    boot = block_bootstrap(z_demeaned.values, n_reps=500, seed=20261102)

    rec = {
        "regime_id": reg["id"],
        "regime_name": reg["name"],
        "short_name": reg["short_name"],
        "start_date": reg["start"],
        "end_date": reg["end"],
        "n_obs": n_obs,
        "mean_bps": round(mean_val, 2),
        "sd_bps": round(sd_val, 2),
        # Band-TAR around regime mean
        "band_c_bps": round(fit_unres["c"], 2),
        "c_ci95_low": round(boot["c_ci"][0], 2),
        "c_ci95_high": round(boot["c_ci"][1], 2),
        "pct_inside": round(fit_unres["pct_in"] * 100, 1),
        "pct_outside": round(fit_unres["pct_out"] * 100, 1),
        "beta_in": round(fit_unres["beta_in"], 3),
        "beta_in_ci95_low": round(boot["beta_in_ci"][0], 3),
        "beta_in_ci95_high": round(boot["beta_in_ci"][1], 3),
        "beta_out": round(fit_unres["beta_out"], 3),
        "beta_out_ci95_low": round(boot["beta_out_ci"][0], 3),
        "beta_out_ci95_high": round(boot["beta_out_ci"][1], 3),
        "half_life_days": round(hl, 2) if not np.isnan(hl) else np.nan,
        "hl_ci95_low": round(boot["hl_ci"][0], 2) if not np.isnan(boot["hl_ci"][0]) else np.nan,
        "hl_ci95_high": round(boot["hl_ci"][1], 2) if not np.isnan(boot["hl_ci"][1]) else np.nan,
        # Restricted Band-TAR (\beta_in = 0)
        "c_restricted_bps": round(fit_res["c"], 2) if fit_res else np.nan,
        "beta_out_restricted": round(fit_res["beta_out"], 3) if fit_res else np.nan,
        "rmse_tar_restricted": round(fit_res["rmse"], 2) if fit_res else np.nan,
        # Band-TAR around 0 parity
        "band_c_zero_bps": round(fit_0["c"], 2) if fit_0 else np.nan,
        "beta_out_zero": round(fit_0["beta_out"], 3) if fit_0 else np.nan,
        # Baselines: In-Sample RMSE
        "rmse_rw_in": round(rmse_rw_in, 2),
        "rmse_ar1_in": round(rmse_ar_in, 2),
        "rmse_tar_in": round(rmse_tar_in, 2),
        "gain_vs_rw_in_pct": round(100 * (rmse_rw_in - rmse_tar_in) / rmse_rw_in, 1),
        "gain_vs_ar1_in_pct": round(100 * (rmse_ar_in - rmse_tar_in) / rmse_ar_in, 1),
        # Baselines: Out-of-Sample RMSE
        "rmse_rw_oos": round(rmse_rw_oos, 2) if not np.isnan(rmse_rw_oos) else np.nan,
        "rmse_ar1_oos": round(rmse_ar_oos, 2) if not np.isnan(rmse_ar_oos) else np.nan,
        "rmse_tar_oos": round(rmse_tar_oos, 2) if not np.isnan(rmse_tar_oos) else np.nan,
    }
    records.append(rec)
    regime_fits[reg["id"]] = {
        "fit": fit_unres,
        "series": z_demeaned,
        "mean": mean_val,
        "sd": sd_val,
        "boot": boot,
    }

    print(f"[{reg['id']}] {reg['short_name']:25s} | c={rec['band_c_bps']:5.1f} bps (CI {rec['c_ci95_low']} to {rec['c_ci95_high']}) | "
          f"b_out={rec['beta_out']:5.2f} | hl={rec['half_life_days']:4.2f}d | "
          f"RMSE: RW={rec['rmse_rw_in']:5.2f}, AR={rec['rmse_ar1_in']:5.2f}, TAR={rec['rmse_tar_in']:5.2f}")

res_df = pd.DataFrame(records)
out_csv = TABLES / "P3-07_band_tar.csv"
res_df.to_csv(out_csv, index=False)
print(f"\nSaved Band-TAR table to {out_csv}")


# 3. Generate Publication Figure
fig, axes = plt.subplots(2, 2, figsize=(14, 11), dpi=300)
plt.subplots_adjust(hspace=0.32, wspace=0.25)

# Color palette
c_blue = "#2563eb"
c_red = "#dc2626"
c_slate = "#475569"
c_green = "#16a34a"
c_amber = "#d97706"

# Panel A: Arbitrage Band Threshold c across Core Regimes
ax_a = axes[0, 0]
core_ids = ["R1", "R2", "R3", "R4", "R5", "R6", "Pooled_Post"]
core_df = res_df[res_df["regime_id"].isin(core_ids)].copy().reset_index(drop=True)
x_pos = np.arange(len(core_df))

bars = ax_a.bar(
    x_pos,
    core_df["band_c_bps"],
    yerr=[core_df["band_c_bps"] - core_df["c_ci95_low"], core_df["c_ci95_high"] - core_df["band_c_bps"]],
    capsize=5,
    color=[c_slate, c_slate, c_slate, c_green, c_red, c_amber, "#7c3aed"],
    alpha=0.85,
    edgecolor="black",
    linewidth=0.8,
)
ax_a.set_xticks(x_pos)
ax_a.set_xticklabels([r["short_name"].replace(": ", "\n") for _, r in core_df.iterrows()], fontsize=8)
ax_a.set_ylabel("Implied Arbitrage Band Threshold $c$ (bps)", fontsize=9, fontweight="bold")
ax_a.set_title("A. No-Arbitrage Band Width across Regimes (95% Bootstrap CI)", fontsize=10, fontweight="bold")
ax_a.grid(True, linestyle=":", alpha=0.5, axis="y")

# Annotate values
for bar, val in zip(bars, core_df["band_c_bps"]):
    ax_a.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2.5, f"{val:.1f}", ha="center", va="bottom", fontsize=8, fontweight="bold")
ax_a.set_ylim(0, max(core_df["c_ci95_high"].fillna(60)) * 1.15)


# Panel B: Mean Reversion Speed & Half-Life
ax_b = axes[0, 1]
ax_b2 = ax_b.twinx()

p1 = ax_b.plot(x_pos, core_df["beta_out"], marker="o", lw=2, color=c_red, label=r"Outside Reversion $\beta_{\mathrm{out}}$")
ax_b.set_ylabel(r"Outside Reversion Speed $\beta_{\mathrm{out}}$ (per day)", color=c_red, fontsize=9, fontweight="bold")
ax_b.tick_params(axis="y", labelcolor=c_red)
ax_b.set_ylim(-1.6, 0.0)

p2 = ax_b2.plot(x_pos, core_df["half_life_days"], marker="s", lw=2, linestyle="--", color=c_blue, label=r"Implied Half-Life $t_{1/2}$")
ax_b2.set_ylabel("Reversion Half-Life $t_{1/2}$ (Trading Days)", color=c_blue, fontsize=9, fontweight="bold")
ax_b2.tick_params(axis="y", labelcolor=c_blue)
ax_b2.set_ylim(0, 2.5)

ax_b.set_xticks(x_pos)
ax_b.set_xticklabels([r["short_name"].replace(": ", "\n") for _, r in core_df.iterrows()], fontsize=8)
ax_b.set_title("B. Arbitrage Reversion Speed & Half-Life across Regimes", fontsize=10, fontweight="bold")
ax_b.grid(True, linestyle=":", alpha=0.5)

lines = p1 + p2
labels = [l.get_label() for l in lines]
ax_b.legend(lines, labels, loc="upper right", fontsize=8, framealpha=0.9)


# Panel C: Nonlinear Threshold Adjustment Functions (R4 vs R5 vs R6)
ax_c = axes[1, 0]
z_grid = np.linspace(-60, 60, 300)

for reg_id, col, lab, ls in [
    ("R4", c_green, "R4: Pre-Notice (c = 1.6 bps, t_{1/2} = 1.0d)", "-"),
    ("R5", c_red, "R5: Acute Spike (c = 42.2 bps, t_{1/2} = 1.0d)", "-"),
    ("R6", c_amber, "R6: Plateau (c = 9.4 bps, t_{1/2} = 0.2d)", "--"),
    ("Pooled_Post", "#7c3aed", "Post-Notice Pooled (c = 32.4 bps, t_{1/2} = 1.6d)", ":"),
]:
    f = regime_fits[reg_id]["fit"]
    c_val = f["c"]
    b_in = f["beta_in"]
    b_out = f["beta_out"]

    dz_curve = np.where(
        np.abs(z_grid) <= c_val,
        b_in * z_grid,
        b_out * (z_grid - np.sign(z_grid) * c_val),
    )
    ax_c.plot(z_grid, dz_curve, color=col, lw=2, linestyle=ls, label=lab)
    # Mark threshold lines
    ax_c.axvline(c_val, color=col, linestyle=":", alpha=0.4)
    ax_c.axvline(-c_val, color=col, linestyle=":", alpha=0.4)

ax_c.axhline(0, color="black", lw=0.8, linestyle="-")
ax_c.axvline(0, color="black", lw=0.8, linestyle="-")
ax_c.set_xlabel(r"Lagged Deviation from Regime Mean $z_{t-1} = y_{t-1} - \mu_r$ (bps)", fontsize=9, fontweight="bold")
ax_c.set_ylabel(r"Expected Adjustment $\Delta z_t$ (bps)", fontsize=9, fontweight="bold")
ax_c.set_title(r"C. Nonlinear Arbitrage Adjustment Functions $\Delta z_t(z_{t-1})$", fontsize=10, fontweight="bold")
ax_c.grid(True, linestyle=":", alpha=0.5)
ax_c.legend(loc="lower left", fontsize=7.5, framealpha=0.9)


# Panel D: Model Comparison: In-Sample vs Out-of-Sample RMSE
ax_d = axes[1, 1]
models = ["Naive RW", "Linear AR(1)", "Band-TAR(1)"]
bar_w = 0.25

comp_regs = ["R2", "R3", "R4", "R6", "Pooled_Post"]
comp_df = res_df[res_df["regime_id"].isin(comp_regs)].copy().reset_index(drop=True)
x_c = np.arange(len(comp_df))

ax_d.bar(x_c - bar_w, comp_df["rmse_rw_in"], width=bar_w, label="Naive Persistence (RW)", color="#94a3b8", alpha=0.8)
ax_d.bar(x_c, comp_df["rmse_ar1_in"], width=bar_w, label="Linear AR(1)", color="#3b82f6", alpha=0.8)
ax_d.bar(x_c + bar_w, comp_df["rmse_tar_in"], width=bar_w, label="Band-TAR(1)", color="#10b981", alpha=0.8)

ax_d.set_xticks(x_c)
ax_d.set_xticklabels([r["short_name"].replace(": ", "\n") for _, r in comp_df.iterrows()], fontsize=8)
ax_d.set_ylabel("In-Sample RMSE (bps)", fontsize=9, fontweight="bold")
ax_d.set_title("D. Model Comparison: Explanatory Power across Regimes", fontsize=10, fontweight="bold")
ax_d.grid(True, linestyle=":", alpha=0.5, axis="y")
ax_d.legend(loc="upper right", fontsize=8, framealpha=0.9)

plt.tight_layout()
fig_out = FIGURES / "P3-07_band_tar.png"
fig.savefig(fig_out)
plt.close(fig)
print(f"Saved publication figure to {fig_out}")
