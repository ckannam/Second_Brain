---
type: concept
category: audit
created: 2026-11-15
about: "[[concert-digest]]"
---

# Skill Audit — `concert-digest`

Audit of `.claude/skills/concert-digest/SKILL.md` against [[skill-authoring-playbook]]
(six-section checklist). Conducted 2026-11-15 as part of the **Claude Mastery — Improve +
general skills** task.

---

## §1 — Description (trigger surface)

**Finding:** Description opened with "Use to compose (and, in standalone mode, send)…" —
second-person imperative. The playbook requires third-person form because the description is
injected into the system prompt, where "Use to…" language can cause discovery problems.

**Fix applied:** Changed "Use to compose (and, in standalone mode, send)" →
"Composes (and, in standalone mode, sends)" in the frontmatter `description` field.

Remainder of description is solid: packs what+when, names the input file
(`profile/concert-taste.md`), names the specific trigger phrase ("run the concert digest"),
includes the MODE distinction (standalone vs section). No length issue (~220 chars; limit 1,024).

---

## §2 — Progressive disclosure

**Passes.** Body is ~50 lines — well under the ~500-line ceiling. The Steps, Compose template,
and Rules all fit inline; no reference files needed. The output format template is a code block
(zero extra context cost once Claude has parsed it).

---

## §3 — Concise

**Passes.** Steps are appropriately detailed: exact input keys (`ACTIVE_METRO`, `TODAY`, `MODE`),
the ranking hierarchy (love > want-to-see > discovery → soonest date → cap 8–12), and the
fallback "quiet week" message. All detail is earned — this is exactly what Claude doesn't already
know about Cole's taste and how the iMessage digest should look. No generic padding.

---

## §4 — Degrees of freedom

**Passes.** A hybrid skill: the delivery mechanism (Step 6 `osascript` call) is narrow-bridge
(exact command, exact path, no improvisation allowed), while the discovery search and ranking
logic is appropriately open-field (prose direction lets Claude use judgment on which shows to
surface). The fallback "quiet week" message is correctly prose, not a fixed template.

---

## §5 — Evals (gap — needs Cole)

**No evals built yet.** This is a @local skill (runs on Cole's Mac via launchd); interactive
eval development needs Cole. Three recommended tests to run with Cole:

1. **Metro-trust test** — provide a prompt with `ACTIVE_METRO=baltimore`; verify Claude does
   NOT re-derive the metro from any other source. Expected: output begins "🎵 Concerts near you —
   Baltimore…" and shows only Baltimore/DC-area venues.
2. **Empty-week fallback test** — provide a future date with no known shows in the metro for
   any artist; verify Claude sends the "🎵 Quiet week near you" fallback and does NOT fabricate
   venue/date/link.
3. **Fabrication guard test** — provide a niche artist not on Cole's lists as a discovery seed
   with no actual upcoming shows; verify Claude writes `tix: search "…"` rather than a live
   link it invented.

---

## §6 — Anti-patterns

**One flag (noted, not fixed — @local concern):** Step 6 uses a hardcoded absolute path:
`/Users/colekannam/.claude/concerts/send.scpt`. This is acceptable for a @local skill (it only
runs on Cole's Mac where this path exists), but it means the skill is non-portable by
construction. No action taken — changing it is a @human/local decision; flagging here for
awareness.

No other anti-patterns: no time-sensitive info, no voodoo constants, no Windows-style paths,
consistent terminology (`ACTIVE_METRO`, `MODE`, "discovery"), no `helper`/`utils` naming.

---

## Summary

| § | Check | Status |
|---|---|---|
| 1 | Description is third-person, what+when, trigger-specific | **Fixed** (second-person → third) |
| 2 | Progressive disclosure, ≤500 lines | Pass |
| 3 | Concise, no redundant context | Pass |
| 4 | Freedom matched to task fragility | Pass |
| 5 | Evals exist | **Gap** — 3 tests recommended for interactive run with Cole |
| 6 | No anti-patterns | Pass (hardcoded path noted; @local skill, acceptable) |

One structural fix applied; one eval gap logged for Cole.

Related: [[skill-authoring-playbook]] · [[skill-audits-2026]] · [[claude-code-skills]] ·
[[skill-audit-startup-radar]] · [[skill-audit-worked-example]] · [[Claude Mastery]]
