---
type: entity
category: model
---
# Opus 4.6

Anthropic Claude model powering [[claude-code]] in the July 2026 sources. Released **February 2026**.
Benchmarked head-to-head against **[[gpt-5-4|GPT-5.4]]** in [[codex-plugin-for-claude-code]]; the
recommended pattern is Opus building + [[codex]]/[[gpt-5-4]] doing [[adversarial-code-review]].
Vendor: [[anthropic]].

## Benchmarks (captured 2026-07-28)
- **SWE-bench Verified: 80.8% (80.84%)** — reported in **Anthropic's Opus 4.6 System Card (Feb 2026)**,
  averaged over 25 trials with adaptive thinking; corroborated by Vellum. This is the one figure with a
  **primary source**. (For continuity: roughly flat vs Opus 4.5's ~80.9% — coding held while other
  capabilities advanced.)
- **vs GPT-5.4:** secondary write-ups describe the two as **converging on standardized coding
  benchmarks** (differences near the margin of error), with **Opus 4.6 keeping the edge on complex,
  multi-file software engineering** while GPT-5.4 is competitive and cheaper. See [[gpt-5-4]] for the
  head-to-head details and the caveats.
- ⚠️ **Sourcing caveat:** apart from the Anthropic System Card figure above, the comparison numbers
  circulating (SWE-bench Pro, Terminal-Bench, pricing) come from **secondary blog/aggregator sites that
  disagree with each other** — treat them as indicative, not authoritative. GPT-5.4's SWE-bench
  *Verified* number in particular is **contradictory across sources** and is left unstated here.

Sources: Anthropic Opus 4.6 System Card (Feb 2026); web research 2026-07-28.
