"""Reproduce the exploratory BRLA window means from the saved Flash tables."""

import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean

BUNDLE = Path(__file__).resolve().parents[1] / "data" / "raw" / "flash-mentor-leads"
WINDOWS = {
    "baseline": ("2026-05-25", "2026-06-23"),
    "acute": ("2026-06-24", "2026-07-21"),
    "fade": ("2026-07-22", "2026-08-31"),
}

with (BUNDLE / "brla/brla_polygon_ptax_merged_daily.csv").open() as source:
    daily_close = {
        row["date"]: float(row["implied_deviation_bps"])
        for row in csv.DictReader(source)
        if row["implied_deviation_bps"]
    }

hourly = defaultdict(dict)
with (BUNDLE / "brla/brla_polygon_ptax_merged_hourly.csv").open() as source:
    for row in csv.DictReader(source):
        hour = int(row["datetime_utc"][11:13])
        if hour in (13, 14, 15, 16) and row["ptax_venda"]:
            quotes = hourly[row["date"]]
            if hour in quotes:
                raise ValueError(f"Duplicate candle: {row['datetime_utc']}")
            quotes[hour] = float(row["brla_per_usdc_open"]) / float(row["ptax_venda"])

ptax_window = {
    date: 10_000 * (mean(quotes.values()) - 1)
    for date, quotes in hourly.items()
    if len(quotes) == 4
}

for label, series in (("daily close", daily_close), ("PTAX window", ptax_window)):
    means = {}
    for window, (start, end) in WINDOWS.items():
        sample = [bps for date, bps in series.items() if start <= date <= end]
        means[window] = mean(sample)
        print(f"{label} | {window}: {means[window]:.1f} bps (n={len(sample)})")
    print(f"{label} | acute minus baseline: {means['acute'] - means['baseline']:+.1f} bps")

print(f"24 June daily close: {daily_close['2026-06-24']:.1f} bps")
start, end = WINDOWS["acute"]
print(f"Acute daily-close maximum: {max(bps for date, bps in daily_close.items() if start <= date <= end):.1f} bps")
