---
type: concept
created: 2026-08-08
---

# Skill audit — a worked example (`startup-radar`)

The [[skill-authoring-playbook]] is the *checklist*; this page is the checklist **run against a
real skill** so it stops being abstract. It audits the vault's `startup-radar` skill against all
six playbook sections, records a verdict + specific finding per section, applies the safe fixes,
and ends with a **copy-paste audit template** Cole can rerun on every other skill. It's the
worked example the *Improve + general skills* task ([[Claude Mastery]]) asked for.

**Subject chosen:** `startup-radar` — at ~198 lines it's the vault's largest skill, so it exposes
the most checklist surface (progressive disclosure, degrees of freedom, anti-patterns), and only
its `SKILL.md` is git-tracked (the company notes it writes are gitignored/local), so auditing it
touches nothing personal.

## How to read this

For each of the playbook's six sections: **Verdict** (✅ clean · 🟡 recommend · 🔧 fixed) →
the specific finding → the action taken. The honest headline is that a mature skill mostly
passes; the value of an audit is catching the *one or two* real issues, not manufacturing churn.

## The audit

### §1 — Description is the trigger surface — ✅ / 🟡
The description is third-person, packs *what it does* (sweep → lane-filter → dedup → write notes)
**and** explicit triggers ("run the startup radar", "weekly startup discovery"), and carries the
concrete nouns retrieval hits on (`health-bio-ai`, `ai-infra`, "newly-funded startups"). It passes.
- 🟡 **Recommend (not applied — trigger-surface change, leave to Cole):** the description omits two
  real capabilities — Step 5.5 *contact enrichment* (it finds a best outreach target per company)
  and the optional iMessage delivery. Naming them would make the *what* complete without touching
  the trigger phrases. Deferred because editing a live skill's description unattended can shift
  firing behavior — exactly the kind of change the morning PR / Cole should sign off on.

### §2 — Progressive disclosure keeps it cheap — 🟡
At ~198 lines the body is **under the playbook's ~500-line ceiling**, so no split is *required*.
But it's the vault's largest skill and the closest to the ceiling.
- 🟡 **Recommend (watch, not applied):** the Step 1 source list (~40 lines of stable URLs/endpoints)
  and the field-schema blocks are the natural first `reference/sources.md` split *if the skill
  grows* — they're stable reference material, read-once, and rarely change per run. No action now
  (splitting a 198-line skill would add nesting cost for no benefit); flagged so the ceiling isn't
  crossed silently later. This is the [[token-context-management]] "context is a public good" lens.

### §3 — Be concise (assume Claude is smart) — ✅
Tight throughout — steps are imperative and lean, no padding explaining what an "HN thread" or a
"careers page" is. No action.

### §4 — Match degrees of freedom to task fragility — ✅
Correctly **medium-freedom**: a fixed recipe (numbered steps, exact field schema, a validator) for
the fragile parts (dedup keys, frontmatter enums, "never invent funding") and prose latitude for
the judgment parts (lane fit, angle guessing). This is the "robot on a path" heuristic applied
right — neither over-scripted nor under-specified. No action.

### §5 — Build evals first, then iterate — 🟡
The skill has **no evals** — the one genuine gap against the playbook's core discipline. There's no
objective signal that a change to its lane filter or dedup logic is an improvement vs. a vibe.
- 🟡 **Recommend (not applied — out of tonight's cloud scope):** write ~3 evals (e.g. "a
  robotics-only company must be dropped", "a company already `status: passed` must not re-surface",
  "a Baltimore health-AI seed co must land as `strong` geo") and measure them. Evals are this
  skill's version of the vault's own HEALTH_DEBT ratchet ([[vault-autoresearch]], [[evals-for-taste]]).
  Building/running them needs the eval harness + live sweeps, so it's a follow-up, not a nightly fix.

### §6 — Anti-patterns — 🔧 (fixed)
One real, safe finding — an **inconsistent path style**. Steps 4–5 reference the vault relatively
(`startup-tracker/companies/…`) against the declared `Vault root` input, but Step 7's validator call
hardcoded the absolute `python3 /Users/colekannam/Desktop/Second\ Brain/startup-tracker/validate.py`.
- 🔧 **Fixed:** normalized Step 7 to `python3 startup-tracker/validate.py` (run from the vault root),
  matching Steps 4–5 and staying portable if the vault moves. This is a structural, no-behavior-change
  fix — the kind that's safe to apply in the audit itself.
- ✅ **Correctly left absolute:** Step 6's `osascript /Users/colekannam/.claude/concerts/send.scpt`
  is a *system-integration* script outside the vault — absolute is right there. The rule is
  "vault-internal paths relative, external system paths absolute," not "all paths relative."

## Verdict

`startup-radar` is a **healthy, mature skill**: 3 sections clean, 2 recommendations logged for Cole,
1 safe fix applied. That ratio is the point — the audit's job is to find the real issue (the Step 7
path) and honestly log the rest, not to farm edits. The two 🟡 recommendations (description
completeness, evals) are now captured so they don't get lost.

## The reusable audit template

Copy this and fill it in per skill. Rerun on any `.claude/skills/<name>/SKILL.md`.

```md
# Skill audit — <name> (<date>)
Subject: <n lines>, tracked/local, why chosen.

§1 Description (trigger surface): ✅/🟡/🔧 — third person? what+when? key nouns? pushy vs under-fire?
§2 Progressive disclosure: — body <500 lines? refs one level deep? TOC on >100-line refs? split candidates?
§3 Concise: — any line Claude already knows? padding?
§4 Degrees of freedom: — open field→prose / narrow bridge→exact script; over- or under-constrained?
§5 Evals: — do any exist? if not, name ~3 (query + files + expected_behavior).
§6 Anti-patterns: — time-sensitive info? too many options? deep/Windows paths? inconsistent terms?
                    voodoo constants? vague helper/utils names? vault-internal path style consistent?

Verdict: <n clean / n recommend / n fixed>. Apply only structural/no-behavior fixes unattended;
leave trigger-surface + content changes for review.
```

**The one safety rule for unattended audits:** apply only **structural, no-behavior-change** fixes
yourself (path/link/format consistency); everything that changes *what a skill does or when it
fires* — descriptions, added options, new steps — is a **recommendation for Cole**, because those
can't be truth-checked without a live run. Same split the [[vault-autoresearch]] loop draws between
its auto-merge fast-track and its review-lane PR.

Related: [[skill-authoring-playbook]] · [[claude-code-skills]] · [[skill-trigger-tuning]] ·
[[token-context-management]] · [[evals-for-taste]] · [[vault-autoresearch]] · [[Claude Mastery]] ·
[[skill-audit-networking-prep]].
