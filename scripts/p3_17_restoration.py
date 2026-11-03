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
Inputs   https://www.bcb.gov.br/api/search/app/normativos/buscanormativos (normativos, retrieved at run time)
         https://www.bcb.gov.br/api/servico/sitebcb/notasimprensa and .../noticias (press notes and news)
         data/processed/P3-10_imports_monthly.csv, results/tables/P3-10_order_flow.csv (both from p3_10_imports.py)
Outputs  results/tables/P3-17_bcb_screen.csv   one row per normativo or press note in the window
         results/tables/P3-17_s4_structure.csv one row per venue x metric with before/spike/after and the revert flag
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
