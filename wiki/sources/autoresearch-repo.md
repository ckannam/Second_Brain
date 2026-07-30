---
source: github
url: "https://github.com/karpathy/autoresearch"
title: "karpathy/autoresearch — README, program.md, prepare.py"
created: 2026-07-24
---
# karpathy/autoresearch (the repo)

**Primary source.** The GitHub repo behind [[autoresearch]], by [[andrej-karpathy]] (March 2026). This page consolidates the clipped repo files: `README.md`, `program.md` (agent instructions), and `prepare.py` (the fixed eval harness). The concept page [[autoresearch]] carries the full synthesis; this records what the repo itself literally specifies.

## What it is
Give an AI agent a small but real LLM training setup (a single-GPU simplification of [[nanochat]]) and let it experiment autonomously overnight. It edits code, trains 5 min, checks if the result improved, keeps or discards, repeats. The repo README opens with a tongue-in-cheek "10,205th generation" fable framing this as the origin story of autonomous AI research.

## The three files (README)
- **`prepare.py`** — fixed constants, one-time data prep (downloads shards from `karpathy/climbmix-400b-shuffle`, trains a BPE tokenizer, vocab 8192), dataloader, and `evaluate_bpb`. Marked **"DO NOT CHANGE — this is the fixed metric."** Not modified.
- **`train.py`** — the **only file the agent edits**: full GPT model, optimizer (Muon + AdamW), training loop. Architecture/hyperparams/batch size all fair game.
- **`program.md`** — human-edited agent instructions ("essentially a super lightweight skill").

## Fixed rules (`prepare.py` constants)
- `TIME_BUDGET = 300` (5 min wall-clock per experiment) · `MAX_SEQ_LEN = 2048` · `VOCAB_SIZE = 8192` · `EVAL_TOKENS = 40 * 524288`.
- Metric = **`val_bpb`** (bits per byte), vocab-independent → architecture changes compare fairly.
- Fixed budget ⇒ ~12 experiments/hr, ~100 overnight; results become platform-specific (not comparable across machines).

## `program.md` — the agent loop
Setup: agree a run tag, `git checkout -b autoresearch/<tag>`, read `README`/`prepare.py`/`train.py`, verify data in `~/.cache/autoresearch/`, init `results.tsv` header. Then **LOOP FOREVER**: hack `train.py` → commit → `uv run train.py > run.log 2>&1` → `grep "^val_bpb:"` → log to `results.tsv` (keep|discard|crash) → improved? advance branch : `git reset`. Guardrails: **NEVER STOP** to ask the human; kill runs > 10 min; a **simplicity criterion** (complexity must earn its keep); VRAM is a soft constraint.

## Running it
"Spin up your Claude/Codex in this repo (disable all permissions), then prompt: *'have a look at program.md and let's kick off a new experiment.'*" Requirements: one NVIDIA GPU (H100 tested), Python 3.10+, `uv`. Fork guidance exists for smaller machines (TinyStories data, lower `DEPTH`/`MAX_SEQ_LEN`/`VOCAB_SIZE`).

## Notes
- Clipped repo files included a near-empty GitHub-UI capture of `analysis.ipynb` (a results-plotting notebook) and the full `prepare.py` source; both fold into the summary above rather than warranting their own pages.
- Companion project referenced by the community: **[[agent-hub]]**.

Entities: [[andrej-karpathy]], [[nanochat]], [[agent-hub]], [[claude-code]], [[codex]]. Concepts: [[autoresearch]], [[self-healing-workflows]], [[eval-driven-model-selection]].

**Raw source clips:** [[karpathyautoresearch AI agents running research on single-GPU nanochat training automatically]] · [[karpathyautoresearch AI agents running research on single-GPU nanochat training automatically 1]] · [[karpathyautoresearch AI agents running research on single-GPU nanochat training automatically 2]] · [[karpathyautoresearch AI agents running research on single-GPU nanochat training automatically 3]] · [[karpathyautoresearch AI agents running research on single-GPU nanochat training automatically 4]]
