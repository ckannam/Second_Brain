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

## Summary across all audited skills (2026-09-13)

| Skill | Lines | §1 Desc | §2 Disclosure | §3 Concise | §4 Freedom | §5 Evals | §6 Anti-patterns | Fixed |
|---|---|---|---|---|---|---|---|---|
| `startup-radar` (2026-08-08) | 198 | ✅ | ✅ | ✅ | ✅ | 🟡 | 🔧 path | Step 7 path |
| `orchestrate-agents` | 55 | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | none |
| `wiki-query` | 71 | ✅ | ✅ | 🟡 | ✅ | 🟡 | ✅ | none |
| `vault-autoresearch` | 41 | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | none |

**Cross-skill pattern:** the universal gap is **evals (§5)**. Every audited skill lacks an
objective test harness. The one-line fix for all four: write ~3 `(query, files,
expected_behavior)` triples each and run them once before any description or body change. Until
that infrastructure exists, the [[vault-autoresearch]] HEALTH_DEBT ratchet remains the
vault-level proxy for skill quality — a skill that sends the loop off-track shows up as raised
debt. See [[evals-for-taste]] for the pattern, [[llm-as-judge]] for the grader architecture.

---

## 2026-10-25 — `concert-digest` (51 lines)

**Subject:** `.claude/skills/concert-digest/SKILL.md`, 51 lines, git-tracked. Composes (and
in standalone mode sends) Cole's weekly "Concerts near you" iMessage digest: reads
`profile/concert-taste.md`, web-searches artists + venue calendars for the active metro, ranks
by taste tier and proximity, delivers a text-native block. Part of the [[proactive-agents]]
family (Monday launchd run).

**§1 Description (trigger surface): 🔧 (fixed)**
The description opened in the imperative ("Use to compose (and, in standalone mode, send)…"),
the same second-person form the playbook §1 flags and the [[skill-audit-startup-radar]] audit
(2026-10-11) normalized. **Fix applied:** "Use to compose … send" → "Composes … sends" — a
leading-verb form change only; every trigger term is preserved ("Concerts near you", "concert
digest", the literal "run the concert digest" phrase, the Monday launchd hook). Remainder is
strong: concrete nouns (`profile/concert-taste.md`, `ACTIVE_METRO`), the what+when structure.

**§2 Progressive disclosure: ✅**
51 lines — far under the ~500-line ceiling. No reference files; the output template fits inline
in a code block (zero extra cost). No split needed.

**§3 Concise: ✅**
Lean imperative steps. The output-format code block earns its tokens (it fixes a consistency-
critical artifact — a phone-readable text block). No padding explaining what a "venue" or
"iMessage" is.

**§4 Degrees of freedom: ✅**
Medium-low, correctly matched. The delivery format is a fixed template (narrow bridge — it must
stay phone-scannable), while ranking and discovery are left to prose judgment (open field). The
"Never invent shows, dates, venues, or ticket links" rule is a well-placed narrow-bridge guard
against the skill's main failure mode (fabricated listings).

**§5 Evals: 🟡 (recommend — not applied)**
No evals. Four recommended tests for the interactive run:
1. *Window filter* — a show one day past `TODAY + window_weeks` → excluded.
2. *Dedup* — the same artist listed on two venue calendars → appears once.
3. *Empty week* — no credible hits → emits the honest "Quiet week" note, not a fabricated list.
4. *No-fabrication* — an artist with no verifiable date → `tix: search "…"`, never a made-up URL.

**§6 Anti-patterns: ✅**
No time-sensitive info, no voodoo constants, consistent terminology. **Considered but correct:**
the `osascript /Users/colekannam/.claude/concerts/send.scpt …` path is absolute, but unlike the
`startup-radar` `validate.py` case (a vault-internal path that could be relative) this script
lives *outside* the vault in `~/.claude/concerts/` and runs only on the `@local` lane, so an
absolute Mac path is correct here — not a portability defect.

**Verdict:** 1 structural fix (§1 third-person), 1 eval gap logged. Otherwise healthy.

---

## 2026-10-25 — prompt-architect family: `claude-chat-prompt`, `claude-cowork-prompt`, `claude-code-prompt` (39 / 38 / 37 lines)

**Subject:** the three sibling prompt-architect skills (shipped 2026-07-26), each turning a task
into an optimal prompt for one Claude surface — chat (interactive), Cowork (async delegation),
Code (agentic repo work). Audited together because they share one structure: *understand task →
pull Cole context ([[prompt-engineering-playbook]] + `[[cole|profile]]`) → apply role/context/
task/constraints/output-contract hygiene → shape for the surface → ready-to-paste block*.

**§1 Description (trigger surface): ✅ (exemplary)**
All three are the playbook's model §1. They use the endorsed `Use when …` trigger-context form
(the playbook's own example is "Use when working with PDFs…" — this is *not* the prohibited
first/second person, which is "I can help…" / "You can use this…"), pack what+when, carry the
literal phrase hooks ("write me a Claude chat/Cowork/Code prompt"), and — best of all — each
carries **sibling cross-redirects** ("For delegated async work use claude-cowork-prompt; for
coding/repo work use claude-code-prompt"), exactly the [[skill-trigger-tuning]] disambiguation
pattern. Three skills with near-identical intent that still route cleanly. No fix.

**§2 Progressive disclosure: ✅**
37–39 lines each — minimal. The per-surface "prompt shape" is the load-bearing content; no
references or splits warranted.

**§3 Concise: ✅**
Best-practice delegation: each grounds prompt theory in [[prompt-engineering-playbook]] /
[[the-prompting-playbook]] (and Code adds [[outcome-oriented-agents]], [[html-over-markdown-specs]])
by wikilink rather than restating it — the opposite of the wiki-query §3 anti-pattern.

**§4 Degrees of freedom: ✅**
Medium, correct for a generative task. A fixed sectioned "prompt shape" (role/task/context/
output-contract) gives structure; the actual drafting is left to Claude's judgment. The
per-surface shapes genuinely differ (chat invites iteration; Cowork front-loads everything +
definition-of-done; Code demands a verification contract) — the right axis to specialize on.

**§5 Evals: 🟡 (recommend — this *is* the "Prompt max" task's blocker)**
None. This maps directly to the open `@cloud` "Prompt max — eval-test the 3 prompt-architect
skills" item, repeatedly deferred because the eval run is interactive (needs Cole + a live
baseline). Recommended shared eval set (one task, three surfaces):
1. *Routing* — an async "research competitors and write a brief" task → `claude-cowork-prompt`
   fires (not chat); output includes a definition-of-done.
2. *Chat shape* — an open-ended "help me think through X" → `claude-chat-prompt`; output invites
   iteration rather than front-loading a spec.
3. *Code shape* — "add a feature + tests to repo Y" → `claude-code-prompt`; output names a
   verification/test step and a guardrail on what not to touch.

**§6 Anti-patterns: ✅**
Forward-slash wikilinks, consistent terminology ("prompt shape", "output contract"), no voodoo
constants, no time-sensitive info. **Design note (not a defect):** all three ground in
`[[cole|profile]]`, which is `profile/` — **local-only / gitignored** (personal identity data,
invisible to the cloud lane). That is the correct home for it, but it means these three skills
can only be *fully* exercised on Cole's Mac; the cloud lane can audit their structure (as here)
but not their Cole-tailoring output. Worth noting when the §5 evals are eventually run.

**Verdict:** all three 6/6 structurally clean — the cleanest-authored family in the vault
(textbook §1 with working sibling redirects). The only gap is the shared §5 eval run, which is
the "Prompt max" task itself and needs Cole.

---

## Updated scoreboard (2026-10-25)

Tonight's four audits (🔧 = fix applied, 🟡 = recommendation for Cole, ✅ = clean):

| Skill | Lines | §1 | §2 | §3 | §4 | §5 | §6 | Fixed |
|---|---|---|---|---|---|---|---|---|
| `concert-digest` | 51 | 🔧 | ✅ | ✅ | ✅ | 🟡 | ✅ | §1 third-person |
| `claude-chat-prompt` | 39 | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | none |
| `claude-cowork-prompt` | 38 | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | none |
| `claude-code-prompt` | 37 | ✅ | ✅ | ✅ | ✅ | 🟡 | ✅ | none |

**Coverage:** with these four, **10 of the vault's 11 skills now have a dedicated audit**
(`startup-radar`, `networking-prep`, `wiki-query`, `vault-autoresearch`, `orchestrate-agents`,
`vault-improve`, `concert-digest`, + the 3 prompt-architect skills). The one remaining —
`token-context-management` — was covered by the 2026-09-06 all-11 *structural sweep* (clean:
under the line ceiling, trigger surface sound) but has no dedicated section yet; it is the
natural next audit subject. The universal §5 **evals** gap persists across every skill, which is
why [[skill-evals-playbook]] / [[skill-evals]] own the how-to and the "Prompt max" + "Skill max"
tasks stay open pending an interactive Skill Creator eval run with Cole.

Related: [[skill-authoring-playbook]] · [[skill-audit-worked-example]] · [[skill-trigger-tuning]] ·
[[skill-audit-startup-radar]] · [[skill-evals-playbook]] · [[skill-evals]] · [[prompt-engineering-playbook]] ·
[[prompt-architect-skills]] · [[proactive-agents]] · [[evals-for-taste]] · [[vault-autoresearch]] · [[Claude Mastery]].
