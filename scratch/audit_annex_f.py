import sys, re
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

with open('deck/annex_v1_ptbr.md', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'# Anexo F.*', text, re.DOTALL)
if not m:
    print("Anexo F not found")
    sys.exit(0)

f_text = m.group(0)

for sec in ['F.1', 'F.2', 'F.3', 'F.4', 'F.5', 'F.6', 'F.7']:
    pat = rf'### {sec}\..*?(?=(?:### F\.|\Z))'
    m_sec = re.search(pat, f_text, re.DOTALL)
    if m_sec:
        content = m_sec.group(0)
        print(f"\n{'='*20} {sec} {'='*20}")
        lines = [l.strip() for l in content.splitlines() if l.strip() and ('|' in l or re.search(r'\d', l))]
        for l in lines[:10]:
            print(f"  {l[:100]}")
