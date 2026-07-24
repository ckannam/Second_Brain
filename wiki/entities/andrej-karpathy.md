---
type: entity
category: person
---

# Andrej Karpathy

Author of the [[llm-wiki-pattern]], published as a gist and ingested here as
[[llm-wiki-karpathy]]. Originated the idea of having an LLM incrementally build and
maintain a persistent wiki over immutable raw sources, with [[obsidian]] as the reading
front end.

His framing — "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase"
— defines how this vault is meant to be used. Credited by [[matt-wolfe]] as the origin of
the [[second-brain-system]] build.

Mentioned: [[ingest-query-lint]] operations, the Memex lineage, [[qmd]] as optional
search tooling. His trajectory doubles as a roadmap for this vault — see
[[extending-the-llm-wiki]].

## More Karpathy sources (July 2026)

- **[[andrej-karpathy-llm-wiki-obsidian]]** — a [[nate-herk]] walkthrough of building
  Karpathy's LLM Wiki in [[obsidian]] + [[claude-code]] (the exact pattern of this vault),
  incl. [[llm-wiki-vs-rag|LLM Wiki vs RAG]].
- **[[skill-issue-karpathy-sarah-guo]]** — interview with [[sarah-guo]]: he now delegates
  nearly all coding to agents ("haven't typed a line of code since December" —
  [[natural-language-coding]], [[vibecoding]]), praises [[openclaw]]'s memory system, and
  describes **AutoResearch** (agents closing the AI-research loop autonomously).

## AutoResearch & Agent Hub (shipped March 2026)

The "loopy era" idea from the interview became **runnable open-source code**: [[autoresearch]]
(source [[autoresearch-repo]]) — an agent that edits one file, trains a small [[nanochat]] GPT
for 5 minutes, keeps or `git reset`s on the `val_bpb` metric, and **loops forever** ("NEVER
STOP"). It went viral (~25k stars in days; endorsed by Toby Lütke / Shopify and Stripe), and
its coverage arrived here as a batch of creator explainers ([[david-andre]], [[nick-saraev]],
[[greg-isenberg]]). His stated end-state is a **SETI@home for AI research** — millions of
distributed agents ("early stages of the singularity"). He followed it with **[[agent-hub]]**
("GitHub for agents"). These are the concrete next rungs of the roadmap in
[[extending-the-llm-wiki]].
