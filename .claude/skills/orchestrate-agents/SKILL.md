---
name: orchestrate-agents
description: Use when Cole asks how to orchestrate multiple Claude Code agents, set up an agent team, parallelize work across agents, assign QA roles, or asks about sub-agents vs. agent teams vs. Claude Managed Agents. Also triggers on "I want agents to work together", "parallel agents", "agent swarm", or "QA agent".
---

# Agent Orchestration

Decision guide for choosing and setting up multi-agent patterns in Claude Code. Full
concepts: [[claude-code-agent-teams]], [[claude-code-subagents]], [[multi-agent-orchestration]].

## Pick your pattern first

```
Single agent     → simple, sequential task
Sub-agent        → scoped, isolated subtask (no peer feedback needed)
Agent team       → tasks that benefit from parallelism + cross-review / QA
CMA platform     → production scale, shared memory, dreaming, outcome-orientation
```

Rule of thumb: **sub-agent when tasks can be isolated; team when tasks gain from
collaboration or QA.** See [[skills-vs-subagents]] for the full ladder.

## Sub-agents (parent → helper)
- Spawn with the **agent tool**; each gets its own context window.
- Best for: heavy file reads, isolated research, or anything that would bloat the
  parent thread. Context isolation is as much the point as delegation.
- The parent reviews and integrates the output.

## Agent teams (peer ↔ peer)
Key rules from [[claude-code-agent-teams]]:
1. **Prompt each agent clearly for its role** — agents that know their lane work better.
2. **Assign a QA/reviewer agent explicitly** — don't assume review happens by default.
3. **Start with 2–3 agents** — complexity compounds fast; keep teams small.
4. **Watch a [[tmux]] split-pane** — one pane per agent makes the swarm visible and
   debuggable during early runs.
5. **Scope write permissions to non-overlapping files** — or use a coordinator agent that
   merges outputs — to avoid agents clobbering each other.

## Common pitfalls
| Pitfall | Fix |
|---|---|
| Agents step on each other's writes | Scope each agent to separate files/dirs |
| Team produces inconsistent output | Add an explicit QA/merger agent |
| Context accumulates too fast | Sub-agents for heavy work; `/compact` the parent |
| Hard to debug what each agent did | tmux split-pane; label each agent's role clearly |

## When to escalate to [[claude-managed-agents]]
CMA handles shared [[agent-memory]], [[agent-dreaming]] (cross-session distillation),
and [[context-anxiety]] automatically. Reach for it when:
- Multiple agents need shared persistent state across sessions.
- The team is a production system (not a one-off experiment).
- You want outcome-oriented orchestration without building the harness yourself.

Related: [[claude-code-agent-teams]], [[claude-code-subagents]], [[parallel-agents]],
[[multi-agent-orchestration]], [[skills-vs-subagents]], [[agent-observability]],
[[claude-managed-agents]], [[tmux]].
