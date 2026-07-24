---
source: youtube
channel: "Anthropic"
url: "https://www.youtube.com/watch?v=19HDQ9HppOA"
event: "Code with Claude"
speaker: "Isabella He (MTS, Applied AI)"
created: 2026-07-24
---

# Ship your first Managed Agent

A hands-on Code with Claude workshop (Isabella He, Applied AI) that builds a working
SRE / incident-response agent on [[claude-managed-agents|Claude Managed Agents]] from six
functions, teaching the server-side agent-loop mental model along the way.

## How we got here
- **2023 — Messages API.** Raw model access (tokens in / tokens out). Developers implement
  every primitive themselves: context management, the agent loop, compaction.
- **Agent SDK.** A harness to programmatically drive [[claude-code]]; more power, but *you*
  still manage hosting, scaling, and sandbox safety.
- **Claude Managed Agents.** First Anthropic harness to handle scaling + production
  components for you — purpose-built harness, sandboxing, observability, tool runtime, all
  managed. Claimed **10–15× faster to production**.

Why managed: *harnesses must evolve with models.* Example — Sonnet 4.5 showed
"[[context-anxiety]]" (wrapping up tasks early with context to spare); the team added
mitigations, then [[opus-4-5]] removed the behavior and made that harness work obsolete.
CMA absorbs that maintenance (compaction, caching, context anxiety) so you focus on tasks
and tools.

## The three primitives
- **Agent** — the *brain*: persona + capabilities (model, system prompt, MCP servers,
  skills, tools). In the demo, an SRE agent on Opus 4.7 with a very simple prompt + tools
  (`get_metrics`, `get_recent_deploys`, `get_diff`, fetch logs).
- **Environment** — the *hands*: a sandbox container with a network **allowlist** and
  pre-installed packages. New: bring-your-own containers/compute + MCP tunnels (private MCP
  servers off the public network).
- **Session** — binds an agent instance to an environment, mounts resources (e.g. a log
  file via the Files API), and streams events back to the user.

## Key architecture — [[brain-hands-decoupling|decouple the loop from tool execution]]
The agent loop runs **server-side**; tool execution is separate. Benefits: security
(credentials never exposed to the sandbox, encrypted via [[agent-vaults|vaults]]), latency
(>90% reduction in P95 time-to-first-token vs. loop+tools in one box), reliability (a dead
container respawns without restarting the loop). Close your laptop / hard-refresh and
everything persists — durability, session persistence, and state management
(idle → running → rescheduling → terminated) are handled for you.

## Events, not tokens
A session is a log of **events** (user messages, agent tool calls, agent responses),
streamed for UX (user sees progress) and observability (built-in console). Webhooks can
resume a session or kick a state from external events.

## Beyond the basics (out of the box)
[[claude-code-subagents|Subagents]]/multi-agent orchestration, [[agent-memory|memory]],
[[agent-dreaming|dreaming]] (Claude curates its own memory logs), [[outcome-oriented-agents|outcomes]]
(define a rubric; the agent iterates toward it), [[agent-vaults|vaults]] (per-user/session
encrypted credentials), webhooks, fine-grained permissions, and a console agent builder.

Companion talk: [[production-faster-managed-agents]]. See also [[claude-managed-agents]].
