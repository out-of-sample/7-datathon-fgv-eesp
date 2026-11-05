"""P5-09: the five charts of deck v3, redrawn in the deck's palette from frozen data and registered outputs.

Purpose  Same numbers as the core study, one consistent look (navy ink, blue = ordinary data, orange = the event).
Inputs   data/processed/P1-02_premium_daily.csv (premium, Binance, PTAX window)
         results/tables/P3-20_reference_values.csv (S20 at the 1,073 clean dates, Binance; frozen 30 Oct)
         results/tables/P3-12_rules.csv (change around each dated rule, ordinary-date band)
         data/raw/bcb/sgs_29644.json (stablecoin purchases abroad by residents, US$ mn; stored with a minus sign)
         results/tables/P3-11_placebo.csv, results/tables/P3-11_transfer.csv (money moved, 194 ordinary windows)
Outputs  results/figures/P5-09_{jump,placebo,rules,imports,money}.png
Run      .venv/bin/python scripts/p5_09_deck_figures.py
         Labels use IBM Plex Sans if PLEX_DIR points to its .ttf files (the deck's face), else the default sans.
Sizes    figsize in inches = the size on the 1920x1080 slide / 100, dpi 200 (2x); font pt = slide px * 0.72.
"""

import json
import os
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parent.parent
FIG, TAB, PROC, RAW = ROOT / "results/figures", ROOT / "results/tables", ROOT / "data/processed", ROOT / "data/raw"
BG, INK, MUTED, GRID = "#F6F4EF", "#14213D", "#5B6573", "#DDD7CC"
BLUE, ORANGE, BAND = "#3B6EA8", "#D9622B", "#E7E2D8"
PX = 0.72  # font points per slide pixel

if os.environ.get("PLEX_DIR"):
    for f in Path(os.environ["PLEX_DIR"]).glob("IBMPlexSans-*.ttf"):
        font_manager.fontManager.addfont(str(f))
    plt.rcParams["font.family"] = "IBM Plex Sans"
plt.rcParams.update({"font.size": 24 * PX, "text.color": INK, "axes.labelcolor": MUTED, "xtick.color": MUTED,
                     "ytick.color": MUTED, "axes.edgecolor": GRID, "figure.facecolor": BG, "axes.facecolor": BG,
                     "savefig.facecolor": BG, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.spines.left": False})


def fig(w, h):
    return plt.subplots(figsize=(w / 100, h / 100), dpi=200)


def save(f, name):
    f.savefig(FIG / f"P5-09_{name}.png", dpi=200)
    plt.close(f)
    print("wrote", f"results/figures/P5-09_{name}.png")


def br(x, d=1):
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


# 1. The jump: weekly mean premium, Jul 2025 - Oct 2026, with the 20-day means before and after 23 Jun.
p = pd.read_csv(PROC / "P1-02_premium_daily.csv", parse_dates=["date_brt"]).set_index("date_brt")["premium_bps"]
t0 = pd.Timestamp("2026-06-23")
pre, post = p[p.index < t0].iloc[-20:], p[p.index > t0].iloc[:20]
assert round(pre.mean(), 1) == 15.2 and round(post.mean(), 1) == 109.1, (pre.mean(), post.mean())
w = p["2025-07-01":].resample("W-FRI").mean().dropna()
f, ax = fig(1100, 560)
ax.plot(w.index, w.values, color=BLUE, lw=2.6)
hot = w[(w.index >= pre.index[-1]) & (w.index <= post.index[-1] + pd.Timedelta(days=7))]
ax.plot(hot.index, hot.values, color=ORANGE, lw=3.6)
ax.axvspan(post.index[0], post.index[-1], color=ORANGE, alpha=0.10, lw=0)
ax.axvline(t0, color=INK, lw=1.4, ls=(0, (3, 3)))
ax.hlines(pre.mean(), pre.index[0], pre.index[-1], color=INK, lw=2.4, ls=(0, (4, 2)))
ax.hlines(post.mean(), post.index[0], post.index[-1], color=ORANGE, lw=2.4, ls=(0, (4, 2)))
ax.text(t0 - pd.Timedelta(days=4), 152, "23/jun: ofício do BCB", ha="right", va="top", fontsize=24 * PX, weight="semibold")
ax.text(pre.index[0] - pd.Timedelta(days=6), pre.mean() + 6, f"20 dias antes: {br(pre.mean())} bps", ha="right",
        va="bottom", fontsize=24 * PX, weight="semibold")
ax.text(post.index[-1] + pd.Timedelta(days=8), post.mean(), f"20 dias depois:\n{br(post.mean())} bps", ha="left",
        va="center", fontsize=24 * PX, weight="semibold", color=ORANGE)
ax.set_ylim(-12, 158)
ax.set_yticks([0, 50, 100, 150], ["0", "50", "100", "150 bps"])
ticks = pd.to_datetime(["2025-07-01", "2025-10-01", "2026-01-01", "2026-04-01", "2026-07-01", "2026-10-01"])
ax.set_xticks(ticks, ["jul/25", "out/25", "jan/26", "abr/26", "jul/26", "out/26"])
ax.grid(axis="y", color=GRID, lw=1)
ax.tick_params(length=0)
ax.axhline(0, color=MUTED, lw=1)
f.tight_layout(pad=0.4)
save(f, "jump")

# 2. Placebo: the same 20-day change at the 1,073 clean dates (Binance, frozen 30 Oct) vs the June change.
r = pd.read_csv(TAB / "P3-20_reference_values.csv")
s20 = r[(r.series == "Binance") & (r.statistic == "S20")].value_bps
assert len(s20) == 1073 and round(s20.max(), 1) == 65.7
jump = post.mean() - pre.mean()
f, ax = fig(560, 560)
ax.hist(s20, bins=np.arange(-60, 75, 10), color=BLUE, edgecolor=BG, lw=2)
ax.vlines(jump, 0, 300, color=ORANGE, lw=4)
ax.plot(jump, 300, "o", color=ORANGE, ms=13)
ax.text(jump, 318, f"+{br(jump)}", ha="center", va="bottom", fontsize=32 * PX, weight="bold", color=ORANGE)
ax.text(s20.max() + 2, 40, f"maior data\ncomum:\n+{br(s20.max())}", ha="center", va="bottom", fontsize=22 * PX)
ax.text(-58, 300, "1.073 datas\ncomuns", ha="left", va="top", fontsize=24 * PX, weight="semibold", color=BLUE)
ax.set_ylim(0, 370)
ax.set_yticks([])
ax.set_xticks([-50, 0, 50, 100], ["−50", "0", "+50", "+100"])
ax.tick_params(length=0)
ax.axhline(0, color=MUTED, lw=1)
f.tight_layout(pad=0.4)
save(f, "placebo")

# 3. Rules: change around each dated rule (announcement ring, effective dot) vs the ordinary-date band.
t = pd.read_csv(TAB / "P3-12_rules.csv")
lo, hi = t.band_low_bps.iloc[0], t.band_high_bps.iloc[0]
names = {"E-05": "Ofício do BCB · não publicado, imediato", "E-01": "Decreto do IOF 3,5% · 1 dia de aviso",
         "E-01b": "Congresso e STF suspendem · 7 dias", "E-02": "Res. 519–521, ativos virtuais · 84 dias",
         "E-06b": "Res. 584, retenção de 24 h · 147 dias", "E-06a": "Res. 561, stablecoins no eFX · 154 dias",
         "E-04": "Res. 521, reporte ao BCB · 175 dias", "E-03": "Proposta de IOF sobre cripto · não vigorou"}
order = ["E-05", "E-01", "E-01b", "E-02", "E-06b", "E-06a", "E-04", "E-03"]
t = t.set_index("event_id").loc[order]
f, ax = fig(1120, 560)
ax.axvspan(lo, hi, color=BAND, lw=0)
ax.axvline(0, color=MUTED, lw=1)
for i, (k, row) in enumerate(t.iterrows()):
    y = len(order) - 1 - i
    c = ORANGE if k == "E-05" else BLUE
    if pd.notna(row.change_announcement_bps):
        ax.plot(row.change_announcement_bps, y, "o", mfc=BG, mec=c, mew=3, ms=15)
    if pd.notna(row.change_effective_bps):
        ax.plot(row.change_effective_bps, y, "o", color=c, ms=15)
    ax.text(lo - 4, y, names[k], ha="right", va="center", fontsize=24 * PX, color=ORANGE if k == "E-05" else INK,
            weight="semibold" if k == "E-05" else "normal")
e = t.loc["E-05", "change_effective_bps"]
ax.text(e - 4, len(order) - 1 + 0.42, f"+{br(e)}", ha="center", va="bottom", fontsize=26 * PX, weight="bold", color=ORANGE)
ax.text((lo + hi) / 2, len(order) - 1, "95% das\ndatas comuns", ha="center", va="center", fontsize=22 * PX, color=MUTED,
        bbox=dict(fc=BAND, ec="none", pad=2), zorder=3)
ax.set_ylim(-0.7, len(order) - 0.2)
ax.set_xlim(lo - 4, 108)
ax.set_yticks([])
ax.set_xticks([-25, 0, 25, 50, 75, 100], ["−25", "0", "+25", "+50", "+75", "+100 bps"])
ax.tick_params(length=0)
ax.spines["bottom"].set_visible(False)
f.subplots_adjust(left=0.43, right=0.98, top=0.97, bottom=0.08)
save(f, "rules")

# 4. Mechanism: stablecoin purchases abroad (BCB SGS 29644) and the monthly mean premium, Jan 2025 - Sep 2026.
s = pd.DataFrame(json.loads((RAW / "bcb/sgs_29644.json").read_text()))
s = pd.Series(-s.valor.astype(float).values, index=pd.to_datetime(s.data, dayfirst=True))["2025-01-01":"2026-09-01"]
m = p.resample("MS").mean()["2025-01-01":"2026-09-01"]
assert round(-100 * (1 - s["2026-07-01"] / s["2026-06-01"])) == -78
f, (a1, a2) = plt.subplots(2, 1, figsize=(11.2, 5.6), dpi=200, gridspec_kw={"height_ratios": [1.15, 1], "hspace": 0.55})
after = s.index >= "2026-07-01"
for ax, ser, title in [(a1, s, "Compras de stablecoins no exterior por residentes, US$ milhões por mês (BCB)"),
                       (a2, m, "Prêmio médio do mês, em bps")]:
    ax.bar(ser.index, ser.values, width=22, color=np.where(after, ORANGE, BLUE))
    ax.set_yticks([])
    ax.tick_params(length=0)
    ax.set_title(title, loc="left", fontsize=24 * PX, weight="semibold", color=INK, pad=10)
    ax.set_xticks([])
for d, ax, ser in [("2026-06-01", a1, s), ("2026-07-01", a1, s), ("2026-06-01", a2, m), ("2026-07-01", a2, m)]:
    v = ser[d]
    ax.text(pd.Timestamp(d), v + ser.max() * 0.04, br(v, 0), ha="center", va="bottom", fontsize=24 * PX, weight="bold",
            color=ORANGE if d >= "2026-07" else INK)
a1.set_ylim(0, s.max() * 1.22)
a2.set_ylim(0, m.max() * 1.3)
a2.set_xticks(pd.to_datetime(["2025-01-01", "2025-07-01", "2026-01-01", "2026-07-01"]),
              ["jan/25", "jul/25", "jan/26", "jul/26"])
f.subplots_adjust(left=0.01, right=0.99, top=0.92, bottom=0.08)
save(f, "imports")

# 5. Money: transfer from buyers to sellers in the 4 weeks after the notice vs 194 ordinary 4-week windows (Binance).
pl = pd.read_csv(TAB / "P3-11_placebo.csv").transfer_brl_mn
tr = pd.read_csv(TAB / "P3-11_transfer.csv")
head = tr[(tr.venue == "Binance") & tr.variant.str.startswith("headline")].transfer_brl_mn.iloc[0]
assert len(pl) == 194 and round(head, 1) == 106.1 and round(pl.max(), 1) == 35.5
f, ax = fig(860, 440)
ax.hist(pl, bins=np.arange(-20, 40, 5), color=BLUE, edgecolor=BG, lw=2)
ax.vlines(head, 0, 70, color=ORANGE, lw=4)
ax.plot(head, 70, "o", color=ORANGE, ms=13)
ax.text(head, 76, f"R$ {br(head, 0)} mi", ha="center", va="bottom", fontsize=32 * PX, weight="bold", color=ORANGE)
ax.text(-18, 92, "194 janelas comuns\nde quatro semanas", ha="left", va="top", fontsize=24 * PX, weight="semibold", color=BLUE)
ax.text(pl.max() + 1, 12, f"maior: R$ {br(pl.max())} mi", ha="left", va="bottom", fontsize=22 * PX)
ax.set_ylim(0, 100)
ax.set_xlim(-22, 118)
ax.set_yticks([])
ax.set_xticks([0, 50, 100], ["0", "+50", "+100 R$ mi"])
ax.tick_params(length=0)
ax.axhline(0, color=MUTED, lw=1)
f.tight_layout(pad=0.4)
save(f, "money")
