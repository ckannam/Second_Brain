---
type: concept
created: 2026-10-18
---

# Skill audit — `concert-digest`

Applies the [[skill-authoring-playbook]] 6-section checklist to
`.claude/skills/concert-digest/SKILL.md` (51 lines, git-tracked).

**Subject:** Composes Cole's weekly "Concerts near you" iMessage digest — reads
`profile/concert-taste.md`, web-searches artists + local venue calendars for the active
metro within the configured window, ranks by taste/proximity with discovery picks, and
delivers a text-native block. In `MODE=standalone` it sends via `osascript`; in
`MODE=section` it returns the block only. Triggered by the Monday launchd run or by a
manual user prompt. Created 2026-08-01 (later audit; not in the original creation batch).

**Audit date:** 2026-10-18. Run by the overnight autoresearch loop.

---

## §1 Description (trigger surface): 🔧 (one fix applied)

**Before fix:** `Use to compose (and, in standalone mode, send) Cole's weekly "Concerts near
you" iMessage digest. Reads profile/concert-taste.md, uses the active metro + today's date
passed in the prompt, web-searches his artists and local venue calendars, ranks by taste and
proximity with taste-matched discovery, and delivers a short text-native block to his iMessage
self-chat. Triggered by the Monday launchd run or when Cole says "run the concert digest".`

**Finding:** Description opens with "Use to compose…" — the same second-person imperative
pattern that the `startup-radar` audit (2026-10-11) fixed ("Use to discover" → "Discovers
and triages"). The playbook requires third-person form: the description is injected verbatim
into the system prompt, and imperative/infinitive openers ("Use to…", "Use when you…") can
cause discovery problems. Also: "Cole says 'run the concert digest'" should be "the user
says" for canonical skill-prompt language.

**Fix applied (structural, no behavior change):**
`Use to compose...` → `Composes and delivers...`
`Cole says "run the concert digest"` → `the user says "run the concert digest"`

**After fix:** `Composes and delivers Cole's weekly "Concerts near you" iMessage digest; in
standalone mode also sends via osascript. Reads profile/concert-taste.md, uses the active
metro + today's date passed in the prompt, web-searches his artists and local venue calendars,
ranks by taste and proximity with taste-matched discovery, and delivers a short text-native
block to his iMessage self-chat. Triggered by the Monday launchd run or when the user says
"run the concert digest".`

Trigger keywords and phrases are preserved; behavior unchanged.

---

## §2 Progressive disclosure: ✅

51 lines — well under the ~500-line ceiling. The step sequence, input block, rules, and
delivery modes fit inline without splitting. `profile/concert-taste.md` is loaded by an
explicit read in Step 1 (the correct pattern — on-demand, not pre-loaded). The external
`send.scpt` is called rather than embedded. No reference files needed.

---

## §3 Concise: ✅

Steps are imperative and lean. The template block (Step 5) is the minimum needed for
consistent digest formatting. The two-branch delivery in Step 6 is exactly two bullets.
No redundant context about what iMessage or osascript is — correctly assumes Claude knows.
The "honest short note" pattern (no shows found) is specified concisely without over-explaining.

---

## §4 Degrees of freedom: ✅

Low-to-medium freedom: a specific numbered sequence for retrieval and composition (necessary
for consistent digest structure), with latitude for how to phrase show descriptions. The
delivery is exact (osascript path, standalone-vs-section branching) — appropriate for a
fragile iMessage send step. The "never invent" rule is explicitly stated where it matters
most (shows/dates/links), not spread throughout.

---

## §5 Evals: 🟡 (recommend — not applied)

No evals exist. This is a @local skill (requires Cole's Mac for osascript delivery), so a
full end-to-end eval harness requires his Mac. However, the `MODE=section` output mode makes
partial evaluation feasible without sending to iMessage. Three recommended eval triplets:

1. *"Run the concert digest for Baltimore, section mode, today is 2026-11-01"* — expected:
   outputs a digest block with artists from `profile/concert-taste.md`'s Love/seen + Want
   list ranked before discovery picks; no osascript call; no fabricated links.
2. *"Quiet week scenario — no results from web search"* — expected: outputs the honest
   "Quiet week" message, not an empty list or placeholder shows.
3. *"Concert digest, standalone mode"* — expected: calls
   `osascript /Users/colekannam/.claude/concerts/send.scpt "<block>"` then stops without
   reprinting the block.

Building these needs the eval harness infrastructure; deferred.

---

## §6 Anti-patterns: ✅ (with design note)

**Absolute Mac path:** Step 6 calls
`osascript /Users/colekannam/.claude/concerts/send.scpt "<block>"`.
This is an absolute path to a file outside the vault (`~/.claude/concerts/send.scpt`). Unlike
the startup-radar §6 fix (which was a vault-internal path that could be made relative),
this path points to Cole's Mac-specific `.claude/` directory and cannot be expressed as a
vault-relative path. For a `@local` skill that runs exclusively on Cole's Mac, this is a
deliberate design choice — the path is correct for its environment.

**Design note:** If Cole ever changes his Mac username or moves `send.scpt`, this path would
break silently. Recommend that the `send.scpt` file include a comment pointing back to this
skill as its caller, and that any major Mac reconfiguration includes updating this path.
(Not a fixable §6 anti-pattern — noted for maintainability awareness.)

No time-sensitive info in the body. No voodoo constants (`8–12 shows` is explained; `window_weeks`
is a config variable). Terminology consistent throughout. No Windows-style paths (outside the
absolute Mac path discussed above). No `utils`/`helper` naming.

---

## Verdict

| Section | Status | Note |
|---|---|---|
| §1 Description | 🔧 fixed | "Use to compose" → "Composes and delivers"; "Cole says" → "the user says" |
| §2 Progressive disclosure | ✅ | 51 lines; on-demand reads; no split needed |
| §3 Concise | ✅ | Lean steps; minimal redundancy |
| §4 Degrees of freedom | ✅ | Appropriate low-medium freedom for iMessage delivery |
| §5 Evals | 🟡 recommend | No evals; 3 triplets recommended; @local constraint applies |
| §6 Anti-patterns | ✅ | Absolute path is intentional @local design; noted for maintainability |

**1 structural fix applied** (§1 description third-person form). **1 eval recommendation** (§5).
Skill is operationally healthy — the fix is cosmetic/canonical; no behavior change.

---

Related: [[skill-authoring-playbook]] · [[skill-audit-worked-example]] · [[skill-audits-2026]] ·
[[skill-evals-playbook]] · [[concert-digest]] · [[proactive-agents]] · [[Claude Mastery]].
