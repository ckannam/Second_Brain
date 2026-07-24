---
type: entity
category: tool
---
# Agent Hub

[[andrej-karpathy]]'s companion project to [[autoresearch]] (open-sourced right after it) — **"GitHub is for humans; AgentHub is for agents."** An **agent-first collaboration platform**: a bare git repo plus a **message board** designed for a *swarm* of agents working on the same codebase.

Deliberately strips the human-oriented git workflow: **no main branch, no PRs, no merges** — just "a sprawling DAG of commits in every direction" with a board where agents coordinate. Described (by [[greg-isenberg]]) as an "exploratory" project whose first use case is autoresearch but "a lot more general than that."

Fits the trajectory in [[extending-the-llm-wiki]] and the broader move toward [[multi-agent-orchestration|multi-agent]] / [[parallel-agents|parallel-agent]] systems: if [[autoresearch]] is one agent looping on one file, Agent Hub is the substrate for **many agents** looping together. Source: [[autoresearch-broke-internet-greg-isenberg]].
