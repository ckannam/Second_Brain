# Claude Code Memory

Two confirmed layers (official source: [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)):

## 1. CLAUDE.md files (human-written)
Persistent instructions you write in markdown — project conventions, commands, architecture.
Loaded into context at session start. Multiple scopes: org-wide, user (`~/.claude/CLAUDE.md`),
project (`./CLAUDE.md` / `.claude/CLAUDE.md`), local (`CLAUDE.local.md`). Target under 200
lines per file for reliable adherence. Manage via `/memory`.

## 2. Auto memory (Claude-written)
Claude accumulates notes automatically across sessions — build commands, debugging insights,
code preferences, workflow patterns. On by default. Storage: `~/.claude/projects/<repo>/memory/`
containing `MEMORY.md` (index, first 200 lines / 25KB loaded at session start) plus optional
topic files loaded on demand. Toggle via `/memory` → auto memory toggle, or set
`autoMemoryEnabled: false` in settings.

## Auto Dream — verification of trigger cadence

**Community source** [[claude-code-memory-2-autodream]] (Nate Herk) describes a third layer:
an "Auto Dream" background sub-agent that periodically consolidates memory files "like sleep,"
runnable via `/dream`, with a cadence of "every N hours or N sessions." A follow-up check
(2026-07-27) found multiple independent third-party sources converging on a specific threshold —
Auto Dream fires when **both** ≥24 hours have passed since the last consolidation **and** ≥5 new
sessions have accumulated — described as reading recent transcripts, merging facts into `MEMORY.md`,
deleting contradicted notes, and converting relative dates to absolute. This is *highly plausible
but still unverified* against official docs (the official What's New page publishes no such numbers).

**What official docs say (checked 2026-07-26):**
- Official Claude Code memory docs describe only CLAUDE.md files and Auto memory.
- No `/dream` command appears in official docs for Claude Code consumer.
- The `/memory` command opens the memory manager (file browser + auto memory toggle);
  **no dreaming toggle** appears there in official documentation.
- "Dreaming" in official Anthropic docs refers exclusively to the **Managed Agents API** 
  feature (research preview, requires `dreaming-2026-04-21` beta header) — see [[agent-dreaming]].
- A third-party GitHub project ("dream-skill") explicitly describes itself as replicating
  "Anthropic's **unreleased** auto-dream feature," suggesting `/dream` for Claude Code
  consumer was not released (as of 2026-07-26).

**Verdict:** Auto Dream trigger cadence remains **unverified** against official sources.
The consolidation concept is real at the platform level ([[agent-dreaming]]) but appears
either unreleased or deprecated for Claude Code consumer. The `/dream` command is not
confirmed in official Claude Code documentation. Treat the community description as
aspirational/experimental.

Related: [[claude-code]], [[ai-executive-assistant]], [[llm-wiki-pattern]] (this vault's own
memory design echoes the "index, not a dump" idea). Platform-level analogue: [[agent-memory]]
and [[agent-dreaming]] (Code with Claude batch).
