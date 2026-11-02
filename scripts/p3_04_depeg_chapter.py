r"""P3-04: Depeg chapter v1 — the same mechanism in dollars.

Purpose
  Produce the empirical chapter tying the primary project's limits-to-arbitrage framework
  (USDT/BRL premium over PTAX driven by FX and banking channel closure) to dollar stablecoin
  parity. When primary redemption channels (US bank wires) close over the weekend, secondary-market
  prices drift below $1.00; as soon as credible 1:1 primary redemption is guaranteed, arbitrageurs
  restore parity even before commercial banking rails physically reopen.

  Evaluates the verified v2 depeg screen from P1-07 / F-013, tests the pre-committed sample-size rule
  for Kaplan-Meier survival curves (n >= 12 required; since n = 11 < 12, KM curves are omitted per protocol),
  builds a structured comparative case table across 4 economic categories, copies the finalized SVB weekend
  figure, and creates a multi-panel chapter figure of trough prices and recovery durations.

Inputs
  results/tables/P1-07_v1_vs_v2.csv          verified v2 depeg screen from P1-07 / F-013
  results/figures/P1-07_svb_weekend_v2.png   finalized Bitstamp USDC/USD SVB weekend hourly chart

Outputs
  results/tables/P3-04_depeg_case_table.csv  11 screen downward depegs + USDC benchmark with categories and mechanisms
  results/tables/P3-04_category_summary.csv  aggregate metrics by economic category
  results/figures/P3-04_svb_weekend.png      chapter slide 1 figure (SVB weekend timeline)
  results/figures/P3-04_depeg_cases.png      chapter slide 2 figure (comparative trough & duration across categories)

How to run
  py scripts/p3_04_depeg_chapter.py
"""
import shutil
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
TAB = ROOT / "results" / "tables"
FIG = ROOT / "results" / "figures"
KM_THRESHOLD = 12

# Color palette aligned with project standard
BLUE = "#1d5b96"
LIGHT_BLUE = "#4a90e2"
TEAL = "#2b8a78"
ORANGE = "#d95f02"
RED = "#b2182b"
GRAY = "#70757a"
LIGHT_GRAY = "#f1f3f4"
GRID = "#e0e0e0"
INK = "#202124"
INK2 = "#5f6368"


def main():
    print("=" * 70)
    print("P3-04: DEPEG CHAPTER V1 (THE SAME MECHANISM IN DOLLARS)")
    print("=" * 70)

    # 1. Load verified screen candidates from P1-07
    screen_path = TAB / "P1-07_v1_vs_v2.csv"
    if not screen_path.exists():
        raise FileNotFoundError(f"Missing screen table: {screen_path}")
    raw_screen = pd.read_csv(screen_path)

    # 2. Filter to USD-confirmed downward depeg events (direction == 'below')
    dn = raw_screen[
        (raw_screen["classification_v2"] == "USD-confirmed")
        & (raw_screen["direction"] == "below")
    ].copy()

    # Distinguish subsets:
    # 11 total downward events
    # 9 excluding USDP pre-delisting drift in Sep 2026 (USDP-09, USDP-10)
    # 8 excluding UST's terminal collapse (UST-03) and the two pre-delisting drifts
    is_usdp_drift = dn["event_id"].isin(["P1-07-USDPUSDT-09", "P1-07-USDPUSDT-10"])
    is_terminal = dn["event_id"] == "P1-07-USTUSDT-03"

    n_events = len(dn)
    n_ex_usdp_drift = len(dn[~is_usdp_drift])
    n_ex_terminal_and_drift = len(dn[~is_usdp_drift & ~is_terminal])

    print(f"\n1. SCREEN FILTERING RESULTS:")
    print(f"   Total USD-confirmed downward depegs (v2_keep): {n_events}")
    print(f"   Excluding pre-delisting drift (USDP Sep 2026): {n_ex_usdp_drift}")
    print(f"   Excluding terminal collapse (UST May 2022) & drift: {n_ex_terminal_and_drift}")

    # 3. Explicit check of pre-committed threshold rule (docs/01-depeg-recovery.md §5, docs/README.md line 96)
    print(f"\n2. PRE-COMMITTED SURVIVAL ANALYSIS THRESHOLD CHECK:")
    print(f"   Required sample threshold: n >= {KM_THRESHOLD} independent events")
    print(f"   Observed downward events:  n = {n_events}")
    if n_events < KM_THRESHOLD:
        print(f"   -> PRE-COMMITTED RULE APPLIED: {n_events} < {KM_THRESHOLD}. Kaplan-Meier survival curves and Cox hazard")
        print("      regressions are OMITTED per research protocol (docs/01-depeg-recovery.md §5).")
        print("      Replaced by a structured 11-event comparative case study table and cross-event duration/trough taxonomy.")
    else:
        print("   -> Threshold satisfied. Survival analysis permitted.")

    # 4. Parse dates, durations, trough prices
    dn["start"] = pd.to_datetime(dn["start_utc_v2"])
    dn["end"] = pd.to_datetime(dn["end_utc_v2"])
    dn["duration_hours"] = (dn["end"] - dn["start"]).dt.total_seconds() / 3600.0
    dn["trough_usd"] = 1.0 - (dn["max_deviation_bps_v2"] / 10000.0)
    dn["max_dev_bps"] = dn["max_deviation_bps_v2"]
    dn["recovered"] = ~dn["censored_v2"].astype(bool)

    # Stablecoin symbol extraction
    dn["coin"] = dn["event_id"].str.extract(r"P1-07-([A-Z]+)USDT-")[0]

    # 5. Economic categorization and mechanisms
    # Category definitions:
    # Cat 1: Weekend / redemption-gate closure on solvent fiat-backed stablecoin
    # Cat 2: Brief liquidity/redemption frictions in fiat/crypto-backed stablecoins
    # Cat 3: Insolvent / algorithmic collapse
    # Cat 4: Pre-delisting drift
    categories = []
    cat_names = []
    mechanisms = []

    for _, row in dn.iterrows():
        eid = row["event_id"]
        coin = row["coin"]

        if "USTUSDT-03" in eid:
            categories.append(3)
            cat_names.append("3. Colapso algorítmico / insolvência")
            mechanisms.append(
                "Espiral da morte algorítmica: corrida no Anchor Protocol esgotou liquidez do Curve; "
                "hiperinflação de LUNA não conteve a pressão vendedora; reservas zeradas; colapso terminal e deslistagem."
            )
        elif is_usdp_drift[row.name]:
            categories.append(4)
            cat_names.append("4. Fim dos dados na Binance (deslistagem a verificar)")
            mechanisms.append(
                "Deslistagem programada na Binance: esvaziamento do livro de ofertas e secagem de "
                "liquidez secundária nos dias finais de negociação da exchange."
            )
        elif "USDPUSDT-02" in eid:
            categories.append(1)
            cat_names.append("1. Fim de semana bancário / canal de resgate fechado")
            mechanisms.append(
                "Contágio do colapso do SVB: apreensão por depósitos da Paxos no Signature Bank combinada ao "
                "fechamento do Fedwire/ACH no fim de semana; paridade restaurada na segunda após abertura bancária."
            )
        elif "USTUSDT-01" in eid:
            categories.append(2)
            cat_names.append("2. Fricção temporária de liquidez/resgate")
            mechanisms.append(
                "Onda de liquidação no DeFi (MIM/Abracadabra); arbitradores absorveram descolamento em 21h "
                "via queima/emissão antes do colapso de reservas."
            )
        elif "FDUSDUSDT-04" in eid:
            categories.append(2)
            cat_names.append("2. Fricção temporária de liquidez/resgate")
            mechanisms.append(
                "Volatilidade súbita do mercado cripto e descompasso transitório no livro de ordens; canal primário "
                "1:1 do emissor permaneceu operacional, fechando o spread em 5 dias."
            )
        elif "FDUSDUSDT-07" in eid:
            categories.append(2)
            cat_names.append("2. Fricção temporária de liquidez/resgate")
            mechanisms.append(
                "Boatos e alegações sobre solvência de custodiantes parceiros geraram desconto secundário; "
                "atestações mensais e honra integral de resgates fiat restabeleceram paridade."
            )
        elif "TUSDUSDT-11" in eid:
            categories.append(2)
            cat_names.append("2. Fricção temporária de liquidez/resgate")
            mechanisms.append(
                "Escrutínio regulatório e atrasos operacionais no processamento de resgates institucionais de TUSD; "
                "arbitragem gradual ao longo de 48 dias conforme resgates foram liquidados."
            )
        elif "TUSDUSDT-13" in eid:
            categories.append(2)
            cat_names.append("2. Fricção temporária de liquidez/resgate")
            mechanisms.append(
                "Esvaziamento gradual de liquidez pós-mudança de política de taxas zero na Binance; arbitragem lenta "
                "via trilhos bancários internacionais."
            )
        elif "TUSDUSDT-14" in eid:
            categories.append(2)
            cat_names.append("2. Fricção temporária de liquidez/resgate")
            mechanisms.append(
                "Choque de demanda por USDT pós-eleição americana; descolamento de 80 bps absorvido em 4,5 dias "
                "sem comprometimento de reservas."
            )
        elif "TUSDUSDT-16" in eid:
            categories.append(2)
            cat_names.append("2. Fricção temporária de liquidez/resgate")
            mechanisms.append(
                "Baixa liquidez secundária persistente e deslistagem parcial; convergência via resgates e queima "
                "lenta pelo emissor ao longo de ~3,7 meses."
            )
        else:
            categories.append(2)
            cat_names.append("2. Fricção temporária de liquidez/resgate")
            mechanisms.append("Descompasso temporário de liquidez e fluxo de resgate.")

    dn["category_id"] = categories
    dn["category_name"] = cat_names
    # Review 2 Nov: none of these causes has an opened source (prompt.md §6), so the table states that instead of
    # asserting a cause. The texts above are kept as leads for whoever sources them.
    dn["mechanism_lead_unsourced"] = mechanisms
    dn["mechanism"] = "Causa não verificada (sem fonte aberta); ver mechanism_lead_unsourced"
    dn["recovery_status"] = np.where(dn["recovered"], "Recuperado", "Não recuperado (censurado)")

    # 6. Add Benchmark Case Row: USDC SVB Weekend (Bitstamp direct USD OHLC)
    usdc_benchmark = {
        "event_id": "CASE-USDC-SVB",
        "pair": "USDC/USD (Bitstamp)",
        "coin": "USDC",
        "category_id": 1,
        "category_name": "1. Fim de semana bancário / canal de resgate fechado",
        "start_utc_v2": "2023-03-10T21:00:00Z",
        "end_utc_v2": "2023-03-13T14:00:00Z",
        "duration_hours": 65.0,
        "trough_usd": 0.863,  # hourly close ($0.805 intra-hour low)
        "max_dev_bps": 1370.0,  # 1950 bps intra-hour
        "recovered": True,
        "recovery_status": "Recuperado",
        "near_delisting": False,
        "mechanism": (
            "Bancos dos EUA fechados de sex 16h a seg 9h30 (NY). Menor fechamento horário US$ 0,863 (sáb 07h UTC; mínimo "
            "intra-hora US$ 0,805, Bitstamp). Garantia dos depósitos do SVB anunciada dom 22h15 UTC (D-13); US$ 0,989 "
            "às 23h, antes da reabertura dos bancos."
        ),
    }

    # Format table for output
    cols_export = [
        "event_id",
        "coin",
        "category_id",
        "category_name",
        "start_utc_v2",
        "end_utc_v2",
        "duration_hours",
        "trough_usd",
        "max_dev_bps",
        "recovery_status",
        "near_delisting",
        "mechanism",
        "mechanism_lead_unsourced",
    ]

    table_11 = dn[cols_export].copy()
    full_table = pd.concat([pd.DataFrame([usdc_benchmark]), table_11], ignore_index=True)
    full_table = full_table.sort_values(["category_id", "start_utc_v2"]).reset_index(drop=True)

    out_table_path = TAB / "P3-04_depeg_case_table.csv"
    full_table.to_csv(out_table_path, index=False, encoding="utf-8")
    print(f"\n3. CASE TABLE CREATED: {out_table_path}")
    for _, r in full_table.iterrows():
        dur_str = f"{r['duration_hours']:5.0f}h" if pd.notna(r['duration_hours']) else "  cens"
        print(f"   {r['event_id']:<18} {r['coin']:<5} Cat {r['category_id']} | Trough: ${r['trough_usd']:.3f} | Dur: {dur_str} | Status: {r['recovery_status']}")

    # 7. Build category summary table
    cat_summary = []
    for cat_id, group in full_table.groupby("category_id"):
        cat_name = group["category_name"].iloc[0]
        n_ev = len(group)
        coins = ", ".join(group["coin"].unique())
        rec_count = (group["recovery_status"] == "Recuperado").sum()
        rec_rate = (rec_count / n_ev) * 100.0
        dur_rec = group[group["recovery_status"] == "Recuperado"]["duration_hours"]
        dur_str = f"{dur_rec.median():.0f}h ({dur_rec.min():.0f}h–{dur_rec.max():.0f}h)" if len(dur_rec) > 0 else "N/A (Censurado)"
        trough_min = group["trough_usd"].min()
        trough_max = group["trough_usd"].max()

        cat_summary.append({
            "category_id": cat_id,
            "category_name": cat_name,
            "n_events": n_ev,
            "stablecoins": coins,
            "recovery_rate_pct": rec_rate,
            "duration_recovered": dur_str,
            "trough_price_range_usd": f"${trough_min:.3f} – ${trough_max:.3f}",
            "core_economic_mechanism": (
                "Arbitragem bloqueada por horário bancário; paridade restaurada imediatamente após garantia de resgate."
                if cat_id == 1 else
                "Solvência mantida; atrito operacional/escrutínio atrasa arbitragem mas paridade é preservada."
                if cat_id == 2 else
                "Insolvência patrimonial completa; espiral da morte sem colateral externo."
                if cat_id == 3 else
                "Secagem de liquidez secundária por deslistagem programada em exchange."
            ),
        })

    cat_summary_df = pd.DataFrame(cat_summary)
    cat_summary_path = TAB / "P3-04_category_summary.csv"
    cat_summary_df.to_csv(cat_summary_path, index=False, encoding="utf-8")
    print(f"\n4. CATEGORY SUMMARY CREATED: {cat_summary_path}")
    for _, r in cat_summary_df.iterrows():
        print(f"   Cat {r['category_id']}: {r['category_name']} | N={r['n_events']} | Taxa rec={r['recovery_rate_pct']:.0f}% | Dur={r['duration_recovered']}")

    # 8. Copy SVB weekend figure
    svb_src = FIG / "P1-07_svb_weekend_v2.png"
    svb_dst = FIG / "P3-04_svb_weekend.png"
    if svb_src.exists():
        shutil.copyfile(svb_src, svb_dst)
        print(f"\n5. SVB WEEKEND FIGURE COPIED: {svb_dst}")
    else:
        print(f"\n5. WARNING: Source SVB figure {svb_src} not found!")

    # 9. Generate publication-grade comparative figure (P3-04_depeg_cases.png)
    plot_comparative_cases(full_table)


def plot_comparative_cases(df: pd.DataFrame):
    """Generate a clean 2-panel comparative visualization of the depeg events."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6.2), gridspec_kw={"width_ratios": [1.1, 1.0]})

    # Palette by category
    cat_colors = {
        1: BLUE,        # Bank closure / weekend
        2: TEAL,        # Operational friction
        3: RED,         # Insolvent collapse
        4: GRAY,        # Pre-delisting
    }

    # Clean display labels
    labels = []
    for _, r in df.iterrows():
        eid = r["event_id"]
        coin = r["coin"]
        dt = r["start_utc_v2"][:7] if pd.notna(r["start_utc_v2"]) else ""
        if eid == "CASE-USDC-SVB":
            lbl = "USDC (SVB, mar/23)*"
        elif "USDPUSDT-02" in eid:
            lbl = "USDP (SVB, mar/23)"
        elif "USTUSDT-03" in eid:
            lbl = "UST (Colapso, mai/22)"
        elif "USTUSDT-01" in eid:
            lbl = "UST (Fricção, jan/22)"
        elif "FDUSDUSDT-04" in eid:
            lbl = "FDUSD (mar/24)"
        elif "FDUSDUSDT-07" in eid:
            lbl = "FDUSD (Custódia, abr/25)"
        elif "TUSDUSDT-11" in eid:
            lbl = "TUSD (jan/24)"
        elif "TUSDUSDT-13" in eid:
            lbl = "TUSD (out/24)"
        elif "TUSDUSDT-14" in eid:
            lbl = "TUSD (nov/24)"
        elif "TUSDUSDT-16" in eid:
            lbl = "TUSD (jun/25)"
        elif "USDPUSDT-09" in eid:
            lbl = "USDP (Deriva 1, set/26)"
        elif "USDPUSDT-10" in eid:
            lbl = "USDP (Deriva 2, set/26)"
        else:
            lbl = f"{coin} ({dt})"
        labels.append(lbl)

    df = df.copy()
    df["display_label"] = labels

    # Invert order for top-to-bottom reading
    df_plot = df.iloc[::-1].reset_index(drop=True)
    y_pos = np.arange(len(df_plot))
    colors = [cat_colors[cid] for cid in df_plot["category_id"]]

    # Panel 1: Trough Price ($)
    troughs = df_plot["trough_usd"].values
    bars1 = ax1.barh(y_pos, troughs, color=colors, height=0.62, alpha=0.88, edgecolor="none")
    ax1.axvline(1.0, color=INK, linestyle="--", linewidth=1.1, label="Paridade (US$ 1,00)")
    ax1.axvline(0.995, color=ORANGE, linestyle=":", linewidth=0.9, alpha=0.8, label="Gatilho de descolamento (0,5%)")

    # Annotate trough values
    for idx, (y, val, rec) in enumerate(zip(y_pos, troughs, df_plot["recovery_status"])):
        txt = f"${val:.3f}" if val >= 0.3 else f"${val:.3f} (terminal)"
        ha = "left" if val < 0.9 else "right"
        col = INK if val < 0.9 else "#ffffff"
        x_coord = val + 0.015 if val < 0.9 else val - 0.015
        ax1.text(x_coord, y, txt, va="center", ha=ha, fontsize=8.2, fontweight="bold", color=col)

    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(df_plot["display_label"], fontsize=9)
    ax1.set_xlim(0.15, 1.05)
    ax1.set_xlabel("Preço mínimo atingido (US$)", fontsize=9.5, color=INK)
    ax1.set_title("A. Profundidade do Descolamento (Menor Preço)", fontsize=11, fontweight="bold", color=INK, pad=10)
    ax1.grid(axis="x", color=GRID, linestyle="-", linewidth=0.6, alpha=0.7)
    ax1.spines[["top", "right"]].set_visible(False)

    # Panel 2: Duration in Hours (log scale)
    durations = df_plot["duration_hours"].fillna(5000.0).values  # placeholder for censored
    is_censored = df_plot["recovery_status"] != "Recuperado"

    bars2 = ax2.barh(y_pos, durations, color=colors, height=0.62, alpha=0.88, edgecolor="none")

    # Hatches for censored
    for idx, (cens, bar) in enumerate(zip(is_censored, bars2)):
        if cens:
            bar.set_hatch("///")
            bar.set_edgecolor(INK)
            bar.set_linewidth(0.8)

    ax2.set_xscale("log")
    ax2.set_xlim(10, 8000)
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels([])  # Share Y-axis conceptually

    # Annotate durations
    for idx, (y, dur, cens) in enumerate(zip(y_pos, durations, is_censored)):
        if cens:
            txt = " Permanente (sem recuperação)" if "UST" in df_plot["coin"].iloc[idx] else " Deslistado / Censurado"
            ax2.text(dur, y, txt, va="center", ha="left", fontsize=8, color=RED, fontweight="bold")
        else:
            txt = f" {dur:.0f}h ({dur/24:.1f}d)"
            ax2.text(dur, y, txt, va="center", ha="left", fontsize=8.2, color=INK)

    ax2.set_xlabel("Duração até recuperação total (horas, escala log)", fontsize=9.5, color=INK)
    ax2.set_title("B. Tempo até Restabelecimento da Paridade", fontsize=11, fontweight="bold", color=INK, pad=10)
    ax2.grid(axis="x", color=GRID, linestyle="-", linewidth=0.6, alpha=0.7)
    ax2.spines[["top", "right"]].set_visible(False)

    # Custom legend for categories
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor=BLUE, label="1. Fim de semana bancário / canal fechado (USDC, USDP)"),
        Patch(facecolor=TEAL, label="2. Fricção temporária de resgate / livro fino (FDUSD, TUSD, UST)"),
        Patch(facecolor=RED, hatch="///", edgecolor=INK, label="3. Insolvência algorítmica terminal (UST mai/22)"),
        Patch(facecolor=GRAY, label="4. Fim dos dados na Binance (USDP set/26; deslistagem a verificar)"),
    ]
    fig.legend(handles=legend_elements, loc="lower center", bbox_to_anchor=(0.5, -0.06),
               ncol=2, frameon=False, fontsize=8.5)

    fig.text(0.01, -0.09,
             "Fonte: Binance spot 1h ajustado por Coinbase USDT/USD (P1-07/F-013); *USDC SVB medido diretamente na Bitstamp (P1-07 v2).\n"
             "Nota: O critério pré-comprometido (n >= 12 eventos) não foi atingido (n = 11), motivando análise comparativa em vez de curvas Kaplan-Meier.",
             fontsize=7.8, color=INK2)

    plt.tight_layout()
    cases_fig_path = FIG / "P3-04_depeg_cases.png"
    fig.savefig(cases_fig_path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(f"6. COMPARATIVE CASES FIGURE CREATED: {cases_fig_path}")


if __name__ == "__main__":
    main()
