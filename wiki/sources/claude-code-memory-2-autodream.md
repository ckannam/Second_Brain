---
source: youtube
channel: "Nate Herk"
url: "https://www.youtube.com/watch?v=LrgfmZkl3nc"
title: "Claude Code Just Dropped Memory 2.0"
created: 2026-07-24
---
# Claude Code Just Dropped Memory 2.0 ("Auto Dream")

**Thesis:** An experimental Claude Code feature, **Auto Dream**, runs a background sub-agent that periodically **consolidates, prunes, and reorganizes** your memory files — likened to how humans consolidate memory during sleep.

## Key points
- Three memory layers: (1) normal session work, (2) **auto-memory** (records project decisions/patterns into `memory.md`, injected at session start), (3) **auto-dream** (background cleanup that merges/prunes/compacts memory files).
- Turn on via `/memory` → toggle "auto dream on"; run manually with `/dream` or natural language ("run your auto dream").
- A dream reviews recent sessions (e.g. 13 vs 285) and rewrites only **memory `.md` files** — never code. Runs ~8–10 min.
- Likely triggers: every N hours or every N sessions (unconfirmed, from community/Reddit discussion — **speculative**).
- Benefits: less repetition, less bloat, better recall, a periodic "checkpoint."
- Inferred dream prompt: "keep under a line limit, it's an index not a dump; link to memory files with one-line descriptions."

Tools/entities: [[claude-code]], [[anthropic]], [[claude-code-memory]]. Note: feature is experimental/rolling out; some details inferred.

**Raw clip:** [[Claude Code Just Dropped Memory 2.0]]
