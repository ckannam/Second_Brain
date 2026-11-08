---
type: concept
category: audit
created: 2026-11-08
about: "[[concert-digest]]"
---

# Skill Audit — `concert-digest`

Audit of `.claude/skills/concert-digest/SKILL.md` (51 lines) against [[skill-authoring-playbook]]
(six-section checklist). Conducted 2026-11-08 as part of the **Claude Mastery — improve + general
skills** task. `concert-digest` was one of the last unaudited vault skills (the others are
`token-context-management` and the three prompt-architect skills).

---

## §1 — Description (trigger surface)

**Finding:** Description opened in second-person imperative ("Use to compose (and, in standalone
mode, send)…") — the playbook §1 requires **third person**, because the description is injected into
the system prompt where first/second-person phrasing causes discovery problems.

**Fix applied (structural, no behavior change):** "Use to compose (and, in standalone mode, send)" →
"Composes (and, in standalone mode, sends)". Same grammatical conversion applied to `startup-radar`
on 2026-10-11 ([[skill-audit-startup-radar]]); it preserves every trigger term.

Remainder is strong: concrete trigger phrase ("run the concert digest") + the automation hook ("the
Monday launchd run"), concrete nouns (`profile/concert-taste.md`, "iMessage self-chat", metro), and a
clear what + when. ~425 chars (limit 1,024).

---

## §2 — Progressive disclosure

**Passes.** 51 lines — far under the ~500-line ceiling. No reference files needed. `send.scpt` is
**executed** via `osascript`, not loaded as text — correct per playbook (script output costs tokens,
source does not). No domain-split warranted at this length.

---

## §3 — Concise

**Passes.** Lean throughout. The detail it carries is earned: the exact text-native block template,
the exact `osascript` delivery call, and the honest-empty fallback. No padding explaining generic
concepts. Correctly assumes Claude knows what a web search or an iMessage is.

---

## §4 — Degrees of freedom

**Passes — well-matched, and the most interesting skill on this axis.** It mixes all three freedom
levels correctly:
- **Low freedom (narrow bridge):** the compose-block template (§5) and the `osascript` delivery call
  (§6) are consistency-critical output/side-effect steps — correctly given as an exact template + exact
  command.
- **Open field (high freedom):** search + rank + discovery (steps 3–4) are judgment calls left as
  prose direction — correct, since taste-matching has many valid routes.
- **The fabrication guard is the right "narrow bridge" rail** for the fragile part: "Never invent
  shows, dates, venues, or ticket links… write `tix: search` instead of a fabricated URL."

---

## §5 — Evals (gap — needs Cole)

**No evals built yet** — the universal gap across every audited vault skill ([[skill-audits-2026]]).
`concert-digest` is a strong eval candidate because its main failure mode (hallucinated shows/links)
is concrete and checkable. Three recommended tests for the interactive Skill Creator run:

1. **Empty-week honesty test** — give a metro + window with no credible shows; expect the honest
   "🎵 Quiet week near you…" note, **not** a fabricated show. (Tests the §Rules fabrication guard.)
2. **Link-fabrication guard** — a real show whose ticket URL isn't confidently found; expect
   `tix: search "{artist} {venue}"`, not a made-up URL.
3. **Mode-contract test** — `MODE=section` returns **only** the block with no `osascript` send;
   `MODE=standalone` sends via `osascript` then stops with no duplicate print. (Tests the two-mode
   delivery contract — a side-effect correctness check, important because standalone actually texts.)

Building + running these needs the eval harness + Cole (a live send) — same `@local`/interactive
blocker as the other skills. See [[skill-evals-playbook]] for the triplet format.

---

## §6 — Anti-patterns

**Passes — clean.** No time-sensitive info; no "too many options"; no nested references; forward
slashes only (the `osascript` path is a correct absolute macOS path); terminology consistent ("block",
"metro"/`ACTIVE_METRO`, "window"); no voodoo constants (the `~8–12` show cap is justified — "so the
text stays scannable"); no `helper`/`utils` naming.

*Minor observation (not a fix):* "do NOT recompute the metro" appears in both §Inputs and §Rules. This
is deliberate safety reinforcement of the cutover contract, not drift — left as-is.

---

## Summary

| § | Check | Status |
|---|---|---|
| 1 | Description third-person, what+when, trigger-specific | **Fixed** (second-person → third) |
| 2 | Progressive disclosure, ≤500 lines | Pass |
| 3 | Concise, no redundant context | Pass |
| 4 | Freedom matched to task fragility | Pass (all three levels, correctly) |
| 5 | Evals exist | **Gap** — 3 tests recommended for interactive run |
| 6 | No anti-patterns | Pass (one minor observation, no fix) |

One structural fix applied (§1 third-person); one eval gap logged for Cole. Skill is otherwise healthy.

Related: [[skill-authoring-playbook]] · [[concert-digest]] · [[skill-audits-2026]] ·
[[skill-audit-startup-radar]] · [[skill-evals-playbook]] · [[claude-code-skills]] · [[Claude Mastery]]
