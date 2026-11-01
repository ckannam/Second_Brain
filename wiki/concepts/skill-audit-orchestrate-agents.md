---
type: concept
created: 2026-11-01
---

# Skill audit — `orchestrate-agents` (2026-11-01)

**Subject:** `.claude/skills/orchestrate-agents/SKILL.md`, ~57 lines, git-tracked. Agent
orchestration decision guide for Claude Code: single → sub-agent → team → CMA pattern picker;
spawning rules, common pitfalls table, CMA escalation signals. Created 2026-08-01 as part of
the Agent max build. A brief audit entry exists in [[skill-audits-2026]] (2026-09-13); this is
the standalone version with a corrected §1 verdict and the full template format. Audited against
[[skill-authoring-playbook]]; format mirrors [[skill-audit-worked-example]].

## The audit

### §1 — Description is the trigger surface — 🟡 (recommend — not applied)

The description packs what+when, four literal phrase hooks ("orchestrate multiple Claude Code
agents", "agent team", "parallel agents", "QA agent"), and names all relevant sub-patterns
(sub-agents, agent teams, Claude Managed Agents). Retrieval surface is solid.

**Correction of 2026-09-13 entry:** The prior audit marked §1 ✅ and described the description
as "Third-person ('Use when Cole asks…')". Strictly, "Use when Cole asks" opens with an
imperative-conditional construction, not true third-person declarative form. The playbook
specifies: *"Write 'Processes Excel files and generates reports'" — not "Use this when…"*.

- 🟡 **Recommend (not applied — consistent with vault precedent):** Rewrite to pure third-person:
  e.g. "Guides agent orchestration in Claude Code: single → sub-agent → team → CMA decision
  ladder. Use when Cole asks how to orchestrate…" — or simply "Answers agent orchestration
  questions in Claude Code, covering sub-agents vs. agent teams vs. Claude Managed Agents…". The
  trigger phrases ("I want agents to work together", "parallel agents", "agent swarm", "QA agent")
  are the real firing hooks and should be kept. **Not applied tonight** because (a) `wiki-query`
  and `networking-prep` both share the "Use when/whenever Cole" pattern and have been audited ✅
  at least twice each — a unilateral fix to one skill while leaving the others unchanged adds
  inconsistency; (b) description changes shift trigger behavior and belong in a human-reviewed
  pass across all affected skills. Flagged for a batch description-style pass with Cole.

### §2 — Progressive disclosure keeps it cheap — ✅

~57 lines — well under the ~500-line ceiling. The decision ladder (code block), pitfall table,
and CMA escalation all fit inline. No reference files needed. No split required.

### §3 — Be concise (assume Claude is smart) — ✅

Steps are imperative and lean. The decision ladder costs near-zero tokens as a code block.
The pitfall table is a tight "narrow bridge" guard. No padding explaining what "context window"
or "tmux" means — correctly assumes Claude knows. No action.

### §4 — Match degrees of freedom to task fragility — ✅

Correctly **medium-freedom**: a fixed decision ladder (code block) for the routing choice (which
can't tolerate ambiguity — picking the wrong pattern compounds fast), with prose latitude for the
judgment call about whether a task "benefits from parallelism + QA." The pitfall table is the
right constraint level for the failure modes that actually happen (write collisions, QA gaps).

### §5 — Build evals first, then iterate — 🟡

No evals exist. The three from the 2026-09-13 entry, reproduced for completeness:

1. *"Isolated file-indexing task → should recommend sub-agent"* — expected: output recommends
   the Sub-agents section + cites "context isolation" as the rationale.
2. *"Parallel QA review task → should recommend agent team with explicit QA role"* — expected:
   output mentions "assign a QA/reviewer agent explicitly" (Rule 2).
3. *"Shared persistent state across sessions → should escalate to CMA"* — expected: CMA section
   mentioned with the "multiple agents need shared persistent state" cue.

Needs eval harness (code-based or model-graded pass/fail). See [[skill-evals-playbook]].

### §6 — Anti-patterns — ✅

No time-sensitive info. All paths are wikilinks (`[[claude-code-agent-teams]]`,
`[[claude-managed-agents]]`, etc.) — no vault-internal file paths. No voodoo constants.
Terminology consistent throughout ("sub-agent", "team", "CMA"). The wikilinks in the Related
section all resolve (`[[claude-code-agent-teams]]`, `[[claude-code-subagents]]`,
`[[multi-agent-orchestration]]`, `[[skills-vs-subagents]]`, `[[agent-observability]]`,
`[[claude-managed-agents]]`, `[[tmux]]`, `[[parallel-agents]]`, `[[agent-memory]]`,
`[[agent-dreaming]]`, `[[context-anxiety]]` — all exist as wiki pages).

## Verdict

4 sections clean, 1 carry-over recommendation corrected from ✅ → 🟡 (§1 description style —
vault-consistent pattern, not applied; batch fix deferred to Cole), 1 eval recommendation (§5).
No structural fixes applied tonight. Skill is healthy and correct as-is.

**Key correction vs. 2026-09-13 entry in [[skill-audits-2026]]:** §1 verdict revised from ✅ to
🟡. The "Use when Cole asks" pattern is functionally acceptable and consistently applied across
multiple vault skills, but it is not strictly third-person per the playbook. Recommend a
coordinated batch update to all skills sharing this pattern (also applies to `wiki-query` and
`networking-prep`) rather than isolated unattended fixes.

---

Related: [[skill-authoring-playbook]] · [[skill-audits-2026]] · [[skill-audit-worked-example]] ·
[[skill-evals-playbook]] · [[claude-code-agent-teams]] · [[claude-code-subagents]] ·
[[multi-agent-orchestration]] · [[skills-vs-subagents]] · [[Claude Mastery]].
