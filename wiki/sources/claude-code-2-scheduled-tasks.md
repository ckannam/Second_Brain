---
source: youtube
channel: "Nate Herk"
url: "https://www.youtube.com/watch?v=BlNJFa3Btm8"
title: "Claude Code 2.0 Is Finally Here"
created: 2026-07-24
---
# Claude Code 2.0 Is Finally Here (Native Scheduled Tasks)

**Thesis:** Anthropic shipped native **scheduled tasks** in Claude Code — cron-triggered agentic sessions that run on their own, turning Claude Code into a "24/7 AI employee."

## Key points
- Set up via the **Schedule** tab in the desktop app or `/schedule` in any session; pick name, prompt, model, mode, folder, and cadence (hourly/daily/weekly).
- Each run is a full **agentic** session (self-healing, sees the whole project, uses all tools) — not a brittle deterministic script. You *can* make it deterministic by having it just run a script.
- **Gotchas:** computer + desktop app must stay on; missed runs are caught up within 7 days; runs are **stateless** (fresh session, no shared memory).
- **Self-improving loop** pattern: have the task fix its own script, refine its own prompt, and read/overwrite a single "last run" status file for memory.
- Notifications are weak by default — add a [[claude-code-hooks]] sound hook and/or have the task message you when done.
- Currently **desktop-app only** (cron metadata lives there); terminal/VS Code can edit but not create tasks.

Tools/entities: [[claude-code]], [[anthropic]], [[claude-code-scheduled-tasks]], [[claude-code-hooks]]. Related: [[claude-code-loops]], [[ai-executive-assistant]].
