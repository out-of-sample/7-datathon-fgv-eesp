import re, sys, os

sys.stdout.reconfigure(encoding='utf-8')

with open('deck/deck_v1_ptbr.md', encoding='utf-8') as f:
    text = f.read()

parts = re.split(r'<!-- SLIDE (\d+) -->', text)

slides = {}
for i in range(1, len(parts), 2):
    num = int(parts[i])
    content = parts[i+1]
    slides[num] = content

print(f"Total slides found: {len(slides)}")

for num in sorted(slides.keys()):
    print(f"\n{'='*25} SLIDE {num} {'='*25}")
    lines = slides[num].strip().split('\n')
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
        # search for numbers (including percentages, currency, decimals, etc.)
        if re.search(r'\d+', line_clean):
            print(f"  {line_clean}")
