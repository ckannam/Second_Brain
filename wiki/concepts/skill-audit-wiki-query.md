---
type: concept
created: 2026-10-04
---

# Skill audit — `wiki-query` (2026-10-04)

**Subject:** `wiki-query` — ~70 lines, the vault's core retrieval skill; fires on any question
meant to be answered from the wiki/CRM/tasks. The most frequently triggered vault skill and the
entry point to every query session. Audited against [[skill-authoring-playbook]]; format mirrors
[[skill-audit-worked-example]] and [[skill-audit-networking-prep]].

## The audit

### §1 — Description is the trigger surface — ✅ / 🟡

The description packs the key triggers ("what does the wiki/vault say about X", "ask the
wiki/vault", "according to my notes") and names the scope (wiki pages, CRM, tasks, journal),
distinguishing vault-grounded answers from general knowledge. It also covers the slash-command
path ("Also runs on the /wiki-query command"). Passes on coverage.

- 🟡 **Recommend (not applied — trigger-surface change, leave to Cole):** The description opens
  with "Use when the user asks a question…" — functional, but the playbook specifies true
  third-person declarative form ("Answers questions from the Second Brain vault/wiki…") to avoid
  discovery problems in larger toolboxes. Deferred: description edits shift trigger behavior and
  belong in a human-reviewed iteration.

### §2 — Progressive disclosure keeps it cheap — ✅

At ~70 lines the body is well under the ~500-line ceiling; no split required. No nested reference
files. The skill explicitly delegates to `AGENTS.md` for canonical rules rather than bundling
them — correct load discipline: AGENTS.md is already in-context at session start, so
referencing it costs nothing extra.

### §3 — Be concise (assume Claude is smart) — ✅ / 🟡

The skill opens with "Do not restate `AGENTS.md`'s rules here" and largely honours this. Steps
are action-oriented and lean. Step 6 includes a necessary reminder list (file-back sub-steps)
that the Common Mistakes section shows are genuinely skipped — the token cost is justified.

- 🟡 **Recommend (not applied — behavioral risk):** The **Guardrails** section (4 bullets: never
  invent, links > pages, snapshots age, don't duplicate) partially restates content already in
  steps 4, 5, and 6, and in Common Mistakes. Merging the unique items into Common Mistakes and
  removing the section would save ~8 lines. Not applied unattended: the explicit guardrails are
  a behaviorally significant reminder at the top of the decision path; removing them could
  increase hallucination or duplication on edge cases. Leave to Cole.

### §4 — Match degrees of freedom to task fragility — ✅

Correctly **medium-freedom**: a 7-step procedure for consistency-critical parts (always check
index first, always file back, always traverse links), with prose latitude for the synthesis
and writing. The "Navigational lookup → skip file-back" short-circuit is properly placed at
step 1 to exit early, not buried in step 6. Appropriate for a query skill where the failure
modes (skipping index, not filing back, answering from memory) are well-defined.

### §5 — Build evals first, then iterate — 🟡

No evals exist. The three obvious ones for future coverage:

1. *"Given a topic that has a page in `wiki/`, the answer must cite `[[page-name]]` and not
   rely on general knowledge alone."*
2. *"After a non-navigational query, `index.md` must contain a new or updated entry for the
   filed answer page."*
3. *"After a query touching a life area (e.g. Job Search), the answer page must link from
   the relevant `buckets/` MOC."*

Building and running these requires an eval harness + baseline runs → follow-up item for Cole,
not a nightly unattended fix.

### §6 — Anti-patterns — ✅

No time-sensitive specifics (model names, product versions). No "too many options" branching —
step 2's sub-cases (CRM / tasks / bucket entry points) are exclusive and clear. Step numbering
is clean 1–7 with no gaps or hybrid labels. No Windows-style paths. No voodoo constants.
Terminology is consistent: "vault" and "wiki" are used as the skill's own index sets
them (vault = everything including crm/tasks; wiki/ = the generated pages). No anti-patterns
found.

## Verdict

`wiki-query` is a **healthy, well-structured skill**: 5 sections clean, 2 recommendations logged
(description third-person form, Guardrails overlap), 0 structural fixes required. The skill's
deliberate choice to restate the file-back sub-steps despite the "no AGENTS.md restatement" norm
is *justified* by the Common Mistakes list — skipping file-back is the most documented failure
mode.

## Reusable audit notes

- "Restate vs. delegate" is a judgment call proportional to skip-rate: when a step is
  frequently skipped in practice (evidence: Common Mistakes), restating it in the procedure is
  worth its token cost — the skill's own failure mode list is the evidence base.
- A vault-entry skill (one that triggers first and sets up everything else) benefits from a
  slightly more prescriptive procedure than a downstream skill that assumes setup is done.

Related: [[skill-authoring-playbook]] · [[skill-audit-worked-example]] · [[skill-audit-networking-prep]] ·
[[wiki-query]] · [[claude-code-skills]] · [[Claude Mastery]].
