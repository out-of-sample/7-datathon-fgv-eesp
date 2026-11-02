r"""P3-05 S1: Build frozen agentic data bundle and checksum manifest.

Purpose:
  Copies raw price files (USDT/BRL, USDC/USDT, BUSD/USDT, BCB PTAX) and neutral
  provider documentation into data/agentic_bundle/, with zero mention of research
  findings or hypotheses. Computes SHA256SUMS and mirrors it to results/agentic/.

Inputs:
  data/raw/binance/USDTBRL/*.zip
  data/raw/binance/USDCUSDT/*.zip
  data/raw/binance/BUSDUSDT/*.zip
  data/raw/bcb/ptax.json

Outputs:
  data/agentic_bundle/data/binance/USDTBRL/*.zip
  data/agentic_bundle/data/binance/USDCUSDT/*.zip
  data/agentic_bundle/data/binance/BUSDUSDT/*.zip
  data/agentic_bundle/data/bcb/ptax.json
  data/agentic_bundle/docs/DATA_README.txt
  data/agentic_bundle/DATA_README.txt
  data/agentic_bundle/SHA256SUMS
  results/agentic/bundle_SHA256SUMS.txt

Run:
  py scripts/p3_05_build_bundle.py
"""
import hashlib
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
BUNDLE_DIR = ROOT / "data" / "agentic_bundle"
RESULTS_AGENTIC_DIR = ROOT / "results" / "agentic"

DATA_README_CONTENT = """Provider Documentation & Data Specifications

1. Binance Kline / Candlestick Data (Hourly)
============================================
Source: Binance public historical market data archive (data.binance.vision).
Files: Headerless CSV files packaged inside .zip archives.
Pairs provided:
  - USDTBRL: Tether USD traded against Brazilian Real (spot market).
  - USDCUSDT: USD Coin traded against Tether USD (spot market).
    Note: USDC/USDT spot pair trading was temporarily delisted on Binance spot
    between late September 2022 and mid-March 2023.
  - BUSDUSDT: Binance USD traded against Tether USD (spot market).

Column Format (12 columns per row, comma-separated, headerless):
  Column 0:  Open time (Unix epoch timestamp, UTC)
  Column 1:  Open price (numeric)
  Column 2:  High price (numeric)
  Column 3:  Low price (numeric)
  Column 4:  Close price (numeric)
  Column 5:  Volume (base asset volume, numeric)
  Column 6:  Close time (Unix epoch timestamp, UTC)
  Column 7:  Quote asset volume (numeric)
  Column 8:  Number of trades (integer)
  Column 9:  Taker buy base asset volume (numeric)
  Column 10: Taker buy quote asset volume (numeric)
  Column 11: Ignore / Unused

Timestamp units:
  - Historical klines through December 2024 use millisecond timestamps (13 digits).
  - Starting in January 2025 (2025-01 files), Binance switched timestamp serialization
    to microseconds (16 digits).
  - To convert to standard milliseconds or unified datetime: if timestamp >= 1e14,
    divide by 1000. All timestamps are recorded in UTC.

2. Banco Central do Brasil (BCB) - PTAX Exchange Rates
======================================================
Source: Banco Central do Brasil (BCB) Olinda API (Servico de Cotacoes de Moedas - PTAX).
Endpoint: CotacaoDolarPeriodo.
File: data/bcb/ptax.json

Format:
  JSON document containing an array of daily records under the key "value":
  {
    "value": [
      {
        "cotacaoCompra": 5.xxxx,
        "cotacaoVenda": 5.xxxx,
        "dataHoraCotacao": "YYYY-MM-DD HH:MM:SS.fff"
      },
      ...
    ]
  }

Field Definitions:
  - cotacaoCompra: Official PTAX purchase exchange rate (BRL per USD).
  - cotacaoVenda: Official PTAX sales exchange rate (BRL per USD).
  - dataHoraCotacao: Timestamp of official quotation publication in local Brasilia time
    (BRT, UTC-3) in format "YYYY-MM-DD HH:MM:SS.fff".

Notes on PTAX:
  - PTAX is calculated and published on Brazilian banking business days.
  - The closing PTAX rate published by BCB is an arithmetic average of four intraday
    consultation windows (10:00-10:10, 11:00-11:10, 12:00-12:10, 13:00-13:10 Brasilia time,
    corresponding to 13:00-13:10, 14:00-14:10, 15:00-15:10, 16:00-16:10 UTC).
  - Brasilia local time has observed UTC-3 continuously with no daylight saving time since 2019.
"""


def sha256_file(filepath: Path) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(1024 * 1024):
            h.update(chunk)
    return h.hexdigest()


def main():
    print(f"Building agentic bundle in: {BUNDLE_DIR}")
    if BUNDLE_DIR.exists():
        print(f"Cleaning existing bundle directory...")
        shutil.rmtree(BUNDLE_DIR)
    BUNDLE_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_AGENTIC_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Copy raw binance pairs
    binance_pairs = ["USDTBRL", "USDCUSDT", "BUSDUSDT"]
    total_copied = 0

    for pair in binance_pairs:
        src_dir = RAW_DIR / "binance" / pair
        dest_dir = BUNDLE_DIR / "data" / "binance" / pair
        dest_dir.mkdir(parents=True, exist_ok=True)
        zips = sorted(src_dir.glob("*.zip"))
        if not zips:
            raise FileNotFoundError(f"No zip files found in {src_dir}")
        for z in zips:
            shutil.copy2(z, dest_dir / z.name)
            total_copied += 1
        print(f"  Copied {len(zips)} zips for {pair}")

    # 2. Copy BCB PTAX
    src_ptax = RAW_DIR / "bcb" / "ptax.json"
    if not src_ptax.exists():
        raise FileNotFoundError(f"Missing {src_ptax}")
    dest_bcb = BUNDLE_DIR / "data" / "bcb"
    dest_bcb.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_ptax, dest_bcb / "ptax.json")
    total_copied += 1
    print("  Copied BCB ptax.json")

    # 3. Write DATA_README.txt
    docs_dir = BUNDLE_DIR / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    readme_docs = docs_dir / "DATA_README.txt"
    readme_docs.write_text(DATA_README_CONTENT, encoding="utf-8")
    readme_root = BUNDLE_DIR / "DATA_README.txt"
    readme_root.write_text(DATA_README_CONTENT, encoding="utf-8")
    total_copied += 2
    print("  Created neutral DATA_README.txt in docs/ and bundle root")

    # 4. Generate SHA256SUMS
    print("Calculating SHA256 checksums...")
    manifest_lines = []
    bundle_files = sorted(
        [p for p in BUNDLE_DIR.rglob("*") if p.is_file() and p.name != "SHA256SUMS"],
        key=lambda p: p.relative_to(BUNDLE_DIR).as_posix()
    )

    for p in bundle_files:
        rel_path = p.relative_to(BUNDLE_DIR).as_posix()
        digest = sha256_file(p)
        manifest_lines.append(f"{digest}  {rel_path}")

    manifest_content = "\n".join(manifest_lines) + "\n"

    manifest_dest1 = BUNDLE_DIR / "SHA256SUMS"
    manifest_dest1.write_text(manifest_content, encoding="utf-8")

    manifest_dest2 = RESULTS_AGENTIC_DIR / "bundle_SHA256SUMS.txt"
    manifest_dest2.write_text(manifest_content, encoding="utf-8")

    total_bytes = sum(p.stat().st_size for p in bundle_files)
    print(f"\nBundle build complete:")
    print(f"  Total files in bundle: {len(bundle_files)} (plus SHA256SUMS)")
    print(f"  Total raw size: {total_bytes / (1024 * 1024):.2f} MB")
    print(f"  Bundle SHA256SUMS written to: {manifest_dest1}")
    print(f"  Manifest copy written to:     {manifest_dest2}")


if __name__ == "__main__":
    main()
