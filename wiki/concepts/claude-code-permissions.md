---
type: concept
---
# Claude Code Permissions (Auto Mode)

Controls what [[claude-code]] may do without asking. Three postures:
- **Ask before every action** — safe, but constant interruptions.
- **Auto Mode** — a **risk classifier** checks each action; safe ones run, risky ones get flagged. The recommended middle ground. Src: [[claude-code-auto-mode-permissions]].
- **Dangerously skip permissions** — full autonomy, no checks.

Pair Auto Mode with deny-rules (e.g. block destructive `rm`) so unattended runs ([[claude-code-scheduled-tasks]]) can't go off the rails. Related: [[claude-code-hooks]]. This is the concrete control for the broader [[agent-security-risks]] threat model (least privilege on a tool-wielding agent).
