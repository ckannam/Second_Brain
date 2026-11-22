---
type: concept
category: audit
created: 2026-11-22
about: "[[concert-digest]]"
---

# Skill Audit — `concert-digest`

Audit of `.claude/skills/concert-digest/SKILL.md` against [[skill-authoring-playbook]]
(six-section checklist). Conducted 2026-11-22 as part of the **Claude Mastery — improve +
general skills** task.

---

## §1 — Description (trigger surface)

**Finding:** Description opened in second-person imperative ("Use to compose…") — the
playbook requires third-person ("Composes…") because the description is injected into the
system prompt, where imperative voice causes discovery problems (same finding as
[[skill-audit-startup-radar]]).

**Fix applied:** Changed "Use to compose (and, in standalone mode, send)" →
"Composes (and, in standalone mode, sends)" in the frontmatter `description` field.

Remainder of description is solid: explicit trigger phrases ("run the concert digest",
"Monday launchd run"), concrete nouns (`concert-taste.md`, `ACTIVE_METRO`, `iMessage self-chat`),
and what + when structure. Length is well under the 1,024-character limit.

---

## §2 — Progressive disclosure

**Finding: ✅ Clean.**

51 lines — well under the ~500-line ceiling. The procedure fits inline without splitting into
reference files. Mode branching (standalone vs. section) is compact.

---

## §3 — Concise

**Finding: ✅ Clean.**

Steps are imperative and direct. The output template in Step 5 is appropriate — it's a
concrete format spec, not padding. The "quiet week" fallback case is a minimal but useful
branch. No restatements of general knowledge.

---

## §4 — Degrees of freedom

**Finding: ✅ Clean.**

Appropriate split: low freedom on the output format (exact block template, platform =
iMessage, no markdown bold), medium freedom on the search and ranking logic. The "never invent"
rule in the Rules section is the right narrow bridge for the most dangerous failure mode
(fabricating a show that doesn't exist).

---

## §5 — Evals

**Finding: 🟡 Recommend — not applied (interactive, needs Cole).**

No evals exist. Three recommended test cases:

1. *"Run the concert digest for ACTIVE_METRO=triangle, TODAY=2026-11-22"* → expected:
   output is text-native (no markdown bold), capped at 8–12 shows, correctly ranked
   taste > discovery, no fabricated links.
2. *"MODE=section run where no strong shows are found"* → expected: outputs the
   "🎵 Quiet week near you" fallback message, NOT an empty list.
3. *"MODE=standalone run"* → expected: skill invokes
   `osascript "$HOME/.claude/concerts/send.scpt"` and does NOT also print a duplicate
   block to stdout.

Needs live concert-taste.md + Cole's Mac for meaningful execution. Deferred.

---

## §6 — Anti-patterns

**Finding: One structural fix applied.**

- **Hardcoded absolute path with username** — `osascript /Users/colekannam/.claude/concerts/send.scpt`
  embedded a machine-specific absolute path. Per §6, paths should use `$HOME` or be
  relative. **Fix applied:** changed to `osascript "$HOME/.claude/concerts/send.scpt"`.
  No behavior change on Cole's Mac (`$HOME` = `/Users/colekannam`); makes the skill
  portable across username or OS reinstall.

No time-sensitive info. No voodoo constants. No inconsistent terminology. No Windows paths.

---

## Verdict

| Section | Status | Action |
|---|---|---|
| §1 Description | 🔧 Fixed | second-person → third-person applied |
| §2 Disclosure | ✅ Clean | — |
| §3 Concise | ✅ Clean | — |
| §4 Freedom | ✅ Clean | — |
| §5 Evals | 🟡 Recommend | 3 test cases logged above; deferred to Cole |
| §6 Anti-patterns | 🔧 Fixed | absolute path → `$HOME`-relative applied |

**2 structural fixes applied. 1 eval recommendation logged for Cole.** Skill is healthy;
no trigger-surface or body changes needed.

---

Related: [[skill-audits-2026]] · [[skill-authoring-playbook]] · [[skill-audit-worked-example]] ·
[[skill-audit-startup-radar]] · [[evals-for-taste]] · [[skill-evals-playbook]] ·
[[Claude Mastery]].
