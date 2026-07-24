# Eval-driven model selection

The repeatable process for deciding whether to adopt a model for *your* use case: build a
small eval and let it give a clear yes/no. Core claims (from [[picking-the-right-model]]):

- A **small, well-designed eval beats any public benchmark** — SWE-bench Verified,
  BrowseComp, etc. are directional but don't match your heterogeneous workload.
- Judge on three pillars: **quality, latency, cost** — and optimize for
  [[cost-per-successful-outcome]], not price/latency per token.
- An eval is a dataset of **tasks** (atomic unit = inputs + success criteria). Treat it like
  a **math exam**: grade the final answer *and the working* (for agentic tasks the steps
  matter).
- Grade with [[llm-as-judge]] (robust to equivalent-but-different outputs, e.g. SQL) plus
  **deterministic code-based checks** (assert tool X was called with arg Y).

Distinguishes "model behaves differently" (fix by prompting) from "model is less capable"
(no prompt fixes it) — the diagnostic in [[the-prompting-playbook]]. Related:
[[test-time-compute]], [[evals-for-taste]], [[prompt-engineering-playbook]].

**The metric *is* the skill.** [[autoresearch]] makes this vivid: once an agent can run
experiments essentially for free, the human's remaining leverage is **choosing what to
measure** and setting the constraints. A well-designed scalar metric with an automated,
un-gameable evaluation is the whole game; a bad metric gets confidently optimized in the
wrong direction. The [[autoresearch]] design enforces this by making the eval harness
(`prepare.py`) read-only so the agent can't cheat it — the same instinct as grading "the
working, not just the answer" here.
