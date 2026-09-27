---
type: concept
created: 2026-09-27
---

# Skill audit — `wiki-query` (2026-09-27)

**Subject:** `wiki-query` — 71 lines, vault-core (reads `index.md`, `crm/index.md`, `tasks/index.md`,
`buckets/`, `wiki/`), the skill Cole runs every query through. Chosen because it's the single most
frequently invoked vault skill and hadn't been audited yet; all five earlier Claude-Mastery audits
covered other skills ([[skill-audit-worked-example]], [[skill-audit-networking-prep]]). Audited
against [[skill-authoring-playbook]]; format mirrors the [[skill-audit-worked-example]] template.

## The audit

### §1 — Description is the trigger surface — ✅ / 🟡

The description packs what it does ("answered from this Second Brain vault/wiki"), explicit trigger
phrases ("what does the wiki/vault say about X", "ask the wiki/vault", "according to my notes"), the
command trigger (`/wiki-query`), and a boundary clause ("question whose answer lives in the wiki
pages, CRM, tasks, or journal rather than general knowledge"). It passes on substance.

- 🟡 **Recommend (not applied — trigger-surface change, leave to Cole):** The description opens with
  "Use when the user asks a question" — functional, but the playbook specifies third-person
  declarative to avoid discovery problems. A tighter rewrite ("Retrieves and synthesizes answers from
  the Second Brain vault — wiki pages, CRM, tasks, and journal — with mandatory file-back so every
  query answer becomes a persistent cross-linked artifact.") would sharpen the signal and put the
  distinctive *file-back* behavior front-and-center. Deferred because description edits shift firing
  behavior and belong in a human-reviewed change.

### §2 — Progressive disclosure keeps it cheap — ✅

At 71 lines the body is far under the ~500-line ceiling. All vault files (`index.md`, `crm/index.md`,
etc.) are read at runtime, not bundled. No nested reference files needed. No action.

### §3 — Be concise (assume Claude is smart) — 🟡

The skill's **Guardrails** section (4 bullets) and **Common Mistakes** section (4 bullets) are
complementary but have a 1-bullet overlap: both sections independently note the "never invent facts"
rule that `AGENTS.md` already states. Guardrails is "what to avoid (canonical rules)"; Common Mistakes
is "where Claude actually goes wrong (behavioral reminders)" — that distinction is real and worth
keeping, but the overlap adds a small token cost for zero new information.

- 🟡 **Recommend (not applied — behavior-adjacent, leave to Cole):** Remove "Never invent facts" from
  the Guardrails section (it's already in `AGENTS.md` and restated in Common Mistake #1), keeping only
  the three guardrails that add something the common-mistake framing doesn't: "Links > pages",
  "Snapshots age", "Don't duplicate." This keeps Guardrails as design-intent reminders and Common
  Mistakes as behavioral reminders, with no overlap. 4→3 bullets saves 2 lines; the single dedup
  rule in Guardrails stays because it's a proactive *gate* ("check before creating"), not a reactive
  mistake.

### §4 — Match degrees of freedom to task fragility — ✅

Correctly **medium-freedom**: a fixed 7-step procedure for the fragile parts (index-first, traverse
links, freshness reconciliation, mandatory file-back) plus prose latitude for synthesis and deciding
which pages to read. The "skip step 6 for navigational lookups" escape hatch is explicit. This is
the right posture for a task that needs consistent structure but can't be scripted at the content
level. No action.

### §5 — Build evals first, then iterate — 🟡

No evals exist. Three obvious candidates:

1. *"A non-navigational query (e.g. 'what does the vault say about spaced repetition?') must produce
   a file in `wiki/` after the run with `type` and `created` frontmatter and at least one `[[wikilink]]`
   citation."*
2. *"The answer must cite `[[wiki-pages]]` that exist in `index.md` — never an invented page name."*
3. *"A life-area query ('what should I do about JHTV?') must read the matching `buckets/` MOC page
   as a step, not just `index.md`."*

Building/running evals requires the eval harness + live runs → follow-up for Cole, not a nightly fix.

### §6 — Anti-patterns — ✅ (one pre-existing fix noted)

- ✅ **No absolute paths.** All vault-internal references (`index.md`, `crm/index.md`, `tasks/index.md`,
  `buckets/<Area>.md`, `wiki/`) are relative — correct style.
- ✅ **No voodoo constants, no inconsistent terminology.** "File back", "link graph", "wikilinks",
  "freshness" are used consistently throughout.
- ✅ **No time-sensitive info or "too many options"** anti-patterns. The one conditional ("skip step 6
  for navigational lookups") is explicit and well-defined.
- **Pre-existing note (structural, applied):** The `skill-audit-worked-example.md` described fixing the
  `startup-radar` Step 7 validator path (absolute → `startup-tracker/validate.py`) on 2026-08-08,
  but the fix was never persisted in the actual SKILL.md file. Applied tonight on the review branch
  so the worked-example's described change actually lands. This is unrelated to `wiki-query` but
  noted here as the only structural fix in this night's audit pass.

## Verdict

`wiki-query` is a **healthy, lean, vault-integrated skill**: 3 sections clean, 2 recommendations
logged for Cole (description third-person form; guardrails dedup), no structural fixes needed on
the skill file itself. The audit surfaced the startup-radar path discrepancy as a side-finding and
applied that fix.

Related: [[skill-authoring-playbook]] · [[skill-audit-worked-example]] · [[skill-audit-networking-prep]] ·
[[wiki-query]] · [[claude-code-skills]] · [[vault-autoresearch]] · [[token-context-management]] ·
[[Claude Mastery]].
