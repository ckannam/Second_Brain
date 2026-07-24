# Claude Code

Anthropic's agentic coding tool and the **central entity** of this vault — nearly every ingested source is about a Claude Code feature, workflow, or business built on it. Available in terminal, desktop app, VS Code/JetBrains, web, and mobile.

## Native features covered by sources
- **[[claude-code-scheduled-tasks|Scheduled tasks]]** — cron-triggered autonomous agentic sessions (desktop app). Src: [[claude-code-2-scheduled-tasks]].
- **[[claude-code-loops|Loops]]** — repeat skills/tasks on an interval up to 3 days. Src: [[claude-code-loops]].
- **[[claude-code-memory|Memory + Auto Dream]]** — auto-memory plus a background sub-agent that consolidates memory files "like sleep." Src: [[claude-code-memory-2-autodream]].
- **[[claude-code-skills|Skills]]** — reusable capabilities; Skill Creator + evals + trigger tuning. Srcs: [[claude-code-skills-update]], [[master-claude-code-skills-28min]].
- **[[claude-code-subagents|Sub-agents]] & [[claude-code-agent-teams|Agent Teams]]** — delegation and parallel, collaborating agents. Src: [[claude-code-agent-teams]].
- **[[claude-code-permissions|Auto Mode permissions]]** — risk-classifier between "ask always" and "skip permissions." Src: [[claude-code-auto-mode-permissions]].
- **[[claude-code-computer-use|Computer Use]]** — control mouse/keyboard/screenshots. Src: [[claude-code-computer-use]].
- **Remote access:** [[claude-code-remote-control|Remote Control]] (mobile), [[claude-code-channels|Channels]] incl. [[claude-code-imessage|iMessage]], and Dispatch. Srcs: [[claude-code-remote-control]], [[claude-code-imessage]].
- **[[artifacts-in-claude-code|Artifacts]]** — turn raw output into a shareable visual page (beta, Team/Enterprise). Src: [[artifacts-in-claude-code]]. See also [[what-new-in-claude-code]], [[beyond-the-basics-claude-code]].

## Ecosystem & integrations
[[codex]] plugin (adversarial review), [[firecrawl]] (scraping), [[n8n]] (self-healing), [[google-workspace-cli]], [[trigger-dev]] (hosting), [[blotato]] (social), [[gemini-embeddings-2]]/[[pinecone]] ([[rag|RAG]]), [[nano-banana-2]] (images), MCP servers.

## Built on Claude Code (in this vault)
[[ai-executive-assistant|Executive assistants]], the [[ai-second-brain-levels|5-level second brain]], [[agentic-workflows]], website building, content pipelines. Competes with [[clawdbot]], [[paperclip]], [[openclaw]].

## Beyond the CLI: the Claude Platform
The Code-with-Claude batch situates Claude Code inside a larger platform:
[[claude-managed-agents]] runs production agents server-side (the Agent SDK drives Claude
Code; Managed Agents hosts it), and [[claude-cowork]] is the delegated async surface. The
Managed Agents "Claude API skill" ships inside Claude Code. See [[how-we-claude-code]] for
how Anthropic dogfoods it internally.

Vendor: [[anthropic]]. Models referenced: [[opus-4-6]]. Most sources here are by [[nate-herk]].
