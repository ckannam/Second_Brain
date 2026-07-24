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

### Personal bucket — CRM & data sources
- [ ] **Enrich the top-tier CRM with relationship context** — read message content for the inner-circle (~43) to fill each "Context" section (how you know them, history). Currently records are stats + inferred category only. (added 2026-07-24)
- [ ] **Instagram** — not reachable via any connector; export your IG data (Settings → Download your information, JSON) and point me at it to catalog the social graph. (added 2026-07-24)
- [ ] Gmail pass 2 — page the rest of Sent/Inbox to catch email-only professional contacts beyond the Uship team. (added 2026-07-24)

### Vault system
- [ ] Fix the raw inbox drift — repoint the Obsidian Web Clipper to `raw/assets/`, or update `AGENTS.md` to say clips land in `raw/`. [[obsidian-web-clipper]] (added 2026-07-24)
- [ ] Decide whether to build the **Journal** pillar (scaffolded only). [[second-brain-system]] (added 2026-07-24)
- [ ] Populate the mostly-empty buckets ([[Duke]], [[Uship]], [[JHTV]], [[Job Search]]) as their content lands in the vault. (added 2026-07-24)

### AutoResearch (Karpathy)
- [ ] **Create the overnight schedule** — wire the [[vault-autoresearch]] loop to run unattended via desktop `/schedule` or a GitHub Actions cron (`claude -p "run the vault-autoresearch loop"`). [[claude-code-scheduled-tasks]] (added 2026-07-24)
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

- [x] **Catalogued 379 people into the CRM** from iMessage history (mapped to Contacts), tiered by interaction volume, with the alphabetical `crm/index.md`. Kept **local-only** (gitignored). Identified the **Uship team** ([[John Gorman]], [[Tag Mehbod]], [[Ray Kwei]], [[Daniel Hieman]], [[Nick Loria]]) via Gmail and created the [[uship]] entity + populated the [[Uship]] bucket. (done 2026-07-24)
- [x] Built the **[[vault-autoresearch]]** loop — `git init` (the ratchet) + frozen `autoresearch/score.py` (HEALTH_DEBT metric) + `program.md` + the `vault-autoresearch` skill; proved MODE A self-healing (drove debt 2→0). (done 2026-07-24)
- [x] Created the 6 **life buckets** as Maps of Content (Duke / Uship / JHTV / Job Search / Personal / Claude Mastery) + `buckets/index.md`, wired into `AGENTS.md` as a re-cuttable overlay. [[buckets/index]] (done 2026-07-24)
- [x] Stored both **session-opening prompts** in [[session-opening-prompts]] (`--dangerously-skip-permissions` + `--channels plugin:imessage@claude-plugins-official`). (done 2026-07-24)
- [x] Folded the parallel **"Code with Claude"** batch (30 first-party Anthropic sessions) into [[Claude Mastery]] (+ future-of-work cross-links into [[Job Search]]). (done 2026-07-24)
