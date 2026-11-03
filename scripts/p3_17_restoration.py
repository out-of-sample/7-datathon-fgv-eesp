r"""P3-17: did the BCB let funds resume the FX imports of crypto that the 23 Jun 2026 notice stopped? (reopening test)
Specification: tasks/P3-17-channel-restoration.md (S1 evidence trail; S2 spec committed before any price is examined).

A        S1 screen of BCB rules and press notes, 20 Jun - 31 Oct 2026, from the BCB's public APIs. Lists every normativo
         and press note in the window, flags subjects that mention FX, virtual assets, funds or foreign capital. The
         flagged texts were read by hand; the classification is in results/tables/P3-17_candidates.md.
Inputs   https://www.bcb.gov.br/api/search/app/normativos/buscanormativos (normativos, retrieved at run time)
         https://www.bcb.gov.br/api/servico/sitebcb/notasimprensa and .../noticias (press notes and news)
Outputs  results/tables/P3-17_bcb_screen.csv   one row per normativo or press note in the window
Run      python scripts/p3_17_restoration.py
"""
import json
import re
import urllib.request
from html import unescape
from pathlib import Path

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
