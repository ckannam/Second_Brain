---
type: concept
---

# Second Brain system (wiki + journal + CRM)

[[matt-wolfe]]'s extension of the [[llm-wiki-pattern]]
([[build-an-ai-second-brain-matt-wolfe]]). Keeps Karpathy's wiki at the center and adds
two interacting layers so the knowledge base becomes something you *act through*, not
just store in.

## Three pillars

1. **Wiki / knowledge base** — the [[llm-wiki-pattern]] core: web clips summarized and
   cross-linked via [[ingest-query-lint|ingest]]. Captured with the
   [[obsidian-web-clipper]].
2. **CRM** — one markdown page per person (how/where you met, conversations, contact
   details) with an alphabetical index. Query it later ("where did I meet X?").
3. **Journal** — grounded journaling. Journal responses pull from the wiki, past journal
   entries, and the CRM, giving advice tailored to what you've actually saved rather than
   generic chatbot output. Also surfaces recurring patterns across entries.

## Operational refinements

- Move processed sources to `raw/processed/` so `raw/` shows only the unprocessed queue.
- Add the YouTube `channel:` to front matter (the clipper omits it).
- Cross-link every generated page back to its source page to avoid orphans.
- Automate: [[codex]] hourly automation processes new files and pushes to a private
  GitHub backup.

> This vault currently implements the **wiki pillar only**. Journal and CRM are documented
> here as a possible expansion, not yet built.

## Related framings (July 2026 sources)

- **[[ai-second-brain-levels]]** — a complementary "5 levels" model of a [[claude-code]]
  second brain (from [[every-level-claude-second-brain]]): find the *lowest* level that
  solves your pain, from a [[claude-md-router|`CLAUDE.md` router]] up to an always-on
  autonomous system.
- **[[ai-executive-assistant]]** — turning the second brain into something proactive you
  act *through* ([[turn-claude-code-executive-assistant]], [[i-turned-clawdbot-personal-assistant]]).
- **[[obsidian-vault-deep-dive-emai]]** — an alternative Obsidian second-brain build using
  local agents, Dataview dashboards, and embedded web viewers.

## Act-through layers actually built here

Beyond the wiki (things to *know*), this vault adds a persistent **action-items board** at
`tasks/index.md` — things to *do*, maintained by the agent across sessions per the
**Action Items** operation in the schema. It's the fourth pillar alongside wiki / CRM /
journal, and the one most directly about *acting through* the second brain rather than
storing in it. Lint findings and journal follow-ups flow into it.
