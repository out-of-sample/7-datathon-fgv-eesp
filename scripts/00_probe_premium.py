r"""Day-0 probe: USDT/BRL premium over PTAX (run on 30 Oct 2026). Exploratory, not a final result.

Inputs
  data/raw/binance/USDTBRL/*.csv  unzipped monthly 1h klines from data.binance.vision
  data/raw/bcb/ptax.json          BCB Olinda CotacaoDolarPeriodo, 01-10-2020 .. 10-30-2026
  data/raw/binance/USDCUSDT/*.csv optional; same download as USDTBRL with the pair name changed
Outputs
  printed tables: premium by year and month, mean premium 30 days before/after dated events,
  weekend test (crypto weekend move vs Friday->Monday PTAX move), USDC/USDT deviation (if given)

Download (bash):
  mkdir -p data/raw/binance/USDTBRL data/raw/bcb && cd data/raw/binance/USDTBRL
  curl -s "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?prefix=data/spot/monthly/klines/USDTBRL/1h/&delimiter=/" \
    | grep -o '<Key>[^<]*zip</Key>' | sed 's/<[^>]*>//g' | xargs -I{} curl -sO "https://data.binance.vision/{}"
  for z in *.zip; do unzip -oq "$z"; done; cd -
  curl -s -o data/raw/bcb/ptax.json "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='10-01-2020'&@dataFinalCotacao='10-30-2026'&\$format=json&\$top=10000"
Run:
  python scripts/00_probe_premium.py [binance_dir] [ptax_json] [usdcusdt_dir]

Known simplifications (fix in the main pipeline): one venue; no USDT/USD adjustment (USDC/USDT moved
<= ~7 bps per month in 2025-26); PTAX timing approximated by the mean of hourly opens 13-16 UTC.
"""
import glob, json, sys
import pandas as pd

kdir = sys.argv[1] if len(sys.argv) > 1 else "data/raw/binance/USDTBRL"
pfile = sys.argv[2] if len(sys.argv) > 2 else "data/raw/bcb/ptax.json"

k = pd.concat(pd.read_csv(f, header=None, usecols=[0, 1, 2, 3, 4]) for f in glob.glob(f"{kdir}/*.csv"))
k.columns = ["t", "o", "h", "l", "c"]
k["t"] = pd.to_datetime(k.t.where(k.t < 1e14, k.t // 1000), unit="ms")  # files from 2025 use microseconds
k = k.set_index("t").sort_index()

p = pd.DataFrame(json.load(open(pfile))["value"])
p["date"] = pd.to_datetime(p.dataHoraCotacao.str[:10])
p = p.groupby("date").cotacaoVenda.last()

# PTAX averages four windows 10h-13h Brasília (13-16 UTC); match with USDTBRL hourly opens in that window
win = k[k.index.hour.isin([13, 14, 15, 16])].o
u = win.groupby(win.index.normalize()).mean()
prem = (u.reindex(p.index) / p - 1).dropna() * 1e4  # bps

y = prem.groupby(prem.index.year)
print(pd.DataFrame({"n": y.size(), "mean": y.mean(), "p10": y.quantile(.1), "p50": y.median(),
                    "p90": y.quantile(.9)}).round(1))
print(prem.groupby(prem.index.to_period("M")).mean().round(1)["2025-01":].to_string())
print("median hourly high-low range (bps):", ((k.h - k.l) / k.c * 1e4).groupby(k.index.year).median().round(1).to_dict())

events = {"2025-05-22": "IOF decree [verify]", "2025-11-10": "BCB Res. 519-521 published",
          "2026-02-02": "BCB Res. 521 in force", "2026-05-04": "reporting obligation [verify]",
          "2026-06-23": "BCB notice to banks/funds [verify]"}
for d, name in events.items():
    e = pd.Timestamp(d)
    pre, post = prem[e - pd.Timedelta(days=30):e - pd.Timedelta(days=1)], prem[e + pd.Timedelta(days=1):e + pd.Timedelta(days=30)]
    print(f"{d} {name:35s} pre30 {pre.mean():6.1f}  post30 {post.mean():6.1f}  (n {len(pre)}/{len(post)})")
print(prem["2026-06-15":"2026-07-03"].round(0).to_string())

# Weekend: does the USDTBRL move from Friday 16 UTC to Sunday 23 UTC anticipate the Friday->Monday PTAX move?
rows = []
for f in p.index[p.index.dayofweek == 4]:
    mon = f + pd.Timedelta(days=3)
    if mon in p.index:
        a, b = k.c.asof(f + pd.Timedelta(hours=16)), k.c.asof(f + pd.Timedelta(days=2, hours=23))
        rows.append({"crypto": (b / a - 1) * 1e4, "ptax": (p[mon] / p[f] - 1) * 1e4})
w = pd.DataFrame(rows).dropna()
print(f"weekends {len(w)}  corr {w.corr().iloc[0, 1]:.2f}  slope {w.cov().iloc[0, 1] / w.crypto.var():.2f}")

# USDT's own dollar price, proxied by USDC/USDT (assumes USDC = US$ 1)
if len(sys.argv) > 3:
    uc = pd.concat(pd.read_csv(f, header=None, usecols=[0, 4]) for f in glob.glob(f"{sys.argv[3]}/*.csv"))
    uc.columns = ["t", "c"]
    uc["t"] = pd.to_datetime(uc.t.where(uc.t < 1e14, uc.t // 1000), unit="ms")
    s = uc.set_index("t").c.sort_index()
    dev = (s - 1) * 1e4
    print("USDC/USDT deviation (bps), monthly mean from 2025-07:")
    print(dev.groupby(dev.index.to_period("M")).mean().round(1)["2025-07":].to_string())
    print("lowest hourly USDC/USDT close:", s.min(), "at", s.idxmin())
