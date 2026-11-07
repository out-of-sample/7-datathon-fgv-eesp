import re, sys, os
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load docs/sources.md
with open('docs/sources.md', encoding='utf-8') as f:
    sources_text = f.read()

# 2. Load annex_v1_ptbr.md
with open('deck/annex_v1_ptbr.md', encoding='utf-8') as f:
    annex_text = f.read()

# 3. Load deck_v1_ptbr.md and deck_v2_ptbr.md
with open('deck/deck_v1_ptbr.md', encoding='utf-8') as f:
    deck_v1_text = f.read()
with open('deck/deck_v2_ptbr.md', encoding='utf-8') as f:
    deck_v2_text = f.read()

# Pattern for IDs:
# R-xx, E-xx, D-xx, L-xx, A-xx, M-xx, DP-xx, F-xxx, Px-xx
patterns = {
    'R': r'\bR-\d+[a-z]?\b',
    'E': r'\bE-\d+(?:\.\d+)?[a-z]?\b',
    'D': r'\bD-\d+\b',
    'L': r'\bL-\d+\b',
    'A': r'\bA-\d+\b',
    'M': r'\bM-\d+\b',
    'DP': r'\bDP-\d+\b',
    'F': r'\bF-\d+\b',
    'P': r'\bP\d+-\d+\b',
}

def extract_ids(text):
    found = defaultdict(set)
    for k, pat in patterns.items():
        matches = re.findall(pat, text)
        for m in matches:
            found[k].add(m)
    return found

ids_sources = extract_ids(sources_text)
ids_annex = extract_ids(annex_text)
ids_deck_v1 = extract_ids(deck_v1_text)
ids_deck_v2 = extract_ids(deck_v2_text)

print("="*60)
print("CITATION & SOURCE CROSS-CHECK")
print("="*60)

for category in patterns.keys():
    in_v1 = ids_deck_v1[category]
    in_v2 = ids_deck_v2[category]
    in_annex = ids_annex[category]
    in_src = ids_sources[category]
    
    print(f"\nCategory {category}:")
    print(f"  Deck v1 ({len(in_v1)}): {sorted(in_v1)}")
    print(f"  Deck v2 ({len(in_v2)}): {sorted(in_v2)}")
    print(f"  Annex ({len(in_annex)}): {sorted(in_annex)}")
    print(f"  Sources.md ({len(in_src)}): {sorted(in_src)}")
    
    # Check if any ID in Deck or Annex is missing from sources.md
    missing_from_sources_v1 = in_v1 - in_src
    missing_from_sources_v2 = in_v2 - in_src
    missing_from_sources_annex = in_annex - in_src
    
    if missing_from_sources_v1:
        print(f"  [!] Missing in sources.md from Deck v1: {sorted(missing_from_sources_v1)}")
    if missing_from_sources_v2:
        print(f"  [!] Missing in sources.md from Deck v2: {sorted(missing_from_sources_v2)}")
    if missing_from_sources_annex:
        print(f"  [!] Missing in sources.md from Annex: {sorted(missing_from_sources_annex)}")
