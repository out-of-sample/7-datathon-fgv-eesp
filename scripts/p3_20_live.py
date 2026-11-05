r"""P3-20: predictions registered before the data (tasks/P3-20-live-predictions.md, registered in 9a522e9).
E1 = Res. BCB 574 reporting from 3 Nov 2026; E2 = Res. BCB 589 art. 91 ban from 6 Nov 2026.

Part 1 (S2, `reference`): reference distributions from frozen data up to 30 Oct 2026, written BEFORE any November
data is downloaded.
Part 2 (S3, `download`): November pulls into data/raw/live/ (a separate folder, so the core scripts' globs never see
them; frozen files untouched). Binance USDTBRL + USDCUSDT daily zips from 31 Oct (checked against Binance's .CHECKSUM);
PTAX 1 Oct 2026 .. today; Foxbit and Mercado Bitcoin hourly from 31 Oct 00h UTC to the last complete hour, one file per
pull. Then: sha256sum data/raw/live/*/* data/raw/live/*/*/* >> data/raw/SHA256SUMS
Part 3 (S4/S6, `readout`): rebuilds the P1-02 premium from frozen + live raw data (formula copied from
scripts/p1_02_premium.py), asserts every row up to 30 Oct equals P1-02_premium_daily.csv, then S1/S2/S20 per event and
series with p = (k+1)/(n+1) against P3-20_reference_values.csv, and the non-overlapping S2 p (P4-04: stride 23, all
offsets). A statistic whose days are not all in the data yet is reported as pending.
Run      python scripts/p3_20_live.py reference | download | readout

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
         data/processed/P3-20_premium_daily.csv      readout: extended daily premium per venue and the two gaps
         results/tables/P3-20_readout.csv            readout: one row per event x series x statistic
"""
import hashlib, json, sys, time, urllib.error, urllib.request
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW, PROC, TAB = ROOT / "data/raw", ROOT / "data/processed", ROOT / "results/tables"
LIVE = RAW / "live"
WINDOW_UTC = [13, 14, 15, 16]
FROZEN_END = pd.Timestamp("2026-10-30")
EVENTS = {"E1": pd.Timestamp("2026-11-03"), "E2": pd.Timestamp("2026-11-06")}  # first day the rule is in force
FOXBIT_COLS = ["open_time_ms", "open", "high", "low", "close", "close_time_ms", "volume_usdt", "volume_brl", "trades",
               "taker_buy_volume_usdt", "taker_buy_volume_brl"]


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


def get(url, tries=3):
    req = urllib.request.Request(url, headers={"User-Agent": "out-of-sample-datathon"})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError:
            raise  # 404 = not published yet; handled by the caller
        except OSError:
            if i == tries - 1:
                raise
            time.sleep(2 ** (i + 1))


def put(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.with_suffix(".part").write_bytes(data)
    path.with_suffix(".part").rename(path)  # never leave a half-written file behind
    print("saved", path.relative_to(ROOT))


def download():
    now = pd.Timestamp.now("UTC").tz_localize(None)
    start, end = pd.Timestamp("2026-10-31"), now.floor("h") - pd.Timedelta(hours=1)  # last complete hour
    stamp = f"{end:%Y%m%dT%H}"
    for pair in ["USDTBRL", "USDCUSDT"]:  # copied from p1_01_download.py: each zip checked against Binance's checksum
        for day in pd.date_range(start, now.normalize() - pd.Timedelta(days=1)):
            name = f"{pair}-1h-{day:%Y-%m-%d}.zip"
            if (LIVE / "binance" / pair / name).exists():
                continue
            url = f"https://data.binance.vision/data/spot/daily/klines/{pair}/1h/{name}"
            try:
                data = get(url)
            except urllib.error.HTTPError as e:
                print(f"{name}: not published yet ({e.code})")
                continue
            if hashlib.sha256(data).hexdigest() != get(url + ".CHECKSUM").split()[0].decode():
                raise SystemExit(f"checksum mismatch: {name}")
            put(LIVE / "binance" / pair / name, data)
    put(LIVE / f"bcb/ptax_to_{stamp}.json", get(
        "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,"
        f"dataFinalCotacao=@dataFinalCotacao)?@dataInicial='10-01-2026'&@dataFinalCotacao='{now:%m-%d-%Y}'"
        "&$format=json&$top=10000"))
    fox, t = {}, start  # Foxbit and Mercado Bitcoin: requests copied from p1_03_second_venue.py
    while t <= end:
        u = min(t + pd.Timedelta(hours=499), end)
        r = json.loads(get(f"https://api.foxbit.com.br/rest/v3/markets/usdtbrl/candlesticks?interval=1h&limit=500"
                           f"&start_time={t:%Y-%m-%dT%H:%M}&end_time={u:%Y-%m-%dT%H:%M}"))
        if not isinstance(r, list):
            raise SystemExit(f"Foxbit error at {t}: {r}")
        fox.update((c[0], c) for c in r if t.value // 10**6 <= int(c[0]) <= u.value // 10**6)
        t = u + pd.Timedelta(hours=1)
    put(LIVE / f"foxbit/USDTBRL-1h_to_{stamp}.csv",
        pd.DataFrame([fox[k] for k in sorted(fox, key=int)], columns=FOXBIT_COLS).to_csv(index=False).encode())
    mb, t = {}, start
    while t <= end:
        u = min(t + pd.Timedelta(days=30) - pd.Timedelta(hours=1), end)
        r = json.loads(get(f"https://api.mercadobitcoin.net/api/v4/candles?symbol=USDT-BRL&resolution=1h"
                           f"&from={t.value // 10**9}&to={u.value // 10**9}"))
        if not isinstance(r, dict) or "t" not in r:
            raise SystemExit(f"Mercado Bitcoin error at {t}: {r}")
        mb.update((ts, [ts, *(r[k][i] for k in "ohlcv")]) for i, ts in enumerate(r["t"])
                  if t.value // 10**9 <= ts <= u.value // 10**9)
        t = u + pd.Timedelta(hours=1)
        time.sleep(1.1)
    put(LIVE / f"mercadobitcoin/USDT-BRL-1h_to_{stamp}.csv",
        pd.DataFrame([mb[k] for k in sorted(mb)], columns=list("tohlcv")).to_csv(index=False).encode())


def load_extended():
    """Frozen + live raw data -> (PTAX days, daily premium d, hourly h, Foxbit f, Mercado Bitcoin m)."""
    def binance(pair):  # copied from p1_02_premium.py, plus the live folder
        files = sorted((RAW / "binance" / pair).glob("*.zip")) + sorted((LIVE / "binance" / pair).glob("*.zip"))
        k = pd.concat(pd.read_csv(f, header=None, usecols=range(6)) for f in files)
        k.index = pd.to_datetime(k[0].where(k[0] < 1e14, k[0] // 1000), unit="ms")
        assert not k.index.duplicated().any(), f"{pair}: overlapping files"
        return k.sort_index().drop(columns=0).set_axis(["open", "high", "low", "close", "volume"], axis=1)

    def ptax(path):
        p = pd.DataFrame(json.loads(path.read_bytes())["value"])
        p["date_brt"] = pd.to_datetime(p.dataHoraCotacao).dt.normalize()
        return p.drop_duplicates("date_brt", keep="last").set_index("date_brt")

    p, live = ptax(RAW / "bcb/ptax.json"), sorted((LIVE / "bcb").glob("ptax_to_*.json"))
    if live:
        q = ptax(live[-1])
        both = p.index.intersection(q.index)
        assert (p.loc[both, "cotacaoVenda"] == q.loc[both, "cotacaoVenda"]).all(), "live PTAX disagrees with the freeze"
        p = pd.concat([p, q[q.index > FROZEN_END]])
    brl, usdc, busd = binance("USDTBRL"), binance("USDCUSDT"), binance("BUSDUSDT")
    h = pd.DataFrame({"usdtbrl_open_brl": brl.open})
    h["usdtusd_open_usd"] = (1 / usdc.open).reindex(h.index).fillna((1 / busd.open).reindex(h.index))
    win = h[h.index.hour.isin(WINDOW_UTC)]
    g = win.groupby(win.index.normalize())
    d = pd.DataFrame({"ptax_sell_brl_per_usd": p.cotacaoVenda, "window_hours": g.usdtbrl_open_brl.count(),
                      "usdtbrl_window_brl": g.usdtbrl_open_brl.mean(),
                      "usdtusd_window_usd": g.usdtusd_open_usd.mean()}).loc[p.index]
    d = d[d.window_hours > 0].copy()
    d["premium_bps"] = (d.usdtbrl_window_brl / (d.ptax_sell_brl_per_usd * d.usdtusd_window_usd) - 1) * 1e4
    core = pd.read_csv(PROC / "P1-02_premium_daily.csv", parse_dates=["date_brt"], index_col="date_brt").premium_bps
    old = d.premium_bps[:FROZEN_END]
    assert old.index.equals(core.index) and np.allclose(old, core, rtol=0, atol=1e-9), "does not reproduce P1-02"
    print(f"P1-02 reproduced exactly on {len(core)} days up to {FROZEN_END.date()}; extended to {d.index.max().date()}")

    def venue(frozen, pattern, read):
        k = pd.concat([read(frozen)] + [read(x) for x in sorted(LIVE.glob(pattern))])
        return k[~k.index.duplicated(keep="last")].sort_index()  # a later pull wins for the same hour
    f = venue(RAW / "foxbit/USDTBRL-1h.csv", "foxbit/*.csv", lambda x: (lambda f: f[f.volume_usdt > 0].set_index(
        pd.to_datetime(f[f.volume_usdt > 0].open_time_ms, unit="ms")))(pd.read_csv(x)))
    m = venue(RAW / "mercadobitcoin/USDT-BRL-1h.csv", "mercadobitcoin/*.csv",
              lambda x: (lambda m: m.set_index(pd.to_datetime(m.t, unit="s")))(pd.read_csv(x)))
    return p.index, d, h, f, m


def readout():
    ptax_days, d, h, f, m = load_extended()
    v = venue_premiums(d, h, f, m)
    v.round(3).to_csv(PROC / "P3-20_premium_daily.csv", index_label="date_brt")
    vals = pd.read_csv(TAB / "P3-20_reference_values.csv", parse_dates=["t0"])
    band = pd.read_csv(TAB / "P3-20_reference.csv").set_index(["series", "statistic"])
    frozen = v.index[v.index <= FROZEN_END]
    rows = []
    for ev, start in EVENTS.items():
        if ptax_days.max() < start:  # t0 is only known once the first treated PTAX day exists
            rows.append(dict(event=ev, status=f"pending: no PTAX day on or after {start.date()} yet"))
            continue
        t0 = ptax_days[ptax_days < start][-1]
        i = v.index.get_loc(t0)
        print(f"\n{ev}: t0 = {t0.date()}; premium (bps) from t0-2:\n{v.iloc[i - 2:i + 21].round(1).to_string()}")
        for series in v.columns:
            for name, need in [("S1", 1), ("S2", 2), ("S20", 20)]:
                post = v.index[i + 1:i + 1 + need]
                row = dict(event=ev, t0=t0.date(), series=series, statistic=name,
                           post_days=f"{post[0].date()}..{post[-1].date()}" if len(post) else "")
                if len(post) < need:
                    rows.append(row | dict(status=f"pending: {len(post)} of {need} post days"))
                    continue
                obs, ref = stat(v[series], i, name), vals[(vals.series == series) & (vals.statistic == name)]
                s = ref.value_bps.to_numpy()
                k = int((np.abs(s) >= abs(obs)).sum())
                row |= dict(status="observed", observed_bps=round(obs, 1), n_ref=len(s), k=k,
                            p_two_sided=round((k + 1) / (len(s) + 1), 4),
                            band_lo_bps=band.loc[(series, name), "band_lo_bps"],
                            band_hi_bps=band.loc[(series, name), "band_hi_bps"])
                if name == "S2":  # P4-04 method: non-overlapping clean dates, stride 23, every offset
                    at = dict(zip(frozen.get_indexer(ref.t0), s))
                    ps = []
                    for off in range(23):
                        kept, last = [], -10**9
                        for j in sorted(at):
                            if j >= off and j - last >= 23:
                                kept.append(j)
                                last = j
                        x = np.array([at[j] for j in kept])
                        ps.append((int((np.abs(x) >= abs(obs)).sum()) + 1) / (len(x) + 1))
                    row |= dict(p_nonoverlap_min=round(min(ps), 3), p_nonoverlap_max=round(max(ps), 3),
                                n_nonoverlap=len(x))
                rows.append(row)
    out = pd.DataFrame(rows)
    out.to_csv(TAB / "P3-20_readout.csv", index=False)
    print("\n" + out.to_string(index=False))


if __name__ == "__main__":
    {"reference": reference, "download": download, "readout": readout}[sys.argv[1] if len(sys.argv) > 1 else "reference"]()
