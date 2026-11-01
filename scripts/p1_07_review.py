"""P1-07 review: checks on Nattan's depeg events (v1) and the SVB-weekend series.

Inputs:  data/processed/P1-07_depeg_events.csv and data/raw/bitstamp/ (python scripts/p1_07_depeg.py),
         data/raw/binance/<stablecoin>USDT/ (same script)
Outputs: printed only (numbers quoted in tasks/P1-07-depeg-detector.md -> Review)
Run:     .venv/bin/python scripts/p1_07_review.py
Checks:  1 direction of each USD-confirmed event (below $1, above $1, both)
         2 censored events: did the Binance (stablecoin/USDT) episode recover?
         3 events of different pairs starting within 48 h of each other (shared shocks)
         4 the first USTC candles (listing price)
         5 SVB weekend: intra-hour low vs lowest hourly close; closes around the Sunday announcement and the Monday open
"""
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import p1_07_depeg as v1  # reuse v1's reader and detector, so check 2 uses exactly v1's rule

e = pd.read_csv(ROOT / "data/processed/P1-07_depeg_events.csv", parse_dates=["start_utc", "end_utc", "coverage_end_utc"])
c = e[e.classification == "USD-confirmed"].copy()

# 1 Direction: below = min price under 0.995, above = max price over 1.005
below, above = c.min_price < 0.995, c.max_price > 1.005
c["direction"] = "both"
c.loc[below & ~above, "direction"], c.loc[above & ~below, "direction"] = "below", "above"
print(f"1. {len(c)} USD-confirmed events by direction:", c.direction.value_counts().to_dict())
print(c[["pair", "start_utc", "end_utc", "direction", "censored", "max_deviation_bps", "min_price", "max_price"]]
      .to_string(index=False))

# 2 Censored events vs the relative (Binance) episode
print(f"\n2. {c.censored.sum()} censored USD-confirmed events; relative episode end on Binance:")
rel = {p: v1.detect(v1.read_pair(p).set_index("timestamp_utc").close.astype(float)) for p in c.pair.unique()}
for _, r in c[c.censored].iterrows():
    hit = [x for x in rel[r.pair] if x["start_utc"] <= r.start_utc + pd.Timedelta(days=14)
           and (x["end_utc"] is None or x["end_utc"] >= r.start_utc)]
    print(f"   {r.pair:10} start {r.start_utc:%Y-%m-%d %H}h  relative end {hit[0]['end_utc'] if hit else '-'}"
          f"  pair data ends {r.coverage_end_utc:%Y-%m-%d}")

# 3 Shared shocks
print("\n3. Events of different pairs starting within 48 h:")
s = c.sort_values("start_utc").reset_index(drop=True)
for i in range(1, len(s)):
    if s.start_utc[i] - s.start_utc[i - 1] < pd.Timedelta(hours=48) and s.pair[i] != s.pair[i - 1]:
        print(f"   {s.pair[i - 1]} {s.start_utc[i - 1]:%Y-%m-%d %H}h | {s.pair[i]} {s.start_utc[i]:%Y-%m-%d %H}h")
b, f = (v1.read_pair(p).set_index("timestamp_utc").close for p in ("BUSDUSDT", "FDUSDUSDT"))
print("   13 Dec 2023, Binance closes:\n", pd.DataFrame({"BUSD/USDT": b, "FDUSD/USDT": f})
      ["2023-12-13 04:00":"2023-12-13 08:00"].to_string())

# 4 USTC listing
print("\n4. First USTC/USDT candles:\n", v1.read_pair("USTCUSDT").head(3)[["timestamp_utc", "open", "close"]]
      .to_string(index=False))

# 5 SVB weekend (Bitstamp USDC/USD)
x = pd.read_csv(ROOT / "data/raw/bitstamp/USDC-USD-1h_2023-03-10_to_2023-03-14.csv", parse_dates=["timestamp_utc"],
                index_col="timestamp_utc")
print(f"\n5. Bitstamp USDC/USD: intra-hour low {x.low.min():.3f} at {x.low.idxmin():%d %b %H}h UTC; lowest hourly "
      f"close {x.close.min():.3f} at {x.close.idxmin():%d %b %H}h; hours closing below 0.90: {(x.close < 0.90).sum()}")
print(x.close.loc[["2023-03-12 21:00", "2023-03-12 22:00", "2023-03-13 12:00", "2023-03-13 13:00", "2023-03-13 14:00"]]
      .to_string())
