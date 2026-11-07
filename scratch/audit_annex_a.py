import sys, re
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

with open('deck/annex_v1_ptbr.md', encoding='utf-8') as f:
    text = f.read()

# Extract Anexo A table
m = re.search(r'# Anexo A.*?\n(\|.*?)(?=\n# Anexo B)', text, re.DOTALL)
table_text = m.group(1).strip()
lines = [l for l in table_text.splitlines() if l.startswith('|') and not l.startswith('|---') and not 'Média Pré' in l]

print(f"Total event rows in Anexo A: {len(lines)}")
df_events = pd.read_csv('results/tables/P2-03_event_table.csv')

for l in lines:
    parts = [p.strip() for p in l.split('|')[1:-1]]
    eid = re.sub(r'[*_]', '', parts[0])
    desc = parts[1]
    notice = parts[2]
    eval_date = parts[3]
    if '—' in parts[4]:
        print(f"  {eid} ({eval_date}): [Unenacted or Future] — OK")
        continue
    pre_str = re.sub(r'[*_]', '', parts[4]).replace(',', '.')
    post_str = re.sub(r'[*_]', '', parts[5]).replace(',', '.')
    diff_str = re.sub(r'[*_]', '', parts[6]).replace(',', '.').replace('+', '')
    pre_m = float(pre_str)
    post_m = float(post_str)
    diff_val = float(diff_str)
    
    # match with df_events
    match = df_events[(df_events['event_id'] == eid) & (df_events['t0_ptax'] == eval_date)]
    if len(match) == 0:
        match = df_events[(df_events['event_id'] == eid) & (df_events['event_date'] == eval_date)]
    if len(match) == 0:
        match = df_events[df_events['event_id'] == eid]
    
    if len(match) > 0:
        ev = match.iloc[0]
        ev_pre = round(ev['pre_mean_bps'], 2)
        ev_post = round(ev['post_mean_bps'], 2)
        ev_diff = round(ev['diff_bps'], 2)
        diff_match = abs(diff_val - ev_diff) < 0.05
        status_str = "MATCH" if diff_match else f"MISMATCH (table={ev_diff}, annex={diff_val})"
        print(f"  {eid} ({eval_date}): diff={diff_val:+.2f} vs table={ev_diff:+.2f} | {status_str}")
    else:
        print(f"  {eid} ({eval_date}): NOT FOUND in P2-03_event_table.csv")
