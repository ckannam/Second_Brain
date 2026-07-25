# Index

Content catalog of the wiki. Every page listed with a link and a one-line summary,
organized by category. Updated on every ingest. Read this first when answering a query.

See [[overview]] for the top-level synthesis and how the pages connect. Contacts live in
the separate CRM index at `crm/index.md`. Open **action items** live in `tasks/index.md`
(the vault's to-do board — read it at the start of a work session). To browse by area of
life, use the **[[buckets/index|buckets]]** (life-area Maps of Content).

## Buckets (by life area)
A re-cuttable overlay — hub notes that link to pages by life area (see [[buckets/index]]):
[[Duke]] · [[Uship]] · [[JHTV]] · [[Job Search]] · [[Personal]] · [[Claude Mastery]].

> **Big batch — 2026-07-24:** ingested 42 YouTube sources (41 by [[nate-herk]], 1 by
> Easy Machine AI, 1 by [[sarah-guo]]) covering the July 2026 Claude Code release wave,
> agentic workflows, second-brain builds, and the business of selling AI automations.

> **Code with Claude batch — 2026-07-24:** ingested 30 first-party [[anthropic|Anthropic]]
> sessions (channel: Anthropic) from the **Code with Claude** event + briefings. New
> surfaces beyond the CLI: [[claude-managed-agents]], [[claude-cowork]], [[claude-tag]],
> [[claude-science]], [[claude-design]]; internal practice ([[how-we-claude-code]],
> [[running-ai-native-engineering-org]]); the prompting/evals/thinking playbooks; agent
> memory + dreaming; and regulated-industry deployments ([[man-group]], [[lovable]],
> [[omni]], [[genspark]], [[elicit]]).
> **Freshness:** these sources are a snapshot — they cite [[opus-4-7]] as newest, but the
> current flagship is [[opus-4-8]]. Treat model/workflow specifics as point-in-time.

> **AutoResearch batch — 2026-07-24:** ingested 8 sources on [[andrej-karpathy]]'s
> **[[autoresearch]]** (the [[autoresearch-repo|GitHub repo]] itself + 3 YouTube explainers by
> [[david-andre]], [[nick-saraev]], [[greg-isenberg]]). One agent edits one file, trains a
> [[nanochat]] GPT for 5 min, keeps or `git reset`s on `val_bpb`, loops forever — a runnable
> [[self-healing-workflows|self-improving loop]]. Generalizes to any objective metric
> (cold email, CRO, trading). Companion project: **[[agent-hub]]** ("GitHub for agents").

## Entities

### People
- [[andrej-karpathy]] — originator of the LLM Wiki pattern; now delegates nearly all coding to agents.
- [[matt-wolfe]] — YouTuber who built a second-brain system (wiki + journal + CRM).
- [[erin-meryl]] — Cambridge student, "Erin Meryl Study" channel; neuroscience of discipline.
- [[nate-herk]] — creator (Uppit AI / AI Automation Society) behind 41 of the Claude Code sources here.
- [[sarah-guo]] — investor (Conviction / No Priors) who interviewed Karpathy.
- [[david-andre]] · [[nick-saraev]] · [[greg-isenberg]] — creators behind the AutoResearch explainer batch.

#### Code with Claude — Anthropic people
- [[fiona-fung]] — leads eng + product for Claude Code & Cowork; "the bottlenecks moved."
- [[boris-cherny]] — Head of Claude Code; introduced Claude Tag / @Claude.
- [[cat-wu]] — Head of Product, Claude Code; co-presented the future-of-work talk.
- [[tariq]] — Claude Code team; "The Unreasonable Effectiveness of HTML files."

#### Code with Claude — customers / founders
- [[james-brady]] — Elicit; trust = mechanism, custom agentic DSL (AshPL).
- [[kay-zhu]] — CTO/cofounder Genspark; "the only moat is the team's culture."

### Tools & orgs
- [[claude-code]] — Anthropic's agentic coding tool; the central subject of this vault.
- [[anthropic]] — maker of Claude Code; shipping features at a rapid cadence.
- [[obsidian]] — markdown front end / reading layer for the wiki.
- [[obsidian-web-clipper]] — browser extension that clips web pages / YouTube transcripts into `raw/`.
- [[codex]] — OpenAI coding agent; now also a plugin for Claude Code.
- [[autoresearch|autoresearch (repo)]] — Karpathy's self-improving research loop (one file, one metric). · [[agent-hub]] — "GitHub for agents." · [[nanochat]] — the small GPT autoresearch trains.
- [[clawdbot]] — young third-party AI agent tool; alternative to Claude Code for assistants.
- [[openclaw]] — open-source Claude-agent project noted for its memory system.
- [[paperclip]] — run an entire company of AI agents (CEO agent hires/delegates).
- [[n8n]] — node-based automation incumbent, repeatedly contrasted with Claude Code.
- [[firecrawl]] — turns any website into LLM-ready data (MCP server).
- [[uship]] — University Shipping: Cole's Duke-focused student shipping/storage venture (see [[Uship]] bucket).
- [[jhtv]] — Johns Hopkins Technology Ventures; Cole's Capital Strategy internship (see [[JHTV]] bucket).
- [[marsh-memory-lab]] — Duke metacognition lab; Cole's PSY 394 study on editing depth & the Illusion of Explanatory Depth (ties to [[vault-autoresearch]]).
- [[qmd]] — optional local markdown search engine (not yet in use).
- [[trigger-dev]] · [[pixel-agents]] · [[blotato]] · [[dispatch]] · [[mcp]] · [[tmux]] · [[vercel]] · [[obsidian-dataview]] · [[obsidian-web-viewer]] — supporting tools.

#### Anthropic platform & products (Code with Claude batch)
- [[claude-managed-agents]] — managed platform for production agents (agent/environment/session).
- [[claude-cowork]] — delegated async knowledge work; scheduled tasks.
- [[claude-tag]] — proactive, multiplayer @Claude (Slack beta).
- [[claude-science]] — reproducible research AI workbench (beta).
- [[claude-design]] — plain-language → production, on-brand design outputs.

#### Companies building on Claude
- [[elicit]] — research assistant; custom agentic DSL. · [[man-group]] — $200B fund; AI trading signals in prod.
- [[omni]] — analytics harness (99% built with Claude Code). · [[lovable]] — vibecoding at 600M+ sessions/mo.
- [[genspark]] — all-in-one AI workspace.

### Google stack
- [[google]] · [[gemini]] · [[gemini-embeddings-2]] · [[gemini-3-1-flash-live]] · [[nano-banana-2]] · [[antigravity]] · [[pinecone]] — models/tools used in Google-centric sources.

### Models & other orgs
- [[opus-4-6]] (Anthropic) · [[gpt-5-4]] / [[openai]] — benchmarked pair in the Codex plugin source.
- [[opus-4-8]] — **current flagship** (freshness reconciliation; not in the sources). · [[opus-4-7]] — flagship across the Code with Claude batch. · [[opus-4-5]] — fixed Sonnet 4.5's context anxiety.
- [[mythos]] — real, publicly-unreleased model named in [[the-thinking-lever]] (~16h human work @50% METR).

### More people
- [[sarah-guo]] — Conviction / No Priors; interviewed Karpathy.
- [[zach-yedegari]] — built [[cal-ai]]. · [[suvam]] — $500k cold-email case. · [[christian]] — first client in 7 days.

### Products / rivals
- [[cal-ai]] — $100M vibecoded calorie app.

## Concepts

### LLM Wiki / knowledge systems
- [[llm-wiki-pattern]] — persistent compounding wiki vs. RAG; three layers, why it works.
- [[ingest-query-lint]] — the three core wiki operations.
- [[second-brain-system]] — Matt Wolfe's wiki + journal + CRM extension.
- [[agentic-note-taking]] — agents do the data entry; friction-free journaling/logging into the vault.
- [[ai-second-brain-levels]] — the "5 levels" of a Claude Code second brain; pick the lowest that helps.
- [[extending-the-llm-wiki]] — roadmap: how this vault instantiates Karpathy's pattern and how to push it further (filed from a query).
- [[vault-autoresearch]] — the self-healing + AutoResearch loop built into this vault (HEALTH_DEBT metric, git ratchet).
- [[llm-wiki-vs-rag]] — human-readable interlinked wiki vs. opaque vector retrieval.
- [[rag]] — retrieval-augmented generation; turnkey multimodal RAG with Gemini Embeddings 2.

### Claude Code capabilities
- [[claude-code-scheduled-tasks]] — cron-triggered autonomous agentic sessions.
- [[claude-code-memory]] — auto-memory + experimental "Auto Dream" consolidation.
- [[claude-code-skills]] — reusable skills; Skill Creator, evals, trigger tuning.
- [[claude-code-permissions]] — Auto Mode risk classifier (link stub).
- [[claude-code-computer-use]] · [[claude-code-remote-control]] · [[claude-code-imessage]] — control & remote access (stubs).
- [[claude-code-agent-teams]] · [[claude-code-subagents]] — parallel & delegated agents.
- [[claude-code-channels]] · [[claude-code-hooks]] · [[claude-code-browser-automation]] — access, notifications, browser.
- [[claude-md-router]] — Level-1 `CLAUDE.md` router. · [[skills-vs-subagents]] — when to use which.

### Agents & orchestration
- [[parallel-agents]] · [[multi-agent-orchestration]] · [[ai-agent-company]] · [[multi-model-workflows]] · [[adversarial-code-review]] · [[agent-observability]] · [[proactive-agents]] · [[autoresearch]].

### Data, RAG & tooling patterns
- [[multimodal-rag]] · [[web-scraping-for-llms]] · [[content-repurposing]] · [[voice-agents]] · [[website-building-with-ai]] · [[hosting-ai-agents]] · [[vps]] · [[natural-language-coding]] · [[ai-app-business]].

### Selling
- [[selling-ai-automations]] · [[zero-risk-offer]] · [[cold-email-outreach]].

### Agentic automation & business
- [[agentic-workflows]] — autonomous, self-healing automation vs. fixed node graphs.
- [[agentic-vs-deterministic]] — the core robustness-vs-predictability trade-off.
- [[self-healing-workflows]] — agents that detect and fix their own failures.
- [[n8n-vs-claude-code]] — the vault's stance on the incumbent vs. agentic tools.
- [[ai-executive-assistant]] — a proactive personal assistant you act *through*.
- [[selling-ai-automations]] — turning agentic workflows into income.
- [[vibecoding]] — building software purely by natural-language delegation.
- [[json-prompting]] — structured prompts for controllable image generation.

### Building agents (Code with Claude batch)
- [[brain-hands-decoupling]] — separate the agent loop from tool execution (security/latency/reliability).
- [[outcome-oriented-agents]] — give a rubric/goal; the agent loops toward it. · [[agent-vaults]] — encrypted per-session credentials.
- [[agent-memory]] — file-system memory, scopes, multi-agent. · [[agent-dreaming]] — out-of-band batch memory curation.
- [[context-anxiety]] — Sonnet 4.5's early-stopping; why harnesses co-evolve with models.
- [[mechanism-over-output]] — trust the *how*, not just the output. · [[agentic-dsl]] — constrained DSL for legible/faithful plans.
- [[instructions-as-code]] — skills as reviewed/merged PRs; teach agents *how to think*.

### Evals, prompting & models
- [[eval-driven-model-selection]] — a small eval beats benchmarks for your decision.
- [[cost-per-successful-outcome]] — the right economic metric for model choice.
- [[test-time-compute]] — the thinking lever; effort levels; two axes of intelligence.
- [[prompt-engineering-playbook]] — eval-first prompt debugging, XML structure, output contracts.
- [[llm-as-judge]] — grade equivalent-but-different outputs (the "evals for taste" idea lives on the source hub [[evals-for-taste]]).
- [[the-capability-curve]] — where model capability is heading (batch hub).

### AI-native work & industry
- [[ai-native-engineering-org]] — the bottlenecks moved; rewrite the norms.
- [[html-over-markdown-specs]] — HTML for legible, verification-native artifacts. · [[bitter-lesson]] — don't over-constrain capable models.
- [[governed-skills-framework]] — teach + govern workflows so compliance says yes. · [[ai-for-science]] — compress 50–100 yrs into 5–10.

### Discipline & behavior change
- [[discipline-without-willpower]] — thesis: discipline is structure, not willpower.
- [[temporal-discounting]] — dopamine discounts future rewards; root cause of low discipline.
- [[temptation-bundling]] — pair a hard task with an immediate reward.
- [[cue-routine-reward-loop]] — automate task initiation via conditioning.
- [[identity-led-goals]] — frame goals as identity ("I am someone who…").
- [[environment-design]] — reduce clutter and friction to make the good action default.
- [[how-to-build-discipline]] — playbook distilled from the discipline cluster (filed from a query).

## Sources

### Foundational
- [[llm-wiki-karpathy]] — Karpathy gist: the LLM Wiki pattern (web).
- [[build-an-ai-second-brain-matt-wolfe]] — YouTube, Matt Wolfe: step-by-step build.
- [[discipline-without-willpower-erin-meryl]] — YouTube, Erin Meryl Study: 5 discipline strategies.

### Claude Code — native features (July 2026)
- [[claude-code-2-scheduled-tasks]] — native scheduled tasks / cron agents.
- [[claude-code-loops]] — repeat skills/tasks on an interval up to 3 days.
- [[claude-code-memory-2-autodream]] — Memory 2.0 / Auto Dream memory consolidation.
- [[claude-code-computer-use]] — control mouse/keyboard/screenshots (research preview).
- [[claude-code-skills-update]] — Skill Creator, evals, trigger tuning.
- [[claude-code-auto-mode-permissions]] — Auto Mode risk-classifier permissions.
- [[claude-code-imessage]] — text your Claude Code session (this vault's channel).
- [[claude-code-remote-control]] — drive Claude Code from your phone.
- [[claude-code-agent-teams]] — parallel, collaborating agents (tmux view).
- [[codex-plugin-for-claude-code]] — OpenAI Codex as adversarial reviewer for Opus.

### Knowledge, second brain & RAG
- [[andrej-karpathy-llm-wiki-obsidian]] — build Karpathy's LLM Wiki in Obsidian + Claude Code.
- [[skill-issue-karpathy-sarah-guo]] — Karpathy interview: agents, AutoResearch, jobs.
- [[master-claude-code-skills-28min]] — skills primer + live build.
- [[master-claude-code-36min-beginner]] — beginner Claude Code framework ("WAT framework").
- [[every-level-claude-second-brain]] — the 5 levels of a Claude second brain.
- [[obsidian-vault-deep-dive-emai]] — Easy Machine AI's agentic Obsidian system.
- [[turn-any-website-llm-ready-firecrawl]] — Firecrawl → LLM-ready data.
- [[google-rag-gemini-embeddings-2]] — turnkey multimodal visual RAG.

### Agentic workflows & n8n
- [[how-to-build-10k-agentic-workflows]] — $10k agentic workflows + how to sell them.
- [[from-zero-first-agentic-workflow-26min]] — beginner first workflow in 26 min.
- [[how-id-teach-10-year-old-agentic]] — simplest framing of agentic workflows.
- [[agentic-workflows-changed-automation]] — why agentic changes build & sell.
- [[i-will-never-fix-n8n-self-healing]] — self-healing n8n via Claude Code MCP.
- [[is-n8n-dead]] — honest take on n8n's future.
- [[stop-learning-n8n-2026]] — learn agentic workflows instead.
- [[500-ai-workflows-businesses-want]] — the 5 boring workflows that sell.

### Assistants, agents, hosting & tools
- [[turn-claude-code-executive-assistant]] — 4-phase executive-assistant blueprint.
- [[i-turned-clawdbot-personal-assistant]] — "Klaus," a proactive Clawdbot assistant.
- [[100-hours-clawdbot-vs-claude-code]] — head-to-head; Claude Code wins.
- [[set-up-clawdbot-vps]] — run Clawdbot 24/7 on a VPS.
- [[claude-code-paperclip-openclaw]] — Paperclip: run an AI-agent company.
- [[easiest-way-host-claude-code-agents]] — host agents with Trigger.dev.
- [[google-workspace-cli]] — control Google Workspace from Claude Code.
- [[pixel-agents-watch-ai-agents]] — watch agents work as pixel-art characters.

### Websites, images, content & voice
- [[building-beautiful-websites-claude-code]] — 5 website-design hacks.
- [[nano-banana-2-claude-code-10k-websites]] — animated $10k websites with Nano Banana 2.
- [[nano-banana-2-antigravity-json-prompting]] — JSON prompting for perfect images.
- [[generate-content-9-socials-blotato]] — repurpose a video into 9 social posts.
- [[gemini-flash-live-voice-agents]] — Gemini 3.1 Flash Live voice agents.
- [[this-100m-ai-app-cal-ai]] — Cal AI, the $100M vibecoded app.

### Business & selling
- [[build-sell-claude-code-course]] — the 10+ hour Build & Sell course (umbrella).
- [[college-student-500k-cold-email]] — Suvam's $500k cold-email framework.
- [[sign-first-ai-client-7-days]] — Christian's 7-day first-client plan.

### Code with Claude event (Anthropic, 2026-07-24 batch)
**Managed Agents & platform**
- [[ship-your-first-managed-agent]] — build an SRE agent; the three primitives.
- [[production-faster-managed-agents]] — infra is the bottleneck; self-hosted sandboxes, MCP tunnels.
- [[memory-and-dreaming-self-learning-agents]] — agent memory architecture + dreaming.
- [[enterprise-managed-auth-mcp]] — org-wide MCP connector auth via IdP.

**How Anthropic works (AI-native)**
- [[how-we-claude-code]] — interview → HTML specs → verification-native artifacts.
- [[running-ai-native-engineering-org]] — the bottlenecks moved; rewritten team norms.
- [[gtm-engineering-anthropic]] — an AE with no code built an email assistant (Class).
- [[ai-native-enterprise-scale]] — Delivery Hero / Doctolib / monday.com.
- [[future-of-work-claude-tag]] — Claude Tag / @Claude (Boris Cherny, Cat Wu).

**Prompting, models & evals**
- [[the-prompting-playbook]] — eval-first prompt debugging. · [[picking-the-right-model]] — build an eval, not a benchmark.
- [[the-thinking-lever]] — test-time compute & effort levels. · [[the-capability-curve]] — where the curve is going.
- [[evals-for-taste]] — rubric-driven evals for a slide-gen agent.
- [[trustworthy-agentic-workflows-dsl]] — Elicit's AshPL DSL.

**Industry & products**
- [[signals-that-trade-themselves]] — Man Group's AI trading signals in prod.
- [[claude-cowork-delegate-schedule]] · [[financial-crime-claude-cowork]] — Cowork delegation + finance.
- [[claude-science-beta]] · [[the-briefing-ai-for-science]] · [[the-briefing-financial-services]] — Science/Finance.
- [[omni-agentic-analytics-harness]] · [[lovable-vibecodes-at-scale]] · [[problem-solvers-kay-zhu-genspark]] — customers.
- [[designing-with-claude-prompt-to-production]] · [[building-with-claude-google-cloud]] — design & cloud build.
- [[artifacts-in-claude-code]] · [[beyond-the-basics-claude-code]] · [[what-new-in-claude-code]] · [[teaching-agents-learn-from-team]] — Claude Code updates.

### AutoResearch (Karpathy, 2026-07-24 batch)
- [[autoresearch-repo]] — the GitHub repo: README + `program.md` (agent loop) + `prepare.py` (fixed eval).
- [[autoresearch-tutorial-david-andre]] — clearest beginner explainer + live website-speed loop.
- [[claude-code-karpathy-autoresearch-nick-saraev]] — porting autoresearch to a cold-email reply-rate optimizer.
- [[autoresearch-broke-internet-greg-isenberg]] — 10 businesses built on autoresearch + [[agent-hub]].

## Reference
- [[session-opening-prompts]] — the launch commands used to start sessions for this vault.
