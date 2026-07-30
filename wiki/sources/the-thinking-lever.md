---
source: youtube
channel: "Anthropic"
url: "https://www.youtube.com/watch?v=T7KqH7kYnE4"
event: "Code with Claude"
speaker: "Alexander Briken (Applied AI research)"
created: 2026-07-24
---

# The thinking lever

Alexander Briken (Applied AI research) on **[[test-time-compute]]** — how Claude spends
tokens at inference to solve harder problems — and the cost/latency/quality tradeoffs of
thinking budgets and effort levels.

## Two axes of intelligence
Performance rises with **model size** (Haiku → Sonnet → Opus, up to ~80% on an internal
agentic-coding benchmark) *and* with **tokens spent thinking** (a log-scale axis) — the two
can reach the same score. Holds across domains: Deep Search QA (reasoning), OSWorld
(computer use), Humanity's Last Exam (PhD-level).

## Effort levels, shown live
Same traffic-simulation prompt on Opus 4.7 at **low / high / max**: low ≈ 50s and ~4,600
tokens (simple); high ≈ 2× (more detail, reactive drivers); max ≈ **10× tokens/time** (best,
physically plausible traffic light, sky scape). More tokens → more time. Extrapolated via
the **METR** benchmark: models handle ever-longer stretches of autonomous human work —
**[[mythos|Mythos]]** ("one of our latest models") ≈ **16 hours** of human work at 50%
accuracy. (Mythos is a real, publicly-unreleased model — see [[mythos]].)

## Three ways to spend test-time compute
1. **Thinking** — a reasoning scratchpad before answering.
2. **Tool calling** — Claude's interface to the outside world (e.g. web search).
3. (continues — sampling / subagents / multiple attempts).

Companion talks: [[picking-the-right-model]], [[the-capability-curve]]. Related:
[[claude-code-permissions|effort/auto controls]], [[outcome-oriented-agents]].

**Raw clip:** [[The thinking lever]]
