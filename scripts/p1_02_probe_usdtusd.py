r"""P1-02 groundwork: which source can stand in for USDT's dollar price where Binance USDCUSDT is missing
(26 Sep 2022 - 11 Mar 2023)? Exploratory probe, reads straight from the web; writes nothing. Finding F-006.

Sources (all public, no key)
  Binance archive   https://data.binance.vision  monthly 1h klines BUSDUSDT, USDTDAI, USDCUSDT, USDTUSD
  Coinbase Exchange https://api.exchange.coinbase.com/products/USDT-USD/candles  (1h, max 300 per call, from 4 May 2021)
  Bitstamp          https://www.bitstamp.net/api/v2/ohlc/<pair>/                (1h, max 1000 per call)
Prints
  1. hours present and USDT/USD deviation from 1 (bps) per source, Oct 2022 - Feb 2023; FTX week daily minimum;
     agreement with Coinbase
  2. Jun 2026 overlap: Coinbase vs 1/USDCUSDT vs Binance USDTUSD
  3. SVB weekend: Bitstamp USDC/USD low (the part Binance misses) and Coinbase USDT/USD high
Run
  python scripts/p1_02_probe_usdtusd.py     (about 1 min)
"""
import io, json, time, urllib.request
import pandas as pd


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "out-of-sample-datathon"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def binance(pair, months):
    d = pd.concat(pd.read_csv(io.BytesIO(get(f"https://data.binance.vision/data/spot/monthly/klines/{pair}/1h/{pair}-1h-{m}.zip")),
                              compression="zip", header=None, usecols=[0, 4]) for m in months)
    d.index = pd.to_datetime(d[0].where(d[0] < 1e14, d[0] // 1000), unit="ms")
    return d[4].sort_index()


def coinbase(start, end):  # candles: [time, low, high, open, close, volume]
    out, t = [], pd.Timestamp(start)
    while t < pd.Timestamp(end):
        u = min(t + pd.Timedelta(hours=299), pd.Timestamp(end))
        out += json.loads(get(f"https://api.exchange.coinbase.com/products/USDT-USD/candles?granularity=3600"
                              f"&start={t:%Y-%m-%dT%H:%M:%SZ}&end={u:%Y-%m-%dT%H:%M:%SZ}"))
        t = u + pd.Timedelta(hours=1)
        time.sleep(0.2)
    d = pd.DataFrame(out, columns=["t", "low", "high", "open", "close", "vol"]).drop_duplicates("t")
    return d.set_index(pd.to_datetime(d.t, unit="s")).sort_index()


def bitstamp(pair, start, end):
    out, t = [], int(pd.Timestamp(start).timestamp())
    while t < pd.Timestamp(end).timestamp():
        r = json.loads(get(f"https://www.bitstamp.net/api/v2/ohlc/{pair}/?step=3600&limit=1000&start={t}"))["data"]["ohlc"]
        if not r:
            break
        out += r
        t = int(r[-1]["timestamp"]) + 3600
        time.sleep(0.2)
    d = pd.DataFrame(out).drop_duplicates("timestamp")
    return d.set_index(pd.to_datetime(d.timestamp.astype(int), unit="s"))[["low", "close"]].astype(float).sort_index()


# 1. The gap (monthly files Oct 2022 - Feb 2023; Sep and Mar are partly covered by USDCUSDT)
gap = ["2022-10", "2022-11", "2022-12", "2023-01", "2023-02"]
s = pd.DataFrame({"coinbase_usdtusd": coinbase("2022-10-01", "2023-03-01").close,
                  "bitstamp_usdtusd": bitstamp("usdtusd", "2022-10-01", "2023-03-01").close,
                  "binance_1/busdusdt": 1 / binance("BUSDUSDT", gap),
                  "binance_usdtdai": binance("USDTDAI", gap)})["2022-10-01":"2023-02-28 23:00"]
bps = (s - 1) * 1e4
print("hours present, Oct 2022 - Feb 2023, of", len(pd.date_range("2022-10-01", "2023-02-28 23:00", freq="h")))
print(s.notna().sum().to_string())
print("\nUSDT/USD deviation from 1, bps, monthly mean:")
print(bps.groupby(bps.index.to_period("M")).mean().round(1).to_string())
print("\nFTX week, daily minimum of hourly closes, bps:")
print(bps["2022-11-08":"2022-11-14"].resample("D").min().round(0).to_string())
d = bps.sub(bps.coinbase_usdtusd, axis=0).drop(columns="coinbase_usdtusd")
print("\nvs Coinbase: hourly corr", s.corr()["coinbase_usdtusd"].round(2).to_dict())
print("vs Coinbase: median |difference| bps", d.abs().median().round(1).to_dict())

# 2. Overlap in the 23 Jun 2026 event month, where USDCUSDT exists
o = pd.DataFrame({"coinbase_usdtusd": coinbase("2026-06-01", "2026-07-01").close,
                  "binance_1/usdcusdt": 1 / binance("USDCUSDT", ["2026-06"]),
                  "binance_usdtusd": binance("USDTUSD", ["2026-06"])})["2026-06-01":"2026-06-30 23:00"]
ob = (o - 1) * 1e4
print("\nJun 2026: mean deviation bps", ob.mean().round(1).to_dict())
print("Jun 2026 vs Coinbase: median |difference| bps", ob.sub(ob.coinbase_usdtusd, axis=0).abs().median().round(1).to_dict())

# 3. SVB weekend: the hours before Binance relisted USDCUSDT (2023-03-11 14:00 UTC)
u = bitstamp("usdcusd", "2023-03-10", "2023-03-15")["2023-03-10":"2023-03-14"]
c = coinbase("2023-03-10", "2023-03-14T23:00:00")
print(f"\nSVB: Bitstamp USDC/USD hours 10-14 Mar {len(u)} of 120; lowest low {u.low.min()} at {u.low.idxmin()}; "
      f"Coinbase USDT/USD highest high {c.high.max()} at {c.high.idxmax()}")
