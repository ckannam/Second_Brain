# Claude Code Memory (Auto-Memory + Auto Dream)

Three layers ([[claude-code-memory-2-autodream]]):
1. **Session work** — normal coding/chat.
2. **Auto-memory** — records project decisions/patterns into `memory.md`, injected at session start.
3. **Auto Dream** — an experimental background sub-agent that periodically **consolidates, prunes, and compacts** memory files, "like human sleep." Toggle via `/memory`; run with `/dream`.

**Benefits:** less repetition, less bloat, better recall, periodic checkpoints. **Triggers** (unconfirmed): every N hours or N sessions. Touches only memory `.md` files, never code. Some details are inferred/experimental.

Related: [[claude-code]], [[ai-executive-assistant]], [[llm-wiki-pattern]] (this vault's own memory design echoes the "index, not a dump" dream prompt). See also the Anthropic first-party framing in [[agent-memory]] and [[agent-dreaming]] (Code with Claude batch) — the same sleep/consolidation idea at the platform level.
