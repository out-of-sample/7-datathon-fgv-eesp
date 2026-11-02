r"""P3-12: which rules moved the premium? One row per dated Brazilian rule (E-01 to E-06b): how it was issued, how much
notice the market had, and its before/after change from P2-03 against the range of ordinary dates. No new estimation.

Issuance  how each rule reached the market, with its source row in docs/sources.md (dict ISSUED below).
Notice    calendar days from announcement to entry into force (data/processed/P1-04_events_brazil.csv).
Change    P2-03 diff_bps (mean premium 20 PTAX days after minus 20 before), at announcement and at entry into force;
          p = p_placebo_all_clean_2s (all 1,073 clean dates).
Band      2.5-97.5% of the 200 P2-03 placebo draws: what an ordinary date shows; a change inside it is not detectable.
Scope     rules only; market events (E-07, M-01 to M-04) are left out. E-04 was announced with E-02 (same resolution,
          10 Nov 2025), so only its entry into force is plotted.
Inputs    results/tables/P2-03_event_table.csv, results/tables/P2-03_placebo_draws.csv, data/processed/P1-04_events_brazil.csv
Outputs   results/tables/P3-12_rules.csv, results/figures/P3-12_rules.png (pt-BR, for the slide)
Run       python scripts/p3_12_rules.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
TAB, FIG, PROC = ROOT / "results/tables", ROOT / "results/figures", ROOT / "data/processed"

# event id: (label pt-BR, instrument, published?, source row in docs/sources.md)
ISSUED = {
    "E-01": ("Decreto do IOF-Câmbio (3,5%)", "decreto presidencial", True, "E-01"),
    "E-01b": ("Congresso e STF suspendem o decreto do IOF", "decreto legislativo e liminar do STF", True, "E-01b"),
    "E-02": ("Res. BCB 519–521: marco dos ativos virtuais", "resolução do BCB", True, "E-02"),
    "E-03": ("Proposta de IOF sobre compra de cripto", "proposta da Fazenda, não editada", True, "E-03"),
    "E-04": ("Res. BCB 521, art. 4º: reporte ao BCB", "resolução do BCB", True, "E-04"),
    "E-05": ("Ofício do BCB: câmbio de fundos para importar cripto", "ofício de supervisão sigiloso", False, "E-05.1, E-05.2"),
    "E-06a": ("Res. BCB 561: stablecoins fora do eFX", "resolução do BCB", True, "E-06a"),
    "E-06b": ("Res. BCB 584: retenção de até 24 h", "resolução do BCB", True, "E-06b"),
}

ev = pd.read_csv(TAB / "P2-03_event_table.csv")
ev = ev[ev.event_id.isin(ISSUED) & (ev.status == "evaluated")]
ev = ev[~((ev.event_id == "E-04") & (ev.eval_date_kind == "announcement"))]
dates = pd.read_csv(PROC / "P1-04_events_brazil.csv", parse_dates=["date_announced", "date_effective"]).set_index("event_id")
band = pd.read_csv(TAB / "P2-03_placebo_draws.csv").placebo_diff_bps.quantile([0.025, 0.975]).values

rows = []
for eid, (label, instrument, published, src) in ISSUED.items():
    a, e = dates.loc[eid, "date_announced"], dates.loc[eid, "date_effective"]
    get = lambda kind: ev[(ev.event_id == eid) & (ev.eval_date_kind == kind)]
    ann, eff = get("announcement"), get("effective")
    rows.append({"event_id": eid, "label": label, "instrument": instrument, "published": published,
                 "announced": a.date(), "effective": None if pd.isna(e) else e.date(),
                 "notice_days": None if pd.isna(e) else (e - a).days,
                 "change_announcement_bps": ann.diff_bps.iloc[0] if len(ann) else None,
                 "p_announcement": ann.p_placebo_all_clean_2s.iloc[0] if len(ann) else None,
                 "change_effective_bps": eff.diff_bps.iloc[0] if len(eff) else None,
                 "p_effective": eff.p_placebo_all_clean_2s.iloc[0] if len(eff) else None, "source": src})
t = pd.DataFrame(rows).sort_values("announced", kind="stable").reset_index(drop=True)
t["band_low_bps"], t["band_high_bps"] = band
TAB.mkdir(parents=True, exist_ok=True)
t.to_csv(TAB / "P3-12_rules.csv", index=False, float_format="%.4f")
print(f"ordinary-date band (2.5-97.5% of 200 placebo draws): {band[0]:.1f} to {band[1]:.1f} bps")
print(t.drop(columns=["label", "band_low_bps", "band_high_bps"]).round(3).to_string(index=False))

# Figure: one row per rule, change in bps at announcement (hollow) and entry into force (filled)
BLUE, ORANGE, INK, INK2, MUTED, GRID, SURFACE = "#2a78d6", "#eb6834", "#1f1e1c", "#52514e", "#b9b8b2", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "axes.edgecolor": GRID, "axes.labelcolor": INK2,
                     "xtick.color": INK2, "ytick.color": INK2, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "axes.axisbelow": True, "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
                     "font.size": 10, "axes.titlesize": 12, "axes.titleweight": "bold", "axes.titlelocation": "left",
                     "legend.frameon": False, "savefig.dpi": 200, "savefig.bbox": "tight"})
fig, ax = plt.subplots(figsize=(11, 5.2))
ax.axvspan(*band, color=MUTED, alpha=0.25, linewidth=0, label="faixa de 95% das datas comuns (placebo)")
ax.axvline(0, color=INK2, lw=0.8)
y = range(len(t))[::-1]
for yi, r in zip(y, t.itertuples()):
    c = ORANGE if r.event_id == "E-05" else BLUE
    if pd.notna(r.change_announcement_bps):
        ax.scatter(r.change_announcement_bps, yi, s=70, facecolor=SURFACE, edgecolor=c, linewidth=2, zorder=3)
    if pd.notna(r.change_effective_bps):
        ax.scatter(r.change_effective_bps, yi, s=70, color=c, edgecolor=SURFACE, linewidth=1.5, zorder=4)
    notice = ("efeito imediato" if r.notice_days == 0 else f"{r.notice_days:.0f} dia{'' if r.notice_days == 1 else 's'} até vigorar" if pd.notna(r.notice_days)
              else "sem vigência")
    if r.event_id == "E-06b":
        notice += " (após o fim da amostra)"
    ax.text(-62, yi + 0.12, r.label, ha="right", va="center", fontsize=9.5, color=INK, fontweight="bold" if r.event_id == "E-05" else None)
    ax.text(-62, yi - 0.22, f"{r.instrument}; {r.announced:%d/%m/%Y}; {notice}", ha="right", va="center", fontsize=8, color=INK2)
e5 = t[t.event_id == "E-05"].iloc[0]
ax.annotate(f"+{e5.change_effective_bps:.0f} pb\n(nenhuma data comum chega perto: p ≈ 0,001)", (e5.change_effective_bps, y[e5.name]),
            xytext=(-10, 0), textcoords="offset points", ha="right", va="center", fontsize=9, color=INK)
ax.scatter([], [], s=70, facecolor=SURFACE, edgecolor=INK2, linewidth=2, label="no anúncio")
ax.scatter([], [], s=70, color=INK2, label="na entrada em vigor")
ax.set_xlim(-60, 110)
ax.set_yticks([])
ax.set_ylim(-0.7, len(t) - 0.4)
ax.set_xlabel("variação do prêmio do USDT sobre a PTAX: 20 dias úteis depois menos 20 antes (pontos-base)")
ax.set_title("Só o ofício sigiloso moveu o prêmio de forma detectável; as regras publicadas ficaram na faixa das datas comuns", x=-0.62)
ax.legend(loc="upper right", fontsize=8.5)
fig.text(-0.36, -0.06, "Fonte: P2-03 (estudo de eventos com datas placebo); fontes de cada regra em docs/sources.md. Uma variação dentro "
         "da faixa cinza não seria detectável: \"sem efeito\" quer dizer \"sem efeito acima de ~35 pb\". As regras também diferem\n"
         "no conteúdo, então o gráfico não separa o efeito de ser sigiloso do efeito do que a regra fechou.", fontsize=8, color=INK2)
FIG.mkdir(parents=True, exist_ok=True)
fig.savefig(FIG / "P3-12_rules.png")
