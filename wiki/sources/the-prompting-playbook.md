---
source: youtube
channel: "Anthropic"
url: "https://www.youtube.com/watch?v=G2B0YWuJUgI"
event: "Code with Claude"
speaker: "Margo van Laar (Applied AI engineer, London)"
created: 2026-07-24
---

# The prompting playbook

Margo van Laar (Applied AI) on applying core prompting principles to agentic systems.
Framed around two real scenarios: (1) an **existing production prompt** that broke on a
model migration, and (2) building a **new agentic prompt** zero-to-one. See
[[prompt-engineering-playbook]].

## Evals come first
You can't tell if a prompt change helped without [[eval-driven-model-selection|evals]].
A broken migration has two possible causes: the new model is **capable but behaves
differently** (fixable by prompting) or **less capable** (no prompting fixes it) — an eval
suite tells them apart. A good suite covers three case types:
- **Control** — unambiguous, should always pass.
- **Edge cases** — things the model failed before; lock in the fix.
- **Capability boundaries** — where the model should hand off to a human or **refuse**.

Worked example: a "Meridian Mobile" telco support bot with 5 test cases (plan data limits,
proration math, policy answers, escalate billing errors, don't withhold info). Process: run
V0 against the eval, then **target failure modes one at a time.**

## Prompt hygiene 101
Before targeting specific failures, clean up: remove junk copied from websites (tell-tale
"hero image" / cookie references), don't tell the bot it's human, and **add structure** —
XML tags separating role / policy / guidelines / tone / data. Rule of thumb: **"if you
can't tell guidelines from policy from data, the model can't either."** Add an **output
contract** (e.g. XML tags, or for nested JSON) for format consistency — and remember the
**harness**, not just the prompt, can enforce consistency.

Companion talks: [[picking-the-right-model]], [[the-thinking-lever]]. Related:
[[evals-for-taste]], [[json-prompting]].

**Raw clip:** [[The prompting playbook]]
