"""P1-05 independent review of donor measurement and coverage.

Inputs: frozen Binance/official FX files and the existing P1-05 output CSVs.
Outputs: results/tables/P1-05_review.csv, _review_yearly.csv, _review_differences.csv.
Run: .venv/bin/python scripts/p1_05_review.py
Reconstructs premiums from raw inputs without importing the production scripts.
Checks numerical implementation, not whether a currency is an admissible control.
"""
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw"
TABLES = ROOT / "results/tables"


def candles(pair):
    frame = pd.concat([pd.read_csv(p, header=None, usecols=[0, 1, 5])
                       for p in sorted((RAW / "binance" / pair).glob("*.zip"))])
    dates = [pd.Timestamp(int(x), unit="us" if int(x) >= 10**14 else "ms", tz="UTC")
             for x in frame[0]]
    frame = pd.DataFrame({"open": frame[1].to_numpy(), "volume": frame[5].to_numpy()}, index=dates)
    assert frame.index.is_unique, f"Duplicate candles: {pair}"
    assert (frame.open > 0).all() and (frame.volume >= 0).all(), pair
    return frame.sort_index()


# With USDC = USD: (local/USDT) * (USDT/USDC) / (local/USD) is dimensionless.
# USDC and the BUSD fallback are assumed to equal USD, as in the original design.
stable_quote = candles("USDCUSDT").open.combine_first(candles("BUSDUSDT").open)
ecb = pd.read_csv(RAW / "fx_official/ecb_exr.csv").pivot(
    index="TIME_PERIOD", columns="CURRENCY", values="OBS_VALUE")
ecb.index = pd.to_datetime(ecb.index)
rates = {c: ecb[c].div(ecb.USD) for c in ["TRY", "ZAR", "MXN", "PLN", "IDR", "BRL"]}
rates["EUR"] = 1 / ecb.USD
trm = pd.read_csv(RAW / "fx_official/trm_cop.csv", parse_dates=["vigenciadesde", "vigenciahasta"])
# The frozen file groups repeated validity days into intervals. Check that subtracting
# a weekday, as the implementation does, agrees with the previous calendar day here.
assert (trm.vigenciadesde - pd.Timedelta(days=1)).equals(trm.vigenciadesde - pd.offsets.BDay(1))
assert (trm.vigenciadesde.iloc[1:].reset_index(drop=True) ==
        (trm.vigenciahasta.iloc[:-1] + pd.Timedelta(days=1)).reset_index(drop=True)).all()
rates["COP"] = pd.Series(trm.valor.to_numpy(), index=trm.vigenciadesde - pd.Timedelta(days=1))
nbu = pd.DataFrame(json.loads((RAW / "fx_official/nbu_uah.json").read_bytes()))
assert nbu.groupby("calcdate").rate.nunique().eq(1).all()
nbu = nbu.drop_duplicates("calcdate")
rates["UAH"] = pd.Series(nbu.rate.to_numpy(), index=pd.to_datetime(nbu.calcdate, dayfirst=True))
bcra = json.loads((RAW / "fx_official/bcra_a3500.json").read_bytes())
assert bcra["metadata"]["resultset"]["count"] <= 3000
ars = pd.DataFrame(bcra["results"][0]["detalle"])
rates["ARS"] = pd.Series(ars.valor.to_numpy(), index=pd.to_datetime(ars.fecha))

saved = pd.read_csv(ROOT / "data/processed/P1-05_donor_premiums_daily.csv", index_col="date", parse_dates=True)
coverage = pd.read_csv(TABLES / "P1-05_donor_coverage.csv").set_index("currency")
rows = []
differences = []
for currency, official in rates.items():
    pair = "EURUSDT" if currency == "EUR" else "USDT" + currency
    bars = candles(pair)
    zone, hours = {
        "COP": ("America/Bogota", list(range(8, 14))),
        "UAH": ("Europe/Kyiv", list(range(10, 17))),
        "ARS": ("America/Argentina/Buenos_Aires", list(range(10, 16))),
    }.get(currency, ("Europe/Berlin", [14]))
    local_clock = bars.index.tz_convert(zone)
    bars = bars.loc[local_clock.hour.isin(hours) & bars.volume.gt(0)]
    local_usdt = 1 / bars.open if currency == "EUR" else bars.open
    implied_usd = local_usdt.mul(stable_quote.reindex(bars.index)).dropna()
    local_day = implied_usd.index.tz_convert(zone).tz_localize(None).normalize()
    sessions = implied_usd.groupby(local_day).agg(["mean", "count"])
    official = official.sort_index()
    assert official.index.is_unique and official.gt(0).all(), currency
    reconstructed = sessions["mean"].div(official).sub(1).mul(10000)
    name = "BRL_ecb" if currency == "BRL" else currency
    # Donor history before the BRL listing is omitted by the production USD input;
    # review the advertised output domain, including missing entries within it.
    expected = reconstructed.reindex(saved.index)
    actual = saved[name]
    assert expected.isna().equals(actual.isna()), f"Missing-value mismatch: {currency}"
    error = (expected - actual).abs().max()
    gap = expected - actual
    for date, value in gap[gap.abs() > 0.005001].items():
        differences.append({"currency": currency, "date": str(date.date()),
                            "independent_bps": expected.loc[date], "production_bps": actual.loc[date],
                            "difference_bps": value})
    for window, start, end in [("pre", "2025-11-01", "2026-06-22"),
                                ("post", "2026-06-24", "2026-09-30")]:
        fixes = official.loc[start:end].index
        counts = sessions["count"].reindex(fixes).fillna(0)
        share = reconstructed.reindex(fixes).notna().mean()
        window_error = gap.reindex(fixes).abs().max()
        assert window_error <= 0.005001, f"Core-period premium mismatch: {currency} {window}"
        assert len(fixes) == coverage.loc[currency, window + "_fix_days"]
        assert round(share, 3) == coverage.loc[currency, window + "_share_with_premium"]
        rows.append({"currency": currency, "window": window, "fix_days": len(fixes),
                     "share_with_premium": round(share, 6),
                     "partial_sessions": int(((counts > 0) & (counts < len(hours))).sum()),
                     "max_error_bps": round(window_error, 6), "history_max_error_bps": round(error, 6)})

pd.DataFrame(rows).to_csv(TABLES / "P1-05_review.csv", index=False)
pd.DataFrame(differences, columns=["currency", "date", "independent_bps", "production_bps", "difference_bps"]).to_csv(
    TABLES / "P1-05_review_differences.csv", index=False)
yearly = saved.loc[:"2026-06-22"].groupby(saved.loc[:"2026-06-22"].index.year).mean()
yearly.round(2).to_csv(TABLES / "P1-05_review_yearly.csv", index_label="year")
print(pd.DataFrame(rows).to_string(index=False))
print("\nYearly means (2026 through 22 June), bps:")
print(yearly.loc[2024:].round(2).to_string())
print("\nHistorical discrepancies beyond CSV rounding:", differences)
print("PASS: independent raw-data reconstruction in the core pre/post windows and coverage checks.")
