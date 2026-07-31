---
type: concept
created: 2026-07-31
---
# Claude Code Agent Teams

Multiple [[claude-code]] agents running **in parallel**, able to communicate with each other
and QA each other's work — the peer-collaboration layer above single-agent and sub-agent
patterns. Sources: [[claude-code-agent-teams|Nate Herk source]], [[build-sell-claude-code-course]].

## What makes them different from sub-agents

| | [[claude-code-subagents\|Sub-agents]] | Agent Teams |
|---|---|---|
| **Relationship** | Parent → helper (one-way delegation) | Peers (many ↔ many) |
| **Context** | Each has its own context window | Each has its own context window |
| **Cross-talk** | No — results return to parent | Yes — agents coordinate during execution |
| **QA** | Parent reviews the output | Team members review each other |
| **Best for** | Isolating a heavy, independent task | Tasks that benefit from cross-review |

The rule of thumb: **use a sub-agent when tasks can be isolated; use a team when tasks gain
from collaboration or QA**. See [[skills-vs-subagents]] for the full decision tree (skills →
sub-agents → teams, roughly ascending in coordination overhead).

## How it works in Claude Code

Agent teams run inside a single Claude Code session. Agents are spawned with the **agent
tool** (or equivalent), given different roles or responsibilities, and can message each
other while working. The standard observability setup is a **[[tmux]] split-pane** view:
each pane shows one agent's thinking and tool use in real time, making the swarm visible
and debuggable.

Key dos (from Nate Herk's video):
- **Prompt each agent clearly for its role** — agents that know their lane work better.
- **Assign a QA/reviewer agent explicitly** — don't assume QA happens by default.
- **Keep team size small** — start with 2–3 agents; complexity compounds fast.
- **Watch the tmux panes live** during early runs — common pitfalls reveal themselves
  quickly when you can see what each agent is doing.

Common pitfall: agents stepping on each other's work when given overlapping write access.
Fix: scope each agent's write permission to non-overlapping files/directories, or use
a coordinator agent that merges outputs.

## Where they fit in the orchestration spectrum

[[multi-agent-orchestration]] describes the full spectrum: **agent teams** (peer
collaboration + QA) → [[paperclip]]'s [[ai-agent-company|AI-company]] model (a CEO agent
hires/delegates with budgets and heartbeats) → [[claude-managed-agents]] at the platform
level (orchestrator spawns agent threads that share [[agent-memory]] and benefit from
[[agent-dreaming]]).

Agent teams are the **developer's native multi-agent entry point** — no managed platform
required, just Claude Code + good prompts. They enable [[parallel-agents|parallel work]]
at the cost of more prompt engineering.

## Observability

Watching an agent team in a [[tmux]] split-pane is the baseline. [[pixel-agents]] takes
this further with a visual animated "pixel office" — each agent rendered as a character
doing work in real time. See [[agent-observability]].

## Decision guide

```
Single agent     → simple, sequential task
Sub-agent        → scoped, isolated subtask (no peer feedback needed)
Agent team       → tasks that benefit from parallelism + cross-review
CMA platform     → production scale, shared memory, dreaming, outcomes
```

Related: [[claude-code-subagents]], [[parallel-agents]], [[multi-agent-orchestration]],
[[skills-vs-subagents]], [[agent-observability]], [[tmux]], [[claude-managed-agents]].
