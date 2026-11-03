r"""P3-20: predictions registered before the data (tasks/P3-20-live-predictions.md, registered in 9a522e9).
E1 = Res. BCB 574 reporting from 3 Nov 2026; E2 = Res. BCB 589 art. 91 ban from 6 Nov 2026.

Part 1 (S2, `reference`): reference distributions from frozen data up to 30 Oct 2026, written BEFORE any November
data is downloaded. Part 2 (S4/S6, `readout`) is added after the download.

Series   Binance  = P1-02 premium_bps (USDT/BRL in the PTAX window over PTAX, USDT/USD-adjusted), the primary outcome
         Foxbit, Mercado Bitcoin = same window premium, built as in scripts/p2_05_checks.py (copied, not imported)
         gap_foxbit, gap_mb = venue premium minus Binance premium
Stats    with t0 a clean date (position i): S1 = p[i+1] - p[i]; S2 = mean p[i+1..i+2] - mean p[i-20..i-1];
         S20 = mean p[i+1..i+20] - mean p[i-20..i-1]  (the stat() of scripts/p4_04_inference.py, copied)
Clean    the P2-03 / P4-04 rule, copied: every PTAX day within 20 PTAX days of a date in P1-04_events_brazil.csv is
         out; t0 must have 20 PTAX days before and after inside the data (so all windows end by 30 Oct 2026)
Missing  rule fixed in S2, before any November data: a pre-window needs >= 15 of its 20 days; S1 and S2 need every
         post day; S20 needs >= 15 of 20 post days. Otherwise that date is dropped for that series
Inputs   data/processed/P1-02_premium_daily.csv, P1-02_premium_hourly.csv, P1-04_events_brazil.csv,
         data/raw/foxbit/USDTBRL-1h.csv, data/raw/mercadobitcoin/USDT-BRL-1h.csv  (all frozen to 30 Oct 2026)
Outputs  results/tables/P3-20_reference.csv          one row per series x statistic: n, 2.5% / 97.5% band, half-width
         results/tables/P3-20_reference_values.csv   every clean-date value (for p-values at readout)
Run      python scripts/p3_20_live.py reference
"""
import sys
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW, PROC, TAB = ROOT / "data/raw", ROOT / "data/processed", ROOT / "results/tables"
WINDOW_UTC = [13, 14, 15, 16]
FROZEN_END = pd.Timestamp("2026-10-30")


def venue_premiums(d, h, f, m):
    """Daily window premium per venue, bps (method of p2_05_checks.py S1)."""
    out = {"Binance": d.premium_bps}
    for name, s in {"Foxbit": f.open, "Mercado Bitcoin": m.o}.items():
        w = (s / h.usdtusd_open_usd.reindex(s.index)).dropna()
        w = w[w.index.hour.isin(WINDOW_UTC)]
        out[name] = ((w.groupby(w.index.normalize()).mean() / d.ptax_sell_brl_per_usd) - 1).mul(1e4).reindex(d.index)
    v = pd.DataFrame(out)
    v["gap_foxbit"] = v["Foxbit"] - v["Binance"]
    v["gap_mb"] = v["Mercado Bitcoin"] - v["Binance"]
    return v


def load():
    d = pd.read_csv(PROC / "P1-02_premium_daily.csv", parse_dates=["date_brt"], index_col="date_brt").sort_index()
    h = pd.read_csv(PROC / "P1-02_premium_hourly.csv", parse_dates=["time_utc"], index_col="time_utc")
    f = pd.read_csv(RAW / "foxbit/USDTBRL-1h.csv")
    f = f[f.volume_usdt > 0].set_index(pd.to_datetime(f[f.volume_usdt > 0].open_time_ms, unit="ms"))
    m = pd.read_csv(RAW / "mercadobitcoin/USDT-BRL-1h.csv")
    m = m.set_index(pd.to_datetime(m.t, unit="s"))
    return d, h, f, m


def clean_positions(index):
    ev = pd.read_csv(PROC / "P1-04_events_brazil.csv")
    mapped = set()
    for _, r in ev.iterrows():
        for col in ["date_announced", "date_effective"]:
            v = str(r[col]).strip()
            if v not in ("N/A", "nan"):
                sub = index[index >= pd.Timestamp(v)]
                if len(sub):
                    mapped.add(index.get_loc(sub[0]))
    black = {q for e in mapped for q in range(max(0, e - 20), min(len(index), e + 21))}
    return [i for i in range(20, len(index) - 20) if i not in black]


def stat(p, i, name):
    pre = p.iloc[i - 20:i]
    if pre.count() < 15:
        return np.nan
    if name == "S1":
        return p.iloc[i + 1] - p.iloc[i]
    post = p.iloc[i + 1:i + 3] if name == "S2" else p.iloc[i + 1:i + 21]
    if (name == "S2" and post.count() < 2) or (name == "S20" and post.count() < 15):
        return np.nan
    return post.mean() - pre.mean()


def reference():
    d, h, f, m = load()
    assert d.index.max() == FROZEN_END, "reference must use the 30 Oct 2026 freeze only"
    v = venue_premiums(d, h, f, m)
    clean = clean_positions(v.index)
    rows, vals = [], []
    for series in v.columns:
        for name in ["S1", "S2", "S20"]:
            s = pd.Series({v.index[i]: stat(v[series], i, name) for i in clean}).dropna()
            lo, hi = s.quantile(0.025), s.quantile(0.975)
            rows.append(dict(series=series, statistic=name, n=len(s), first=s.index.min().date(),
                             last=s.index.max().date(), band_lo_bps=round(lo, 1), band_hi_bps=round(hi, 1),
                             half_width_bps=round(max(-lo, hi), 1), sd_bps=round(s.std(), 1)))
            vals.append(pd.DataFrame({"series": series, "statistic": name, "t0": s.index.date, "value_bps": s.values}))
    ref = pd.DataFrame(rows)
    ref.to_csv(TAB / "P3-20_reference.csv", index=False)
    pd.concat(vals).round(3).to_csv(TAB / "P3-20_reference_values.csv", index=False)
    print(f"clean t0 dates: {len(clean)} ({v.index[clean[0]].date()} .. {v.index[clean[-1]].date()})")
    print(ref.to_string(index=False))


if __name__ == "__main__":
    {"reference": reference}[sys.argv[1] if len(sys.argv) > 1 else "reference"]()
