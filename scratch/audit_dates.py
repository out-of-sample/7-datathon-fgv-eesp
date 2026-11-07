import re, sys, os
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

print("="*60)
print("DATE & EVENT TIMELINE CONSISTENCY CHECK")
print("="*60)

files_to_check = [
    'deck/deck_v1_ptbr.md',
    'deck/deck_v2_ptbr.md',
    'deck/annex_v1_ptbr.md',
    'STATUS.md',
]

# Key events to verify:
# 1. 23 Jun: BCB notice sent (confidential/restricted)
# 2. 24 Jun: First day of new regime / price break / press (Cointelegraph)
# 3. 25 Jun: Exame report on notice excerpt
# 4. 26 Jun: BCB meeting with associations (suspension maintained, order-book arb allowed, 24h hold draft)
# 5. 1 Jul: Res. BCB 580 (prudential regime type 3)
# 6. 3 Jul: Peak day (+185.9 bps, +170.7 bps above pre-mean)
# 7. 22 Jul: Bai-Perron break 5 (fade begins; 109.1 -> 26.8 bps)
# 8. 29-30 Oct: Binance security incident (29 Oct 20:05 UTC attack; 30 Oct withdrawal freeze & -30.3 bps dip)
# 9. 3-4 Nov: E1 post-window (Res. BCB 574 effective 3 Nov; evaluated on 3-4 Nov)
# 10. 5-6 Nov: E2 window (Res. BCB 589 art. 91 effective 6 Nov; 5 Nov pre, 6 Nov S1 early reading)

target_events = {
    '23/jun': r'23/jun|23 de junho|2026-06-23',
    '24/jun': r'24/jun|24 de junho|2026-06-24',
    '25/jun': r'25/jun|25 de junho|2026-06-25',
    '26/jun': r'26/jun|26 de junho|2026-06-26',
    '1/jul': r'1/jul|1º de julho|2026-07-01',
    '3/jul': r'3/jul|3 de julho|2026-07-03',
    '22/jul': r'22/jul|22 de julho|2026-07-22',
    '29-30/out': r'29/out|30/out|29–30/out|29 de outubro|30 de outubro|2026-10-29|2026-10-30',
    '3-4/nov': r'3–4/nov|3-4/nov|3 e 4 de nov|3 e 4/nov|2026-11-03',
    '5-6/nov': r'5–6/nov|5-6/nov|6/nov|6 de nov|2026-11-06',
}

for fpath in files_to_check:
    print(f"\n--- Checking file: {fpath} ---")
    with open(fpath, encoding='utf-8') as f:
        content = f.read()
    
    for label, pat in target_events.items():
        matches = list(re.finditer(pat, content, re.IGNORECASE))
        print(f"  Event '{label}': {len(matches)} occurrences")
        # Check contexts of a few occurrences
        for m in matches[:2]:
            start = max(0, m.start() - 60)
            end = min(len(content), m.end() + 60)
            ctx = content[start:end].replace('\n', ' ')
            # print(f"    ctx: ...{ctx}...")
