---
type: concept
---

# Spaced repetition (the technique + the tools)

The **applied technique** that operationalizes the [[spacing-effect]] + [[retrieval-practice]]:
review each item at **expanding intervals**, timed to hit *just as you're about to forget it*.
Where the spacing effect is the *phenomenon*, spaced repetition is the *product* built on it —
flashcards, scheduling algorithms, and the apps around them.

## The stack
- **Ebbinghaus → forgetting curve** (130+ years old): memory decays predictably; a well-timed
  review resets the curve flatter each time ([[neuroscience-of-spacing-brainfacts]]).
- **Anki + FSRS** — the incumbent. FSRS (Free Spaced Repetition Scheduler) is an open,
  best-in-class algorithm that models each card's forgetting curve and schedules the next review.
  **This is a commodity — not worth rebuilding.** The right move for the *Fact* bucket is to
  *wrap* Anki/FSRS (e.g. `.apkg` export or AnkiConnect), not reimplement a scheduler.
- **[[spacerep]]** — a current competitor: FSRS + Google Calendar integration. Confirms the
  market and reveals the gap (flashcards only; no knowledge-type routing, no concept coaching).

## The load-bearing limitation
Spaced repetition, as everyone ships it, is a **flashcard/Fact tool**. The evidence says that's
correct *for facts* and *wrong as a universal strategy*:
- The math [[retrieval-practice|testing effect]] was **not robust** (g = 0.18, CI crosses zero) —
  flashcard retrieval is the weak tool for problem-solving material.
- [[knowledge-types|Concepts and skills]] need *different* retrieval: spaced **re-explanation**
  (concept) and spaced **[[interleaving|interleaved practice]]** (skill), not more cards.

So the differentiated product isn't "another Anki" — it's a **spacing engine that schedules the
right retrieval modality per knowledge type**, with an LLM doing the parts a flashcard can't
(triage, grading a from-scratch explanation, generating interleaved problems). That thesis lives
on [[neuro-channel]] (channel × app), grounded in [[optimizing-spaced-learning-smolen-2016]]
(optimal spacing is computable) and the [[neuroscience-of-behavior]] hub.
</content>
