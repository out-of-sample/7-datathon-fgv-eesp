import sys, re, os
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

with open('deck/annex_v1_ptbr.md', encoding='utf-8') as f:
    text = f.read()

# Let's inspect numbers in Annex sections
sections = re.split(r'\n# Anexo ([A-F])', text)

print("="*60)
print("ANNEX SECTIONS NUMBER SCAN")
print("="*60)

for i in range(1, len(sections), 2):
    letter = sections[i]
    content = sections[i+1]
    print(f"\n--- Anexo {letter} (length: {len(content)} chars) ---")
    
    # Check key numbers
    # For instance: B.1, B.2, B.3, B.4, B.5, B.6, etc.
    lines = content.splitlines()
    table_lines = [l for l in lines if '|' in l and re.search(r'\d', l)]
    print(f"  Total table rows with numbers: {len(table_lines)}")
    # Print sample table lines
    for tl in table_lines[:3]:
        print(f"    {tl[:100]}")
