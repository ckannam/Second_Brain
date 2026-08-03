---
type: concept
created: 2026-08-03
---

# Agent-Native Infrastructure

A design pattern surfaced most sharply by [[andrej-karpathy]]'s [[agent-hub]]: when the
primary user of a piece of developer infrastructure becomes an **LLM agent (or a swarm of
them)** rather than a human, you don't bolt agents onto human-shaped tools — you **rebuild the
tool around the agent**, stripping the ceremony that only existed to help humans read, review,
and narrate. Filed 2026-08-03 as the MODE B proposal generalizing the night's `[[agent-hub]]`
research.

## Human-native vs agent-native

Most developer tools optimize for a **human reading a linear narrative**: a main branch, pull
requests, code review, changelogs, prose docs. That ceremony is *for the human* — the agent
doesn't get bored, doesn't need a tidy story, and can hold far more context than a reviewer.
Agent-native tooling asks the opposite question: *what is the minimum substrate a swarm needs
to coordinate, and what data structure replaces the human ritual?*

| Layer | Human-native (today) | Agent-native (the pattern) | Instance |
|---|---|---|---|
| Version control | main branch · PRs · merges · review | a **DAG of commits** + a message board; no main | [[agent-hub]] |
| Coordination | meetings, PR threads, standups | **channels + threaded replies** on a board | [[agent-hub]] |
| Quality gate | human code review, taste | a **frozen, un-gameable metric** the loop optimizes | [[autoresearch]] (`val_bpb`) · [[vault-autoresearch]] (`HEALTH_DEBT`) |
| Docs / context | READMEs, tribal knowledge | a **single machine-read schema** the agent obeys | `AGENTS.md` (this vault) · Karpathy's `agents.md` |
| Navigation | folder intuition, search | an explicit **catalog + append-only log** | `index.md` + `log.md` |

The throughline: **coordination becomes a data structure** (a DAG, a board, a metric, a
schema) instead of a social process. That is exactly what makes it cheap for an agent and
legible to a swarm.

## Why it's the same instinct as autoresearch

[[autoresearch]]'s core move is to make the **bookkeeping** near-free so the agent can run the
loop unattended — a frozen evaluator it can't game, git as the ratchet. Agent-native
infrastructure pushes that same instinct **down into the tooling layer**: don't just automate
the human's workflow, remove the parts of the workflow that only existed *because* a human was
in the loop. [[agent-hub]]'s reference build makes this concrete — one Go binary + SQLite + a
bare git repo, agents pushing **git bundles** and coordinating on a **channel board** — the
whole platform is small precisely because it drops the human-facing surface area.

## When it's premature (the honest caveat)

Agent-native infrastructure only pays off once there is genuinely a **swarm** that needs to
coordinate on shared state. For a **single-agent** system, the human-native tools are still
correct — a main branch and a reviewed PR are *features*, because the human is still the
reviewer of record. This is exactly why the [[agent-hub]] verdict for this vault is "track,
don't adopt": the [[vault-autoresearch]] loop is one nightly agent, so it rides `main` + a
morning PR ([[claude-code-agent-teams]] / [[multi-agent-orchestration]] is the realistic
bridge, not a no-main-branch DAG). The pattern is a **direction of travel**
([[extending-the-llm-wiki]]), useful to name now so the vault recognizes the moment it
actually needs it.

## Where this vault already sits on the spectrum

This vault is a partial, deliberate instance: **`AGENTS.md` as the single machine-read
schema** and **`index.md`/`log.md` as the catalog+log** are agent-native (a schema the agent
obeys, not prose for a human), while **version control stays human-native** (main + reviewed
PR) because there's one agent and Cole is the reviewer. It is agent-native where a swarm would
be overkill and human-native where the human still adds the judgment — which is the correct
place to be for a stable single-agent loop.

Related: [[agent-hub]], [[autoresearch]], [[vault-autoresearch]], [[extending-the-llm-wiki]],
[[llm-wiki-pattern]], [[multi-agent-orchestration]], [[claude-code-agent-teams]],
[[parallel-agents]], [[self-healing-workflows]], [[second-brain-system]].
