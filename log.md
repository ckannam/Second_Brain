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

## [2026-07-25] autoresearch | Nightly AutoResearch run
MODE A: HEALTH_DEBT was already 0 (no orphans, no missing-from-index, no stale-claims). Nothing to fix.
MODE B: Filled [[adversarial-code-review]] stub from a 6-line placeholder to a substantive synthesis page drawing from [[codex-plugin-for-claude-code]], [[running-ai-native-engineering-org]], [[how-we-claude-code]], [[mechanism-over-output]], and [[ai-native-engineering-org]]. Added links to Fiona Fung's "spec drift" framing, the multi-model vs self-review distinction, and the mechanism-over-output trust connection. Proposed on branch `autoresearch/night-2026-07-25` for review.

## [2026-07-26] autoresearch | Nightly AutoResearch run

**MODE A:** HEALTH_DEBT was 0 at baseline; no self-healing iterations needed.

**MODE B:** Expanded [[claude-code-hooks]] from a 3-sentence stub into a full concept page.
Sources: official Anthropic docs (code.claude.com/docs/en/hooks-guide + hooks reference).
Covers 30+ hook events, 5 types, settings.json config, exit codes, common patterns.

**MODE C item 1:** Grounded [[claude-code-permissions]] against official docs. Corrected the
community "three postures" framing (Nate Herk source) — official docs show 6 modes
(default/acceptEdits/plan/auto/dontAsk/bypassPermissions). Added classifier model detail:
Sonnet 5 by default (v2.1.210+), falls back to session model. Preserved community framing
with an explicit supersession note.

**MODE C item 2:** Verified Auto Dream trigger cadence → [[claude-code-memory]] updated to
mark this **unverified**. Official Claude Code memory docs cover only CLAUDE.md + Auto memory;
no /dream command or dreaming toggle documented. "Dreaming" in official Anthropic docs is the
Managed Agents API (research preview) only. A third-party community repo explicitly calls the
consumer feature "unreleased." Queue items 1 and 2 checked off in nightly-queue.md.

## [2026-07-27] tasks | Backfilled @cloud/@local/@human lanes on all open action items; reconciled 2 Sourcing & verification items completed by the nightly run.

## [2026-07-27] autoresearch | Nightly AutoResearch run
MODE A: HEALTH_DEBT was 0 on arrival — no self-healing fixes needed. Logged clean night.
MODE B: Created [[model-speciation]] concept page (fills dangling Karpathy link from skill-issue-karpathy-sarah-guo; covers divergence of AI models into ecological niches, implications for eval-driven selection and multi-model workflows). Added to index.md.
MODE C: (1) Updated [[claude-code-browser-automation]] — grounded against official Anthropic Week 28 docs (built-in browser, v2.1.202–v2.1.206, July 6–10 2026); added computer use research preview timeline (Week 13–14 March 2026); distinguished Claude in Chrome extension. (2) Updated [[claude-code-memory]] — verified Auto Dream cadence as ≥24h AND ≥5 sessions (community-observed; not in official docs); added launch timeline. Checked off both queue items in nightly-queue.md.

## [2026-07-27] ingest | Carson Eisner's UShip vault page (shared by Cole)
Ingested Carson's own UShip topic page (Cole shared it to fill his vault's thin, email-only
UShip coverage). Saved raw → `raw/Processed/2026-07-27 Carson Eisner UShip vault page (shared).md`;
source summary [[carson-uship-vault-page]]. Framing per Cole: absorb the facts but **expansion is
not the #1 point and applies least to Cole** (he forfeits his equity at graduation, spring 2027);
Cole-POV, not Carson's expansion-protagonist voice.
- **Rewrote [[uship]]** from a stub into a full overview: Cole's position (**35% of the legacy
  UShip 6 LLC, tied-largest with [[John Gorman]]; 70% between the two seniors; forfeits at
  graduation; brand-leverage in the Ventures restructure**), storage-first franchise model,
  Fall-2018 history + scale, cap table, finances (~$80K net YTD; margins 54–79%), pricing catalog,
  the Wix/Net-ID email moat (Cole's former domain), Columbia + the trademark cease-and-desist
  ([[Daniel Eisner]]), and the UShip Ventures (DE holdco) restructure.
- **New page [[uship-os]]** — Carson's multi-tenant OS (Next.js/Prisma/Supabase, Render); the 2027
  expansion linchpin.
- **Enriched CRM** with roles + legacy-LLC stakes: [[Carson Eisner]] (5%, data/finance+OS, father
  [[Daniel Eisner]]), [[John Gorman]] (35%, logistics/Duke liaison), [[Daniel Hieman|Heiman]] (10%,
  expansion/Columbia), [[Matthew Moskow]] (10%, data/CTO, holds the list CSVs), [[Luca Adams-Agresti]]
  (5%, ambassadors), [[Ray Kwei]] ("Papa Ray"? possible founder).
- Updated [[Uship]] bucket + `index.md`; filed 3 `@human` tasks (name-spelling reconciliation
  incl. the `Daniel Hieman`→Heiman filename typo; confirm Papa Ray/founding; Cole's stake in the
  Ventures/pass-down decision).
- **Cross-check kept:** Carson (joined Feb 2026) omits alumni [[Ray Kwei]]/[[Nick Loria]] and
  narrows Cole to "email" — the vault keeps Cole's longer tenure (Sep 2023), broader ops role, and
  those alumni. Carson's page is treated as a rich *secondary* source, not overriding Cole's own
  knowledge.

## [2026-07-27] update | UShip — Cole's confirmations (Heiman rename, Papa Ray, equity caveat)
Cole confirmed three things on the Carson-page ingest: (1) Carson's 2018 figure is just his
Square-**data** range — Carson joined the company in 2026 (already reflected); (2) **name is
Heiman** → renamed `crm/Daniel Hieman.md`→`Daniel Heiman.md` and updated all live
`[[Daniel Hieman]]` links (buckets, [[uship]], crm/index, profile); (3) **"Papa Ray" = [[Ray
Kwei]]** (early/founding-era figure) — updated [[Ray Kwei]] + [[uship]]. Also softened the
"Cole's leverage" framing on [[uship]] per Cole: team is exploring holding companies but **Cole
is unsure he'll hold this equity long-term** — flagged as a later conversation, not a decision to
force. Tasks updated accordingly. (Historical `[[Daniel Hieman]]` mentions in earlier log entries
left as-is per append-only.)

## [2026-07-27] ingest | Neuroscience batch (3 sources) — seeded neuroscience-of-behavior cluster
Cole asked to ingest the raw queue and flagged a standing goal: he's **obsessed with neuroscience
and wants his behaviors/decisions justified in neuro mechanisms** (saved to auto-memory). Ingested
3 sources: **[[neuroplasticity-rewiring-brain-ixcarus]]** and **[[conscious-subconscious-mind-ixcarus]]**
(both *ixcarus* on Substack) + **[[how-to-remember-everything-brainhealthdecoded]]** (*Brain Health
Decoded*).
- **Filename collision resolved:** the two files both clipped as `How To Remember Everything You
  Learn(.md / 1.md)` are *different* articles — `1.md` is actually the conscious/subconscious deep
  dive, not a memory-technique piece. Noted on the source page.
- **11 new concept pages** (hub + 10): [[neuroscience-of-behavior]], [[neuroplasticity]],
  [[predictive-processing]], [[productive-discomfort]], [[hebbian-learning]], [[memory-consolidation]],
  [[learning-by-connection]], [[knowledge-types]], [[conscious-vs-subconscious]],
  [[reticular-activating-system]], [[cognitive-biases]].
- **Enrichment / reciprocal links:** [[identity-led-goals]] (identity is neurological),
  [[environment-design]] (mirror neurons/cues), [[discipline-without-willpower]] +
  [[how-to-build-discipline]] (neuroplasticity as the "restructure the brain" mechanism),
  [[agent-dreaming]] (machine ↔ human memory consolidation), [[erin-meryl]] (thread origin),
  [[marsh-memory-lab]] (IOED ↔ "explain from scratch").
- Reconciled pop-science claims (7-second pre-decision, superconscious, subliminals, pineal) as
  framing, not fact, on the source pages. Updated index.md (new concept + source sections, batch
  note) and the [[Personal]] bucket.
- **Still in the inbox (not ingested):** re-clip of the Obsidian Vault Deep Dive (already covered by
  [[obsidian-vault-deep-dive-emai]]) and `I Tested Opus 5 vs. Fable 5` (description/timestamps only,
  no transcript) — flagged to Cole for a decision.

## [2026-07-27] filed | Neuro — Cole's neuroscience YouTube channel (venture)
Cole introduced his **[[neuro-channel|Neuro]]** venture: a stick-figure "walking brain" character
explaining neuroscience in ~45–90s YouTube Shorts, to make brain science accessible. Filed it into
the vault as the natural output layer of the neuroscience ingest.
- New entity pages: **[[neuro-channel]]** (venture hub — mission, character, pipeline, status,
  tech) + tool stubs **[[remotion]]** (React→MP4 renderer) and **[[elevenlabs]]** (voice).
- **Key connection made:** the vault's [[neuroscience-of-behavior]] cluster *is* the channel's
  topic bank — mapped 10 existing concept pages to ready video hooks on the [[neuro-channel]] page.
  Ingest → wiki → Shorts is the same compounding loop as [[llm-wiki-pattern]].
- Enriched [[cole|profile]] (Neuro under ventures + interests; framed as the synthesis of his
  science↔business↔service tensions). Updated index.md (Tools/venture) and [[Personal]] bucket.
- **Open offers to Cole:** (1) give **Neuro its own bucket** (it's a real venture like Uship/JHTV);
  (2) pick the first real (non-trailer) video topic from the bank; (3) when ready, help build
  video #2 in the `neuro-video/` Remotion repo. Repo is separate from this vault — nothing built
  there this session.

## [2026-07-27] update | Neuro bucket + production-pipeline design
Per Cole ("just incorporate into my vault for now" + asked how to auto-produce/store videos):
- Created the **[[Neuro]] bucket** (venture, like Uship/JHTV); added to buckets/index, root index
  buckets line, and repointed the Personal bucket's Neuro note to it.
- Filed **[[neuro-production-pipeline]]** answering the automation question (design only, not built):
  core principle **spec.json = source of truth, MP4 = rebuildable artifact**; spec-driven pipeline
  (Claude API script ← vault concept page → ElevenLabs voice → Remotion render → YouTube upload);
  3-layer storage (git specs / binaries not-in-git via YouTube-unlisted or R2 / **vault = queryable
  video catalog**); v1 = local one-command render, v2 = Remotion Lambda / GH Actions + scheduled
  task; keep Cole's human taste gate. Linked from [[neuro-channel]] and indexed.

## [2026-07-27] query | Best way to build Neuro stick-figure animation automatically → filed design
Cole asked the best way to build stick-figure animation like Neuro automatically with Claude Code.
Filed **[[neuro-character-rig]]**: recommend an **articulated SVG rig as a Remotion React component**
— nested joint `<g>` transforms, a named **pose library** + procedural idle/blink/brain-pulse,
sequenced to script cue frames; **amplitude-driven mouth-sync** via `@remotion/media-utils`
(upgrade to Rhubarb visemes later). Chosen over Rive/Lottie/AI-video specifically because the rig is
**code Claude can author & tweak from a script**, not a binary/visual-tool artifact. One-time step:
trace/redraw `neuro.png` into a layered, style-matched SVG (round-cap strokes). Linked from
[[neuro-channel]] (future articulated character), [[neuro-production-pipeline]] (its animation step),
and the [[Neuro]] bucket; deferred until Cole leaves the flat-PNG format.

## [2026-07-27] ingest | Fulbright application (Cole's brief + Anna's Duke process email)
Ingested two sources into a new **[[Fulbright]]** bucket: Cole's project brief
(`raw/Processed/2026-07-27 Fulbright Application Project Context (Cole).md` → [[fulbright-project-context]])
and [[Anna Bernard-Hoverstad]]'s 2026-07-14 "Fulbright @ Duke 2026" email
(`raw/Processed/2026-07-14 Anna Bernard-Hoverstad Fulbright Duke email.md` → [[anna-fulbright-duke-2026-07-14]]).
Created entity [[fulbright-us-student-program]]; concepts [[ai-lowering-entrepreneurship-barriers]]
(the Open Study/Research thesis, grounded in [[jhtv]]/[[translational-funding]]) and
[[fulbright-country-selection]] (India/Brazil/Indonesia); CRM records for [[Anna Bernard-Hoverstad]],
[[Cyprene Caines]], [[Clayton Beasley]]. **Reconciliation** (email supersedes the stale brief):
added the hard **Sept 10 12pm ET** rec-letter + language-eval deadline, corrected the campus deadline to
**Aug 21 12pm ET** (lock/"Ready for Review", not submit) and final to **Oct 6 4:59pm ET**; noted the
July 10 Anna meeting already happened and the **writing-group signup (July 20) already passed** as of today.
Filed 10 Fulbright action items in `tasks/index.md` (binding constraint = Sept 10 rec letters).

## [2026-07-27] tasks | Captured 9 laned Neuro action items
Filed a **Neuro — YouTube channel** section on [[tasks/index]]: 2 @cloud (draft top-3 scripts from
the vault concept pages; benchmark successful neuro Shorts channels), 5 @human (pick first topic;
create the YouTube channel; get an ElevenLabs API key → Keychain not vault; decide master storage;
upload video #1), 2 @local (build the v1 render pipeline; build the articulated SVG rig — deferred).
Sequence: @cloud drafts → Cole picks → @human voice → @local build/render → @human upload.

## [2026-07-27] ingest | Stickman-animation free-AI batch (7 videos) → no-subscription Neuro stack
Cole added 7 YouTube tutorials on making stick-figure videos with free AI tools; goal = a Neuro
pipeline that adds **no subscription but the Claude one he has**, and he must **review every video
before it posts**. Ingested as a cluster:
- **[[stickman-animation-free-ai-tutorials]]** — one source-cluster page cataloging all 7 (unique
  URLs; fully read #1 Digital Income Project/Claude, #2 Jackson free course, #5 Mark AI Guy
  character-consistent finance template; #3/#4/#6/#7 catalogued by tool coverage).
- **[[neuro-free-tool-stack]]** (new concept) — the $0 stack: **Claude** (brain/script) + **Google
  Flow / Nano Banana 2** (free image gen, `neuro.png` as consistency reference) + **Cole's own
  voice** or free TTS (no ElevenLabs) + **Remotion or CapCut** + YouTube audio library + Canva.
  Hard-wires the **review-before-post** gate (nothing auto-publishes).
- Enriched [[neuro-production-pipeline]] (own-voice step, review gate, per-scene art) and
  [[neuro-character-rig]] (added the image-per-scene path alongside the SVG rig).
- Updated tasks: replaced the "get ElevenLabs API key" @human item with **decide voice (record
  your own)** + **create free Google Flow/CapCut accounts**; retargeted the build task to the free
  stack + review gate. Updated index (concept/source/batch note) + [[Neuro]] bucket.
- Moved 7 files to `raw/Processed/`. **Inbox still holds** the Obsidian re-clip + Opus5/Fable5 stub
  (both previously flagged, awaiting Cole's call).

## [2026-07-27] research | Fulbright host outreach — expanded roster + 10 drafted emails
Per [[Anna Bernard-Hoverstad|Anna]]'s advice (contact academic universities + ecosystem hosts in tandem,
>1 per country), researched and drafted **10 tailored outreach emails** → new working doc
[[fulbright/outreach|fulbright/outreach.md]]. **Confirmed emails** (official/faculty pages):
Setia (pankajsetia@iima.ac.in) + IIMA CDT co-chair Deodhar (swanandd@iima.ac.in), CIIE.CO (info@ciie.co),
Geber Ramalho/CIn-UFPE (glr@cin.ufpe.br), Porto Digital (portodigital@portodigital.org),
IIE-EAP desk (FBstudent.EAP@iie.org). **Verify-before-send:** ISB Deepa Mani, NSRCEL, CESAR, AMINEF,
ITB-LPIK, Prasetiya Mulya (contact-page + address pattern given). New hosts added beyond the brief:
Deepa Mani (ISB), NSRCEL (IIMB), CESAR (Recife), ITB-LPIK, Prasetiya Mulya. Noted Indonesia's AMINEF
finalizes affiliation post-award. Updated [[fulbright-country-selection]], [[Fulbright]] bucket, tasks.

## [2026-07-27] research | Fulbright outreach — verified addresses + project abstract
Verified the 6 unconfirmed host emails: **confirmed** AMINEF `infofulbright_usa@aminef.or.id` and
Prasetiya Mulya `info@prasetiyamulya.ac.id`; **no public email** for ISB (Deepa Mani), NSRCEL, CESAR,
and ITB-LPIK — route via their contact forms / LinkedIn (recorded per-contact in
[[fulbright/outreach|outreach.md]], no addresses guessed). 7 of 11 contacts now have a confirmed inbox.
Wrote a reusable 1-page [[fulbright/project-abstract|project abstract]] (from [[ai-lowering-entrepreneurship-barriers]])
to attach to the emails, with per-country/host brackets. Updated the [[Fulbright]] bucket + tasks.

## [2026-07-27] decision | Neuro voice plan + brand identity (email/handle/domain)
- **Voice:** free AI TTS now for drafting/preview; **re-record in Cole's own voice as the final
  step before each post** (updated [[neuro-free-tool-stack]] + [[neuro-production-pipeline]]).
- **Brand identity (proposed):** "Meet Neuro" / **`@meetneuro`** (backups `@heyneuro`, `@askneuro`),
  email `meetneuro@gmail.com` (Cole creating now), domain `meetneuro.com` (~$12/yr, later).
  Recorded on [[neuro-channel]]; tasks updated (email/handle + channel + domain). Availability TBC.

## [2026-07-27] task | Fulbright — degree reconciled + 10 outreach emails staged to Duke inbox
Cole confirmed his degree: **Neuroscience + Chemistry** (double major; Statistics dropped, I&E minor) —
updated [[Duke]] + all outreach materials, closed the reconcile task. Finalized the signature
(cdk35@duke.edu). Created **10 Gmail drafts** (the Gmail connector is draft-only — no send tool),
each addressed to **cdk35@duke.edu**, titled `[Fulbright 1/10 … 10/10]`, each with a header block
(real recipient + confirmed address or contact-form channel + subject + attach reminder) above the
ready-to-send body. Cole reviews in Gmail, sends to himself, then sends to hosts from his Duke account.

## [2026-07-27] crm | Networking engine built + 6 contacts added (Job Search)
Built the **networking engine** for the [[Job Search]]: [[outreach-pipeline]] (the weekly board —
Lane 0 warm/active · Tier 1 marquee cold · Tier 2 roster cold) + [[outreach-kit]] (reusable pitch /
proof points / ask-menu). **Monday-morning batch** drafts into Gmail (`colekannam@gmail.com`) as
ready-to-send drafts; **Cole reviews + sends — nothing auto-sends** (connector is draft-only).
Added/enriched 6 CRM records, all on-strategy (health/bio/AI): **[[Arielle (Forus Health)]]**
(warm — called 7/14, reconnect near grad re: joining the team, from iMessage), **[[Sean Tunis]]**
(enriched: Cole's JHTV mentor, CMTP founder / ex-CMS CMO), and 4 from Cole's `~/Documents/Networking
People/` prep docs — **[[Christina DeMur]]** (JHTV Tech Dev), **[[Dhevi Kumar]]** (Microsoft Health),
**[[Kahlil DSouza]]** (GondolaBio/BridgeBio), **[[Nancy Kass]]** (Hopkins bioethics + FDA). Updated
`crm/index.md`, the [[Job Search]] bucket (new Networking-engine section + action items). First
batch pending Cole's go.

## [2026-07-27] Neuro build session — character solved + pivot to AI doodle scenes (paused)
Long build session on the [[neuro-channel|Neuro]] / **Doodlecortex** channel (repo `~/Desktop/neuro-video`):
- **Fixed** a Remotion crash (missing-voice-MP3 404 → `useOptionalAudioData` makes audio optional).
- **Character solved:** cut Cole's real drawing to `neuro-real.png` + `neuro-head.png`; rebuilt `NeuroSVG`
  = his head on the existing rigged limb skeleton → Neuro **walks + gestures** and looks exactly like his art.
  Rebuilt the intro (walk-ins, per-line gestures, kinetic chunked captions); rendered `~/Downloads/neuro-intro-v2.mp4`.
- **Pivot validated:** Cole set the bar at **@Zenn0009** — those are AI-generated **hand-drawn doodle
  scenes** (new illustration every few seconds), not a rigged character. Proved **Gemini/Nano Banana**
  makes Zenn-quality doodle scenes **free via Cole's login** (2 scenes: kitchen doorway; "WORKING MEMORY"
  brain-door). New direction: AI doodle scenes = engine, Remotion = captions/assembly.
- **Decided:** brand **Doodlecortex** (`@doodlecortex`); **Shorts** format; AI voice now / own voice as the
  final pre-post step. **Open decision:** image pipeline route A (Gemini API, ~cents, recommended) vs B (free web UI).
- Updated [[neuro-channel]], [[Neuro]] tasks (resume note), and the project memory. Working changes in the
  video repo are uncommitted. Remotion Studio dev server left running on :3000.

## [2026-07-27] improve | Outreach engine upgraded (vault-improve, local steps 1–4)
Ran `/vault-improve` on the networking engine ([[outreach-pipeline]] + [[outreach-kit]]). Diagnosis:
open loop, thin manual supply, undirected, unmeasured. Plan → `tasks/improvements/2026-07-27-outreach-engine.md`.
Executed the 4 local steps: **(1)** closed the loop — runbook now reconciles status via Gmail
`search_threads` + fires the 7–10-day follow-up rule; **(2)** ran an iMessage career-signal
**warm-lead harvest** → queue of candidates to confirm (found a Forus-connected connector + Chai
Discovery; re-found Arielle/Sean, validating the method); **(3)** wired the real résumé PDF into the
kit + **installed Cole's `networking-prep` skill** to `.claude/skills/`; **(4)** parsed the full
~1,900-person PIKE roster PDF (pdfplumber) → NY/DC **Tier-2 expansion** (email column garbles on
auto-extract → verify addresses from the PDF at draft time; no grad-year → verify recency). Parked:
@cloud target-org map (seed Chai Discovery + Forus), @local reply-rate scoreboard, @human confirm inputs.

## [2026-07-27] improve | networking-prep skill → vault-native (local steps 1–7)
Ran `/vault-improve` on the `networking-prep` skill (built before the vault, frozen profile).
Rewrote `.claude/skills/networking-prep/SKILL.md`: loads Cole's **live** positioning
([[cole]] + [[five-year-plan]] + [[outreach-kit]]) instead of a hardcoded bio; reads the **CRM +
iMessage history + [[outreach-pipeline]] status** before web research; **Section 5 pitch** now pulls
the outreach-kit's pitch/proof-points/ask-menu + a take grounded in Cole's own wiki; **Section 2**
anchors to the current health/bio/AI operator lane; output is a linked **markdown prep page**
(`crm/prep/<Name>.md`, .docx optional — dropped the Cowork-only tool); and it now **feeds the
engine** (CRM record + pipeline row + index + log). Kept the strong research method + tone bar.
Plan: `tasks/improvements/2026-07-27-networking-prep-skill.md`. Parked: @human output-format pref
(default markdown + optional .docx).

## [2026-07-27] decision | networking-prep = markdown-only
Cole chose **markdown-only** output for the [[networking-prep]] skill — no `.docx`. Updated
`SKILL.md` (Step 5-output + description) and **deleted the now-dead `scripts/doc_helper.py`**. The
vault prep page (`crm/prep/<Name>.md`) is the sole artifact. Closed the parked @human task.

## [2026-07-27] ingest | Spaced-learning batch (4 sources + SpaceRep) for the channel × app vision
Ingested Cole's spaced-repetition research bundle, tied to the [[neuro-channel|Neuro channel × learning-app]]
vision. **Sources:** [[spacing-math-meta-analysis-murray-2025]] (keystone meta-analysis — spacing robust for
math g=0.28; retrieval *not* robust, g=0.18 CI crosses zero; PDF preserved in `raw/Processed/`),
[[neuroscience-of-spacing-brainfacts]] (CREB/molecular mechanism; cross-species; the adoption gap),
[[spacing-testing-complex-skills-study]] (combined spacing+testing protects complex *skills* at 3mo),
[[optimizing-spaced-learning-smolen-2016]] (**recovered from a broken clip** — molecular optimum; optimal
spacing is computable). **New concepts:** [[spacing-effect]], [[retrieval-practice]], [[interleaving]],
[[spaced-repetition]]. **New entity:** [[spacerep]] (competitor — FSRS + Google Calendar; the gap it leaves).
**Enriched:** [[knowledge-types]] (spacing layer + the type→retrieval-modality routing = the product wedge),
[[memory-consolidation]] (molecular clock), [[neuroscience-of-behavior]] hub, [[neuro-channel]] (added the
"channel × app" thesis: *not another Anki* — triage + type-matched retrieval; don't rebuild FSRS). Filed a
new **Neuro — learning app** task section (spec the Learning-Triage vault skill as the finishable wedge).
**Off-thread, same batch:** [[opus-5-vs-fable-5-nate-herk]] (Nate Herk; freshness-flagged — [[opus-5]]/[[fable-5]]
are beyond the vault's [[opus-4-8]] snapshot, to-verify). **Re-clips moved to Processed** (no new pages):
Obsidian-Deep-Dive + 2 stickman clips (already covered by [[stickman-animation-free-ai-tutorials]]).

## [2026-07-27] build | Proactive iMessage networking briefs (launchd + AppleScript)
Wired **proactive iMessage** as Cole's reminder channel (he doesn't keep a calendar; already lives
in texts; declined Slack/Discord). Delivery proven: sends to his self-chat **+14436822254** via
AppleScript (`~/.claude/networking/send.scpt`) — no Claude session needed at fire-time. A
deterministic composer (`brief.py`, no LLM) reads [[outreach-pipeline]] + `tasks/index.md` and builds
a short **morning brief**; Mondays append the **"reply go to run the batch"** trigger line. Scheduled
via a user **launchd** agent (`com.cole.networking-brief`, daily 8:07am; loaded + tested end-to-end,
two texts confirmed received). Files in `~/.claude/networking/`. **Pending Cole's call:** whether to
wire the reply-"go" → auto-run (needs a headless-Claude poller w/ skipped permissions — a
deliberate security choice; nothing to run until his first batch anyway).

## [2026-07-27] build | Morning brief upgraded: time-remaining countdowns + Google "Claude-layer" calendar
Per Cole: the brief now leads with **time-left countdowns** (fights [[temporal-discounting]]) —
anchors: **JHTV internship ends Aug 13, 2026**, Fulbright lock Aug 21, rec letters Sept 10,
**Graduation Sun May 9, 2027** (north star). Config in `~/.claude/networking/brief.py`.
Found Cole's **Google Calendar is empty going forward → his real calendar (like his email) is
Outlook**, which I can't read (no Microsoft connector). So the **two-way calendar** uses his Google
Calendar as a **"Claude layer"**: seeded the 4 milestones as all-day events (with popup reminders)
via the connector; he subscribes on his phone next to Outlook. **Gmail is NOT his inbox** (Outlook
is) — dropped inbox-watching; Gmail stays only for outreach drafts. Saved both facts to memory.

## [2026-07-27] build | Weekly concert digest (hobbies: travel + live music)
Built Cole a **weekly concert digest** over the proven iMessage channel — his first deliberate
"invest in hobbies" tool. Every **Monday ~8am** a launchd agent (`com.cole.concert-digest`) runs
`~/.claude/concerts/run_digest.sh`, which computes the active metro deterministically
(`active_metro.py`: **Baltimore until 2026-08-17, then Triangle/Durham–Raleigh** on his move) and
launches a headless Claude session running the **`concert-digest`** skill: it reads the
Cole-editable taste profile (`profile/concert-taste.md` — local-only, gitignored), web-searches his
artists (Phish, Billy Strings, Goose, Caamp, Tyler Childers, Zach Bryan, JRAD, Sturgill…) + local
venue calendars, ranks by taste + proximity with 🔎 **taste-matched discovery**, and texts a
scannable block to his self-chat **+14436822254**. Reuses the [[outreach-pipeline]]/networking-brief
delivery pattern (AppleScript `send.scpt`). Ships standalone; exposes a `section` mode so a future
combined weekly update can absorb it. Spec + plan in `docs/superpowers/`.

## [2026-07-28] autoresearch | Night 2026-07-28 (6-phase loop)
Phase 1 build (web research): corrected a factual error — **Clawdbot and OpenClaw are the same
project** (Peter Steinberger; Clawdbot ~Nov 2025 → renamed OpenClaw ~Jan 2026), made [[openclaw]]
canonical and reframed [[clawdbot]] as the former name; captured **Opus 4.6 = 80.8% SWE-bench
Verified** (Anthropic System Card, Feb 2026) into [[opus-4-6]] and flagged GPT-5.4's contradictory
secondary numbers in [[gpt-5-4]]. Phase 2: marked both @cloud verification items done. Phase 3
(MODE A): HEALTH_DEBT already 0 — no objective fix. Phase 4 (MODE B): created [[agent-security-risks]]
concept (threat model + mitigations for running autonomous/always-on agents), wired into index,
[[claude-code-permissions]], and [[openclaw]].

## [2026-07-28] journal | Caffeine, social wins, and golf-course anger
First journal entry. Cole's day: first Fast Forward team meeting (met [[Stewart Neifart|Stew]]'s
boss **Myra** — new CRM stub), office bowling day where he was notably talkative. Key self-insight:
he's "leagues more social when caffeinated" → **coffee-before-networking** is now a standing rule,
tied into [[cole-job-search-strategy|relationship-first job search]] and [[networking-prep]]. Also
flagged golf-course anger that spikes specifically around [[Dad]] — gave affect-labeling / breath-reset
/ reframe tactics. Entry: [[2026-07-28 - caffeine-social-and-golf-anger]].

## [2026-07-29] crm | Job-search targets: Flourish + FedTech added, Ian Ryu (warm path) created
Added two recruit targets to [[target-orgs]]. **Flourish** (flourishlabs.ai) → 🟢: Bezos-anchored
($500M, $2.5B val, Jun 2026) **brain-inspired AI** startup; hook = co-founder Thomas Reardon's Duke
neurobiology MS + Cole's neuro-and-build fit; actively hiring; value-first cold draft written to
info@. **FedTech** (deep-tech venture studio, actively hiring) filed under a new **🤝 Warm-path
targets** section (established employers reached via a warm connection, where the no-jobs-ask rule
relaxes). Created CRM record for **[[Ian Senungwan Ryu]]** — JHTV colleague, ex-FedTech, Cole's
warm-intro/referral path into FedTech. Next: ask Ian for the inside read + an intro.

## [2026-07-29] ingest | WIRED — Flourish (Bezos-funded neuro-AI startup)
Ingested Steven Levy's WIRED launch profile of **[[flourish|Flourish]]** (PDF Cole dropped; copied to
`raw/Processed/`). Created [[flourish-wired-core-algorithm]] (source), [[flourish]] (company entity),
[[catalio-capital]] (Baltimore neuro VC / backer), and CRM records [[Joshua Vogelstein]] + [[Thomas Reardon]].
**Key job-search finding:** cofounder **[[Joshua Vogelstein]] is a Johns Hopkins BME professor** and backer
**[[catalio-capital|Catalio]]** is Baltimore-based → a real **Hopkins/[[jhtv|JHTV]] warm cluster** into
Flourish, much stronger than a cold info@ note. Corrected the earlier Reardon-Duke hook (he's Columbia;
Duke MS is minor). Updated [[target-orgs]] Flourish row (→ enriching, route via Vogelstein/JHTV) and
index.md. Flourish's hippocampus-inspired, learn-without-retraining approach echoes this vault's
[[llm-wiki-pattern|file-based memory]].

## [2026-07-29] ingest | UShip Fall 2026 move-in signups (Wix export) + funding-feed seed
Cleared the raw inbox (2 files). **(1) UShip "Forms & Submissions"** — 100 Fall-2026 move-in booking
submissions. **PII-heavy** (names/emails/phones/home addresses), so per the "customers aren't catalogued"
rule I kept the raw file **local-only** (moved to new gitignored `raw/private/`; added `.gitignore` rule)
and synced **only aggregates**: created [[uship-fall2026-signups]] and a "Fall 2026 demand snapshot" on
[[uship]]. Key: **Email Campaign = 58% of signups** (validates Cole's email-list moat), ~35% repeat/referral,
Home Pickup upsell chosen ~half, NYC-metro corridor; dedupe needed (edited re-submissions). **(2) "Best
Startups with Recent Funding in 2026"** = the `startups.gallery/news` feed already seeded into [[target-orgs]]
on 2026-07-28 → moved to `raw/Processed/` (public data). Both sources out of the inbox.

## [2026-07-29] query | Tell me about my work at JHTV
Answered from [[JHTV]] bucket → [[jhtv]], [[capital-strategy]], [[vc-matching-second-brain]],
[[jhtv-grant-finder]], [[translational-funding]], [[Stewart Neifart]]. Synthesis (Capital
Strategy Intern since Jun 2026; VC-matcher flagship + grant finder + TF app review + memos/
one-pagers/VC network DB) is already fully owned by [[capital-strategy]] — no new page created
(would duplicate). No page changes; query logged only.

## [2026-07-29] ingest | FedTech General Application (talent database)
Ingested the FedTech "General Application" web clip. Key: FedTech runs a **general application / talent
database** (`fedtech.applytojob.com/apply/dGXQKN4HZq`) — apply with no specific role posted and they reach
out on a future match. Folded into [[target-orgs]] (FedTech row: entry point + the "Ian intro → then submit
general app" play) and [[Ian Senungwan Ryu]] next-action. Reaffirms FedTech's self-framing as deep-tech
"venture builders" (since 2015). Moved source to raw/Processed/. Inbox clear.

## [2026-07-29] ingest | Kronos — foundation model for financial markets (GitHub README)
Ingested the stray raw file (shiyu-coder/Kronos README). Created [[kronos-financial-foundation-model]]:
first open-source foundation model for financial K-lines (OHLCV candlesticks), 45+ exchanges,
decoder-only Transformer + hierarchical tokenizer; AAAI 2026 / arXiv 2508.02739. Framed it as the
**"foundation-model recipe applied to a non-language domain"** pattern and cross-linked it to [[flourish]]
(brain) and Chai (antibodies) as siblings. Noted authors' own caveats (raw signals ≠ pure alpha; model
costs/slippage). Open question logged: why Cole saved it (quant interest vs AI-trend tracking). Moved
source to raw/Processed/ (renamed cleaner). Inbox clear.

## [2026-07-29] connect | Kronos → quant-investing cluster
Per Cole, connected [[kronos-financial-foundation-model]] into the investing cluster (not just standalone
AI): it's a signal generator whose caveats restate [[signals-that-trade-themselves]] ([[man-group]]) — the
forecast is the tip; backtest/Sharpe/drawdown/risk-neutralization/costs are the iceberg. Added reciprocal
links from signals-that-trade-themselves + man-group. Noted the contrast with Cole's own passive
[[investment-plan]] (time-not-timing). Cool tech + genuine quant-AI curiosity.

## [2026-07-29] ingest | Job-search playbook — Ben Lang cold-email + hidden-roles + July hiring thread (3 sources)
Batch-ingested a coherent Ben Lang / Next Play job-search cluster. Created concept [[cold-email-job-search]]
(the ≤200-word/one-ask/no-fake-personalization rules + who-why-whycare format + 9 discovery sources) and
source [[july-hiring-thread-benlang]] (86 hiring startups from @benln's July thread). **Engine enrichment:**
added the 9 discovery sources to the [[outreach-pipeline]] runbook (step 2) and a pre-send checklist to
[[outreach-kit]]. **Leads:** promoted in-lane NYC health/bio/AI names to [[target-orgs]] 🟡 — **Ataraxis AI**
(precision oncology), **Formation Bio** (AI drug dev), **PhotonHealth**. Big theme reinforced: best roles are
filled before they're posted → discovery + warm-specific outreach beats mass applications. Moved all 3 sources
to raw/Processed/. Inbox clear.
## [2026-07-30] autoresearch night | branch autoresearch/night-2026-07-30
Phase 0: selected 3 @cloud builds (skipped target-org map — deliverable `crm/target-orgs.md` is
gitignored/local-only, can't persist from cloud). Phase 1 builds (web research): (1) **verified
Fulbright award rates** — India ~46% and Brazil ~64% confirmed, **Indonesia corrected ~40%+ → ~24%**,
added 2027–28 cycle + Indonesia language/award-count/timeline into [[fulbright-country-selection]];
(2) **web-grounded [[optimizing-spaced-learning-smolen-2016]]** — added the 10/10/5/30-min enhanced
protocol vs 20-min uniform, phospho-CREB1 result, Aplysia PKA+ERK mechanism, free arXiv full text,
DOI fix; (3) **benchmarked neuroscience/psychology Shorts channels** → new [[neuro-channel-benchmarks]]
(Psych2Go, 2-Minute Neuroscience, Neuro Transmissions, Sprouts) with hook/pacing/title patterns +
Neuro's doodle wedge. Phase 2: 3 items → Done; target-org + draft-scripts got progress notes.
Phase 3 (MODE A): HEALTH_DEBT 0 after build — no objective fix. Phase 4 (MODE B): created source
[[enhancing-learning-rats-computational-protocol-2023]] — Smolen's computational-spacing result
extended from sea slugs to a mammal (irregular schedule beat fixed spacing in rats), reciprocally
linked. One morning PR (base main); not merged.

## [2026-07-30] outreach | Fulbright host-affiliation emails — all 10 sent
Sent Cole's 10 Fulbright host-outreach emails from Duke (cdk35@duke.edu): India (Setia/IIMA,
Deepa Mani/ISB, CIIE.CO, NSRCEL), Brazil (Geber Ramalho/CIn-UFPE, Porto Digital, CESAR),
Indonesia (IIE+AMINEF guidance, ITB-LPIK, Prasetiya Mulya). Closed all 4 former "no public
email" gaps with verified addresses (Mani `deepa_mani@isb.edu`, NSRCEL
`nsrcel.socialmedia@iimb.ac.in`, CESAR `biz@cesar.org.br`, LPIK `lpik@lpik.itb.ac.id`).
Built 3 per-country 1-page abstract PDFs (Desktop) + attached Cole's CV; added an
Andrej-Karpathy-inspired AI-query-engine credential line to every email; fixed the Gmail
CIIE.CO auto-linkify. Updated [[fulbright/outreach]] status + [[tasks/index]] (send item done,
follow-up nudge queued for 2026-08-13).

## [2026-07-30] ingest | Claude chat export ("Claude Past data") — career mining
Mined the 133-conversation export (Sep 2024–Jul 2026). Distilled Cole's BD/deal-fluency
positioning + a Duke/JHU biotech & AI-bio target roster + warm leads into **local-only** crm
files (kept out of git per the PII rule): new [[bd-target-companies]], warm leads added to
[[outreach-pipeline]] (Connor Larkin, Ben Freeberg, Sabah Oney, Matthew Rizzo; Arielle's Jonah
Scherl intro path). Saved memories: [[cole-working-style]] + folded positioning into
[[cole-job-search-strategy]]. Raw export not ingested into the wiki.

## [2026-07-30] ingest | The Economist — Musk & Carlson interviews (2 YouTube)
Ingested 2 long-form [[the-economist|Economist]] "Insider" interviews (channel: The Economist).
Created sources [[elon-musk-economist-2026]] + [[tucker-carlson-economist-2026]] and entities
[[elon-musk]], [[tucker-carlson]], [[the-economist]]. **Connection:** the Musk interview corroborates
the vault's AI picture from outside — Anthropic as "the leader in AI" and the [[mythos]]→[[fable-5|Fable]]
lineage (plus China's Kimi K3) — so enriched [[anthropic]], [[mythos]], [[fable-5]] with reciprocal links
and added a Musk *convergent-superintelligence* counterpoint to [[model-speciation]]. Musk's "work becomes
optional / abundance" theme linked to [[ai-lowering-entrepreneurship-barriers]] + Cole's freedom frame.
Carlson kept standalone (geopolitics, off the main clusters). Freshness-flagged (predictions = snapshots).
Sources moved to `raw/Processed/`.

## [2026-07-30] ingest | The Culture series (Wikipedia) — Banks
Ingested the Wikipedia clip on Iain M. Banks's *Culture* series (Cole clipped it after the Musk thread).
Created source [[culture-series-wikipedia]] + entity [[the-culture]], and a new hub concept
[[post-scarcity-and-meaning]] connecting **[[elon-musk-economist-2026|Musk's "work optional"]] ↔ the Culture
↔ Cole's own meaning-crisis essay / "free + useful."** Enriched [[elon-musk]] (cites the Culture; SpaceX
drone-ship names). Also taught Cole the series (what it is, why Musk/Bezos love it, where to start:
Player of Games → Use of Weapons → Surface Detail). Source moved to `raw/Processed/`.

## [2026-07-30] query | Who is Cole & how can he get better
Answered a synthesis question from the vault. Read [[cole|profile]], [[five-year-plan]], the
[[Job Search]] + [[Personal]] buckets, and the discipline/neuro clusters. Filed the answer to
**local-only** `profile/growth-plan.md` (built from gitignored PII, so kept out of the synced wiki/;
not added to root index.md for the same reason). Core verdict: concentrate the spine (operator-first,
health/bio/AI), reframe "guarantee" as antifragile compounding assets, work the [[outreach-pipeline]]
weekly (not just build it), and close the knowing-doing gap on discipline (the YouTube/Shorts leak).

## [2026-07-30] lint | Orphan sweep — reconnected all raw source nodes to the graph
Went through the vault's orphans (notes with no real inbound links) and fixed the ones that shouldn't be orphans.
- **Root cause found:** all **119 `raw/Processed/` source files floated as fully disconnected graph nodes** (e.g. "A full-length interview with Tucker Carlson The Economist"). Their `wiki/sources/` summaries existed but cited the raw file only as plain-text/backtick paths — never as `[[wikilinks]]` — so the graph never joined them (violating AGENTS.md "cite raw sources so the human can trace it back").
- **Fixed:** added a `**Raw clip:** [[…]]` wikilink from each summary to its raw file (85 matched by URL, 7 by title). The remaining 27 disconnected raws (8 near-duplicate stickman reclips, 5 karpathy/autoresearch repo fragments, 4 JHTV website scrapes, singles) were linked to their nearest existing summary/entity/bucket. **Result: 0 disconnected raw nodes, 0 broken links.**
- **Trivial strays:** deleted empty `Untitled.md`; linked orphaned `[[growth-plan]]` into the [[Job Search]] bucket.
- **Confirmed correct-as-orphans (by design, left untouched):** ~360 `crm/` person files (catalog-linked contact DB via `crm/index.md`), 33 `startup-tracker/` notes (gitignored, Obsidian `.base` frontmatter dashboard — not wikilinks), 9 `docs/superpowers/` plans/specs, plus `AGENTS.md`/`CLAUDE.md`/`log.md`/`autoresearch/` infra.
- **Weak-source weaving:** checked for near-leaf source summaries (≤1 real neighbor) — found none; every source already links ≥2 real pages, so no forced links added.
- **Flag for Cole:** the 8 stickman-animation reclips + 5 karpathy repo fragments + 4 JHTV page scrapes are genuine near-duplicates now clustered on their summary pages — prune them if you want a cleaner graph (left in place; deleting source captures is your call).

## [2026-07-30] lint | Deduplicated the raw stragglers (true duplicates only)
Followed up on the orphan sweep: checked the 27 reconnected stragglers for TRUE duplicates (same video/content), per "create sources only when needed."
- **Found the stickman cluster is 7 DISTINCT videos** (different YouTube IDs), not duplicates — kept all, they remain linked to [[stickman-animation-free-ai-tutorials]].
- **Deleted 3 true duplicates** (canonical original already held all their content — nothing unique to fold): `Making UNLIMITED Stickman Animations…FREE (reclip 2026-07-27)` (partial reclip of the same Zenn0009 video), `Obsidian Vault Deep Dive!…(reclip 2026-07-27)` (same video VaGpWWiHXm8 as the fuller original; reclip was a strict subset), and `karpathyautoresearch…automatically 4` (body byte-identical to the base README). Removed their now-dangling wikilinks from the summary pages first.
- **Result: 116 raw source files, 0 disconnected, 0 broken links.** The JHTV website scrapes (4 distinct pages) and karpathy repo fragments (distinct files) were NOT duplicates, so kept.

## [2026-07-30] query | Science of alcohol → sleep → dementia
Cole asked to learn the science of how alcohol affects sleep and in turn dementia. Researched + filed as two cross-linked concept pages.
- **[[glymphatic-system]]** — the brain's overnight waste-clearance drain (deep NREM opens the interstitial space ~60%, NE-gated, AQP4-dependent; clears amyloid-β/tau). Foundational/reusable. Sources: Xie 2013 *Science*, Nedergaard & Goldman 2020 *Science*, Nature Communications 2026 human validation.
- **[[alcohol-sleep-dementia]]** — the full mechanistic chain: alcohol suppresses REM/slow-wave sleep → less glymphatic clearance; heavy/binge alcohol *also* damages the plumbing directly (Lundgaard 2018, J-shaped dose effect, AQP4 mislocalization, GFAP astrogliosis); plus acetaldehyde/thiamine/Korsakoff. Kept the epidemiology nuance honest: the "moderate protects" J-curve (Sabia 2018 BMJ) is likely confounded; imaging + Mendelian-randomization (Topiwala 2022; PLOS Med 2022; eClinicalMedicine 2024) point to "no safe level" for brain structure, with clear harm at heavy/binge levels. Includes Cole-actionable timing guidance.
- Enriched [[memory-consolidation]] with a reciprocal link (deep sleep does double duty: consolidation + clearance); added both to the [[Neuro]] bucket cluster and index.md.

## [2026-07-30] query | Orders of kinetics (zero vs first order)
Explained reaction kinetics orders; filed [[reaction-order-kinetics]] (zero-order = flat amount/hr, saturated enzyme, no half-life, e.g. alcohol ~1 drink/hr; first-order = fixed %/hr, half-life, e.g. caffeine; Michaelis–Menten transition). Linked from [[alcohol-sleep-dementia]] and index.

## [2026-07-30] ingest | Introducing Claude Corps (Anthropic fellowship)
Ingested the Claude Corps announcement. Anthropic + [[codepath]] (employer of record) + Social Finance; paid 12-mo full-time in-person fellowship at US nonprofits, $85k + benefits, $150M / 1,000 fellows.
- **Timeline:** cohort 1 (Oct 2026 start) closed July 17; rolling apps now open for **Jan 2027** and **Aug 2027** starts.
- **Best fit for Cole (grad May 2027) = Aug 2027 cohort** (Jan 2027 lands mid-final-semester). Rolling → apply early. Eligibility clears easily.
- Filed source [[claude-corps]] summary + entity [[claude-corps]]; linked into [[Job Search]] bucket (third post-grad path competing with [[Fulbright]] + direct role), [[anthropic]] + [[fulbright-us-student-program]] (reciprocal), [[comp-targets]], index. Added decision + apply-early + build-CodePath/Anthropic-channel tasks (stub [[codepath]] entity flagged). Moved source to raw/Processed/.

## [2026-07-30] crm | Code the Dream (Claude Corps host) — value-first outreach drafted
Researched Code the Dream (Durham) for a pre-application [[claude-corps]] touch. Co-EDs: **Daisy Magnus-Aryitey** + Daniel Rearick. Created [[Daisy Magnus-Aryitey]] CRM record with a value-first, no-ask draft (Claude Corps deliberately kept out of the first email); added to crm/index + [[outreach-pipeline]] Tier 1; updated [[claude-corps-application]]. Next: confirm her direct email, then send.

## [2026-07-31] autoresearch | Nightly run — 2 heals on vault-state, 2 builds + 1 MODE B on night branch
**Git note:** Vault backup hooks had committed 75 commits to a detached HEAD (not on any branch); `origin/main` was stale at the 2026-07-24 JHTV fill. Tonight rescued those commits as `vault-state-2026-07-31` branch. Phase-1 heals committed there; Phase 2–4 on `autoresearch/night-2026-07-31`. Morning PR covers recovery + build.

**Phase 0 baseline:** HEALTH_DEBT=3 — `wiki/entities/codepath.md` (missing_from_index ×2) + `wiki/entities/anthropic.md` (stale_claim ×1).

**Phase 1 heals (vault-state branch):**
1. `codepath.md` → added to `index.md` catalog. Debt 3→1.
2. `anthropic.md` → added "point-in-time snapshot" label; changed "later flagship" → "then-flagship". Debt 1→0.

**Phase 2 build:**
- **Agent max:** Created [[claude-code-agent-teams]] concept page (peer vs sub-agent distinction, decision guide, tmux observability, orchestration spectrum). Enriched [[claude-code-subagents]] stub. Fills a dangling wikilink from 5+ pages.
- **Token max:** Created [[token-context-management]] concept page (CLAUDE.md sizing, compaction, PreCompact/PostCompact hooks, sub-agent isolation, CMA absorption). Added to index + Claude Mastery bucket; reciprocal link from [[claude-code-memory]].

**Phase 3 write-back:** Added ⏳ progress notes to Agent max + Token max in [[tasks/index]]. No build-introduced debt.

**Phase 4 MODE B:** Enriched [[agent-hub]] entity page — design philosophy, DAG model, vault-relevance table, and evaluation of when/whether to adopt for this vault.

## [2026-07-31] crm/outreach | Fulbright host outreach — CIIE.CO email bounced
`info@ciie.co` (host #3, IIMA Ahmedabad incubator) **BOUNCED**. The `@ciie.co` domain is stale — the org rebranded **CIIE.CO → IIMA Ventures**. Found + verified the live replacement on their own contact page (ahmedabad.iimaventures.com/contact-us): **`venturesfrontdesk@iima.ac.in`** (Tel +91 79 71524201; backup support form go.iimaventures.com/WebsiteForm). Updated [[fulbright/outreach]] (host #3 → RESEND, address-status table) and filed a resend task in [[tasks/index]]. Same #3 email body — just swap the address. cc: `ciie@iimahd.ernet.in` is a legacy ernet.in address, not used.

## [2026-08-01] autoresearch | Nightly loop — 2026-08-01

Phase 0: HEALTH_DEBT = 0, no pre-existing defects. Phase 1 fast-track lane empty tonight.
Phase 2: Built 2 skill files — `token-context-management` (4-lever quick-ref) + `orchestrate-agents` (decision ladder + pitfall table). Both complete the pending ⏳ progress notes for Token max + Agent max.
Phase 3: Marked Token max + Agent max done in `tasks/index.md`; moved to Done section. HEALTH_DEBT remains 0 (no build-introduced debt).
Phase 4: MODE B — created `wiki/concepts/agentic-automation-patterns.md` (fills dangling `[[agentic-automation-patterns]]` link from `claude-code-loops.md`; 5 patterns + anti-pattern table; web-grounded). Linked from `index.md` + `agentic-workflows.md`.
Phase 5: PR open → `autoresearch/night-2026-08-01` → `main`. No fast-track heals tonight.

## [2026-08-01] ingest | Conversation takeaways — conversational presence
Filed Cole's takeaways from a long morning conversation with Claude into the local profile.
New page [[conversational-presence]] (profile/, gitignored): his **operating model of people**
(subconscious-driven, self-focused, incentive-predictable; predictability useful+frustrating;
rarely blames individuals) and his **social growth front** (talk less, lead with curiosity, pivot
the spotlight, listen better) + four tools (half-second silence, excitement→questions, two-sentence
pitch, asking about others = his "quiet superpower"). Cross-linked to [[conscious-vs-subconscious]],
[[predictive-processing]], [[cognitive-biases]], [[neuroscience-of-behavior]], [[identity-led-goals]].
Reciprocal enrichments in [[cole]] (Values) and [[growth-plan]] (new lever 5b + Related).

## [2026-08-01] update | conversational-presence promoted to the synced wiki
Per Cole, moved [[conversational-presence]] from local-only `profile/` into `wiki/concepts/` (now
part of the synced graph). Added to [[index]] (Discipline & behavior change) and the [[Personal]]
bucket (new Relationships & presence line); reciprocal prose link added in [[conscious-vs-subconscious]]
("Cole's operating model of people"). Frontmatter retyped profile → concept.

## [2026-08-01] crm/research | FedTech direct-reach contacts
Cole asked for the best FedTech person to reach beyond [[Ian Senungwan Ryu]] (warm/ex-FedTech).
Researched fedtech.io/team → top pick **Iris Briancon (Head of Tech Transfer & Commercialization)**,
co-lead **Thomas B. Shiell (Director, Tech & Commercialization Strategy)** — both role-mirror Cole's
JHTV Capital Strategy work; door-opener **Ellen Erickson (Sr Mgr, Venture Relations)**. Play:
Ian flags internally → Cole reaches Iris/Thomas directly. Filed to startup-tracker/companies/fedtech.md.

## [2026-08-04] autoresearch | Nightly loop — 2026-08-04

Phase 0: HEALTH_DEBT = 0, empty pre-existing defect set. Phase 1 fast-track lane empty.
Regenerated `autoresearch/nightly-queue.md`. Note: the `main` branch boundary is disabled
in this cloud environment (harness scopes work to one branch → one PR), so no direct-to-main
heals — the clean baseline made that moot anyway.
Phase 2 (build): deepened `wiki/sources/build-sell-claude-code-course.md` from a 23-line
skeleton into a full **30-chapter map** (grounded in the raw transcript's Course Outline),
each chapter cross-linked to the vault page(s) that deep-dive it — the umbrella now navigates
the whole ~40-page Nate-Herk batch. (@cloud "deeper notes on course chapters" task, advanced.)
  ↳ Skipped: the `raw/assets/` 5CAST clip (wrongful-convictions podcast) — ingest is the
    @local lane's job by design ("scoped to stay out of the cloud lane"); flagged in the queue.
Phase 3 (self-heal, MODE A): HEALTH_DEBT already 0; no objective fix. Logged skip.
Phase 4 (MODE B): created `wiki/concepts/claude-code-worktrees.md` — git-worktree file
isolation for parallel Claude Code sessions/sub-agents (`--worktree`, `isolation: worktree`,
base-ref, `.worktreeinclude`, shared-`.git`). Web-grounded vs official docs. Fills the
"GitHub & Worktrees" course chapter I'd left unlinked; reciprocal links from
[[claude-code-agent-teams]], [[claude-code-subagents]], index, and the Claude Mastery bucket.
Phase 5: one morning PR (night branch → main). HEALTH_DEBT stays 0.

## [2026-08-04] crm/prep | R. Jacob Vogelstein (Catalio / Flourish)
Built Tier-1 networking-prep brief for cold LinkedIn outreach to **R. Jacob Vogelstein** (Co-Founder & MP,
[[catalio-capital|Catalio]]; neuroscientist-turned-VC; [[flourish|Flourish]] investor). Key insight: Flourish's
"core algorithm" thesis = the **IARPA MICrONS** program he ran → the outreach hook. Created [[Jacob Vogelstein]]
CRM record + `crm/prep/Jacob Vogelstein.md` (6-section brief + LinkedIn connection note + full message + a
learning-only cortex/hippocampus explainer for Cole). Added Tier-1 row to [[outreach-pipeline]]; updated
crm/index; reciprocated links from [[flourish]] + [[catalio-capital]]. Channel = LinkedIn (3rd-degree, no email).

## [2026-08-04] crm/prep + outreach | Joshua T. Vogelstein (Flourish cofounder, JHU)
Cole provided `jovo@jhu.edu` — which is **Joshua** (JHU BME prof + [[flourish|Flourish]] cofounder), not
brother **Jacob** (the Catalio VC prepped earlier). Flagged the mix-up; Cole chose to target **Joshua** (warmer
Hopkins-faculty tie via [[jhtv|JHTV]]). Built `crm/prep/Joshua Vogelstein.md` (6-section brief, hook =
fly-connectome-~10×-transformer → Flourish's efficiency bet), **created a Gmail draft** to jovo@jhu.edu
(subject "Hopkins student (JHTV) — your connectome work + Flourish", 20-min learn ask). Updated
[[Joshua Vogelstein]] CRM (email + prep link + next action), added Tier-1 `drafted` row to [[outreach-pipeline]],
updated crm/index. Follow-up ~Aug 14 if no reply.

## [2026-08-05] autoresearch night (run 1) | MODE B: test-driven-development concept page
Pure-maintenance night (Phase 0 selected no bounded @cloud build; HEALTH_DEBT already 0, no
objective self-heal). MODE B generative proposal: created [[test-driven-development]]
(wiki/concepts) — grounds the two existing dangling refs from [[ai-native-engineering-org]] +
[[running-ai-native-engineering-org]]. Angle = Fiona Fung's "Claude removes the test-writing
tax → TDD as the agentic control surface / executable spec"; ties to spec-drift +
[[adversarial-code-review]], [[mechanism-over-output]], and the frozen-evaluator parallel in
[[vault-autoresearch]]. Added reciprocal prose link in [[adversarial-code-review]], indexed under
"AI-native work & industry", linked from the [[Claude Mastery]] bucket.

## [2026-08-05] autoresearch (run 2) | Skill-max enrichment + agent-hub monitor + outreach-pipeline
Second nightly run. HEALTH_DEBT=0 baseline; no Phase-1 heals.
Phase 2: (1) substantially enriched [[claude-code-skills]] concept page — from sparse stub to full
reference covering skill anatomy, Skill Creator workflow, evals (grader types, QA loop), trigger tuning,
skills-vs-subagents table, anti-patterns, and vault skill inventory. (2) agent-hub standing monitor:
web-verified no new material (1.5k stars, no tagged releases); updated page with 2026-08-05 check.
Phase 3: Skill max progress note added; agent-hub task marked done and moved to Done.
Phase 4 (MODE B run 2): created [[outreach-pipeline]] concept page (tier structure, Monday batch
runbook, templates, reply-rate tracker plan, current pipeline state, auto-trigger design); indexed.

## [2026-08-05] crm/prep | Christy Wyskiel (head of JHTV) — meeting today
Her 15-min advice ask (sent 2026-07-29) landed → conversation TODAY (Wed Aug 5). Built confidence-forward
prep `crm/prep/Christy Wyskiel.md` (6 sections + a "why you have the high ground" opener). Core thesis: Cole
IS her mission — Baltimore kid (BCPS-servant parents) × works on her Capital Strategy team × founder-profile
(neuro/chem + Uship operator + AI builder). Refreshed her track record (174 companies, $378M rev, $3B+ VC,
UpSurge cofounder, Abell trustee) + confirmed contact `wyskiel@jhu.edu`. Ask = advice + stay-in-touch, NO job
ask. Updated CRM + [[outreach-pipeline]] (status → meeting). Post-meeting: thank-you <24h + log what she said.

## [2026-08-06] autoresearch night — Phase 2 build | skill-authoring-playbook
MODE (Phase 2, @cloud): created `wiki/concepts/skill-authoring-playbook.md` — the actionable
"how to write a skill that triggers reliably & stays lean" companion to [[claude-code-skills]].
Advances the Claude-Mastery cluster (Skill max / Train skills / Improve+general skills) with one
grounded page instead of three thin ones. Web-grounded in Anthropic's official Skill authoring
best practices (platform.claude.com, 2026): description-as-trigger-surface (third person, what+when,
key terms, pushy-against-under-triggering), progressive disclosure (metadata→SKILL.md→refs,
<500 lines, one level deep), degrees-of-freedom heuristic, eval-first Claude-A/Claude-B iteration,
anti-patterns. Reciprocal links added from [[claude-code-skills]], `index.md`, and the
[[Claude Mastery]] bucket. HEALTH_DEBT 0→0 (indexed + linked, no build debt).

## [2026-08-06] autoresearch night — Phase 3 write-back | tasks/index.md
Appended ⏳ progress notes (2026-08-06) to the three Claude-Mastery cluster items advanced by the
skill-authoring-playbook build (Train skills, Skill max, Improve+general). None marked done — all
are ongoing mastery goals; the page is a materially-advancing artifact, not completion.

## [2026-08-06] autoresearch night — Phase 4 MODE B | test-driven-development
Generative enrichment: created `wiki/concepts/test-driven-development.md`, filling a genuine
dangling link that TWO existing pages already reference ([[ai-native-engineering-org]] +
[[running-ai-native-engineering-org]]). Frames TDD in the agentic era — the test as the agent's
objective spec + spec-drift guardrail, the code-side twin of eval-first skill authoring
([[skill-authoring-playbook]]/[[evals-for-taste]]) and the vault's own HEALTH_DEBT ratchet.
Inbound links already reciprocal; added to index (AI-native work). HEALTH_DEBT 0.

## [2026-08-06] ingest | The Antichrist is Here: Story of Peter Thiel (Volksgeist)
Ingested `raw/assets/The Antichrist is Here Story of Peter Thiel.md` — a ~90-min left-critical video
essay. First political/tech-power domain in the vault; connected it into the existing AI-landscape
cluster rather than leaving it siloed. **Source page** [[antichrist-story-peter-thiel]] (flagged POV:
biographical spine corroborated, motive attribution is the creator's argument). **New entities**
[[peter-thiel]], [[palantir]], [[founders-fund]], [[paypal-mafia]], [[jd-vance]]. **New concept**
[[tech-authoritarianism]] (Thiel "capitalism > democracy" + Yarvin CEO-monarch + Land Dark Enlightenment) —
framed as the **dark mirror** of [[post-scarcity-and-meaning]]. **Enrichments (reciprocal):**
[[elon-musk]] (PayPal-Mafia origin + Thiel/Founders Fund upstream), [[openai]] (Founders Fund early
investor + Altman-as-mentee), [[post-scarcity-and-meaning]] (who-controls-the-abundance branch),
[[agent-security-risks]] (personal↔civilizational-scale surveillance). Updated `index.md` (Thiel-network
subsection under World & ideas; concept under Futures & meaning; source under World & ideas). Moved source
to `raw/Processed/`.

## [2026-08-07] ingest (batch of 3) | Ramp AI agents · BBC doomscrolling · Channel 5 carceral
Swept the inbox (3 clips). **New source pages:** [[ramp-ai-agents-every-step]], [[doomscrolling-attention-science-bbc]],
[[us-carceral-system-channel5-freleng]]. **New concepts:** [[build-for-future-models]] (Ramp's velocity/tech-debt
bet), [[doomscrolling-attention-science]] (harm = swipe-to-decide interaction, not short content; fix = context-limits),
[[mass-incarceration]] (values context under Cole's "useful/help others" half).
**Enrichments / connection pass:** upgraded [[fable-5]] from creator-rumor → **in-prod corroboration** (Ramp using it
as the frontier model) — a real freshness reconciliation; added Ramp as a customer instance on [[ai-native-engineering-org]]
+ [[future-of-work-claude-tag]] (@Inspect echo); added the context-limit worked example to [[environment-design]]; linked
the doomscroll page into the [[neuroscience-of-behavior]] hub; added two pointers into [[cole]] (attention-leak + values).
**Editorial call:** Channel-5 back-half conspiracy content (Epstein / Charlie Kirk / Israel / QAnon) **deliberately not
encoded** as fact per AGENTS.md; flagged in the source page. Updated index (batch note + entries). Moved all 3 to Processed.

## [2026-08-10] autoresearch | Night build — skill improvement + loops concept page

**Phase 0:** HEALTH_DEBT = 0; pre-existing defect set empty; no Phase-1 fast-track heals.

**Phase 2 — Build:**
1. **`vault-improve` SKILL.md improved** — applied [[skill-authoring-playbook]] 6-section checklist.
   Finding: Guardrails section was a partial duplicate of Invariants. Fix: removed the duplicate
   section, absorbed the one unique item (snapshot-reconciliation) into Invariant #1. File trimmed
   102→94 lines with no loss of coverage. Advances "Improve + general skills" @cloud task.
2. **[[skills-vs-subagents]] enriched** — stub (11 lines) expanded to a full concept page with
   decision table, context-economics rationale, concrete rubric, and escalation ladder (skill →
   sub-agent → team → CMA). Advances "Skill max" and "Train skills" @cloud tasks.

**Phase 3 — Write-back:** tasks/index.md updated with ⏳ progress notes for "Skill max" (trigger
tuning pass complete: all 11 vault skills pass) and "Improve + general skills" (vault-improve worked
example + skills-vs-subagents enrichment).

**Phase 4 — MODE B:** Created [[claude-code-loops]] concept page — the in-session `/loop` command,
distinct from [[claude-code-scheduled-tasks]]. Web-grounded: fixed vs. dynamic mode, 50-iteration
cap, July 2026 Anthropic vocabulary (/goal /loop /schedule taxonomy). Fills the dangling wikilink
from [[overview]] and [[claude-code]]. HEALTH_DEBT = 0 after all changes.

**Phase 5 — PR:** opened autoresearch/night-2026-08-10 → main.

## [2026-08-07] config | AutoResearch/self-heal cadence: daily → weekly
Too many `autoresearch/night-*` branches accruing (13 merged + 1 open as of today). Added a **weekly
cadence gate** to `autoresearch/program.md`: scheduled/unattended runs execute the full loop **only on
Sunday (ET)**; other nights are a clean no-op (no branch, no PR) even if a session spawns. **Manual runs
(the `vault-autoresearch` skill / "run autoresearch") are exempt** and still run any day. Net: ~1 night
branch/week instead of ~7. Note: the daily *cloud trigger* itself could not be isolated via the schedule
tool (the routines API returned only the spawned one-shot PR-babysitter jobs; cursor paginated in a loop),
so the program.md gate is the enforcement point — Cole can also flip the routine to weekly at
claude.ai/code/routines to stop the off-day spawn entirely. 13 merged night branches queued for cleanup
(pending Cole's go).

## [2026-08-10] doc | JHTV Second Brain — Vision & Handoff
Brainstormed + wrote the long-term vision / handoff document for Cole's [[vc-matching-second-brain|VC-matching
tool]] as his internship ends (handoff to coworker Justin; to be discussed with Stewart & Oliver). Saved to
`docs/JHTV-Second-Brain-Vision-and-Handoff.md`. Spine: the tool = the **capital-matching engine** behind
Oliver's internal "Studio Portal" (system of record), alongside Justin's mentorship/Programs matcher. Adds
the **Translational Funding** pillar + the TF→MII/SBIR→seed→A escalator; two data upgrades (PitchBook API for
live deals; live portal data to keep tech/firm profiles current + exclude just-licensed techs); the
stated-vs-revealed ("portfolio does the most work") scoring principle; internal + external firm-view designs
(grounded in Cole's Notion/Claude-artifact mockups, read via the browser). Anchor use case throughout: the
team walking into a firm/tech meeting knowing what to say. Linked from [[vc-matching-second-brain]], the
[[JHTV]] bucket, and index. Draft — pending Cole's review before a copy goes to the tool repo.

## [2026-08-10] journal | Senior year, confidence, and not knowing what's next
New entry [[2026-08-10 - senior-year-confidence-and-whats-next]]. Cole heading into senior
year — excited and overwhelmed at once; doesn't know what's next but believes he spent his
time/energy in the right places and is confident it leads somewhere great; wants to *keep*
that self-confidence. Grounded the response in [[identity-led-goals]] (confidence rests on
accumulated behavioral evidence, and the Erin-Meryl caveat: anchor it in identity/behavior,
not single outcomes), tied to the live "what's next" forks — [[fulbright-us-student-program]],
[[outreach-pipeline]], [[claude-corps]], and the 5-year-plan talk with [[Stewart Neifart|Stew]].
Referenced the prior [[2026-07-28 - caffeine-social-and-golf-anger]] outcome-vs-self-worth thread.
Added to journal/index.

## [2026-08-18] job-search | Science-commercialization / venture-building lane
Cole loved the [[capital-strategy|JHTV Capital Strategy]] work but can't stay post-grad; he's in contact
with **Activate**'s chief of staff (a science→company fellowship like his summer job). Built a matching
target lane in [[outreach-pipeline]]: 10 orgs that help early-stage science cross the valley of death
(fellowships, venture creation, incubators, non-dilutive funders). Web-researched named, profile-matched
contacts for the starred ones — **Nucleate DMV / Raygan Murray** (JHU, warmest), **IndieBio / Mohan Iyer**
(Duke BME), **Flagship / Yinan Liu** (JHU→Associate), **ARCH / Sabah Oney** (warm Duke alum), **ARPA-H /
Kimberley Steele** (ex-JHU, advice-only); The Engine held pending a warm entry. Ties to [[five-year-plan]]
(operator-first, health/bio/AI, science→capital) and [[Job Search]].

## [2026-08-18] ingest | Big Think / Arthur Brooks — phone addiction vs. flow
Ingested [[phone-addiction-flow-arthur-brooks]] (channel: Big Think). Layered a **happiness/meaning**
frame on the existing attention-science + discipline clusters. New: person [[arthur-brooks]]; concepts
[[tech-addiction]] (phone as a literal [[temporal-discounting|dopamine]] hijack — the "once every 5 min"
addiction test, the emotional-numbing role, and the recovery→prevention protocol: tech-free
times/zones/fasts, grayscale, notifications-off) and [[flow-state]] (Csikszentmihalyi; **boredom is the
doorway** — tech-driven boredom-aversion is why flow is getting rarer). Enriched
[[temporal-discounting]] (dopamine = anticipation-of-reward, hijacked), [[doomscrolling-attention-science]]
(named it the sibling page; both reach the "monkey mind"), [[environment-design]] +
[[how-to-build-discipline]] (added the phone protocol), and the [[neuroscience-of-behavior]] hub. Wired
into the [[Personal]] and [[Neuro]] buckets. Updated index; moved source to Processed.

## [2026-08-18] ingest | Relentless (joinrelentless.com) — job-search service, flagged for Q&A
Cole flagged this one to **remember for questions.** Ingested 3 "Relentless Reviews" testimonials
([[relentless-review-roger-wyatt]] +$60K Director of Eng, [[relentless-review-yasmin-endassa]] offer while
running her business, [[relentless-review-yanis-romero]] +$155K in 6 weeks) and built the reference entity
[[relentless]] — a **done-for-you executive job-search service** (resume/positioning, direct recruiter +
hiring-manager outreach, interview prep, calendar management; "applying online is only ~10% of the work").
Flagged the outcomes as marketing/survivorship bias; noted founder is referred to as "her" + coach
**Kareem**. Positioned as the paid mirror of Cole's own [[outreach-pipeline]] + [[outreach-kit]] (added a
reciprocal note there), and as **market intel, not a new-grad fit** — wired into the [[Job Search]] bucket.
Updated index; moved 3 sources to Processed.

## [2026-08-18] job-search | Duke commercialization angle + TIME incubators triage
Cole flagged TIME's "Best Incubators & Accelerators 2026" — triaged in [[outreach-pipeline]] (it's a GENERAL
list; kept the NY/DC/MD + science-capable cut as employer targets; **dropped FastForward@JHU as a reach — his
own org**, talking point only). New distinctive angle he wants: reach **Duke's commercialization ecosystem** to
learn AND offer how JHTV's success could influence change at Duke (he's a Duke student who worked inside JHTV, a
top-10 incubator). Named targets: **[[Doug Speight]]** (his close professor + Duke I&E fellow / serial founder /
ex-ED American Underground = warmest entry), **Jeff Welch** (Dir. New Ventures, Duke OTC = peer function),
**Robin Rasor** (AVP, Duke OTC = the Duke analog of [[Christy Wyskiel]]). Enriched Doug Speight's CRM.

## 2026-08-19 — Networking prep: Natasha Feshbach (Activate — Chief of Staff, Fellowship)
Ran `networking-prep` for Cole's warm intro call with **Natasha Feshbach, Chief of Staff, Fellowship at
[[activate]]** (family-friend referral). *(First research pass targeted the wrong person — Caitlin Cutter,
the CEO-side COS; corrected to Natasha, who Cole named.)* Researched Activate (2-yr, non-dilutive, equity-
free, $300K+, PhD hard-tech founders; 5 communities; Cyclotron Road roots; 346 scientists→276 cos) and
pinned Natasha's real vantage: rose through **fellowship operations**, **ran the NY community ~3 yrs**;
Yale enviro/food-justice/climate-comms background (mission-driven, not science-PhD or finance). Built the
brief around Cole's ask: **learn the fellowship + compare/contrast to JHTV** (IP/equity, scope, stage,
funder-role, sector, duration table), with the **NYC overlap** (she ran Activate NY, Cole's target city).
Created **[[Natasha Feshbach|prep]]** + CRM record; entity **[[activate]]**; added to [[outreach-pipeline]].

## 2026-08-19 — Natasha Feshbach call done → confirmed resource
Cole's intro call with **[[Natasha Feshbach]]** (Chief of Staff, Fellowship @ [[activate]]) happened and
the **thank-you note went out**. Outcome: **she's a confirmed job-search resource** — agreed to flag
fitting roles (Activate or portfolio) + point Cole to others. Cole's commitments: apply to an Activate
**internship**; forwarded the fellowship to [[Stewart Neifart]] as a destination for Hopkins spinouts.
Updated her CRM record + [[outreach-pipeline]] (status `nurtured`, ⭐resource). Re-engage **spring 2027**;
open decision = **climate-hardtech vs. health/bio** fork before asking her to point at portfolio companies.

## 2026-08-20 — Ryan Berger call (best yet) + CRM: Ryan, Hugo, Natasha as job-search assets
Cole's call with **[[Ryan Berger]]** (Head of Ops @ [[ply]], **Justin's brother**) was his **most
successful yet** — Ryan: **"I'd love to hire you,"** blocked only by **timeline** (May-2027 grad vs.
short small-company hiring windows). Excited to connect Cole to people + be an ongoing asset;
**follow-up next week** to strategize. Uship internal-OS build landed as peer credibility. Created CRM
records + pipeline rows for **[[Ryan Berger]]** (⭐advocate) and **[[Hugo]]** (⚠️stub — mentor who hires
for VC/startup, Mon 12pm ET call; needs last name/company); confirmed **[[Natasha Feshbach]]** in CRM.
New entity **[[ply]]**. All three now queryable in [[outreach-pipeline]] Lane 0 as active assets.

## [2026-08-20] ingest | Duke P&N — Graduation with Distinction (GwD)
Webclip of Duke Psychology & Neuroscience GwD program page (Psych + Neuro tracks). Cole's
[[marsh-memory-lab]] research is his GwD thesis. New pages: source summary [[gwd-psychology-program]]
+ operational tracker [[gwd-thesis-pathway]]. Enriched [[psy-394-marsh-lab]] (thesis link + course-
sequence flag + key dates), [[marsh-memory-lab]] (GwD status), coursework [[coursework/index|index]],
[[Duke]] bucket, and root index.md. **Hard deadline surfaced: GwD application due Nov 9, 2026.**
Open flag: RIS sequence — GwD wants PSY 493→495, currently logged as PSY 394 (confirm w/ Joyce/Marsh).
Source moved to raw/Processed/.

## [2026-08-26] ingest | fMRI / Functional Neuroimaging (NEUROSCI 382) — syllabus + Weeks 1–5
Cataloged Cole's Fall 2026 Functional Neuroimaging class from 9 provided items: the
[[fmri-syllabus-fall2026|syllabus]], Week 1 lecture deck ([[fmri-week1-lecture-intro]]), textbook
[[huettel-ch1-intro-to-fmri|Ch 1]] & [[huettel-ch2-mri-scanners|Ch 2]] (scanned PDFs OCR'd via two
parallel subagents), and Weeks 2/3/5 lab handouts ([[fmri-lab1-neuroanatomy]],
[[fmri-lab2-kspace-contrast]], [[fmri-lab3-preprocessing]]). New concept cluster: [[mri-physics]],
[[mri-contrast]], [[k-space]], [[bold-signal]], [[fmri-preprocessing]], [[fmri-glm-analysis]],
[[mni-space]], [[neuroanatomy-landmarks]]. New entities: [[spm]], [[biac]], [[huettel-fmri-textbook]].
New CRM: [[Tobias Overath]] (prof), [[Hector Sanchez Melendez]] (TA), [[Jim Voyvodic]] (guest).
Rewrote the [[fmri]] hub with full course info, a complete reading/lab/exam/project tracker, and key
dates. Updated [[coursework/index]], [[Duke]] + [[Neuro]] buckets, root index.md (+ dated callout),
crm/index.md. The 486 MB SPM lab dataset (`bia5_20105_*`, = the finger-tapping analysis) is referenced
by its Downloads path, NOT copied into the vault. Source docs (syllabus/lecture/chapters/labs) copied
to raw/Processed/. Minor flag: lecture deck template says "Thursdays"/"SPM25" while the syllabus says
Tuesdays and labs were written for spm12 — syllabus treated as authoritative, version discrepancy noted.

## [2026-08-26] ingest | CHEM 210D — Modern Applications of Inorganic Chemistry (syllabus + Unit 1)
Cole handed over the first batch of CHEM 210 materials (Prof. [[Charlie Cox]], Fall 2026): syllabus + Unit 1
(59-slide lecture deck, unit overview handout, Bohr-model derivation handout). **Connection-first:** corrected the
old "Inorganic Chemistry II" misnomer and **renamed** the stub `coursework/inorganic-chemistry-2.md` →
[[chem-210]] (git mv; updated the 2 inbound links in [[coursework/index|coursework index]] + [[Duke]] bucket).
Built the hub [[chem-210]] (info, grading 50/35/15 + resurrection quizzes, HW tracker, exam dates Oct 1 / Nov 12 /
Dec 9) and three atomic Unit-1 knowledge notes: [[chem-210-nuclear-chemistry]], [[chem-210-quantum-atomic-structure]],
[[chem-210-periodic-trends]]. Source summaries: [[chem-210-syllabus-fall-2026]], [[chem-210-unit1-nuclear-quantum]],
[[chem-210-bohr-model-handout]]. Enriched [[reaction-order-kinetics]] with a reciprocal link (radioactive decay =
the pure first-order case). Updated root index.md (ingest callout + Concepts + Sources sections) and the [[Duke]]
knowledge cluster. HW deadlines live in the [[chem-210]] tracker (not `tasks/index.md`, which is vault-system-only).
4 source PDFs moved to raw/Processed/. Open flags: confirm Cole's discussion section (10D–18D); HW points 10 vs 12
(syllabus vs Unit 1 handout); [[Charlie Cox]] left as a stub link (worth a CRM entry — possible Duke recommender).
"This is a start of all the data" — later units + problem sets to follow.

## [2026-08-26] ingest | CHEM 210 Discussion I — Stoichiometry Review (prereq)
Cole's Discussion I worksheet (prereq review from Chem 101/110 — stoichiometry, limiting reagent, ideal gas law,
formula-from-mole-ratio). Worked all three problems with him and filed the methods + solutions as
[[chem-210-prereq-review]] (linked from [[chem-210]] material section + root index). Answers: 1a) 0.370 L H₂ + 2.06 g
Al left; 1b) 19 soda cans; 2) MnCl₄; 3) ≈45 mL O₂. Flagged prereq (Unit 0), distinct from the first graded content
([[chem-210-nuclear-chemistry|Unit 1: Nuclear]]). Source moved to raw/Processed/.

## [2026-08-26] ingest | NEUROSCI 206L — Introduction to Systems Neuroscience (syllabus + Week 1)
Cole handed over NEUROSCI 206L materials (Profs [[Leonard White]] & [[Henry Yin]], Fall 2026) ahead of his Wed
afternoon class. **Connection-first:** the existing "Introduction to Brain Systems" stub was this course — corrected the
name and **renamed** `coursework/intro-brain-systems.md` → [[neurosci-206]] (git mv; updated 3 inbound links: [[coursework/index]],
[[Duke]] bucket, and [[neuroanatomy-landmarks]] which already cross-referenced it). Built the hub [[neurosci-206]]
(TBL format, 60/40 individual/team grading, drop policy, 15-week sensory→motor schedule, midterm Oct 14 / final Dec 13,
Lt + Sylvius = free-for-Duke via Canvas) and the Wk1 knowledge note [[neurosci-206-human-neuroanatomy]] (human-brain
anatomy foundations). Source summaries: [[neurosci-206-syllabus-fall-2026]], [[neurosci-206-first-class-human-brain]].
Reciprocated the fMRI tie — [[neuroanatomy-landmarks]] ↔ 206 share gross anatomy. Updated root index.md (callout +
Concepts + Sources) and the [[Duke]] knowledge cluster. Also answered Cole's live questions (Lt via Canvas Week-0 module;
readings = Neuroscience 7e / used 4th–6th ed ~$15 / Oxford Insight; Wk1 = Neuroanatomy Appendix; do the Getting-to-Know-You
survey for team assignment). Open flags: confirm Cole's lab day (Thu vs Fri); Profs White/Yin left as stub links (possible
CRM entries + recommenders). 2 source PDFs moved to raw/Processed/. More weeks to follow.

## [2026-08-27] networking-prep | Will Lipman (Transcend Therapeutics)
Stew connected Cole with **Will Lipman** — UNC neuroscience grad, **JHTV Commercialization Fellow '24**
(one year ahead of Cole), now **Associate, Clinical Operations at [[transcend-therapeutics|Transcend
Therapeutics]]** (NYC). Ran the vault-native networking-prep: loaded [[cole]], [[five-year-plan]],
[[outreach-kit]], [[Stewart Neifart]]; web-researched the company. **Headline: Transcend was acquired by
Otsuka for $700M + up to $525M milestones (closed June 2026)** — 3 months after Will joined; a live
science→capital→exit that mirrors Cole's operator-first health/bio lane. Wrote deep brief
`crm/prep/Will Lipman.md`; created CRM record `crm/Will Lipman.md` and entity page
[[transcend-therapeutics]] (TSND-201/methylone = non-hallucinogenic neuroplastogen for PTSD; IMPACT-1
Phase 2 met primary endpoint, JAMA Psychiatry Feb 2026; FDA Breakthrough Therapy Jul 2025; Phase 3
recruiting). Added Lane 0 row to [[outreach-pipeline]] (queued, no job ask), plus crm/index + root index
entries. Ask = advice + keep-warm for 2027 recruiting.

## [2026-08-30] autoresearch | AutoResearch night (Sunday weekly run)
Full six-phase loop on branch `autoresearch/night-2026-08-30`. **Phase 1 build:** ran the
[[skill-authoring-playbook]] checklist against the `networking-prep` skill (2nd worked example on
[[skill-audit-worked-example]]) — one safe fix: removed a baked, stale-prone lane snapshot from
Step 1 that violated the skill's own Freshness principle; lane now read live from `five-year-plan.md`.
Advances *Improve + general skills* ([[Claude Mastery]]). **Phase 3 self-heal:** drove HEALTH_DEBT
16→0 — fixed the `startup-radar` orphan (reciprocal links from [[outreach-pipeline]] + [[Job Search]])
and indexed 5 missing pages ([[startup-radar]], [[skill-audit-worked-example]], [[claude-api]],
[[activate]], [[ply]]). **Phase 4 MODE B:** built the [[mcp]] stub (14 lines) into a full hub —
host/client/server architecture, the tools/resources/prompts primitives, stdio + Streamable HTTP
transports, and a web-grounded 2026-07-28 spec snapshot (stateless core, Tasks/MCP Apps/EMA
extensions, OAuth/CIMD); promoted its index entry from a "supporting tools" mention. All on the branch
→ one morning PR. Baseline debt 16 → final 0.
