# Claude Code Skill Creation Playbook

A practical, end-to-end guide for building, testing, and tuning [[claude-code-skills|Claude Code skills]] reliably. Synthesized from [[master-claude-code-skills-28min]], [[claude-code-skills-update]], [[governed-skills-framework]], and the official Anthropic skills docs (verified August 2026).

## When to build a skill (vs the alternatives)

| You keep doing… | Use |
|---|---|
| Pasting the same instructions every session | Skill |
| A section of `CLAUDE.md` growing into a multi-step procedure | Skill (extracts it; body only loads when needed) |
| A one-off workflow with side-effects you must control | Skill + `disable-model-invocation: true` |
| A decision that requires live codebase context | Subagent (see [[skills-vs-subagents]]) |
| A standing fact or convention Claude should always know | `CLAUDE.md` entry (not a skill) |

Feedback cycle: **build a skill when you find yourself repeating the same instructions.** Source: [[master-claude-code-skills-28min]].

## Anatomy — the directory structure

```
.claude/skills/my-skill/
├── SKILL.md              # required — instructions + frontmatter
├── reference.md          # optional — large docs Claude reads on demand
├── examples/
│   └── sample.md         # optional — expected output format
└── scripts/
    └── validate.sh       # optional — executable script
```

Reference supporting files from `SKILL.md` so Claude knows they exist. Keep `SKILL.md` under 500 lines — move large reference material to separate files.

## SKILL.md frontmatter — key fields

```yaml
---
name: my-skill                      # display label (directory name = /command)
description: >                      # THE trigger surface — see below
  What the skill does and when to use it.
when_to_use: >                      # extends description; both count toward 1,536-char cap
  Trigger phrases or example requests.
disable-model-invocation: true      # only YOU can invoke (use for deploys, commits, etc.)
user-invocable: false               # only CLAUDE invokes (for background reference)
context: fork                       # runs in isolated subagent (background by default)
background: false                   # wait for forked result in current turn (v2.1.218+)
effort: high                        # override session effort level for this skill
allowed-tools: Bash(git *) Read     # tools pre-approved for the invoking turn only
disallowed-tools: AskUserQuestion   # tools blocked while skill runs (e.g. background loops)
paths: "src/**/*.ts"                # only activate for files matching this glob
---
```

**Who-invokes matrix:**

| Frontmatter | You | Claude | Description in context |
|---|---|---|---|
| (default) | ✅ | ✅ | Always loaded |
| `disable-model-invocation: true` | ✅ | ❌ | Not loaded (can't trigger) |
| `user-invocable: false` | ❌ | ✅ | Always loaded |

## The description is the most important field

Claude decides when to auto-invoke a skill by treating all `SKILL.md` descriptions as tool definitions. **`description` + `when_to_use` are truncated together at 1,536 characters in the skill listing** — put the key use case first.

**Proven patterns:**
- Lead with what the skill does, then when: `"Summarizes uncommitted changes and flags anything risky. Use when the user asks what changed, wants a commit message, or asks to review their diff."`
- Add explicit triggers: `"DO trigger when the user says: 'write me a prompt', 'create a prompt', 'build a prompt'"`
- Add explicit exclusions: `"Do NOT trigger when the user is just asking a question about prompting"`
- Match the phrases users actually type — not how *you* would describe the task

**Failure modes to avoid:**
- Too vague (`"Do X"`) → fires on everything or nothing
- Too long → truncated at 1,536 chars; move detail to `when_to_use`
- Doesn't match natural phrasing → silent non-invocation

## Nate Herk's 6-step build framework

Source: [[master-claude-code-skills-28min]]

1. **Identify the repetition** — what instruction do you keep pasting?
2. **Create the directory** under `~/.claude/skills/` (personal, all projects) or `.claude/skills/` (project only)
3. **Write the SKILL.md** — description first, then instructions
4. **Test automatic invocation** — type something matching the description; confirm skill loads
5. **Test direct invocation** — type `/skill-name`; confirm skill loads
6. **Debug and tune** — if it doesn't fire, update the description with the exact phrase you used

## Skill Creator + Evals workflow (Anthropic-native, March 2026)

The `/skill-creator` bundled skill scaffolds new skills and measures existing ones. Source: [[claude-code-skills-update]].

### Step 1 — Create or scaffold
Run `/skill-creator` and describe what you want. It writes the `SKILL.md` frontmatter and body.

### Step 2 — Write 3 evals (5 min investment)
Save to `<skill-dir>/evals/evals.json`. Write exactly three:

- **Positive case** — a prompt where the skill *should* fire and work correctly
- **Negative case** — a prompt where the skill *should not* fire (false positive check)
- **Edge case** — ambiguous or boundary condition

Anthropic found issues in 5 of 6 of their own internal skills when they ran evals. If Anthropic's skills need fixing, assume yours do too.

### Step 3 — Run Skill Creator's eval mode
It runs your eval prompts, scores pass/fail, and surfaces which case failed.

### Step 4 — Trigger tuning
The Skill Creator analyzes your `description` against your eval prompts and suggests edits to cut false positives and false negatives. Iterate until all 3 evals pass.

### Step 5 — Re-run after model updates
Evals ensure skills survive model upgrades. Run after any major Claude version bump.

## Dynamic context injection

Inject live data into the skill before Claude sees it:

```markdown
## Current state
!`git status --short`
!`git log --oneline -5`
```

The shell command runs first; output replaces the placeholder. Claude receives actual data, not the command. **Only fires when `!` is at the start of a line or after whitespace.**

Multi-line version:
````markdown
```!
node --version
cat package.json | jq '.dependencies'
```
````

## Running a skill in a subagent

```yaml
---
description: Run a full code review in isolation
context: fork
background: false   # wait for result before continuing (v2.1.218+)
---
```

`context: fork` runs the skill in a fresh subagent with no conversation history. Use for long-running, isolated tasks (reviews, deploys, batch operations). Without `background: false`, the fork runs in background while you continue working.

## Where skills live — precedence

| Location | Path | Scope |
|---|---|---|
| Enterprise | managed settings | All org users |
| Personal | `~/.claude/skills/<name>/` | All your projects |
| Project | `.claude/skills/<name>/` | This repo only |
| Plugin | `<plugin>/skills/<name>/` | Where plugin enabled |

Enterprise overrides personal; personal overrides project. A project skill with the same name as a bundled skill (e.g. `code-review`) replaces it.

**Cloud sessions (Cowork / routines):** personal `~/.claude/skills/` is NOT synced to cloud. For cloud availability:
- Enable the skill for your claude.ai account, OR
- Commit it to the project's `.claude/skills/`

## Skill content lifecycle

Once invoked, the skill's rendered `SKILL.md` stays in context for the rest of the session. After auto-compaction, Claude Code re-attaches the most recent invocation of each skill (up to 5,000 tokens each, shared 25,000 token budget). If a skill stops influencing behavior after compaction, re-invoke it.

`allowed-tools` grants clear when you send your next message — the permission is per-turn, not per-session.

## Arguments

```yaml
---
arguments: [issue, branch]   # named positional args
---
Fix issue $issue on branch $branch.
```

Or positionally: `/my-skill "hello world" second` → `$0` = `hello world`, `$1` = `second`. Use `$ARGUMENTS` for the full raw string.

## Anti-patterns

- **Skill ≠ CLAUDE.md fact**: CLAUDE.md is for standing conventions; a skill's body only loads when invoked — move long procedures out of CLAUDE.md into a skill.
- **Don't skip evals**: a skill that fires correctly today may break after a model update.
- **Don't set `disable-model-invocation` by default**: only use it for workflows with side effects (deploys, sends, merges).
- **Don't write multi-paragraph SKILL.md body for reference content that changes**: put that in a supporting file and reference it.

## Related pages
- [[claude-code-skills]] — concept overview
- [[skills-vs-subagents]] — when to delegate to a subagent instead
- [[governed-skills-framework]] — teaching + governing skills at org scale
- [[claude-code-subagents]] — subagent architecture
- [[claude-code-hooks]] — hooks that fire deterministically around skill invocations
- [[token-context-management]] — keeping skill content cost under control
