---
source: youtube
channel: "Anthropic"
url: "https://www.youtube.com/watch?v=IGo225tfF2I"
event: "Code with Claude"
speaker: "Ravi (leads API Knowledge team, Platform)"
created: 2026-07-24
---

# Memory and dreaming for self-learning agents

Ravi (API Knowledge team) on the two features that turn [[claude-managed-agents]] into
self-learning systems: **[[agent-memory|memory]]** and **[[agent-dreaming|dreaming]]**.

## Why memory
Timeline: MCP (2024) → [[claude-code]] + Agent SDK (2025) → Skills → Managed Agents (last
month). Through-line: agents operate over longer horizons (METR: task length doubling ~every
7 months). Memory lets agents **carry learnings forward** — task→task, environment→
environment, and **agent→agent** (swarms sharing an org's understanding). Goal: each task
better than the last. Results cited: **Rakuten −97% first-pass errors**, **WiseDocs**
cross-session memory in doc verification.

## How memory is designed
"Get out of Claude's way — let it cook." Memory is modeled as a **file system** (like
[[claude-code-skills|skills]]); [[opus-4-7]] is SOTA at file-system memory, good at judging
what to save for its future self. Three architecture layers: **storage** (tracked changes),
**structure** (format Claude reads best), **Claude-driven processing** (agents take notes
as they work). Multi-agent: shared stores with **read-only vs read-write scopes** (org-wide
read-only + granular read-write → a hierarchy), **optimistic concurrency control** for write
conflicts, enterprise controls (version history, diffs, attribution), and a **standalone
memory API** (CRUD + exports/redactions).

## Dreaming
Scaling memory surfaced a problem: updates were **locally but not globally optimal** —
agents repeated each other's mistakes, memory duplicated/fragmented. **Dreaming** (research
preview) is an **out-of-band batch process**, fully decoupled from the agent loop: it reads
cross-session/cross-agent transcripts, finds mistake patterns, and curates/reconciles memory
into a **verified, better-organized snapshot** agents can adopt. Trigger ad-hoc / nightly /
hourly / on session-end via API. Benefits: cross-agent pattern detection, clear objectives
(no task-vs-memory tradeoff), **zero added latency** (off the hot path). Result: **Harvey
6× completion rate** on a legal benchmark. "Shared, improving memory raises the floor for
every agent; dreaming raises it further."

> Distinct from Claude Code's consumer "[[claude-code-memory|Auto Dream]]" — same metaphor,
> but this is the Managed Agents platform primitive. Related:
> [[production-faster-managed-agents]], [[ship-your-first-managed-agent]].
