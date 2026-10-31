r"""P2-02: blind structural-break test on the daily USDT/BRL premium. The algorithm gets no event dates; matching breaks
to events (S3) happens afterwards. Specification fixed before the first run: tasks/P2-02-blind-break-test.md.

Model    pure mean shift (Bai-Perron, constant only), least squares by dynamic programming (ruptures.Dynp, cost l2,
         exact optimum per number of breaks), minimum segment 20 PTAX days, 0-8 breaks.
Count    BIC  ln(SSR_m/T) + p ln(T)/T,  p = 2m+1;  LWZ  ln(SSR_m/(T-p)) + (p 0.299/T) (ln T)^2.1.
         Headline = BIC, unless BIC picks the maximum (8): then LWZ (pre-committed; BIC over-selects with serial correlation).
CI       Bai (1997): break +/- 11.03 w2/d2 PTAX days (95%), d = change in mean, w2 = Newey-West long-run variance of the
         residuals (Bartlett kernel, lag floor(4 (T/100)^(2/9))).
Inputs   data/processed/P1-02_premium_daily.csv (scripts/p1_02_premium.py), data/processed/P2-01_noise_floor_daily.csv
Outputs  results/tables/P2-02_breaks.csv      every break of the headline model per series, with CI and regime means
         results/tables/P2-02_criteria.csv    SSR, BIC, LWZ for 0-8 breaks per series
         results/figures/P2-02_premium_breaks.png
Run      python scripts/p2_02_breaks.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
import ruptures as rpt
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
PROC, TAB, FIG = ROOT / "data/processed", ROOT / "results/tables", ROOT / "results/figures"
MIN_SEG, MAX_BREAKS, C95 = 20, 8, 11.03
SERIES = {"premium_bps": "main (PTAX window)", "premium_dayclose_bps": "S4a: day-close timing",
          "premium_cb_bps": "S4b: Coinbase USDT/USD"}

d = pd.read_csv(PROC / "P1-02_premium_daily.csv", parse_dates=["date_brt"], index_col="date_brt")


def lrv(e):
    """Newey-West long-run variance, Bartlett kernel."""
    e = e - e.mean()
    L = int(4 * (len(e) / 100) ** (2 / 9))
    return e @ e / len(e) + 2 * sum((1 - j / (L + 1)) * (e[j:] @ e[:-j]) / len(e) for j in range(1, L + 1))


def fit(y):
    """Break positions (first index of each new regime) for m = 0..8, and the information criteria."""
    T, algo = len(y), rpt.Dynp(model="l2", min_size=MIN_SEG, jump=1).fit(y)
    out, rows = {}, []
    for m in range(MAX_BREAKS + 1):
        b = algo.predict(n_bkps=m)[:-1] if m else []
        ssr = sum(((s - s.mean()) ** 2).sum() for s in np.split(y, b))
        p = 2 * m + 1
        out[m] = b
        rows.append({"breaks": m, "ssr": ssr, "bic": np.log(ssr / T) + p * np.log(T) / T,
                     "lwz": np.log(ssr / (T - p)) + p * 0.299 / T * np.log(T) ** 2.1})
    return out, pd.DataFrame(rows)


breaks, crit = [], []
for col, label in SERIES.items():
    s = d[col].dropna()
    y = s.to_numpy()
    cand, c = fit(y)
    m_bic, m_lwz = int(c.bic.idxmin()), int(c.lwz.idxmin())
    m = m_lwz if m_bic == MAX_BREAKS else m_bic
    crit.append(c.assign(series=col, chosen_bic=m_bic, chosen_lwz=m_lwz, headline=m))
    b = cand[m]
    segs = np.split(y, b)
    means = [g.mean() for g in segs]
    w2 = lrv(y - np.concatenate([np.full(len(g), g.mean()) for g in segs]))
    print(f"\n{label} ({col}): {len(y)} days {s.index[0].date()}..{s.index[-1].date()}; BIC picks {m_bic}, LWZ picks {m_lwz}, "
          f"headline {m}; long-run sd of residuals {np.sqrt(w2):.1f} bps; extra (not in the spec): a one-break model "
          f"puts its break at {s.index[cand[1][0]].date()}")
    for i, k in enumerate(b):
        delta = means[i + 1] - means[i]
        h = C95 * w2 / delta ** 2
        lo, hi = max(int(np.floor(k - h)), 0), min(int(np.ceil(k + h)), len(y) - 1)
        breaks.append({"series": col, "break": i + 1, "first_day_new_regime": s.index[k].date(),
                       "ci95_low": s.index[lo].date(), "ci95_high": s.index[hi].date(), "ci95_halfwidth_days": round(h, 1),
                       "mean_before_bps": round(means[i], 1), "mean_after_bps": round(means[i + 1], 1),
                       "change_bps": round(delta, 1), "matched_event": "pending P1-04 (S3)"})
    print(pd.DataFrame([r for r in breaks if r["series"] == col]).drop(columns=["series", "matched_event"]).to_string(index=False))

TAB.mkdir(parents=True, exist_ok=True)
br = pd.DataFrame(breaks)
br.to_csv(TAB / "P2-02_breaks.csv", index=False)
pd.concat(crit).to_csv(TAB / "P2-02_criteria.csv", index=False)
main = br[br.series == "premium_bps"]
hit = main[(pd.to_datetime(main.ci95_low) <= "2026-06-24") & (pd.to_datetime(main.ci95_high) >= "2026-06-23")]
pos = d.index.get_indexer(pd.to_datetime(main.first_day_new_regime))
near = main[np.abs(pos - d.index.get_loc(pd.Timestamp("2026-06-23"))) <= 5]
print(f"\nFound 23-24 Jun 2026 (main series)? CI contains it: {len(hit) > 0}; break within +/-5 PTAX days: {len(near) > 0}")

# Figure: premium, noise band, regime means, breaks with 95% CIs
BLUE, ORANGE = "#2a78d6", "#eb6834"
INK2, MUTED, GRID, SURFACE = "#52514e", "#b9b8b2", "#e4e3df", "#fcfcfb"
plt.rcParams.update({"figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "axes.edgecolor": GRID, "axes.labelcolor": INK2,
                     "xtick.color": INK2, "ytick.color": INK2, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6,
                     "axes.axisbelow": True, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10,
                     "axes.titlesize": 12, "axes.titleweight": "bold", "axes.titlelocation": "left",
                     "legend.frameon": False, "savefig.dpi": 150, "savefig.bbox": "tight"})
n = pd.read_csv(PROC / "P2-01_noise_floor_daily.csv", parse_dates=["date_utc"], index_col="date_utc")
band = n.noise_band_bps.reindex(d.index)
y = d.premium_bps
starts = [d.index[0]] + list(pd.to_datetime(main.first_day_new_regime))
level = pd.Series(np.nan, index=d.index)
for a, z, mu in zip(starts, starts[1:] + [d.index[-1] + pd.Timedelta(days=1)], [main.mean_before_bps.iloc[0]] + list(main.mean_after_bps)):
    level[(d.index >= a) & (d.index < z)] = mu
fig, ax = plt.subplots(figsize=(11, 4.6))
ax.fill_between(band.index, -band, band, color=ORANGE, alpha=0.25, linewidth=0, label="noise band: ± typical spread (P2-01)")
ax.plot(d.index, y, color=MUTED, linewidth=0.7, label="daily premium")
ax.plot(level.index, level, color=BLUE, linewidth=2, drawstyle="steps-post", label="regime mean (breaks found blind)")
prev = pd.Timestamp("1900-01-01")
for _, r in main.iterrows():
    t = pd.Timestamp(r.first_day_new_regime)
    ax.axvspan(pd.Timestamp(r.ci95_low), pd.Timestamp(r.ci95_high) + pd.Timedelta(days=1), color=BLUE, alpha=0.12, linewidth=0)
    ax.annotate(t.strftime("%d %b %Y"), (t, 1.0), xycoords=("data", "axes fraction"), rotation=90, va="top",
                ha="left" if (t - prev).days < 90 else "right", fontsize=8, color=INK2)  # close breaks: label on the other side
    prev = t
ax.axhline(0, color=INK2, linewidth=0.8)
ax.set_ylim(max(y.min(), -250), min(y.max(), 350))
ax.set_ylabel("premium over PTAX (bps; axis cut at 350)")
ax.set_title("USDT/BRL premium: regimes found by the break test, with 95% intervals (shaded)")
ax.legend(loc="lower left", ncol=3)
FIG.mkdir(parents=True, exist_ok=True)
fig.savefig(FIG / "P2-02_premium_breaks.png")
