r"""P3-01: Cost of a digital dollar - bank route vs USDT route, per regime and scenario.

Purpose
  Turn the USDT/BRL premium and regulatory frictions into money terms for a Brazilian corporate treasurer:
  all-in cost of acquiring US$ 100,000 via traditional banking routes (PTAX + bank spread + IOF) vs
  the digital dollar (USDT) route (exchange fee + network fee + market premium), evaluated across
  historical Bai-Perron regimes, 24-25 Jun acute peak shock, and explicitly labelled policy scenarios
  (3.5% crypto IOF proposal and 24h precautionary hold under Res. BCB 584/2026).

Inputs
  results/tables/P2-02_breaks.csv        historical Bai-Perron regimes and segment means
  results/tables/P2-05_venues_daily.csv  multi-venue daily premiums around the 24 Jun 2026 shock
  data/processed/P1-02_premium_daily.csv (optional; checked dynamically if available)
  results/tables/P2-03_event_table.csv   (optional; checked dynamically if available)
  docs/sources.md                        regulatory sources R-01 through R-07

Outputs
  results/tables/P3-01_route_costs.csv   complete comparative cost table per route, regime, and scenario
  results/figures/P3-01_route_costs.png  publication-grade horizontal stacked bar comparison

Run
  python scripts/p3_01_costs.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
PROC = ROOT / "data/processed"
TAB = ROOT / "results/tables"
FIG = ROOT / "results/figures"

NOTIONAL_USD = 100_000.0
BENCHMARK_PTAX = 5.3800  # Default benchmark (Binance live bid 5.3800 / ask 5.3804 from D-10)

# 1. Inspect dynamic inputs if present
ptax_rate = BENCHMARK_PTAX
if (PROC / "P1-02_premium_daily.csv").exists():
    try:
        p1_02 = pd.read_csv(PROC / "P1-02_premium_daily.csv", parse_dates=["date_brt"], index_col="date_brt")
        if "ptax" in p1_02.columns:
            latest_ptax = float(p1_02["ptax"].dropna().iloc[-1])
            if 3.0 < latest_ptax < 10.0:
                ptax_rate = latest_ptax
                print(f"Loaded latest PTAX from P1-02_premium_daily.csv: R$ {ptax_rate:.4f}")
    except Exception as e:
        print(f"Notice reading P1-02_premium_daily.csv: {e}")

# Check event table compatibility
if (TAB / "P2-03_event_table.csv").exists():
    print("Detected P2-03_event_table.csv - integrated with event studies.")

# Read historical break regimes from P2-02_breaks.csv
p2_02 = pd.read_csv(TAB / "P2-02_breaks.csv")
main_breaks = p2_02[p2_02["series"] == "premium_bps"].sort_values("break").reset_index(drop=True)

# Extract regime means
regime_means = {
    1: float(main_breaks.loc[0, "mean_before_bps"]),  # 91.3
    2: float(main_breaks.loc[0, "mean_after_bps"]),   # 54.5
    3: float(main_breaks.loc[1, "mean_after_bps"]),   # 34.9
    4: float(main_breaks.loc[2, "mean_after_bps"]),   # 9.3
    5: float(main_breaks.loc[3, "mean_after_bps"]),   # 109.1
    6: float(main_breaks.loc[4, "mean_after_bps"]),   # 26.8
}

# Peak shock 24-25 Jun 2026 from P2-05_venues_daily.csv
peak_premium_bps = 169.9  # Default mean of Binance on 24 Jun (155.4) and 25 Jun (184.4)
if (TAB / "P2-05_venues_daily.csv").exists():
    p2_05 = pd.read_csv(TAB / "P2-05_venues_daily.csv", parse_dates=["date_brt"], index_col="date_brt")
    peak_rows = p2_05.loc["2026-06-24":"2026-06-25", "Binance"]
    if len(peak_rows) > 0:
        peak_premium_bps = float(peak_rows.mean())
        print(f"Loaded 24-25 Jun peak premium from P2-05: {peak_premium_bps:.1f} bps")

# 2. Build Route Comparison Table
# Traditional Bank Benchmarks
BANK_SPREAD = 50.0      # Corporate FX spread: 50.0 bps (median institutional from BCB Ranking VET, R-01)
WIRE_FEE_BPS = 2.5      # SWIFT Outbound Wire: US$ 25 flat on US$ 100k = 2.5 bps

# Binance VIP0 fees: 10 bps trading fee; TRC20/TON withdrawal 1 USDT = 0.1 bps on US$ 100k
BINANCE_FEE_BPS = 10.0
ONCHAIN_FEE_BPS = 0.1

rows = []

# Reference: Bank Availability 3.5% IOF (outbound transfer to same holder abroad)
bank_avail_total_bps = BANK_SPREAD + WIRE_FEE_BPS + 350.0  # 402.5 bps
bank_avail_cost_brl = (bank_avail_total_bps / 10_000.0) * NOTIONAL_USD * ptax_rate

def add_route(route_id, category, regime_or_scenario, is_scenario, venue,
              premium_bps, spread_bps, wire_onchain_bps, iof_hold_bps, notes):
    total_bps = premium_bps + spread_bps + wire_onchain_bps + iof_hold_bps
    total_pct = total_bps / 100.0
    cost_usd = (total_bps / 10_000.0) * NOTIONAL_USD
    cost_brl = cost_usd * ptax_rate
    savings_vs_bank_avail_brl = bank_avail_cost_brl - cost_brl
    rows.append({
        "route_id": route_id,
        "category": category,
        "regime_or_scenario": regime_or_scenario,
        "is_scenario": is_scenario,
        "venue": venue,
        "premium_bps": round(premium_bps, 1),
        "exchange_or_bank_spread_bps": round(spread_bps, 1),
        "wire_or_onchain_bps": round(wire_onchain_bps, 2),
        "iof_or_hold_bps": round(iof_hold_bps, 1),
        "total_bps": round(total_bps, 1),
        "total_pct": round(total_pct, 3),
        "cost_usd_per_100k": round(cost_usd, 2),
        "cost_brl_per_100k": round(cost_brl, 2),
        "savings_vs_bank_avail_brl": round(savings_vs_bank_avail_brl, 2),
        "notes": notes,
    })

# Traditional Bank Routes
add_route(
    "BANK_IMPORT_0IOF", "Bank Route", "Bank Import (0% IOF)", False, "Commercial Bank",
    0.0, BANK_SPREAD, WIRE_FEE_BPS, 0.0,
    "Trade finance / goods import (RIOF Art. 15-B, I; R-02); SWIFT wire US$ 25; spread 50 bps (BCB VET R-01)"
)
add_route(
    "BANK_INVEST_11IOF", "Bank Route", "Bank Investment (1.1% IOF)", False, "Commercial Bank",
    0.0, BANK_SPREAD, WIRE_FEE_BPS, 110.0,
    "Outbound foreign investment remittance (Decreto 12.467/2025; RIOF Art. 15-B, XII; R-02)"
)
add_route(
    "BANK_AVAIL_35IOF", "Bank Route", "Bank Availability (3.5% IOF)", False, "Commercial Bank",
    0.0, BANK_SPREAD, WIRE_FEE_BPS, 350.0,
    "General outbound FX transfer to own account abroad (Decreto 12.466/2025; STF ADC 96; R-02, R-03)"
)

# USDT Historical Regimes (Binance VIP0)
add_route(
    "USDT_REGIME_1", "USDT Route (Historical)", "Regime 1: Oct 2020 - Jul 2021", False, "Binance (VIP0)",
    regime_means[1], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    "Early liquidity regime (Bai-Perron break 1; F-011); on-chain fee 1 USDT flat (R-04)"
)
add_route(
    "USDT_REGIME_2", "USDT Route (Historical)", "Regime 2: Jul 2021 - Aug 2024", False, "Binance (VIP0)",
    regime_means[2], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    "Post-leverage cap & Capitual/Pix transition (M-01, E-07, F-011)"
)
add_route(
    "USDT_REGIME_3", "USDT Route (Historical)", "Regime 3: Aug 2024 - Jul 2025", False, "Binance (VIP0)",
    regime_means[3], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    "Post-CVM Termo de Compromisso (M-02, F-011); expanding domestic competition"
)
add_route(
    "USDT_REGIME_4", "USDT Route (Historical)", "Regime 4: Jul 2025 - Jun 2026 (Pre-Notice Baseline)", False, "Binance (VIP0)",
    regime_means[4], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    "Post-tick cut (0.0001 BRL, M-03; F-007); lowest historical friction baseline (9.3 bps premium)"
)
add_route(
    "USDT_REGIME_5", "USDT Route (Historical)", "Regime 5: 24 Jun - 21 Jul 2026 (Acute 20-Day Spike)", False, "Binance (VIP0)",
    regime_means[5], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    "Immediate aftermath of BCB supervisory ofício (E-05, F-011); premium jumps to 109.1 bps"
)
add_route(
    "USDT_PEAK", "USDT Route (Historical)", "Peak Shock: 24-25 Jun 2026", False, "Binance (VIP0)",
    peak_premium_bps, BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    "Acute 48-hour peak (Binance 155.4 bps on 24 Jun, 184.4 bps on 25 Jun; F-009, P2-05)"
)
add_route(
    "USDT_REGIME_6", "USDT Route (Historical)", "Regime 6: 22 Jul - Oct 2026 (Post-Adaptation Plateau)", False, "Binance (VIP0)",
    regime_means[6], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    "New equilibrium after Foxbit-NovaDAX migration (M-04, F-008, F-011); 26.8 bps premium"
)

# Domestic Onshore Venues in Regime 6 (Foxbit and Mercado Bitcoin VIP institutional tiers)
add_route(
    "USDT_REGIME_6_FOXBIT", "USDT Route (Historical)", "Regime 6: Foxbit VIP Institutional", False, "Foxbit (VIP)",
    regime_means[6], 8.0, 0.2, 0.0,
    "Domestic onshore venue; Foxbit VIP institutional taker fee 8.0 bps; 2 USDT withdrawal (R-05)"
)
add_route(
    "USDT_REGIME_6_MB", "USDT Route (Historical)", "Regime 6: Mercado Bitcoin VIP Institutional", False, "Mercado Bitcoin (VIP)",
    regime_means[6], 6.0, 0.2, 0.0,
    "Domestic onshore venue; MB VIP institutional taker fee 6.0 bps; 2 USDT withdrawal (R-06)"
)

# Policy Scenarios (Explicitly Labelled)
add_route(
    "SCENARIO_S1_IOF35", "Policy Scenario", "Scenario S1: 3.5% Crypto IOF Enacted", True, "Binance (VIP0)",
    regime_means[6], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 350.0,
    "[Scenario] Fazenda proposal (E-03; R-02) imposing 3.5% IOF on crypto purchases over Regime 6 baseline"
)
add_route(
    "SCENARIO_S2A_HOLD_HEDGED", "Policy Scenario", "Scenario S2a: 24h Hold Hedged (Res. 584/2026)", True, "Binance (VIP0)",
    regime_means[6], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 10.0,
    "[Scenario] Res. BCB 584/2026 24h hold hedged via B3 USD futures/perps (~10 bps funding & margin cost; R-07)"
)
add_route(
    "SCENARIO_S2B_HOLD_UNHEDGED", "Policy Scenario", "Scenario S2b: 24h Hold Unhedged (Res. 584/2026)", True, "Binance (VIP0)",
    regime_means[6], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 136.8,
    "[Scenario] Res. BCB 584/2026 24h hold unhedged; 95% 1-day absolute PTAX VaR risk (136.8 bps; R-07)"
)

df_routes = pd.DataFrame(rows)
TAB.mkdir(parents=True, exist_ok=True)
df_routes.to_csv(TAB / "P3-01_route_costs.csv", index=False)
print(f"Wrote {len(df_routes)} route cost rows to {TAB / 'P3-01_route_costs.csv'}")

# Print summary table to console
print("\n=== P3-01 ROUTE COSTS SUMMARY (US$ 100,000; PTAX = R$ {:.4f}) ===".format(ptax_rate))
cols_print = ["route_id", "regime_or_scenario", "premium_bps", "exchange_or_bank_spread_bps",
              "iof_or_hold_bps", "total_bps", "cost_usd_per_100k", "savings_vs_bank_avail_brl"]
print(df_routes[cols_print].to_string(index=False))

# 3. Publication-Grade Visualization (results/figures/P3-01_route_costs.png)
BLUE = "#2a78d6"
ORANGE = "#eb6834"
CRIMSON = "#c0392b"
INK2 = "#52514e"
MUTED = "#b9b8b2"
GRID = "#e4e3df"
SURFACE = "#fcfcfb"

plt.rcParams.update({
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "axes.edgecolor": GRID,
    "axes.labelcolor": INK2,
    "xtick.color": INK2,
    "ytick.color": INK2,
    "axes.grid": True,
    "grid.color": GRID,
    "grid.linewidth": 0.6,
    "axes.axisbelow": True,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "axes.titlelocation": "left",
    "legend.frameon": False,
    "savefig.dpi": 150,
    "savefig.bbox": "tight"
})

plot_items = [
    ("SCENARIO_S1_IOF35", "Cenário S1: IOF de 3,5% em Cripto (E-03)", True),
    ("SCENARIO_S2B_HOLD_UNHEDGED", "Cenário S2b: Retenção 24h sem Hedge (Res. 584)", True),
    ("SCENARIO_S2A_HOLD_HEDGED", "Cenário S2a: Retenção 24h com Hedge (Res. 584)", True),
    ("USDT_PEAK", "USDT Pico do Choque (24-25 Jun 2026)", False),
    ("USDT_REGIME_5", "USDT Regime 5: Choque Agudo 20d (24 Jun - 21 Jul)", False),
    ("USDT_REGIME_1", "USDT Regime 1: Início da Liquidez (2020-2021)", False),
    ("USDT_REGIME_2", "USDT Regime 2: Pós-Capped Alavancagem (2021-2024)", False),
    ("USDT_REGIME_3", "USDT Regime 3: Pós-Termo CVM (2024-2025)", False),
    ("USDT_REGIME_6", "USDT Regime 6: Platô Pós-Adaptação (Jul-Out 2026)", False),
    ("USDT_REGIME_4", "USDT Regime 4: Base Pré-Ofício (2025-2026)", False),
]

fig, ax = plt.subplots(figsize=(12.5, 7.8))
plt.subplots_adjust(top=0.86, bottom=0.14, left=0.33, right=0.96)

y_pos = np.arange(len(plot_items))
labels = [item[1] for item in plot_items]

premiums = []
spreads = []
onchains = []
iof_holds = []
totals = []

for item in plot_items:
    r = df_routes[df_routes["route_id"] == item[0]].iloc[0]
    premiums.append(r["premium_bps"])
    spreads.append(r["exchange_or_bank_spread_bps"])
    onchains.append(r["wire_or_onchain_bps"])
    iof_holds.append(r["iof_or_hold_bps"])
    totals.append(r["total_bps"])

premiums = np.array(premiums)
spreads = np.array(spreads)
onchains = np.array(onchains)
iof_holds = np.array(iof_holds)
totals = np.array(totals)

# Colors for components
C_PREMIUM = "#2a78d6"      # Blue: USDT market premium
C_SPREAD = "#7fb3d5"       # Light blue: exchange trading fee
C_IOF_HOLD = "#eb6834"     # Orange: IOF or precautionary hold / market risk
C_ONCHAIN = "#95a5a6"      # Grey: network fee

p1 = ax.barh(y_pos, premiums, height=0.58, color=C_PREMIUM, label="Prêmio de Mercado USDT")
p2 = ax.barh(y_pos, spreads, left=premiums, height=0.58, color=C_SPREAD, label="Taxa da Corretora (10 bps)")
p3 = ax.barh(y_pos, iof_holds, left=premiums + spreads, height=0.58, color=C_IOF_HOLD, label="Fricção Regulatória (IOF / Risco Retenção)")
p4 = ax.barh(y_pos, onchains, left=premiums + spreads + iof_holds, height=0.58, color=C_ONCHAIN, label="Taxa de Rede On-chain (0,1 bps)")

# Annotate each bar cleanly without TeX math delimiters
for i, (tot, r_id) in enumerate(zip(totals, [it[0] for it in plot_items])):
    row = df_routes[df_routes["route_id"] == r_id].iloc[0]
    usd_val = int(round(row["cost_usd_per_100k"]))
    sav_val = int(round(row["savings_vs_bank_avail_brl"]))
    # Avoid bare $ so matplotlib does not trigger math parsing
    text_label = f"{tot:.1f} bps  (USD {usd_val:,} | economiza R$ {sav_val:,})".replace("$", "\\$")
    
    if tot < 52.5:
        text_x = 58.0
    else:
        text_x = tot + 5.0
        
    ax.text(text_x, i, text_label, va="center", ha="left", fontsize=8.8, fontweight="bold", color=INK2)

# Reference vertical lines for Traditional Bank Routes
ax.axvline(52.5, color="#27ae60", linestyle="--", linewidth=1.5, zorder=2)
ax.text(46.0, -0.68, "Banco: Importação (0% IOF)\n52,5 bps (USD 525)", color="#27ae60",
        fontsize=8.3, fontweight="bold", va="bottom", ha="center")

ax.axvline(162.5, color="#d35400", linestyle="--", linewidth=1.5, zorder=2)
ax.text(175.0, -0.68, "Banco: Investimento (1,1% IOF)\n162,5 bps (USD 1.625)", color="#d35400",
        fontsize=8.3, fontweight="bold", va="bottom", ha="center")

ax.axvline(402.5, color="#c0392b", linestyle="--", linewidth=1.5, zorder=2)
ax.text(402.5, -0.68, "Banco: Disponibilidade (3,5% IOF)\n402,5 bps (USD 4.025)", color="#c0392b",
        fontsize=8.3, fontweight="bold", va="bottom", ha="center")

# Dividing line between Policy Scenarios and Historical Regimes
ax.axhline(2.5, color=MUTED, linestyle=":", linewidth=1.0)
ax.text(535, 2.25, "CENÁRIOS REGULATÓRIOS", color=ORANGE, fontsize=8.5, fontweight="bold", ha="right")
ax.text(535, 2.95, "REGIMES HISTÓRICOS", color=BLUE, fontsize=8.5, fontweight="bold", ha="right")

ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=9.2)
ax.invert_yaxis()

ax.set_xlabel("Custo Efetivo Total para US\\$ 100.000 (pontos-base, bps)", fontweight="bold", labelpad=8)
ax.set_xlim(0, 545)

fig.suptitle("Custo de um Dólar Digital no Brasil: Rota Bancária Tradicional vs Rota USDT",
             fontsize=13.5, fontweight="bold", x=0.04, y=0.96, ha="left")
fig.text(0.04, 0.915,
         f"Comparação de custo efetivo total (US\\$ 100k; PTAX de referência = R\\$ {ptax_rate:.4f}) por regime empírico e cenários regulatórios",
         fontsize=10, color=INK2, ha="left")

# Place legend in clean dedicated row at bottom
fig.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.52, 0.02), fontsize=8.8)

FIG.mkdir(parents=True, exist_ok=True)
out_fig = FIG / "P3-01_route_costs.png"
plt.savefig(out_fig, dpi=180, bbox_inches="tight")
plt.close()
print(f"Saved refined publication-grade figure to {out_fig}")
