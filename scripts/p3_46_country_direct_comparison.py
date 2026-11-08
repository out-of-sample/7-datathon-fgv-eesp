"""P3-46: Direct before/after comparison of official USD exchange rates and USDT premiums.

Inputs: frozen P1-05 premium CSV, P1-02 Brazil PTAX CSV, ECB FX CSV, Colombia TRM CSV.
Output: results/tables/P3-46_country_direct_comparison.csv.
Run: python scripts/p3_46_country_direct_comparison.py

Official rate is units of local currency per USD. Positive percent change means
the dollar became more expensive in that currency. Premium is the USDT price
relative to official USD converted to local currency, after USDT/USD adjustment.
Windows are fixed calendar intervals: 25 May–22 Jun and 24 Jun–21 Jul 2026.
"""

import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
premiums = pd.read_csv(
    DATA / "processed/P1-05_donor_premiums_daily.csv", parse_dates=["date"], index_col="date"
)
ecb = pd.read_csv(DATA / "raw/fx_official/ecb_exr.csv", parse_dates=["TIME_PERIOD"])
ecb = ecb.pivot(index="TIME_PERIOD", columns="CURRENCY", values="OBS_VALUE")
official = pd.DataFrame({currency: ecb[currency] / ecb.USD for currency in ["TRY", "ZAR", "MXN"]})
official["EUR"] = 1 / ecb.USD

brazil = pd.read_csv(
    DATA / "processed/P1-02_premium_daily.csv", parse_dates=["date_brt"], index_col="date_brt"
)
official["BRL_ptax"] = brazil.ptax_sell_brl_per_usd

trm = pd.read_csv(DATA / "raw/fx_official/trm_cop.csv", parse_dates=["vigenciadesde"])
colombia_dates = trm.vigenciadesde - pd.offsets.BDay(1)
official["COP"] = pd.Series(trm.valor.values, index=colombia_dates.values).groupby(level=0).last()

bcra = json.loads((DATA / "raw/fx_official/bcra_a3500.json").read_text())
ars = pd.DataFrame(bcra["results"][0]["detalle"])
official["ARS"] = pd.Series(ars.valor.values, index=pd.to_datetime(ars.fecha)).sort_index()

rows = []
for country, currency in [
    ("Brasil", "BRL_ptax"),
    ("Zona do euro", "EUR"),
    ("Turquia", "TRY"),
    ("África do Sul", "ZAR"),
    ("México", "MXN"),
    ("Colômbia", "COP"),
    ("Argentina", "ARS"),
]:
    aligned = pd.concat(
        [premiums[currency].rename("premium_bps"), official[currency].rename("local_per_usd")], axis=1
    ).dropna()
    before = aligned.loc["2026-05-25":"2026-06-22"]
    after = aligned.loc["2026-06-24":"2026-07-21"]
    assert len(before) >= 15 and len(after) >= 15, (country, len(before), len(after))
    before_rate, after_rate = before.local_per_usd.mean(), after.local_per_usd.mean()
    before_premium, after_premium = before.premium_bps.mean(), after.premium_bps.mean()
    rows.append({
        "country": country,
        "currency": "BRL" if currency == "BRL_ptax" else currency,
        "comparison_status": "excluded: capital controls and own June rule" if currency == "ARS" else "main comparison",
        "days_before": len(before),
        "days_after": len(after),
        "official_local_per_usd_before": round(before_rate, 5),
        "official_local_per_usd_after": round(after_rate, 5),
        "official_usd_change_pct": round(100 * (after_rate / before_rate - 1), 3),
        "usdt_premium_before_bps": round(before_premium, 2),
        "usdt_premium_after_bps": round(after_premium, 2),
        "usdt_premium_change_bps": round(after_premium - before_premium, 2),
    })

out = pd.DataFrame(rows)
path = ROOT / "results/tables/P3-46_country_direct_comparison.csv"
path.parent.mkdir(parents=True, exist_ok=True)
out.to_csv(path, index=False)
print(out.to_string(index=False))
print(f"\nSaved {path}")
