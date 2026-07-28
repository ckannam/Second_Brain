---
type: concept
---
# Adversarial Code Review

A **second model (or agent) critiques the first's output**, the critique feeds back into a fix cycle — a quality loop that scales the review bottleneck without adding humans.

## Two flavors

**Heterogeneous (multi-model):** [[codex]]/[[gpt-5-4]] reviews [[opus-4-6]]'s work inside [[claude-code]] — genuinely adversarial because different training surfaces different failure modes. Demonstrated in [[codex-plugin-for-claude-code]]: Codex spots what Opus missed; Opus fixes it. Related: [[multi-model-workflows]].

**Self-review (same model):** Claude Code reviews its own output — less adversarial but still catches spec drift, style violations, and obvious bugs. [[fiona-fung|Fiona Fung]]'s team at Anthropic uses this as the default review tier ([[running-ai-native-engineering-org]], [[how-we-claude-code]]). The trick: **check the spec into the repo** so the reviewer can compare code against the stated contract.

## What it's good (and not good) for

Good at: style/lint, obvious bugs, **spec-drift** (code that no longer matches the spec), consistency enforcement.

Keep humans for: legal review, risk tolerance, trust boundaries, and **product sense / taste** — the judgment call Fiona described as "the snowman that was actually Mr. Peanut." An AI reviewer can catch that a component renders, not that it looks wrong.

## Why this is trustworthy

Connects to [[mechanism-over-output]]: identical output text means something different depending on the *process* that produced it. "This code is safe to ship" from an agent that did tool-use, critique, and redrafting carries more weight than the same sentence from a one-shot generation. The adversarial step is what makes the mechanism legible and spot-checkable.

## In the AI-native org

[[ai-native-engineering-org|When agentic coding scales org-wide]], code review becomes one of the new bottlenecks — throughput and contributor count both explode. Adversarial review is one structural response: run a critique pass before human review so humans spend their cycles on the things only humans can judge. Sources: [[running-ai-native-engineering-org]], [[how-we-claude-code]].
