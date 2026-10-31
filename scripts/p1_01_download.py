r"""P1-01: download and freeze the raw price data, then audit its coverage. Safe to re-run.

Sources
  Binance public archive  https://data.binance.vision  (spot 1h klines; listing via
                          https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?prefix=...&delimiter=/)
  BCB Olinda PTAX API     https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo
Outputs (frozen at 30 Oct 2026)
  data/raw/binance/<PAIR>/<PAIR>-1h-YYYY-MM.zip     monthly files up to 2026-09, zips exactly as published
  data/raw/binance/<PAIR>/<PAIR>-1h-YYYY-MM-DD.zip  daily files 2026-10-01 .. 2026-10-30 (no monthly file yet)
  data/raw/bcb/ptax.json                            PTAX closing rate, 01 Oct 2020 .. 30 Oct 2026
  results/tables/P1-01_coverage.csv                 coverage audit per pair (also printed)
Run (from the repo root)
  python scripts/p1_01_download.py [PAIR ...]       default pairs below; existing files are skipped
  sha256sum -c data/raw/SHA256SUMS                  every file must say OK

Each zip holds one headerless CSV: open_time, open, high, low, close, volume, close_time, ... (UTC).
open_time is in milliseconds up to 2024 and in microseconds from 2025. pandas reads the zips directly.
"""
import hashlib, json, re, sys, time, urllib.request
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data/raw"
PAIRS = sys.argv[1:] or ["USDTBRL", "USDCUSDT", "BTCBRL", "BTCUSDT"]
LAST_MONTH, LAST_DAY = "2026-09", "2026-10-30"  # freeze cutoff; a later monthly 2026-10 file would duplicate the dailies
BUCKET = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision"
PTAX_URL = ("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo("
            "dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='10-01-2020'"
            "&@dataFinalCotacao='10-30-2026'&$format=json&$top=10000")


def get(url, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                return r.read()
        except OSError:
            if i == tries - 1:
                raise
            time.sleep(2 ** i)


def keys(prefix):
    x = get(f"{BUCKET}?prefix={prefix}&delimiter=/").decode()
    if "<IsTruncated>false</IsTruncated>" not in x:
        raise SystemExit(f"listing truncated or failed: {prefix}")
    return re.findall(r"<Key>([^<]*\.zip)</Key>", x)


# 1. Binance klines, each file checked against Binance's own .CHECKSUM before it is kept
for pair in PAIRS:
    out = RAW / "binance" / pair
    out.mkdir(parents=True, exist_ok=True)
    stamp = lambda k: k.rsplit("-1h-", 1)[1][:-4]  # "2026-09" or "2026-10-30"
    wanted = [k for k in keys(f"data/spot/monthly/klines/{pair}/1h/") if stamp(k) <= LAST_MONTH]
    wanted += [k for k in keys(f"data/spot/daily/klines/{pair}/1h/{pair}-1h-2026-10") if stamp(k) <= LAST_DAY]
    new = 0
    for k in wanted:
        f = out / k.rsplit("/", 1)[1]
        if f.exists():
            continue
        data = get(f"https://data.binance.vision/{k}")
        if hashlib.sha256(data).hexdigest() != get(f"https://data.binance.vision/{k}.CHECKSUM").split()[0].decode():
            raise SystemExit(f"checksum mismatch: {k}")
        f.with_suffix(".part").write_bytes(data)
        f.with_suffix(".part").rename(f)  # never leave a half-written zip behind
        new += 1
    print(f"{pair}: {len(wanted)} files listed, {new} downloaded")

# 2. PTAX, saved byte for byte as the API returned it
ptax = RAW / "bcb/ptax.json"
if not ptax.exists():
    data = get(PTAX_URL)
    v = json.loads(data)["value"]
    if not v or max(r["dataHoraCotacao"] for r in v)[:10] != LAST_DAY:
        raise SystemExit("PTAX response empty or does not reach the cutoff date")
    ptax.parent.mkdir(parents=True, exist_ok=True)
    ptax.write_bytes(data)

# 3. Coverage audit
rows = []
for pair in PAIRS:
    parts = []
    for f in sorted((RAW / "binance" / pair).glob("*.zip")):
        d = pd.read_csv(f, header=None, usecols=range(6))
        if not pd.api.types.is_integer_dtype(d[0]):
            raise SystemExit(f"header row or non-integer timestamp in {f.name}")
        parts.append(d.assign(file=f.name, us=d[0] >= 1e14))
    k = pd.concat(parts, ignore_index=True)
    k["t"] = pd.to_datetime(k[0].where(~k.us, k[0] // 1000), unit="ms")
    t = k.t.drop_duplicates().sort_values(ignore_index=True)
    gap = t.diff().dt.total_seconds() / 3600 - 1  # hours missing right before each row
    for i in gap[gap > 24].index:
        print(f"  {pair} gap > 24h: {t[i - 1] + pd.Timedelta(hours=1)} .. {t[i] - pd.Timedelta(hours=1)} ({gap[i]:.0f} h)")
    lo, hi = k[[1, 4]].min(axis=1), k[[1, 4]].max(axis=1)
    rows.append({"pair": pair, "files": k.file.nunique(), "rows": len(k), "first_utc": t.iloc[0], "last_utc": t.iloc[-1],
                 "missing_h": int(gap.sum()), "longest_gap_h": int(gap.max()), "longest_gap_before_utc": t[gap.idxmax()],
                 "gaps_gt24h": int((gap > 24).sum()), "dup_ts": int(k.t.duplicated().sum()),
                 "off_hour": int((k.t != k.t.dt.floor("h")).sum()),
                 "bad_ohlc": int(((k[3] > lo) | (k[2] < hi) | (k[3] <= 0)).sum()),
                 "zero_vol_pct": round(100 * (k[5] == 0).mean(), 2),
                 "last_ms_file": k[~k.us].file.max(), "first_us_file": k[k.us].file.min(),
                 "mixed_unit_files": int((k.groupby("file").us.nunique() > 1).sum())})
cov = pd.DataFrame(rows)
(ROOT / "results/tables").mkdir(parents=True, exist_ok=True)
cov.to_csv(ROOT / "results/tables/P1-01_coverage.csv", index=False)
print(cov.T.to_string())

p = pd.DataFrame(json.loads(ptax.read_bytes())["value"])
ts = pd.to_datetime(p.dataHoraCotacao)
day = ts.dt.normalize()
print(f"\nPTAX: {len(p)} rows, {day.nunique()} dates, {day.min().date()} .. {day.max().date()}, "
      f"duplicate dates {day.duplicated().sum()}, venda {p.cotacaoVenda.min()} .. {p.cotacaoVenda.max()}, "
      f"rows with venda < compra {(p.cotacaoVenda < p.cotacaoCompra).sum()}")
print("publication hour (Brasília):", ts.dt.hour.value_counts().sort_index().to_dict())
print("weekdays without PTAX (should all be holidays):",
      " ".join(x.strftime("%Y-%m-%d") for x in pd.bdate_range(day.min(), day.max()).difference(day)))
