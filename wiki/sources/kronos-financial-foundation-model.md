---
type: source
source: github-readme
title: "Kronos: A Foundation Model for the Language of Financial Markets"
authors: "Yu Shi, Zongliang Fu, Shuo Chen, Bohan Zhao, Wei Xu, Changshui Zhang, Jian Li"
repo: "https://github.com/shiyu-coder/Kronos"
paper: "https://arxiv.org/abs/2508.02739"
venue: "AAAI 2026"
created: 2026-07-29
raw: "raw/Processed/Kronos - Foundation Model for Financial Markets (shiyu-coder README).md"
---

# Source: Kronos — a foundation model for financial candlesticks

The GitHub README for **Kronos**, billed as the **first open-source foundation model for financial
candlesticks (K-lines)**, trained on data from **45+ global exchanges**. Paper on arXiv (Aug 2025),
accepted to **AAAI 2026**.

## The idea
Kronos treats **market price action as a "language"** and applies the LLM recipe to it. Instead of
text tokens, it models **K-line (OHLCV candlestick) sequences**. A **decoder-only autoregressive
Transformer** family, purpose-built for the high-noise nature of financial data (vs. general-purpose
time-series models). Two-stage design:
1. **Specialized tokenizer** quantizes continuous multi-dimensional OHLCV data into **hierarchical
   discrete tokens**.
2. A large **autoregressive Transformer** is pre-trained on those tokens → one model for many
   quantitative tasks (forecasting, etc.).

## Facts worth keeping
- **Model zoo** (open on Hugging Face, `NeoQuasar/…`): Kronos-**mini** (4.1M params, ctx 2048),
  **small** (24.7M, ctx 512), **base** (102.3M, ctx 512); **large** (499.2M) is **not** open-sourced.
- **Usage:** a `KronosPredictor` takes a historical OHLCV DataFrame + timestamps and forecasts future
  bars; forecasting is **probabilistic** (temperature `T`, nucleus `top_p`, `sample_count` paths).
- **Fine-tuning** pipeline via Microsoft **Qlib** (demoed on Chinese A-shares) with a top-K backtest.
- **Live demo:** 24-hour BTC/USDT forecast.

## Honest caveats (from the authors themselves)
- The demo signals are **raw predictions, not "pure alpha"** — a real workflow feeds them into
  portfolio optimization + risk-factor neutralization (beta, size, value) to isolate alpha.
- A credible backtest must model **transaction costs, slippage, and market impact**; the top-K demo
  is a starting point, not a production strategy.
- Some `finetune/` code comments were **AI-generated (Gemini 2.5 Pro)** and may be inaccurate.

## How it connects (why it's interesting)

**1. Domain-specific foundation models.** Kronos is a clean example of an emerging pattern: take the
transformer/foundation-model recipe and point it at a **non-language domain**. Sibling to
[[flourish|Flourish]] (the recipe aimed at the **brain**) and Chai ([[chai-hook-experiment]], aimed at
**antibodies/proteins**). Shared move: *tokenize a domain → pre-train autoregressively → forecast/generate.*

**2. Systematic / quant investing — the real second hook.** Kronos is a **signal generator**, and its
own caveats *are* the thesis of [[signals-that-trade-themselves]] ([[man-group|Man Group]]): the model's
forecast is only the **visible tip**; the mass underneath is the workflow that makes it tradeable —
backtests over 15+ yrs, **Sharpe / drawdown**, portfolio optimization, risk-factor neutralization, and
modeling transaction costs. Kronos hands you the tip; Man Group's point is that the iceberg is the work.
A good concrete artifact for the AI-authored-trading-signals space Cole is tracking.

**3. Contrast with his own plan.** Worth noting Kronos is **active/quant** trading — the opposite of
Cole's personal [[investment-plan|Freedom Engine]] ("time, not timing; simple aggressive portfolio").
So it's interesting-to-watch tech, not a nudge to change how *he* invests.

_Why saved (Cole, 2026-07-29): thinks it's cool — and it genuinely plugs into his **quant/AI-in-markets**
curiosity (the [[man-group]] / [[signals-that-trade-themselves]] cluster), not job search or a build._

**Raw clip:** [[Kronos - Foundation Model for Financial Markets (shiyu-coder README)]]
