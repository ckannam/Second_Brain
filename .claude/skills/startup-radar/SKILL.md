---
name: startup-radar
description: Use to discover and triage newly-funded startups matching Cole's job-search lanes. Sweeps free public sources, lane-filters to health-bio-ai and ai-infra, dedupes against existing company notes, and writes new startup-tracker entries. Triggered when Cole says "run the startup radar" or "weekly startup discovery".
---

# Startup Radar

You are Cole's weekly startup discovery engine. You sweep free public surfaces, filter to his target lanes, dedup against what he already knows, and write new company notes into `startup-tracker/companies/`.

## Inputs

- `TODAY`: today's ISO date (`YYYY-MM-DD`). Use the `currentDate` in your context if available; otherwise ask.
- Vault root: `/Users/colekannam/Desktop/Second Brain`

## Step 1 — Sweep sources (free surfaces only)

Fetch each of the following. Use `WebFetch` / `WebSearch` as needed. Skip any that require a paid account.

### HN "Who's Hiring" (monthly thread)
1. Fetch: `https://hn.algolia.com/api/v1/search?query=Ask%20HN%20Who%20is%20hiring&tags=story`
2. Find the newest thread (highest `created_at` or largest `objectID`). Note its `objectID`.
3. Fetch comments: `https://hn.algolia.com/api/v1/items/<objectID>`
4. Scan top-level comment texts for company names, locations, and role descriptions.

### YC Jobs directory
- Fetch: `https://www.ycombinator.com/jobs`
- Extract company name, location, role tags.

### VC portfolio job boards
Fetch each board and extract company listings:
- `https://jobs.sequoiacap.com`
- `https://portfolio-jobs.a16z.com`
- `https://jobs.indexventures.com`
- `https://jobs.greylock.com`

### Harmonic Hot 25
- Fetch: `https://harmonic.ai/hot-25-startups`
- Extract company names and any funding/location shown.

### Founders You Should Know
- Fetch: `https://foundersysk.com`
- Extract featured companies.

### Startups.gallery news
- Fetch: `https://startups.gallery/news`
- Extract recently-featured companies.

### Public Substack newsletters
Search for recent issues (use `WebSearch`):
- "Next Play Substack startup" — recent issues
- "Early Days Substack startup" — recent issues
- "a16z Build Substack" — recent issues
Extract company names mentioned in hiring/funding context.

**Do NOT use:** Ramp vendor data, full Harmonic (paid), or any source requiring authentication.

## Step 2 — Extract fields

For each company found, note:
- `company`: proper name
- `location`: city/state or "remote" if stated; empty string if unknown
- `careers_url`: direct link to careers page if visible
- `funding`: round + amount + date + lead investor if shown; empty string if not shown
- `source`: which source surface (e.g. `hn-who-is-hiring`, `yc-jobs`, `sequoia-jobs`, `a16z-jobs`, `index-jobs`, `greylock-jobs`, `harmonic-hot-25`, `foundersysk`, `startups-gallery`, `substack-next-play`, `substack-early-days`, `substack-a16z-build`)

## Step 3 — Lane filter

Keep only companies that fit `health-bio-ai` or `ai-infra`. Drop everything else.

**Lane definitions:**
- `health-bio-ai`: biotech, pharma, clinical AI, health-tech, drug discovery, diagnostics, medical imaging, genomics, life-science tooling — any intersection of biology/medicine and AI.
- `ai-infra`: AI agents, memory systems, developer tooling for AI, LLM infrastructure, MLOps, training/inference platforms, AI orchestration — tools that AI builders use.
- `other`: everything else (robotics, climate, fintech, SaaS, etc.) — **drop these**.

**Geo fit assignment** (assign based on `location` field):
- `strong` — NYC, DC, Baltimore, or surrounding metro (Northern Virginia, Maryland)
- `ok` — Boston, Philadelphia, or other East Coast hubs
- `remote` — explicitly "remote" or "fully distributed"
- `weak` — SF, Bay Area, London, or anywhere else; also use `weak` when location is unknown

## Step 4 — Dedup

Read all existing notes: `startup-tracker/companies/*.md` (skip `_template.md`).

For each, parse the frontmatter fields `company` (exact name), `website`, and `careers_url`.

Skip any candidate company if:
- Its name matches an existing `company` field (case-insensitive), OR
- Its domain (from `careers_url` or `website`) matches an existing note's domain, OR
- The existing note has `status: parked` or `status: passed` — still skip; don't re-surface dismissed companies.

## Step 5 — Write new company notes

For each company that passes dedup, create `startup-tracker/companies/<kebab-case-name>.md` by copying `startup-tracker/companies/_template.md` and filling in:

```yaml
company: "<Company Name>"
website: "<homepage URL if known, else empty>"
careers_url: "<careers URL if found, else empty>"
lane: "<health-bio-ai or ai-infra>"
location: "<city/state or empty>"
geo_fit: "<strong|ok|remote|weak>"
status: discovered
funding: "<funding string if known, else empty>"
source: "<source surface>"
discovered: "<TODAY>"
angle: "<one-sentence first-pass angle: what hook Cole has — product familiarity, lane alignment, JHTV connection, etc.>"
```

Leave `person`, `contact`, `last_touch`, `replied`, `next_action`, `aliases` as empty/false defaults.

Add one interaction-log line:
```
- <TODAY> discovered via <source>
```

Filename: kebab-case of the company name (e.g. `chai-discovery.md`, `prime-intellect.md`).

## Step 5.5 — Contact enrichment

For every new company note, find the single best outreach target and fill the `person` and `contact` fields. Do this before reporting.

**Who to target (in priority order):**
1. **Warm path first** — check `crm/*.md` for anyone who works at or is connected to this company. If found, set `person: "[[Their Name]]"` and `contact: "warm intro via [[Their Name]]"`.
2. **Early-stage (Seed / Series A, team < ~30)** — target the CEO or a cofounder directly. They read their own email and make hiring calls.
3. **Series B+ with engineering team** — target the Head of Engineering, VP Engineering, or a CTO. Avoid generic HR.
4. **No individual found** — use the company's general hiring email (e.g. `jobs@company.com`, `careers@company.com`) or a careers page URL as `contact`.

**How to find them (use WebSearch and WebFetch):**
- Search `"[Company] CEO" OR "[Company] founder" site:linkedin.com` for name.
- Search `"[Company] [Name] email"` or `"[Name] @[domain]"` for a direct address.
- Check the careers page (`/jobs`, `/careers`) for a posted hiring email address.
- For YC companies: fetch `https://www.ycombinator.com/companies?q=[company]` — founders are listed.
- GitHub profile pages sometimes contain email addresses.
- If only a name is findable (no direct email), set `contact: "linkedin.com/in/[slug]"` or `contact: "[first]@[domain] (pattern — verify)"`.

**Do NOT invent email addresses.** If the domain pattern is guessable from other public sources, mark it `(pattern — verify)`. If nothing is findable, leave `contact` empty and note `"no public contact found"` in the interaction log.

**Update the note** — edit `person` and `contact` frontmatter fields in place, and append to the interaction log:
```
- <TODAY> contact research: [what was found or "no public contact found"]
```

## Step 6 — Report shortlist in-session

After writing notes, print a ranked shortlist in this format:

```
## Startup Radar — <TODAY>

### Strong geo + health-bio-ai (reach soonest)
1. **<Company>** — <location> — <funding snippet> — <angle>
   Source: <source> | <careers_url>

### Strong geo + ai-infra
...

### Remote + health-bio-ai
...

### Remote + ai-infra
...

### Weak geo (FYI — low priority)
...

Total new notes written: N
```

Then ask Cole:
> "Want me to push this shortlist to iMessage?"

If yes, deliver via AppleScript (same pattern as concert-digest):
```
osascript /Users/colekannam/.claude/concerts/send.scpt "<shortlist text>"
```
Keep the iMessage version tight — company name, location, one-line angle, source. Plain text, no markdown.

## Step 7 — Validate

Run the validator to confirm all new notes are schema-valid:

```bash
python3 startup-tracker/validate.py
```
Run from the vault root (the `Vault root` input above), so the path stays consistent with
Steps 4–5 and portable if the vault moves.

Expected output: `OK: N company notes valid`

If validation fails, read the error messages, fix the flagged notes (usually a missing required field or bad enum value), and re-run until clean.

## Rules

- Never invent funding figures, locations, or careers URLs. If a field isn't shown in the source, leave it empty.
- Do not write notes for `other`-lane companies, even if they look interesting.
- Do not re-surface `parked` or `passed` companies.
- Angle guesses should be brief (one sentence) and honest — note when there's no clear hook yet.
- The `startup-tracker/` folder is gitignored; new company notes are local-only. Do not commit them.
- Only the skill file itself (`.claude/skills/startup-radar/SKILL.md`) is tracked in git.
