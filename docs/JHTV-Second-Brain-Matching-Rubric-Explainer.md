---
type: doc
category: JHTV / Capital Strategy
created: 2026-08-12
author: Cole Kannam
audience: Cole (reference) · shareable with Stewart / Oliver
status: draft
---

# How the Matching Rubric Works

A reference for how the Second Brain scores the fit between a Hopkins technology and an investor. It
covers the model, each component, the design principles behind it, the known limitations, and where a
live data feed changes things.

## In plain terms first

Every technology–firm pair gets one score between 0 and 1, which is shown as Strong, Good, or Possible.
The score rewards, above all, what a firm has *actually funded*: more than half of it comes from how well
the firm's real portfolio companies line up with the technology by field and by funding stage. The rest
comes from whether the firm invests at the right stage and check size, and a small amount from how the
firm describes its own focus. The guiding principle throughout is that what a firm has done outweighs what
a firm says.

## The model

Each firm is scored by one of two rubrics. A firm with portfolio (deal) data on file is scored by the
current rubric, v2. A firm with only a stated profile and no portfolio falls back to the older v1. The v2
rubric is:

```
Fit = 0.55 · Portfolio  +  0.30 · StageCheck  +  0.15 · Sector
```

Geography was removed from scoring (it is still displayed as background information). The weights live in
one place in the code and are meant to be tuned, since there is no validated fundraising-outcome data to
fit them against.

## Portfolio (55%) — the dominant term

This scores the firm's actual portfolio companies against the technology. The tool goes company by
company and asks two questions: is this company in the same field as the technology, and is it at a
similar funding stage. Each company earns credit accordingly:

| Company vs. technology | Credit |
|---|---|
| Same field, same stage | 1.0 |
| Same field, one stage apart | 0.75 |
| Same field, stage unknown or far apart | 0.5 |
| Different field | 0 |

Stage proximity is measured on a ladder (pre-seed, seed, Series A, Series B, Series C, growth), so "one
stage apart" means one rung. A company in an unrelated field contributes nothing at all.

The per-company credits are summed into a total, and the total is converted to a 0–1 score through a curve
with diminishing returns rather than a straight sum. The effect is that the first few matching companies
move the score a great deal, each additional match moves it less, and the score approaches but never
reaches 1.0. The curve is governed by a single constant, currently set to 3, which was tuned by reviewing
real firms: it takes roughly five solid matches for the portfolio term to cross into "Strong," and it
keeps deep portfolios from all piling up at a perfect score (a very deep portfolio lands near 0.99 while a
mid-depth one lands near 0.94, so they remain distinguishable).

Rough reference points for how a firm's total credit maps to the portfolio score: 1 point ≈ 0.28, 3 points
≈ 0.63, 5 points ≈ 0.81, 8.5 points ≈ 0.94, 14 points ≈ 0.99.

## StageCheck (30%) — stage and check size

This term is half a stage test and half a check-size test.

The stage test here is firm-level and close to pass/fail. If the technology's stage falls within a stage
range the firm invests at, the firm gets the full mark; if not, it drops to a low floor of 0.2. The
compatibility ranges are slightly forgiving, since each stage a firm invests at also covers the adjacent
stage and the equivalent clinical milestones, so a Series A firm is treated as compatible with a Series A
technology as well as a late-seed one. This is distinct from the graded, per-company stage measurement
inside the portfolio term above.

For firms with deal data, the firm's stage range is not taken from a stated profile but derived from their
deals, keeping the stages that make up at least ten percent of their rounds. Only a firm with no deal data
at all uses a hand-entered stated stage.

The check-size half is still a heuristic based on how mature the technology's field is, rather than real
round data. It is the clearest place a PitchBook feed would upgrade the rubric, by supplying actual
round-size benchmarks to compare against a firm's check size.

## Sector (15%) — the taxonomy

The technology catalog uses eight clean JHTV domains (Therapeutics, Diagnostics, Medical Devices, Digital
Health, Research Technologies, Clean Tech, Agricultural Tech, Cybersecurity). Two different translators
convert messier inputs into those eight domains.

The first translator handles a firm's *stated focus* text. Investor self-descriptions ("oncology," "ADC
platform," "AI in healthcare") run through a dictionary of a few hundred industry terms. Each term maps to
a **primary** bucket, where the term really lives, and to **secondary** buckets, the adjacent territory it
reaches into. For example, "ADC" is primarily Therapeutics with Diagnostics secondary, and "cancer" is
primarily Therapeutics with Diagnostics, Digital Health, and Medical Devices secondary. The dictionary's
buckets crosswalk down onto the eight JHTV domains; categories JHTV does not commercialize contribute
nothing.

The sector score then depends on where the technology's field lands for the firm:

| Overlap between the technology's field and the firm's focus | Sector score |
|---|---|
| The technology is in one of the firm's primary buckets | 1.0 |
| The technology is only in a secondary bucket | 0.5 |
| No bucket overlap, but the firm used a broad catch-all term ("healthcare," "deep tech") | 0.5 |
| No overlap | 0 |

A single primary overlap earns the full sector mark, regardless of how many categories the firm lists, and
a technology in two fields is not penalized as long as either field is a primary match. This term is
deliberately a simple "is the firm in this space" signal; measuring genuine focus is left to the portfolio
term.

The second translator handles a firm's *actual deals* when the portfolio comes from PitchBook. PitchBook
already tags every deal with an industry label, and a fixed table maps the relevant labels onto the eight
domains ("Biotechnology" to Therapeutics, "Diagnostic Equipment" to Diagnostics and Medical Devices, and
so on). Any label outside JHTV's fields maps to nothing and is dropped, so a firm's unrelated deals are
simply ignored. The deal type ("Series A," "Seed," "Later Stage") is mapped to a stage at the same time.
This table is a fixed, label-based rule rather than a judgment call, which makes it reproducible and lets a
live PitchBook feed flow straight into the portfolio term without any change to the scoring.

## Handling missing data

The rubric scores whatever evidence exists rather than penalizing gaps. A firm with both a stated profile
and a portfolio is scored on the full formula. A firm with a portfolio but no stated profile is scored on
the portfolio term alone. A firm with only a stated profile and no portfolio is scored on the stage and
sector terms, rescaled, and then **capped at 0.75**, which sits at the top of the "Good" band. That cap is
the mechanism that enforces the core principle: a firm with no portfolio evidence can never earn a
"Strong" rating, because there is nothing revealed to justify it.

## Tiers, ranking, and ties

Scores map to tiers at 0.80 (Strong) and 0.60 (Good), with anything below 0.45 excluded from a
technology's list. Within a tier, matches are ordered by score, then by a tiebreak that combines portfolio
depth with how recently the firm invested in the technology's field (recency only orders ties, it never
changes the score), then by name. When several matches are genuinely indistinguishable at the top, the
tool shows the cluster and labels it "equally strong" rather than inventing an order.

## The v1 fallback

A firm with no portfolio data at all is scored by v1, a simpler two-part formula of 0.60 sector plus 0.40
stage, using an older fixed keyword table. It exists so that firms the tool has only just researched still
get a reasonable placement, but it is the weaker path, and moving firms off it onto the portfolio-led v2 is
exactly what more deal data accomplishes.

## Known limitations and where this is headed

- **Breadth is the hardest case.** A broad firm earns the full sector mark from a single primary overlap,
  and a firm with a large, diverse portfolio can score highly on many technologies at once. The
  diminishing-returns curve and the tiebreakers soften this, and the portfolio term is meant to be the
  thing that rewards genuine focus, but a very broad fund is still the least discriminating input.
- **The score depends on data coverage.** Because the portfolio term rewards the absolute count of
  matching deals, a firm with only a handful of deals on file is unlikely to score high even when it is a
  strong fit, while a firm with a large captured history has more chances to accumulate credit. In effect
  the score partly reflects how complete our data on a firm is. This is largely an artifact of today's
  uneven, hand-entered data, and a complete deal feed removes most of it. The remaining, permanent version
  of the question, how to fairly compare a small focused firm against a large one, is best solved by making
  the portfolio term size-aware, either by scoring the share of a firm's deals that fit or by adjusting for
  small samples so a firm with two deals cannot look identical to one with fifty. Because the scoring curve
  is isolated configuration, this is a tuning change rather than a rebuild.
- **Check size is still a heuristic.** It uses field maturity as a proxy rather than real round sizes.

The through-line is that the engine is already built to reward revealed behavior, and its main weaknesses
are consequences of incomplete data. A live PitchBook feed puts every firm on the portfolio-led path with
its complete, current deal history, supplies real round-size benchmarks for the check-size term, and keeps
the whole thing current as firms raise new funds and shift direction. What remains after that is
deliberate tuning, most notably making the portfolio score size-aware, which the design already
accommodates.
