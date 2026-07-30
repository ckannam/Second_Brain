---
source: youtube
channel: "Anthropic"
url: "https://www.youtube.com/watch?v=EOg4gY0Yln0"
event: "Code with Claude"
speaker: "Sharan (Tushara) Fernando (Head of Data & AI, Man Group)"
created: 2026-07-24
---

# Building signals that trade themselves

Sharan Fernando (Head of Data & AI, [[man-group|Man Group]]) on getting AI-authored trading
signals into production at a regulated firm running real capital.

## The claim
There are trading signals **live in production**, running real capital, where **AI came up
with the idea, got the data, ran the backtest, wrote the strategy proposal, and
productionized the signal** — with humans reviewing all output. (The signal itself is IP,
undisclosed.)

## Systematic trading, briefly
A trading **signal** is like picking a fantasy-football squad: rank securities by some
**factor** (e.g. past-3-month returns), go long the top, short the bottom. You never know if
it works a priori, so you **backtest** over 15+ years of history and read statistical
factors — annualized return, **drawdown**, **Sharpe ratio**.

## What actually made it possible — the iceberg
Coming up with the signal is the quick, visible tip. The mass underneath is the **workflows**
that make it actionable: cleaning data, stitching prices, detecting outliers, infra, running
backtests. If different teams run different versions, results aren't comparable — you can't
tell a better *idea* from a different *measurement*. **Shared workflows fix that.** Claude
out of the box is a great generalist but "doesn't know us," so Man Group **taught it — not by
retraining, but via [[claude-code-skills|skills]]** + a core data layer, under a
**[[governed-skills-framework|governed skills framework]]** (~750 devs/quants, 100+ skills)
that lets compliance say yes on load-bearing workflows.

A concrete open-source example of the "signal" tip of this iceberg: [[kronos-financial-foundation-model|Kronos]],
a foundation model that forecasts price bars — its authors stress the same point (raw signals still need
backtesting, risk neutralization, and cost modeling to become tradeable alpha).

Related: [[the-briefing-financial-services]], [[self-healing-workflows]], [[claude-code]], [[kronos-financial-foundation-model]].

**Raw clip:** [[Building signals that trade themselves]]
