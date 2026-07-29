# Startup Tracker Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an end-to-end startup discovery → outreach → logging → analytics engine for Cole's job search, rendered as a native Obsidian **Bases** dashboard over a folder of one-note-per-company files, fed by a new `startup-radar` Claude skill.

**Architecture:** A local-only, gitignored `startup-tracker/` folder holds one markdown note per company (frontmatter = data) plus a `Startup Tracker.base` dashboard. A `startup-radar` skill sweeps free source surfaces, lane-filters, dedupes, and writes new company notes. The outreach/logging/analytics half reuses the existing `outreach-kit` / `networking-prep` / `outreach-pipeline` machinery.

**Tech Stack:** Markdown + YAML frontmatter, Obsidian Bases (native core plugin), Python 3 (stdlib only) for a schema validator, a Claude Code skill (SKILL.md), Gmail MCP for drafts.

## Global Constraints

- **Privacy:** `startup-tracker/` and `crm/` are **gitignored**. Company notes, the `.base`, and the validator are **local-only, never committed**. Only committable artifacts: the `.gitignore` change, `.claude/skills/startup-radar/`, and files under `docs/`.
- **Frontmatter enums (exact):** `lane` ∈ {`health-bio-ai`, `ai-infra`, `other`}; `status` ∈ {`discovered`, `triaged`, `enriching`, `reach-now`, `contacted`, `replied`, `meeting`, `nurtured`, `parked`, `passed`}; `geo_fit` ∈ {`strong`, `ok`, `remote`, `weak`}.
- **Dates:** ISO `YYYY-MM-DD`.
- **No paid APIs** (Ramp vendor data, full Harmonic) — free/public source surfaces only.
- **No auto-send** — all outreach is Gmail drafts Cole reviews and sends.
- **Company-centric scope** — warm/relationship networking (Lane 0, PIKE roster) stays in `crm/outreach-pipeline.md`; the tracker cross-links to `crm/` person records but does not absorb them.
- Filenames in `companies/` are `kebab-case` of the company name.

---

### Task 1: Scaffold the folder + gitignore

**Files:**
- Modify: `.gitignore`
- Create: `startup-tracker/README.md`
- Create: `startup-tracker/companies/_template.md`

**Interfaces:**
- Produces: the `startup-tracker/` tree and the canonical company-note template all later tasks copy.

- [ ] **Step 1: Add the gitignore rule.** Append to `.gitignore`:

```
# Startup tracker — outreach/contact data, local-only (never sync)
startup-tracker/
```

- [ ] **Step 2: Verify the ignore works.**

Run: `mkdir -p startup-tracker/companies && touch "startup-tracker/companies/x.md" && git check-ignore -v "startup-tracker/companies/x.md" && rm "startup-tracker/companies/x.md"`
Expected: prints a `.gitignore:<line>:startup-tracker/` match (confirms ignored).

- [ ] **Step 3: Create the company-note template** at `startup-tracker/companies/_template.md`:

```markdown
---
company: ""
aliases: []
website: ""
careers_url: ""
lane: ""          # health-bio-ai | ai-infra | other
location: ""
geo_fit: ""       # strong | ok | remote | weak
status: discovered # discovered|triaged|enriching|reach-now|contacted|replied|meeting|nurtured|parked|passed
funding: ""
person: ""
contact: ""
angle: ""
source: ""
discovered: ""
last_touch: ""
replied: false
next_action: ""
---
# <Company>

## Interaction log
- <YYYY-MM-DD> discovered via <source>
```

- [ ] **Step 4: Create `startup-tracker/README.md`** documenting: the folder is local-only; the schema (copy the enums from Global Constraints); how to run the radar ("run the startup radar"); and that the dashboard opens via `Startup Tracker.base`.

- [ ] **Step 5: Commit the tracked change only.**

```bash
git add .gitignore
git commit -m "chore: gitignore startup-tracker/ (local-only outreach data)"
```
(Note: `startup-tracker/` files are intentionally NOT committed.)

---

### Task 2: Frontmatter schema validator

**Files:**
- Create: `startup-tracker/validate.py`

**Interfaces:**
- Produces: `validate.py`, runnable as `python3 startup-tracker/validate.py`; exits non-zero and prints per-file errors if any company note violates the schema. This is the automatable test harness for Tasks 3 and 6.

- [ ] **Step 1: Write the validator** at `startup-tracker/validate.py`:

```python
#!/usr/bin/env python3
"""Validate startup-tracker company notes against the schema."""
import sys, glob, re, os

LANE = {"health-bio-ai", "ai-infra", "other"}
STATUS = {"discovered","triaged","enriching","reach-now","contacted",
          "replied","meeting","nurtured","parked","passed"}
GEO = {"strong","ok","remote","weak"}
REQUIRED = ["company","lane","status","geo_fit","source","discovered"]
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def parse_fm(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m: return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line: continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip().strip('"')
    return fm

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    files = [f for f in glob.glob(os.path.join(base,"companies","*.md"))
             if not os.path.basename(f).startswith("_")]
    errors = []
    for f in files:
        fm = parse_fm(open(f).read())
        name = os.path.basename(f)
        if fm is None:
            errors.append(f"{name}: no frontmatter"); continue
        for k in REQUIRED:
            if not fm.get(k): errors.append(f"{name}: missing/empty '{k}'")
        if fm.get("lane") and fm["lane"] not in LANE:
            errors.append(f"{name}: bad lane '{fm['lane']}'")
        if fm.get("status") and fm["status"] not in STATUS:
            errors.append(f"{name}: bad status '{fm['status']}'")
        if fm.get("geo_fit") and fm["geo_fit"] not in GEO:
            errors.append(f"{name}: bad geo_fit '{fm['geo_fit']}'")
        if fm.get("discovered") and not DATE.match(fm["discovered"]):
            errors.append(f"{name}: bad discovered date '{fm['discovered']}'")
    if errors:
        print("\n".join(errors)); print(f"\n{len(errors)} error(s)"); sys.exit(1)
    print(f"OK: {len(files)} company notes valid"); sys.exit(0)

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Create a deliberately-broken sample** to prove the validator catches errors. Create `startup-tracker/companies/_bad_sample.md` with `lane: nonsense` and no `status`.

- [ ] **Step 3: Run the validator; verify it FAILS on the bad sample.**

Run: `python3 startup-tracker/validate.py`
Expected: prints `_bad_sample.md: bad lane 'nonsense'` — wait, `_`-prefixed files are skipped. Rename the check: temporarily copy it to `companies/zzbad.md`, run, expect FAIL, then delete `zzbad.md` and `_bad_sample.md`.

- [ ] **Step 4: Run the validator on just the template dir; verify PASS with 0 notes.**

Run: `python3 startup-tracker/validate.py`
Expected: `OK: 0 company notes valid` (the `_template.md` is skipped).

---

### Task 3: Migrate existing target-orgs rows into company notes

**Files:**
- Create: `startup-tracker/companies/<one per company>.md`
- Read (for source data): `crm/target-orgs.md`

**Interfaces:**
- Consumes: the template from Task 1, the validator from Task 2.
- Produces: the initial company dataset the Bases dashboard (Task 4) renders.

- [ ] **Step 1: Re-read `crm/target-orgs.md`** to get the live rows (it may have changed since this plan was written). Use the table below as the mapping; if a row differs, prefer the file.

| file (kebab) | company | lane | location | geo_fit | status | funding | person | angle (short) | source |
|---|---|---|---|---|---|---|---|---|---|
| engram | Engram | ai-infra | SF | weak | reach-now | $98M·Seed·Jun23·General Catalyst | Dan Biderman (CEO) | Karpathy adviser + this vault = file-based agent memory | startups-gallery |
| collate | Collate | bio-ai→`health-bio-ai` | SF | weak | reach-now | $95M·Series A·Jun3·Redpoint | Surbhi Sarna (CEO) | life-sci reg docs + agentic doc workflows + JHTV lens | startups-gallery |
| flourish | Flourish | health-bio-ai | NYC | strong | enriching | $500M·Jun4·Bezos+Catalio ($2.5B) | Joshua Vogelstein (cofounder, JHU) | Hopkins warm cluster (Vogelstein/Catalio) | wired |
| fedtech | FedTech | other | Arlington VA | strong | reach-now | est. 2015 venture studio; hiring | Ian Senungwan Ryu (warm) | JHTV tech-transfer wheelhouse + Ian intro + general app | fedtech-app |
| chai-discovery | Chai Discovery | health-bio-ai | — | weak | enriching | $400M·Series C·Jul14·Index ($3.8B) | Joshua Meier (CEO; reach researchers) | run Chai-1 model → sharp observation ([[chai-hook-experiment]]) | startups-gallery |
| candid-health | Candid Health | health-bio-ai | — | weak | triaged | $120M·Series D·Jul22·Sixth Street | | healthcare billing AI; need contact+angle | startups-gallery |
| assort-health | Assort Health | health-bio-ai | — | weak | triaged | $120M·Series C·Jun24·Menlo | | AI patient calls; need contact+angle | startups-gallery |
| prime-intellect | Prime Intellect | ai-infra | — | weak | triaged | $130M·Series A·Jul8·Radical | | agent-building wheelhouse | startups-gallery |
| dust | Dust | ai-infra | — | weak | triaged | $40M·Series B·May18·Abstract | | multiplayer AI agents | startups-gallery |
| nourish | Nourish | health-bio-ai | — | weak | triaged | $100M·Series C·May19·Menlo | | nutrition telehealth | startups-gallery |
| prosper-ai | Prosper AI | health-bio-ai | — | weak | triaged | $30M·Series A·Jun22·a16z | | AI workforce for healthcare | startups-gallery |
| cuspai | CuspAI | other | — | weak | triaged | $450M·Series B·Jul21·Kleiner (Bezos/NEA) | | AI materials discovery; weak hook | startups-gallery |
| ataraxis-ai | Ataraxis AI | health-bio-ai | NYC | strong | triaged | hiring Jul 2026 | | NYC precision-oncology AI; JHTV lens + I build AI | july-hiring-thread |
| formation-bio | Formation Bio | health-bio-ai | NYC | strong | triaged | hiring | | AI-native drug development; JHTV translational lens | july-hiring-thread |
| photon-health | PhotonHealth | health-bio-ai | NYC | strong | triaged | hiring | | prescription/pharmacy dev platform | july-hiring-thread |
| forus-health | Forus Health | health-bio-ai | — | ok | nurtured | $160M·Series B·May12·General Catalyst | Arielle | already connected; reconnect Feb–Mar 2027 | startups-gallery |
| physicsx | PhysicsX | other | — | weak | parked | $300M·Series C | | industrial/physical AI; no hook | startups-gallery |
| generalist-ai | Generalist AI | other | — | weak | parked | $400M | | robotics AI; no hook | startups-gallery |
| isometric | Isometric | other | — | weak | parked | $40M·Series A | | climate-science AI; no hook | startups-gallery |
| inherent-labs | Inherent Labs | other | — | weak | parked | $50M·seed | | no Cole hook | startups-gallery |

- [ ] **Step 2: Create one note per row** by copying `_template.md` and filling the frontmatter from the table. Set `discovered: 2026-07-28` for the startups-gallery/wired rows, `2026-07-29` for the july-hiring-thread and fedtech-app rows. For `location: —`, set `location: ""` and `geo_fit: weak`. Add one interaction-log line matching `source`. For `flourish`, set `person: "[[Joshua Vogelstein]]"` and add a note linking `[[flourish]]`, `[[catalio-capital]]`.

- [ ] **Step 3: Run the validator; verify PASS.**

Run: `python3 startup-tracker/validate.py`
Expected: `OK: 20 company notes valid` (count = rows created; adjust if the live file differed).

- [ ] **Step 4: No commit** (gitignored). Confirm nothing staged: `git status --porcelain startup-tracker/` prints nothing.

---

### Task 4: Build the `Startup Tracker.base` dashboard

**Files:**
- Create: `startup-tracker/Startup Tracker.base`

**Interfaces:**
- Consumes: the company notes from Task 3 (their frontmatter property names).
- Produces: the interactive dashboard; no downstream code depends on it.

- [ ] **Step 1: Write the base config.** Obsidian Bases uses YAML. Create `startup-tracker/Startup Tracker.base` with five views. Use this as the starting config (property names must match the frontmatter exactly):

```yaml
filters:
  and:
    - file.folder == "startup-tracker/companies"
    - file.name != "_template"
formulas:
  age_days: 'if(discovered, (date(now()) - date(discovered)).days, "")'
  followup: 'if(and(status == "contacted", replied == false), "⏰ nudge", "")'
properties:
  company: { displayName: Company }
  lane: { displayName: Lane }
  location: { displayName: Loc }
  status: { displayName: Status }
views:
  - type: table
    name: "📥 Fresh Finds"
    filters:
      and:
        - 'status == "discovered" || status == "triaged"'
        - 'formula.age_days <= 14'
    order: [company, lane, location, source, formula.age_days]
    sort: [{ property: discovered, direction: DESC }]
  - type: table
    name: "🟢 Reach Now"
    filters: [ 'status == "reach-now"' ]
    order: [company, lane, location, person, angle, formula.age_days]
    sort: [{ property: discovered, direction: DESC }]
  - type: table
    name: "🚚 In Progress"
    filters: [ 'status == "contacted" || status == "replied" || status == "meeting"' ]
    order: [company, status, person, last_touch, formula.followup]
    sort: [{ property: last_touch, direction: ASC }]
  - type: table
    name: "🗂 By Lane"
    filters: [ 'status != "parked" && status != "passed"' ]
    order: [company, lane, location, status]
    sort: [{ property: lane, direction: ASC }]
  - type: table
    name: "📊 Metrics"
    filters: []
    order: [company, status, lane, replied]
    sort: [{ property: status, direction: ASC }]
```

- [ ] **Step 2: Open it in Obsidian and verify the views render.** In Obsidian, open `Startup Tracker.base`. Confirm each of the five tabs shows rows. **Bases syntax risk:** if the app rejects a formula or filter expression, adjust it to the syntax shown in the installed Bases version's docs (Settings → Core plugins → Bases, or the property/formula editor UI). The load-bearing behavior is: Fresh Finds shows recent untriaged, Reach Now shows `reach-now`, In Progress shows active with a follow-up flag, By Lane groups active, Metrics shows everything by status.

- [ ] **Step 3: Verify reply-rate.** In the Metrics view, add a **summary/footer** on the `replied` column (Bases table views support column summaries). If the installed Bases version can't compute `replied ÷ contacted` directly, create `startup-tracker/Metrics.md` with a short manual formula note and link it from the README. Confirm the count of `status == contacted` and `replied == true` are both visible.

- [ ] **Step 4: No commit** (gitignored).

---

### Task 5: Repoint target-orgs + wire the outreach-pipeline runbook

**Files:**
- Modify: `crm/target-orgs.md`
- Modify: `crm/outreach-pipeline.md`

**Interfaces:**
- Consumes: the company notes + Base (as the new source of truth for org tracking).

- [ ] **Step 1: Reduce `crm/target-orgs.md` to a pointer.** Replace the triage tables with a short note: the org tracker now lives in `startup-tracker/` (open `Startup Tracker.base`); this file is retained only as a historical breadcrumb. Keep the "Strategy (why this exists)" paragraph and the weekly-log history; delete the now-migrated tables.

- [ ] **Step 2: Update the `crm/outreach-pipeline.md` runbook step 2** so "scan → triage" reads/writes `startup-tracker/companies/*.md` and the Base instead of the old `target-orgs` tables. Keep Lane 0 / Tier 1 / Tier 2 (PIKE) people rows exactly as-is (out of scope). Add a line: "Company discovery now runs via the `startup-radar` skill (see Task 6); this runbook consumes its output."

- [ ] **Step 3: Verify links.** Run: `grep -n "startup-tracker\|Startup Tracker.base" crm/target-orgs.md crm/outreach-pipeline.md` — confirm both point to the new home.

- [ ] **Step 4: No commit** (both files are under gitignored `crm/`).

---

### Task 6: Build the `startup-radar` skill

**Files:**
- Create: `.claude/skills/startup-radar/SKILL.md`

**Interfaces:**
- Consumes: the company-note template + validator + lane enums.
- Produces: the `startup-radar` skill, invocable by "run the startup radar."

- [ ] **Step 1: Write `SKILL.md`** with YAML frontmatter (`name: startup-radar`, a `description` that triggers on "run the startup radar" / weekly startup discovery) and a body specifying this procedure:

  1. **Sources to sweep (free surfaces only):** HN "Who's Hiring" (fetch latest monthly thread via `https://hn.algolia.com/api/v1/search?query=Ask HN Who is hiring&tags=story` → get the newest thread id → fetch its comments), YC jobs directory (`ycombinator.com/jobs`), VC portfolio boards (`jobs.sequoiacap.com`, `portfolio-jobs.a16z.com`, `jobs.indexventures.com`, `jobs.greylock.com`), Harmonic Hot 25 (`harmonic.ai/hot-25-startups`), Founders You Should Know (`foundersysk.com`), `startups.gallery/news`, and public Substack posts (Next Play, Early Days, a16z Build). **Skip** paid data (Ramp, full Harmonic).
  2. **Extract** company, location, careers URL, funding (if shown), and which source.
  3. **Lane filter:** keep only `health-bio-ai` or `ai-infra` (AI agents/memory/dev-tools Cole can speak to); set `geo_fit` from location (NYC/DC = strong, remote = remote, else weak). Drop clearly out-of-lane companies.
  4. **Dedup:** read existing `startup-tracker/companies/*.md`; skip any whose `company` or domain already exists, including `parked`/`passed`.
  5. **Write** new notes from the template with `status: discovered`, `discovered: <today>`, `source: <origin>`, and a one-line first-pass `angle` guess.
  6. **Report** a ranked shortlist (strong geo + health-bio-ai first) in-session; offer an optional iMessage push using the concert-digest AppleScript pattern.
  7. **Validate:** run `python3 startup-tracker/validate.py` at the end; fix any flagged note.

- [ ] **Step 2: Dry-run the skill.** Invoke "run the startup radar." Verify it: fetches at least 2 sources, creates only lane-filtered notes, skips companies already present, and prints a shortlist.

- [ ] **Step 3: Verify schema.** Run: `python3 startup-tracker/validate.py`
Expected: `OK: N company notes valid` (N grew by the number of new finds).

- [ ] **Step 4: Commit the skill (tracked).**

```bash
git add ".claude/skills/startup-radar/SKILL.md"
git commit -m "feat: startup-radar skill (weekly startup discovery sweep)"
```

---

## Self-Review

**Spec coverage:** Discovery Radar → Task 6. Company data model → Tasks 1–3. Bases dashboard (5 views) → Task 4. Loop integration + migration → Tasks 3, 5. Privacy/gitignore → Task 1 + Global Constraints. Analytics (Metrics/reply rate) → Task 4 step 3. Scope boundaries (people stay in outreach-pipeline; no paid APIs; no auto-send) → Global Constraints + Task 5. All spec sections covered.

**Placeholder scan:** No TBD/TODO. The validator, template, base config, and migration table contain actual content. The `angle`/`person` blanks in the migration table are real data states (unknown yet), not plan placeholders.

**Type consistency:** Frontmatter property names (`company`, `lane`, `status`, `geo_fit`, `discovered`, `last_touch`, `replied`, `source`, `person`, `angle`) are identical across the template (Task 1), validator (Task 2), migration (Task 3), base config (Task 4), and skill (Task 6). Enum values match the Global Constraints. The `formula.age_days` / `formula.followup` names used in the base views match their `formulas:` definitions.
