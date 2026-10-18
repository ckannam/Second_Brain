---
type: concept
created: 2026-09-13
---

# Skill audits — running log (2026)

Applies the [[skill-authoring-playbook]] 6-section checklist to each vault skill. The
companion to [[skill-audit-worked-example]] (which is the detailed walkthrough of the template
using `startup-radar` as the subject). This page is the **audit log** — a running record of
findings across all vault skills, dating from the first batch in Sept 2026. New audits are
appended as they're run.

One safety rule for every entry: **structural / no-behavior-change fixes only** are applied
unattended (path consistency, link format); trigger-surface and content changes are
**recommendations for Cole** (those shift what a skill does or when it fires, which can't be
verified without a live run — same split as the [[vault-autoresearch]] auto-merge / PR lane).

---

## 2026-09-13 — `orchestrate-agents` (55 lines)

**Subject:** `.claude/skills/orchestrate-agents/SKILL.md`, 55 lines, git-tracked. Agent
orchestration decision guide: single → sub-agent → team → CMA; spawning rules, common
pitfalls table, CMA escalation. Created 2026-08-01 as part of the Agent max build.

**§1 Description (trigger surface): ✅**
Third-person ("Use when Cole asks how to orchestrate…"), packs what+when, carries concrete
trigger nouns ("orchestrate multiple Claude Code agents", "agent team", "parallel agents",
"QA agent"). Four literal phrase hooks. No under-triggering risk.

**§2 Progressive disclosure: ✅**
55 lines — well under the ~500-line ceiling. No references needed. Decision table fits inline.

**§3 Concise: ✅**
Steps are imperative and lean. Decision ladder in a code block costs near-zero tokens. No
padding about what "context window" or "tmux" means — correctly assumes Claude knows.

**§4 Degrees of freedom: ✅**
Medium freedom: a fixed decision ladder (code block) for the routing choice, prose latitude for
the judgment call about which pattern fits. The pitfall table is a good "narrow bridge" guard
for the fragile parts (write collisions, QA gaps).

**§5 Evals: 🟡 (recommend — not applied)**
No evals exist. Three recommended tests to build when eval infrastructure is ready:
1. *"Isolated file-indexing task → should recommend sub-agent"* — expected: output recommends
   the Sub-agents section + cites "context isolation" as the rationale.
2. *"Parallel QA review task → should recommend agent team with explicit QA role"* — expected:
   output mentions "assign a QA/reviewer agent explicitly" (Rule 2).
3. *"Shared persistent state across sessions → should escalate to CMA"* — expected: CMA section
   mentioned with the "multiple agents need shared persistent state" cue.
Building + running these needs the eval harness, so deferred.

**§6 Anti-patterns: ✅**
No time-sensitive info. All paths are wikilinks (no vault-internal file paths). No voodoo
constants. Terminology consistent throughout ("sub-agent", "team", "CMA"). No `utils`/`helper`
naming.

**Verdict:** 4 sections clean, 1 recommendation (evals). No structural fixes applied — skill is
healthy as-is.

---

## 2026-09-13 — `wiki-query` (71 lines)

**Subject:** `.claude/skills/wiki-query/SKILL.md`, 71 lines, git-tracked. Executable form of
the AGENTS.md Query operation: index-first, graph traversal, freshness reconciliation, file-back.

**§1 Description (trigger surface): ✅**
Third-person ("Use when the user asks a question meant to be answered from this Second Brain
vault/wiki"), four specific trigger phrasings, includes the `/wiki-query` command literal.
Covers the key user intent ("according to my notes"). Solid retrieval surface.

**§2 Progressive disclosure: ✅**
71 lines — under the ceiling. The procedure fits inline; no split needed.

**§3 Concise: 🟡 (recommend — not applied)**
The Guardrails section partially restates AGENTS.md content ("Never invent facts", "Links >
pages", "Snapshots age") — the skill's own header says "Do not restate AGENTS.md's rules here."
The bullets do add an operation-specific framing (emphasizing the file-back discipline for
queries), but they echo language already in AGENTS.md. Recommend trimming the Guardrails to
only what the header correctly exempts — operational reminders that are unique to query
mode — on the next human-reviewed skill pass.

**§4 Degrees of freedom: ✅**
Medium freedom: a numbered procedure for the retrieval discipline, prose latitude for synthesis.
Navigational-vs-real-query classification at step 1 correctly routes the most common short-circuit.

**§5 Evals: 🟡 (recommend — not applied)**
No evals. Three recommended tests:
1. *"What does the vault say about spaced repetition?" → should cite wiki pages, not general
   knowledge; answer traced to specific `[[pages]]`.*
2. *"Which page covers X?" (navigational) → should skip the file-back step; answer is direct.*
3. *"Question whose answer spans two contradicting pages → should flag the contradiction.*
Needs eval harness.

**§6 Anti-patterns: ✅**
No time-sensitive info, no voodoo constants, no Windows paths. The only internal path reference
(`index.md`) is correct and stable.

**Verdict:** 3 sections clean, 1 structural recommendation (Guardrails condensation — review
lane, not applied tonight), 1 eval recommendation. No unattended fixes needed — skill is
healthy.

---

## 2026-09-13 — `vault-autoresearch` (41 lines)

**Subject:** `.claude/skills/vault-autoresearch/SKILL.md`, 41 lines, git-tracked. Routes the
vault self-heal / AutoResearch loop to `autoresearch/program.md`; states the five invariants and
the two-lane rule.

**§1 Description (trigger surface): ✅**
Exemplary: specific triggers ("run autoresearch", "heal the wiki", "improve the vault", "lower
the health debt", "/vault-autoresearch command"), AND a sibling-skill redirect ("For answering a
question from the wiki use wiki-query instead") — exactly the cross-redirect pattern the
[[skill-trigger-tuning]] playbook recommends. No ambiguity with `vault-improve` or `wiki-query`.

**§2 Progressive disclosure: ✅**
41 lines. The Invariants are the load-bearing content; the Quick start is 3 steps. Nothing to
split; nothing to add.

**§3 Concise: ✅**
Correctly delegates to `program.md` and `AGENTS.md` rather than restating their rules — the
opposite of the wiki-query anti-pattern. Best-practice conciseness.

**§4 Degrees of freedom: ✅**
Low freedom: exact commands (`python3 autoresearch/score.py`, `git checkout -- .`), exact phase
order, exact invariants. Correct for this fragile, ratcheted process.

**§5 Evals: 🟡 (recommend — meta-note)**
No evals in the traditional sense. The loop *is* its own eval (score.py is the objective
measure). A meta-eval would test whether the skill correctly routes the loop without deviation
(e.g. "should mention program.md as source of truth", "should cite invariant against editing
score.py"). Worth building once the eval harness is in place; lower priority than skills
without a built-in metric.

**§6 Anti-patterns: ✅**
Clean throughout. Commands are complete (`python3 autoresearch/score.py --json`, not just
`score.py`). No inconsistent terminology. No voodoo constants.

**Verdict:** 5 sections clean, 1 meta-eval recommendation. Healthiest skill in the vault — no
fixes applied or needed.

---

## 2026-10-18 — `concert-digest` (50 lines)

**Subject:** `.claude/skills/concert-digest/SKILL.md`, 50 lines, git-tracked. Composes (and in
standalone mode sends) Cole's weekly "Concerts near you" iMessage digest from
`profile/concert-taste.md` + web search. One of the two previously un-audited vault skills (the
other being the three prompt-architect skills, queued).

**§1 Description (trigger surface): 🔧 fixed (structural, no behavior change)**
Carried the same second-person lead-verb defect `startup-radar` had before its 2026-10-11 fix:
"**Use to compose** (and … send)…". Normalized to the declarative third-person "**Composes** (and …
sends)…" — matching the house style of every other audited skill. The actual trigger surface is
untouched: the literal hooks ("Concerts near you", "weekly … iMessage digest") and the explicit
*when* clause ("Triggered by the Monday launchd run or when Cole says 'run the concert digest'")
are preserved verbatim, so this is a mood/consistency edit, not a trigger-content change — the same
safe category applied to `startup-radar`.

**§2 Progressive disclosure: ✅**
50 lines — far under the ceiling. The 6-step procedure + Inputs + Rules all fit inline; no
reference split warranted.

**§3 Concise: ✅**
Steps are lean and imperative. The composed-block template is a worked example (earns its tokens by
pinning the exact iMessage-native format), not padding. Correctly assumes Claude knows what "web
search" and "iMessage" are.

**§4 Degrees of freedom: ✅**
Low-to-medium, correctly matched: an exact output template and exact `MODE` branch logic (fragile —
`standalone` sends, `section` must NOT), prose latitude for taste-ranking. The "never invent shows/
dates/links; write `tix: search \"…\"` instead" rule is a good narrow-bridge guard against the
hallucinated-ticket-link failure mode.

**§5 Evals: 🟡 (recommend — not applied)**
No evals (the universal vault-skill gap). Three recommended tests when the harness exists:
1. *Artist on the Love list with a real tour date in-window → block lists it under the taste tier,
   soonest-first, with a real or `tix: search` link (never a fabricated URL).*
2. *Empty week (no credible shows) → emits the honest "Quiet week" fallback, not an invented lineup.*
3. *`MODE=section` → returns ONLY the block and does NOT fire the `osascript` send.* (Guards the
   outward-action branch — the highest-stakes behavior in the skill.)

**§6 Anti-patterns: ✅**
No time-sensitive constants. The one absolute path (`/Users/colekannam/.claude/concerts/send.scpt`)
is **correct, not a defect** — it's a Mac-only `osascript` send step on the `@local`/standalone lane,
unlike the `startup-radar` case where a *vault-internal* path should have been relative. Terminology
consistent (`ACTIVE_METRO`, `MODE`, `window_weeks`). No voodoo constants.

**Verdict:** 5 sections clean, 1 structural fix applied (§1 third-person normalization), 1 eval
recommendation. Skill is healthy; the fix brings its description into house style.

---

## Summary across all audited skills (updated 2026-10-18)

| Skill | Lines | §1 Desc | §2 Disclosure | §3 Concise | §4 Freedom | §5 Evals | §6 Anti-patterns | Fixed |
|---|---|---|---|---|---|---|---|---|
| `startup-radar` (2026-08-08) | 198 | ✅ | ✅ | ✅ | ✅ | 🟡 | 🔧 path | Step 7 path |
| `orchestrate-agents` | 55 | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | none |
| `wiki-query` | 71 | ✅ | ✅ | 🟡 | ✅ | 🟡 | ✅ | none |
| `vault-autoresearch` | 41 | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | none |
| `concert-digest` (2026-10-18) | 50 | 🔧 → ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | §1 3rd-person |

**Cross-skill pattern:** the universal gap is **evals (§5)**. Every audited skill lacks an
objective test harness. The one-line fix for all of them: write ~3 `(query, files,
expected_behavior)` triples each and run them once before any description or body change. Until
that infrastructure exists, the [[vault-autoresearch]] HEALTH_DEBT ratchet remains the
vault-level proxy for skill quality — a skill that sends the loop off-track shows up as raised
debt. See [[evals-for-taste]] for the pattern, [[llm-as-judge]] for the grader architecture.

Related: [[skill-authoring-playbook]] · [[skill-audit-worked-example]] · [[skill-trigger-tuning]] ·
[[evals-for-taste]] · [[vault-autoresearch]] · [[Claude Mastery]].
