r"""P3-21 review (G): PTAX calendar cross-check and inventory of files quoting the F-015 money figures.
Written by Codex for Renzo (review, 3 Nov 2026), copied from its scratch folder; now runs its own grep.
Inputs   data/processed/P1-02_premium_daily.csv, data/raw/bcb/ptax.json, deck/ findings/ docs/ notebooks/ STATUS.md
Output   printed only
Run      python scripts/p3_21_review_audit.py
"""
import csv
import json
import subprocess
from collections import defaultdict
from pathlib import Path

root = Path(__file__).resolve().parent.parent
rows = list(csv.DictReader((root/'data/processed/P1-02_premium_daily.csv').open()))
observed = {r['date_brt'] for r in rows if '2026-01-01' <= r['date_brt'] <= '2026-10-30'}
ptax = {r['dataHoraCotacao'][:10] for r in json.loads((root/'data/raw/bcb/ptax.json').read_text())['value'] if '2026-01-01' <= r['dataHoraCotacao'][:10] <= '2026-10-30'}
print('PTAX_calendar', len(observed), len(ptax), 'missing', sorted(ptax-observed), 'extra', sorted(observed-ptax))
assert observed == ptax
relevant, false = defaultdict(list), defaultdict(list)
for line in subprocess.run(['grep', '-rn', r'5.052\|5,052\|5.050\|5,050\|621\|620', 'deck/', 'findings/', 'docs/', 'notebooks/', 'STATUS.md'], cwd=root, capture_output=True, text=True).stdout.splitlines():
    path, number, text = line.split(':', 2)
    is_false = len(text) > 1500 or (path, number) in [('deck/annex_v1_ptbr.md','38'),('findings/F-018-btc-heterogeneity.md','45'),('findings/F-030-no-verified-reopening.md','52')]
    (false if is_false else relevant)[path].append(number)
print('RELEVANT_FILES', len(relevant), dict(relevant))
print('FALSE_MATCHES', dict(false))
sources = ['scripts/p3_01_costs.py', 'tasks/P3-01-money-layer.md', 'docs/sources.md', 'findings/F-015-route-costs.md', 'findings/F-033-who-paid.md', 'deck/deck_v1_ptbr.md', 'deck/annex_v1_ptbr.md', 'notebooks/p5_07_story.ipynb', 'STATUS.md']
generated = ['results/tables/P3-01_route_costs.csv','results/figures/P3-01_route_costs.png','deck/deck_apresentacao.html']
assert all((root / p).exists() for p in sources + generated)
print('SWITCH_WORKLOAD', len(sources), 'sources', len(generated), 'generated', len(sources + generated), 'files plus final PDF')
