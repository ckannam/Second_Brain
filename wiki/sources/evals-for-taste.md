---
source: youtube
channel: "Anthropic"
url: "https://www.youtube.com/watch?v=v9FTCvkV_a0"
event: "Code with Claude"
created: 2026-07-24
---

# Evals for taste: Hill-climbing a slide-generation agent

Building a **rubric-driven, replayable eval system** from real user projects that yields
quality / cost / latency / error / token signals in **under 6 hours per model change** — and
evolves into a development **flywheel** powered by real user dissatisfaction signals. Worked
example: a **slide-generation agent**, where "quality" is a matter of *taste*, not a string
match.

## What evals are and why
Evals = systematic tests (tasks + grading logic) measuring how well a system performs on a
**specific** use case. They're the bridge from **vibes** ("feels worse today" — useful as a
sense-check, but not actionable) to something actionable. Public benchmarks (SWE-bench,
Terminal Bench, τ-Bench, OSWorld, ARC-AGI-2) are directional but don't measure *your*
use case → **build your own** (echoes [[eval-driven-model-selection]]).

Without evals you're in a **reactive loop**: catch issues only in prod, fix one and break
others, can't separate genuine feedback from noise, can't verify improvement vs regression.
With evals you get **clarity** (defining success forces you to formalize expectations), can
iterate on optimal agent configs, adopt new models faster, and surface problems before
launch.

## Graders
- **Code-based graders** — like unit tests (string / regex / fuzzy match): fast, cheap,
  deterministic, but **brittle and lacking nuance**. Good for "a slide deck exists."
- **Model-based graders** ([[llm-as-judge]]) — for **nuanced quality** ("is the slide deck
  *good?*"). The heart of "evals for taste": encode taste into a **rubric** the judge
  applies. Made **replayable** over real user projects so each model/config change is
  re-scored cheaply.

Related: [[prompt-engineering-playbook]], [[picking-the-right-model]], [[cost-per-successful-outcome]].

**Raw clip:** [[Evals for taste Hill-climbing a slide-generation agent]]
