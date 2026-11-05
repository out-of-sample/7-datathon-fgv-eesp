# Independent Claude review: P5-04 script exports

Renzo asked for an independent Claude review after Codex completed [P5-04](../tasks/P5-04-scripts-txt.md). Please review the exported submission scripts before marking the task done. Do not rewrite the analysis or add a new experiment in this review.

## What Codex delivered

- `submission/scripts/`: 18 executable `.txt` exports covering the computed claims and six existing charts in both current 10-slide deck drafts.
- `submission/README.md`: run order, figure/claim map, raw-data and hand-coded event-table inputs.
- `scripts/p5_04_export.py`: regenerates exports from the source `.py` files, adding standard headers and adjusting the repository root path for the deeper directory.
- `scripts/p5_04_reproduce.py`: runs all exports in a fresh temporary workspace using a copy of frozen raw data and compares outputs; see `submission/reproduction.json`.
- `scripts/p2_03_events.py`: one disclosed reproducibility fix. It now fixes weekday draw order so the seeded placebo sample matches the frozen 2 Nov sample. F-016 and F-025 History record the fix; numerical claims are unchanged.

## Review steps

1. Check the two 10-slide drafts, `deck/deck_v1_ptbr.md` and `deck/deck_v2_ptbr.md`, against the map in `submission/README.md`. Identify any figure or computed claim with a missing script. Felipe's final deck choice and P5-02 replacement visuals remain open.
2. Inspect `scripts/p5_04_export.py`. The intended changes inside each export are `ROOT = Path(__file__).resolve().parents[2]`, the `p3_03_monitor.txt` lookup of exported dependencies, and trailing whitespace removal. Check a few exports against their `.py` source and the SHA-256 header.
3. Run `.venv/bin/python scripts/p5_04_reproduce.py` from the repository root. It should exit 0. All six existing deck charts should have pixel difference 0. The frozen P2-03 placebo and P3-11 transfer/placebo tables should match byte for byte. The P2-03 event table should match on event coding and numbers; its E-05 source description was expanded later, and `p_param` differs only by floating-point rounding below 1e-12.
4. Check the P2-03 weekday-order fix against the frozen `results/tables/P2-03_placebo_draws.csv` and confirm that the P3-11 largest placebo transfer remains R$ 35.5 million. Check that the reported R$ 106.1 million headline did not change.
5. Record review findings in the P5-04 task log. Mark `done` only after the final PDF's actual figures and numbers are reconciled with the exported set; add any new P5-02 script exports before submission.

Known limitations: frozen raw files are outside Git and must be restored per `data/README.md`; the manually coded P1-04 event table is a documented input; P3-20 E2 readout remains pending until its registered window is observed.
