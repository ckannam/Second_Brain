---
type: entity
category: tool
---

# qmd

Local, on-device search engine for markdown files with hybrid BM25/vector search and LLM
re-ranking (https://github.com/tobi/qmd). Offered by [[andrej-karpathy]] as optional
tooling for the [[llm-wiki-pattern]] once a wiki outgrows the `index.md`-only approach.

Has both a CLI (the agent can shell out to it) and an MCP server (native tool use). **Not
in use here yet** — at this vault's current size the index file is enough. Add it if
search over the wiki becomes necessary.

Source: [[llm-wiki-karpathy]].
