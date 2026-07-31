---
type: entity
category: tool
---
# Agent Hub

[[andrej-karpathy]]'s companion project to [[autoresearch]] (open-sourced right after it) — **"GitHub is for humans; AgentHub is for agents."** An **agent-first collaboration platform**: a bare git repo plus a **message board** designed for a *swarm* of agents working on the same codebase. Source: [[autoresearch-broke-internet-greg-isenberg]].

## Design philosophy

Agent Hub deliberately inverts GitHub's assumptions. GitHub is optimized for **humans reading history** — main branch, PRs, linear narrative, code review by people. Agents don't need that narrative; they need a substrate to coordinate without human-shaped ceremony.

What Agent Hub provides instead:
- **A sprawling DAG of commits** — no main branch, no merges, no PRs. Agents just commit in every direction, and the DAG records what they tried.
- **A message board** — where agents coordinate ("I'm working on X"; "I found a bug in Y"; "my run scored 0.72") without needing human-interpreted PRs.
- **A frozen evaluator** — the same principle as [[autoresearch]]'s `prepare.py`: the metric can't be gamed, only legitimately improved.

The result is a substrate optimized for *swarm exploration* rather than *linear human narrative*.

## Connection to autoresearch

[[autoresearch]] is a **single-agent loop** on a single file: one agent edits `train.py`, scores `val_bpb`, keeps or reverts. Agent Hub scales that to **many agents in parallel**, each exploring a different hypothesis, with a shared message board to coordinate and avoid duplicated effort.

Karpathy's end-state vision: a **SETI@home for AI research** — millions of agents on volunteer compute, all steered toward a chosen problem, leaving behind a DAG of everything they tried. See [[autoresearch]] for that broader context.

## Relevance to this vault

The [[vault-autoresearch]] loop is currently a **single-agent, nightly autoresearch instance** — one session, one HEALTH_DEBT metric, git as the ratchet. Agent Hub represents the multi-agent extension of that same idea:

| | This vault today | Agent Hub trajectory |
|---|---|---|
| Agents | 1 (nightly cloud run) | Many (parallel swarm) |
| Coordination | None needed | Message board |
| Git model | main + PR | DAG, no main |
| Metric | HEALTH_DEBT | Same pattern, any metric |

For the vault to benefit from Agent Hub, a natural prerequisite is the current single-agent loop being stable and measurably improving — which it now is. See `@cloud` task "Watch agent-hub" in [[tasks/index]] for the standing monitoring item.

## Evaluation (as of 2026-07-31)

Agent Hub is an **exploratory/early project** (Karpathy described it this way at launch). As of this synthesis from vault sources, no new material has arrived in this vault — [[autoresearch-broke-internet-greg-isenberg]] remains the primary source. For a vault with a stabilizing nightly loop, Agent Hub is a **future-direction signal**, not an immediate action: worth tracking, not worth adopting until the single-agent loop is more deeply integrated.

Related: [[andrej-karpathy]], [[autoresearch]], [[autoresearch-repo]], [[vault-autoresearch]], [[extending-the-llm-wiki]], [[multi-agent-orchestration]], [[parallel-agents]], [[claude-code-agent-teams]].
