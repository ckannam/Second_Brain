---
type: concept
created: 2026-08-10
---
# Skills vs Sub-agents

The two primary reuse primitives in Claude Code — and the choice between them is a
**context-boundary decision**, not a complexity one. The authoring craft lives on
[[writing-reliable-skills]]; the full orchestration ladder (skill → sub-agent → team → CMA)
is in the [[orchestrate-agents]] skill.

## The core distinction

| | **Skill** | **Sub-agent** |
|---|---|---|
| What it is | Packaged instructions loaded *into the current context window* when triggered | A separate Claude instance with its **own** context window |
| Token cost | ~100 tokens at startup; body only when triggered | Full new context window per invocation |
| Trigger | Automatic — description match at startup | Explicit — orchestrator calls it |
| Ideal for | Repeatable procedure in the same conversation | Context isolation, heavy reads, parallel work |
| Composable? | Yes — a skill can instruct Claude to spawn sub-agents | Yes — sub-agents can load skills of their own |

## The decision rubric

**Reach for a skill when:**
- The same procedure recurs across sessions ("always do X when Y").
- The task fits comfortably in the current context window.
- You want automatic triggering from a description match — no explicit call needed.

**Reach for a sub-agent when:**
- The task needs its own clean context window (e.g. reading 10+ files would bloat the parent).
- Work can run in **parallel** with the main session or other sub-agents.
- You want **adversarial / QA isolation** — a fresh Claude B that hasn't seen Claude A's reasoning.
- The task is one-shot and doesn't need to be reused — spawning is cheaper than authoring a skill.

**Escalate to an agent team when:**
- Multiple sub-agents must coordinate, share state, or produce a jointly-synthesized result.
- The job exceeds one context window's capacity even with compaction.
- (See [[claude-code-agent-teams]] and the [[orchestrate-agents]] decision ladder.)

## Why the distinction matters

Choosing wrong costs either tokens or context clarity:
- A sub-agent for a simple repeatable step wastes a full context window and loses the
  auto-trigger convenience of a skill.
- A skill for a heavy read-intensive task bloats the parent window and blocks parallelism.

The guiding question is: **"Does this task need its own context boundary?"** If yes → sub-agent.
If it can share the current window and recurs → skill.

Context economics is explained on [[token-context-management]]; the portable skill format
(one format across Claude Code, claude.ai, and the API) is on [[agent-skills]].

## The reuse ladder

```
skill           → reusable procedure, in-context, triggered automatically
sub-agent       → isolated context, explicit, one-off or parallel
agent team      → coordinated sub-agents, shared state, parallel synthesis
Claude Managed  → server-side orchestration, long-running, production-grade
  Agents (CMA)
```

Each rung is appropriate at a different scale and isolation need. Don't skip rungs: a
simple repeatable procedure doesn't need a CMA; a production pipeline doesn't want a
fragile in-context skill.

Related: [[claude-code-skills]] (the skill overview) · [[writing-reliable-skills]] (authoring
craft) · [[claude-code-subagents]] (sub-agent mechanics) · [[claude-code-agent-teams]]
(coordinating multiple sub-agents) · [[token-context-management]] (context economics) ·
[[agent-skills]] (portable skill format) · [[orchestrate-agents]] (the full decision ladder
as a skill) · [[multi-agent-orchestration]] · [[build-sell-claude-code-course]].
