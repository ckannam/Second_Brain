---
source: youtube
channel: "Nate Herk"
url: "https://www.youtube.com/watch?v=OUyfxhFtGCo"
title: "This New Claude Code Feature is a Game Changer"
created: 2026-07-24
---
# This New Claude Code Feature is a Game Changer (Loops)

**Thesis:** Claude Code can now **loop** — run recurring tasks, set reminders, and repeat skills on an interval for up to **3 days** with no input.

## Key points
- Powered by **cron tools** under the hood; invoked with a loop/interval feature distinct from scheduled tasks.
- Good for continuous polling / repeated skill runs within a bounded window (≤3 days).
- **Loops vs [[claude-code-scheduled-tasks]]:** loops run on a short repeating interval inside a session window; scheduled tasks are calendar-based, indefinite, and spawn fresh stateless sessions.
- Same limitations family as scheduled tasks (machine must stay on).

Tools/entities: [[claude-code]], [[claude-code-scheduled-tasks]]. Concept: [[agentic-automation-patterns]].
