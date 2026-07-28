---
type: concept
---

# Knowledge types (match the strategy to the type)

The brain has several memory systems, and each needs a different learning strategy. Defaulting
to one study habit for everything is the core mistake. From
[[how-to-remember-everything-brainhealthdecoded]].

| Type | What it is | Strategy |
|---|---|---|
| **Procedural (skill)** | how to *do* things | **practice, not study** |
| **Conceptual** | ideas, frameworks, mechanisms | **active processing** — wrestle, question, map |
| **Factual** | dates, names, constants (no conceptual anchor) | **engineered retrieval** — spaced repetition |

## Matched tactics

- **Skill:** *try it before you study it* (struggling before instruction scored up to 3× better);
  one tutorial per problem, not a playlist; short daily reps beat one long session
  ([[memory-consolidation]]); **stop before you get sloppy** — the brain saves tired, messy reps
  too.
- **Concept:** ask *"why does this work?"* before *"what is this?"* (elaborative interrogation:
  76% vs 69%); **explain it out loud** to an absent listener; build **your own analogy** and
  stress-test where it breaks; on revisiting, **explain from scratch — never just re-read**
  (the brain mistakes familiarity for understanding — see [[marsh-memory-lab|IOED]]). This is
  [[learning-by-connection]] in practice.
- **Fact:** put it in a spaced-repetition app (Anki) and let the algorithm schedule; keep cards
  **atomic** (one card, one fact — if it says "Explain…/Compare…" it's a concept, not a fact);
  don't use flashcards for anything but isolated facts.

**Sort as you go:** whether learning by choice ("let the walls you face tell you what to learn")
or following a curriculum (bucket each line as skill/concept/fact), classify first, then apply
the matching strategy. Gate on [[memory-consolidation|process-before-you-move-on]].

## The spacing layer — *when* to revisit each type (and the app thesis)

[[knowledge-types|Type]] governs the *strategy*; the [[spacing-effect]] governs the *schedule*.
Spacing is robust and domain-general (g ≈ 0.46; g = 0.28 even in math —
[[spacing-math-meta-analysis-murray-2025]]), and it protects **skills**, not just facts
([[spacing-testing-complex-skills-study]]). But the *retrieval modality must match the type* — the
key correction the evidence forces:

| Type | Spaced retrieval that actually works | Not this |
|---|---|---|
| **Fact** | flashcard recall on an expanding schedule ([[spaced-repetition]]; wrap Anki/FSRS) | — |
| **Concept** | spaced **explain-from-scratch** (elaborative retrieval), graded for gaps | more flashcards |
| **Skill** | spaced, **[[interleaving|interleaved]] practice problems** | flashcards — the math [[retrieval-practice\|testing effect]] was *not* robust (g = 0.18) |

**Why this is the product wedge.** [[spacerep|SpaceRep]] and Anki schedule *one* modality
(flashcards) for everything. A tool that **triages material into these three types and schedules the
right retrieval for each** — with an LLM doing the triage, the concept-grading, and the interleaved-
problem generation — is the differentiated [[neuro-channel|channel × app]] idea. Optimal spacing is
even *computable* in principle ([[optimizing-spaced-learning-smolen-2016]]). The hard, unsolved part
is [[spacing-effect|adoption]] — people know spacing works and still don't do it, which is why the
intervention belongs at *capture time*, not review time.
