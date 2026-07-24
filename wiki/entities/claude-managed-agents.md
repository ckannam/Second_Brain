# Claude Managed Agents (CMA)

[[anthropic|Anthropic]]'s managed platform for building **production-grade agents** — the
first Anthropic harness that handles scaling, sandboxing, observability, and tool runtime
for you, so developers configure tasks/tools instead of infrastructure. Claimed **10–15×
faster to production**. Sits at the end of the lineage: Messages API (2023) → Agent SDK
(drives [[claude-code]], you host) → **Managed Agents** (Anthropic hosts the loop).

## Three primitives
- **Agent** — the brain: system prompt, model, [[mcp]] servers, [[claude-code-skills|skills]],
  tools, permissions.
- **Environment** — the hands: a sandbox container (network allowlist, packages). Supports
  bring-your-own compute / self-hosted sandboxes (Cloudflare, Daytona, Modal, Vercel) and
  [[mcp|MCP tunnels]].
- **Session** — binds agent + environment, streams **events** (not tokens), persists
  server-side.

## Defining ideas
- [[brain-hands-decoupling]] — the loop runs server-side, decoupled from tool execution →
  security, >90% P95 TTFT reduction, resilient container respawn, durable/persistent
  sessions with managed state (idle → running → rescheduling → terminated).
- Events model + built-in observability console; webhooks resume sessions on external
  events.
- Out-of-box: [[multi-agent-orchestration]]/[[claude-code-subagents|subagents]],
  [[agent-memory]], [[agent-dreaming]], [[outcome-oriented-agents|outcomes]],
  [[agent-vaults]], fine-grained permissions, console agent builder.

Sources: [[ship-your-first-managed-agent]] (SRE demo, Isabella He),
[[production-faster-managed-agents]] (Michael & Harrison, partner panel). Related:
[[claude-code]], [[agent-observability]], [[the-capability-curve]].
