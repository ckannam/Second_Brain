---
type: concept
category: skill-audit
created: 2026-10-25
about: "[[orchestrate-agents]]"
---

# Skill Audit — `orchestrate-agents`

Audit of `.claude/skills/orchestrate-agents/SKILL.md` against the six-section
[[skill-authoring-playbook]] checklist. Run 2026-10-25 as part of the ongoing "Improve +
general skills" @cloud task.

Prior audits in this series: [[skill-audit-worked-example]] (`startup-radar`),
[[skill-audit-networking-prep]], [[skill-audit-vault-autoresearch]], [[skill-audit-wiki-query]],
[[skill-audit-startup-radar]].

## Skill snapshot

| Field | Value |
|---|---|
| File | `.claude/skills/orchestrate-agents/SKILL.md` |
| Lines | 57 |
| Last edited | 2026-08-01 (created as part of "Agent max" task) |
| Audited | 2026-10-25 |

## Section-by-section findings

### §1 — Description (trigger surface)

**Finding: ⚠️ minor — description used imperative/named-person form.**

Previous description:
> "Use when Cole asks how to orchestrate multiple Claude Code agents, set up an agent team,
> parallelize work across agents, assign QA roles, or asks about sub-agents vs. agent teams
> vs. Claude Managed Agents. Also triggers on 'I want agents to work together', 'parallel
> agents', 'agent swarm', or 'QA agent'."

The description opened with "Use when Cole asks…" — an imperative instruction that names a
specific person ("Cole") rather than describing the skill in third-person form per the
playbook. The playbook's anti-pattern is "You can use this to…" / "I can help you…"; the
named-person variant ("Cole asks") has the same discovery-surface problem.

**🔧 Fix applied (2026-10-25):** Rewrote to third-person action form:
> "Guides multi-agent orchestration decisions in Claude Code — choosing between sub-agents,
> agent teams, and Claude Managed Agents; setting up teams; parallelizing work; assigning QA
> roles. Triggers on: 'orchestrate agents', 'set up an agent team', 'parallelize work across
> agents', 'sub-agents vs. agent teams', 'I want agents to work together', 'parallel agents',
> 'agent swarm', 'QA agent'."

Improvement: (a) leads with what the skill *does* before listing triggers; (b) adds "set up
an agent team", "parallelize work across agents", "sub-agents vs. agent teams" as explicit
trigger terms to strengthen retrieval.

### §2 — Progressive disclosure

✅ **Clean.** Body is 57 lines — well under the ~500-line ceiling. Content is a decision table,
pattern descriptions, pitfall table, and escalation guide — all appropriately in the body (no
need to externalize to `reference/` files at this scale). No nested reference chains. The
skill references wiki pages via wikilinks rather than loading them inline, which is correct.

### §3 — Conciseness

✅ **Clean.** No filler or over-explanation. The pattern-picker table is tight (4 rows × 1
column), the pitfall table covers the real failure modes without padding, and the CMA
escalation section gives only the decision criteria. The "Related" footer is appropriate
in-body navigation rather than redundant prose.

### §4 — Degrees of freedom

✅ **Clean.** Skill is an open-field decision guide: multiple valid orchestration patterns exist,
so the body gives direction with a table and rules of thumb rather than an exact script. This
matches the "open field → prose direction" heuristic.

### §5 — Evals (universal vault gap)

❌ **No evals** (same as every other vault skill except `vault-autoresearch`, whose HEALTH_DEBT
ratchet is its built-in eval). Recommended triplets for Cole when implementing
([[skill-evals-playbook]]):

1. **"How do I run 3 agents in parallel on separate tasks?"** — should trigger; Claude should
   produce the tmux split-pane setup + 3-agent team with non-overlapping file scopes.
2. **"Should I use a sub-agent or a skill for this research step?"** — should trigger; Claude
   should route to [[skills-vs-subagents]] and give the isolation-vs-procedure decision.
3. **"What is Claude Managed Agents?"** — should trigger; Claude should cover the CMA
   escalation criteria (shared state across sessions, production scale, outcome-orientation).

### §6 — Anti-patterns

✅ **Clean.** No voodoo constants, no deep reference nesting, no time-sensitive advice that
will rot, no too-many-options overload, no Windows-style paths, no inconsistent terminology.

## Summary

| Section | Status | Action |
|---|---|---|
| §1 Description | ⚠️ minor | 🔧 Fixed: third-person form |
| §2 Progressive disclosure | ✅ Clean | None |
| §3 Conciseness | ✅ Clean | None |
| §4 Degrees of freedom | ✅ Clean | None |
| §5 Evals | ❌ No evals | Recommendation for Cole (3 triplets above) |
| §6 Anti-patterns | ✅ Clean | None |

**Overall: healthy skill.** One structural fix applied (§1 description form). No behavioral
changes. The universal §5 evals gap is noted for Cole.

Related: [[orchestrate-agents]] · [[skill-authoring-playbook]] · [[skill-evals-playbook]] ·
[[skill-audit-worked-example]] · [[skill-audit-vault-autoresearch]] · [[skill-audit-wiki-query]] ·
[[skill-audit-startup-radar]] · [[skill-audits-2026]] · [[claude-code-skills]] · [[Claude Mastery]]
