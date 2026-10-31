r"""P1-07: detect independent stablecoin depegs and draw the SVB-weekend case figure.

Purpose
-------
Screen Binance hourly stablecoin/USDT prices, correct each candidate with a direct
USDT/USD price where available, log rejected relative-price candidates, and draw
the USDC/USD path over the SVB weekend.  The event definition is frozen in
``tasks/P1-07-depeg-detector.md`` before this script was written.

Inputs
------
* Binance Vision public 1h archives (downloaded unchanged to data/raw/binance/)
* Coinbase Exchange public USDT/USD 1h candles, fetched only around candidates
* Bitstamp public USDC/USD 1h candles for 10--14 Mar 2023

Outputs
-------
* data/processed/P1-07_depeg_events.csv
* results/figures/P1-07_svb_weekend.png
* data/raw/bitstamp/USDC-USD-1h_2023-03-10_to_2023-03-14.csv (not committed)

Run
---
python scripts/p1_07_depeg.py

The default download cutoff is 30 Sep 2026, the final complete Binance monthly
archive available when P1 ran.  Binance prices are a *screen*: a direct USDT/USD
reference is required before a candidate is counted as a USD-level depeg.  A
candidate without that reference remains explicitly labelled ``relative-price
candidate`` rather than becoming a claim about the numerator stablecoin.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import time
import urllib.request
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed" / "P1-07_depeg_events.csv"
FIG = ROOT / "results" / "figures" / "P1-07_svb_weekend.png"
BINANCE_BUCKET = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision"
PAIRS = ("USDCUSDT", "BUSDUSDT", "TUSDUSDT", "USTUSDT", "USTCUSDT", "FDUSDUSDT", "USDPUSDT")
FIRST_MONTH, LAST_MONTH = "2019-01", "2026-09"
HOUR = pd.Timedelta(hours=1)


def get(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "out-of-sample-datathon"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.read()
        except OSError:
            if attempt == 2:
                raise
            time.sleep(2**attempt)
    raise AssertionError("unreachable")


def archive_keys(pair: str) -> list[str]:
    """Return complete monthly 1h archives in the pre-specified study period."""
    prefix = f"data/spot/monthly/klines/{pair}/1h/"
    xml = get(f"https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?prefix={prefix}&delimiter=/").decode()
    keys = re.findall(r"<Key>([^<]*\.zip)</Key>", xml)
    if "<IsTruncated>false</IsTruncated>" not in xml:
        raise RuntimeError(f"truncated Binance listing for {pair}")
    month = lambda key: key.rsplit("-1h-", 1)[1][:7]
    return [key for key in keys if FIRST_MONTH <= month(key) <= LAST_MONTH]


def fetch_zip(key: str) -> tuple[str, bytes]:
    """Download a canonical archive only when Binance's published checksum matches."""
    data = get(f"{BINANCE_BUCKET}/{key}")
    expected = get(f"{BINANCE_BUCKET}/{key}.CHECKSUM").split()[0].decode()
    if hashlib.sha256(data).hexdigest() != expected:
        raise RuntimeError(f"Binance checksum mismatch: {key}")
    return key, data


def download_binance(pairs: tuple[str, ...] = PAIRS) -> None:
    """Fetch missing monthly archives concurrently; existing publisher bytes stay untouched."""
    missing: list[str] = []
    for pair in pairs:
        for key in archive_keys(pair):
            if not (RAW / "binance" / pair / Path(key).name).exists():
                missing.append(key)
    print(f"Binance monthly archives: {len(missing)} missing across {len(pairs)} pairs", flush=True)
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(fetch_zip, key): key for key in missing}
        for n, future in enumerate(as_completed(futures), start=1):
            key, data = future.result()
            target = RAW / "binance" / key.split("/")[-3] / Path(key).name
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_suffix(".part")
            temporary.write_bytes(data)
            temporary.replace(target)
            if n % 25 == 0 or n == len(missing):
                print(f"  downloaded {n}/{len(missing)}", flush=True)


def read_pair(pair: str) -> pd.DataFrame:
    files = sorted((RAW / "binance" / pair).glob("*.zip"))
    if not files:
        raise RuntimeError(f"no local Binance archives for {pair}")
    parts = []
    for file in files:
        x = pd.read_csv(file, header=None, usecols=[0, 1, 2, 3, 4, 5],
                        names=["open_time", "open", "high", "low", "close", "volume"])
        timestamp = x.open_time.where(x.open_time < 1e14, x.open_time // 1000)
        x["timestamp_utc"] = pd.to_datetime(timestamp, unit="ms", utc=True)
        parts.append(x[["timestamp_utc", "open", "high", "low", "close", "volume"]])
    out = pd.concat(parts, ignore_index=True).drop_duplicates("timestamp_utc").sort_values("timestamp_utc")
    return out[(out.timestamp_utc >= f"{FIRST_MONTH}-01") & (out.timestamp_utc < "2026-10-01")].reset_index(drop=True)


def contiguous(times: pd.Series) -> bool:
    return len(times) > 1 and bool((times.diff().iloc[1:] == HOUR).all())


def detect(prices: pd.Series, start_band: float = 0.005, recovery_band: float = 0.001) -> list[dict]:
    """Apply the frozen hourly version of the event rule to a UTC-indexed close series."""
    prices = prices.dropna().sort_index()
    events, i, n = [], 0, len(prices)
    while i < n - 1:
        start_window = prices.iloc[i:i + 2]
        if (len(start_window) == 2 and contiguous(start_window.index.to_series())
                and (start_window.sub(1).abs() > start_band).all()):
            start = start_window.index[0]
            j, end = i + 2, None
            while j <= n - 6:
                recovery_window = prices.iloc[j:j + 6]
                if (contiguous(recovery_window.index.to_series())
                        and (recovery_window.sub(1).abs() < recovery_band).all()):
                    end = recovery_window.index[0]
                    break
                j += 1
            stop = j + 6 if end is not None else n
            segment = prices.loc[start:(end if end is not None else prices.index[-1])]
            events.append({"start_utc": start, "end_utc": end, "censored": end is None,
                           "max_deviation_bps": float(segment.sub(1).abs().max() * 1e4),
                           "min_price": float(segment.min()), "max_price": float(segment.max())})
            i = stop
        else:
            i += 1
    # The frozen definition merges episodes separated by fewer than 24 hours.
    merged: list[dict] = []
    for event in events:
        if merged and merged[-1]["end_utc"] is not None and event["start_utc"] - merged[-1]["end_utc"] < pd.Timedelta(hours=24):
            old = merged[-1]
            old["end_utc"], old["censored"] = event["end_utc"], event["censored"]
            old["max_deviation_bps"] = max(old["max_deviation_bps"], event["max_deviation_bps"])
            old["min_price"], old["max_price"] = min(old["min_price"], event["min_price"]), max(old["max_price"], event["max_price"])
            old["merged_episodes"] += 1
        else:
            event["merged_episodes"] = 1
            merged.append(event)
    return merged


def coinbase_usdt_usd(start: pd.Timestamp, end: pd.Timestamp) -> pd.Series:
    """Fetch direct USDT/USD closes in 300-hour chunks for candidate confirmation."""
    candles: dict[int, list] = {}
    start, end = pd.Timestamp(start).tz_convert("UTC"), pd.Timestamp(end).tz_convert("UTC")
    cursor = start.floor("h")
    while cursor <= end:
        finish = min(cursor + pd.Timedelta(hours=299), end)
        url = ("https://api.exchange.coinbase.com/products/USDT-USD/candles?granularity=3600"
               f"&start={cursor:%Y-%m-%dT%H:%M:%SZ}&end={finish:%Y-%m-%dT%H:%M:%SZ}")
        data = json.loads(get(url))
        if not isinstance(data, list):
            raise RuntimeError(f"Coinbase response at {cursor}: {data}")
        candles.update({row[0]: row for row in data})
        cursor = finish + HOUR
        time.sleep(0.08)
    if not candles:
        return pd.Series(dtype=float, name="usdt_usd")
    frame = pd.DataFrame(candles.values(), columns=["time", "low", "high", "open", "close", "volume"])
    frame.index = pd.to_datetime(frame.time, unit="s", utc=True)
    return frame.close.astype(float).sort_index().rename("usdt_usd")


def direct_confirmation(pair: str, relative: pd.Series, event: dict) -> dict:
    """Turn one relative-price candidate into a direct-dollar event where the reference permits."""
    start = event["start_utc"]
    # Binance relisted USDC/USDT in the middle of the SVB weekend.  The direct Bitstamp
    # series is used for the case figure, but this truncated Binance episode cannot be
    # an independently timed event in the automatic count.
    if pair == "USDCUSDT" and pd.Timestamp("2023-03-11T14:00:00Z") <= start < pd.Timestamp("2023-03-13T00:00:00Z"):
        return {"classification": "rejected",
                "reason": "Binance relisted USDC/USDT mid-SVB episode; use the direct Bitstamp case figure, not this truncated record, for timing",
                "confirmation_end_utc": pd.NaT}
    # Terminal episodes need no multi-year API request; the direct check is a 14-day diagnostic window.
    end = event["end_utc"] if event["end_utc"] is not None else min(start + pd.Timedelta(days=14), relative.index[-1])
    try:
        ref = coinbase_usdt_usd(start - pd.Timedelta(hours=24), end + pd.Timedelta(hours=12))
    except (OSError, RuntimeError, ValueError) as exc:
        return {"classification": "relative-price candidate", "reason": f"USDT/USD reference unavailable: {exc}",
                "confirmation_end_utc": pd.NaT}
    direct = pd.concat([relative.rename("relative"), ref], axis=1).dropna()
    if direct.empty or start not in direct.index:
        return {"classification": "relative-price candidate", "reason": "no direct USDT/USD candle at the candidate start",
                "confirmation_end_utc": pd.NaT}
    usd = direct.relative * direct.usdt_usd
    direct_events = detect(usd)
    hits = [x for x in direct_events if x["start_utc"] <= end and (x["end_utc"] is None or x["end_utc"] >= start)]
    if not hits:
        return {"classification": "rejected", "reason": "relative movement disappears after direct USDT/USD adjustment",
                "confirmation_end_utc": direct.index.max()}
    confirmed = hits[0]
    return {"classification": "USD-confirmed", "reason": "direct USDT/USD adjustment available",
            "confirmation_end_utc": direct.index.max(), **confirmed}


def quality_rejections(pair: str, candles: pd.DataFrame) -> list[dict]:
    """Log observations excluded by the frozen persistence and artefact rules."""
    price = candles.set_index("timestamp_utc").close.astype(float)
    outside = price.sub(1).abs() > 0.005
    rejected: list[dict] = []
    run_start = 0
    values = outside.to_numpy()
    for i in range(1, len(values) + 1):
        if i == len(values) or values[i] != values[run_start]:
            if values[run_start] and i - run_start == 1:
                stamp = price.index[run_start]
                rejected.append({"start_utc": stamp, "end_utc": stamp, "censored": False,
                                 "max_deviation_bps": round(float(abs(price.iloc[run_start] - 1) * 1e4), 1),
                                 "min_price": float(price.iloc[run_start]), "max_price": float(price.iloc[run_start]),
                                 "reason": "single hourly deviation: excluded by the two-consecutive-hour persistence rule"})
            run_start = i
    gaps = candles.timestamp_utc.diff() > pd.Timedelta(hours=24)
    for _, row in candles.loc[gaps].iterrows():
        if row.low < 0.995 or row.high > 1.005:
            rejected.append({"start_utc": row.timestamp_utc, "end_utc": row.timestamp_utc, "censored": False,
                             "max_deviation_bps": round(float(max(1 - row.low, row.high - 1) * 1e4), 1),
                             "min_price": float(row.low), "max_price": float(row.high),
                             "reason": "first candle after a >24-hour gap: excluded as a listing/relisting artefact"})
    return rejected


def scan() -> pd.DataFrame:
    rows = []
    for pair in PAIRS:
        candles = read_pair(pair)
        relative = candles.set_index("timestamp_utc").close.astype(float)
        candidates = detect(relative)
        print(f"{pair}: {len(candidates)} relative-price candidates ({candles.timestamp_utc.min():%Y-%m-%d} to {candles.timestamp_utc.max():%Y-%m-%d})")
        for number, event in enumerate(candidates, start=1):
            assessed = direct_confirmation(pair, relative, event)
            chosen = assessed if assessed.get("classification") == "USD-confirmed" else event
            rows.append({"event_id": f"P1-07-{pair}-{number:02d}", "pair": pair,
                         "price_frequency": "1h", "screen_price": "Binance close, stablecoin/USDT",
                         "classification": assessed["classification"], "reason": assessed["reason"],
                         "start_utc": chosen["start_utc"], "end_utc": chosen["end_utc"],
                         "confirmation_end_utc": assessed.get("confirmation_end_utc", pd.NaT),
                         "censored": chosen["censored"], "max_deviation_bps": round(chosen["max_deviation_bps"], 1),
                         "min_price": chosen["min_price"], "max_price": chosen["max_price"],
                         "merged_episodes": chosen.get("merged_episodes", 1),
                         "coverage_start_utc": candles.timestamp_utc.min(), "coverage_end_utc": candles.timestamp_utc.max()})
        for number, rejection in enumerate(quality_rejections(pair, candles), start=1):
            rows.append({"event_id": f"P1-07-{pair}-REJECT-{number:02d}", "pair": pair,
                         "price_frequency": "1h", "screen_price": "Binance close/high/low, stablecoin/USDT",
                         "classification": "rejected", "reason": rejection["reason"],
                         "start_utc": rejection["start_utc"], "end_utc": rejection["end_utc"],
                         "confirmation_end_utc": pd.NaT, "censored": rejection["censored"],
                         "max_deviation_bps": rejection["max_deviation_bps"], "min_price": rejection["min_price"],
                         "max_price": rejection["max_price"], "merged_episodes": 1,
                         "coverage_start_utc": candles.timestamp_utc.min(), "coverage_end_utc": candles.timestamp_utc.max()})
    frame = pd.DataFrame(rows).sort_values(["pair", "start_utc"]).reset_index(drop=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(OUT, index=False, date_format="%Y-%m-%dT%H:%M:%SZ")
    return frame


def bitstamp_usdc_usd() -> pd.DataFrame:
    """Fetch and freeze the direct-dollar SVB-weekend series used in the figure."""
    start, end = pd.Timestamp("2023-03-10T00:00:00Z"), pd.Timestamp("2023-03-14T23:00:00Z")
    url = f"https://www.bitstamp.net/api/v2/ohlc/usdcusd/?step=3600&limit=1000&start={int(start.timestamp())}"
    data = json.loads(get(url))["data"]["ohlc"]
    frame = pd.DataFrame(data)
    frame["timestamp_utc"] = pd.to_datetime(frame.timestamp.astype(int), unit="s", utc=True)
    frame = frame[(frame.timestamp_utc >= start) & (frame.timestamp_utc <= end)].copy()
    for col in ["open", "high", "low", "close", "volume"]:
        frame[col] = frame[col].astype(float)
    frame = frame.sort_values("timestamp_utc")[["timestamp_utc", "open", "high", "low", "close", "volume"]]
    target = RAW / "bitstamp" / "USDC-USD-1h_2023-03-10_to_2023-03-14.csv"
    target.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(target, index=False, date_format="%Y-%m-%dT%H:%M:%SZ")
    return frame


def draw_svb(frame: pd.DataFrame) -> None:
    """Draw USDC/USD with the US bank-weekend closure window clearly labelled."""
    FIG.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(11, 5.8), layout="constrained")
    ax.plot(frame.timestamp_utc, frame.close, color="#1769aa", lw=2.1, label="USDC/USD — fechamento horário")
    ax.fill_between(frame.timestamp_utc, frame.low, frame.high, color="#1769aa", alpha=.16,
                    label="mínimo–máximo na hora")
    bank_close = pd.Timestamp("2023-03-10T21:00:00Z")  # Fri 16:00 New York (EST)
    bank_open = pd.Timestamp("2023-03-13T13:30:00Z")   # Mon 09:30 New York (EDT)
    ax.axvspan(bank_close, bank_open, color="#f4b183", alpha=.34, label="fim de semana bancário dos EUA (aprox.)")
    ax.axhline(1, color="#333333", lw=1, ls="--", label="paridade: US$ 1")
    low = frame.loc[frame.low.idxmin()]
    ax.scatter(low.timestamp_utc, low.low, color="#b2182b", zorder=3)
    ax.annotate(f"mínimo intrahora: US${low.low:.3f}\n{low.timestamp_utc:%d %b %H:%M UTC}",
                xy=(low.timestamp_utc, low.low), xytext=(22, -37), textcoords="offset points",
                arrowprops={"arrowstyle": "-", "color": "#555555"}, fontsize=9)
    ax.set(title="USDC perdeu a paridade enquanto os bancos dos EUA estavam fechados",
           xlabel="Hora (UTC)", ylabel="US$ por USDC", ylim=(0.76, 1.02))
    ax.xaxis.set_major_locator(mdates.DayLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
    ax.grid(axis="y", color="#d9d9d9", lw=.7)
    ax.legend(loc="lower right", frameon=True, fontsize=8)
    fig.text(.01, .01, "Fonte: Bitstamp OHLC 1h (USDC/USD), recuperado em 31 out. 2026. "
             "A faixa indica o fim de semana bancário dos EUA; não mede diretamente a disponibilidade de resgate da Circle.", fontsize=8)
    fig.savefig(FIG, dpi=200, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="P1-07 stablecoin depeg detector")
    parser.add_argument("--download-only", action="store_true", help="fetch missing Binance archives, then stop")
    parser.add_argument("--pairs", nargs="+", choices=PAIRS, help="pair subset for --download-only")
    args = parser.parse_args()
    selected = tuple(args.pairs) if args.pairs else PAIRS
    download_binance(selected)
    if args.download_only:
        return
    if selected != PAIRS:
        raise SystemExit("analysis requires the complete pre-specified pair universe; omit --pairs")
    events = scan()
    svb = bitstamp_usdc_usd()
    draw_svb(svb)
    confirmed = (events.classification == "USD-confirmed").sum()
    print(f"wrote {OUT.relative_to(ROOT)}: {len(events)} screened candidates; {confirmed} USD-confirmed events")
    print(f"wrote {FIG.relative_to(ROOT)}; Bitstamp rows={len(svb)}, low={svb.low.min():.3f}")


if __name__ == "__main__":
    main()
