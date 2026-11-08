"""P5-10: the new charts of deck v4, in deck v3's palette, from frozen data and registered outputs.

Purpose  Slide 2 (the anomaly that started the story), slide 6 (on-chain route), slide 7 (price vs market, three panels) and slide 9 (cost budget for waiting).
Inputs   data/processed/P1-05_donor_premiums_daily.csv (USDT premiums of the 5 comparison currencies; F-010)
         results/tables/P2-04_synth_weights.csv (synthetic-control weights, headline spec; F-017)
         data/processed/P1-02_premium_daily.csv (Binance premium, PTAX window; core study)
         data/processed/P3-24_brla_daily.csv (Pix -> BRLA -> USDC route on Polygon, PTAX window; F-037)
         data/raw/bcb/sgs_29644.json (stablecoin purchases abroad by residents, US$ mn, stored negative; F-024)
         results/tables/P3-25_composition.csv (Foxbit share of three-exchange volume by period; F-036)
         results/tables/P3-38_june_ceiling.csv (waiting's cost budget, central and 216-scenario range; F-048)
Outputs  results/figures/P5-10_{synth,anomaly,brla,rec_price,rec_imports,rec_share,wait}.png
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

# 4. Slide 2: the anomaly. Binance premium, 5-day trailing mean, Jan 2025 to 29 Oct 2026 (30 Oct = Binance incident, F-045).
#    The mean keeps one-day outliers (e.g. one day in early 2025) from looking like the month-long June shift.
pre_mean, post_mean = p.loc["2025-07-08":"2026-06-23"].mean(), p.loc["2026-06-24":"2026-07-21"].mean()
assert (round(pre_mean, 1), round(p.loc["2026-06-24"], 1), round(post_mean, 1)) == (9.3, 155.4, 109.1)
d = p.rolling(5).mean().loc["2025-01-01":"2026-10-29"]
f, ax = fig(600, 300)
ax.axvspan(pd.Timestamp("2026-06-24"), pd.Timestamp("2026-07-21"), color=ORANGE, alpha=0.14, lw=0)
ax.axhline(0, color=GRID, lw=1)
ax.plot(d.index, d.values, color=BLUE, lw=1.4)
spike = d.loc["2026-06-24":"2026-07-21"]
ax.plot(spike.index, spike.values, color=ORANGE, lw=1.8)
ax.annotate("24/jun", xy=(pd.Timestamp("2026-06-26"), d.loc["2026-06-26"]), xytext=(pd.Timestamp("2025-12-01"), 150),
            fontsize=22 * PX, weight="semibold", color=ORANGE, va="center",
            arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.4))
ax.set_ylim(-10, 160)
ax.set_yticks([0, 50, 100, 150], ["0", "50", "100", "150 bps"])
ticks = [pd.Timestamp(x) for x in ("2025-01-01", "2025-07-01", "2026-01-01", "2026-07-01")]
ax.set_xticks(ticks, ["jan/25", "jul/25", "jan/26", "jul/26"])
ax.set_xlim(pd.Timestamp("2025-01-01"), pd.Timestamp("2026-10-31"))
ax.grid(axis="y", color=GRID, lw=1)
ax.tick_params(length=0)
save(f, "anomaly")

# 5. Slide 5: Brazil vs synthetic Brazil (headline 5-donor weights, F-017), common trading days, 5-day trailing mean.
dp = pd.read_csv(PROC / "P1-05_donor_premiums_daily.csv", parse_dates=["date"], index_col="date")
wt = pd.read_csv(TAB / "P2-04_synth_weights.csv").query("spec == '5-donor (Headline)' and unit == 'BRL_ptax'")
donors = ["EUR", "TRY", "ZAR", "MXN", "COP"]
dd = dp[["BRL_ptax"] + donors].dropna()
synth = sum(dd[c] * float(wt[c].iloc[0]) for c in donors)
gap = dd.BRL_ptax - synth
assert round(gap.loc["2026-06-24":"2026-07-21"].mean(), 1) == 109.3, gap.loc["2026-06-24":"2026-07-21"].mean()
assert round(float(((gap.loc["2025-11-01":"2026-06-22"]) ** 2).mean() ** 0.5), 0) == 7
br5, sy5 = dd.BRL_ptax.rolling(5).mean().loc["2025-11-01":"2026-09-30"], synth.rolling(5).mean().loc["2025-11-01":"2026-09-30"]
f, ax = fig(560, 280)
ax.axvspan(pd.Timestamp("2026-06-24"), pd.Timestamp("2026-07-21"), color=ORANGE, alpha=0.14, lw=0)
ax.axvline(T0, color=INK, lw=1.2, ls=(0, (3, 3)))
ax.plot(sy5.index, sy5.values, color=MUTED, lw=2.2)
ax.plot(br5.index, br5.values, color=ORANGE, lw=2.4)
ax.text(pd.Timestamp("2025-11-10"), 42, "Brasil", color=ORANGE, fontsize=22 * PX, weight="semibold")
ax.text(pd.Timestamp("2026-01-20"), -32, "Brasil sintético", color=MUTED, fontsize=22 * PX, weight="semibold")
ax.set_ylim(-40, 160)
ax.set_yticks([0, 50, 100, 150], ["0", "50", "100", "150 bps"])
ticks = [pd.Timestamp(x) for x in ("2025-11-01", "2026-02-01", "2026-05-01", "2026-08-01")]
ax.set_xticks(ticks, ["nov/25", "fev/26", "mai/26", "ago/26"])
ax.grid(axis="y", color=GRID, lw=1)
ax.tick_params(length=0)
save(f, "synth")

# 6. Slide 9: value of waiting 10 PTAX days with a hedge, hedged buyer, by decision date in 2026 (F-055, P3-48).
wd = pd.read_csv(TAB / "P3-48_waiting_daily_h10.csv", parse_dates=["decision_date"], index_col="decision_date").buyer_w_brl / 1e3
assert round(wd.min(), 1) == -8.8 and round(wd.max(), 1) == 6.7, (wd.min(), wd.max())
f, ax = fig(1000, 300)
ax.axvspan(pd.Timestamp("2026-06-24"), pd.Timestamp("2026-07-21"), color=ORANGE, alpha=0.12, lw=0)
ax.bar(wd.index, wd.values, width=1.6, color=[ORANGE if v > 0 else BLUE for v in wd.values])
ax.axhline(0, color=INK, lw=1)
ax.text(pd.Timestamp("2026-06-25"), 7.6, "decisões no choque", color=ORANGE, fontsize=20 * PX, weight="semibold", va="bottom")
ax.text(pd.Timestamp("2026-01-05"), 5.2, "laranja: esperar foi melhor · azul: comprar já foi melhor", color=MUTED, fontsize=20 * PX)
ax.set_ylim(-10, 9.5)
ax.set_yticks([-8, -4, 0, 4, 8], ["−8", "−4", "0", "+4", "+8 mil"])
ticks = [pd.Timestamp(f"2026-{m:02d}-01") for m in range(1, 11)]
ax.set_xticks(ticks, MONTHS)
ax.grid(axis="y", color=GRID, lw=1)
ax.tick_params(length=0)
save(f, "waiting")

# 7. Slide 4 (methods): vertical row labels as images (the slide editor drops CSS writing-mode).
for name, text in (("label_mecanismo", "MECANISMO"), ("label_consequencias", "CONSEQUÊNCIAS")):
    f = plt.figure(figsize=(40 / 100, 166 / 100), dpi=200)
    f.text(0.5, 0.5, " ".join(text), rotation=90, ha="center", va="center", fontsize=13 * PX, weight="semibold", color="#3D4A5C")
    f.savefig(FIG / f"P5-10_{name}.png", dpi=200, transparent=True)
    plt.close(f)
    print("wrote", f"results/figures/P5-10_{name}.png")
