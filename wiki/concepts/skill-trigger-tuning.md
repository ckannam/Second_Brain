---
type: concept
created: 2026-08-02
---
# Skill Trigger Tuning

How to make a [[claude-code-skills|Claude Code skill]] fire reliably — or not fire when it shouldn't. The **description field is the trigger surface**: Claude reads every skill's name and description at startup to build a candidate list; a skill whose description doesn't match the request never loads at all.

## How triggering works (lifecycle)

1. **Startup scan** — Claude reads `name` + `description` from every SKILL.md in scope (global `~/.claude/skills/`, project `.claude/skills/`, shared `.claude/agents/`). Only the frontmatter is read at this stage; the body stays on disk.
2. **Semantic matching** — Claude compares the user's request (and current task context) against every loaded description. If the request semantically matches a description, that skill is selected.
3. **Full load + execution** — Claude loads the complete SKILL.md and follows it.

Implication: **the body of a SKILL.md is invisible until the description already matched.** All triggering decisions are made on `name` + `description` alone.

## What makes a description effective

Grounded in the real skills in this vault + patterns from [[claude-code-skills-update]] and [[master-claude-code-skills-28min]].

### Lead with "Use when…" or "Use to…"
Every description should state immediately *what situation* activates the skill. Claude parses this as intent-to-match.

```
# Good
description: Use when Cole asks how to manage context, avoid hitting the context
  limit, or asks about /compact…

# Weak
description: Helps with Claude context management.
```

### Be specific, not vague
A vague description rarely fires on the right query; a specific one fires reliably. Include the *exact phrases* Cole is likely to say.

```
# Good — covers semantic + literal
description: Use when Cole asks how to orchestrate multiple Claude Code agents,
  set up an agent team, parallelize work across agents, assign QA roles, or asks
  about sub-agents vs. agent teams vs. Claude Managed Agents. Also triggers on
  "I want agents to work together", "parallel agents", "agent swarm", or "QA agent".

# Weak
description: Helps with agent orchestration.
```

### Add explicit exclusions (redirect to sibling skills)
When two skills cover adjacent territory, add a redirect in each description so Claude picks the right one. Without this, the model has to guess.

```
description: Use when Cole wants an optimized prompt to paste into the Claude.ai
  chat app… For delegated async work use claude-cowork-prompt; for coding/repo work
  use claude-code-prompt.
```

The sibling-skill redirect pattern appears in every prompt-architect skill in this vault — it prevents overlap triggering and makes the skill set self-consistent.

### Cover both semantic intent AND literal phrases
Some skills fire on intent ("prep for a networking conversation"), others need to also catch specific phrases Cole says literally ("run the concert digest", "run the startup radar"). Use both:
- **Intent coverage**: describe the *situation* broadly enough to catch paraphrases.
- **Literal coverage**: list the exact strings Cole commonly types.

### Describe what the skill does (not just when)
Including a one-phrase summary of the output helps Claude distinguish overlapping skills:

```
description: Use to compose (and, in standalone mode, send) Cole's weekly
  "Concerts near you" iMessage digest. Reads profile/concert-taste.md, uses the
  active metro + today's date…
```

## Skill Creator + automated trigger tuning

[[claude-code-skills-update]] describes Anthropic's **Skill Creator** tool, which includes automated trigger tuning via A/B testing:
- Splits test queries: ~60% training / 40% held-out.
- Evaluates the current description by running each query **3 times** for a reliable trigger rate.
- Calls Claude to propose description improvements based on failure cases.
- Reports trigger-rate improvement across Anthropic's own skills — 5 of 6 public document-creation skills showed improved trigger accuracy after one optimization pass.

This loop mirrors [[eval-driven-model-selection]] applied to trigger matching: **don't guess at descriptions — measure, iterate, and keep the change only if it improves the metric** (same ratchet as [[vault-autoresearch]]'s HEALTH_DEBT pattern).

## Disabling automatic triggering

Set `disable-model-invocation: true` in frontmatter to prevent Claude from triggering the skill automatically. The skill then only runs when explicitly invoked (slash command or Skill tool call). Useful for skills whose body is expensive or whose trigger should be under manual control.

## Debugging misfires

| Symptom | Likely cause | Fix |
|---|---|---|
| Skill never fires | Description too vague / misses the user's phrasing | Add literal trigger phrases; check for synonym gaps |
| Skill fires on wrong queries | Description overlaps with sibling skills | Add "Do NOT use for X; use [[skill-Y]] instead" |
| Two skills compete | Adjacent descriptions without redirects | Cross-link redirects in both descriptions |
| Fires inconsistently | Description covers some phrasings but not others | Use the Skill Creator A/B loop to surface missed cases |

Related: [[claude-code-skills]], [[skills-vs-subagents]], [[claude-code-skills-update]], [[master-claude-code-skills-28min]], [[governed-skills-framework]], [[eval-driven-model-selection]].
