"""P5-04: re-run exported .txt scripts in an empty workspace and compare deck figures.

Run: .venv/bin/python scripts/p5_04_reproduce.py
Copies frozen raw data, so no source or checked-in result is modified. Writes a
compact report to submission/reproduction.json.
"""

import json
import hashlib
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import matplotlib.image as mpimg
import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = [
    ("p1_02_premium",), ("p1_05_donors",), ("p2_01_noise",),
    ("p2_02_breaks",), ("p2_03_events",), ("p2_04_synth",),
    ("p2_05_checks",), ("p3_01_costs",), ("p3_02_btc",),
    ("p3_03_monitor",), ("p3_10_imports",), ("p3_11_money",),
    ("p3_12_rules",), ("p3_13_prediction",), ("p3_21_who_paid",),
    ("p4_01_robustness",), ("p4_04_inference",),
    ("p3_20_live", "reference"), ("p3_20_live", "readout"),
]
FIGURES = [
    "P2-02_premium_breaks.png", "P2-05_hourly_22_26_jun.png",
    "P3-12_rules.png", "P2-04_synthetic_control.png",
    "P3-10_imports.png", "P4-01_robustness_forest.png",
]
TABLES = ["P2-03_placebo_draws.csv", "P2-03_event_table.csv",
          "P3-11_transfer.csv", "P3-11_placebo.csv"]


def main() -> None:
    report = {"run_utc": datetime.now(timezone.utc).isoformat(), "commands": [], "figures": [], "tables": []}
    with tempfile.TemporaryDirectory(prefix="p5-04-") as temp:
        work = Path(temp)
        shutil.copytree(ROOT / "data/raw", work / "data/raw")
        (work / "data/processed").mkdir(parents=True)
        shutil.copy2(ROOT / "data/processed/P1-04_events_brazil.csv", work / "data/processed")
        shutil.copytree(ROOT / "submission/scripts", work / "submission/scripts")
        for folder in ("results/tables", "results/figures", "results/agentic"):
            (work / folder).mkdir(parents=True)
        for name, *args in SCRIPTS:
            command = [sys.executable, str(work / "submission/scripts" / f"{name}.txt"), *args]
            print(f"Running {name} {' '.join(args)}", flush=True)
            process = subprocess.run(command, cwd=work, text=True, capture_output=True, timeout=300)
            report["commands"].append({"script": name, "args": args, "exit_code": process.returncode,
                                       "stdout_tail": process.stdout[-300:], "stderr_tail": process.stderr[-500:]})
            if process.returncode:
                print(process.stdout[-2000:])
                print(process.stderr[-2000:], file=sys.stderr)
                break
        if all(item["exit_code"] == 0 for item in report["commands"]) and len(report["commands"]) == len(SCRIPTS):
            for figure in FIGURES:
                baseline = ROOT / "results/figures" / figure
                rebuilt = work / "results/figures" / figure
                if not rebuilt.exists():
                    report["figures"].append({"file": figure, "exists": False})
                    continue
                before, after = mpimg.imread(baseline), mpimg.imread(rebuilt)
                same_shape = before.shape == after.shape
                mean_absolute_difference = float(np.abs(before - after).mean()) if same_shape else None
                report["figures"].append({"file": figure, "exists": True, "same_shape": same_shape,
                                          "mean_absolute_pixel_difference": mean_absolute_difference})
                print(f"{figure}: same shape={same_shape}, mean pixel difference={mean_absolute_difference}")
            for table in TABLES:
                baseline = ROOT / "results/tables" / table
                rebuilt = work / "results/tables" / table
                same_bytes = rebuilt.exists() and hashlib.sha256(baseline.read_bytes()).digest() == hashlib.sha256(rebuilt.read_bytes()).digest()
                same_values = same_bytes
                if table == "P2-03_event_table.csv" and rebuilt.exists():
                    # P1-04's source-checked description was expanded after the
                    # frozen table. Numeric and event-coding columns must match.
                    old = pd.read_csv(baseline).drop(columns="description")
                    new = pd.read_csv(rebuilt).drop(columns="description")
                    try:
                        # Rebuilding P1-02 from the same raw candles changes
                        # p_param by at most ~8e-14 through float rounding.
                        pd.testing.assert_frame_equal(old, new, check_exact=False,
                                                      rtol=1e-10, atol=1e-12)
                        same_values = True
                    except AssertionError:
                        same_values = False
                report["tables"].append({"file": table, "exists": rebuilt.exists(),
                                          "same_bytes": same_bytes, "same_values": same_values})
                print(f"{table}: same bytes={same_bytes}, same values={same_values}")
    out = ROOT / "submission/reproduction.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if len(report["commands"]) != len(SCRIPTS) or any(item["exit_code"] for item in report["commands"]):
        raise SystemExit("Exported script re-run failed; see submission/reproduction.json")
    if len(report["figures"]) != len(FIGURES) or any(
        not item["exists"] or not item["same_shape"] or item["mean_absolute_pixel_difference"] > 0.01
        for item in report["figures"]
    ):
        raise SystemExit("Deck figure mismatch; see submission/reproduction.json")
    if len(report["tables"]) != len(TABLES) or any(not item["same_values"] for item in report["tables"]):
        raise SystemExit("Frozen event or money table mismatch; see submission/reproduction.json")
    print(f"Reproduction passed; report: {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
