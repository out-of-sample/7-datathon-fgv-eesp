r"""P3-01: Cost of a digital dollar - bank route vs USDT route, per regime and scenario.

Purpose
  Turn the USDT/BRL premium and regulatory frictions into money terms for a Brazilian corporate treasurer:
  (1) Headline: the direct cost of the 23 Jun 2026 BCB notice on a US$ 100,000 USDT acquisition (+93.9 bps =
      R$ 5,052 during the 20-day spike; +11.5 bps = R$ 621 after the spike, not distinguishable from drift).
  (2) Context: neutral comparison of total transaction frictions across traditional banking FX routes
      (PTAX + BCB corporate spread R-01 + SWIFT wire R-01b + statutory IOF R-02) and the digital dollar
      (USDT) route (exchange fee + network fee + market premium), evaluated across historical Bai-Perron
      regimes and explicitly labelled policy scenarios (3.5% crypto IOF proposal E-03 and 24h precautionary
      hold under Res. BCB 584/2026 R-07). Framed neutrally per docs/02-dolar-cripto.md §10.

Inputs
  results/tables/P2-02_breaks.csv        historical Bai-Perron regimes and segment means
  results/tables/P2-05_venues_daily.csv  multi-venue daily premiums around the 24 Jun 2026 shock
  data/processed/P1-02_premium_daily.csv daily PTAX and premium series
  results/tables/P2-03_event_table.csv   event-study estimates for E-05
  docs/sources.md                        opened, quoted sources R-01 through R-07

Outputs
  results/tables/P3-01_route_costs.csv   complete comparative cost table per route, regime, and scenario
  results/figures/P3-01_route_costs.png  publication-grade neutral horizontal stacked bar comparison

Run
  py scripts/p3_01_costs.py
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
BENCHMARK_PTAX = 5.3800  # Pre-committed reference FX (Binance live bid 5.3800 / ask 5.3804 from D-10)

# 1. Inspect dynamic inputs if present
ptax_rate = BENCHMARK_PTAX
empirical_last_ptax = None
if (PROC / "P1-02_premium_daily.csv").exists():
    try:
        p1_02 = pd.read_csv(PROC / "P1-02_premium_daily.csv", parse_dates=["date_brt"], index_col="date_brt")
        if "ptax_sell_brl_per_usd" in p1_02.columns:
            empirical_last_ptax = float(p1_02["ptax_sell_brl_per_usd"].dropna().iloc[-1])
            print(f"Verified latest PTAX in P1-02_premium_daily.csv: R$ {empirical_last_ptax:.4f} (benchmark pre-committed to R$ {BENCHMARK_PTAX:.4f})")
    except Exception as e:
        print(f"Notice reading P1-02_premium_daily.csv: {e}")

if (TAB / "P2-03_event_table.csv").exists():
    print("Detected P2-03_event_table.csv - integrated with event studies.")

# Read historical break regimes from P2-02_breaks.csv
p2_02 = pd.read_csv(TAB / "P2-02_breaks.csv")
main_breaks = p2_02[p2_02["series"] == "premium_bps"].sort_values("break").reset_index(drop=True)

regime_means = {
    1: float(main_breaks.loc[0, "mean_before_bps"]),  # 91.3
    2: float(main_breaks.loc[0, "mean_after_bps"]),   # 54.5
    3: float(main_breaks.loc[1, "mean_after_bps"]),   # 34.9
    4: float(main_breaks.loc[2, "mean_after_bps"]),   # 9.3
    5: float(main_breaks.loc[3, "mean_after_bps"]),   # 109.1
    6: float(main_breaks.loc[4, "mean_after_bps"]),   # 26.8
}

# Peak shock 24-25 Jun 2026 from P2-05_venues_daily.csv
peak_premium_bps = 169.9
if (TAB / "P2-05_venues_daily.csv").exists():
    p2_05 = pd.read_csv(TAB / "P2-05_venues_daily.csv", parse_dates=["date_brt"], index_col="date_brt")
    peak_rows = p2_05.loc["2026-06-24":"2026-06-25", "Binance"]
    if len(peak_rows) > 0:
        peak_premium_bps = float(peak_rows.mean())
        print(f"Loaded 24-25 Jun peak premium from P2-05: {peak_premium_bps:.1f} bps")

# 2. Sourced Route Parameters (docs/sources.md R-01..R-07, opened 2 Nov 2026)
# BCB Estudo Especial no. 48/2019 (R-01): volume-weighted corporate FX spread is 20.0 bps (0.20%);
# 4th quartile (> US$ 55.6k, covering US$ 100k) median is 15-25 bps (50 bps kept in notes as conservative upper bound).
BANK_SPREAD = 20.0
# Banco do Brasil Tabela de Tarifas PJ (R-01b): SWIFT communication R$ 100 (US$ 18.59); online payment order R$ 440 (US$ 81.78).
# US$ 25.00 flat (2.5 bps on US$ 100k) represents direct SWIFT wire messaging cost.
WIRE_FEE_BPS = 2.5

# Binance VIP0 standard spot taker fee: 10.0 bps; TRC-20/TON withdrawal 1 USDT = 0.1 bps on US$ 100k (R-04)
BINANCE_FEE_BPS = 10.0
ONCHAIN_FEE_BPS = 0.1

# 1-day USD/BRL forward/futures carry via Covered Interest Parity (R-07, BCB EE 48/2019 p. 5 n. 9):
# (CDI ~10.75% - SOFR ~5.00%) / 252 = 2.28 bps/day + ~0.22 bps B3 DOL fee = 2.5 bps
HEDGE_CARRY_1D_BPS = 2.5

rows = []

def add_route(route_id, category, regime_or_scenario, is_scenario, venue,
              premium_bps, spread_bps, wire_onchain_bps, iof_hold_bps, notes, avail_iof_bps=350.0):
    # avail_iof_bps: statutory IOF on bank availability in force in that period (R-02):
    # 1.1% (110 bps) before 23 May 2025, 3.5% (350 bps) from 23 May 2025 (Decreto 12.466/2025)
    bank_avail_cost_brl = ((BANK_SPREAD + WIRE_FEE_BPS + avail_iof_bps) / 10_000.0) * NOTIONAL_USD * ptax_rate
    total_bps = premium_bps + spread_bps + wire_onchain_bps + iof_hold_bps
    total_pct = total_bps / 100.0
    cost_usd = (total_bps / 10_000.0) * NOTIONAL_USD
    cost_brl = cost_usd * ptax_rate
    diff_vs_bank_avail_brl = bank_avail_cost_brl - cost_brl
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
        "bank_avail_iof_in_force_bps": avail_iof_bps,
        "savings_vs_bank_avail_brl": round(diff_vs_bank_avail_brl, 2),
        "notes": notes,
    })

# Traditional Bank Routes (sourced corporate spread 20 bps, R-01; with 50 bps upper bound noted)
add_route(
    "BANK_IMPORT_0IOF", "Bank Route", "Bank Import (0% IOF)", False, "Commercial Bank",
    0.0, BANK_SPREAD, WIRE_FEE_BPS, 0.0,
    "Goods import (RIOF Art. 15-B, I; R-02); BCB corporate spread median 20 bps (>US$ 55.6k, EE 48/2019 R-01; 50 bps upper bound = 52.5 bps); SWIFT US$ 25 (R-01b)"
)
add_route(
    "BANK_INVEST_11IOF", "Bank Route", "Bank Investment / Pre-May 2025 Avail. (1.1% IOF)", False, "Commercial Bank",
    0.0, BANK_SPREAD, WIRE_FEE_BPS, 110.0,
    "Availability abroad pre-23 May 2025 & investment remittance post-May 2025 (Decreto 12.467/2025, Art. 15-B, XXI-A; R-02); spread 20 bps (R-01; 162.5 bps at 50 bps spread)"
)
add_route(
    "BANK_AVAIL_35IOF", "Bank Route", "Bank Availability Post-May 2025 (3.5% IOF)", False, "Commercial Bank",
    0.0, BANK_SPREAD, WIRE_FEE_BPS, 350.0,
    "General outbound availability transfer from 23 May 2025 (Decreto 12.466/2025; STF ADC 96; R-02, R-03); spread 20 bps (R-01; 402.5 bps at 50 bps spread)"
)

# USDT Historical Regimes (Binance VIP0)
add_route(
    "USDT_REGIME_1", "USDT Route (Historical)", "Regime 1: Oct 2020 - Jul 2021", False, "Binance (VIP0)",
    regime_means[1], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    "Regime 1 (F-011); compared against 1.1% IOF in force (R-02); on-chain fee 1 USDT flat (R-04)",
    avail_iof_bps=110.0
)
add_route(
    "USDT_REGIME_2", "USDT Route (Historical)", "Regime 2: Jul 2021 - Aug 2024", False, "Binance (VIP0)",
    regime_means[2], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    "Regime 2 (F-011); compared against 1.1% IOF in force (R-02)",
    avail_iof_bps=110.0
)
add_route(
    "USDT_REGIME_3", "USDT Route (Historical)", "Regime 3: Aug 2024 - Jul 2025", False, "Binance (VIP0)",
    regime_means[3], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    "Regime 3 (F-011); 1.1% IOF in force for ~9.5 of 11 months (3.5% from 23 May 2025, R-02)",
    avail_iof_bps=110.0
)
add_route(
    "USDT_REGIME_4", "USDT Route (Historical)", "Regime 4: Jul 2025 - Jun 2026 (Pre-Notice Baseline)", False, "Binance (VIP0)",
    regime_means[4], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    "Post-tick cut (0.0001 BRL, M-03; F-007); lowest historical friction baseline (9.3 bps premium); 3.5% IOF in force on bank availability"
)
add_route(
    "USDT_REGIME_5", "USDT Route (Historical)", "Regime 5: 24 Jun - 21 Jul 2026 (Acute 20-Day Spike)", False, "Binance (VIP0)",
    regime_means[5], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    "Immediate aftermath of BCB supervisory oficio (E-05, F-011); premium jumps to 109.1 bps"
)
add_route(
    "USDT_PEAK", "USDT Route (Historical)", "Peak Shock: 24-25 Jun 2026", False, "Binance (VIP0)",
    peak_premium_bps, BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    "Acute 48-hour peak (Binance 155.4 bps on 24 Jun, 184.4 bps on 25 Jun; F-009, P2-05)"
)
add_route(
    "USDT_REGIME_6", "USDT Route (Historical)", "Regime 6: 22 Jul - Oct 2026 (after the spike)", False, "Binance (VIP0)",
    regime_means[6], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    "After the spike (F-011); level not distinguishable from ordinary drift (placebo p = 0.24, F-022)"
)

# Domestic Onshore Venues in Regime 6 (Foxbit and Mercado Bitcoin)
add_route(
    "USDT_REGIME_6_FOXBIT", "USDT Route (Historical)", "Regime 6: Foxbit VIP 6-7 Taker", False, "Foxbit (VIP 6-7)",
    regime_means[6], 8.0, 0.2, 0.0,
    "Domestic onshore venue; Foxbit VIP 6-7 (R$ 5M-25M) taker fee 7-9 bps (midpoint 8.0 bps); 2 USDT withdrawal (R-05)"
)
add_route(
    "USDT_REGIME_6_MB", "USDT Route (Historical)", "Regime 6: Mercado Bitcoin VIP Maker (Taker = 60 bps)", False, "Mercado Bitcoin (VIP Maker)",
    regime_means[6], 6.0, 0.2, 0.0,
    "Domestic onshore venue; MB 6.0 bps is VIP passive MAKER fee (>R$ 10M); active taker for R$ 500k-10M is 60.0 bps -> 87.0 bps total (R-06)"
)

# Policy Scenarios (Explicitly Labelled)
add_route(
    "SCENARIO_S1_IOF35", "Policy Scenario", "Scenario S1: 3.5% Crypto IOF Enacted", True, "Binance (VIP0)",
    regime_means[6], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 350.0,
    "[Scenario] Unenacted Fazenda proposal (E-03; R-02) imposing 3.5% IOF on crypto purchases over Regime 6 baseline"
)
add_route(
    "SCENARIO_S2A_HOLD_HEDGED", "Policy Scenario", "Scenario S2a: 24h Hold Hedged (Res. 584/2026)", True, "Binance (VIP0)",
    regime_means[6], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, HEDGE_CARRY_1D_BPS,
    "[Scenario] Res. BCB 584/2026 (R-07) 24h hold hedged via 1-day CIP carry (CDI 10.75% - SOFR 5.00%)/252 = 2.28 bps + 0.22 bps B3 fee = 2.5 bps"
)
_r = np.log(p1_02["ptax_sell_brl_per_usd"]).diff().loc["2025-01-01":] * 1e4
hold_risk_bps = float(1.645 * _r.std())
add_route(
    "SCENARIO_S2B_HOLD_UNHEDGED", "Policy Scenario", "Scenario S2b: 24h Hold Unhedged (Res. 584/2026)", True, "Binance (VIP0)",
    regime_means[6], BINANCE_FEE_BPS, ONCHAIN_FEE_BPS, 0.0,
    f"[Scenario] Res. BCB 584/2026 (R-07) 24h hold, unhedged: 0 bps expected cost, but 95% 1-day FX risk of "
    f"{hold_risk_bps:.0f} bps (1.645 x sd of daily PTAX changes, 2025-26; P1-02). Risk is not added to cost."
)

# Cost of the notice for a buyer of US$ 100k in USDT (the project's headline question): premium change, F-016 / F-022
_e = pd.read_csv(TAB / "P2-03_event_table.csv")
spike_bps = float(_e[(_e.event_id == "E-05") & (_e.eval_date_kind == "effective")].diff_bps.iloc[0])
_d = p1_02["premium_bps"]; _i = _d.index.get_loc(pd.Timestamp("2026-06-23"))
after_bps = float(_d.iloc[_i + 21:].mean() - _d.iloc[_i - 20:_i].mean())
for rid, lab, v, note in [
    ("NOTICE_COST_SPIKE", "Cost of the notice: spike (24 Jun - 21 Jul 2026)", spike_bps,
     "Premium change after E-05, [+1,+20] vs [-20,-1] (F-016); placebo p ~ 0.001"),
    ("NOTICE_COST_AFTER", "Cost of the notice: after the spike (22 Jul - 30 Oct 2026)", after_bps,
     "[+21,end] vs [-20,-1]; NOT distinguishable from ordinary drift (placebo p = 0.24, F-022)")
]:
    add_route(rid, "Cost of the notice", lab, False, "Binance (VIP0)", v, 0.0, 0.0, 0.0, note)

df_routes = pd.DataFrame(rows)
df_routes.loc[df_routes.category == "Cost of the notice", "savings_vs_bank_avail_brl"] = np.nan
TAB.mkdir(parents=True, exist_ok=True)
df_routes.to_csv(TAB / "P3-01_route_costs.csv", index=False)
print(f"Wrote {len(df_routes)} route cost rows to {TAB / 'P3-01_route_costs.csv'}")

print("\n=== P3-01 ROUTE COSTS SUMMARY (US$ 100,000; PTAX = R$ {:.4f}) ===".format(ptax_rate))
cols_print = ["route_id", "regime_or_scenario", "premium_bps", "exchange_or_bank_spread_bps",
              "iof_or_hold_bps", "total_bps", "cost_usd_per_100k", "cost_brl_per_100k"]
print(df_routes[cols_print].to_string(index=False))

# 3. Neutral Publication-Grade Visualization (results/figures/P3-01_route_costs.png)
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
    ("SCENARIO_S2A_HOLD_HEDGED", "Cenário S2a: Retenção 24h com Hedge CIP (Res. 584)", True),
    ("SCENARIO_S2B_HOLD_UNHEDGED", "Cenário S2b: Retenção 24h sem Hedge (risco 130 bps)", True),
    ("USDT_PEAK", "USDT Pico do Choque (24-25 Jun 2026)", False),
    ("USDT_REGIME_5", "USDT Regime 5: Choque Agudo 20d (24 Jun - 21 Jul)", False),
    ("USDT_REGIME_1", "USDT Regime 1 (out/2020-jul/2021; IOF vig. 1,1%)", False),
    ("USDT_REGIME_2", "USDT Regime 2 (jul/2021-ago/2024; IOF vig. 1,1%)", False),
    ("USDT_REGIME_3", "USDT Regime 3 (ago/2024-jul/2025; IOF vig. 1,1%)", False),
    ("USDT_REGIME_6", "USDT Regime 6: após o pico (jul-out/2026; p=0,24)", False),
    ("USDT_REGIME_4", "USDT Regime 4: Base Pré-Ofício (jul/2025-jun/2026)", False),
]

fig, ax = plt.subplots(figsize=(12.5, 7.8))
plt.subplots_adjust(top=0.85, bottom=0.14, left=0.34, right=0.96)

y_pos = np.arange(len(plot_items))
labels = [item[1] for item in plot_items]

premiums, spreads, onchains, iof_holds, totals = [], [], [], [], []
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

C_PREMIUM = "#2a78d6"
C_SPREAD = "#7fb3d5"
C_IOF_HOLD = "#eb6834"
C_ONCHAIN = "#95a5a6"

ax.barh(y_pos, premiums, height=0.58, color=C_PREMIUM, label="Prêmio de Mercado USDT")
ax.barh(y_pos, spreads, left=premiums, height=0.58, color=C_SPREAD, label="Taxa da Corretora (10 bps)")
ax.barh(y_pos, iof_holds, left=premiums + spreads, height=0.58, color=C_IOF_HOLD, label="Tributo / Carrego CIP (IOF / Hedge 2,5 bps)")
ax.barh(y_pos, onchains, left=premiums + spreads + iof_holds, height=0.58, color=C_ONCHAIN, label="Taxa de Rede On-chain (0,1 bps)")

for i, (tot, r_id) in enumerate(zip(totals, [it[0] for it in plot_items])):
    row = df_routes[df_routes["route_id"] == r_id].iloc[0]
    usd_val = int(round(row["cost_usd_per_100k"]))
    brl_val = int(round(row["cost_brl_per_100k"]))
    text_label = f"{tot:.1f} bps  (USD {usd_val:,} | R$ {brl_val:,})".replace("$", "\\$")
    text_x = tot + 5.0
    ax.text(text_x, i, text_label, va="center", ha="left", fontsize=8.8, fontweight="bold", color=INK2)

# Reference vertical lines for Traditional Bank Routes (BCB corporate spread 20 bps + 2.5 bps SWIFT + statutory IOF)
bank_imp_bps = BANK_SPREAD + WIRE_FEE_BPS
bank_inv_bps = BANK_SPREAD + WIRE_FEE_BPS + 110.0
bank_avl_bps = BANK_SPREAD + WIRE_FEE_BPS + 350.0

ax.axvline(bank_imp_bps, color="#27ae60", linestyle="--", linewidth=1.5, zorder=2)
ax.text(bank_imp_bps + 3.0, -0.68, f"Banco: Importação (0% IOF)\n{bank_imp_bps:.1f} bps (R\\$ 1.211)", color="#27ae60",
        fontsize=8.1, fontweight="bold", va="bottom", ha="left")

ax.axvline(bank_inv_bps, color="#d35400", linestyle="--", linewidth=1.5, zorder=2)
ax.text(bank_inv_bps + 3.0, -0.68, f"Banco: Inv./Disp. pré-mai/25 (1,1% IOF)\n{bank_inv_bps:.1f} bps (R\\$ 7.129)", color="#d35400",
        fontsize=8.1, fontweight="bold", va="bottom", ha="left")

ax.axvline(bank_avl_bps, color="#c0392b", linestyle="--", linewidth=1.5, zorder=2)
ax.text(bank_avl_bps, -0.68, f"Banco: Disponibilidade pós-mai/25 (3,5% IOF)\n{bank_avl_bps:.1f} bps (R\\$ 20.041)", color="#c0392b",
        fontsize=8.1, fontweight="bold", va="bottom", ha="center")

ax.axhline(2.5, color=MUTED, linestyle=":", linewidth=1.0)
ax.text(515, 2.25, "CENÁRIOS REGULATÓRIOS", color=ORANGE, fontsize=8.5, fontweight="bold", ha="right")
ax.text(515, 2.95, "REGIMES HISTÓRICOS", color=BLUE, fontsize=8.5, fontweight="bold", ha="right")

ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=9.2)
ax.invert_yaxis()

ax.set_xlabel("Fricção Total de Transação para US\\$ 100.000 (pontos-base, bps)", fontweight="bold", labelpad=8)
ax.set_xlim(0, 525)

fig.suptitle("Fricções de Transação por Canal e Regime: Rota USDT e Referenciais Bancários",
             fontsize=13.2, fontweight="bold", x=0.04, y=0.96, ha="left")
fig.text(0.04, 0.912,
         f"Custo do ofício de 23/jun na rota USDT: +93,9 bps (R\\$ 5.052 por US\\$ 100k) no pico de 20 dias | Spread bancário PJ >US\\$ 55k: 20 bps (BCB EE 48/2019)",
         fontsize=9.6, color=INK2, ha="left")

fig.legend(loc="lower center", ncol=4, bbox_to_anchor=(0.52, 0.02), fontsize=8.8)

FIG.mkdir(parents=True, exist_ok=True)
out_fig = FIG / "P3-01_route_costs.png"
plt.savefig(out_fig, dpi=180, bbox_inches="tight")
plt.close()
print(f"Saved neutral publication-grade figure to {out_fig}")
