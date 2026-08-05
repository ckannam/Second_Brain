# Claude Code Skills

Reusable capabilities you give [[claude-code]]: a folder with a markdown `SKILL.md` (name + trigger description) plus optional reference files. When Claude sees a prompt matching a skill's description, it loads and follows the skill automatically — or it fires on a slash command (`/skill-name`).

Sources: [[master-claude-code-skills-28min]], [[claude-code-skills-update]], [[evals-for-taste]], [[governed-skills-framework]].

## The two types

| Type | Description | Durability |
|---|---|---|
| **Capability uplift** | Teaches Claude to do something it can do imprecisely (design conventions, formula patterns) | Disposable — retire if the next model handles it natively; evals detect this |
| **Encoded preference** | A personal sequential workflow Claude isn't trained on (concert digest, startup radar) | Durable — models won't learn your personal procedures |

Encoded-preference skills are the more valuable long-term investment. Capability uplift skills pay off quickly but age out.

## Anatomy of a good SKILL.md

```yaml
---
name: skill-name
description: >
  Use when [specific conditions]. Triggered by [exact phrases].
  Do NOT use when [boundary conditions — differentiate adjacent skills].
---
```

**Body patterns from high-performing skills:**
- One-sentence purpose statement up top.
- Point to external files for heavyweight logic (don't stuff SKILL.md with the entire workflow — it's a router, not a dump). See `vault-autoresearch/SKILL.md → program.md` or `startup-radar`.
- Numbered steps for sequential workflows; prose for judgment-based ones.
- Explicit "Guardrails / Rules" or "NEVER" section — what the skill must not do.
- Keep it thin. SKILL.md loads on every trigger; heavy context costs tokens every invocation.

Optional frontmatter: `disable_model_invocation: false` (allows natural-language invocation, not just slash commands); `argument_hint` (Cole can pass context at invocation time).

## Trigger tuning — the description is the only trigger surface

Claude sees only the `description` field when deciding whether to fire a skill. Weak descriptions produce false triggers or misfires; strong ones are crisp and differentiated:

**Patterns that work:**
- Lead with `Use when` or `Use to`, followed by exact user phrasing that should trigger it.
- Enumerate specific phrases: `"run the concert digest"`, `"weekly startup discovery"`, `/wiki-query`.
- Explicitly differentiate adjacent skills: e.g., `vault-autoresearch` says "for answering a question from the wiki use wiki-query instead."
- Multi-line YAML (`>`) for complex triggers improves accuracy.

Slash commands (`/skill-name`) are a reliable fallback when natural-language triggering is uncertain.

## Anthropic's Skill Creator

Install via `/plugins` → search `skill-creator`. It:
- Scaffolds a new SKILL.md from a natural-language description (asks clarifying questions first).
- Modifies and optimizes existing skills.
- Runs evals → pass rate / latency / token cost with and without the skill.
- Performs trigger tuning: tests sample prompts against the description, scores them, rewrites the description.
- Runs an audit step at the end of any build.

**Future direction (Anthropic):** "Over time, a natural-language description of what the skill should do may be enough, with the model figuring out the rest." Trend is toward high-level specs, not step-by-step instructions.

## Evals — two distinct goals

| Goal | Description |
|---|---|
| **Catch regressions** | As models improve, a previously good skill may degrade silently. Evals give early signal to iterate or retire. |
| **Spot growth** | If the model handles the task better *without* the skill, delete the skill. Don't drag dead weight. |

**Grader types** (from [[evals-for-taste]]):
- **Code-based** — deterministic (count, string match). Fast, cheap, brittle. Use for "does it exist?" checks.
- **Model-based** — rubric-driven, scored 0–5. Use for quality judgments. Critical: ask for pros/cons *first*, then derive a score — not the reverse (the model will rationalize whatever number it generates first). Anchor the grader with bad and good examples or scores drift high.
- **Human** — spot checks and A/B tests only; too expensive for routine evals.

**QA loop:** Create-agent → Critic-agent (told "there ARE problems, find them") → iterate until both converge. The adversarial framing beats confirmation mode.

Evals are living artifacts — graders saturate and need recalibration as the system improves.

## Skills vs Subagents vs Inline (CLAUDE.md)

| | Skill | Subagent | Inline (CLAUDE.md) |
|---|---|---|---|
| Scope | Loaded on trigger | Independent context window | Always loaded |
| Best for | Repeatable named procedure | Heavy/isolated/parallel task | Universal rules and preferences |
| Token cost | Zero when not triggered | Own window | Always in context |
| Improvable with evals | Yes | Yes | Harder |

See [[skills-vs-subagents]] for the full decision tree.

## Build a skill when…

- You have given the same instructions more than twice.
- You want auto-triggering from natural language.
- You want to track quality over model upgrades with evals.

## Anti-patterns

- **Generic trigger** — description so broad it fires on unrelated prompts. Erodes trust in the whole system.
- **Over-specific trigger** — skill effectively never runs on natural language.
- **No `Don't use when` boundary** — adjacent skills collide.
- **Hardcoded volatile facts** — model names, pricing, external URLs age out and become noise.
- **Capability uplift without evals** — no way to detect when the model has outpaced the skill.
- **SKILL.md as a documentation dump** — loads on every invocation; heavy context costs tokens every time.

## This vault's skill inventory

Vault skills live in `.claude/skills/`. Current set:
- **claude-chat-prompt / claude-code-prompt / claude-cowork-prompt** — prompt-architect trilogy for Claude chat / Code / Cowork contexts.
- **concert-digest** — Monday iMessage digest of concerts near Cole by his artists.
- **networking-prep** — per-person prep brief + pitch for networking conversations, linked to [[outreach-pipeline]].
- **orchestrate-agents** — decision ladder for single→sub→team→CMA agent orchestration (built 2026-08-01).
- **startup-radar** — weekly startup discovery / triage.
- **token-context-management** — 4-lever quick-ref for context hygiene + compaction (built 2026-08-01).
- **vault-autoresearch** — nightly self-heal + build loop (the loop this vault runs on).
- **vault-improve** — ad-hoc vault quality improvements on demand.
- **wiki-query** — answer a question from the vault wiki.

Related: [[skills-vs-subagents]], [[claude-code-subagents]], [[ai-second-brain-levels]] (Level 3), [[evals-for-taste]], [[governed-skills-framework]], [[claude-code-skills-update]], [[prompt-engineering-playbook]].
