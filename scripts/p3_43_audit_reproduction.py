"""Reproduce P3-43 finalization risks using synthetic records only.
Run from repository root: python scripts/p3_43_audit_reproduction.py
Inputs: current scorer code; no real labels/runs. Outputs: scratch/review-temp/current-score-fixture/.
Does not modify production scorer or experiment artifacts.
"""
import sys, tempfile, pathlib, csv, json, contextlib, io
sys.path.insert(0, 'scripts')
import p3_28_methods as m
root=pathlib.Path('scratch/review-temp/current-score-fixture').resolve()
(root/'results/tables').mkdir(parents=True,exist_ok=True)
(root/'reference').mkdir(exist_ok=True)
m.ROOT=root; m.RAW=root; m.RUNS=root/'runs'; m.SCHEDULE={'A':1}
c={'case_id':'C','split':'dev','group_id':'synthetic','profile_id':'COMPANY','destination_asset':'USDT','chain':'TRON','as_of_utc':'2026-11-07'}
f={'field_id':'F01','kind':'availability','answer':'state','question':'Is route supported?'}
m.cases=lambda:{'C':c}; m.fields_for=lambda c:[f]; m.M.latest=lambda:({}, {'S':{}})
m.doc_text=lambda i:'Contact support for further information.'; m.corpus_hash=lambda ids:'fixture'
a={'field_id':'F01','state':'supported','value':'','source_ids':['S'],'passages':['Contact support for further information.'],'note':'The complete route is available.'}
r={'permitted':['S'],'corpus_hash':'fixture','errors':[],'answers':[a],'usage':{},'model':'synthetic','n_calls':1,'turns':1,'wall_s':0,'notional_usd':0}
(root/'runs/A').mkdir(parents=True,exist_ok=True)
(root/'runs/A/C_r1.json').write_text(json.dumps(r))
for name, rows in [('ref',[{'case_id':'C','field_id':'F01','state':'supported','value':'','unit':''}]),('audit',[{'key':'unrelated-key','supports':'yes','value_ok':'yes','note_claim':'no'}])]:
 with (root/(name+'.csv')).open('w',newline='') as out:
  w=csv.DictWriter(out,rows[0]); w.writeheader();w.writerows(rows)
m.score(root/'ref.csv','dev',audit_path=root/'audit.csv')
b=dict(a,note='The route is NOT available.')
print('Opposite notes share audit key:',m.audit_key('C','F01',a)==m.audit_key('C','F01',b))
