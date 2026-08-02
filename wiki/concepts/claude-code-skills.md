# Claude Code Skills

Reusable capabilities you give [[claude-code]]: a folder with a markdown instruction file (name + description that controls **when it triggers**) plus optional **reference files**.

## Anatomy

```
.claude/skills/<skill-name>/
  SKILL.md        # required — frontmatter + body
  <ref-files>     # optional — any files Claude may read during execution
```

**Frontmatter fields** (YAML between `---` markers at top of SKILL.md):
- `name` — the skill's identifier (kebab-case).
- `description` — **the trigger surface.** Claude reads only `name` + `description` at startup; the body loads only when a description match fires. See [[skill-trigger-tuning]] for how to write effective descriptions.
- `disable-model-invocation: true` — opt out of automatic triggering; skill runs only on explicit invocation.
- `allowed-tools` — restrict which tools the skill may use during execution.

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

Related: [[skills-vs-subagents]], [[claude-code-subagents]], [[ai-second-brain-levels]] (Level 3). Depth: [[skill-trigger-tuning]] (trigger reliability), [[evals-for-taste]] and [[governed-skills-framework]] (evaluating and governing skills at scale).
