---
type: concept
created: 2026-09-06
---

# Skill evals — the concrete how-to

The [[skill-authoring-playbook]] §5 says "build evals *first*" is the **core discipline** of
reliable skill creation, and the [[skill-audit-worked-example|vault-wide skill audit]] (2026-09-06)
found the one systemic gap across all 11 vault skills: **none has evals.** This page is the missing
*mechanics* — the exact eval file format, the baseline-first process, what "running" an eval actually
means (there's no built-in runner), and a **worked, runnable eval set** for a real vault skill — so
the recurring "Skill Creator A/B eval run" [[Claude Mastery]] task stops being blocked on *how*.

Grounded in Anthropic's official **Skill authoring best practices**
(platform.claude.com/docs, 2026). It's the runnable companion to the playbook's §5 summary: playbook
= *the principle*, this page = *the file you write and the loop you run*.

## What an eval actually is

An eval is one **task + rubric** pair: a representative request, the files it needs, and a checklist
of **observable behaviors** a correct run must exhibit. It is the skill's version of the vault's own
**HEALTH_DEBT ratchet** ([[vault-autoresearch]]) — an *objective* signal that a change is an
improvement, not a vibe ([[evals-for-taste]], [[llm-as-judge]]).

The official structure is a small JSON object:

```json
{
  "skills": ["pdf-processing"],
  "query": "Extract all text from this PDF file and save it to output.txt",
  "files": ["test-files/document.pdf"],
  "expected_behavior": [
    "Successfully reads the PDF using an appropriate library or CLI tool",
    "Extracts text from all pages without missing any",
    "Saves the text to output.txt in a clear, readable format"
  ]
}
```

- **`skills`** — which skill(s) load for the run.
- **`query`** — the user request, phrased as a real user would.
- **`files`** — fixtures the task needs (test inputs; here, vault fixtures).
- **`expected_behavior`** — the rubric: 2–4 *observable* checks. Write behaviors you can *see in the
  transcript / output*, not internal intentions ("filters test accounts" → "the query excludes rows
  where `account_type = 'test'`").

## Evaluation-driven development (the 5 steps)

Do this **before** writing extensive skill instructions — it's what separates a skill that *solves a
real problem* from one that *documents an imagined one*:

1. **Identify gaps** — run the task with **no** skill; record the specific failures.
2. **Create ~3 evals** — build three scenarios that target those gaps (the checklist minimum is
   *at least three*).
3. **Establish baseline** — measure no-skill performance against the rubrics. This is the number to
   beat.
4. **Write minimal instructions** — just enough to pass the evals; resist pre-emptive bloat
   (the [[token-context-management]] "context is a public good" lens).
5. **Iterate** — run evals, compare to baseline, refine. `name`/`description` are the
   highest-leverage things to tune ([[skill-trigger-tuning]]).

### The Claude-A / Claude-B loop

The most effective iteration uses two Claude instances: **Claude A** helps author/refine the skill;
a fresh **Claude B** *uses* it on real tasks; you observe where B struggles and bring specifics back
to A ("B forgot to drop robotics-only cos — make that rule MUST, not 'always'"). Watch how B
navigates: unexpected read order, ignored files, or a file read every run all signal a *structure*
fix, not a wording one.

### The runner reality

**There is no built-in way to run these evals** — Anthropic ships the *format*, not an execution
harness; you build your own. In practice that means: load the fixtures, run the `query` twice (once
with the skill, once without), and grade each `expected_behavior` yourself or with an
[[llm-as-judge|LLM-as-judge]] rubric. For this vault the fixtures are just files under a scratch dir;
the "harness" can be as small as a shell script that stages them and a checklist you score. This is
why the eval run stays a [[Claude Mastery]] follow-up needing Cole at the keyboard — not an unattended
cloud step.

## Worked eval set — `startup-radar`

Formalizing the three evals the [[skill-audit-worked-example#§5 — build evals first, then iterate|audit]]
sketched in prose. These target `startup-radar`'s fragile logic (lane filter, dedup, geo scoring):

```json
[
  {
    "skills": ["startup-radar"],
    "query": "Run the startup radar for 2026-09-06.",
    "files": ["fixtures/feed-with-robotics-co.md", "startup-tracker/companies/"],
    "expected_behavior": [
      "A robotics-only company with no health/bio/AI or AI-infra angle is DROPPED (lane filter)",
      "No new note is written for it",
      "The skip is defensible from the company's stated focus, not invented"
    ]
  },
  {
    "skills": ["startup-radar"],
    "query": "Run the startup radar for 2026-09-06.",
    "files": ["fixtures/feed-repeats-known-co.md", "startup-tracker/companies/acme-bio.md"],
    "expected_behavior": [
      "A company already present with status: passed does NOT re-surface as new (dedup)",
      "No duplicate note is created for the same company",
      "Dedup keys on canonical name, not exact string match"
    ]
  },
  {
    "skills": ["startup-radar"],
    "query": "Run the startup radar for 2026-09-06.",
    "files": ["fixtures/feed-baltimore-health-ai.md"],
    "expected_behavior": [
      "A Baltimore health-AI seed company lands as a new note with a strong geo signal",
      "Funding facts are copied from the source, never invented",
      "The note validates against startup-tracker/validate.py"
    ]
  }
]
```

Baseline expectation: a no-skill run typically **passes eval 3** (obvious add) but **fails 1 and 2**
(it doesn't know the lane rule or the dedup key) — which is exactly what the skill exists to fix, and
exactly the gap an eval makes visible.

## When *not* to eval

Evals earn their cost on skills with **fragile, consistency-critical logic** (filters, dedup, enums,
exact sequences — the "narrow bridge" of the playbook's degrees-of-freedom heuristic). A pure
high-freedom prose skill (e.g. the prompt-architect trio) gets less from a rubric and more from the
Claude-A/B observe loop. Match eval investment to task fragility, same as everything else.

Related: [[skill-authoring-playbook]] · [[skill-audit-worked-example]] · [[skill-trigger-tuning]] ·
[[evals-for-taste]] · [[llm-as-judge]] · [[governed-skills-framework]] · [[claude-code-skills]] ·
[[vault-autoresearch]] · [[token-context-management]] · [[Claude Mastery]].
