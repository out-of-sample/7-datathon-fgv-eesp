"""P3-40: inexpensive offline project-integrity and buyer-output audit.
Run python scripts/p3_40_project_review.py. Does not rewrite research outputs.
"""
from pathlib import Path
import ast
import csv
import json
import re

ROOT=Path(__file__).resolve().parents[1]

def main():
    problems=[]; counts={}
    for folder in ('tasks','findings'):
        ids={}
        for p in (ROOT/folder).glob('*.md'):
            if p.name.startswith('_'): continue
            m=re.search(r'^id:\s*(\S+)',p.read_text(encoding='utf-8'),re.M)
            if not m: problems.append(f'Missing id: {p.relative_to(ROOT)}');continue
            ids.setdefault(m[1],[]).append(p.name)
        for ident,files in ids.items():
            if len(files)>1: problems.append(f'Duplicate {ident}: {files}')
        counts[folder]=len(ids)
    scripts=list((ROOT/'scripts').glob('*.py'))
    for p in scripts:
        try: ast.parse(p.read_text(encoding='utf-8-sig'),filename=str(p))
        except SyntaxError as exc: problems.append(str(exc))
    counts['scripts_parsed']=len(scripts)
    tracked=['STATUS.md','docs/README.md','deck/deck_v1_ptbr.md','deck/annex_v1_ptbr.md']
    for rel in tracked:
        if re.search(r'^(<<<<<<< |=======\s*$|>>>>>>> )',(ROOT/rel).read_text(encoding='utf-8'),re.M):
            problems.append(f'Conflict marker: {rel}')
    # Independent terminal cash-flow identity, using exported fields rather than model code.
    with (ROOT/'results/tables/P3-38_june_ceiling.csv').open(encoding='utf-8') as f:
        rows=list(csv.DictReader(f))
    for r in rows:
        expected=float(r['buy_now_terminal_brl'])-float(r['wait_conversion_brl'])+float(r['hedge_payoff_brl'])
        if abs(expected-float(r['max_additional_cost_brl']))>1e-7:
            problems.append('Buyer terminal identity mismatch')
        expected_bps=expected/float(r['initial_outlay_brl'])*10000
        if abs(expected_bps-float(r['max_additional_cost_bps']))>1e-8:
            problems.append('Buyer denominator mismatch')
        if not r['actual_decision'].startswith('no_cost_ranking:'):
            problems.append('Unresolved access produced an actionable ranking')
    counts['buyer_rows_reconciled']=len(rows)
    print(json.dumps(dict(counts=counts,problems=problems),indent=2))
    if problems: raise SystemExit(1)

if __name__=='__main__': main()
