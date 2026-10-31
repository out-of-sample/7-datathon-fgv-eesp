r"""P1-03: USDT/BRL from two Brazilian exchanges besides Binance, to check that the premium is not a Binance artefact.
Downloads and freezes hourly candles, then audits coverage and agreement with Binance. Safe to re-run.

Sources (public, no key; limits from each API's docs, read 31 Oct 2026)
  Foxbit          https://api.foxbit.com.br/rest/v3/markets/usdtbrl/candlesticks   500 candles/call, 15 calls per 2 s
                  docs https://docs.foxbit.com.br/rest/v3/ ; "open" is the previous candle's close (per the docs)
  Mercado Bitcoin https://api.mercadobitcoin.net/api/v4/candles?symbol=USDT-BRL    1 call/s; open = first trade
                  docs https://api.mercadobitcoin.net/api/v4/docs ; USDT-BRL candles start 2023-03-11 22h UTC;
                  hours without trades have no candle
Outputs (frozen at 30 Oct 2026 23h UTC, like P1-01)
  data/raw/foxbit/USDTBRL-1h.csv            columns as the API returns them (names from the docs)
  data/raw/mercadobitcoin/USDT-BRL-1h.csv   columns t, o, h, l, c, v (t = bucket start, Unix seconds UTC; v in USDT)
  results/tables/P1-03_venue_coverage.csv   coverage and agreement with Binance (also printed)
Run (from the repo root, after scripts/p1_01_download.py)
  python scripts/p1_03_second_venue.py
  then add the new files to data/raw/SHA256SUMS (command in tasks/P1-01 Handoff) and check with sha256sum -c
"""
import csv, json, time, urllib.request
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw"
END = pd.Timestamp("2026-10-30 23:00")  # same freeze as P1-01
FOXBIT_COLS = ["open_time_ms", "open", "high", "low", "close", "close_time_ms", "volume_usdt", "volume_brl", "trades",
               "taker_buy_volume_usdt", "taker_buy_volume_brl"]


def get(url, tries=3):
    req = urllib.request.Request(url, headers={"User-Agent": "out-of-sample-datathon"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read())
        except OSError:
            if i == tries - 1:
                raise
            time.sleep(2 ** (i + 1))


def save(path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path.with_suffix(".part"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    path.with_suffix(".part").rename(path)  # never leave a half-written file behind


# 1. Foxbit, 500-hour chunks from Oct 2020
fox = RAW / "foxbit/USDTBRL-1h.csv"
if not fox.exists():
    rows, t = {}, pd.Timestamp("2020-10-01")
    while t <= END:
        u = min(t + pd.Timedelta(hours=499), END)
        r = get(f"https://api.foxbit.com.br/rest/v3/markets/usdtbrl/candlesticks?interval=1h&limit=500"
                f"&start_time={t:%Y-%m-%dT%H:%M}&end_time={u:%Y-%m-%dT%H:%M}")
        if not isinstance(r, list):
            raise SystemExit(f"Foxbit error at {t}: {r}")
        rows.update((c[0], c) for c in r if t.value // 10**6 <= int(c[0]) <= u.value // 10**6)
        t = u + pd.Timedelta(hours=1)
        time.sleep(0.2)
    save(fox, FOXBIT_COLS, (rows[k] for k in sorted(rows, key=int)))
    print(f"Foxbit: {len(rows)} hourly candles")

# 2. Mercado Bitcoin, 30-day chunks from Mar 2023
mb = RAW / "mercadobitcoin/USDT-BRL-1h.csv"
if not mb.exists():
    rows, t = {}, pd.Timestamp("2023-03-01")
    while t <= END:
        u = min(t + pd.Timedelta(days=30) - pd.Timedelta(hours=1), END)
        r = get(f"https://api.mercadobitcoin.net/api/v4/candles?symbol=USDT-BRL&resolution=1h"
                f"&from={t.value // 10**9}&to={u.value // 10**9}")
        if not isinstance(r, dict) or "t" not in r:
            raise SystemExit(f"Mercado Bitcoin error at {t}: {r}")
        rows.update((ts, [ts, *(r[k][i] for k in "ohlcv")]) for i, ts in enumerate(r["t"])
                    if t.value // 10**9 <= ts <= u.value // 10**9)
        t = u + pd.Timedelta(hours=1)
        time.sleep(1.1)  # documented limit: 1 request per second
    save(mb, ["t", "o", "h", "l", "c", "v"], (rows[k] for k in sorted(rows)))
    print(f"Mercado Bitcoin: {len(rows)} hourly candles")

# 3. Coverage and agreement with Binance (hourly closes, same hour)
f = pd.read_csv(fox)
f = pd.DataFrame({"c": f.close, "l": f.low, "h": f.high, "v": f.volume_usdt}).set_index(pd.to_datetime(f.open_time_ms, unit="ms"))
m = pd.read_csv(mb)
m = pd.DataFrame({"c": m.c, "l": m.l, "h": m.h, "v": m.v}).set_index(pd.to_datetime(m.t, unit="s"))
b = pd.concat(pd.read_csv(z, header=None, usecols=[0, 4, 5]) for z in sorted((RAW / "binance/USDTBRL").glob("*.zip")))
b = b.set_index(pd.to_datetime(b[0].where(b[0] < 1e14, b[0] // 1000), unit="ms")).sort_index()
venues = {"Foxbit": f[f.v > 0], "Mercado Bitcoin": m[m.v > 0]}  # Foxbit fills no-trade hours with zeros; MB omits them
out = []
for name, k in venues.items():
    t = k.index.to_series()
    gap = t.diff().dt.total_seconds() / 3600 - 1  # hours without trades right before each traded hour
    span = (t.iloc[-1] - t.iloc[0]) / pd.Timedelta(hours=1) + 1
    diff = ((k.c / b[4].reindex(k.index) - 1) * 1e4).dropna()
    out.append({"venue": name, "hours_with_trades": len(k), "first_utc": t.iloc[0], "last_utc": t.iloc[-1],
                "no_trade_pct": round(100 * (1 - len(k) / span), 1), "longest_gap_h": int(gap.max()),
                "longest_gap_before_utc": t[gap.idxmax()], "gaps_gt24h": int((gap > 24).sum()),
                "dup_ts": int(t.duplicated().sum()), "bad_hlc": int(((k.l > k.c) | (k.h < k.c) | (k.l <= 0)).sum()),
                "median_abs_diff_vs_binance_bps": round(diff.abs().median(), 1), "mean_diff_vs_binance_bps": round(diff.mean(), 1)})
    for i in gap.nlargest(3).index:
        print(f"  {name} longest no-trade stretches: {t[i] - pd.Timedelta(hours=gap[i])} .. {t[i] - pd.Timedelta(hours=1)} ({gap[i]:.0f} h)")
cov = pd.DataFrame(out)
(ROOT / "results/tables").mkdir(parents=True, exist_ok=True)
cov.to_csv(ROOT / "results/tables/P1-03_venue_coverage.csv", index=False)
print(cov.T.to_string())
share = {n: k.v.gt(0).reindex(pd.date_range(k.index[0], END, freq="h"), fill_value=False) for n, k in venues.items()}
print("share of hours with trades, by year:\n",
      pd.DataFrame({n: s.groupby(s.index.year).mean() for n, s in share.items()}).round(2).to_string())
vol = pd.DataFrame({**{n: k.v.resample("ME").sum() / 1e6 for n, k in venues.items()}, "Binance": b[5].resample("ME").sum() / 1e6})
fx = pd.read_csv(fox).set_index(pd.to_datetime(pd.read_csv(fox).open_time_ms, unit="ms"))
vol["Foxbit_trades_k"] = fx.trades.resample("ME").sum() / 1e3
vol["Foxbit_avg_trade_usdt"] = fx.volume_usdt.resample("ME").sum() / fx.trades.resample("ME").sum()
print("traded volume, million USDT per year:\n", vol.groupby(vol.index.year).sum().round(0).to_string())
print("traded volume, million USDT per month, 2026:\n", vol.loc["2026"].round(0).to_string())
