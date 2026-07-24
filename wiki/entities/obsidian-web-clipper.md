---
type: entity
category: tool
---

# Obsidian Web Clipper

Browser extension that converts web pages to markdown and saves them into an [[obsidian]]
vault. Configured here to drop clips into the `raw/assets/` inbox with front-matter properties
(title, source URL, created date, WebClip tag).

Notably **auto-pulls YouTube transcripts** into the clipped note, making it easy to
ingest videos. Its one gap: it does **not** capture the YouTube **channel name** — which
is why this vault's `CLAUDE.md` has a rule to add `channel:` to front matter during
[[ingest-query-lint|ingest]].

Sources: [[llm-wiki-karpathy]], [[build-an-ai-second-brain-matt-wolfe]].
