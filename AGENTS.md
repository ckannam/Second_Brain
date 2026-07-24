# Second Brain — LLM Wiki Schema

This vault is an **LLM Wiki** in the sense of Karpathy's pattern
(https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). You (the LLM)
incrementally build and maintain a persistent, interlinked wiki of markdown files from
raw sources. The human curates sources, directs analysis, and asks questions. You do the
summarizing, cross-referencing, filing, and bookkeeping.

The human reads the vault in Obsidian; you write it. Obsidian is the IDE, you are the
programmer, the wiki is the codebase.

> **This file is the single source of truth for how the vault works.** It applies to any
> agent — Codex (`AGENTS.md`) or Claude Code (`CLAUDE.md` points here). Co-evolve it with
> the human as you learn what works.

## Layout

```
raw/            immutable source documents
  assets/       inbox — new data lands here, unprocessed
  Processed/    sources move here after ingest
wiki/           LLM-generated wiki pages (entities/, concepts/, sources/, overview.md)
crm/            one file per person + index.md
journal/        grounded journal entries (see Journal below)
tasks/          action items you maintain across sessions + index.md (see Action Items below)
buckets/        life-area Maps of Content + index.md (see Buckets below)
index.md        content catalog of the wiki (vault root)
log.md          append-only chronological record (vault root)
AGENTS.md       this schema
CLAUDE.md       pointer to this schema
```

## The layers

**`raw/`** — Source documents (clipped articles, PDFs, notes, data, images). The source of
truth. **Never edit a source's content.** Files move through a two-stage lifecycle
(relocating a file is bookkeeping, not modifying it):
- **`raw/assets/`** — Inbox. New data lands here first (point the Obsidian Web Clipper's
  note location here). Anything in `assets/` is unprocessed and waiting to be ingested.
- **`raw/Processed/`** — After a source is fully ingested, move the source file here so
  `assets/` only ever shows the unprocessed queue.

**`wiki/`** — LLM-generated, LLM-owned markdown pages. Summaries, entity pages, concept
pages, comparisons, an overview, a synthesis. You create and maintain every page here,
keeping cross-references and content consistent as new sources arrive.

## Buckets (life-area Maps of Content)

`buckets/` holds one **MOC (Map of Content)** per major area of life — currently **Duke,
Uship, JHTV, Job Search, Personal, Claude Mastery** — plus `buckets/index.md`. A bucket is a
**hub note that links to** relevant pages across `wiki/`, `crm/`, `tasks/`, and `journal/`.
It never holds or moves those pages.

This is deliberately a **re-cuttable overlay, not a filing system.** The bucket set — and
the whole premise of organizing by life-area — is expected to change; because buckets only
*link*, they can be renamed, split, merged, or replaced at any time without touching a
single underlying page. **Never** relocate wiki/CRM pages into bucket folders, and never
build logic that assumes today's buckets are permanent.

When you create or substantially update a page, add a link to it from the relevant
bucket(s). When answering a query scoped to a life area, the bucket is a good entry point.

## Page conventions

- One markdown file per page in `wiki/`. Filenames in `kebab-case`.
- **Entity pages**: a person, org, company, tool, place — anything concrete.
- **Concept pages**: an idea, topic, theme, or question.
- **Source summary pages**: one per ingested item in `raw/`.
- Link between pages with Obsidian wikilinks: `[[page-name]]`. Link liberally — the
  connections are as valuable as the pages. A link to a page that doesn't exist yet is
  fine; it marks a page worth creating.
- Cite raw sources when a claim comes from one, so the human can trace it back.
- Keep pages atomic and focused — split a page when it starts covering two things.
- Frontmatter is optional; add it only if the human wants Dataview queries later.

## Source-type rules

**YouTube videos** (clipped into `raw/assets/` with the Obsidian Web Clipper): when
ingesting, always pull the **channel name** from the source and add it to the source
summary page's frontmatter as a `channel:` field. The Web Clipper usually captures it
(e.g. in the `author`, `channel`, or byline metadata); if it isn't in the clipped
markdown, fetch it from the video URL. Example frontmatter:

```yaml
---
source: youtube
channel: "<YouTube channel name>"
url: "<video url>"
---
```

## Two special files

**`index.md`** (vault root) — Content catalog. Every wiki page listed with a link and a
one-line summary, organized by category (entities, concepts, sources, …). Update it on
every ingest. When answering a query, read the index first to find relevant pages, then
drill in.

**`log.md`** (vault root) — Append-only chronological record. One entry per ingest, query,
lint, or CRM update. Start every entry with a consistent prefix so it's greppable:
`## [YYYY-MM-DD] ingest | Source Title`. Never rewrite past entries; only append.

## Operations

**Ingest.** The human drops a source into `raw/assets/` (or provides a URL/path) and asks
you to process it.

> **The point of an ingest is connection, not accumulation.** New knowledge is the input;
> the *value you add* is weaving it into what already exists — enriching existing pages and
> drawing new links. Your **first move is always to enrich what's already there**; creating a
> new page is the second move, not a rare one.
>
> **Expect the mix to shift with maturity.** While the wiki is young (it is now), most
> ingests are mostly-new content and creating pages is normal and expected — don't suppress
> it. As coverage fills in, a rising share of each ingest becomes pure enrichment and fewer
> new pages are needed. That downward trend is a sign of a maturing graph, not a target to
> force. Optimize for how much better the *existing* graph is afterward — enrichment plus the
> new pages a source genuinely warrants.

1. **Read `index.md` first** — know what already exists before you write anything, so you
   enrich rather than duplicate. Then read the source.
2. Discuss the key takeaways with the human.
3. Write a source summary page in `wiki/sources/`.
4. **Connect before you create.** Walk the entities/concepts the source touches (a single
   source may touch 10–15 pages) and, for each, **update the existing page** — fold in the
   new insight, add reciprocal links (if page A now links B, B's *prose* should acknowledge
   A — don't rely on backlinks alone), and **flag contradictions / supersessions** instead
   of silently overwriting (e.g. mark an old model claim as superseded).
   - **New-page test** — create a page when **(a)** no existing page owns the topic **and**
     **(b)** it's a distinct, reusable thing (an entity/concept you'd want to link to again),
     not a passing detail. A single strong source is enough — reuse across sources or hub
     status makes it *obvious*, but isn't required. When it fails the test, fold the idea into
     the nearest existing page or the source summary instead. Before creating, check for a
     same-named page in another folder (basename collisions break links). Erring toward a new
     page for a genuinely distinct topic is fine; the thing to avoid is duplicating a topic an
     existing page already owns, or spinning up a thin page for a one-off detail.
5. Update `index.md`.
6. Append an entry to `log.md`.
7. **Connection pass (do not skip).** Before moving the source, re-read the pages you
   touched: confirm links are reciprocated, no near-duplicate page was created, and stub
   links you spawned are worth their debt. This pass is where the graph actually gets
   smarter.
8. **Move the source file from `raw/assets/` to `raw/Processed/`** so the inbox only shows
   unprocessed items. (Move only — never alter the file's content.)

Prefer ingesting one source at a time and staying in dialogue unless told to batch. **When
batching,** still connect as you go, and run one consolidated connection pass (step 7) plus a
[[#Lint]] sweep across all touched pages at the end — batches are where sprawl and missed
back-links accumulate fastest.

**Query.** The human asks a question against the wiki.
1. Read `index.md`, then read the relevant pages.
2. Synthesize an answer with citations back to wiki pages and raw sources.
3. **Always file the answer back into the wiki** — automatically, without asking. Every
   query answer becomes a new wiki page (or an update to an existing one) so the
   exploration compounds instead of disappearing into chat. Cross-link it to the pages
   and sources it drew from, add it to `index.md`, and give it `type` + `created`
   frontmatter. Only skip filing if the "answer" is purely a navigational lookup with no
   synthesis (e.g. "which page is X on?"); when in doubt, file it.
4. Log the query in `log.md`.

**Lint.** The human asks you to health-check the wiki. Look for:
- contradictions between pages
- stale claims superseded by newer sources
- orphan pages with no inbound links
- important concepts mentioned but lacking their own page
- missing cross-references
- data gaps worth filling with a web search or new source
Report findings and suggested fixes, new questions to investigate, and sources to seek.
Log the lint pass in `log.md`.

**CRM.** When the human says they're giving you information for the CRM, either add the
person or update their existing record.
1. Identify the person. Each contact is **one file in `crm/`, named for the person**
   (e.g. `crm/Matthew Berman.md`).
2. Create or update that contact record with whatever details the human gives: name,
   contact details, where/how you met, relationship context, and anything known about
   them. Merge new details into the existing record rather than overwriting.
3. Update `crm/index.md` — the same style as `index.md`: the names of everyone in the
   CRM listed **alphabetically**, each with a short bio of the information on file. This
   is what lets the human ask questions about contacts.
4. Cross-link where useful — a contact may connect to wiki entities, concepts, or
   sources, and vice versa.
5. Log the CRM update in `log.md`.

**Journal.** When the human starts a chat with **`Journal:`**, treat the whole exchange as
a journal entry.
1. Save the text of that chat **and the subsequent conversation** as a new markdown file in
   `journal/`. The entire conversation goes into the file.
2. Decide a short title based on the entry's contents. The filename is the **date + title**
   (e.g. `journal/2026-07-23 - video-count-anxiety.md`).
3. Update `journal/index.md` (same style as `index.md`): add the date and title, linked to
   the entry.
4. Append the journal entry's title and a short summary to `log.md`.
5. **Ground your response in the wiki.** Just as a Query reads `index.md` and answers from
   wiki content, respond to the journal entry using what's available in the wiki, **plus
   past journal entries and the CRM**, plus your own LLM knowledge. Provide helpful advice,
   insights, guidance, tactics, and ideas — tailored to what the human has actually saved,
   not a blank-slate answer.

**Action Items.** A running to-do list you maintain **across sessions** in `tasks/index.md`
— the vault's memory of things to *do* (vs. the wiki, which is things to *know*). **Read it
at the start of a work session** and whenever the human asks "what's open?" / "what should
I do?".
1. **Capture.** When an action item arises — the human says "remember to X" / "add a task",
   or a Lint pass, Query, or Journal entry surfaces a follow-up — append it under **Open**
   in `tasks/index.md` as an Obsidian checkbox:
   `- [ ] <action> — <one-line context> [[related-page]] (added YYYY-MM-DD)`. Cross-link the
   wiki pages, sources, or CRM people it relates to. Group under a short subheading.
2. **Complete.** When done, flip `- [ ]` to `- [x]`, append `(done YYYY-MM-DD)`, and move it
   to the **Done** section (newest at top). Never delete history.
3. **Ground.** Because items link back into the wiki/CRM, "what should I do about X?" can be
   answered from both the knowledge and the task board. Lint findings are natural task
   sources — file them here, not just in `log.md`.
4. Append a one-line entry to `log.md` when you add or complete a batch of items.

## Principles

- The human owns sourcing, direction, and questions. You own the bookkeeping.
- **Links > pages.** The value is in the connections; a page nothing links to is nearly
  worthless. On every ingest the **first move is to enrich what already exists** and make
  links reciprocal — but a well-linked new page for a genuinely distinct topic *is* enrichment.
  Early on (now), new pages will dominate; as coverage grows the balance tips toward pure
  enrichment. Success is a denser, more current graph — not page count in either direction.
- Never invent facts. Everything in the wiki traces to a raw source or is clearly marked
  as synthesis/inference.
- Ingested material is a **snapshot** — model names, capabilities, and workflows age fast.
  Reconcile against what's currently known and mark superseded claims rather than trusting
  the source as live truth.
- Keep the wiki current, consistent, and cross-referenced — that maintenance is the whole
  point of the pattern.
