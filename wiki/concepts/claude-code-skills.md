# Claude Code Skills

Reusable capabilities you give [[claude-code]]: a folder with a markdown `SKILL.md` (name + trigger description) plus optional reference files. When Claude sees a prompt matching a skill's description, it loads and follows the skill automatically — or it fires on a slash command (`/skill-name`).

## Anatomy

```
.claude/skills/<skill-name>/
  SKILL.md        # required — frontmatter + body
  <ref-files>     # optional — any files Claude may read during execution
```

**Frontmatter fields** (YAML between `---` markers at top of SKILL.md). Only `description`
is really needed; everything else is optional (grounded in the official
[Claude Code skills docs](https://code.claude.com/docs/en/skills)):

| Field | What it does |
|---|---|
| `name` | Display name in the skill listing; defaults to the directory name. Kebab-case. |
| `description` | **The trigger surface.** What the skill does *and when to use it* — Claude reads only `name` + `description` at startup and matches requests against it; the body loads only on a match. Combined with `when_to_use`, truncated at **1,536 chars** in the listing, so put the key use case first. See [[skill-trigger-tuning]]. |
| `argument-hint` | Autocomplete hint for expected args (e.g. `[issue-number]`). |
| `disable-model-invocation` | `true` = never auto-load; runs only on explicit `/name`. Also blocks preloading into [[claude-code-subagents|subagents]] and (as of v2.1.196) **prevents the skill from firing when a [[proactive-agents|scheduled task]] uses it as the prompt** — relevant to this vault's own nightly run. Default `false`. |
| `user-invocable` | `false` = hide from the `/` menu (background knowledge users shouldn't call directly). Default `true`. |
| `allowed-tools` | Tools pre-approved **without a permission prompt** for the turn that invokes the skill; the grant **clears on your next message**. Space/comma-separated or a YAML list. (Not a restriction list — a per-turn pre-approval.) |
| `model` | Model override while the skill is active; reverts to the session model next prompt. |
| `context: fork` | Run the skill in a **forked subagent context** instead of the main thread — the frontmatter bridge to [[skills-vs-subagents|skills-vs-subagents]]. |
| `agent` | Which subagent type to use when `context: fork` is set. |
| `paths` | Glob patterns that limit auto-activation to matching files (comma-separated or YAML list). |

Custom slash commands (`.claude/commands/*.md`) are now the same primitive — see
[[claude-code-custom-commands]].

## Skill types (personal vs project)

- **Global skills** (`~/.claude/skills/`) — available across all Claude Code sessions.
- **Project skills** (`.claude/skills/` inside a repo) — active only in that project.

Src: [[claude-code-skills-update]].

## Triggering lifecycle

1. **Startup scan** — Claude reads `name` + `description` from all skills in scope.
2. **Semantic match** — Claude compares the user's request against descriptions; selects the matching skill.
3. **Full load + execution** — Claude loads the complete SKILL.md and follows it.

For trigger reliability, description quality is everything — see [[skill-trigger-tuning]].

## Six-step build workflow

From [[master-claude-code-skills-28min]] (Nate Herk's 28-min primer):

1. **Identify the repetition** — notice you're giving Claude the same instructions across sessions; that's the signal to package them into a skill.
2. **Define scope** — personal vs project, global vs local; what files does the skill need?
3. **Write the SKILL.md** — frontmatter (name + description) + the instruction body (what Claude should do).
4. **Add reference files** if the skill needs persistent knowledge (a style guide, a template, an API spec).
5. **Test** — invoke the skill, check if it fires as expected, watch for under- or over-triggering.
6. **Debug + tune** — iterate on the description if triggering is unreliable; use the Skill Creator's A/B eval loop ([[claude-code-skills-update]]) for systematic improvement.

## Skill Creator + evals

[[claude-code-skills-update]]: Anthropic's **Skill Creator** scaffolds new skills; the built-in **eval system** measures trigger performance (A/B, 3 runs per query, held-out test set) and proposes description improvements. The loop: build → eval → tune description → re-eval. See [[skill-trigger-tuning]] for the trigger side; [[evals-for-taste]] for the broader grading-system pattern.

## When to build a skill (the feedback cycle)

Build when you find yourself repeating the same instructions across Claude Code sessions. A skill packages that once and re-applies it without repetition. At scale, a library of well-tuned skills becomes a governed organizational asset — see [[governed-skills-framework]] for the Man Group example (~100+ skills, regulated environment).

## In practice (examples from this vault)

| Skill | What it does | Key trigger pattern |
|---|---|---|
| [[wiki-query]] | Answers questions from vault content | "what does the wiki say about X" |
| [[vault-autoresearch]] | Runs the nightly self-heal loop | "run autoresearch", "heal the wiki" |
| [[networking-prep]] | Preps Cole for a networking meeting | "I'm networking with X", "prep for a call" |
| [[orchestrate-agents]] | Guides agent-team design | "parallel agents", "agent swarm" |
| [[token-context-management]] | Manages context efficiently | "context is getting long" |

**Legacy form:** `.claude/commands/<name>.md` creates the same `/name` slash command without a folder. As of 2026 this is unified with skills (same frontmatter, same `/` menu). See [[claude-code-custom-commands]] for the full comparison.

Related: [[skills-vs-subagents]], [[claude-code-subagents]], [[ai-second-brain-levels]] (Level 3). Depth: [[skill-trigger-tuning]] (trigger reliability), [[evals-for-taste]] and [[governed-skills-framework]] (evaluating and governing skills at scale).
