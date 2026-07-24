---
source: youtube
channel: "Anthropic"
url: "https://www.youtube.com/watch?v=zenIB7XLZxQ"
event: "Code with Claude"
speaker: "Michael & Harrison (MTS, Claude Managed Agents)"
created: 2026-07-24
---

# How to get to production faster with Claude Managed Agents

Michael and Harrison (MTS on the [[claude-managed-agents|Managed Agents]] team) on why
infrastructure — not model intelligence — is now the bottleneck, and how CMA removes it.
Includes a partner panel (Cloudflare, Daytona, Modal, Vercel) on self-hosted sandboxes.

## The capability curve, restated
[[the-capability-curve|Model capability]] went vertical: Opus 3 → generate a test function
(you approve every tool); Opus 4 + [[claude-code]] → drive a whole feature / a PR (you
still steer); **[[opus-4-7]]** → people clear entire backlogs and wake to merge-ready PRs.
Next: **a quarter of work in a few hours** via swarms of agent teams (e.g. an end-to-end
M&A pipeline). At that scale, prompt + tool use isn't enough — you need
[[outcome-oriented-agents|task completion]] and real agent infrastructure.

## Why the infra layer is the bottleneck
To do more, agents need access to more — secure credentials, internal systems, private
repos, and **identity/auth** (an agent is a principal, like an employee with Slack + email).
Research surfaced the sticking points: context management + memory (great when right,
catastrophic when wrong), **infrastructure** (the #1 blocker — reliability, scalability,
security, latency in prod), and **observability** (you can't assess an agent you can't see).
CMA does that platform work so you pick composable primitives off the shelf.

## Getting started
Define an **agent** (config: system prompt, model, skills, tools, permissions) → an
**environment** (sandbox: network allowlist, packages) → kick off a **session** and listen
to the **event stream**. Event domains: user events, agent events, session (lifecycle)
events, span events. Fastest path in: the **Claude API skill** shipped with Claude Code
(knows CMA), plus a **CLI** and copy-paste **cookbooks**. Demo: "Pascal," a grocery-habits
analytics agent, with an "Ask Claude" button that reads the session transcript and suggests
config optimizations.

## Advanced features (announced/recent)
- [[multi-agent-orchestration]] — Claude spawns agent threads with their own context and
  passes messages between them.
- [[outcome-oriented-agents|Outcomes]] — a rubric/goal set Claude grades and loops toward.
- [[agent-memory|Memory]] — long-lived stores; each session better than the last.
- [[agent-dreaming|Dreaming]] (research preview) — reflect over *thousands* of sessions to
  produce/edit memories.
- **Self-hosted sandboxes** (bring-your-own compute in your VPC; partners **Cloudflare,
  Daytona, Modal, Vercel**) and **MCP tunnels** (research preview) — expose private
  [[mcp]] servers to Claude without the public internet.

Companion workshop: [[ship-your-first-managed-agent]]. Hub: [[claude-managed-agents]].
