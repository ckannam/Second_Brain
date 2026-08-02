---
type: concept
created: 2026-08-02
---
# Claude Code Custom Commands

Custom slash commands — defined as markdown files in `.claude/commands/` — let you build reusable shortcuts that appear in the `/` menu and accept `$ARGUMENTS`. As of 2026 they are unified with [[claude-code-skills]]: a file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and support the same frontmatter. Official docs label the single-file form "legacy" and recommend skills, but existing `.claude/commands/` files keep working. Src: web-verified against official Claude Code docs, 2026-08-02.

## Anatomy (`.claude/commands/` form)

```
.claude/
  commands/
    deploy.md         # → /deploy command (project-scoped)
~/.claude/
  commands/
    my-review.md      # → /my-review command (global, all projects)
```

The markdown file's **body is the prompt** Claude runs when the command fires. Use `$ARGUMENTS` as a placeholder for anything the user types after the slash command:

```markdown
---
name: test-component
description: Run tests for a specific component
---
Run the tests for $ARGUMENTS, then report any failures with suggested fixes.
```

## Relationship with skills (2026 unification)

| Feature | `.claude/commands/<name>.md` | `.claude/skills/<name>/SKILL.md` |
|---|---|---|
| Creates `/name` slash command | ✅ | ✅ |
| Supports frontmatter | ✅ | ✅ |
| Accepts `$ARGUMENTS` | ✅ | ✅ |
| Can include reference files | ❌ (single file) | ✅ (full folder) |
| Official recommendation | Legacy | Current |
| Still works | ✅ | ✅ |

**When to use which:** for a simple prompt-as-shortcut (no reference files), either works. For a skill that needs supporting files (a style guide, an API spec, a template), use the `.claude/skills/` folder form. For new work, skills are preferred; commands files are a fine stepping stone.

## Scope

- **Project-scoped** (`.claude/commands/` in a repo) — available only in that project.
- **Global** (`~/.claude/commands/`) — available in every Claude Code session.
- Commands and skills can coexist in the same project; both appear in the `/` menu.

## Arguments

`$ARGUMENTS` is replaced at runtime with whatever the user types after the command name:

```
/deploy production          # $ARGUMENTS → "production"
/test-component AuthForm    # $ARGUMENTS → "AuthForm"
```

Commands without `$ARGUMENTS` run the file body verbatim.

## Relationship to CLAUDE.md

Each custom command executes within the context of the session's `CLAUDE.md` — project standards and conventions defined there are in scope without repeating them in the command file. This keeps command files focused on *the action*, not the *ambient rules*.

Related: [[claude-code-skills]], [[skill-trigger-tuning]], [[claude-md-router]].
