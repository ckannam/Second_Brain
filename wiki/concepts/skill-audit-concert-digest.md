---
type: concept
created: 2026-11-08
---

# Skill audit — `concert-digest`

Applies the [[skill-authoring-playbook]] 6-section checklist to `.claude/skills/concert-digest/SKILL.md`.
Part of the ongoing "Improve + general skills" @cloud task; companion to [[skill-audits-2026]].

**Subject:** `.claude/skills/concert-digest/SKILL.md`, 51 lines, git-tracked.
Composes (and in standalone mode sends) Cole's weekly "Concerts near you" iMessage digest.
Reads `profile/concert-taste.md`, web-searches artists and venue calendars for the active metro,
ranks by taste tier, and formats a text-native block for iMessage. Triggered by the Monday launchd
run or Cole's manual prompt. Created as part of the Personal bucket automation.

---

## §1 Description (trigger surface): 🟡 (recommend — not applied)

**Current:** `Use to compose (and, in standalone mode, send) Cole's weekly "Concerts near you"
iMessage digest. Reads profile/concert-taste.md, uses the active metro + today's date passed in
the prompt, web-searches his artists and local venue calendars, ranks by taste and proximity with
taste-matched discovery, and delivers a short text-native block to his iMessage self-chat.
Triggered by the Monday launchd run or when Cole says "run the concert digest".`

**Findings:**
- **Second-person form.** `"Use to compose…"` is imperative/second-person. The playbook §1 rule
  is "Third person, always" — the description is injected into the system prompt and third-person
  form aids consistent retrieval. It should read `"Composes Cole's weekly…"`.
- **What + when: ✅** The description packs both what (compose/send iMessage digest) and when
  (Monday launchd run OR `"run the concert digest"`). Trigger phrase coverage is good.
- **Key terms: ✅** "concert", "iMessage", "digest", "Concerts near you" — solid match surface.
- **Length: ✅** ~430 chars, well under the 1,024-char limit.

**Recommendation for Cole:** Change the opening from `"Use to compose"` to `"Composes"` (or
`"Composes and delivers"`). This is a §1 description-surface change; it affects what the system
prompt sees at startup, so it falls in the review lane rather than an unattended structural fix.

---

## §2 Progressive disclosure: ✅

51 lines — well under the ~500-line ceiling. No reference files needed. All procedure fits inline:
inputs in the header, numbered steps for the core logic, and a labeled output-format template.
Single-level structure with no nested references. Good.

---

## §3 Concise: ✅

Steps are imperative and lean. The output-format code block gives the template at near-zero token
cost (a code block is cheaper than prose description of the same structure). No padding about what
iMessage or a venue calendar is. The `osascript` delivery command is specific and self-contained —
nothing ambiguous for Claude to figure out at runtime. 51 lines is appropriately compact for a
multi-step task with a web-search component.

---

## §4 Degrees of freedom: ✅

Appropriate split between low and medium freedom:
- **Low freedom (narrow bridge):** Inputs are pre-decided (`ACTIVE_METRO`, `TODAY`, `MODE` come
  from the caller — do NOT recompute); output format is an exact template; delivery is an exact
  `osascript` command. The "Rules" section (never invent shows; don't override the metro; keep the
  message phone-readable) are the right guardrails for a fragile, consistency-critical output.
- **Medium freedom:** Ranking (taste tier → soonest date), discovery selection, and "how many
  shows to cap at" (8–12) leave appropriate room for judgment within the template structure.

The balance matches §4's "robot on a path" heuristic: narrow bridge for the delivery mechanics,
open field for the content curation within those constraints.

---

## §5 Evals: 🟡 (recommend — not applied)

No evals exist. Three recommended test triplets for when eval infrastructure is ready:

1. **Honest "quiet week" behavior:**
   - Query: `"Run concert digest MODE=section ACTIVE_METRO=triangle TODAY=2026-11-10 — no shows
     found in the search"`
   - Expected: output sends the honest fallback format (`"🎵 Quiet week near you…"`) with no
     invented shows, dates, or links.
   
2. **Taste-tier ranking + format compliance:**
   - Query: `"Run concert digest MODE=section ACTIVE_METRO=triangle TODAY=2026-11-10"` (seed
     search with a known Love-tier artist playing that week)
   - Expected: output follows the exact template; Love-tier artist appears before discovery;
     no markdown bold; no fabricated URLs (uses `tix: search …` if unsure).

3. **MODE routing:**
   - Query: `"Run concert digest standalone"` vs `"section"`
   - Expected: `standalone` triggers the `osascript` send command; `section` outputs the block
     only without calling any external command.

---

## §6 Anti-patterns: ✅ (with one intentional exception noted)

- **Time-sensitive info:** None. No dated guidance in the body.
- **Too many options:** One approach (search → rank → template → deliver). Clean.
- **Hardcoded absolute path:** `osascript /Users/colekannam/.claude/concerts/send.scpt` is an
  absolute Mac path — the same anti-pattern flagged in `startup-radar`'s Step 7. **However,
  this is intentional and correct here:** `concert-digest` is a `@local` skill designed to run
  on Cole's Mac (iMessage delivery requires macOS). The absolute path is the right form for a
  user-specific system-level script. No fix applied.
- **Terminology:** Consistent throughout ("active metro", `ACTIVE_METRO`, "metro"). ✅
- **Voodoo constants:** `~8–12 shows` is explained inline ("so the text stays scannable"). ✅
- **Vague names:** No `helper`/`utils` naming. ✅

---

## Verdict

| Section | Status | Action |
|---|---|---|
| §1 Description | 🟡 | Recommend: change `"Use to compose"` → `"Composes"` (third-person form; review lane) |
| §2 Progressive disclosure | ✅ | None |
| §3 Concise | ✅ | None |
| §4 Degrees of freedom | ✅ | None |
| §5 Evals | 🟡 | Recommend: 3 eval triplets above (needs eval harness) |
| §6 Anti-patterns | ✅ | None (absolute path is intentional for @local iMessage delivery) |

**No unattended structural fixes applied** — the one structural note (§1 form) affects the trigger
surface and belongs in the review lane.

**Overall health: good.** The skill is well-scoped, correctly constrained, and compact. The two
recommendations (§1 form, §5 evals) are the same universal patterns the vault's other skills share.

---

Related: [[skill-authoring-playbook]] · [[skill-audits-2026]] · [[skill-evals-playbook]] ·
[[claude-code-skills]] · [[Claude Mastery]].
