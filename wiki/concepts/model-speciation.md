---
type: concept
created: 2026-07-27
---
# Model Speciation

The idea, articulated by [[andrej-karpathy]] in [[skill-issue-karpathy-sarah-guo]], that AI models are *diverging* into distinct ecological niches rather than converging on one universal system. By analogy to biological speciation: different selection pressures (latency, cost, reasoning depth, domain specificity) push models down different evolutionary paths until you get a diverse ecosystem of purpose-fit species rather than a single dominant form.

## Why it happens

- **Cost/capability tradeoffs** aren't linear — a model maximally optimized for fast, cheap inference makes different architectural choices than one maximized for deep reasoning, and neither is "the best model"; they're different organisms.
- **Context matters more than raw capability.** A coding specialist, a vision model, a real-time voice agent, and a long-horizon planner each need different training mixes, inference stacks, and safety postures. Forcing them into one model dilutes all of them.
- **The hardware layer speciate too.** Inference chips, edge deployments, and memory-bandwidth-bound inference encourage models that fit specific silicon constraints.

## Implications for using AI

- **Eval-driven selection becomes essential** (→ [[eval-driven-model-selection]]): when models are specialized, "use the best model" is underspecified — you have to pick the right species for the task.
- **Multi-model workflows** (→ [[multi-model-workflows]]) become the norm: route tasks to the species they fit.
- **Cost-per-successful-outcome** (→ [[cost-per-successful-outcome]]) rather than raw benchmarks is the right lens, because two models on the same benchmark can win in completely different deployment contexts.
- Karpathy contrasted this with the "one model to rule them all" narrative — he believes speciation is already happening and will accelerate.

Related: [[the-capability-curve]], [[anthropic]], [[multi-agent-orchestration]], [[eval-driven-model-selection]], [[cost-per-successful-outcome]], [[bitter-lesson]].
