"""P5-04: make executable .txt copies of the scripts behind the current deck drafts.

Run from the repository root: .venv/bin/python scripts/p5_04_export.py
The exports preserve the analysis code. ROOT and the monitor's internal script
lookup change because submission/scripts/ is one directory deeper; trailing
whitespace is removed.
"""

from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "submission/scripts"

# Execution order. The union covers the figures and computed claims in both
# deck_v1_ptbr.md and deck_v2_ptbr.md as of 5 Nov 2026.
SPECS = [
    ("p1_02_premium", "Core USDT/BRL premium and PTAX alignment", "Frozen Binance, Coinbase and PTAX files in data/raw/", "data/processed/P1-02_premium_{daily,hourly}.csv"),
    ("p1_05_donors", "Comparison-currency premiums", "Frozen Binance and official FX files in data/raw/; P1-02 outputs", "data/processed/P1-05_donor_premiums_daily.csv"),
    ("p2_01_noise", "Trading-friction noise floor", "P1-02 daily and hourly CSVs", "data/processed/P2-01_noise_floor_daily.csv and P2-01 figures"),
    ("p2_02_breaks", "Blind premium break test and slide 4 chart", "P1-02 daily CSV, P2-01 noise CSV, curated P1-04 event CSV", "results/tables/P2-02_*.csv and results/figures/P2-02_premium_breaks.png"),
    ("p2_03_events", "Event estimates and placebo dates", "P1-02 daily CSV and curated P1-04 event CSV", "results/tables/P2-03_*.csv and P2-03 figure"),
    ("p2_04_synth", "Synthetic Brazil comparison and slide 6 chart", "P1-05 donor premiums CSV", "results/tables/P2-04_*.csv and results/figures/P2-04_synthetic_control.png"),
    ("p2_05_checks", "Three-venue premium checks and slide 4 detail", "P1-02 CSVs; frozen Foxbit and Mercado Bitcoin hourly files", "results/tables/P2-05_venues_daily.csv and results/figures/P2-05_hourly_22_26_jun.png"),
    ("p3_01_costs", "US$100k cost conversion and bank-route comparison", "P1-02, P2-02, P2-03, P2-05 outputs; sourced route parameters", "results/tables/P3-01_route_costs.csv and P3-01 figure"),
    ("p3_02_btc", "BTC comparison for the 23 June jump", "Frozen BTC files; P1-02 premium CSV; curated P1-04 events", "data/processed/P3-02_btc_premium_daily.csv and P3-02 outputs"),
    ("p3_03_monitor", "CUSUM monitor and its reported backtest", "Frozen raw data via exported P1-02 and P2-01 scripts", "results/tables/P3-03_backtest.csv and P3-03 figure"),
    ("p3_10_imports", "BCB stablecoin imports and slide 7 chart", "Frozen BCB SGS 29644, P1-02 CSV, P2-03 placebo draws, venue raw files", "results/tables/P3-10_*.csv and results/figures/P3-10_imports.png"),
    ("p3_11_money", "Trading-volume-weighted transfer estimate", "P1-02 CSV, P2-03 placebo draws, frozen venue raw files", "results/tables/P3-11_transfer.csv and P3-11_placebo.csv"),
    ("p3_12_rules", "Rule comparison and slide 5 chart", "P2-03 event/placebo CSVs and curated P1-04 events", "results/tables/P3-12_rules.csv and results/figures/P3-12_rules.png"),
    ("p3_13_prediction", "Res. 584 dated prediction inputs", "Frozen BCB SGS 432, P1-02, P2-03 and P3-03 outputs", "Printed prediction figures; recorded in results/tables/P3-13_prediction.md"),
    ("p3_21_who_paid", "Four illustrative user cases in deck v2", "P1-02 daily premium CSV", "results/tables/P3-21_who_paid.csv"),
    ("p4_01_robustness", "Robustness battery and slide 8 chart", "P1-02, P1-05, P2-01, P2-02, P2-04, P2-05 and P3-02 outputs", "results/tables/P4-01_robustness.csv and results/figures/P4-01_robustness_forest.png"),
    ("p4_04_inference", "Non-overlapping placebo inference shown on slides 4–5", "P1-02 daily CSV and curated P1-04 events", "results/tables/P4-04_nonoverlap.csv and P4-04_window_events.csv"),
    ("p3_20_live", "Registered November rule predictions in deck v2", "Frozen core and live raw data; P1-02 CSVs; curated P1-04 events", "results/tables/P3-20_reference*.csv and P3-20_readout.csv"),
]


def export(name: str, purpose: str, inputs: str, outputs: str) -> Path:
    source = ROOT / "scripts" / f"{name}.py"
    code = source.read_text(encoding="utf-8")
    old_root = "ROOT = Path(__file__).resolve().parent.parent"
    assert code.count(old_root) == 1, f"Unexpected ROOT definition: {source}"
    code = code.replace(old_root, "ROOT = Path(__file__).resolve().parents[2]", 1)
    if name == "p3_03_monitor":
        old_lookup = 'ROOT / "scripts" / script'
        assert code.count(old_lookup) == 1
        code = code.replace(old_lookup, 'ROOT / "submission/scripts" / script.replace(".py", ".txt")', 1)
    code = "\n".join(line.rstrip() for line in code.splitlines()) + "\n"
    digest = sha256(source.read_bytes()).hexdigest()
    header = (
        f"# Purpose: {purpose}.\n"
        f"# Inputs: {inputs}.\n"
        f"# Outputs: {outputs}.\n"
        f"# How to run: .venv/bin/python submission/scripts/{name}.txt"
        + (" reference|readout" if name == "p3_20_live" else "")
        + "\n"
        f"# Source: scripts/{name}.py (SHA-256 {digest}).\n"
        "# Run from the repository root with the frozen data/raw/ folder present.\n\n"
    )
    target = DEST / f"{name}.txt"
    target.write_text(header + code, encoding="utf-8")
    return target


def main() -> None:
    DEST.mkdir(parents=True, exist_ok=True)
    for spec in SPECS:
        target = export(*spec)
        print(target.relative_to(ROOT))


if __name__ == "__main__":
    main()
