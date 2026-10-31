r"""Rebuild the progress board in STATUS.md from the task and finding files.

Inputs:  tasks/*.md and findings/*.md (front matter between the first two '---' lines; task checkboxes in
         the '## Subtasks' and '## Success criteria' sections), docs/phases.md ('## P1 — Name' headings)
Output:  the block between <!-- BOARD:START --> and <!-- BOARD:END --> in STATUS.md
Run:     python scripts/board.py   (after changing any task or finding; after a git merge conflict in the
         board block, keep either side and re-run)
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
ICON = {"todo": "⬜ todo", "doing": "🔄 doing", "paused": "⏸️ paused", "blocked": "⛔ blocked",
        "review": "👀 review", "done": "✅ done", "dropped": "✖️ dropped", "exploratory": "🔍 exploratory",
        "confirmed": "✔️ confirmed", "frozen": "🧊 frozen", "retracted": "❌ retracted"}


def count(text, section):
    """'done/total' checkboxes in a '## section', or '–' if it has none."""
    m = re.search(rf"^## {section}\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    body = re.sub(r"<!--.*?-->", "", m.group(1), flags=re.S) if m else ""
    done, total = len(re.findall(r"^- \[x\]", body, re.M)), len(re.findall(r"^- \[[ x]\]", body, re.M))
    return f"{done}/{total}" if total else "–"


def meta(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    d = {k.strip(): v.strip() for k, v in (line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)}
    return {**d, "file": path.relative_to(ROOT).as_posix(),
            "steps": count(text, "Subtasks"), "criteria": count(text, "Success criteria")}


def rows(folder):
    return sorted((meta(p) for p in (ROOT / folder).glob("*.md") if not p.name.startswith("_")), key=lambda d: d["id"])


phases = dict(re.findall(r"^## (P\d) — (.+)$", (ROOT / "docs/phases.md").read_text(encoding="utf-8"), re.M))
tasks, findings = rows("tasks"), rows("findings")
for r in tasks + findings:
    if r["status"] not in ICON or r.get("phase", "P0") not in phases:
        print("check status/phase in", r["file"])

out = []
for ph, name in phases.items():
    ts = [t for t in tasks if t["phase"] == ph]
    if not ts:
        continue
    closed = sum(t["status"] in ("done", "dropped") for t in ts)
    out += [f"**{ph} — {name}** ({closed}/{len(ts)} closed)", "",
            "| ID | Task | Status | Owner | Working now | Steps | Criteria | Due | Depends |",
            "|---|---|---|---|---|---|---|---|---|"]
    out += [f"| [{t['id']}]({t['file']}) | {t['title']} | {ICON[t['status']]} | {t['owner']} | {t.get('working', '-')} "
            f"| {t['steps']} | {t['criteria']} | {t['due']} | {t['depends']} |" for t in ts]
    out.append("")
out += ["**Findings**", "", "| ID | Claim | Status | Task | Checked by |", "|---|---|---|---|---|"]
out += [f"| [{f['id']}]({f['file']}) | {f['title']} | {ICON[f['status']]} | {f['task']} | {f['checked_by']} |"
        for f in findings]

status = ROOT / "STATUS.md"
text = status.read_text(encoding="utf-8")
new, n = re.subn(r"(<!-- BOARD:START -->).*?(<!-- BOARD:END -->)",
                 lambda m: m.group(1) + "\n" + "\n".join(out) + "\n" + m.group(2), text, flags=re.S)
if n != 1:
    raise SystemExit("STATUS.md must contain exactly one BOARD:START / BOARD:END marker pair")
status.write_text(new, encoding="utf-8")
print(f"board updated: {len(tasks)} tasks, {len(findings)} findings")
