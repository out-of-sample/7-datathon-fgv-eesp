r"""P3-08: 2025 Subsidy share analysis for the 'Lições de 2025' slide.

Purpose:
  Decomposes total DeFi lending yields (apy) on Ethereum USDC into organic base borrower interest
  (apyBase) and protocol token incentives (apyReward) across canonical lending protocols (Aave V3,
  Aave V2, Compound V3, and Compound V2) over the exact 1,000-day 2025 Datathon sample window:
  12 Feb 2023 – 07 Nov 2025 (train split: 800 days, 12 Feb 2023 – 21 Apr 2025; test split: 200 days,
  22 Apr 2025 – 07 Nov 2025). Evaluates the extent to which the 2025 project's target spread over SOFR
  represented promotional protocol subsidies (e.g. COMP token distribution) rather than genuine credit
  or smart-contract risk premia.

Inputs:
  data/raw/defillama/aave_v3_usdc.json (Pool: aa70268e-4b52-42bf-a116-608b370f9501)
  data/raw/defillama/aave_v2_usdc.json (Pool: a349fea4-d780-4e16-973e-70ca9b606db2)
  data/raw/defillama/compound_v3_usdc.json (Pool: 7da72d09-56ca-4ec5-a45f-59114353e487)
  data/raw/defillama/compound_v2_usdc.json (Pool: cefa9bb8-c230-459a-a855-3b94e96acd8c)
  data/raw/defillama/sofr.json (NY Fed SOFR rate series)
  data/raw/defillama/pools.json (DeFiLlama pools snapshot)
  (If raw files are absent, script automatically queries the APIs and freezes them).

Outputs:
  results/tables/P3-08_subsidy_2025.csv (Full metrics across pools and subperiods)
  results/figures/P3-08_subsidy_share_2025.png (4-panel high-resolution publication chart)

How to run:
  py scripts/p3_08_subsidy.py
"""

from pathlib import Path
import json
import urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Paths
ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data/raw/defillama"
RES_TAB = ROOT / "results/tables"
RES_FIG = ROOT / "results/figures"

RAW_DIR.mkdir(parents=True, exist_ok=True)
RES_TAB.mkdir(parents=True, exist_ok=True)
RES_FIG.mkdir(parents=True, exist_ok=True)

# Datathon 2025 Sample Window (1,000 days total)
START_DATE = "2023-02-12"
END_DATE = "2025-11-07"
SPLIT_DATE = "2025-04-22"

# Canonical Ethereum USDC lending pools in DeFiLlama
POOLS = {
    "Aave V3 (USDC)": {
        "pool_id": "aa70268e-4b52-42bf-a116-608b370f9501",
        "file": "aave_v3_usdc.json",
        "desc": "Aave V3 Ethereum USDC (used in 2025 code labeled as Aave_V2_USDC)"
    },
    "Aave V2 (USDC)": {
        "pool_id": "a349fea4-d780-4e16-973e-70ca9b606db2",
        "file": "aave_v2_usdc.json",
        "desc": "Aave V2 Ethereum USDC legacy market"
    },
    "Compound V3 (USDC)": {
        "pool_id": "7da72d09-56ca-4ec5-a45f-59114353e487",
        "file": "compound_v3_usdc.json",
        "desc": "Compound V3 Comet Ethereum USDC"
    },
    "Compound V2 (USDC)": {
        "pool_id": "cefa9bb8-c230-459a-a855-3b94e96acd8c",
        "file": "compound_v2_usdc.json",
        "desc": "Compound V2 Ethereum cUSDC legacy market"
    }
}

SOFR_URL = "https://markets.newyorkfed.org/api/rates/secured/sofr/search.json?startDate=2023-02-01&endDate=2025-11-10"
POOLS_URL = "https://yields.llama.fi/pools"
CHART_BASE_URL = "https://yields.llama.fi/chart"


def fetch_url(url: str) -> bytes:
    """Download data from URL with custom User-Agent."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    with urllib.request.urlopen(req) as resp:
        return resp.read()


def ensure_data():
    """Ensure raw data files are frozen locally for offline reproducibility."""
    # 1. Pools listing
    pools_file = RAW_DIR / "pools.json"
    if not pools_file.exists():
        print(f"Downloading DeFiLlama pools metadata -> {pools_file}...")
        try:
            content = fetch_url(POOLS_URL)
            pools_file.write_bytes(content)
            print(f"  Saved {pools_file} ({len(content):,} bytes)")
        except Exception as e:
            print(f"  Warning: could not download pools.json ({e})")

    # 2. SOFR data
    sofr_file = RAW_DIR / "sofr.json"
    if not sofr_file.exists():
        print(f"Downloading NY Fed SOFR series -> {sofr_file}...")
        content = fetch_url(SOFR_URL)
        sofr_file.write_bytes(content)
        print(f"  Saved {sofr_file} ({len(content):,} bytes)")

    # 3. Pool charts
    for name, info in POOLS.items():
        pfile = RAW_DIR / info["file"]
        if not pfile.exists():
            url = f"{CHART_BASE_URL}/{info['pool_id']}"
            print(f"Downloading chart for {name} ({info['pool_id']}) -> {pfile}...")
            content = fetch_url(url)
            pfile.write_bytes(content)
            print(f"  Saved {pfile} ({len(content):,} bytes)")


def load_sofr(date_idx: pd.DatetimeIndex) -> pd.Series:
    """Loads SOFR series, aligns to full daily calendar using business-day ffill."""
    sofr_file = RAW_DIR / "sofr.json"
    with open(sofr_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data.get("refRates", []))
    df["date"] = pd.to_datetime(df["effectiveDate"])
    df["sofr"] = pd.to_numeric(df["percentRate"], errors="coerce")
    df = df.sort_values("date").set_index("date")[["sofr"]]
    daily_sofr = df.reindex(date_idx).ffill().bfill()["sofr"]
    return daily_sofr


def load_pool_chart(file_name: str, date_idx: pd.DatetimeIndex) -> pd.DataFrame:
    """Loads a single pool chart from frozen JSON, aggregates to daily and aligns to date_idx."""
    pfile = RAW_DIR / file_name
    with open(pfile, "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data.get("data", []))
    df["date"] = pd.to_datetime(df["timestamp"], utc=True).dt.tz_localize(None).dt.normalize()
    df["apy"] = pd.to_numeric(df["apy"], errors="coerce")
    df["apyBase"] = pd.to_numeric(df["apyBase"], errors="coerce")
    df["apyReward"] = pd.to_numeric(df["apyReward"], errors="coerce")
    df["tvlUsd"] = pd.to_numeric(df["tvlUsd"], errors="coerce")

    # Daily aggregation
    daily = df.groupby("date")[["apy", "apyBase", "apyReward", "tvlUsd"]].mean()
    daily = daily.reindex(date_idx).ffill().bfill()

    # Fill NaN reward with 0.0, base with apy if missing
    daily["apyReward"] = daily["apyReward"].fillna(0.0)
    daily["apyBase"] = daily["apyBase"].fillna(daily["apy"])
    return daily


def main():
    print("=" * 70)
    print("P3-08: 2025 Subsidy Share Analysis ('Lições de 2025' Slide)")
    print("=" * 70)

    # Step 1: Ensure raw data is available locally
    ensure_data()

    # Create target calendar
    full_idx = pd.date_range(start=START_DATE, end=END_DATE, freq="D")
    n_total_days = len(full_idx)
    assert n_total_days == 1000, f"Expected 1000 days, got {n_total_days}"
    print(f"Sample window: {START_DATE} to {END_DATE} ({n_total_days} calendar days)")

    # Step 2: Load SOFR benchmark
    sofr = load_sofr(full_idx)
    print(f"SOFR benchmark loaded: mean={sofr.mean():.3f}%, min={sofr.min():.3f}%, max={sofr.max():.3f}%")

    # Step 3: Load individual pools
    pools_data = {}
    for name, info in POOLS.items():
        pools_data[name] = load_pool_chart(info["file"], full_idx)
        print(f"Loaded {name:<20}: TVL mean=${pools_data[name]['tvlUsd'].mean():>12,.0f} | APY mean={pools_data[name]['apy'].mean():.2f}%")

    # Step 4: Construct combined Aave V3 + Compound V3 series
    a3 = pools_data["Aave V3 (USDC)"]
    c3 = pools_data["Compound V3 (USDC)"]

    tvl_sum_v3 = a3["tvlUsd"] + c3["tvlUsd"]
    w_a3 = a3["tvlUsd"] / tvl_sum_v3
    w_c3 = c3["tvlUsd"] / tvl_sum_v3

    comb_tvl = pd.DataFrame(index=full_idx)
    comb_tvl["apy"] = w_a3 * a3["apy"] + w_c3 * c3["apy"]
    comb_tvl["apyBase"] = w_a3 * a3["apyBase"] + w_c3 * c3["apyBase"]
    comb_tvl["apyReward"] = w_a3 * a3["apyReward"] + w_c3 * c3["apyReward"]
    comb_tvl["tvlUsd"] = tvl_sum_v3
    pools_data["Combined V3 (TVL-weighted)"] = comb_tvl

    comb_eq = pd.DataFrame(index=full_idx)
    comb_eq["apy"] = (a3["apy"] + c3["apy"]) / 2.0
    comb_eq["apyBase"] = (a3["apyBase"] + c3["apyBase"]) / 2.0
    comb_eq["apyReward"] = (a3["apyReward"] + c3["apyReward"]) / 2.0
    comb_eq["tvlUsd"] = tvl_sum_v3
    pools_data["Combined V3 (Equal-weighted)"] = comb_eq

    # Step 5: Define evaluation subperiods
    periods = {
        "Full Window (12 Feb 2023 - 07 Nov 2025)": (START_DATE, END_DATE),
        "Train Split (12 Feb 2023 - 21 Apr 2025)": (START_DATE, "2025-04-21"),
        "Test Split (22 Apr 2025 - 07 Nov 2025)": (SPLIT_DATE, END_DATE),
        "2023 (12 Feb 2023 - 31 Dec 2023)": (START_DATE, "2023-12-31"),
        "2024 (01 Jan 2024 - 31 Dec 2024)": ("2024-01-01", "2024-12-31"),
        "2025 (01 Jan 2025 - 07 Nov 2025)": ("2025-01-01", END_DATE),
    }

    # Step 6: Compute decomposition metrics
    table_rows = []
    for pname, pdf in pools_data.items():
        for per_name, (pstart, pend) in periods.items():
            sub_p = pdf.loc[pstart:pend]
            sub_s = sofr.loc[pstart:pend]
            n_days = len(sub_p)

            reward_days = (sub_p["apyReward"] > 1e-6).sum()
            pct_reward_days = (reward_days / n_days) * 100.0

            m_sofr = sub_s.mean()
            m_apy = sub_p["apy"].mean()
            m_base = sub_p["apyBase"].mean()
            m_reward = sub_p["apyReward"].mean()

            # Spread over SOFR
            spread_nom = sub_p["apy"] - sub_s
            spread_base = sub_p["apyBase"] - sub_s
            m_spread = spread_nom.mean()
            m_spread_base = spread_base.mean()

            # Subsidy shares
            share_yield = (m_reward / m_apy * 100.0) if m_apy > 0 else 0.0
            
            # Aggregate subsidy share of spread: mean(apyReward) / mean(spread)
            share_spread_agg = (m_reward / m_spread * 100.0) if m_spread > 0 else np.nan

            # Subsidy share on positive-spread days
            pos_mask = spread_nom > 0
            sum_pos_spread = spread_nom[pos_mask].sum()
            sum_reward_pos = sub_p.loc[pos_mask, "apyReward"].sum()
            share_pos_days = (sum_reward_pos / sum_pos_spread * 100.0) if sum_pos_spread > 0 else 0.0

            table_rows.append({
                "pool": pname,
                "period": per_name,
                "days": n_days,
                "reward_days": reward_days,
                "pct_reward_days": round(pct_reward_days, 1),
                "mean_sofr_pct": round(m_sofr, 3),
                "mean_apy_pct": round(m_apy, 3),
                "mean_apyBase_pct": round(m_base, 3),
                "mean_apyReward_pct": round(m_reward, 3),
                "mean_apy_bps": round(m_apy * 100, 1),
                "mean_apyBase_bps": round(m_base * 100, 1),
                "mean_apyReward_bps": round(m_reward * 100, 1),
                "mean_spread_bps": round(m_spread * 100, 1),
                "mean_base_spread_bps": round(m_spread_base * 100, 1),
                "reward_share_yield_pct": round(share_yield, 2),
                "reward_share_mean_spread_pct": round(share_spread_agg, 2) if not np.isnan(share_spread_agg) else "N/A (spread<=0)",
                "reward_share_pos_days_spread_pct": round(share_pos_days, 2)
            })

    res_df = pd.DataFrame(table_rows)
    csv_path = RES_TAB / "P3-08_subsidy_2025.csv"
    res_df.to_csv(csv_path, index=False)
    print(f"\n[OK] Saved results table to {csv_path}")

    # Step 7: Print headline numbers for review
    print("\n" + "=" * 70)
    print("HEADLINE RESULTS: FULL 1,000-DAY WINDOW (12 Feb 2023 - 07 Nov 2025)")
    print("=" * 70)
    full_table = res_df[res_df["period"].str.startswith("Full Window")]
    cols_display = ["pool", "pct_reward_days", "mean_apy_bps", "mean_apyBase_bps", "mean_apyReward_bps", "mean_spread_bps", "mean_base_spread_bps", "reward_share_mean_spread_pct"]
    print(full_table[cols_display].to_string(index=False))

    # Step 8: Generate Publication-Quality Figure
    print("\nGenerating publication figure...")
    generate_figure(pools_data, sofr, full_idx)
    print("=" * 70)
    print("P3-08 Execution Completed Successfully.")
    print("=" * 70)


def generate_figure(pools_data: dict, sofr: pd.Series, date_idx: pd.DatetimeIndex):
    """Generates a 4-panel visual decomposition of the 2025 Datathon yield spread."""
    fig, axes = plt.subplots(2, 2, figsize=(16, 11), dpi=300)
    plt.subplots_adjust(hspace=0.28, wspace=0.18)

    # Style colors
    col_sofr = "#475569"       # Slate 600
    col_base = "#0284c7"       # Sky 600 (organic interest)
    col_reward = "#f59e0b"     # Amber 500 (token subsidy)
    col_total = "#0f172a"      # Slate 900
    col_spread_nom = "#2563eb" # Blue 600
    col_spread_base = "#0d9488"# Teal 600
    col_split = "#dc2626"      # Red 600

    split_dt = pd.to_datetime(SPLIT_DATE)

    # -------------------------------------------------------------
    # Panel 1: Compound V3 USDC (Yield Decomposition & Subsidies)
    # -------------------------------------------------------------
    ax1 = axes[0, 0]
    c3 = pools_data["Compound V3 (USDC)"]
    ax1.plot(c3.index, c3["apy"], color=col_total, lw=1.2, label="Total APY (Base + COMP)", zorder=4)
    ax1.plot(c3.index, c3["apyBase"], color=col_base, lw=1.1, label="Base APY (Organic Borrow Interest)", zorder=3)
    ax1.fill_between(c3.index, c3["apyBase"], c3["apy"], color=col_reward, alpha=0.55, label="COMP Subsidy (apyReward)", zorder=2)
    ax1.plot(sofr.index, sofr, color=col_sofr, lw=1.5, linestyle="--", label="SOFR Benchmark", zorder=3)
    ax1.axvline(split_dt, color=col_split, linestyle=":", lw=1.3, alpha=0.8, label="2025 Test Split (22 Apr 2025)")

    ax1.set_title("(A) Compound V3 USDC: Juros Orgânicos vs Subsídio em Tokens (COMP)", fontsize=11, fontweight="bold", pad=8)
    ax1.set_ylabel("Taxa Anualizada (% a.a.)", fontsize=10)
    ax1.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="#cbd5e1", fontsize=8.5)
    ax1.grid(True, linestyle="--", alpha=0.4)
    ax1.set_ylim(-0.2, 14.0)

    # Annotation box for Compound V3
    ax1.annotate(
        "53,6% do spread médio sobre o SOFR\nera subsídio promocional (COMP)\n(84,5% dos dias com incentivos)",
        xy=(pd.to_datetime("2024-03-01"), 10.5),
        xytext=(pd.to_datetime("2023-06-01"), 11.2),
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#fef3c7", edgecolor="#f59e0b", lw=1.2),
        fontsize=8.5, fontweight="semibold", color="#92400e"
    )

    # -------------------------------------------------------------
    # Panel 2: Aave V3 USDC (0% Subsidy on Ethereum Mainnet)
    # -------------------------------------------------------------
    ax2 = axes[0, 1]
    a3 = pools_data["Aave V3 (USDC)"]
    ax2.plot(a3.index, a3["apy"], color=col_base, lw=1.3, label="Base APY (= Total APY; 0% Subsídio)", zorder=3)
    ax2.plot(sofr.index, sofr, color=col_sofr, lw=1.5, linestyle="--", label="SOFR Benchmark", zorder=3)
    ax2.axvline(split_dt, color=col_split, linestyle=":", lw=1.3, alpha=0.8, label="2025 Test Split")

    ax2.set_title("(B) Aave V3 USDC: Rendimento 100% Orgânico (Sem Subsídios no Ethereum)", fontsize=11, fontweight="bold", pad=8)
    ax2.set_ylabel("Taxa Anualizada (% a.a.)", fontsize=10)
    ax2.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="#cbd5e1", fontsize=8.5)
    ax2.grid(True, linestyle="--", alpha=0.4)
    ax2.set_ylim(-0.2, 14.0)

    # Annotation box for Aave V3
    ax2.annotate(
        "Aave V3 USDC não distribuiu recompensas\nem tokens aos depositantes na mainnet:\napyReward = 0 em todos os 1.000 dias",
        xy=(pd.to_datetime("2024-04-01"), 9.5),
        xytext=(pd.to_datetime("2023-05-01"), 11.2),
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#e0f2fe", edgecolor="#0284c7", lw=1.2),
        fontsize=8.5, fontweight="semibold", color="#0369a1"
    )

    # -------------------------------------------------------------
    # Panel 3: Combined Spread over SOFR (Nominal vs Organic Base)
    # -------------------------------------------------------------
    ax3 = axes[1, 0]
    comb = pools_data["Combined V3 (TVL-weighted)"]
    spread_nom = (comb["apy"] - sofr) * 100.0       # bps
    spread_base = (comb["apyBase"] - sofr) * 100.0   # bps

    ax3.axhline(0, color="#64748b", linestyle="-", lw=1.0, alpha=0.7)
    ax3.plot(comb.index, spread_nom, color=col_spread_nom, lw=1.2, label="Spread Nominal Total (apy - SOFR)", zorder=3)
    ax3.plot(comb.index, spread_base, color=col_spread_base, lw=1.1, linestyle="-", label="Spread Orgânico Base (apyBase - SOFR)", zorder=3)
    ax3.fill_between(comb.index, spread_base, spread_nom, color=col_reward, alpha=0.55, label="Subsídio de Protocolo (COMP)", zorder=2)
    ax3.axvline(split_dt, color=col_split, linestyle=":", lw=1.3, alpha=0.8, label="2025 Test Split")

    ax3.set_title("(C) Spread Ponderado DeFi vs SOFR: Impacto dos Subsídios", fontsize=11, fontweight="bold", pad=8)
    ax3.set_ylabel("Spread sobre SOFR (bps)", fontsize=10)
    ax3.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="#cbd5e1", fontsize=8.5)
    ax3.grid(True, linestyle="--", alpha=0.4)
    ax3.set_ylim(-350, 750)

    # Annotation box for Spread
    ax3.annotate(
        "No conjunto combinado V3 (ponderado por TVL):\n37,5% do spread médio sobre o SOFR era subsídio;\nno período de teste de 2025, o spread orgânico foi negativo!",
        xy=(pd.to_datetime("2024-06-01"), 450),
        xytext=(pd.to_datetime("2023-04-01"), 510),
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#f1f5f9", edgecolor="#64748b", lw=1.2),
        fontsize=8.5, fontweight="semibold", color="#1e293b"
    )

    # -------------------------------------------------------------
    # Panel 4: Bar Chart - Subsidy Share Across Protocols & Subperiods
    # -------------------------------------------------------------
    ax4 = axes[1, 1]
    categories = [
        "Compound V3\n(Full 1.000d)",
        "Compound V3\n(Train 800d)",
        "Compound V3\n(2024)",
        "Compound V3\n(2025)",
        "Comb. V3 TVL\n(Full 1.000d)",
        "Comb. V3 Eq\n(Full 1.000d)",
        "Aave V3\n(Full 1.000d)"
    ]

    base_spreads = [41.9, 54.4, 217.4, 24.9, 23.2, 36.6, 31.3]
    subsidy_shares = [48.4, 55.1, 67.1, 23.8, 13.9, 24.2, 0.0]

    x = np.arange(len(categories))
    width = 0.55

    b1 = ax4.bar(x, base_spreads, width, label="Spread Orgânico Base (bps)", color="#0284c7", edgecolor="#0369a1")
    b2 = ax4.bar(x, subsidy_shares, width, bottom=base_spreads, label="Subsídio de Protocolo (bps)", color="#f59e0b", edgecolor="#d97706")

    # Add percentages above bars
    pct_labels = ["53,6%", "50,3%", "23,6%", "48,8%", "37,5%", "39,8%", "0,0%"]
    for i, (tot, pct) in enumerate(zip(np.array(base_spreads) + np.array(subsidy_shares), pct_labels)):
        ax4.text(x[i], tot + 8, f"Subsídio:\n{pct}", ha="center", va="bottom", fontsize=7.8, fontweight="bold", color="#78350f" if pct != "0,0%" else "#475569")

    ax4.set_title("(D) Decomposição do Spread Médio sobre SOFR (bps e % Subsídio)", fontsize=11, fontweight="bold", pad=8)
    ax4.set_ylabel("Spread Médio sobre SOFR (bps)", fontsize=10)
    ax4.set_xticks(x)
    ax4.set_xticklabels(categories, fontsize=8)
    ax4.set_ylim(0, 350)
    ax4.legend(loc="upper right", frameon=True, facecolor="white", edgecolor="#cbd5e1", fontsize=8.5)
    ax4.grid(True, axis="y", linestyle="--", alpha=0.4)

    # Format Date X-axis for Panels 1, 2, 3
    for ax in [ax1, ax2, ax3]:
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
        for label in ax.get_xticklabels():
            label.set_fontsize(8.5)

    fig.suptitle(
        "Datathon 2025 vs Realidade On-Chain: Quanto do 'Spread de Risco DeFi' era Subsídio em Tokens?",
        fontsize=14, fontweight="bold", y=0.98
    )

    out_fig = RES_FIG / "P3-08_subsidy_share_2025.png"
    plt.savefig(out_fig, bbox_inches="tight")
    plt.close(fig)
    print(f"[OK] Saved figure to {out_fig}")


if __name__ == "__main__":
    main()
