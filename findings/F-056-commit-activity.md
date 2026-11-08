---
id: F-056
title: Git commit activity by teammate and Brasília day
status: exploratory
task: -
date: 2026-11-07
checked_by: -
---

## Claim
Using a two-hour inactivity threshold between consecutive commits, the 255 reachable commits form 35 inferred sessions across 20 user-days. Summed first-to-last intervals within those sessions are Renzo 29.04 h, Felipe 12.53 h, Jonathan 8.54 h, and Nattan 1.02 h (51.13 h total). These are commit-based estimates, not measured work hours.

## Evidence
- Scope: all commits reachable from current `HEAD`, grouped by teammate and Brasília calendar date. Author timestamps were converted to `America/Sao_Paulo` before grouping.
- Identity mapping: Renzo's two emails merged; Felipe's two emails merged; Jonathan and Nattan mapped by their listed emails in `docs/README.md`.
- Session rule: sort a user's commits within each Brasília date; start a new session when the gap from the previous commit is **2 hours or more**. Session duration is first to last commit within that uninterrupted sequence. Sum session durations by day and user. Commits inside a session contribute their gaps to the span; single-commit sessions have zero measured duration.
- Reproduce from the repository root:

```bash
python3 - <<'PYCODE'
import subprocess, datetime, collections, zoneinfo
raw = subprocess.check_output(['git', 'log', '--format=%an%x09%ae%x09%aI'], text=True)
tz = zoneinfo.ZoneInfo('America/Sao_Paulo')
rows = []
for line in raw.splitlines():
    name, email, stamp = line.split('\t')
    dt = datetime.datetime.fromisoformat(stamp).astimezone(tz)
    if email in {'renzofilho2004z@gmail.com', '109882518+Renzo-Filho@users.noreply.github.com'}: user = 'Renzo'
    elif email in {'177073024+Cordyluz@users.noreply.github.com', 'felipe@fgv.br'}: user = 'Felipe'
    elif email == 'jonathanspereira21@gmail.com': user = 'Jonathan'
    elif email == 'nattanferreira58@gmail.com': user = 'Nattan'
    else: user = f'{name} <{email}>'
    rows.append((user, dt))
days = collections.defaultdict(list)
for user, dt in rows:
    days[(user, dt.date().isoformat())].append(dt)
total_hours = collections.Counter()
session_counts = collections.Counter()
for (user, day), stamps in sorted(days.items(), key=lambda item: (item[0][1], item[0][0])):
    stamps.sort()
    sessions = []
    first = previous = stamps[0]
    commits = 1
    for stamp in stamps[1:]:
        if (stamp - previous).total_seconds() >= 7200:
            sessions.append((first, previous, commits))
            first, commits = stamp, 1
        else:
            commits += 1
        previous = stamp
    sessions.append((first, previous, commits))
    hours = sum((last - first).total_seconds() / 3600 for first, last, _ in sessions)
    total_hours[user] += hours
    session_counts[user] += len(sessions)
    detail = '; '.join(f'{a:%H:%M}–{b:%H:%M} ({(b-a).total_seconds()/3600:.2f} h, {n} commits)' for a,b,n in sessions)
    print(f'{day}\t{user}\t{len(stamps)} commits\t{detail}\t{hours:.2f} h')
print('SUMS:', dict(total_hours))
PYCODE
```

- Per-user totals:

| User | Commits | Sessions | Inferred elapsed time |
|---|---:|---:|---:|
| Renzo | 183 | 17 | 29.04 h |
| Felipe | 40 | 10 | 12.53 h |
| Jonathan | 27 | 6 | 8.54 h |
| Nattan | 5 | 2 | 1.02 h |
| **Total** | **255** | **35** | **51.13 h** |

- Daily sessions (Brasília time; each range is one inferred session, followed by its commit count):

| Date | User | Commits | Inferred sessions | Daily sum |
|---|---|---:|---|---:|
| 2026-10-27 | Renzo | 1 | 17:37–17:37 (1) | 0.00 h |
| 2026-10-31 | Jonathan | 6 | 14:29–18:09 (6) | 3.66 h |
| 2026-10-31 | Nattan | 4 | 16:32–17:33 (4) | 1.02 h |
| 2026-10-31 | Renzo | 30 | 02:28–03:23 (6); 11:25–11:33 (2); 13:43–17:33 (19); 22:53–23:49 (3) | 5.82 h |
| 2026-11-01 | Felipe | 1 | 21:50–21:50 (1) | 0.00 h |
| 2026-11-01 | Jonathan | 5 | 08:34–08:42 (2); 21:46–22:11 (3) | 0.55 h |
| 2026-11-01 | Nattan | 1 | 13:33–13:33 (1) | 0.00 h |
| 2026-11-01 | Renzo | 4 | 00:36–00:53 (4) | 0.28 h |
| 2026-11-02 | Felipe | 14 | 00:22–00:56 (2); 09:42–10:37 (5); 14:54–18:07 (7) | 4.69 h |
| 2026-11-02 | Renzo | 51 | 13:33–19:47 (43); 22:26–23:57 (8) | 7.76 h |
| 2026-11-03 | Jonathan | 1 | 09:33–09:33 (1) | 0.00 h |
| 2026-11-03 | Renzo | 22 | 00:19–02:57 (14); 13:00–14:51 (8) | 4.48 h |
| 2026-11-04 | Felipe | 5 | 19:59–19:59 (1); 22:26–23:58 (4) | 1.55 h |
| 2026-11-04 | Renzo | 9 | 22:48–23:56 (9) | 1.12 h |
| 2026-11-05 | Felipe | 1 | 00:07–00:07 (1) | 0.00 h |
| 2026-11-05 | Renzo | 22 | 00:06–02:24 (20); 12:42–14:05 (2) | 3.68 h |
| 2026-11-06 | Felipe | 2 | 22:01–23:14 (2) | 1.22 h |
| 2026-11-06 | Renzo | 8 | 03:16–04:02 (5); 23:43–23:50 (3) | 0.88 h |
| 2026-11-07 | Felipe | 17 | 00:15–03:55 (15); 13:56–15:21 (2) | 5.07 h |
| 2026-11-07 | Jonathan | 15 | 00:26–02:04 (3); 15:41–18:22 (12) | 4.33 h |
| 2026-11-07 | Renzo | 36 | 00:10–03:33 (30); 17:09–18:47 (6) | 5.02 h |

## Caveats
- Commit counts measure recorded Git commits, not code volume, effort, quality, or ownership. A commit may be authored by an agent using a teammate's identity.
- The two-hour split is a heuristic: a contributor may work without committing for two hours, or may commit while not continuously working. Each session duration includes all gaps shorter than two hours, so this can understate or overstate actual work. A one-commit session contributes zero duration, not zero work.
- Dates use author timestamps converted to Brasília time; this may differ from the date shown by a contributor's local clock. Results depend on the current reachable Git history and alias mapping above.

## Used in deck
Not used.

## History
- 2026-11-07: Created from all commits reachable at current `HEAD`; grouped aliases and daily times in Brasília time.
- 2026-11-07: Recomputed as commit sessions separated by gaps of 2 hours or more; added per-day and per-user inferred durations.
