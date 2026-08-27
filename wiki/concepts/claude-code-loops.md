---
type: concept
created: 2026-08-10
---
# Claude Code Loops (`/loop`)

The **in-session** automation primitive in Claude Code — repeating a prompt on an interval
while you're actively at your desk. Landed March 2026. Distinct from
[[claude-code-scheduled-tasks|Scheduled Tasks]], which run on a calendar, unattended.

## What it is

`/loop [interval] [prompt]` runs the prompt immediately and then repeats it at the given
interval for the life of the current session (max ~50 iterations). The interval can be in
seconds (`30s`), minutes (`5m`), or hours (`2h`). A bare `/loop` uses a built-in
maintenance prompt.

Two modes:
- **Fixed interval** — clock-based repeat: `/loop 5m check if the Vite dev server is still
  running and report any new errors`. Reliable for polling at a known cadence.
- **Dynamic (self-paced)** — omit the interval; Claude wakes up, checks the condition, and
  schedules its next check based on what it finds — polling faster when something is
  changing, backing off when nothing has changed. Useful for event-driven babysitting.

Anthropic's July 2026 guide gives the full vocabulary: **turn-based loops** (manual, one at
a time) → `/goal` (loop until a verifiable condition holds) → `/loop` (time-triggered,
same session) → `/schedule` (calendar-based, indefinite, fresh sessions each time).

## What it's for

The vault's own [[ramp-ai-agents-every-step]] example: *"Loops = repetitive, known work — a
horizontal slice of the one task every engineer does daily."* Concrete cases:
- Babysitting a PR (check CI every 5 min, post if failed)
- Waiting for a deploy to go green then notify
- Deleting dead code on an interval during a refactor
- Polling an external service for a result

## What it is NOT

- **Not persistent** — stops when the session ends. For work that should continue while you're
  away from your desk, use [[claude-code-scheduled-tasks]] instead.
- **Not a replacement for `/schedule`** — loops are bounded (session + 50-iteration cap);
  scheduled tasks are indefinite and survive machine restarts.
- **Not suited for dynamic/unknown-next-step work** — for that, see [[agentic-workflows]].

## Choosing the right automation shape

| Shape | When | Persistent? |
|---|---|---|
| `/loop` | Same session, repeating check/action, you're at your desk | No |
| `/schedule` | Calendar-based, runs unattended, indefinite | Yes |
| `/goal` | Loop until a verifiable condition is met, then stop | Session |
| [[claude-code-agent-teams|Agent team]] | Parallel tasks, coordinated output | No |

See [[claude-code-scheduled-tasks]] for the unattended lane; [[agentic-automation-patterns]]
for the broader taxonomy.

Related: [[claude-code]] · [[claude-code-scheduled-tasks]] · [[agentic-automation-patterns]] ·
[[claude-code-hooks]] · [[self-healing-workflows]] · [[claude-code-agent-teams]] ·
[[ai-executive-assistant]].
