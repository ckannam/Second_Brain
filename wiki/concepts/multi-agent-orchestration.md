---
type: concept
---
# Multi-Agent Orchestration

Coordinating many specialized agents toward a goal. Spectrum in the vault: [[claude-code-agent-teams]] (peer collaboration/QA) → [[paperclip]]'s [[ai-agent-company|AI company]] (a CEO agent hires and delegates, with heartbeats/routines/budgets) → [[openclaw]]. Related: [[parallel-agents]].

**Platform primitive — [[claude-managed-agents]] subagents:** an orchestrator spawns agent threads, each with its **own context window**, and passes messages between them ([[production-faster-managed-agents]]) — the managed version of [[claude-code-subagents|Claude Code subagents]]. It composes with the other CMA features: shared [[agent-memory]] (with read/write scopes so a swarm keeps a common understanding), [[agent-dreaming]] (cross-agent memory reconciliation that a single agent couldn't do alone), and [[outcome-oriented-agents|outcomes]]. Real builds: [[omni]]'s analytics harness; [[elicit]]'s writer/interpreter/critique loop over an [[agentic-dsl]].
