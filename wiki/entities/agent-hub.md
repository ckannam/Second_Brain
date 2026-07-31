---
type: entity
category: tool
---
# Agent Hub

[[andrej-karpathy]]'s companion project to [[autoresearch]] (open-sourced right after it) — **"GitHub is for humans; AgentHub is for agents."** An **agent-first collaboration platform**: a bare git repo plus a **message board** designed for a *swarm* of agents working on the same codebase.

Deliberately strips the human-oriented git workflow: **no main branch, no PRs, no merges** — just "a sprawling DAG of commits in every direction" with a board where agents coordinate. Described (by [[greg-isenberg]]) as an "exploratory" project whose first use case is autoresearch but "a lot more general than that."

Fits the trajectory in [[extending-the-llm-wiki]] and the broader move toward [[multi-agent-orchestration|multi-agent]] / [[parallel-agents|parallel-agent]] systems: if [[autoresearch]] is one agent looping on one file, Agent Hub is the substrate for **many agents** looping together. Source: [[autoresearch-broke-internet-greg-isenberg]].

## How it works (web-grounded 2026-07-31)

The whole system is deliberately tiny: **one Go binary (`agenthub-server`), one SQLite database, one bare git repo on disk** — no containers, no heavy dependencies. Two layers:

- **Git layer (code).** Agents share code as **git bundles** (compressed git objects). The server validates a bundle, then unbundles it into the shared bare repo. Instead of branch/PR/merge, agents: push commits via bundles; fetch any commit by hash; **browse the commit DAG** and query its structure — *children*, *leaves* (frontier commits), *lineage* (ancestry), and diffs between arbitrary commits. Merges never happen; the DAG just sprawls, and interesting frontier commits are found by inspection rather than promoted by a merge.
- **Coordination layer (talk).** A **threaded message board** with channels sits alongside git. Agents post results, hypotheses, failures, and coordination notes asynchronously — sharing insight without blocking on code operations.
- **Guardrails.** Each agent gets an **API key**; the server enforces a **bundle-size cap (default 50 MB)** and a **per-agent rate ceiling (~100 pushes/posts per hour)** — the minimum needed to keep a swarm from trampling the shared repo.

**First use case:** organizing [[autoresearch]] agents — "simulated PhD students" optimizing LLM training — into an internet-scale **"autonomous agent-first academia,"** where anyone can point an agent at the platform and have it collaborate.

**Status (per README, 2026-07-31): "Work in progress. Just a sketch. Thinking…"** — an active experiment, not a stable release, though it has drawn heavy attention (tens of thousands of GitHub stars and community forks, e.g. `ottogin/agenthub`). Treat the design as directional, not settled.

## Relevance to this vault (evaluation)

*The [[tasks/index|action item]] was to judge whether Agent Hub is relevant to this vault's multi-agent direction. Verdict: **conceptually load-bearing, operationally not yet — watch, don't adopt.***

- **Not a fit for the current single-writer loop.** This vault's whole discipline is the opposite of Agent Hub's design: [[vault-autoresearch]] runs the git **ratchet** on a *linear* history — one heal per iteration, kept only if `score.py`'s HEALTH_DEBT strictly drops, with `main` as the reviewed source of truth and one morning PR. Agent Hub throws out exactly the primitives the ratchet depends on — **a main branch, merges, and a human-reviewable PR** — in favor of a never-collapsed DAG. Adopting it today would remove the very control surface that keeps the unattended loop safe.
- **Where it *would* matter: the parallelism rung.** [[extending-the-llm-wiki]] names "parallelize; you're the bottleneck" as an open rung, and [[multi-agent-orchestration]] / [[parallel-agents]] as the escalation path for big ingests and lints. Agent Hub is the natural *substrate* for that rung — many enrich/lint agents exploring the graph at once, posting findings to a board — **if** paired with a collapse step that promotes a chosen frontier commit back onto the reviewed `main`. The vault's ratchet is precisely such a collapse rule: DAG-explore many candidate heals in parallel, then let HEALTH_DEBT + the morning PR pick the one that lands.
- **The transferable idea (usable now, no new infra): the message board.** Even without the git substrate, the "agents coordinate through an async threaded board" pattern maps directly onto `log.md` + `results.tsv` + `nightly-queue.md` — this vault's existing cross-run memory. That's already a lightweight, single-agent version of Agent Hub's coordination layer.
- **Net.** Keep watching Agent Hub as the reference design for *if/when* this vault escalates from one nightly agent to a swarm — but the near-term multi-agent gain is [[claude-code-subagents|sub-agents]]/parallel fan-out under the existing ratchet, not a branch-less DAG. Re-evaluate when Agent Hub graduates from "just a sketch" and when a real ingest/lint backlog justifies parallel writers.

Related: [[autoresearch]] · [[vault-autoresearch]] · [[extending-the-llm-wiki]] · [[multi-agent-orchestration]] · [[parallel-agents]] · [[andrej-karpathy]].
