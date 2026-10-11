---
type: concept
category: audit
created: 2026-10-11
about: "[[startup-radar]]"
---

# Skill Audit — `startup-radar`

Audit of `.claude/skills/startup-radar/SKILL.md` against [[skill-authoring-playbook]]
(six-section checklist). Conducted 2026-10-11 as part of the **Claude Mastery — improve +
general skills** task.

---

## §1 — Description (trigger surface)

**Finding:** Description opened in second-person imperative ("Use to discover and triage…") —
the playbook requires third-person ("Discovers and triages…") because the description is
injected into the system prompt, where first/second-person causes discovery problems.

**Fix applied:** Changed "Use to discover and triage" → "Discovers and triages" in the
frontmatter `description` field.

Remainder of description is solid: explicit trigger phrases ("run the startup radar" / "weekly
startup discovery"), concrete nouns (`health-bio-ai`, `ai-infra`, `startup-tracker`), and the
what + when structure. No length issue (~210 chars; limit 1,024).

---

## §2 — Progressive disclosure

**Passes.** Body is ~199 lines (limit ~500). No nested reference files. The `validate.py`
script is *executed*, not loaded as text — correct per playbook (script output costs tokens;
source code does not). No domain-split needed at this length.

---

## §3 — Concise

**Passes.** Steps are detailed but the detail is earned: exact API URLs (HN Algolia, YC jobs,
VC job boards), exact field names for frontmatter, and a prioritized contact-enrichment
protocol. These are all "things Claude doesn't already know." No redundant explanations of
generic concepts.

---

## §4 — Degrees of freedom

**Passes.** This skill is narrow-bridge: fragile, consistency-critical, sequential (exact
field names, exact enum values, exact dedup logic). The prescriptive step-by-step format is
appropriate. The open-field moments (Step 2 field extraction, Step 5a contact search) are
correctly left as prose direction rather than over-specified scripts.

---

## §5 — Evals (gap — needs Cole)

**No evals built yet.** The remaining work on the `@cloud` Skill max / Improve + general
skills task is an interactive Skill Creator eval run (needs Cole). Three recommended tests
to run with Cole:

1. **Lane filter test** — give a sample of 5 companies (3 health-bio-ai, 1 ai-infra, 1 other);
   verify `other` is dropped and correct lanes assigned.
2. **Dedup test** — pre-seed `startup-tracker/companies/` with one note matching a discovered
   company; verify it's skipped, not re-written.
3. **Contact enrichment test** — provide one early-stage (Seed) company; verify it finds and
   sets a CEO contact rather than a generic `jobs@` address.

---

## §6 — Anti-patterns

**Finding:** Step 5.5 was an anomalous numbering pattern (5, 5.5, 6, 7 rather than consistent
integers or sub-labels).

**Fix applied:** Renamed "Step 5.5" → "Step 5a" for consistent notation.

**Minor / not fixed:** The `validate.py` invocation uses a backslash-escaped space
(`/Users/colekannam/Desktop/Second\ Brain/…`). Quoting the path (`"…/Second Brain/…"`) is
more robust and portable. Left as-is since it's @local only and changing it is a copy-paste
risk on Cole's machine; flagging here for the next manual pass.

---

## Summary

| § | Check | Status |
|---|---|---|
| 1 | Description is third-person, what+when, trigger-specific | **Fixed** (second-person → third) |
| 2 | Progressive disclosure, ≤500 lines | Pass |
| 3 | Concise, no redundant context | Pass |
| 4 | Freedom matched to task fragility | Pass |
| 5 | Evals exist | **Gap** — 3 tests recommended for interactive run |
| 6 | No anti-patterns | **Fixed** (Step 5.5 → Step 5a); path quoting minor/noted |

Two structural fixes applied; one eval gap logged for Cole.

Related: [[skill-authoring-playbook]] · [[startup-radar]] · [[claude-code-skills]] ·
[[skill-audit-networking-prep]] · [[skill-audit-worked-example]] · [[Claude Mastery]]
