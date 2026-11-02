r"""P3-14: do the price moves reported in the press after the 23 Jun 2026 notice match our premium series?
Reported (docs/sources.md E-05.5 to E-05.9): about 0.1% before, 0.7% after the notice, 1-2% at the peak on 24 Jun,
0.5% on Friday 26 Jun. The press calls these a "spread" without one definition (level over the market or bid-ask),
so this is a check of size and timing, not a test.

Inputs   data/processed/P1-02_premium_daily.csv (PTAX-window premium), data/processed/P1-02_premium_hourly.csv
         (premium against the last published PTAX, so hours after 13h BRT use that day's PTAX)
Outputs  results/tables/P3-14_press_vs_series.csv  one row per calendar day 22-30 Jun 2026
Run      python scripts/p3_14_press_check.py
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
PROC, TAB = ROOT / "data/processed", ROOT / "results/tables"

d = pd.read_csv(PROC / "P1-02_premium_daily.csv", parse_dates=["date_brt"]).set_index("date_brt").premium_bps
h = pd.read_csv(PROC / "P1-02_premium_hourly.csv", parse_dates=["time_utc"]).set_index("time_utc").premium_vs_last_ptax_bps
pre = d[:"2026-06-22"].iloc[-20:].mean()
days = h["2026-06-22":"2026-06-30"].resample("D").agg(["min", "median", "max"])
days.columns = [f"hourly_{c}_bps" for c in days.columns]
days["daily_ptax_window_bps"] = d.reindex(days.index)
days.index.name = "day_utc"
TAB.mkdir(parents=True, exist_ok=True)
days.to_csv(TAB / "P3-14_press_vs_series.csv", float_format="%.1f")
print(f"pre-notice level, mean of the 20 PTAX days to 22 Jun: {pre:.1f} bps")
print(days.round(0).to_string())
