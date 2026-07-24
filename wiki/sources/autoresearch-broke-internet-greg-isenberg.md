---
source: youtube
channel: "Greg Isenberg (Startup Ideas Podcast)"
url: "https://www.youtube.com/watch?v=qb90PPbAWz4"
title: "Karpathy's \"autoresearch\" broke the internet"
created: 2026-07-24
---
# Karpathy's "autoresearch" broke the internet (Greg Isenberg)

**Thesis:** a solo primer on [[autoresearch]] plus **10 concrete businesses** you could build on top of it, community reaction, Karpathy's companion launch **[[agent-hub]]**, and a step-by-step "how to actually run it."

## Mental model
"A super-nerd robot intern that runs science experiments while you sleep." You give a goal + define what *better* means (cheaper leads, more clicks, higher model score); the agent plans → acts → reads results → keeps only the winners → repeats. Generalizes beyond ML to any research/optimization loop (search, read, summarize, compare, repeat).

## The 10 business ideas
1. **Niche agent-in-a-box** products (Amazon-listing tuner, realtor email tuner, SaaS pricing optimizer) on subscription.
2. **A/B-testing for marketing** — landing pages & ad creatives as a retainer service.
3. **Research-as-a-service** — always-fresh competitor/market/compliance reports.
4. **"Optimize" button inside your own SaaS** — a wedge to upsell pro/enterprise.
5. **Agency that runs 100× more tests** — pitch = more experiments than any human shop, + performance fees.
6. **Auto-quant for trading** — overnight backtests; trade or sell signals.
7. **Always-on lead qualification** — score CRM leads, draft follow-ups.
8. **Finance-ops autopilot** — invoice matching, expense reports, exception detection.
9. **Internal productivity lab** — treat your company like Karpathy's GPU lab; iterate on workflows/KPIs.
10. **Done-for-you research / due-diligence shop** — living memos for investors/acquirers.

## Other notes
- Non-business angle (via Morgan Linton): **clinical-trial design as hyperparameter search** — agent swarms optimize protocols on cheap proxy experiments before humans review.
- **[[agent-hub]]** — Karpathy's follow-up: "GitHub for agents," a message board + bare git repo for a swarm on one codebase, no main branch / PRs / merges — a sprawling DAG of commits.
- **Getting started:** ask [[claude-code]] to walk you through install; needs an NVIDIA GPU (H100 tested) — rent via Lambda Labs / Vast / RunPod / Google Colab (he used Colab, T4 runtime). Repo had 25k+ stars at recording.

Entities: [[greg-isenberg]], [[andrej-karpathy]], [[agent-hub]], [[claude-code]]. Concepts: [[autoresearch]], [[selling-ai-automations]], [[ai-app-business]].
