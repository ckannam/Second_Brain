---
type: entity
category: tool
---
# nanochat

[[andrej-karpathy]]'s minimal, hackable LLM training/chat codebase. [[autoresearch]] ships a **simplified single-GPU implementation of nanochat** as its training target — the small GPT the agent iterates on (model + Muon/AdamW optimizer + loop live in `train.py`).

The full/parent nanochat repo has wider platform support (CPU/MPS, Flash-Attention-3 fallback, device autodetection); Karpathy points people running autoresearch on non-NVIDIA hardware to reference it. In the same lineage as his earlier teaching repos (nanoGPT) — small, readable, "the code is the lesson." Source: [[autoresearch-repo]].
