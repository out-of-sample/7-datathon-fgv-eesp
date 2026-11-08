"""P5-10: the new charts of deck v4, in deck v3's palette, from frozen data and registered outputs.

Purpose  Slide 6 (on-chain route), slide 7 (price vs market, three panels) and slide 9 (cost budget for waiting).
Inputs   data/processed/P1-02_premium_daily.csv (Binance premium, PTAX window; core study)
         data/processed/P3-24_brla_daily.csv (Pix -> BRLA -> USDC route on Polygon, PTAX window; F-037)
         data/raw/bcb/sgs_29644.json (stablecoin purchases abroad by residents, US$ mn, stored negative; F-024)
         results/tables/P3-25_composition.csv (Foxbit share of three-exchange volume by period; F-036)
         results/tables/P3-38_june_ceiling.csv (waiting's cost budget, central and 216-scenario range; F-048)
Outputs  results/figures/P5-10_{brla,rec_price,rec_imports,rec_share,wait}.png
Run      .venv/bin/python scripts/p5_10_deck_figures.py
         Labels use IBM Plex Sans if PLEX_DIR points to its .ttf files (the deck's face), else the default sans.
Sizes    figsize in inches = the size on the 1920x1080 slide / 100, dpi 200 (2x); font pt = slide px * 0.72.
"""

import json
import os
from pathlib import Path

import matplotlib
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parent.parent
FIG, TAB, PROC, RAW = ROOT / "results/figures", ROOT / "results/tables", ROOT / "data/processed", ROOT / "data/raw"
BG, INK, MUTED, GRID = "#F6F4EF", "#14213D", "#5B6573", "#DDD7CC"
BLUE, ORANGE, BAND = "#3B6EA8", "#D9622B", "#E7E2D8"
PX = 0.72  # font points per slide pixel
T0 = pd.Timestamp("2026-06-23")

if os.environ.get("PLEX_DIR"):
    for f in Path(os.environ["PLEX_DIR"]).glob("*.ttf"):
        font_manager.fontManager.addfont(str(f))
    plt.rcParams["font.family"] = "IBM Plex Sans"
plt.rcParams.update({"font.size": 24 * PX, "text.color": INK, "axes.labelcolor": MUTED, "xtick.color": MUTED,
                     "ytick.color": MUTED, "axes.edgecolor": GRID, "figure.facecolor": BG, "axes.facecolor": BG,
                     "savefig.facecolor": BG, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.spines.left": False})


def fig(w, h):
    return plt.subplots(figsize=(w / 100, h / 100), dpi=200)


def save(f, name):
    f.tight_layout(pad=0.4)
    f.savefig(FIG / f"P5-10_{name}.png", dpi=200)
    plt.close(f)
    print("wrote", f"results/figures/P5-10_{name}.png")


def br(x, d=1):
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


MONTHS = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out"]
p = pd.read_csv(PROC / "P1-02_premium_daily.csv", parse_dates=["date_brt"]).set_index("date_brt")["premium_bps"]

# 1. Slide 6: the on-chain route (Pix -> BRLA -> USDC) against USDT on Binance, same PTAX windows (F-037).
b = pd.read_csv(PROC / "P3-24_brla_daily.csv", parse_dates=["date_brt"]).set_index("date_brt")
pre_days, post_days = p[p.index < T0].index[-20:], p[p.index > T0].index[:20]
brla_pre, brla_post = b.loc[b.index.isin(pre_days), "brla_bps"].mean(), b.loc[b.index.isin(post_days), "brla_bps"].mean()
assert abs(brla_post - brla_pre - 111.0) < 0.6, (brla_pre, brla_post)
s = b.loc["2026-05-04":"2026-08-31", ["brla_bps", "binance_bps"]].dropna()
f, ax = fig(840, 330)
ax.axvspan(post_days[0], post_days[-1], color=ORANGE, alpha=0.10, lw=0)
ax.axvline(T0, color=INK, lw=1.4, ls=(0, (3, 3)))
ax.plot(s.index, s.binance_bps, color=BLUE, lw=2.4)
ax.plot(s.index, s.brla_bps, color=ORANGE, lw=2.4)
ax.text(s.index[3], 235, "Rota on-chain (BRLA)", color=ORANGE, fontsize=24 * PX, weight="semibold", va="top")
ax.text(s.index[3], 205, "USDT na Binance", color=BLUE, fontsize=24 * PX, weight="semibold", va="top")
ax.text(post_days[-1] + pd.Timedelta(days=3), 230, f"+{br(brla_post - brla_pre)} bps on-chain\n+93,9 bps Binance",
        fontsize=24 * PX, weight="semibold", va="top", color=INK)
ax.set_ylim(-40, 245)
ax.set_yticks([0, 100, 200], ["0", "100", "200 bps"])
ax.set_xticks(pd.to_datetime(["2026-05-01", "2026-06-01", "2026-07-01", "2026-08-01"]), ["mai", "jun", "jul", "ago"])
ax.grid(axis="y", color=GRID, lw=1)
save(f, "brla")

# 2a. Slide 7, panel 1: the price came back (weekly mean premium, Binance, 2026).
# ends 29 Oct: the Binance-only dip of 30 Oct is the 29 Oct security incident (F-045), not a market move
w = p["2026-01-01":"2026-10-29"].resample("W-FRI").mean().dropna()
hot = w[(w.index >= T0) & (w.index <= post_days[-1] + pd.Timedelta(days=7))]
f, ax = fig(528, 270)
ax.axvspan(post_days[0], post_days[-1], color=ORANGE, alpha=0.12, lw=0)
ax.plot(w.index, w.values, color=BLUE, lw=2.4)
ax.plot(hot.index, hot.values, color=ORANGE, lw=3.2)
ax.set_ylim(-10, 170)
ax.set_yticks([0, 50, 100, 150], ["0", "50", "100", "150 bps"])
ax.set_xticks(pd.to_datetime([f"2026-{m:02d}-01" for m in (1, 4, 7, 10)]), ["jan", "abr", "jul", "out"])
ax.grid(axis="y", color=GRID, lw=1)
save(f, "rec_price")

# 2b. Panel 2: purchases abroad did not come back (BCB, monthly, US$ bn).
raw = pd.DataFrame(json.loads((RAW / "bcb/sgs_29644.json").read_text()))
m = pd.Series(-raw.valor.astype(float).values / 1000, index=pd.to_datetime(raw.data, dayfirst=True))["2026-01":"2026-09"]
assert round(1 - m["2026-07"].iloc[0] / m["2026-06"].iloc[0], 2) == 0.78
f, ax = fig(528, 270)
colors = [ORANGE if d >= pd.Timestamp("2026-07-01") else BLUE for d in m.index]
ax.bar(range(len(m)), m.values, color=colors, width=0.7)
for i, v in enumerate(m.values):
    ax.text(i, v + 0.06, br(v), ha="center", va="bottom", fontsize=20 * PX, color=MUTED)
ax.set_xticks(range(len(m)), MONTHS[: len(m)])
ax.set_ylim(0, 3.3)
ax.set_yticks([0, 1, 2, 3], ["0", "1", "2", "US$ 3 bi"])
ax.grid(axis="y", color=GRID, lw=1)
save(f, "rec_imports")

# 2c. Panel 3: the market changed (Foxbit share of USDT volume on the three exchanges, business hours, by period).
c = pd.read_csv(TAB / "P3-25_composition.csv").set_index("period")["foxbit_share_pct"]
assert [round(c[k], 2) for k in ("pre", "wave", "after")] == [6.80, 27.99, 34.74]
f, ax = fig(528, 270)
labels = ["antes\n(mai–jun)", "pico\n(jun–jul)", "depois\n(jul–out)"]
ax.bar(range(3), c[["pre", "wave", "after"]].values, color=[BLUE, ORANGE, ORANGE], width=0.6)
for i, v in enumerate(c[["pre", "wave", "after"]].values):
    ax.text(i, v + 1, br(v) + "%", ha="center", va="bottom", fontsize=24 * PX, weight="semibold")
ax.set_xticks(range(3), labels)
ax.set_ylim(0, 44)
ax.set_yticks([0, 20, 40], ["0", "20", "40%"])
ax.grid(axis="y", color=GRID, lw=1)
save(f, "rec_share")

# 3. Slide 9: waiting's cost budget at 5/10/20 PTAX days, central scenario and the 216-scenario stress range (F-048).
j = pd.read_csv(TAB / "P3-38_june_ceiling.csv").set_index("horizon_ptax_days")
assert [round(j.loc[h, "max_additional_cost_bps"], 1) for h in (5, 10, 20)] == [90.1, 92.9, 165.5]
f, ax = fig(760, 230)
ax.axvspan(-60, 0, color=BAND, lw=0)
ax.axvline(0, color=INK, lw=1.4)
for i, h in enumerate((20, 10, 5)):
    lo, mid, hi = j.loc[h, ["stress_min_ceiling_bps", "max_additional_cost_bps", "stress_max_ceiling_bps"]]
    ax.hlines(i, lo, hi, color=ORANGE, lw=7, alpha=0.35)
    ax.plot(mid, i, "o", color=ORANGE, ms=11)
    ax.text(hi + 6, i, f"central +{br(mid, 0)} bps · faixa {br(lo, 0).replace('-', '−')} a +{br(hi, 0)}", va="center", fontsize=20 * PX)
ax.set_yticks(range(3), ["20 dias", "10 dias", "5 dias"])
ax.set_xlim(-60, 420)
ax.set_ylim(-0.6, 2.6)
ax.set_xticks([0, 100, 200], ["0", "+100", "+200 bps"])
ax.tick_params(axis="y", length=0)
ax.grid(axis="x", color=GRID, lw=1)
save(f, "wait")
