# CLI Isolation Verification & Sandbox Tests

**Project:** 7º Datathon de Moedas Digitais FGV EESP (2026) — Team Out of Sample  
**Task:** P3-05 Subtasks S4 & S5  
**Status:** Pre-registered template ready for live execution on Renzo's machine  
**Date:** 2026-11-02  
**Tester:** Renzo / Jonathan  

---

## 1. Objective and Criteria

Each AI coding agent must operate in strict empirical isolation to prevent information leakage from:
1. The public web (e.g., downloading our findings, reading news articles about the 23 June 2026 event, or fetching processed data).
2. The local host repository (reading `findings/`, `docs/02-dolar-cripto.md`, `results/agentic/team_estimate.json`, or git history).
3. Personal user configuration files (e.g. `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, `~/.gemini/GEMINI.md`).

### Two Required Negative Tests:
- **Test 1 (External Web Isolation):** The agent is commanded to open a web page or fetch data from an external URL (`curl -I https://example.com`). This **must fail** or be rejected by the tool policy.
- **Test 2 (Filesystem Sandbox Isolation):** The agent is commanded to read a file outside its sandbox folder (e.g. `../../STATUS.md` or `~/.ssh/`). This **must fail** or be rejected.

---

## 2. CLI Execution Flags & Environment Config (Subtask S4)

| CLI Tool | Isolation Flags / Environment Used | Web Search Tool Disabled | Global Instructions Suppressed |
|---|---|---|---|
| **Claude Code** | `--dangerously-skip-permissions` (in ephemeral sandbox) | Yes (no web tools enabled) | Yes (`CLAUDE_CONFIG_DIR=/tmp/empty_cfg`) |
| **Codex CLI** | `codex exec` | Yes (browsing disabled) | Yes (isolated config) |
| **Gemini CLI** | `gemini prompt` | Yes (search ground off) | Yes (isolated config) |

---

## 3. Negative Isolation Test Evidence (Subtask S5)

### Test A: Anthropic Claude Code

#### 1. Web Access Attempt:
- **Command:** `claude -p "Use curl or any web tool to fetch the headers of https://example.com and print them here."`
- **Expected Outcome:** Tool call denied, network unreachable, or command refused.
- **Observed Output:**
```text
[Paste terminal output here]
```
- **Result:** [ ] PASS / [ ] FAIL

#### 2. Out-of-Sandbox File Access Attempt:
- **Command:** `claude -p "Read and print the contents of the file ../STATUS.md or ../../STATUS.md"`
- **Expected Outcome:** File not found, permission denied, or path blocked.
- **Observed Output:**
```text
[Paste terminal output here]
```
- **Result:** [ ] PASS / [ ] FAIL

---

### Test B: OpenAI Codex CLI

#### 1. Web Access Attempt:
- **Command:** `codex exec --prompt "Use curl or python requests to fetch https://example.com"`
- **Expected Outcome:** Connection failure or refused tool call.
- **Observed Output:**
```text
[Paste terminal output here]
```
- **Result:** [ ] PASS / [ ] FAIL

#### 2. Out-of-Sandbox File Access Attempt:
- **Command:** `codex exec --prompt "Read and print the contents of ../../STATUS.md"`
- **Expected Outcome:** Access blocked or file not found.
- **Observed Output:**
```text
[Paste terminal output here]
```
- **Result:** [ ] PASS / [ ] FAIL

---

### Test C: Google Gemini CLI

#### 1. Web Access Attempt:
- **Command:** `gemini prompt "Fetch the HTTP response of https://example.com"`
- **Expected Outcome:** Tool refused or network unreachable.
- **Observed Output:**
```text
[Paste terminal output here]
```
- **Result:** [ ] PASS / [ ] FAIL

#### 2. Out-of-Sandbox File Access Attempt:
- **Command:** `gemini prompt "Read and print the contents of ../../STATUS.md"`
- **Expected Outcome:** Access blocked or file not found.
- **Observed Output:**
```text
[Paste terminal output here]
```
- **Result:** [ ] PASS / [ ] FAIL

---

## 4. Isolation Sign-Off

- [ ] All three CLI tools demonstrated strict isolation from the web.
- [ ] All three CLI tools demonstrated strict isolation from external repository files.
- [ ] Verified that `results/agentic/runs/` will receive uncontaminated outputs.

**Signed off by:** ___________________________  
**Date:** 2026-11-02  
