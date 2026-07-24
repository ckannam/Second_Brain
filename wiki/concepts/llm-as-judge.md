# LLM-as-judge

Using a model to grade another model's output against expected behavior — a key ingredient
in [[eval-driven-model-selection|evals]]. Strength: robust to outputs that are **equivalent
but not identical** (e.g. syntactically different SQL that pulls the same data, or prose that
conveys the same answer), where a string match would fail.

Best paired with **deterministic code-based checks** for the things that must be exact
(a specific tool was called, with a specific argument). In agentic evals, judge both the
**final outcome** and the **working/steps** ([[picking-the-right-model]]). Taken further,
[[evals-for-taste]] shows how to build LLM judges for **subjective quality** (a slide-gen
agent), not just correctness.

Related: [[test-time-compute]], [[prompt-engineering-playbook]].
