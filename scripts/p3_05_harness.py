r"""P3-05 S4-S6: Cross-platform runner and validator harness for AI agent runs.

Purpose:
  Sets up an isolated ephemeral sandbox for an AI agent run, populates it with
  the frozen data bundle (data/agentic_bundle/) and PROMPT.txt, executes the
  agent CLI (Claude Code, Codex CLI, Gemini CLI, or mock/custom), validates the
  resulting answer.json against the pre-registered schema, and archives outputs
  to results/agentic/runs/<run_id>/.

Usage:
  # Dry-run: set up isolated sandbox, write PROMPT.txt, print command without running
  py scripts/p3_05_harness.py --family claude --run-id A-01 --dry-run

  # Mock run: verify pipeline end-to-end without spending quotas
  py scripts/p3_05_harness.py --family claude --run-id test-mock --mock

  # Live run on Renzo's machine:
  py scripts/p3_05_harness.py --family claude --run-id A-01
  py scripts/p3_05_harness.py --family codex --run-id B-01
  py scripts/p3_05_harness.py --family gemini --run-id C-01

  # Validate and archive an already-run folder:
  py scripts/p3_05_harness.py --run-id A-01 --validate-dir /path/to/completed_sandbox
"""
import argparse
import datetime
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Dict, Any, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
BUNDLE_DIR = ROOT / "data" / "agentic_bundle"
RUNS_DIR = ROOT / "results" / "agentic" / "runs"

FROZEN_PROMPT_TEMPLATE = """You are an empirical economist. The folder `data/` contains hourly USDT/BRL prices from Binance, the Brazilian central bank's official dollar rate (PTAX) and hourly USDC/USDT prices, with the providers' documentation in `docs/`. Question: did the price of USDT in reais, relative to the official dollar, change after 23 June 2026, and by how much? Estimate the change in basis points with a standard error. Make and justify your own analysis choices. Use only the files provided. Write your code to `analysis.py`, your answer to `answer.json` (schema below) and a short explanation (<= 300 words) to `report.md`.

Required JSON schema for answer.json:
{
  "run_id": "{run_id}",
  "model": "<model name and exact version string>",
  "direction": "up | down | no change",
  "estimate_bps": 0.0,
  "std_error_bps": 0.0,
  "premium_definition": "<formula in words>",
  "time_matching": "<how USDT/BRL and PTAX were aligned in time>",
  "usdt_usd_adjustment": false,
  "window_pre_days": 0,
  "window_post_days": 0,
  "estimator": "<difference in means, regression, ...>",
  "controls": [],
  "data_issues_found": [],
  "notes": "<concise summary of findings>"
}
"""

SCHEMA_FIELDS = {
    "run_id": (str,),
    "model": (str,),
    "direction": (str,),
    "estimate_bps": (int, float),
    "std_error_bps": (int, float),
    "premium_definition": (str,),
    "time_matching": (str,),
    "usdt_usd_adjustment": (bool,),
    "window_pre_days": (int,),
    "window_post_days": (int,),
    "estimator": (str,),
    "controls": (list,),
    "data_issues_found": (list,),
    "notes": (str,),
}

VALID_DIRECTIONS = {"up", "down", "no change"}


def validate_answer_json(answer_path: Path, expected_run_id: str = None) -> Tuple[bool, List[str], Dict[str, Any]]:
    errors = []
    if not answer_path.exists():
        return False, [f"Missing answer file: {answer_path}"], {}

    try:
        data = json.loads(answer_path.read_text(encoding="utf-8"))
    except Exception as e:
        return False, [f"Invalid JSON syntax in {answer_path}: {e}"], {}

    if not isinstance(data, dict):
        return False, ["Root JSON object must be an object/dict"], {}

    for field, expected_types in SCHEMA_FIELDS.items():
        if field not in data:
            errors.append(f"Missing required field: '{field}'")
        else:
            val = data[field]
            if not isinstance(val, expected_types):
                errors.append(f"Field '{field}' has invalid type {type(val).__name__}, expected {tuple(t.__name__ for t in expected_types)}")

    if "direction" in data and isinstance(data["direction"], str):
        dir_clean = data["direction"].strip().lower()
        if dir_clean not in VALID_DIRECTIONS:
            errors.append(f"Invalid direction: '{data['direction']}'. Must be one of {VALID_DIRECTIONS}")

    if expected_run_id and "run_id" in data:
        if str(data["run_id"]).strip() != expected_run_id:
            errors.append(f"run_id mismatch: expected '{expected_run_id}', found '{data['run_id']}'")

    return len(errors) == 0, errors, data


def setup_sandbox(sandbox_dir: Path, run_id: str):
    print(f"Setting up sandbox in: {sandbox_dir}")
    if sandbox_dir.exists():
        shutil.rmtree(sandbox_dir)
    sandbox_dir.mkdir(parents=True, exist_ok=True)

    if not BUNDLE_DIR.exists():
        raise FileNotFoundError(
            f"Bundle directory {BUNDLE_DIR} does not exist. Run scripts/p3_05_build_bundle.py first."
        )

    # Copy bundle data and docs
    for item in BUNDLE_DIR.iterdir():
        dest = sandbox_dir / item.name
        if item.is_dir():
            shutil.copytree(item, dest)
        else:
            shutil.copy2(item, dest)

    # Write PROMPT.txt
    prompt_file = sandbox_dir / "PROMPT.txt"
    prompt_file.write_text(FROZEN_PROMPT_TEMPLATE.replace("{run_id}", run_id), encoding="utf-8")
    print(f"Sandbox initialized with bundle and PROMPT.txt")


def get_default_cli_command(family: str, sandbox_dir: Path, prompt_text: str) -> List[str]:
    """Default isolated CLI invocation commands for the 3 families."""
    if family == "claude":
        # Claude Code: non-interactive print mode, permission prompt bypassed for automated runner
        return [
            "claude",
            "--dangerously-skip-permissions",
            "-p",
            prompt_text,
        ]
    elif family == "codex":
        # Codex CLI (ChatGPT): headless exec mode
        return [
            "codex",
            "exec",
            "--prompt",
            prompt_text,
        ]
    elif family == "gemini":
        # Gemini CLI: headless prompt
        return [
            "gemini",
            "prompt",
            prompt_text,
        ]
    else:
        raise ValueError(f"Unknown family: {family}")


def run_mock_agent(sandbox_dir: Path, run_id: str, family: str):
    """Simulates an autonomous agent run to verify the pipeline."""
    print("Running simulated mock agent...")
    time.sleep(1)

    analysis_code = '''# Simulated mock agent analysis
import pandas as pd
import json

# Dummy calculation for pipeline verification
print("Computing USDT/BRL premium change around 2026-06-23...")
estimate = 91.5
se = 15.0

answer = {
    "run_id": "%s",
    "model": "mock-%s-model-v1",
    "direction": "up",
    "estimate_bps": estimate,
    "std_error_bps": se,
    "premium_definition": "USDTBRL / PTAX - 1 in basis points",
    "time_matching": "Daily close matching",
    "usdt_usd_adjustment": True,
    "window_pre_days": 20,
    "window_post_days": 20,
    "estimator": "Difference in means (OLS)",
    "controls": [],
    "data_issues_found": ["Delisting gap in late 2022"],
    "notes": "Mock agent successfully verified pipeline."
}

with open("answer.json", "w", encoding="utf-8") as f:
    json.dump(answer, f, indent=2)

with open("report.md", "w", encoding="utf-8") as f:
    f.write("# Analysis Report\\n\\nFound a statistically significant rise of 91.5 bps after 23 June 2026.\\n")
''' % (run_id, family)

    (sandbox_dir / "analysis.py").write_text(analysis_code, encoding="utf-8")
    proc = subprocess.run([sys.executable, "analysis.py"], cwd=sandbox_dir, capture_output=True, text=True)
    return proc.returncode, proc.stdout + "\n" + proc.stderr


def archive_run(sandbox_dir: Path, run_id: str, log_content: str, validation_errors: List[str]):
    dest_dir = RUNS_DIR / run_id
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Save log
    log_file = dest_dir / "run.log"
    full_log = log_content
    if validation_errors:
        full_log += "\n\n=== SCHEMA VALIDATION ERRORS ===\n" + "\n".join(validation_errors)
    log_file.write_text(full_log, encoding="utf-8")

    # Copy generated files
    for fname in ["answer.json", "report.md", "analysis.py"]:
        src = sandbox_dir / fname
        if src.exists():
            shutil.copy2(src, dest_dir / fname)

    # Copy any extra charts or csvs generated by agent
    for extra in sandbox_dir.glob("*.png"):
        shutil.copy2(extra, dest_dir / extra.name)
    for extra in sandbox_dir.glob("*.csv"):
        shutil.copy2(extra, dest_dir / extra.name)

    print(f"Run outputs archived to: {dest_dir}")


def main():
    parser = argparse.ArgumentParser(description="P3-05 Agent Harness and Schema Validator")
    parser.add_argument("--family", choices=["claude", "codex", "gemini", "mock"], default="mock",
                        help="Model family CLI")
    parser.add_argument("--run-id", required=True, help="Run identifier, e.g. A-01, B-01, C-01, pilot-claude")
    parser.add_argument("--cli-cmd", default=None, help="Custom CLI command override string")
    parser.add_argument("--dry-run", action="store_true", help="Prepare sandbox and prompt, then print instructions")
    parser.add_argument("--mock", action="store_true", help="Run simulated agent to test validation and archiving")
    parser.add_argument("--validate-dir", default=None, help="Directly validate and archive an existing sandbox directory")
    parser.add_argument("--keep-sandbox", action="store_true", help="Do not delete temporary sandbox directory on exit")
    args = parser.parse_args()

    run_id = args.run_id

    if args.validate_dir:
        sandbox_dir = Path(args.validate_dir).resolve()
        print(f"Validating existing directory: {sandbox_dir}")
        answer_path = sandbox_dir / "answer.json"
        valid, errors, data = validate_answer_json(answer_path, run_id)
        log_content = (sandbox_dir / "run.log").read_text(encoding="utf-8") if (sandbox_dir / "run.log").exists() else "No existing run.log"
        archive_run(sandbox_dir, run_id, log_content, errors)
        if valid:
            print(f"SUCCESS: {run_id} is valid! Estimate: {data.get('estimate_bps')} bps, SE: {data.get('std_error_bps')}")
            sys.exit(0)
        else:
            print(f"VALIDATION FAILED for {run_id}:")
            for err in errors:
                print(f"  - {err}")
            sys.exit(1)

    temp_base = Path(tempfile.gettempdir())
    sandbox_dir = temp_base / f"agent_run_{args.family}_{run_id}"

    setup_sandbox(sandbox_dir, run_id)
    prompt_text = (sandbox_dir / "PROMPT.txt").read_text(encoding="utf-8")

    if args.dry_run:
        print("\n--- DRY RUN PREPARATION COMPLETE ---")
        print(f"Sandbox directory ready: {sandbox_dir}")
        print("To launch this agent manually:")
        if args.family == "claude":
            print(f"  cd \"{sandbox_dir}\" && claude -p \"$(cat PROMPT.txt)\"")
        elif args.family == "codex":
            print(f"  cd \"{sandbox_dir}\" && codex exec --prompt \"$(cat PROMPT.txt)\"")
        elif args.family == "gemini":
            print(f"  cd \"{sandbox_dir}\" && gemini prompt \"$(cat PROMPT.txt)\"")
        print(f"\nAfter completion, validate and archive with:")
        print(f"  py scripts/p3_05_harness.py --run-id {run_id} --validate-dir \"{sandbox_dir}\"")
        return

    start_time = datetime.datetime.now(datetime.timezone.utc)
    log_lines = [
        f"=== P3-05 AGENT RUN LOG ===",
        f"Run ID: {run_id}",
        f"Family: {args.family}",
        f"Started: {start_time.isoformat()}",
        f"Sandbox: {sandbox_dir}",
    ]

    if args.mock:
        code, out = run_mock_agent(sandbox_dir, run_id, args.family)
        log_lines.append(f"Mock Execution Return Code: {code}")
        log_lines.append(f"Output:\n{out}")
    else:
        cmd = args.cli_cmd.split() if args.cli_cmd else get_default_cli_command(args.family, sandbox_dir, prompt_text)
        log_lines.append(f"Command: {' '.join(cmd)}")
        print(f"Executing: {' '.join(cmd)} in {sandbox_dir}")
        env = os.environ.copy()
        # Suppress local repo git roots or nested configs
        env["GIT_DIR"] = ""
        try:
            proc = subprocess.run(cmd, cwd=sandbox_dir, capture_output=True, text=True, env=env)
            log_lines.append(f"Return Code: {proc.returncode}")
            log_lines.append("STDOUT:\n" + proc.stdout)
            log_lines.append("STDERR:\n" + proc.stderr)
        except Exception as e:
            log_lines.append(f"EXECUTION EXCEPTION: {e}")

    end_time = datetime.datetime.now(datetime.timezone.utc)
    duration = (end_time - start_time).total_seconds()
    log_lines.append(f"Finished: {end_time.isoformat()} (duration: {duration:.1f}s)")

    # Validate output
    answer_path = sandbox_dir / "answer.json"
    valid, errors, data = validate_answer_json(answer_path, run_id)

    log_str = "\n".join(log_lines)
    archive_run(sandbox_dir, run_id, log_str, errors)

    if not args.keep_sandbox and valid:
        try:
            shutil.rmtree(sandbox_dir)
            print(f"Cleaned up sandbox {sandbox_dir}")
        except Exception as e:
            print(f"Note: Could not clean up {sandbox_dir}: {e}")

    if valid:
        print(f"\n[OK] Run {run_id} completed successfully in {duration:.1f}s!")
        print(f"     Direction: {data.get('direction')}, Estimate: {data.get('estimate_bps')} bps (SE: {data.get('std_error_bps')} bps)")
        print(f"     Model: {data.get('model')}")
    else:
        print(f"\n[FAILED] Run {run_id} failed schema validation:")
        for err in errors:
            print(f"     - {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
