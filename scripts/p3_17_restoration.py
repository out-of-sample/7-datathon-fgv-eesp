r"""P3-17: did the BCB let funds resume the FX imports of crypto that the 23 Jun 2026 notice stopped? (reopening test)
Specification: tasks/P3-17-channel-restoration.md (S1 evidence trail; S2 spec committed before any price is examined).

A        S1 screen of BCB rules and press notes, 20 Jun - 31 Oct 2026, from the BCB's public APIs. Lists every normativo
         and press note in the window, flags subjects that mention FX, virtual assets, funds or foreign capital. The
         flagged texts were read by hand; the classification is in results/tables/P3-17_candidates.md.
B        S4 consistency check for the fall from 22 Jul (rule fixed in the task file, S2, before this part was run).
         R = mean(Aug, Sep 2026) / mean(Jan-May 2026) of BCB stablecoin purchases abroad, and Aug vs Jul.
         Per venue and metric (avg trade, buyer share): reverts if |log(after/before)| < |log(after/spike)|.
         Demand: Binance volume per day, log(after/before) < -0.29; buyer share after < before.
         No restoration test is run: the S2 credible set is empty.
C        POST HOC (S6, asked after S4 was seen; not pre-registered): who traded while the premium fell? Daily order flow
         on Binance and Foxbit, 1 May - 30 Sep 2026. Net seller-initiated volume = volume - 2 x taker-buy volume (USDT).
         Phases: pre 1 May - 22 Jun, wave 30 Jun - 21 Jul, after 22 Jul - 30 Sep. Flows use UTC days, premium BRT dates.
Inputs   https://www.bcb.gov.br/api/search/app/normativos/buscanormativos (normativos, retrieved at run time)
         https://www.bcb.gov.br/api/servico/sitebcb/notasimprensa and .../noticias (press notes and news)
         data/processed/P3-10_imports_monthly.csv, results/tables/P3-10_order_flow.csv (both from p3_10_imports.py)
         data/processed/P1-02_premium_daily.csv, results/tables/P2-05_venues_daily.csv,
         data/raw/binance/USDTBRL/*.zip, data/raw/foxbit/USDTBRL-1h.csv, data/raw/mercadobitcoin/USDT-BRL-1h.csv
Outputs  results/tables/P3-17_bcb_screen.csv   one row per normativo or press note in the window
         results/tables/P3-17_s4_structure.csv one row per venue x metric with before/spike/after and the revert flag
         results/tables/P3-17_daily_flow.csv   one row per day, premium and order flow by venue (part C)
Run      python scripts/p3_17_restoration.py
"""
import json
import re
import urllib.request
from html import unescape
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
TAB = ROOT / "results/tables"
START, END = "2026-06-20", "2026-10-31"
KW = re.compile(r"ativos? virtua|cripto|stablecoin|fundos? de investimento|câmbio|cambia|capitais|exterior|SPSAV|PSAV",
                re.I)


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return json.load(urllib.request.urlopen(req, timeout=60))


def clean(s):
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()


# A1: every normativo in the window (the search API pages 50 rows at a time)
q = ("https://www.bcb.gov.br/api/search/app/normativos/buscanormativos?querytext=ContentType:normativo%20AND%20"
     "contentSource:normativos&rowlimit=50&startrow={}&sortlist=Data1OWSDATE:descending&refinementfilters="
     f"Data:range(datetime({START}),datetime({END}))")
first = get(q.format(0))
rows = first["Rows"] + [r for s in range(50, first["TotalRows"], 50) for r in get(q.format(s))["Rows"]]
norm = pd.DataFrame([dict(source="normativo", date=r["data"][:10], kind=r["TipodoNormativoOWSCHCS"], title=r["title"],
                          subject=clean(r.get("AssuntoNormativoOWSMTXT"))) for r in rows if "title" in r])
norm = norm.drop_duplicates(["kind", "title"])

# A2: press notes and news (the APIs return the latest N; 400 reaches back past June)
press = []
for kind, path in [("nota à imprensa", "notasimprensa"), ("notícia", "noticias")]:
    for r in get(f"https://www.bcb.gov.br/api/servico/sitebcb/{path}?quantidade=400")["conteudo"]:
        press.append(dict(source="press", date=r["dataPublicacao"][:10], kind=kind, title=f"Id {r['Id']}",
                          subject=r["titulo"]))
press = pd.DataFrame(press)
press = press[(press.date >= START) & (press.date <= END)]

out = pd.concat([norm, press]).sort_values(["date", "kind", "title"])
out["flag_keyword"] = out.subject.str.contains(KW)
out.to_csv(TAB / "P3-17_bcb_screen.csv", index=False)
print(f"A normativos {START}..{END}: {len(norm)} (API TotalRows {first['TotalRows']}); by type:",
      norm.kind.value_counts().to_dict())
print(f"A press notes and news in window: {len(press)}; flagged by keyword: normativos "
      f"{int(out[out.source == 'normativo'].flag_keyword.sum())}, press {int(out[out.source == 'press'].flag_keyword.sum())}")
nc = out[(out.source == "normativo") & (out.kind != "Comunicado") & out.flag_keyword]
print("A flagged non-Comunicado normativos:")
for _, r in nc.iterrows():
    print(f"  {r.date} {r.title}: {r.subject[:110]}")

# B1: BCB stablecoin purchases abroad (SGS 29644, US$ million per month)
imp = pd.read_csv(ROOT / "data/processed/P3-10_imports_monthly.csv", parse_dates=["month"], index_col="month")
imp = imp["imports_usd_mn"]
pre = imp["2026-01-01":"2026-05-01"].mean()
r = imp["2026-08-01":"2026-09-01"].mean() / pre
print(f"\nB1 purchases abroad, US$ mn: Jan-May mean {pre:.0f}; " +
      "; ".join(f"{m:%b} {v:.0f}" for m, v in imp["2026-06-01":"2026-09-01"].items()) +
      f" | R = {r:.2f} ({'>=' if r >= 0.5 else '<'} 0.5) | Aug > Jul: {imp['2026-08-01'] > imp['2026-07-01']}")

# B2: exchange structure, before [-20,-1] / spike [+1,+20] / after [+21,+60] PTAX days around 23 Jun
of = pd.read_csv(TAB / "P3-10_order_flow.csv")
of["w"] = of.window.str.split().str[0]
rows = []
for (venue, metric), g in of.melt(["w", "venue"], ["avg_trade_usdt", "buyer_initiated_share", "volume_usdt_per_day"],
                                  var_name="metric").groupby(["venue", "metric"]):
    v = g.set_index("w").value
    d_before, d_spike = np.log(v["after"] / v["before"]), np.log(v["after"] / v["spike"])
    rows.append(dict(venue=venue, metric=metric, before=v["before"], spike=v["spike"], after=v["after"],
                     log_after_before=round(d_before, 3), log_after_spike=round(d_spike, 3),
                     reverts=abs(d_before) < abs(d_spike)))
# Mercado Bitcoin has hourly candles only, so no trade size or buyer share: those rows are dropped, not counted
st = pd.DataFrame(rows).dropna(subset=["before", "spike", "after"])
st.to_csv(TAB / "P3-17_s4_structure.csv", index=False)
print("B2 exchange windows (before / spike / after):")
print(st.to_string(index=False))
s = st[st.metric != "volume_usdt_per_day"]
print(f"B2 structure reverts on {int(s.reverts.sum())} of {len(s)} venue-metrics (avg trade, buyer share)")
b = st.set_index(["venue", "metric"])
bs = st[st.metric == "buyer_initiated_share"]
print(f"B3 demand: Binance volume log(after/before) = {b.loc[('Binance', 'volume_usdt_per_day'), 'log_after_before']:+.3f} "
      f"(fell > 25%: {b.loc[('Binance', 'volume_usdt_per_day'), 'log_after_before'] < -0.29}); buyer share after < before: "
      + ", ".join(f"{r.venue} {r.after < r.before}" for r in bs.itertuples()))

# C (post hoc): order flow while the premium fell. Loading as in p3_10_imports.py
RAW = ROOT / "data/raw"
bz = pd.concat(pd.read_csv(z, header=None, usecols=[0, 1, 4, 5, 8, 9]) for z in sorted((RAW / "binance/USDTBRL").glob("*.zip")))
t = bz[0].astype("int64")
bz.index = pd.to_datetime(np.where(t > 1e14, t // 1000, t), unit="ms")  # Binance files from 2025 use microseconds
bz = bz.rename(columns={1: "open", 4: "close", 5: "volume", 8: "trades", 9: "buyer_volume"}).sort_index()
fz = pd.read_csv(RAW / "foxbit/USDTBRL-1h.csv")
fz = pd.DataFrame({"open": fz.open.values, "close": fz.close.values, "volume": fz.volume_usdt.values, "trades": fz.trades.values,
                   "buyer_volume": fz.taker_buy_volume_usdt.values}, index=pd.to_datetime(fz.open_time_ms, unit="ms"))
fz = fz[fz.volume > 0].sort_index()
mz = pd.read_csv(RAW / "mercadobitcoin/USDT-BRL-1h.csv")
mz = pd.Series(mz.v.values, index=pd.to_datetime(mz.t, unit="s")).sort_index()

# C0: sign check of the taker-buy field: hours with more buyer-initiated volume should have rising prices
for name, h in [("Binance", bz.loc["2026"]), ("Foxbit", fz.loc["2026"])]:
    h = h[h.volume > 1000]
    print(f"\nC0 {name} 2026: corr(hourly buyer share, hourly return) = "
          f"{(h.buyer_volume / h.volume).corr(h.close / h.open - 1):+.3f} (n = {len(h)} hours)")

day = {k: v[["volume", "trades", "buyer_volume"]].resample("D").sum() for k, v in [("bin", bz), ("fox", fz)]}
ven = pd.read_csv(TAB / "P2-05_venues_daily.csv", parse_dates=["date_brt"], index_col="date_brt")
prem = pd.read_csv(ROOT / "data/processed/P1-02_premium_daily.csv", parse_dates=["date_brt"], index_col="date_brt").premium_bps
fl = pd.DataFrame({"premium_bps": prem, "premium_binance": ven.Binance, "premium_foxbit": ven.Foxbit,
                   "mb_volume_mn": mz.resample("D").sum() / 1e6})
for k, v in day.items():
    fl[f"{k}_volume_mn"] = v.volume / 1e6
    fl[f"{k}_buyer_share"] = v.buyer_volume / v.volume
    fl[f"{k}_avg_trade"] = v.volume / v.trades
    fl[f"{k}_net_sell_mn"] = (v.volume - 2 * v.buyer_volume) / 1e6
fl = fl["2026-05-01":"2026-09-30"]
fl["fox_share"] = fl.fox_volume_mn / fl[["fox_volume_mn", "bin_volume_mn", "mb_volume_mn"]].sum(axis=1)
fl.to_csv(TAB / "P3-17_daily_flow.csv", float_format="%.4f")

# C1: was anything like the Foxbit selling seen before the notice?
fd = day["fox"][day["fox"].volume > 0]
fn = (fd.volume - 2 * fd.buyer_volume) / 1e6
pre_f, wave_f = fn[:"2026-06-22"], fn["2026-06-30":"2026-07-21"]
print(f"C1 Foxbit {pre_f.index[0]:%d %b %Y} - 22 Jun 2026 ({len(pre_f)} days): largest daily net selling {pre_f.max():.1f} mn USDT "
      f"({pre_f.idxmax():%d %b %Y}), days above 10 mn: {(pre_f > 10).sum()} | wave: {(wave_f > 10).sum()} of {len(wave_f)} days")

# C2: phases (weekdays for the daily means)
PH = [("pre", "2026-05-01", "2026-06-22"), ("wave", "2026-06-30", "2026-07-21"), ("after", "2026-07-22", "2026-09-30")]
wd = fl[fl.index.dayofweek < 5]
for lab, a, z in PH:
    s, h = wd[a:z], fz.loc[a:z]
    brt = h.index - pd.Timedelta(hours=3)
    print(f"C2 {lab:5} {a}..{z}: net selling per weekday, Binance {s.bin_net_sell_mn.mean():+.1f}, Foxbit {s.fox_net_sell_mn.mean():+.1f} "
          f"mn USDT (total Foxbit {(h.volume - 2 * h.buyer_volume).sum() / 1e6:+.1f}, Binance {fl[a:z].bin_net_sell_mn.sum():+.1f}) | "
          f"Foxbit avg trade median {s.fox_avg_trade.median():.0f} USDT, share {s.fox_share.mean():.2f}, "
          f"09-18h BRT {h.volume[(brt.hour >= 9) & (brt.hour < 18)].sum() / h.volume.sum():.2f}, weekend "
          f"{h.volume[brt.dayofweek >= 5].sum() / h.volume.sum():.3f} | Foxbit - Binance premium "
          f"{(s.premium_foxbit - s.premium_binance).mean():+.2f} bps | premium {fl[a:z].premium_bps.mean():.1f} bps")

# C3: within the episode (PTAX days 24 Jun - 31 Jul, n is one episode, not independent events)
e = fl["2026-06-24":"2026-07-31"].dropna(subset=["premium_bps"]).copy()
e["d"] = e.premium_bps.diff()
for c in ["fox_net_sell_mn", "bin_net_sell_mn"]:
    print(f"C3 {c}: corr with premium level {e.premium_bps.corr(e[c]):+.2f}; with same-day change {e.d.corr(e[c]):+.2f}; "
          f"with next-day change {e.d.shift(-1).corr(e[c]):+.2f} (n = {e.d.notna().sum()} PTAX days)")
print("C4 monthly mean premium, bps: " + "; ".join(f"{m:%b} {v:.1f}" for m, v in fl.premium_bps.resample("MS").mean().items()))

# C5: weekend drift (Fri 17h -> Mon 09h BRT, both against Friday's PTAX); the big seller traded 1% of its volume on weekends
hp = pd.read_csv(ROOT / "data/processed/P1-02_premium_hourly.csv", usecols=["time_utc", "premium_vs_last_ptax_bps", "ptax_last_date_brt"],
                 parse_dates=["time_utc"], index_col="time_utc")
wk = {}
for fri in pd.date_range("2026-01-02", "2026-09-25", freq="W-FRI"):
    a, z = fri + pd.Timedelta(hours=20), fri + pd.Timedelta(days=3, hours=12)
    if a in hp.index and z in hp.index and hp.ptax_last_date_brt[a] == hp.ptax_last_date_brt[z]:
        wk[fri] = hp.premium_vs_last_ptax_bps[z] - hp.premium_vs_last_ptax_bps[a]
wk = pd.Series(wk)
for lab, a, z in [("pre", "2026-01-01", "2026-06-22"), ("wave", "2026-06-30", "2026-07-21"), ("after", "2026-07-22", "2026-09-30")]:
    s = wk[a:z]
    print(f"C5 weekend change {lab:5}: n = {len(s)}, mean {s.mean():+.1f} bps, sd {s.std():.1f}; values {', '.join(f'{v:+.0f}' for v in s)}"
          if len(s) < 6 else f"C5 weekend change {lab:5}: n = {len(s)}, mean {s.mean():+.1f} bps, sd {s.std():.1f}")
