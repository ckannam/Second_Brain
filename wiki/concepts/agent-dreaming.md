# Agent dreaming

An **out-of-band batch process** that curates and reconciles [[agent-memory]] between
sessions — the [[claude-managed-agents]] "frontier memory" feature (research preview), from
[[memory-and-dreaming-self-learning-agents]].

**Problem it solves:** as memory scaled across many sessions/agents, updates were **locally
optimal but not globally optimal** — agents repeated each other's mistakes, memory
duplicated and fragmented.

**How it works:** fully **decoupled from the agent loop**. Each run reads cross-session /
cross-agent transcripts, finds mistake patterns, and proposes a **verified, better-organized
snapshot** of memory that agents can adopt. Triggerable ad-hoc, nightly, hourly, or on
session-end via API.

**Why out-of-band matters:** cross-agent pattern detection a single agent couldn't spot;
**clear objectives** (no tradeoff between improving memory and finishing the task); and
**zero added latency** (off the hot path). Result cited: **Harvey 6× completion rate** on a
legal benchmark. "Shared, improving memory raises the floor for every agent; dreaming raises
it further."

> Same "sleep/dream" metaphor as Claude Code's consumer **[[claude-code-memory|Auto Dream]]**
> (a background sub-agent consolidating memory), but this is the multi-agent **platform**
> version. Related: [[outcome-oriented-agents]], [[multi-agent-orchestration]].

The metaphor is load-bearing: this is the machine mirror of human **[[memory-consolidation]]** —
an out-of-band replay pass that reorganizes memory off the hot path, exactly what the brain does
during sleep ([[neuroscience-of-behavior]]).
