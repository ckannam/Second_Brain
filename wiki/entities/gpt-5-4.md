---
type: entity
category: model
---
# GPT 5.4

OpenAI model behind [[codex]], benchmarked vs [[opus-4-6]] in [[codex-plugin-for-claude-code]]. Used as
an adversarial reviewer of Opus's work in the two-model quality loop (see [[adversarial-code-review]]).
Released **March 5, 2026**. Vendor: [[openai]]. Positioned as OpenAI's cheaper "value workhorse" tier.

## Benchmarks (captured 2026-07-28)
- ⚠️ **SWE-bench Verified — NOT confirmed.** Secondary sources **contradict each other**: some report
  **~77.2%**, others **~58.7%** for GPT-5.4. Because they disagree and no primary OpenAI figure was
  located, **no SWE-bench Verified score is asserted here.** (One cross-check suggests the 77.2% figure
  is actually **Sonnet 4.5's** score mis-attributed to GPT-5.4 — a good reason not to trust it.)
- **SWE-bench Pro — ~57.7%** — the most consistently repeated GPT-5.4 figure across multiple secondary
  write-ups (a harder, less "gameable" variant). Still secondary-sourced; treat as indicative.
- **Other (single-source, low confidence):** ~75% OSWorld (computer use), ~83% GDPval (knowledge work),
  and a Terminal-Bench 2.0 gap favoring GPT-5.4 over Opus (~75% vs ~65%). Not corroborated — flagged.
- **Pricing (secondary-reported):** GPT-5.4 ≈ **$2.50 in / $15 out** per M tokens vs Opus 4.6 ≈
  **$5 in / $25 out** — i.e. GPT-5.4 is the comprehensively cheaper option. Unverified against primary
  pricing pages.

**Bottom line for the vault:** the head-to-head is close and the *narrative* (converging benchmarks;
Opus 4.6 leads complex multi-file SWE; GPT-5.4 competitive and cheaper) is well-attested, but the
**specific GPT-5.4 numbers are secondary and partly contradictory** — the only firm number in the pair
is Opus 4.6's 80.8% SWE-bench Verified ([[opus-4-6]], Anthropic System Card).

Sources: web research 2026-07-28 (multiple secondary aggregators; no primary OpenAI benchmark located).
