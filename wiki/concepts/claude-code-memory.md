# Claude Code Memory (Auto-Memory + Auto Dream)

Three layers ([[claude-code-memory-2-autodream]]):
1. **Session work** — normal coding/chat.
2. **Auto-memory** — records project decisions/patterns into `memory.md`, injected at session start. Launched February 2026.
3. **Auto Dream** — a background sub-agent that periodically **consolidates, prunes, and compacts** memory files between sessions ("like human sleep"). Phased rollout began late March 2026. Toggle via `/memory`; trigger manually with `/dream`.

**Benefits:** less repetition, less bloat, better recall, periodic checkpoints.

**Trigger cadence** (community-observed; not explicitly documented in official Anthropic release notes as of 2026-07-27): Auto Dream fires when **both** conditions are met — ≥24 hours since the last consolidation **and** ≥5 new sessions accumulated. One long session over two days won't trigger it (not enough sessions); ten quick sessions in two hours won't either (not enough time). Multiple independent third-party sources report this same threshold; treat as *highly plausible but unverified against official Anthropic docs*. (Checked: official [What's New](https://code.claude.com/docs/en/whats-new) page does not publish the specific numbers.)

**What Auto Dream does:** reads recent transcripts → merges new facts into `MEMORY.md` and topic files → deletes contradicted notes → converts relative dates to absolute ones ("yesterday" → "2026-03-15") → trims the index to ≤200 lines. Touches only memory `.md` files, never code.

Related: [[claude-code]], [[ai-executive-assistant]], [[llm-wiki-pattern]] (this vault's own memory design echoes the "index, not a dump" dream prompt). See also the Anthropic first-party framing in [[agent-memory]] and [[agent-dreaming]] (Code with Claude batch) — the same sleep/consolidation idea at the platform level.
