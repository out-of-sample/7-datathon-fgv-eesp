import re, sys, os

sys.stdout.reconfigure(encoding='utf-8')

files = [
    'deck/deck_v1_ptbr.md',
    'deck/deck_v2_ptbr.md',
    'deck/annex_v1_ptbr.md',
    'STATUS.md',
]

print("="*60)
print("TEXT QUALITY, TYPOS & ANOMALIES AUDIT")
print("="*60)

for fpath in files:
    print(f"\nScanning {fpath}...")
    with open(fpath, encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    
    # 1. Check for unicode replacement character 
    bad_chars = []
    # 2. Check for leftover placeholder tags like [verify], TODO, FIXME, XXX
    placeholders = []
    # 3. Check for empty links [text]() or broken links
    broken_links = []
    # 4. Check for double punctuation or formatting glitches
    glitches = []
    
    for idx, line in enumerate(lines, 1):
        if '' in line:
            bad_chars.append((idx, line.strip()))
        if re.search(r'\b(TODO|FIXME|XXX)\b|\[verify\]', line, re.I):
            placeholders.append((idx, line.strip()))
        if re.search(r'\[[^\]]+\]\(\s*\)', line):
            broken_links.append((idx, line.strip()))
            
    print(f"  Replacement characters (): {len(bad_chars)}")
    for lno, text in bad_chars[:5]:
        print(f"    Line {lno}: {text[:100]}")
    print(f"  Placeholders (TODO/verify): {len(placeholders)}")
    for lno, text in placeholders[:5]:
        print(f"    Line {lno}: {text[:100]}")
    print(f"  Empty/Broken links: {len(broken_links)}")
    for lno, text in broken_links[:5]:
        print(f"    Line {lno}: {text[:100]}")
