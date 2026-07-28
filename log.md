# Log

Append-only chronological record of ingests, queries, and lint passes. Newest entries
at the bottom. Each entry starts with `## [YYYY-MM-DD] <op> | <title>` so it stays
greppable: `grep "^## \[" log.md | tail -5`.

<!-- Append entries below this line. -->

## [2026-07-23] ingest | LLM Wiki (Karpathy gist)
Ingested `raw/llm-wiki.md`. Created source page [[llm-wiki-karpathy]]; entities
[[andrej-karpathy]], [[obsidian]], [[qmd]]; concepts [[llm-wiki-pattern]],
[[ingest-query-lint]]. Established [[overview]].

## [2026-07-23] ingest | Build An AI Second Brain (Matt Wolfe, YouTube)
Ingested `raw/Build An AI Second Brain Knowledge Base (Step-By-Step).md`. Channel: Matt
Wolfe (added to source front matter). Created source page
[[build-an-ai-second-brain-matt-wolfe]]; entities [[matt-wolfe]], [[obsidian-web-clipper]],
[[codex]]; concept [[second-brain-system]]. Cross-linked to [[llm-wiki-pattern]].

## [2026-07-23] ingest | Discipline without willpower (Erin Meryl Study, YouTube)
Ingested `raw/how to trick your brain into becoming so disciplined...`. Channel: Erin
Meryl Study (added to source front matter). Created source page
[[discipline-without-willpower-erin-meryl]]; entity [[erin-meryl]]; concepts
[[discipline-without-willpower]], [[temporal-discounting]], [[temptation-bundling]],
[[cue-routine-reward-loop]], [[identity-led-goals]], [[environment-design]].

## [2026-07-23] query | How do I get more discipline?
Answered from the discipline cluster. Filed the answer back as playbook page
[[how-to-build-discipline]] and linked it in [[index]].

## [2026-07-23] schema | raw lifecycle: assets inbox -> Processed
Added a two-stage raw lifecycle to `CLAUDE.md`: new data lands in `raw/assets/`, and
ingest now moves each source to `raw/Processed/` as its final step. Moved the three
already-processed sources into `raw/Processed/`.

## [2026-07-23] schema | AGENTS.md is now canonical; index/log at root; CRM added
Consolidated the full schema into `AGENTS.md` (single source of truth); `CLAUDE.md` is now
a pointer to it. Updated all `index.md`/`log.md` references to the vault root (they were
moved out of `wiki/`). Added a **CRM** operation and created `crm/index.md`. Noted
`journal/` as scaffolded (rules TBD). Verified the schema against Karpathy's gist.

## [2026-07-23] schema | Journal operation defined
Added the full **Journal** operation to `AGENTS.md`: a `Journal:` chat is saved as a
`date - title` file in `journal/`, indexed, logged, and answered grounded in the wiki +
past journal entries + CRM. Created `journal/index.md`.

## [2026-07-24] ingest | Batch: 43 YouTube sources (Claude Code / agentic / second-brain wave)
Bulk-ingested 43 clipped YouTube sources dropped into `raw/` (42 by Nate Herk, 1 by Easy
Machine AI, 1 by Sarah Guo/No Priors) — the pile grew from 18 to 43 during processing as
more were clipped in; a final sweep caught the last straggler
([[master-claude-code-36min-beginner]]). Wrote 42 source summary pages under `wiki/sources/`
(added `channel:` frontmatter to each per schema). Large sources handled by structural
pass: the ~830KB [[build-sell-claude-code-course]] summarized from its chapter outline, not
a full read; several near-duplicate beginner agentic-workflow videos cross-linked rather
than expanded.

Created entity hubs: [[claude-code]], [[anthropic]], [[nate-herk]], [[clawdbot]],
[[openclaw]], [[n8n]], [[firecrawl]], [[paperclip]]. Created concept hubs:
[[agentic-workflows]], [[agentic-vs-deterministic]], [[selling-ai-automations]],
[[ai-second-brain-levels]], [[ai-executive-assistant]], [[self-healing-workflows]],
[[n8n-vs-claude-code]], [[claude-code-skills]], [[claude-code-memory]],
[[claude-code-scheduled-tasks]], [[rag]], [[llm-wiki-vs-rag]], [[json-prompting]],
[[vibecoding]]. Updated [[codex]], [[andrej-karpathy]], [[second-brain-system]] to link the
new cluster. Rebuilt [[index]].

Notes / open items: many wikilinks intentionally point to not-yet-created stub pages
(e.g. [[claude-code-subagents]], [[claude-code-computer-use]], [[gemini-3-1-flash-live]],
[[nano-banana-2]], [[opus-4-6]]) — marked for future creation. "Clawdbot"/"OpenClaw"
spellings and exact product identities are from transcripts and remain slightly uncertain.
Auto Dream trigger cadence is community-inferred, not officially documented. Moved all 42
sources from `raw/` to `raw/Processed/`.

## [2026-07-24] lint | Post-batch health check + stub fill
Fleshed out ~50 stub pages (all wikilinks with 2+ inbound refs, plus named people). Vault
now 136 wiki pages. **Link integrity: 0 orphans**, every page inbound-linked. 7 stubs left
intentionally (minor/incidental: [[vs-code]], [[hostinger]], [[clickup]], [[model-speciation]],
[[agentic-automation-patterns]]; `[[page]]` is an inline-code example in [[obsidian]], not a
real link).

Findings for the human:
- **Workflow drift (action needed):** schema (`AGENTS.md`) says the Obsidian Web Clipper
  should point at `raw/assets/`, but all 43 clips landed directly in `raw/`. Either repoint
  the clipper to `raw/assets/` or update the schema to match reality.
- **Single-source risk:** ~42/44 sources are one creator (Nate Herk). Feature claims about
  Claude Code (scheduled tasks, Auto Dream, skills, Auto Mode) are a YouTuber's read, not
  primary docs. Recommend ingesting official Anthropic Claude Code docs to ground them.
- **Claims to verify (data gaps):** Auto Dream trigger cadence (community-inferred);
  "Clawdbot"/"OpenClaw"/"Open Claude" exact identities & spellings; Opus 4.6 vs GPT 5.4
  benchmark numbers (not captured); deeper notes on any [[build-sell-claude-code-course]]
  chapter (summarized from outline only).
- **Overlap (not errors):** 4 beginner agentic-workflow videos and 3 n8n takes overlap
  heavily; consolidated via the [[agentic-workflows]] and [[n8n-vs-claude-code]] concept
  pages rather than merging source pages (schema keeps sources atomic).
- **Not yet built:** Journal & CRM pillars (documented in [[second-brain-system]] as future).

## [2026-07-24] schema | Added Action Items (tasks/) pillar
Created `tasks/index.md` — a persistent action-items board (things to *do*), parallel to
`crm/` and `journal/`. Added `tasks/` to the Layout in `AGENTS.md` and defined a new
**Action Items** operation (capture / complete / ground / log), so future sessions read and
maintain it across sessions. Seeded it with the 7 open follow-ups from the 2026-07-24 lint
pass. Wired it into `index.md`, `overview.md`, and [[second-brain-system]] (noted as the
fourth act-through pillar).

## [2026-07-24] tasks | Added vault-improvement action items (buckets, skills, CRM, prompts)
Clarified the board's scope in `tasks/index.md`: it tracks **vault/second-brain
improvements only**, not personal to-dos (separate board later). Added items: create the
6 **life buckets** (Duke / Uship / JHTV / Job Search / Personal / Claude Mastery) — recommend
MOC index notes as the mechanism; a **Claude Mastery** cluster (train skills, token max,
skill max, agent max, improve + general skills); a **Personal** cluster (build the CRM, give
the agent Instagram/iMessage access to learn contacts); and storing the session-opening
prompts. Created reference note [[session-opening-prompts]] (has `--dangerously-skip-permissions`;
iMessage channel command still TBD) and cataloged it in [[index]].

## [2026-07-24] schema | Added Buckets (life-area MOCs) + prompt max, stored session prompts
Created `buckets/` with 6 life-area Maps of Content ([[Duke]], [[Uship]], [[JHTV]],
[[Job Search]], [[Personal]], [[Claude Mastery]]) + `buckets/index.md`. Buckets are a
**re-cuttable link overlay** (never move underlying pages; the set can change anytime) —
added a **Buckets** section to `AGENTS.md` stating this, plus `buckets/` in the Layout.
Claude Mastery and Personal are populated from existing wiki content; the other four are
scaffolds. Wired into [[index]] and [[overview]].

Also: added **prompt max** to the Claude Mastery skills track and refined its goal (best
Claude skills to maintain/maximize the second brain AND build faster). Completed and moved
to Done: creating the buckets, and storing both session-opening prompts in
[[session-opening-prompts]] (filled in the iMessage command
`--channels plugin:imessage@claude-plugins-official`).

## [2026-07-24] ingest | Batch: 30 Anthropic "Code with Claude" sessions
Bulk-ingested 31 first-party Anthropic YouTube clips (channel: Anthropic) dropped into
`raw/` root — the July 2026 **Code with Claude** event, "The Briefing" virtual events, and
"The Problem Solvers" — into **30 source pages** (two identical "Designing with Claude" clips
deduped into one). Processed in six thematic clusters: Managed Agents, AI-native org,
prompting/models, research/agent-design, industry verticals, and short blurbs. Added
`channel:` frontmatter per schema; long transcripts summarized structurally.

New entity hubs: [[claude-managed-agents]], [[claude-cowork]], [[claude-tag]],
[[claude-science]], [[claude-design]], [[elicit]], [[man-group]], [[omni]], [[lovable]],
[[genspark]]; people [[fiona-fung]], [[boris-cherny]], [[cat-wu]], [[tariq]], [[james-brady]],
[[kay-zhu]]; models [[opus-4-7]], [[opus-4-5]].

New concept hubs: [[brain-hands-decoupling]], [[outcome-oriented-agents]], [[agent-vaults]],
[[context-anxiety]], [[agent-memory]], [[agent-dreaming]], [[ai-native-engineering-org]],
[[html-over-markdown-specs]], [[bitter-lesson]], [[eval-driven-model-selection]],
[[cost-per-successful-outcome]], [[test-time-compute]], [[prompt-engineering-playbook]],
[[llm-as-judge]], [[evals-for-taste]], [[mechanism-over-output]], [[agentic-dsl]],
[[governed-skills-framework]], [[ai-for-science]], [[instructions-as-code]],
[[the-capability-curve]]. Updated [[anthropic]], [[claude-code]], [[mcp]], [[google]] to link
the new cluster. Rebuilt [[index]] with a second batch callout + a "Code with Claude event"
sources section.

Notes / open items: the batch predates the current Opus 4.8 flagship — talks cite **Opus 4.7**
as newest (transcripts sometimes render it "Opus 47"); flagged in [[opus-4-7]]. "Mythos" in
[[the-thinking-lever]] is a model name as heard in the transcript and may be a mishearing.
Several links intentionally point at not-yet-created stubs (e.g. [[frontend-design]],
[[multi-model-workflows]], [[autoresearch]] from the prior batch). "Dreaming" now has two
pages — consumer [[claude-code-memory|Auto Dream]] vs. platform [[agent-dreaming]] — cross-
linked to avoid confusion. Moved all 31 source files from `raw/` to `raw/Processed/`; the
`raw/assets/` inbox is empty.

## [2026-07-24] correction | Mythos + model-freshness note
Two corrections to the Code with Claude batch above. (1) **[[mythos|Mythos]]** is **not** a
transcription error as I speculated — per the vault maintainer it is a **real model, not
publicly released** (reportedly held back for cybersecurity reasons); recorded in [[mythos]],
marked unverified (outside source + my Jan-2026 cutoff). (2) **Freshness:** the batch cites
[[opus-4-7]] as newest, but the current flagship is **[[opus-4-8]]** (family also incl.
Sonnet 4.6, Haiku 4.5, Fable 5). Added [[opus-4-8]] and updated the Opus lineage so the
vault treats batch model claims as a point-in-time snapshot. General principle going forward:
ingested model/workflow details age fast — reconcile against current known models on read.

## [2026-07-24] lint | Reconciled the two parallel batches (creator videos + Code with Claude)
The parallel **Code with Claude** ingest (30 first-party Anthropic sessions) finished and
merged cleanly with my creator-video batch — shared hubs ([[claude-code]], [[anthropic]])
were enriched by both, not clobbered. Combined vault: **214 pages, 0 orphans**, 8 trivial
stubs left ([[vs-code]], [[hostinger]], [[clickup]], [[test-driven-development]],
[[frontend-design]], etc.). Folded the Anthropic batch into [[Claude Mastery]] (platform,
playbooks, agent memory, models, enterprise, people) and cross-linked future-of-work items
into [[Job Search]]. Added reverse cross-links between overlapping concepts:
[[claude-code-memory]]↔[[agent-memory]]/[[agent-dreaming]],
[[claude-code-skills]]↔[[evals-for-taste]]/[[governed-skills-framework]],
[[json-prompting]]→[[prompt-engineering-playbook]]. The four [[opus-4-6]] / opus-4-5/7/8
model pages are all valid versions (per the ingest-freshness rule) and already linked — left
as-is rather than force-merged.

## [2026-07-24] schema | Ingest = connection-first (co-evolution)
Reworked the **Ingest** operation in `AGENTS.md` to emphasize, top-down, that the point of an
ingest is **connection, not accumulation**: default to *updating* existing pages, gate
new-page creation behind a **new-page test** (no existing owner AND reused ≥2 sources or a
hub), require **reciprocal links** and contradiction/supersession flags, read `index.md`
first, and run a mandatory **connection pass** (+ lint sweep for batches) before moving a
source. Added two Principles: **"Links > pages"** and **"ingested material is a snapshot"
(reconcile against current knowledge).** Prompted by the 30-source Code with Claude batch
running create-heavy.

## [2026-07-24] schema | Refine new-page guidance for early-stage vault
Softened the connection-first wording in `AGENTS.md`: enriching existing pages is still the
first move, but **creating pages is normal, not rare** — a single strong source can warrant a
new page for a distinct/reusable topic (dropped the "≥2 sources" bar). Added the **maturity
curve**: while the wiki is young, most ingests are mostly-new content and new pages dominate;
the new-page share naturally falls as coverage fills in — a trend to expect, not force. The
one hard rule stays: don't duplicate a topic an existing page already owns, and don't spin up
thin pages for one-off details.

## [2026-07-24] query | Andrej Karpathy & how his insight is built into this design
Q: explain Karpathy and how his insight is built into this vault's design and can be built
further. Retrieved index-first → [[andrej-karpathy]], [[llm-wiki-pattern]],
[[skill-issue-karpathy-sarah-guo]], traversed links. Filed a new concept page
[[extending-the-llm-wiki]] (roadmap: three-layer structure + `wiki-query` skill already
embody the pattern; memory/parallel-agents/AutoResearch/qmd/self-healing as next rungs up the
[[ai-second-brain-levels]] ladder). Added reciprocal links from [[llm-wiki-pattern]] and
[[andrej-karpathy]]; listed in [[index]] and the [[Claude Mastery]] bucket. First query filed
via the new `.claude/skills/wiki-query` procedure (run by hand — skill registers next session).

## [2026-07-24] ingest | AutoResearch batch (Karpathy) — 8 sources
Ingested 8 sources (all landed directly in `raw/`, not `raw/assets/` — the known inbox-drift
task) on [[andrej-karpathy]]'s **[[autoresearch]]**: the GitHub repo itself (README +
`program.md` + `prepare.py` + two low-value UI clips) → source [[autoresearch-repo]], plus 3
YouTube explainers → [[autoresearch-tutorial-david-andre]], [[claude-code-karpathy-autoresearch-nick-saraev]],
[[autoresearch-broke-internet-greg-isenberg]].
- **Enriched (primary work):** rebuilt the one-line [[autoresearch]] stub into a full concept
  page (three-file architecture, the forever-loop, `val_bpb`/5-min budget, the three
  generalization conditions + failure modes, business applications). Reciprocal links added to
  [[andrej-karpathy]] (new AutoResearch/Agent Hub section), [[agentic-workflows]] (frontier
  self-optimizing form), [[self-healing-workflows]] (self-improving vs self-healing),
  [[selling-ai-automations]], [[cold-email-outreach]], [[eval-driven-model-selection]]
  (the metric is the skill), [[claude-code-scheduled-tasks]] (run-while-you-sleep), [[codex]].
- **New pages:** entities [[agent-hub]], [[nanochat]], [[david-andre]], [[nick-saraev]],
  [[greg-isenberg]]; the 4 source pages above.
- Updated [[index]] (batch note + People/Tools/Sources) and the [[Claude Mastery]] bucket.
- **Freshness:** repo dated March 2026; ~25k GitHub stars at recording time (point-in-time).
- Moved all 8 source files `raw/` → `raw/Processed/`.

## [2026-07-24] tasks | Captured AutoResearch follow-up
Added an open item to try an autoresearch loop hands-on (GPU access). Noted again that the
raw inbox drift recurred (clips landed in `raw/`, not `raw/assets/`).

## [2026-07-24] build | Vault AutoResearch loop (self-healing + AutoResearch)
Implemented Karpathy's [[autoresearch]] loop against the vault (all phases). Phase 0:
`git init` (the keep/revert ratchet) + baseline commit. Phase 1: frozen `autoresearch/score.py`
emitting **HEALTH_DEBT** (3·orphans + 2·missing-from-index + 1·stale-claims; soft signals
reported but unscored to keep the metric trustworthy). Phases 2-3: `autoresearch/program.md`
(MODE A self-healing → `main`; MODE B generative → `autoresearch/pending` review branch) +
the `vault-autoresearch` skill. Phases 4-5: overnight scheduling recipe + branch-based human
review documented. Proved MODE A live: HEALTH_DEBT 2→0 by indexing [[agentic-note-taking]]
(logged in `autoresearch/results.tsv`). Documented as [[vault-autoresearch]]; cross-linked
from [[autoresearch]], [[self-healing-workflows]], [[extending-the-llm-wiki]], [[index]],
[[Claude Mastery]], [[tasks/index]].

## [2026-07-24] crm | Catalogued people from iMessage + Gmail
Built the CRM from device data. iMessage `chat.db` (1,087 handles) mapped to Contacts →
**379 people** catalogued, one `crm/` file each + alphabetical `crm/index.md`, tiered by
message volume (inner-circle 43 / close 44 / regular 46 / known 86 / acquaintance 159).
Records are factual (contact + interaction stats + inferred category); relationship context
left for enrichment. **`crm/` is local-only (gitignored)** — never synced to GitHub or the
cloud routine. Gmail (Sent) revealed **Uship = University Shipping**, Cole's Duke-focused
student-shipping venture; identified the team via `.uss@gmail.com` addresses → enriched
[[John Gorman]], [[Tag Mehbod]], [[Ray Kwei]], [[Daniel Hieman]], [[Nick Loria]], created the
[[uship]] entity page, and populated the [[Uship]] bucket. Instagram not reachable (needs a
data export); JHTV produced no email signal (needs a primary source).

## [2026-07-24] crm | Re-catalogued Uship team (current vs. alumni)
Corrected the Uship roster per Cole. **Current team:** Cole, [[John Gorman]], [[Matthew Moskow]]
(created — email-only), [[Daniel Hieman|Danny Heiman]], [[Carson Eisner]], [[Luca Adams-Agresti]]
(Luca joined ~Feb 2026, found via Gmail). **Alumni (graduated):** [[Tag Mehbod]], [[Ray Kwei]],
[[Nick Loria]], [[Marshall Sellingson]]. Enriched each CRM record with `uship_status` + company
`.uss@gmail.com` (and Duke) addresses. Updated the [[uship]] entity (door-to-dorm shipping,
universityshipping.com/signup, weekly Tue meeting) and the [[Uship]] bucket. Also confirmed the
connected Gmail IS the Uship account (`cole.kannamuss@gmail.com`), not Cole's personal address.

## [2026-07-25] build | Finance planning area (local-only)
Set up an investment-planning area in the **local-only** (gitignored) `finance/` folder:
`investment-plan.md` (long-term target + biotech-vs-med-school scenarios, grounded in
`profile/cole.md`) and `data-connection.md` (safe options for connecting bank/investment
data — recommend manual CSV export first, Plaid-based app later; credentials never in the
vault). Linked from the [[Personal]] bucket; added 3 finance tasks to [[tasks/index]]. No
account numbers, balances, or credentials stored anywhere.

## [2026-07-25] build | Finance planning tool (local-only) — a first-class part of the project
Per Cole's direction, made his financial future a central part of the vault (portfolio =
the biggest piece), planning-based and **not** dependent on live bank data. Built in the
local-only `finance/` folder: `index.md` (money & freedom hub — goals anchored to his
"freedom" north star + the Freedom Number framework + open inputs), rewrote `investment-plan.md`
(70/30 VTI/VBR engine, account waterfall, reconciled to the operator-first NYC path — med
school demoted to contingency), and `financial-roadmap.md` (life-stage fuel schedule: the
golden low-expense window now → senior year → the post-grad NYC budget model → scaling).
Grounded in `profile/cole.md` + [[five-year-plan]]. Linked from the [[Personal]] bucket;
updated the finance tasks (define the Freedom Number; open a Roth now; personalize). No
account numbers/credentials stored; everything stays gitignored.

## [2026-07-25] build | Target compensation research (finance/comp-targets.md)
Researched new-grad target salaries for Cole's 3 paths (2026 web sources, cited): JHTV/tech-
transfer ~$60–75k (Baltimore), startup operator ~$80–95k+equity (NYC, primary), VC
analyst/associate ~$95–130k all-in (NYC, stretch). Set planning anchor to **~$85k NYC operator**
(raised the $75k placeholder). Linked from [[finance/index]], [[Job Search]], [[investment-plan]].

## [2026-07-25] finance | Captured real snapshot + analysis (local-only)
Cole provided actual account balances + expected income; recorded in local-only
`finance/snapshot.md` (a living net-worth record) and pointed [[finance/index]] at it. Ran the
analysis and updated the finance tasks — headline actions: max the Roth (underfunded vs
taxable), verify the Roth is actually invested, move idle checking to a HYSA, deploy the
incoming income into the 70/30 plan. No balances in this synced log; all figures stay in
gitignored `finance/`.

## [2026-07-25] ingest | JHTV — org, Capital Strategy, and Cole's tools
Ingested Cole's JHTV materials (homepage / FastForward / Translational Funding / People pages
from jhtv.org + GitHub repo snapshots of his two projects). Enriched [[jhtv]] with FY25 facts
(2,000+ techs, 130+ startups, $4.8B raised, since 2014). Created [[fast-forward]],
[[translational-funding]], [[capital-strategy]] (the team's mandate + Cole's actual work), and
project pages [[vc-matching-second-brain]] (his flagship tech→VC auto-matcher — 151 commits, 391
PitchBook investors, Vercel API, Claude Code) and [[jhtv-grant-finder]] (non-dilutive grant finder
+ AI deadline-updater skill). Populated the [[JHTV]] bucket. **Confidentiality:** licensed
PitchBook data left in the repos, not copied here; the JHTV staff directory (People page) was
not catalogued. Moved 6 sources to Processed (deduped one clip).

## [2026-07-25] ingest | JHTV work — deepened from Cole's local repos/files
Cole pointed to 5 local work dirs (~/Documents: JHTV Second Brain, JHU VC DATABASE, TF reviews,
Grant Finder, Application Memo). Explored **read-only**; enriched [[vc-matching-second-brain]]
with the real architecture (JSON-in-git as DB, client-side scoring, Claude+web-search backend
that auto-researches unknown VCs, ~74 techs/~28 VCs/827 people, shares a grant engine with the
external Grant Finder). Added two responsibilities to [[capital-strategy]]: **reviewing
Translational Funding applications** (Spring 2026 review tracker) and **writing application
memos/one-pagers** (built templates), plus the JHU VC network database.
**Confidentiality upheld:** did NOT copy any proprietary/licensed content into the vault —
PitchBook data, the JHU_VC_Network.xlsx, TF review docs, and application memos stay in Cole's
local repos only. Only experience-level descriptions were written.

## [2026-07-27] tasks | Backfilled @cloud/@local/@human lanes on all open action items; reconciled 2 Sourcing & verification items completed by the nightly run.

## [2026-07-27] autoresearch | Nightly AutoResearch run
MODE A: HEALTH_DEBT was 0 on arrival — no self-healing fixes needed. Logged clean night.
MODE B: Created [[model-speciation]] concept page (fills dangling Karpathy link from skill-issue-karpathy-sarah-guo; covers divergence of AI models into ecological niches, implications for eval-driven selection and multi-model workflows). Added to index.md.
MODE C: (1) Updated [[claude-code-browser-automation]] — grounded against official Anthropic Week 28 docs (built-in browser, v2.1.202–v2.1.206, July 6–10 2026); added computer use research preview timeline (Week 13–14 March 2026); distinguished Claude in Chrome extension. (2) Updated [[claude-code-memory]] — verified Auto Dream cadence as ≥24h AND ≥5 sessions (community-observed; not in official docs); added launch timeline. Checked off both queue items in nightly-queue.md.

## [2026-07-28] autoresearch | Night 2026-07-28 (6-phase loop)
Phase 1 build (web research): corrected a factual error — **Clawdbot and OpenClaw are the same
project** (Peter Steinberger; Clawdbot ~Nov 2025 → renamed OpenClaw ~Jan 2026), made [[openclaw]]
canonical and reframed [[clawdbot]] as the former name; captured **Opus 4.6 = 80.8% SWE-bench
Verified** (Anthropic System Card, Feb 2026) into [[opus-4-6]] and flagged GPT-5.4's contradictory
secondary numbers in [[gpt-5-4]]. Phase 2: marked both @cloud verification items done. Phase 3
(MODE A): HEALTH_DEBT already 0 — no objective fix. Phase 4 (MODE B): created [[agent-security-risks]]
concept (threat model + mitigations for running autonomous/always-on agents), wired into index,
[[claude-code-permissions]], and [[openclaw]].
