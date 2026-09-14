---
type: concept
created: 2026-07-31
---
# Token & Context Management in Claude Code

Strategies for staying inside the context window and keeping the active context **signal-dense** — the "Tokens & context windows" chapter of [[build-sell-claude-code-course]] treats this as core Claude Code literacy. Most problems compound fast once you hit the limit, so management up-front beats recovery.

## Why it matters

Claude Code's context window is finite. As a session grows — tool outputs, file reads, long conversations — older content is pushed out and eventually compacted. Poor context hygiene means:
- CLAUDE.md instructions get buried under noise and are ignored
- The agent loses track of earlier decisions and repeats work
- Compaction fires more often, potentially losing critical state

## The four layers

### 1. CLAUDE.md files (human-written instructions)
The most durable context: loaded at session start, project-scoped, not consumed by conversation. Key rule from [[claude-code-memory]]: **keep each CLAUDE.md under ~200 lines** so Claude reliably adheres to everything in it. Content beyond that threshold tends to be under-followed.

Scopes (from most to least broad): org-wide → user (`~/.claude/CLAUDE.md`) → project (`./CLAUDE.md`) → local (`CLAUDE.local.md`). Narrower scope overrides broader for the same key.

**What belongs in CLAUDE.md:** project conventions, test/build commands, file layout, known constraints, workflow rules. What does NOT belong: large reference docs, raw data, things that belong in wiki pages.

### 2. Auto memory (Claude-written)
Claude writes notes to `~/.claude/projects/<repo>/memory/MEMORY.md` automatically across sessions — build commands, debugging insights, patterns. Only the first 200 lines / 25KB load at session start; topic files load on demand. Manage via `/memory`. Source: [[claude-code-memory]].

### 3. Compaction (/compact)
When the context window fills, Claude Code compacts — summarizing the conversation history into a shorter form. This is automatic, but you can trigger it with `/compact`. **What you lose:** fine-grained tool-use history; **what survives:** the model's synthesis of what happened.

Compaction is a reset point, not just pruning. To survive it well:
- Put durable rules in CLAUDE.md, not in the conversation
- Use **`PreCompact`/`PostCompact` hooks** (see [[claude-code-hooks]]) to trigger cleanup before/after
- A **`SessionStart` hook with a `compact` matcher** can re-inject critical reminders into the fresh context after compaction fires

### 4. Sub-agents as context isolation
Each [[claude-code-subagents|sub-agent]] gets **its own context window** — so delegating a heavy file-read task to a sub-agent keeps the parent's context clean. This is as much a context strategy as a delegation one: when a task will consume a lot of context, isolating it in a sub-agent protects the main thread. See [[skills-vs-subagents]].

For [[claude-code-agent-teams|agent teams]], each team member also has its own window — the cost of parallelism is that coordination messages consume context in every agent.

## Platform-level context management

[[claude-managed-agents]] (the production platform) absorbs context-management maintenance automatically: compaction, caching, [[context-anxiety]] handling (the model behavior where an agent declares done too early). This is a key reason to reach for CMA in production: the harness co-evolves with models so individual apps don't have to. Source: [[context-anxiety]].

## Practical heuristics

- **Dense > verbose in CLAUDE.md:** One specific rule beats three vague ones. Under 200 lines.
- **Read small:** Ask for specific sections rather than whole files; favor targeted file reads over broad context dumps.
- **Compact proactively:** If you're about to switch to a very different task in the same session, `/compact` first rather than letting noise accumulate.
- **Sub-agent for heavy reads:** If a task requires reading 10+ files, consider a sub-agent so the parent thread isn't consumed.

## Concrete knobs & the MCP budget (from ECC)
The third-party [[ecc]] harness packages a set of specific context-economy settings worth knowing
(reconcile against the current [[opus-4-8]] defaults — these are its 2026 opinions, not Anthropic law):
- **`CLAUDE_CODE_SUBAGENT_MODEL=haiku`** — run [[claude-code-subagents|sub-agents]] on a cheaper model; pairs with the context-isolation point above.
- **`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50`** — compact at 50% rather than ~95%, trading a little history for better quality in long sessions.
- **`MAX_THINKING_TOKENS`** — cap hidden reasoning spend per request.
- **The MCP budget rule (the one most relevant to this vault):** each enabled MCP server's tool
  descriptions consume context. **Keep <10 MCP servers and <80 tools active** — a window overloaded
  with MCP metadata can shrink a 200k budget to ~70k of usable space. Cole runs *many* connectors
  (Notion, Gmail, Calendar, Drive, PitchBook, Spotify, Strava, Wispr, Chrome…); disabling unused ones
  per-project is real context reclaimed. Src: [[affaan-ecc-agent-harness-os]].

## Rules as a third, always-loaded layer
ECC also argues for separating **rules** — always-loaded, *selectively installed* language/project
standards — from [[claude-code-skills|skills]] (loaded on demand) and [[claude-code-hooks|hooks]] (run
outside the model). The insight for context hygiene: always-loaded standards are a permanent tax, so
install only the one or two packs you actually use rather than dumping every convention into
`CLAUDE.md`. This vault collapses all of this into CLAUDE.md/[[instructions-as-code|AGENTS.md]]; the
layer distinction is a cleaner mental model even without adopting ECC's tooling.

Related: [[claude-code-memory]], [[claude-code-hooks]], [[claude-code-subagents]], [[claude-code-agent-teams]], [[context-anxiety]], [[skills-vs-subagents]], [[ecc]], [[mcp]], [[instructions-as-code]].
