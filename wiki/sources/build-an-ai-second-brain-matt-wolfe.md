---
type: source
source: youtube
channel: "Matt Wolfe"
url: "https://www.youtube.com/watch?v=yke4fLQUsh4"
ingested: 2026-07-23
---

# Source: Build An AI Second Brain Knowledge Base (Step-By-Step)

YouTube video by [[matt-wolfe]] (channel: **Matt Wolfe**).

## Summary

A step-by-step build of a personal [[second-brain-system]] on top of Karpathy's
[[llm-wiki-pattern]]. Wolfe credits [[andrej-karpathy]] for the core wiki idea and adds
two layers of his own: a **journal** and a **CRM**.

Three pillars:
1. **Wiki / knowledge base** — everything clipped from the web (YouTube transcripts,
   articles, tweets, podcasts) via the [[obsidian-web-clipper]], summarized and
   cross-linked into entity/concept pages.
2. **CRM** — one page per person (how/where you met, conversations, contact details),
   with an alphabetical index.
3. **Journal** — grounded journaling: responses pull from the wiki, past journal
   entries, and the CRM rather than answering from a blank slate.

Build details:
- Built in [[codex]] against the [[obsidian]] vault folder; prompt was literally "build
  out architecture based on Karpathy's LLM wiki." First pass over-produced 51 files;
  pruned to the minimal game plan (raw/, wiki/, `AGENTS.md`, `index.md`, `log.md`).
- Refinements shown: move processed sources to `raw/processed/`, pull the YouTube
  **channel name** into front matter, cross-link generated pages back to their source to
  avoid orphans.
- Automation: a Codex hourly automation processes new `raw/` files and pushes to a
  private GitHub repo as backup.

## Notes

This is a meta-source — it describes building the very kind of system this vault is. The
channel-name front-matter rule now in this vault's `CLAUDE.md` came from this video.

**Raw clip:** [[Build An AI Second Brain Knowledge Base (Step-By-Step)]]
