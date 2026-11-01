---
type: concept
category: audit
created: 2026-11-01
about: "[[concert-digest]]"
---

# Skill Audit — `concert-digest`

Audit of `.claude/skills/concert-digest/SKILL.md` against [[skill-authoring-playbook]]
(six-section checklist). Conducted 2026-11-01 as part of the **Claude Mastery — improve +
general skills** task ([[Claude Mastery]]). First dedicated audit of `concert-digest`; it was
on the 2026-10-04 remaining-audits list (with `orchestrate-agents` and the three prompt skills).

---

## §1 — Description (trigger surface)

**Finding:** Description opened in second-person imperative ("**Use to compose** (and, in
standalone mode, send)…") — the playbook §1 requires third-person because the description is
injected into the system prompt, where first/second-person phrasing causes discovery problems.
This is the same defect found and fixed in [[skill-audit-startup-radar]].

**Fix applied:** Changed "Use to compose (and, in standalone mode, send)" → "**Composes** (and,
in standalone mode, **sends**)" in the frontmatter `description` field.

Remainder of the description is solid: explicit trigger surfaces ("run the concert digest",
"Monday launchd run"), concrete nouns (`profile/concert-taste.md`, "iMessage", "metro",
"venue calendars"), and a clean what + when structure. Length fine (~430 chars; limit 1,024).

**Minor / not fixed:** the `name` is noun-form (`concert-digest`) rather than the playbook's
preferred gerund (`composing-concert-digest`). Left as-is — renaming would break the launchd
trigger and every reference, and the whole vault skill set uses noun-form names consistently
(changing one in isolation would create inconsistency, not fix it).

---

## §2 — Progressive disclosure

**Passes.** Body is ~51 lines (limit ~500). No reference files, and none are warranted at this
length. The `send.scpt` AppleScript is *executed* via `osascript`, not loaded as text — correct
per the playbook (script output costs tokens; source does not). No domain-split needed.

---

## §3 — Concise

**Passes.** Every step is earned detail Claude doesn't already have: the exact window math
(`TODAY .. TODAY + window_weeks`), the exact text-native block format (including the empty-week
fallback copy), the ~8–12-show cap with its rationale ("so the text stays scannable"), and the
exact delivery invocation. The single line of color ("Two hobbies he is investing in: travel +
live music") is one short sentence and gives the skill useful intent framing — not bloat.

---

## §4 — Degrees of freedom

**Passes.** Freedom is matched to fragility. Composition and ranking (taste tier → soonest date,
dedup, cap) are correctly left as open-field prose — there are many valid orderings and Claude
should route. Delivery is correctly narrow-bridge: the exact `osascript …/send.scpt "<block>"`
command plus "then stop, do not also print a duplicate" and the `MODE=section` "output ONLY the
block; do NOT send" rule. The anti-fabrication rule ("Never invent shows, dates, venues, or
ticket links… write `tix: search …` instead of a fabricated URL") is exactly the kind of
low-freedom guardrail a consistency-critical, outward-sending step needs.

---

## §5 — Evals (gap — needs Cole)

**No evals built yet** — the systemic gap shared by every vault skill (see [[skill-audits-2026]],
[[skill-evals-playbook]]). The remaining work on the `@cloud` Skill max / Improve + general
skills task is an interactive Skill Creator eval run (needs Cole). Three recommended tests:

1. **Empty-week honesty test** — feed a metro + window with no credible shows; verify it emits
   the honest "🎵 Quiet week near you…" note and does **not** fabricate shows or links (tests the
   §4 anti-fabrication rule, the highest-risk failure for an outward-sending skill).
2. **Mode test** — `MODE=section` returns ONLY the block with no send and no `osascript` call;
   `MODE=standalone` sends via `send.scpt` and then stops without printing a duplicate.
3. **Ranking + dedup test** — a mix of love / want-to-see / discovery artists including one
   duplicate show; verify tier order (love > want-to-see > discovery) then soonest-date, dedup
   applied, and the ~8–12 cap respected.

---

## §6 — Anti-patterns

**Passes** — a clean sweep:

- **Paths:** forward slashes throughout; no Windows-style paths.
- **Time-sensitive info:** none hardcoded (the date arrives as `TODAY`, the metro as
  `ACTIVE_METRO` — the skill explicitly says "do NOT recompute").
- **Too many options:** one default path per step; the only branch (standalone vs section) is a
  genuine mode, not option-sprawl.
- **Terminology:** consistent ("block", "window", "metro", "lane").
- **Voodoo constants:** the one magic number (~8–12) carries its justification inline;
  `window_weeks` is read from settings, not hardcoded.
- **Helper naming:** `send.scpt` is named for its activity.

**Minor / not fixed:** `send.scpt` is referenced by the absolute path
`/Users/colekannam/.claude/concerts/send.scpt`. This is correct — the skill runs `@local` on
Cole's Mac in standalone mode — so it is intentional, not a portability defect (same situation
as the `startup-radar` path note).

---

## Summary

| § | Check | Status |
|---|---|---|
| 1 | Description is third-person, what+when, trigger-specific | **Fixed** (second-person → third); name noun-form noted/kept |
| 2 | Progressive disclosure, ≤500 lines | Pass |
| 3 | Concise, no redundant context | Pass |
| 4 | Freedom matched to task fragility | Pass |
| 5 | Evals exist | **Gap** — 3 tests recommended for interactive run |
| 6 | No anti-patterns | Pass (local absolute path intentional) |

One structural fix applied (§1 description → third-person); one eval gap logged for Cole.
Mirrors the `startup-radar` result — the second-person-description defect is now confirmed in
two of the five skills on the remaining-audits list, worth a quick sweep of the other three
(`orchestrate-agents`, the three prompt skills) on a future night.

Related: [[skill-authoring-playbook]] · [[concert-digest]] · [[claude-code-skills]] ·
[[skill-audits-2026]] · [[skill-evals-playbook]] · [[skill-audit-startup-radar]] ·
[[skill-audit-networking-prep]] · [[skill-audit-wiki-query]] · [[skill-audit-worked-example]] ·
[[Claude Mastery]]
