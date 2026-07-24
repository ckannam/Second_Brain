# Claude Code Scheduled Tasks

Native cron-triggered **autonomous agentic sessions** ([[claude-code-2-scheduled-tasks]]). Set via the Schedule tab or `/schedule`; each run is a fresh, **stateless**, self-healing agent with full project access.

## Patterns & gotchas
- **Self-improving loop:** the task fixes its own script, refines its own prompt, and reads/overwrites a single "last run" status file for cross-run memory.
- **Gotchas:** machine + desktop app must stay on; missed runs caught up within 7 days; desktop-app-only for creation.
- **Safety:** pair with [[claude-code-permissions|Auto Mode]] + deny-rules so unattended agents can't go off the rails.
- **vs [[claude-code-loops|Loops]]:** scheduled = calendar-based, indefinite, fresh sessions; loops = short repeating interval, ≤3 days.

The engine behind Level 5 of the [[ai-second-brain-levels]] and always-on [[ai-executive-assistant|executive assistants]].

## Run-while-you-sleep loops
The same "kick off before bed, wake up to a log of results" idea powers [[autoresearch]]: a fixed 5-min experiment budget yields ~100 unattended runs overnight. Creators schedule the business version with **GitHub Actions cron** rather than the native scheduler — e.g. [[nick-saraev]]'s hourly cold-email optimizer ([[claude-code-karpathy-autoresearch-nick-saraev]]). Native scheduled tasks and an external cron are two routes to the same unattended-loop shape; both pair well with a single status/results file for cross-run memory.
