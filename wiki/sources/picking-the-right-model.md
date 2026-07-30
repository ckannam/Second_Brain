---
source: youtube
channel: "Anthropic"
url: "https://www.youtube.com/watch?v=P0uMXS6emHA"
event: "Code with Claude"
speaker: "Lucas (Applied AI)"
created: 2026-07-24
---

# Picking the right model

Lucas (Applied AI) on building a **repeatable process** to decide, each time a new model
ships, whether to adopt it for *your* use case — i.e. build an [[eval-driven-model-selection|eval]].

## The decision
Baseline heuristic: need intelligence → **Opus**; need low latency/cost → **Haiku**;
balance → **Sonnet**. Then it gets deep: effort/thinking levels (Sonnet max-thinking vs
Opus low-thinking vs Haiku no-thinking) and cross-provider comparisons. Frame the choice on
three pillars: **quality** (task completion / accuracy), **latency** (esp. customer-facing),
**cost**.

## Three takeaways
1. A **small, well-designed eval** beats any public benchmark for your decision.
2. Choose the model that's **cheapest per successful outcome**, not cheapest/fastest per
   token — see [[cost-per-successful-outcome]].
3. There are many **knobs** to move along *or shift* the cost/accuracy Pareto frontier.

## Building the eval
Public benchmarks (SWE-bench Verified, BrowseComp) are directional but don't match your
**heterogeneous** workload. Instead compose a dataset of **tasks** (atomic unit: inputs +
success criteria). Treat it like a **math exam** — the final answer *and* the working
matter, so for agentic tasks check the steps, not just the outcome. Grade with
[[llm-as-judge]] (robust to e.g. syntactically-different-but-equivalent SQL) plus
**deterministic code-based evals** (assert a specific tool was called with the right args).

Companion talks: [[the-thinking-lever]], [[the-prompting-playbook]]. Related:
[[the-capability-curve]], [[picking-the-right-model]].

**Raw clip:** [[Picking the right model]]
