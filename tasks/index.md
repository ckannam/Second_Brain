# Action Items — Vault & Second-Brain Improvements

Work to improve the **Obsidian vault / second-brain system itself** — *not* personal
to-dos (those get a separate board, added later). Maintained across sessions per the
**Action Items** operation in `AGENTS.md`. Newest open items at top; completed items drop
to **Done** (never deleted).

Format: `- [ ] <action> — <context> [[related-page]] (added YYYY-MM-DD)`

## Open

### Claude Mastery — skills & agents
_Goal: create the best possible Claude skills to (a) **maintain & maximize** this second brain and (b) build **alongside** it at a much faster rate._
- [ ] **Train skills** — build & optimize skills with the Skill Creator + evals workflow, for both vault upkeep and faster building. [[claude-code-skills]] [[claude-code-skills-update]] (added 2026-07-24)
- [ ] **Prompt max** — master prompt quality (structured prompts, clarifying-question prompting) as a reusable skill. [[prompt-engineering-playbook]] [[the-prompting-playbook]] [[master-claude-code-36min-beginner]] [[json-prompting]] (added 2026-07-24)
- [ ] **Token max** — build a token/context-management skill & mastery (efficient context use, compaction, memory). [[claude-code-memory]] (added 2026-07-24)
- [ ] **Skill max** — master reliable skill creation + trigger tuning. [[master-claude-code-skills-28min]] [[claude-code-skills]] (added 2026-07-24)
- [ ] **Agent max** — master agent orchestration: sub-agents + agent teams. [[claude-code-subagents]] [[claude-code-agent-teams]] (added 2026-07-24)
- [ ] **Improve + general skills** — continuously improve existing skills and maintain a set of general-purpose ones. (added 2026-07-24)

### Personal bucket — finance
- [ ] Data connection — **decided 2026-07-25: no paid apps** (Tiller/Monarch declined). Free path = **Empower Personal Dashboard** (fka Personal Capital) for the investment/net-worth dashboard + occasional **manual CSV export** into local-only `finance/` when Cole wants a spending/holdings analysis. [[data-connection]] (added 2026-07-25)
- ✅ **Built the finance planning tool** (2026-07-25): [[finance/index]] hub + [[investment-plan]] (portfolio + Freedom Number) + [[financial-roadmap]] (life-stage plan incl. post-grad NYC budget). Grounded in profile + 5-year plan; no live data needed.
- [ ] **Define the Freedom Number** — the key missing input: pick the annual "freedom income" you want; ×25 = target portfolio. Then the plan reverse-engineers the monthly contribution. [[finance/index]] [[five-year-plan]] (added 2026-07-25)
- ✅ **Captured real numbers** (2026-07-25) → [[snapshot]]: net worth ~$14.7k (checking $3k · taxable $8.9k · Roth $2.8k) + ~$47–55k incoming over the year (JHTV/Uship/grandma).
- [ ] 💰 **Max the Roth** — ⏳ **planned Sept 2026** with the next Uship check (Cole's call, deliberate). Fund 2026 to ~$7k (at $2.8k), then max 2027 in Jan. *(No rush: 2026 Roth can be funded until Tax Day ~April 2027.)* [[snapshot]] (added 2026-07-25)
- [ ] **Verify the Roth is invested** in VTI/VBR, not idle settlement cash (the 3.5% return is a flag). [[snapshot]] (added 2026-07-25)
- [ ] Move idle checking → **HYSA (~4%)** + start the emergency fund. [[financial-roadmap]] (added 2026-07-25)
- [ ] **VXUS decision** — add ~20% international or keep US-only 70/30? [[investment-plan]] (added 2026-07-25)
- [ ] 🔽 **LOW PRIORITY / someday** — build a **DIY Plaid export script** (self-hosted, no paid app): scaffold in free Plaid **Sandbox** first, then only pursue if willing to do Plaid **Production** approval + BofA OAuth enablement. Runs on the nightly `@local` lane → writes to local-only `finance/`; keys/token in Keychain, never the vault. [[data-connection]] (added 2026-07-25)

### Personal bucket — CRM & data sources
- [ ] **Enrich the top-tier CRM with relationship context** — read message content for the inner-circle (~43) to fill each "Context" section (how you know them, history). Currently records are stats + inferred category only. (added 2026-07-24)
- [ ] Gmail pass 2 — page the rest of Sent/Inbox to catch email-only professional contacts beyond the Uship team. (added 2026-07-24)
- [ ] **Spotify + concert alerts** — when Spotify is added, set up proactive alerts for nearby/close concerts by Cole's favorite artists (he's into live shows). Pairs with a scheduled/proactive agent. [[proactive-agents]] (added 2026-07-24)
- [ ] **Add YouTube watch history** — ⏳ **Takeout export requested 2026-07-24; awaiting zip in `~/Downloads`.** Ingest watch/search history (JSON) → profile interests/taste when it lands. (added 2026-07-24)

### Uship
- [ ] **Build a Uship email responder** — automate replies to the `contact@universityshipping.com` customer inbox (student shipping/storage inquiries); the team currently answers these by hand. [[uship]] [[Uship]] (added 2026-07-24)

### Vault system
- [ ] **Build a password holder** — a secure place to store passwords/credentials. ⚠️ Must be **local-only** (gitignored like `crm/`) — never synced to GitHub or the cloud routine — or better, integrate a real password manager rather than plaintext markdown. Decide approach before building. (added 2026-07-24)
- [ ] **Export Instagram information** — request the IG data export (app → Settings → Accounts Center → *Download your information*, **JSON**; include Messages + Connections), drop the zip in `~/Downloads`, then have the agent ingest it to catalog the social graph. (added 2026-07-24)

- [ ] Decide whether to build the **Journal** pillar (scaffolded only). [[second-brain-system]] (added 2026-07-24)
- [ ] Populate the buckets — ✅ [[Uship]], [[JHTV]], [[Job Search]] done; [[Duke]] structured by org/club but **awaiting Cole to name key people per group** so they can be tagged `category: Duke`. (updated 2026-07-25)

### AutoResearch (Karpathy)
- **Nightly automation = TWO coordinated lanes (chosen 2026-07-25 for resilience over a single merged routine):**
  - ✅ **@cloud lane** — cloud routine `Vault AutoResearch (nightly)` (2 AM ET, always-on even if Mac off): self-heal + 1 generative + `autoresearch/nightly-queue.md` research (MODE C, web tools). Works on a review branch → morning PR.
  - ✅ **@local lane** — local `daily-ingest` scheduled task (~3 AM, needs Mac awake): **only** ingests `raw/assets/` clips → wiki per AGENTS.md, commits to main. Scoped to stay out of the cloud lane. *(SKILL.md rewritten 2026-07-25.)*
  - [ ] **Extend the @local lane** to also do personal-data tasks (CRM enrichment from messages, ingest IG/YouTube exports) once those are ready. [[proactive-agents]] (added 2026-07-25)
- [ ] **Build the source-seeking (MODE B) rung** — extend the loop to propose *new sources to ingest*, not just heal defects (the furthest roadmap rung). [[proactive-agents]] [[extending-the-llm-wiki]] (added 2026-07-24)
- [ ] Tune HEALTH_DEBT weights / add metrics as the vault grows (e.g. promote reciprocal-link gaps into the score once noise is understood). [[vault-autoresearch]] (added 2026-07-24)
- [ ] Try an **autoresearch loop hands-on** — clone `karpathy/autoresearch`, run it via [[claude-code]] on a rented GPU (Colab T4 / Lambda / RunPod), or adapt the pattern to a business metric (cold email, CRO). [[autoresearch]] [[autoresearch-repo]] (added 2026-07-24)
- [ ] Watch **[[agent-hub]]** ("GitHub for agents") — evaluate whether it's relevant to this vault's multi-agent direction. [[extending-the-llm-wiki]] (added 2026-07-24)

### Sourcing & verification
- [ ] Ingest official **Anthropic Claude Code docs** to ground single-source (Nate Herk) feature claims. [[claude-code]] [[anthropic]] (added 2026-07-24)
- [ ] Verify the **Auto Dream** trigger cadence (community-inferred). [[claude-code-memory]] (added 2026-07-24)
- [ ] Confirm the identities/spellings of **Clawdbot** / **OpenClaw**. [[clawdbot]] [[openclaw]] (added 2026-07-24)
- [ ] Capture the **Opus 4.6 vs GPT 5.4** benchmark numbers. [[opus-4-6]] [[gpt-5-4]] (added 2026-07-24)
- [ ] (Optional) Deeper notes on specific [[build-sell-claude-code-course]] chapters. (added 2026-07-24)

## Done

- [x] **Fixed the raw-inbox drift** — clipper defaults to vault-root `assets/` (not `raw/assets/`); made ingest + `AGENTS.md` sweep **both** inboxes so no clip is lost, and cleared a stray duplicate. [[obsidian-web-clipper]] (done 2026-07-25)
- [x] **Created the overnight schedule** — cloud routine `Vault AutoResearch (nightly)` runs 2 AM ET; fired 2026-07-25 and opened a MODE B branch. [[vault-autoresearch]] (done 2026-07-25)
- [x] **Catalogued 379 people into the CRM** from iMessage history (mapped to Contacts), tiered by interaction volume, with the alphabetical `crm/index.md`. Kept **local-only** (gitignored). Identified the **Uship team** ([[John Gorman]], [[Tag Mehbod]], [[Ray Kwei]], [[Daniel Hieman]], [[Nick Loria]]) via Gmail and created the [[uship]] entity + populated the [[Uship]] bucket. (done 2026-07-24)
- [x] Built the **[[vault-autoresearch]]** loop — `git init` (the ratchet) + frozen `autoresearch/score.py` (HEALTH_DEBT metric) + `program.md` + the `vault-autoresearch` skill; proved MODE A self-healing (drove debt 2→0). (done 2026-07-24)
- [x] Created the 6 **life buckets** as Maps of Content (Duke / Uship / JHTV / Job Search / Personal / Claude Mastery) + `buckets/index.md`, wired into `AGENTS.md` as a re-cuttable overlay. [[buckets/index]] (done 2026-07-24)
- [x] Stored both **session-opening prompts** in [[session-opening-prompts]] (`--dangerously-skip-permissions` + `--channels plugin:imessage@claude-plugins-official`). (done 2026-07-24)
- [x] Folded the parallel **"Code with Claude"** batch (30 first-party Anthropic sessions) into [[Claude Mastery]] (+ future-of-work cross-links into [[Job Search]]). (done 2026-07-24)
