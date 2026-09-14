---
type: concept
created: 2026-08-30
---

# Skill audit — `networking-prep` (2026-08-30)

**Subject:** `networking-prep` — ~119 lines, vault-local (reads `crm/` + `profile/`), used for every
informational-interview / networking call prep. Chosen because it's one of Cole's highest-leverage
job-search skills and hadn't been audited yet. Audited against [[skill-authoring-playbook]]; format
mirrors the [[skill-audit-worked-example]] template.

## The audit

### §1 — Description is the trigger surface — ✅ / 🟡
The description packs explicit trigger phrases ("I'm networking with X", "prep for a meeting/call
with X", "info interview with X", "I'm meeting someone at [company]"), names both deliverables
(prep brief + pitch), and includes a key anti-under-trigger clause ("even if he doesn't ask for a
document"). It passes on substance.
- 🟡 **Recommend (not applied — trigger-surface change, leave to Cole):** The description opens with
  "Use whenever Cole needs" — functional but not true third-person declarative form, which the playbook
  specifies to avoid discovery problems. A tighter rewrite ("Prepares a research-backed pre-meeting
  brief…") would sharpen the signal. Deferred because any description edit shifts trigger behavior and
  belongs in a human-reviewed PR.

### §2 — Progressive disclosure keeps it cheap — ✅
At ~119 lines the body is well under the ~500-line ceiling; no split required. The three local files
(`crm/`, `profile/`) are read at run time, not bundled into the skill — good load discipline. No
nested reference files needed at current size.

### §3 — Be concise (assume Claude is smart) — ✅
Steps are imperative and lean. The self-qualifying note on Cole's lane ("As of this writing it's…
but **trust the file over this sentence**") is correctly self-aware rather than stale-baking a fact.
No padding explaining what an "informational interview" is.

### §4 — Match degrees of freedom to task fragility — ✅
Correctly **medium-freedom**: a fixed procedure (numbered steps, required section structure) for the
consistent-output parts, with prose latitude for the research and writing. The "do not fabricate
specific claims" rule is explicit in the research step. This matches the fragility level — prep briefs
need consistent structure but can't be over-scripted.

### §5 — Build evals first, then iterate — 🟡
No evals exist. The same gap as startup-radar; the three obvious ones:
1. *"Given a person whose `crm/<Name>.md` exists, Section 5 pitch must include ≥1 proof-point drawn
   verbatim from `crm/outreach-kit.md`'s proof-point bank."*
2. *"Section 3 questions must name the person's actual employer/role — not generic 'industry' questions."*
3. *"A `crm/prep/<Name>.md` file must exist after a run; it must cross-link to the person's CRM record."*
Building them requires live runs + the eval harness → follow-up item, not a nightly unattended fix.

### §6 — Anti-patterns — 🔧 (fixed)
One real, safe finding — **inconsistent step numbering**. The top-level steps ran: 0, 0.5, 1, 2, 3,
**5-output**, 6 — skipping Step 4 and using "5-output" as a hybrid label. This was a refactor
remnant (the Section 1–6 sub-structure inside Step 3 created a visual numbering collision that was
resolved by renaming the save step "5-output" instead of renumbering cleanly).
- 🔧 **Fixed:** renamed `## Step 5-output` → `## Step 4` and `## Step 6` → `## Step 5`; updated
  the internal cross-reference ("Output format is in Step 5-output" → "Output format is in Step 4").
  This is a structural, no-behavior-change fix — what the skill *does* at each step is unchanged.
- ✅ **CRM/profile paths:** all vault-internal paths are relative (`crm/prep/`, `profile/cole.md`,
  `log.md`) — correct style. No absolute paths found.

## Verdict

`networking-prep` is a **healthy, vault-integrated skill**: 4 sections clean, 2 recommendations
logged, 1 safe structural fix applied. The step-numbering fix was the one real issue; the two
recommendations (description third-person form, evals) are the honest next-step items for Cole.

## Reusable audit notes

For future audits of skills that read local-only files (`crm/`, `profile/`):
- Verify all paths are relative (absolute paths break portability).
- Note that §5 eval coverage is especially valuable when the skill draws from live vault files —
  it's easy for a path typo or file rename to silently degrade output without a behavioral signal.

Related: [[skill-authoring-playbook]] · [[skill-audit-worked-example]] · [[startup-radar]] ·
[[networking-prep]] · [[claude-code-skills]] · [[Claude Mastery]].
