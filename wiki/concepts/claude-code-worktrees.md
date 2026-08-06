---
type: concept
created: 2026-08-04
---
# Claude Code Worktrees — file isolation for parallel agents

A **git worktree** is a separate working directory with its own files and its own branch,
sharing the same `.git` history and remote as the main checkout. [[claude-code|Claude Code]]
uses worktrees so that **parallel sessions and sub-agents edit different files without
colliding** — one session can build a feature while another fixes a bug, and neither stomps
the other's edits. Worktrees isolate the *files*; [[claude-code-subagents|sub-agents]] and
[[claude-code-agent-teams|agent teams]] coordinate the *work*. (Grounded in the official
[Claude Code worktrees docs](https://code.claude.com/docs/en/worktrees), Aug 2026 snapshot.)

## Why it matters here

This vault's direction is increasingly **multi-agent** (see [[claude-code-agent-teams]],
[[claude-code-subagents]], [[multi-agent-orchestration]]). The blocker for running agents in
parallel is not reasoning — it's **write conflicts**: two agents editing the same tree
corrupt each other's work. Worktrees are the mechanism that makes safe parallelism possible,
which is why the course's own **"GitHub & Worktrees"** chapter sits right before the selling
section (see [[build-sell-claude-code-course]]).

## The two everyday moves

Most sessions need only these:

1. **Start a session in a worktree** — `claude --worktree <name>` (or `-w`). Creates an
   isolated worktree under `.claude/worktrees/<name>/` on a new branch `worktree-<name>`,
   and launches Claude there. Run it again with a different name in another terminal for a
   second isolated session. Omit the name and Claude generates one (e.g. `bright-running-fox`).
   You can also just ask Claude to *"work in a worktree"* mid-session — it uses the
   `EnterWorktree` tool.
2. **Clean up on exit** — on exit Claude checks the worktree for work that removal would
   delete (changed/untracked files, new commits). A **clean** unnamed worktree is removed
   automatically; a **named** one or a worktree **with work** prompts you to keep or remove.
   Non-interactive `-p` runs don't prompt or clean up — remove them with `git worktree remove`.

> Add `.claude/worktrees/` to `.gitignore` so worktree contents don't show as untracked
> files in the main checkout.

## Sub-agent isolation (`isolation: worktree`)

The multi-agent payoff: give each parallel sub-agent its own worktree so their edits never
conflict. Ask Claude to *"use worktrees for your agents"*, or make it permanent for a custom
sub-agent by adding `isolation: worktree` to its frontmatter in `.claude/agents/`:

```markdown
---
name: refactorer
description: Applies mechanical refactors across many files
isolation: worktree
---
```

Each sub-agent gets a **temporary** worktree, auto-removed when it finishes **without
changes**; a worktree that still holds work stays on disk until a periodic sweep can remove
it safely. While an agent runs, Claude Code `git worktree lock`s its worktree so cleanup
can't yank it out from under a running agent.

## Base branch — where a worktree forks from

The `worktree.baseRef` setting controls the fork point:
- **`"fresh"` (default)** — branch from the remote default branch (usually `main`), so the
  worktree starts clean. Claude keeps `origin/HEAD` current (fetches if stale >24h, 5s cap).
- **`"head"`** — branch from your current local `HEAD`, carrying unpushed commits. Use this
  when isolating sub-agents that must operate on **in-progress work**.

You can't point `baseRef` at an arbitrary branch name; to start from a specific existing
branch, create the worktree with git directly (`git worktree add`). You can also fork a
worktree from a PR: `claude --worktree "#1234"` (quote the `#`).

## Carrying gitignored files in (`.worktreeinclude`)

A worktree is a fresh checkout, so untracked files like `.env` aren't present. A
`.worktreeinclude` file (`.gitignore` syntax) at the project root copies matching gitignored
files into every new worktree Claude creates — env files, secrets configs — without
duplicating tracked files.

## What a worktree shares with the main checkout

Not everything is isolated. A worktree **shares**: the repository's `.git` directory (so
`git commit` works from inside a worktree, even under [[claude-code-permissions|sandboxing]]),
project-scope plugins (no reinstall per worktree), and saved permission approvals ("Yes,
don't ask again" saves to the main checkout and applies everywhere). Only the **working
files and branch** are isolated.

## Manual git equivalent

Worktrees are a plain git feature; Claude's flags are conveniences over it:
```bash
git worktree add ../project-feature -b feature-a   # new branch in a sibling dir
cd ../project-feature && claude                     # start Claude there
git worktree list                                   # see them all
git worktree remove ../project-feature              # clean up (--force if dirty)
```
For non-git VCS (SVN, Perforce, Mercurial), `WorktreeCreate`/`WorktreeRemove`
[[claude-code-hooks|hooks]] replace the default git logic.

## Related

- [[claude-code-subagents]] · [[claude-code-agent-teams]] · [[multi-agent-orchestration]] ·
  [[parallel-agents]] — the work-coordination side that worktrees make safe to parallelize.
- [[claude-code-permissions]] — sandboxing still allows the shared-`.git` writes worktrees need.
- [[agentic-automation-patterns]] — worktree-per-agent is the isolation pattern that keeps
  parallel automation from corrupting a shared tree.
- [[build-sell-claude-code-course]] — the "GitHub & Worktrees" chapter this expands.

**Sources:** official Claude Code docs — [Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees).
