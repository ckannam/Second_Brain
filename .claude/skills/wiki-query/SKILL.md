---
name: wiki-query
description: >
  Use when Cole asks a question meant to be answered from his Second Brain vault/wiki —
  "what does the wiki say about X", "ask the vault", "what do I know about X", "what's in
  my notes on X", "according to my notes", "what should I do about X", or any question
  whose answer lives in wiki pages, CRM, tasks, journal, or life-area buckets rather than
  general knowledge. Skill files the synthesized answer back into the vault automatically.
  Also runs on the /wiki-query command.
---

# Wiki Query

## Overview

The executable form of the **Query** operation defined in `AGENTS.md` (vault root).
`AGENTS.md` is the single source of truth for the vault's rules; this skill adds only the
*trigger* and a sharpened *retrieval procedure*. **Do not restate `AGENTS.md`'s rules here
— read it if unsure, and if anything conflicts, `AGENTS.md` wins.**

**Core principle:** the link graph is the retrieval engine. Answer *only* from what's in the
vault (plus clearly-marked synthesis), cite it, and file the answer back so exploration
compounds instead of vanishing into chat.

## Procedure

1. **Classify the request.** Is this a real question needing synthesis, or a pure
   navigational lookup ("which page is X on?")? Navigational → answer directly and **skip
   the file-back step** (step 6). Everything else runs the full loop.

2. **Index-first.** Read `index.md` and pick candidate pages from its one-line summaries.
   Also read the matching index when the question is shaped that way:
   - contacts / people → `crm/index.md`
   - "what should I do / what's open" → `tasks/index.md`
   - a life area (Duke, Uship, JHTV, Job Search, Personal, Claude Mastery) → that
     `buckets/<Area>.md` as an entry point.

3. **Traverse the graph.** Read the candidate pages, then follow their `[[wikilinks]]`
   outward one hop to gather the connected neighborhood — go a further hop when the first
   pass is thin. Read `wiki/overview.md` for cross-cutting / synthesis questions. The links
   between pages are where the answer usually completes.

4. **Reconcile freshness.** Sources are point-in-time snapshots. Honor `superseded` markers
   and freshness notes (e.g. a source citing `opus-4-7` when the current flagship is
   `opus-4-8`), flag contradictions between pages, and never treat a source as live truth.

5. **Answer with citations.** Synthesize a direct answer. Cite the `[[wiki-pages]]` you
   used and the raw source(s) behind key claims so the human can trace them. If the vault's
   evidence is thin or absent, say so plainly — **never invent facts**; mark any inference
   as inference.

6. **File the answer back** (skip only for navigational lookups — see step 1). Follow
   `AGENTS.md`'s Query rules: new page in `wiki/` *or* update an existing one per the
   new-page test, with `type` + `created` frontmatter; cross-link to the pages and sources
   it drew from; add a link from the relevant `buckets/` MOC; update `index.md`; append an
   entry to `log.md`.

7. **Report.** Give the answer in chat and note where it was filed (page name + that
   `index.md`/`log.md` were updated).

## Guardrails

- **Never invent facts.** Everything traces to a raw source or is clearly marked synthesis.
- **Links > pages.** Prefer enriching/connecting existing pages over spinning up thin new
  ones; apply `AGENTS.md`'s new-page test before creating.
- **Snapshots age.** Reconcile against what's currently known; mark superseded claims.
- **Don't duplicate.** Before creating a page, check the graph doesn't already own the topic
  (and watch for basename collisions across folders — they break links).

## Common Mistakes

- Answering from general knowledge instead of the vault, or without citations.
- Skipping the file-back step on a real query (only navigational lookups skip it).
- Reading only the candidate pages and not traversing their links — the neighborhood is
  where the answer completes.
- For life-area questions (Duke, Uship, JHTV, Job Search, Personal, Claude Mastery), not
  opening the relevant `buckets/<Area>.md` first — that's the hub and entry point.
- Re-copying `AGENTS.md`'s rules into an answer or into this skill instead of following them.
