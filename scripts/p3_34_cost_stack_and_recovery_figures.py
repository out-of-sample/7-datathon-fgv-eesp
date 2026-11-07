"""P3-34: Cost-stack decomposition ("A Rede Não É o Custo") and 3-panel recovery & microstructure exhibit.

Purpose  Publication-grade figures and summary CSV for Tier 2 enhancements (F-040, improvements-proposal.md §4.B4).
         Figure 1: Cost stack comparison (access premium vs trading fee vs on-chain withdrawal fee, CEX vs DeFi).
         Figure 2: 3-panel aligned vertical exhibit ("Preço Normal Não É Mercado Normal"):
                   Panel A (daily): digital dollar premium on Binance, Foxbit, Mercado Bitcoin (bps).
                   Panel B (monthly): net foreign stablecoin acquisitions by residents (BCB SGS 29644, US$ bi/month).
                   Panel C (daily / regimes): 3-venue volume composition shift (Foxbit share: 6.8% -> 28.0% -> 34.7%)
                                             and business-hours seller-initiated flow (+361.9 mn USDT).
         Table:   results/tables/P3-34_cost_stack.csv (cost breakdown in bps and R$ per US$ 100k at PTAX).
Inputs   data/processed/P1-02_premium_daily.csv
         data/processed/P3-20_premium_daily.csv
         data/raw/bcb/sgs_29644.json
         results/tables/P3-17_daily_flow.csv
         results/tables/P3-25_composition.csv
         results/tables/P3-24_brla_s20.csv
Outputs  results/tables/P3-34_cost_stack.csv
         results/figures/P3-34_cost_stack.png
         results/figures/P3-34_price_vs_market_recovery.png
Run      py scripts/p3_34_cost_stack_and_recovery_figures.py
"""

import json
import os
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "results/figures"
TAB = ROOT / "results/tables"
PROC = ROOT / "data/processed"
RAW = ROOT / "data/raw"

FIG.mkdir(parents=True, exist_ok=True)
TAB.mkdir(parents=True, exist_ok=True)

# Visual palette matching scripts/p5_09_deck_figures.py
BG, INK, MUTED, GRID = "#F6F4EF", "#14213D", "#5B6573", "#DDD7CC"
BLUE, ORANGE, BAND = "#3B6EA8", "#D9622B", "#E7E2D8"
PX = 0.72  # font points per slide pixel

if os.environ.get("PLEX_DIR"):
    for f in Path(os.environ["PLEX_DIR"]).glob("IBMPlexSans-*.ttf"):
        font_manager.fontManager.addfont(str(f))
    plt.rcParams["font.family"] = "IBM Plex Sans"

plt.rcParams.update({
    "font.size": 22 * PX,
    "text.color": INK,
    "axes.labelcolor": MUTED,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "axes.edgecolor": GRID,
    "figure.facecolor": BG,
    "axes.facecolor": BG,
    "savefig.facecolor": BG,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": False,
})


def br(x, d=1):
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


# ==============================================================================
# 1. Table P3-34_cost_stack.csv
# ==============================================================================
def generate_cost_stack_table():
    # PTAX average over the acute shock window = 5.1418 BRL/USD (F-015, NOTICE_COST_SPIKE)
    ptax_ref = 5.1418

    # Table rows per specification
    rows = [
        {
            "cenario_ou_rota": "1. Antes do ofício (25/mai–22/jun)",
            "regime": "Pré-ofício (20 dias)",
            "tipo_rota": "USDT (CEX / Binance & Foxbit)",
            "premio_acesso_bps": 15.2,
            "taxa_negociacao_bps": "8,0–10,0",
            "taxa_saque_onchain_bps": "0,1–0,2",
            "custo_total_bps": "23,3–25,4",
            "custo_reais_por_100k_ptax": f"R$ {br(15.2 * 10 * ptax_ref + 8.0 * 10 * ptax_ref, 0)} – R$ {br(15.2 * 10 * ptax_ref + 10.0 * 10 * ptax_ref + 0.2 * 10 * ptax_ref, 0)}",
            "razao_choque_vs_rede": "—",
            "fontes": "F-016; R-04; R-05; A-02",
            "notas": "Prêmio médio na janela PTAX de 20 dias antes do ofício (F-016). Taxa de negociação VIP0 Binance (10 bps) / VIP Foxbit (8 bps). Taxa de saque: 1 USDT (0,1 bp) a 2 USDT (0,2 bp) em US$ 100k."
        },
        {
            "cenario_ou_rota": "2. Pico pós-ofício (24/jun–21/jul)",
            "regime": "Pico agudo (20 dias)",
            "tipo_rota": "USDT (CEX / Binance & Foxbit)",
            "premio_acesso_bps": 109.1,
            "taxa_negociacao_bps": "8,0–10,0",
            "taxa_saque_onchain_bps": "0,1–0,2",
            "custo_total_bps": "117,2–119,3",
            "custo_reais_por_100k_ptax": f"R$ {br(109.1 * 10 * ptax_ref + 8.0 * 10 * ptax_ref, 0)} – R$ {br(109.1 * 10 * ptax_ref + 10.0 * 10 * ptax_ref + 0.2 * 10 * ptax_ref, 0)}",
            "razao_choque_vs_rede": "—",
            "fontes": "F-016; R-04; R-05; A-02",
            "notas": "Prêmio médio na janela PTAX de 20 dias após o ofício (+93,9 bps de salto agudo)."
        },
        {
            "cenario_ou_rota": "3. Pós-pico (22/jul–30/out)",
            "regime": "Pós-pico / Arrefecimento",
            "tipo_rota": "USDT (CEX / Binance & Foxbit)",
            "premio_acesso_bps": 26.8,
            "taxa_negociacao_bps": "8,0–10,0",
            "taxa_saque_onchain_bps": "0,1–0,2",
            "custo_total_bps": "34,9–37,0",
            "custo_reais_por_100k_ptax": f"R$ {br(26.8 * 10 * ptax_ref + 8.0 * 10 * ptax_ref, 0)} – R$ {br(26.8 * 10 * ptax_ref + 10.0 * 10 * ptax_ref + 0.2 * 10 * ptax_ref, 0)}",
            "razao_choque_vs_rede": "—",
            "fontes": "F-011; F-022; P3-01; R-04; R-05",
            "notas": "Regime 6 em P3-01; resíduo pós-arrefecimento não distinguível de deriva ordinária (placebo p = 0,24)."
        },
        {
            "cenario_ou_rota": "4. Choque regulatório do ofício (+20 dias)",
            "regime": "Impacto regulatório marginal",
            "tipo_rota": "USDT (Impacto no prêmio)",
            "premio_acesso_bps": 93.9,
            "taxa_negociacao_bps": "0,0",
            "taxa_saque_onchain_bps": "0,0",
            "custo_total_bps": "93,9",
            "custo_reais_por_100k_ptax": "R$ 4.842,04",
            "razao_choque_vs_rede": "469,5× a 939,0× (~470× a 939× a taxa on-chain de 0,1–0,2 bps)",
            "fontes": "F-015; F-016; A-02; R-05; R-12",
            "notas": "Salto puro no prêmio de acesso: +93,9 bps equivale a 470× a taxa de 2 USDT (0,2 bp) e 939× a taxa de 1 USDT (0,1 bp)."
        },
        {
            "cenario_ou_rota": "5. Rota DeFi Polygon (Pix → BRLA → USDC) — Antes",
            "regime": "Pré-ofício (20 dias)",
            "tipo_rota": "DeFi On-Chain Polygon (Uniswap v3)",
            "premio_acesso_bps": 34.9,
            "taxa_negociacao_bps": "5,0 (pool fee)",
            "taxa_saque_onchain_bps": "0,0 (já on-chain)",
            "custo_total_bps": "39,9",
            "custo_reais_por_100k_ptax": f"R$ {br(39.9 * 10 * ptax_ref, 0)}",
            "razao_choque_vs_rede": "—",
            "fontes": "F-037; D-19 (pool 0x0e77...c956)",
            "notas": "Prêmio da rota Polygon na janela PTAX de 20 dias antes do ofício (F-037). Taxa do pool Uniswap v3 USDC/BRLA: 0,05% (5 bps)."
        },
        {
            "cenario_ou_rota": "6. Rota DeFi Polygon (Pix → BRLA → USDC) — Pico",
            "regime": "Pico agudo (20 dias)",
            "tipo_rota": "DeFi On-Chain Polygon (Uniswap v3)",
            "premio_acesso_bps": 145.9,
            "taxa_negociacao_bps": "5,0 (pool fee)",
            "taxa_saque_onchain_bps": "0,0 (já on-chain)",
            "custo_total_bps": "150,9",
            "custo_reais_por_100k_ptax": f"R$ {br(150.9 * 10 * ptax_ref, 0)}",
            "razao_choque_vs_rede": "—",
            "fontes": "F-037; D-19",
            "notas": "Prêmio da rota Polygon na janela PTAX de 20 dias após o ofício (+111,0 bps sobre o pré-ofício)."
        },
        {
            "cenario_ou_rota": "7. Rota DeFi Polygon — Choque (+20 dias)",
            "regime": "Impacto regulatório marginal",
            "tipo_rota": "DeFi On-Chain Polygon (Uniswap v3)",
            "premio_acesso_bps": 111.0,
            "taxa_negociacao_bps": "0,0",
            "taxa_saque_onchain_bps": "0,0",
            "custo_total_bps": "111,0",
            "custo_reais_por_100k_ptax": f"R$ {br(111.0 * 10 * ptax_ref, 0)}",
            "razao_choque_vs_rede": "22,2× taxa do pool (555× a 1.110× taxa on-chain 0,1–0,2 bps)",
            "fontes": "F-037; P3-24",
            "notas": "Salto regulatório na rota DeFi (+111,0 bps): 22× a taxa do pool de 5 bps. Observação compatível com fricções compartilhadas; sem identificação causal."
        }
    ]

    df = pd.DataFrame(rows)
    df.to_csv(TAB / "P3-34_cost_stack.csv", index=False, encoding="utf-8-sig")
    print("wrote results/tables/P3-34_cost_stack.csv")
    return df


# ==============================================================================
# 2. Figure 1: P3-34_cost_stack.png
# ==============================================================================
def plot_cost_stack():
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(16.0, 7.0), dpi=200, gridspec_kw={"width_ratios": [1.05, 1.05]})

    # --- Panel 1: USDT CEX Route Decomposition ---
    categories = [
        "1. Antes do ofício\n(25/mai–22/jun)",
        "2. Pico pós-ofício\n(24/jun–21/jul)",
        "3. Pós-pico\n(22/jul–30/out)"
    ]
    y_pos = np.array([2.2, 1.25, 0.35])

    prem = np.array([15.2, 109.1, 26.8])
    fee = np.array([9.0, 9.0, 9.0])       # midpoint of 8.0-10.0 bps
    onchain = np.array([0.15, 0.15, 0.15]) # midpoint of 0.1-0.2 bp (1-2 USDT on 100k)

    # Horizontal stacked bars
    ax1.barh(y_pos, onchain, color=INK, height=0.42, label="Taxa de saque on-chain (0,1–0,2 bps; 1–2 USDT)")
    ax1.barh(y_pos, fee, left=onchain, color=BLUE, height=0.42, label="Taxa corretora (8–10 bps)")

    # Differentiate the jump in the peak bar
    colors_prem = [BLUE, ORANGE, BLUE]
    for i, y in enumerate(y_pos):
        ax1.barh(y, prem[i], left=onchain[i] + fee[i], color=colors_prem[i], height=0.42,
                 label="Prêmio de acesso s/ PTAX (bps)" if i == 0 else "")

    # Add text labels on bars
    for i, y in enumerate(y_pos):
        tot = onchain[i] + fee[i] + prem[i]
        label_text = f"Total: {br(tot)} bps"
        if i == 1:
            label_text += f"\n(+{br(prem[1] - prem[0])} bps choque)"
        ax1.text(tot + 3.0, y, label_text, va="center", ha="left", fontsize=17.5 * PX, weight="bold",
                 color=ORANGE if i == 1 else INK)

    # Highlight ratio box placed cleanly below bars (single $ to avoid Matplotlib TeX math mode)
    ratio_box = (
        "PRÊMIO INCREMENTAL / TAXA LISTADA:\n"
        "• Choque na porta: +93,9 bps (R$ 4.842 p/ 100k USDT)\n"
        "• Taxa de rede on-chain: 0,1 a 0,2 bps (1 a 2 USDT)\n"
        "→ Razão: 470–939× (não compara custos totais)"
    )
    ax1.text(0.02, 0.03, ratio_box, transform=ax1.transAxes, fontsize=15.8 * PX,
             bbox=dict(boxstyle="round,pad=0.5", facecolor=BAND, edgecolor=ORANGE, lw=1.5),
             color=INK, weight="semibold", va="bottom", ha="left")

    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(categories, fontsize=18 * PX, weight="semibold", color=INK)
    ax1.set_ylim(-0.95, 3.05)
    ax1.set_xlim(0, 185)
    ax1.set_xlabel("Proxy: prêmio + taxas listadas (bps sobre PTAX)", fontsize=18 * PX)
    ax1.set_title("Decomposição do Custo: Rota USDT Centralizada", fontsize=19.5 * PX, weight="bold", color=INK, pad=10)
    ax1.grid(axis="x", color=GRID, lw=0.8, ls="--")
    ax1.tick_params(length=0)
    ax1.legend(loc="upper right", fontsize=15 * PX, frameon=False)

    # --- Panel 2: CEX vs DeFi On-Chain Comparison ---
    routes = [
        "Binance USDT/BRL\n(Corretora CEX)",
        "Polygon Pix → BRLA → USDC\n(DeFi / Uniswap v3)"
    ]
    y_r = np.array([2.0, 0.95])
    pre_shocks = np.array([15.2, 34.9])
    shock_deltas = np.array([93.9, 111.0])

    # Plot base pre-shock premium and shock delta
    ax2.barh(y_r, pre_shocks, color=BLUE, height=0.42, label="Prêmio pré-ofício (20 dias antes)")
    ax2.barh(y_r, shock_deltas, left=pre_shocks, color=ORANGE, height=0.42, label="Salto do ofício (+20 dias pós-ofício)")

    for i, y in enumerate(y_r):
        total_prem = pre_shocks[i] + shock_deltas[i]
        fee_name = "taxa CEX 8–10 bps" if i == 0 else "taxa pool 5 bps"
        ax2.text(total_prem + 3.0, y, f"Pico: {br(total_prem)} bps\n(+{br(shock_deltas[i])} bps; {fee_name})",
                 va="center", ha="left", fontsize=17.5 * PX, weight="bold", color=ORANGE)

    defi_box = (
        "O PRÊMIO TAMBÉM SUBIU NA ROTA DEFI:\n"
        "• Uniswap v3 (Polygon): +111,0 bps (34,9 → 145,9 bps)\n"
        "• Taxa do pool é de apenas 5,0 bps (0,05%)\n"
        "→ Choque DeFi = 22,2× a taxa do pool (sem identificação causal)"
    )
    ax2.text(0.02, 0.03, defi_box, transform=ax2.transAxes, fontsize=15.5 * PX,
             bbox=dict(boxstyle="round,pad=0.5", facecolor=BAND, edgecolor=BLUE, lw=1.5),
             color=INK, weight="semibold", va="bottom", ha="left")

    ax2.set_yticks(y_r)
    ax2.set_yticklabels(routes, fontsize=18 * PX, weight="semibold", color=INK)
    ax2.set_ylim(-0.95, 3.05)
    ax2.set_xlim(0, 285)
    ax2.set_xlabel("Prêmio sobre PTAX (bps)", fontsize=18 * PX)
    ax2.set_title("Comparação: Corretora CEX vs. DeFi On-Chain", fontsize=19.5 * PX, weight="bold", color=INK, pad=10)
    ax2.grid(axis="x", color=GRID, lw=0.8, ls="--")
    ax2.tick_params(length=0)
    ax2.legend(loc="upper right", fontsize=15 * PX, frameon=False)

    f.suptitle("Transferência barata não garante conversão barata: salto observado (+93,9 bps) equivale a 470–939× a taxa on-chain (0,1–0,2 bps) e alta na rota DeFi (+111,0 bps)",
               fontsize=19 * PX, weight="bold", color=INK, y=0.97)
    f.subplots_adjust(left=0.15, right=0.98, top=0.86, bottom=0.11, wspace=0.38)
    f.savefig(FIG / "P3-34_cost_stack.png", dpi=200)
    plt.close(f)
    print("wrote results/figures/P3-34_cost_stack.png")


# ==============================================================================
# 3. Figure 2: P3-34_price_vs_market_recovery.png (3-Panel Exhibit)
# ==============================================================================
def plot_recovery_3panel():
    # Load inputs
    # 1. Premium across 3 venues (daily, Jan-Oct 2026)
    p320 = pd.read_csv(PROC / "P3-20_premium_daily.csv", parse_dates=["date_brt"]).set_index("date_brt")
    p2026 = p320.loc["2026-01-02":"2026-10-30"]

    # 2. BCB SGS 29644 net foreign stablecoin acquisitions (monthly, Jan-Sep 2026)
    s_raw = pd.DataFrame(json.loads((RAW / "bcb/sgs_29644.json").read_text()))
    s_series = pd.Series(-s_raw.valor.astype(float).values / 1000.0,
                         index=pd.to_datetime(s_raw.data, dayfirst=True)).loc["2026-01-01":"2026-09-01"]

    # 3. Microstructure: daily Foxbit share and flow
    # P3-17 has daily flow from 2026-05-01 to 2026-09-30
    p317 = pd.read_csv(TAB / "P3-17_daily_flow.csv").rename(columns={"Unnamed: 0": "date_brt"})
    p317["date_brt"] = pd.to_datetime(p317["date_brt"])
    p317 = p317.set_index("date_brt")

    # Dates and events
    t_oficio = pd.Timestamp("2026-06-23")
    t_fade = pd.Timestamp("2026-07-22")
    start_date = pd.Timestamp("2025-12-18")
    end_date = pd.Timestamp("2026-11-02")

    f, (ax_a, ax_b, ax_c) = plt.subplots(3, 1, figsize=(14.2, 11.4), dpi=200, sharex=True,
                                         gridspec_kw={"height_ratios": [1.15, 1.05, 1.15], "hspace": 0.32})

    # --------------------------------------------------------------------------
    # Painel A: Prêmio Diário nas 3 Corretoras (Binance, Foxbit, Mercado Bitcoin)
    # --------------------------------------------------------------------------
    ax_a.plot(p2026.index, p2026["Binance"], color=INK, lw=2.0, label="Binance (USDT/BRL)")
    ax_a.plot(p2026.index, p2026["Foxbit"], color=ORANGE, lw=2.0, label="Foxbit (USDT/BRL)")
    ax_a.plot(p2026.index, p2026["Mercado Bitcoin"], color=BLUE, lw=1.6, ls="-.", label="Mercado Bitcoin (USDT-BRL)")

    # Event highlight
    ax_a.axvspan(pd.Timestamp("2026-06-24"), pd.Timestamp("2026-07-21"), color=ORANGE, alpha=0.12, lw=0)
    ax_a.axvline(t_oficio, color=INK, lw=1.5, ls="--")
    ax_a.axvline(t_fade, color=MUTED, lw=1.3, ls=":")

    # Text annotations
    ax_a.text(t_oficio - pd.Timedelta(days=4), 178, "23/jun: Ofício BCB\n(+93,9 bps)", ha="right", va="top",
              fontsize=17.5 * PX, weight="bold", color=INK)
    ax_a.text(t_fade + pd.Timedelta(days=6), 170, "22/jul: Arrefecimento do preço\n(26,8 bps; placebo p = 0,24)",
              ha="left", va="top", fontsize=17 * PX, weight="semibold", color=MUTED)

    # 20-day pre/post lines
    t_pre_start = t_oficio - pd.Timedelta(days=29)
    ax_a.hlines(15.2, t_pre_start, t_oficio, color=INK, lw=2.2, ls="--")
    ax_a.text(t_pre_start - pd.Timedelta(days=3), 18.0, "Pré: 15,2 bps", ha="right", va="center",
              fontsize=17 * PX, weight="bold")

    ax_a.hlines(109.1, pd.Timestamp("2026-06-24"), pd.Timestamp("2026-07-21"), color=ORANGE, lw=2.6)
    ax_a.text(pd.Timestamp("2026-07-07"), 113.0, "Pico: 109,1 bps", ha="center", va="bottom",
              fontsize=17 * PX, weight="bold", color=ORANGE)

    ax_a.set_ylabel("Prêmio s/ PTAX (bps)", fontsize=18 * PX)
    ax_a.set_ylim(-40, 210)
    ax_a.set_title("Painel A · Diário: Prêmio do dólar digital sobre a PTAX nas 3 corretoras (salto em 24/jun e arrefecimento pós-22/jul)",
                   loc="left", fontsize=18 * PX, weight="bold", color=INK, pad=8)
    ax_a.legend(loc="upper left", fontsize=16 * PX, frameon=False, ncol=3)
    ax_a.grid(axis="y", color=GRID, lw=0.8, ls="--")
    ax_a.tick_params(length=0)

    # --------------------------------------------------------------------------
    # Painel B: Aquisições Líquidas de Stablecoins no Exterior (BCB SGS 29644)
    # --------------------------------------------------------------------------
    # Monthly discrete bars (never interpolating monthly into daily)
    bar_width = 18  # days
    is_post_july = s_series.index >= "2026-07-01"
    colors_b = np.where(is_post_july, ORANGE, BLUE)

    ax_b.bar(s_series.index, s_series.values, width=bar_width, color=colors_b, align="center")

    # Annotations on values
    for dt_val, val in s_series.items():
        txt = f"{br(val, 2)} bi"
        if dt_val.strftime("%Y-%m") == "2026-07":
            txt += "\n(−78%)"
        ax_b.text(dt_val, val + 0.08, txt, ha="center", va="bottom", fontsize=16 * PX,
                  weight="bold", color=ORANGE if dt_val >= pd.Timestamp("2026-07-01") else INK)

    # Pre-notice average horizontal line (Jan-Jun: ~2.45 bi/month)
    pre_mean_b = s_series.loc["2026-01-01":"2026-06-01"].mean()
    post_mean_b = s_series.loc["2026-08-01":"2026-09-01"].mean()

    ax_b.hlines(pre_mean_b, pd.Timestamp("2025-12-22"), pd.Timestamp("2026-06-15"), color=BLUE, lw=1.8, ls=":")
    ax_b.text(pd.Timestamp("2026-01-02"), 3.22, f"Média jan–jun: US$ {br(pre_mean_b, 2)} bi/mês",
              fontsize=17 * PX, color=BLUE, weight="bold", va="center")

    ax_b.hlines(post_mean_b, pd.Timestamp("2026-07-20"), pd.Timestamp("2026-09-25"), color=ORANGE, lw=1.8, ls=":")
    ax_b.text(pd.Timestamp("2026-07-26"), 1.65, f"Média ago–set: US$ {br(post_mean_b, 2)} bi (~32% do pré)",
              fontsize=17 * PX, color=ORANGE, weight="bold", ha="left", va="center")

    ax_b.axvline(t_oficio, color=INK, lw=1.5, ls="--")
    ax_b.axvline(t_fade, color=MUTED, lw=1.3, ls=":")
    ax_b.set_ylabel("Aquisições (US$ bi/mês)", fontsize=18 * PX)
    ax_b.set_ylim(0, 3.65)
    ax_b.set_title("Painel B · Mensal: Aquisições líquidas de stablecoins no exterior (BCB SGS 29644) recuam −78% e persistem em um terço",
                   loc="left", fontsize=18 * PX, weight="bold", color=INK, pad=8)
    ax_b.grid(axis="y", color=GRID, lw=0.8, ls="--")
    ax_b.tick_params(length=0)

    # --------------------------------------------------------------------------
    # Painel C: Microestrutura e Composição entre as Três Corretoras
    # --------------------------------------------------------------------------
    # Foxbit share rolling 7 days from P3-17
    fox_share_pct = p317["fox_share"] * 100
    rolling_fox = fox_share_pct.rolling(7, min_periods=1).mean()

    ax_c.plot(rolling_fox.index, rolling_fox.values, color=ORANGE, lw=2.4, label="Fatia da Foxbit (média móvel 7 dias, %)")

    # Regime lines from P3-25 composition table: 6.8% -> 28.0% -> 34.7%
    reg_pre_start, reg_pre_end = pd.Timestamp("2026-05-01"), pd.Timestamp("2026-06-22")
    reg_wave_start, reg_wave_end = pd.Timestamp("2026-06-24"), pd.Timestamp("2026-07-21")
    reg_after_start, reg_after_end = pd.Timestamp("2026-07-22"), pd.Timestamp("2026-10-30")

    ax_c.hlines(6.8, reg_pre_start, reg_pre_end, color=BLUE, lw=2.8, ls="-")
    ax_c.text(reg_pre_start, 9.0, "Pré: 6,8%", fontsize=17 * PX, weight="bold", color=BLUE)

    ax_c.hlines(28.0, reg_wave_start, reg_wave_end, color=ORANGE, lw=3.2, ls="-")
    ax_c.text(reg_wave_start + pd.Timedelta(days=1), 30.5, "Pico: 28,0%", fontsize=17.5 * PX, weight="bold", color=ORANGE)

    ax_c.hlines(34.7, reg_after_start, reg_after_end, color=INK, lw=2.8, ls="-")
    ax_c.text(pd.Timestamp("2026-08-02"), 37.5, "Pós-pico: 34,7% (+27,9 p.p.)", fontsize=17.5 * PX, weight="bold", color=INK)

    # Annotate seller-initiated trading during the wave (F-031) in clean left space (Jan-Apr)
    wave_box = (
        "FLUXO VENDEDOR EM HORÁRIO COMERCIAL (F-031 / F-036):\n"
        "• Foxbit registrou +361,9 mi USDT de vendas agressivas (30/jun–21/jul)\n"
        "• 96,5% do volume concentrado entre 9h e 18h Brasília (vs 81,7% pré)\n"
        "• Tamanho médio do trade saltou 5× (740 → 4.019 USDT)"
    )
    ax_c.text(0.015, 0.38, wave_box, transform=ax_c.transAxes, fontsize=16 * PX,
              bbox=dict(boxstyle="round,pad=0.5", facecolor=BAND, edgecolor=ORANGE, lw=1.2),
              color=INK, weight="semibold", va="center", ha="left")

    ax_c.axvspan(pd.Timestamp("2026-06-24"), pd.Timestamp("2026-07-21"), color=ORANGE, alpha=0.12, lw=0)
    ax_c.axvline(t_oficio, color=INK, lw=1.5, ls="--")
    ax_c.axvline(t_fade, color=MUTED, lw=1.3, ls=":")

    ax_c.set_ylabel("Fatia Foxbit (% do vol.)", fontsize=18 * PX)
    ax_c.set_ylim(0, 62)
    ax_c.set_title("Painel C · Microestrutura: Recomposição persistente da fatia da Foxbit (6,8% → 28,0% → 34,7%) e fluxo vendedor comercial",
                   loc="left", fontsize=18 * PX, weight="bold", color=INK, pad=8)
    ax_c.grid(axis="y", color=GRID, lw=0.8, ls="--")
    ax_c.tick_params(length=0)
    ax_c.legend(loc="upper left", fontsize=16 * PX, frameon=False)

    # Common x-axis formatting
    ax_c.set_xlim(start_date, end_date)
    month_ticks = pd.date_range("2026-01-01", "2026-10-01", freq="MS")
    ax_c.set_xticks(month_ticks)
    ax_c.set_xticklabels(["jan/26", "fev/26", "mar/26", "abr/26", "mai/26", "jun/26", "jul/26", "ago/26", "set/26", "out/26"],
                         fontsize=18 * PX)

    f.suptitle("Preço Normal Não É Mercado Normal: Enquanto o Prêmio Cedeu, o Fluxo Cambial Caiu 78% e a Estrutura de Mercado Mudou",
               fontsize=19 * PX, weight="bold", color=INK, y=0.98)

    f.subplots_adjust(left=0.075, right=0.98, top=0.93, bottom=0.055)
    f.savefig(FIG / "P3-34_price_vs_market_recovery.png", dpi=200)
    plt.close(f)
    print("wrote results/figures/P3-34_price_vs_market_recovery.png")


def main():
    print("Executing P3-34 cost-stack and recovery figures...")
    generate_cost_stack_table()
    plot_cost_stack()
    plot_recovery_3panel()
    print("P3-34 completed successfully.")


if __name__ == "__main__":
    main()
