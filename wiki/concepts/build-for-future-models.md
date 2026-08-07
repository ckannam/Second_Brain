---
type: concept
created: 2026-08-07
---

# Build for future models, not today's

A design principle for AI-native teams, sharpened by **Ramp** ([[ramp-ai-agents-every-step]]): **don't
over-invest in scaffolding for the model you have — build for the one arriving in 3–6 months.** Elaborate
present-day harnesses (custom prompt-glue, guardrail hacks, task decomposition the model can't yet do
itself) become **technical debt almost immediately**, because the next release outgrows them. Ramp says
they repeatedly *delete* their own scaffolding as models improve.

## Why it's a velocity bet
If you build for what's available *today*, "it might already be too late by the time you ship." Aiming a
little (or a lot) further ahead means the same engineering effort **carries you further** as capability
rises underneath it. The corollary tactic: when something doesn't work yet, sometimes the right move is
**"ship it and wait"** — trust the capability curve to close the gap rather than hand-engineering around a
gap that's about to vanish. The CTO-level version: **track the *rate of change*, not the current snapshot.**

## The tension (don't over-read it)
You still have to make the product work *today* or you have no business — so it's a *bias*, not an
absolute. The skill is spending scaffolding only where the model genuinely can't reach yet, and giving it
**more tools / context / agency** ("treat the agent like a coworker") everywhere else, so you inherit the
next model's gains for free.

## Where it sits in the vault
- Cousin of the **[[bitter-lesson]]** (don't hand-encode what learning/compute will solve) — but distinct:
  the bitter lesson is about *method* (general learning beats hand-crafted features); this is about
  *timing* (don't amortize scaffolding across a model generation that's about to end).
- Explains **[[context-anxiety]]** and why **harnesses co-evolve with models** — you expect to throw
  scaffolding away.
- The operating posture behind the whole **[[ai-native-engineering-org]]** rewrite and
  **[[the-capability-curve]]**.

Source: [[ramp-ai-agents-every-step]]. Related: [[bitter-lesson]] · [[the-capability-curve]] ·
[[context-anxiety]] · [[ai-native-engineering-org]].
