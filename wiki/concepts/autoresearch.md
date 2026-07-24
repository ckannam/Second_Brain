---
type: concept
---
# AutoResearch

[[andrej-karpathy]]'s open-source project (released **March 2026**; ~25k GitHub stars within days) that lets an AI agent **close the loop on a piece of AI research autonomously** — form a hypothesis, edit the code, train, evaluate, keep or discard, and repeat, all with **no human in the loop**. A frontier example of fully [[agentic-workflows|agentic]] work and Karpathy's "loopy era of AI" (first named in [[skill-issue-karpathy-sarah-guo]], then shipped as a runnable repo — see the source [[autoresearch-repo]]).

> *"Give an AI agent a small but real LLM training setup and let it experiment autonomously overnight. You wake up in the morning to a log of experiments and (hopefully) a better model."* — Karpathy, README

## How the repo works
The reference implementation trains a small GPT (a single-GPU simplification of [[nanochat]]). It is deliberately tiny — **three files matter**:
- **`prepare.py`** — fixed constants, data prep, tokenizer, dataloader, and the **evaluation harness**. The agent **must not touch it** — this is what stops the agent from cheating the metric.
- **`train.py`** — the **single file the agent edits**. Model architecture, optimizer (Muon + AdamW), hyperparameters, batch size, training loop — all fair game.
- **`program.md`** — the **human-edited** agent instructions; Karpathy calls it "essentially a super lightweight [[claude-code-skills|skill]]." Iterating on `program.md` (and adding more agents) is how you tune your "research org."

**Metric:** `val_bpb` (validation **bits per byte**) — lower is better, and vocab-size-independent so architectural changes compare fairly.
**Time budget:** a **fixed 5 minutes** of wall-clock training per experiment (`TIME_BUDGET=300`). This makes experiments directly comparable regardless of what the agent changed, and yields ~**12 experiments/hour, ~100 overnight**.

## The experiment loop (from `program.md`)
Runs on a dedicated git branch (`autoresearch/<tag>`):
1. Hypothesize an improvement, hack `train.py` directly.
2. `git commit`.
3. Run `uv run train.py > run.log` (never flood context — redirect, don't `tee`).
4. `grep "^val_bpb:"` the log; empty output = crash → read the traceback, try to fix, else discard.
5. Record to `results.tsv` (`commit / val_bpb / memory_gb / status / description`; status = keep|discard|crash).
6. **Improved?** advance the branch (keep the commit). **Equal or worse?** `git reset` back.
7. Repeat **forever**. `program.md` explicitly says **"NEVER STOP"** — don't ask the human whether to continue; they may be asleep. If out of ideas, read referenced papers, combine near-misses, try more radical changes.

Two design rules worth stealing: a **simplicity criterion** (a tiny gain that adds ugly complexity isn't worth it; a simplification that holds results is always a keep) and **VRAM as a soft constraint**. The keep/`git reset` mechanism is a [[self-healing-workflows|self-correcting loop]] with git as the ratchet.

## The general pattern (beyond ML)
The sources' central claim: **this works for anything you can measure.** Three conditions must all hold ([[autoresearch-tutorial-david-andre]]):
1. **A clear scalar metric** — one number, one direction.
2. **An automated evaluation** — no human in the loop, or it can't run while you sleep.
3. **Exactly one thing the agent can change** — one editable file/input.

Given those, the **execution of experiments becomes ~free**; what stays scarce (and valuable) is *knowing what to measure* — picking the metric and constraints. This reframes the skill of the operator toward eval design — see [[eval-driven-model-selection]] and [[cost-per-successful-outcome]]. Karpathy: *"any metric you care about that is reasonably efficient to evaluate can be auto-researched."*

**Where it fails:** subjective "better" (brand design, UX, most pricing), feedback loops too slow to iterate, or no API/handle to change the input. A bad metric gets confidently optimized in the wrong direction.

## Business applications (creator framing)
The three explainer sources dwell almost entirely on money-making uses:
- **Cold email** — [[nick-saraev]]'s `email-optimizer`: metric = reply rate, changeable input = copy, run via GitHub Actions cron; a **baseline vs. challenger** A/B loop that logs learnings to a growing `resource.md`. Ties into [[cold-email-outreach]] / [[selling-ai-automations]].
- **Marketing / CRO** — landing pages (conversion rate), ad creatives (CAC/ROAS), YouTube titles, subject lines. Eric Seu's line: *"most marketing teams run 30 experiments/year; the next generation will run 36,000."*
- **Trading** — backtest simple rules overnight, score by Sharpe ratio ([[signals-that-trade-themselves|cf. Man Group]]).
- **[[autoresearch-broke-internet-greg-isenberg|Greg Isenberg's 10 business ideas]]** — niche "agent-in-a-box" products, A/B-testing agencies ("we run 100× more tests"), research-as-a-service, an "optimize" button inside your SaaS, finance-ops autopilot, done-for-you due-diligence.
- Non-business: clinical-trial design as hyperparameter search (medicine), self-improving system prompts.

## Vision & context
Karpathy frames autoresearch as the seed of **recursive self-improvement** — what all frontier labs (OpenAI, Anthropic, Google) already do internally, now open-sourced and democratized. His stated end-state is a **SETI@home for AI research**: millions of agents distributed across volunteer compute, steered toward chosen problems ("early stages of the singularity"). Endorsed publicly by Toby Lütke (Shopify) and the Stripe CEO. Companion project: **[[agent-hub]]** ("GitHub for agents"). Requires an NVIDIA GPU (H100 tested); rent via Lambda Labs / Vast / RunPod / Google Colab if you lack one.

## Sources & links
Sources: [[autoresearch-repo]] (the repo itself — README, `program.md`, `prepare.py`), [[autoresearch-tutorial-david-andre]], [[claude-code-karpathy-autoresearch-nick-saraev]], [[autoresearch-broke-internet-greg-isenberg]], and the origin interview [[skill-issue-karpathy-sarah-guo]].
Related: [[andrej-karpathy]], [[agent-hub]], [[nanochat]], [[agentic-workflows]], [[self-healing-workflows]], [[claude-code-scheduled-tasks]] (the run-while-you-sleep loop), [[claude-code]] / [[codex]] (the agents that drive it), [[eval-driven-model-selection]], [[selling-ai-automations]].
