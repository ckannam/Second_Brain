---
type: doc
category: JHTV / Capital Strategy
created: 2026-08-12
author: Cole Kannam
audience: Cole (reference) · shareable with Stewart / Oliver
status: draft
---

# How the Matching Rubric Works — Technical Reference

A complete account of how the Second Brain scores the fit between a Hopkins technology and an investor:
the formula, each component, the exact functions and data files behind it, how that data is produced, and
the known limitations. Repo: `ckannam/VC_Matching_Second_Brain` (static GitHub Pages site; all matching
runs client-side in the browser).

## Overview

Every technology–firm pair is scored to a single value in [0, 1], displayed as Strong, Good, or Possible.
The score is portfolio-led: over half of it comes from how well a firm's *actual* portfolio companies line
up with the technology by field and stage. The current rubric (v2) is:

```
Fit = 0.55 · Portfolio  +  0.30 · StageCheck  +  0.15 · Sector          
```

The guiding principle is that revealed behavior (what a firm has funded) beats stated preference (what a
firm says). The weights are tunable configuration; there is no validated fundraising-outcome data to fit
them against, so they were set by reviewing real rankings.

## Where everything lives (code + data map)

**Scoring logic (single source of truth):**
- `scoring.js` (repo root) — the entire rubric. Loaded by the browser via `<script defer>` and `require`d
  by Node scripts, with a `module.exports` guard so both use one copy. Key constants: `WEIGHTS =
  { portfolio: 0.55, stageCheck: 0.30, sector: 0.15 }`, `PORTFOLIO_K = 3`, `STATED_MAX = 0.75`. Key
  functions: `scoreVC` (dispatch), `vcFitScore` (v2), `portfolioFit`, `mapFocusToDomains`,
  `techStageScore`, `checkSizeScore`, `techStageToRung` / `companyStageToRung`, `selectWithTies`,
  `fitTier`, `vcFitScoreV1` (v1 fallback).
- `taxonomy.js` (repo root, generated) — the sector dictionary. Exports `VC_KEYWORD_TAXONOMY` (324 keyword
  entries, each `{ primary, secondary[] }`), `BUCKET_TO_DOMAIN` (crosswalk from 10 venture buckets to the
  8 JHTV domains; the 3 non-JHTV buckets map to `null`), `CYBER_KEYWORDS` (overlay), `DOMAIN_SELF_MAP`,
  `CATCH_ALL`. Loaded before `scoring.js`.
- `scripts/lib/deal_mapping.js` — `PB_INDUSTRY_TO_DOMAIN` (PitchBook industry label → JHTV domains),
  `dealTypeToStage`, `dealTypeToVcStage`, `deriveStageFocus`.

**Data the scorer reads (all under `data/`, fail-soft-loaded in `index.html`'s `loadData()`):**
- `technologies.json` — 74 technologies: `{ id, name, sectors[], stage, pi, description, cohort, onePager }`.
  `sectors[]` uses the 8 JHTV domain names; `stage` is a financing-round string. → `TECHS`.
- `vcs.json` — firm records (stated profile + provisional auto-researched entries):
  `{ id, name, aliases, focus, sectors, stage, matchedTechs, vcOnePager, geographicFocus,
  checkSize:{min,max}, provisional? }`. → `VCS`.
- `vc_portfolios.json` — **the 55% input.** Keyed by `vcId`:
  `{ vcId, sourceUrl, scrapedAt, note, companies:[{ name, domains[], stage? }] }`. 65 entries: 19
  hand-classified (real firm-website `sourceUrl`) + 46 derived (`sourceUrl:"pitchbook-deals"`). →
  `PORTFOLIO_BY_VC` (Map `vcId → companies`).
- `vc_recency.json` — per-VC, per-domain recency weight → `RECENCY_BY_VC`. **Tiebreak only**, never changes
  score.
- `vc_recent_deals.json` — 10 newest deals per firm → `RECENT_BY_VC` (powers the "recent activity" block, not
  scoring).
- `tech_status.json` — `{ pausedTechIds[] }` → `PAUSED` (Set). Paused techs are excluded from matching.
- `jhtv_investors.json` — JHTV backers (revealed co-investment; 299 venture/angel firms) → `INVESTORS_BY_VC`
  + `BACKERS_BY_COMPANY`. Drives the relationship signal and the "already invested in this tech" pin, not the
  base fit score.
- `jhu_connections.json` — JHU alumni at firms (827 people) → warm-intro paths (display, not scoring).
- `data/source/vc_deals.json` — committed deal source of truth (58 firms / ~2,872 deals) that the derived
  portfolios are built from.
- `vc_pitchbook.json` — standalone catalog of 391 PitchBook investors; **not loaded by the live UI** (a
  future benchmark source).

## The dispatch: `scoreVC(vc, tech, portfolioCompanies)`

One entry point routes every pair. If the firm has a non-empty portfolio array (`PORTFOLIO_BY_VC.get(vc.id)`),
it is scored by v2 (`vcFitScore`). Otherwise it falls back to v1 (`vcFitScoreV1`). The backend
`scripts/generate_vc.js` calls `scoreVC(vc, tech, undefined)` for a newly researched firm, so new firms
start on v1 until portfolio data is added.

## Portfolio (55%) — `portfolioFit(companies, tech)`

Input is the firm's `companies[]` from `vc_portfolios.json` and the technology's `sectors[]` + `stage`. The
function walks each company and assigns credit by field and stage proximity:

| Company vs. technology                           | Credit |
| ------------------------------------------------ | ------ |
|                                                  | 1.0    |
| Shares a domain, one rung apart                  | 0.75   |
| Shares a domain, stage unknown or ≥2 rungs apart | 0.5    |
| No shared domain                                 | 0      |

Stage rungs come from `companyStageToRung` (company round string) and `techStageToRung` (tech milestone
string) on a 0–5 ladder: pre-seed, seed, Series A, Series B, Series C, growth/late. Milestone tokens like
`pre-clinical`, `phase ii`, `clinical`, `commercial` map onto the same ladder so clinical-stage techs slot
in.

The per-company credits are summed into `credit`, then converted with a smooth saturating curve:

```
portfolioScore = 1 − exp( −credit / PORTFOLIO_K )        PORTFOLIO_K = 3
```

This replaced an older hard clamp (`min(1, credit/6)`) that pinned deep portfolios to a flat 1.0 (2048
Ventures had 21 techs tied at 1.0). The curve is monotonic in depth and asymptotic below 1.0, so more or
closer matches always score higher without ever ceiling out. `portfolioFit` also returns the uncapped
`depth` (= `credit`) used later as a tiebreak. Reference points: credit 1 → 0.28, 3 → 0.63, 5 → 0.81, 8.5 →
0.94, 14 → 0.99. Crossing into Strong (0.80) on the portfolio term alone takes ≈ 4.8 credit (roughly five
same-stage matches).

## StageCheck (30%) — `0.5 · techStageScore + 0.5 · checkSizeScore`

**Stage half — `techStageScore(vc.stage[], tech.stage)`.** Firm-level and near pass/fail: if the tech's
stage falls in a range the firm invests at, it returns 1.0; otherwise 0.2 (0.5 if the tech has no stage).
The compatibility map is slightly generous — each firm stage also covers the adjacent stage and the
equivalent clinical milestones (a `series a` firm is compatible with a Series A tech and a late-seed one,
plus `phase i/ii`, `clinical`). For firms with deal data, `vc.stage[]` is not hand-stated but derived from
their deals by `deriveStageFocus` (stages ≥10% of their rounds, written into `vcs.json` by the pipeline).
Only no-data firms use a hand-entered stage.

**Check-size half — `checkSizeScore(vc, techDomains)`.** A heuristic: it reads the tech's field maturity
(`DOMAIN_MATURITY`) and checks whether the firm's `checkSize:{min,max}` fits that maturity band (early-stage
fields want smaller checks, etc.), returning 1.0 or 0.4. This is a proxy, and the explicit upgrade path is
to slot real PitchBook round-size benchmarks in here behind a data-present guard.

## Sector (15%) — `mapFocusToDomains(focusStrings)` + the taxonomy

Two separate translators feed the 8 JHTV domains, because two different inputs need normalizing.

**Stated focus → domains (drives this 15% term).** A firm's `focus`/`sectors` text runs through the
324-keyword dictionary in `taxonomy.js`. `mapFocusToDomains` normalizes each string (`normalizeFocus`),
matches keywords on whole-word boundaries (`hasPhrase`, so "ai" doesn't fire inside "supply chain"), keeps
the most specific keyword when several overlap, and sorts the results into a **primary** set and a
**secondary** set via each entry's `{ primary, secondary[] }`. Buckets crosswalk to JHTV domains through
`BUCKET_TO_DOMAIN` (non-JHTV buckets → `null`, contribute nothing); `CYBER_KEYWORDS` re-points cyber terms
to the Cybersecurity domain; `DOMAIN_SELF_MAP` lets the 8 domain names round-trip. A domain proven primary
is removed from secondary. The score in `vcFitScore`:

| Overlap of tech domains with the firm's focus | Sector score |
|---|---|
| In the firm's **primary** set | 1.0 |
| Only in the **secondary** set | 0.5 |
| No overlap, but a `CATCH_ALL` term matched ("healthcare", "deep tech") | 0.5 |
| None | 0 |

A single primary overlap earns the full mark regardless of how many categories the firm lists, and
multi-domain techs are not penalized. The term is deliberately a simple "in this space or not" signal;
concentration is left to the portfolio term.

**PitchBook deal labels → domains (feeds the portfolio companies).** When a portfolio is derived from deal
data, each deal's company domain comes from `PB_INDUSTRY_TO_DOMAIN` in `deal_mapping.js` (e.g.
`Biotechnology → Therapeutics`, `Diagnostic Equipment → Diagnostics + Medical Devices`). Labels outside
JHTV's fields map to `[]` and are dropped, so a firm's unrelated deals are ignored (and, thanks to the
saturating count, harmless). The deal type maps to a stage via `dealTypeToStage`. This is a fixed,
label-based rule, which is what lets a live PitchBook feed flow straight into `portfolioFit` unchanged.

## Missing data — evidence renormalization + the cap

`vcFitScore` scores whatever evidence exists and records a `basis`:
- stated profile **and** portfolio → `0.55·P + 0.30·SC + 0.15·Sec` (`basis:'full'`)
- portfolio only → `P` (`basis:'portfolio'`)
- stated only → `(0.30·SC + 0.15·Sec) / 0.45`, then **capped at `STATED_MAX` = 0.75** (`basis:'stated'`)
- neither → `null` (dropped)

The 0.75 cap is the enforcement mechanism for the core principle: with no portfolio evidence, a firm cannot
reach Strong (≥ 0.80).

## Tiers, ranking, ties — `fitTier`, `selectWithTies`

`fitTier`: ≥ 0.80 Strong, ≥ 0.60 Good, else Possible; the UI floor for inclusion on a tech's list is 0.45.
Ranking sorts by `score`, then a tiebreak `tieKey = depth × domain-recency` (`RECENCY_BY_VC`; recency is
ordering-only and never changes the score), then name. `selectWithTies(ranked, {base:4, max:6})` shows the
top 4 but extends to 6 only when the trailing items are genuinely indistinguishable (|Δscore| and |ΔtieKey|
< 0.005), flagging that cluster so the UI labels it "equally strong — not rank-ordered." Scores render as a
decimal beside the tier (e.g. `Strong fit · 0.86`).

## How it's invoked in the app

- **Tech → firms (`findVCsForTech` in `index.html`):** ranks all firms by `scoreVC(vc, tech,
  PORTFOLIO_BY_VC.get(vc.id))`, keeps those ≥ 0.45 (or an "In VC brief" match, which gets a gold badge and
  a +0.1 sort bonus), shows top 4 + "show more." Firms in `jhtv_investors.json` that funded this exact tech
  (`BACKERS_BY_COMPANY`) pin to the top with an "already invested" badge; other resolved backers get a
  capped +0.1 `relationshipBonus`.
- **Firm → techs (`topTechsForVC(vc, n=4)`):** ranks all active techs (`TECHS` minus `PAUSED`) by the same
  scorer with no floor, so it always returns 4 (via `selectWithTies`, 4–6). `vc.pinnedTechs` can force a
  curated tech onto a firm's page at its real score.
- **Backend (`generate_vc.js`):** new firms are scored via v1 (`scoreVC(..., undefined)`) until portfolio
  data exists.

## How the data is produced (pipelines)

- **Deal-derived portfolios (the 46 `pitchbook-deals` entries):** PitchBook export →
  `vc json deal histories/by_firm/*.json` (gitignored staging) → `scripts/merge_backer_deals.js` →
  `data/source/vc_deals.json` → `scripts/build_deal_derived.js` → derived `vc_portfolios.json` entries +
  `vcs.json` `stage` for those firms + `vc_recent_deals.json`. Uses `scripts/lib/deal_mapping.js` and
  `scripts/lib/deals_firm_to_vcid.js`. Rerun only when deal data changes — adding techs needs no
  re-derivation, since matching recomputes client-side. The 19 hand-classified portfolio entries are
  preserved across reruns.
- **Sector taxonomy:** `data/source/VC_Keyword_Taxonomy_Venture_Grade.xlsx` → `npm run convert-taxonomy`
  (`scripts/convert_keyword_taxonomy.js`) → `taxonomy.js`. The crosswalk/overlay is edited in the converter,
  never in the generated file.
- **JHU warm-intro network:** `~/Documents/JHU VC DATABASE/JHU_VC_Network.xlsx` →
  `scripts/convert_jhu_connections.js` → `jhu_connections.json` (manual today; a live SharePoint/Graph sync
  is specced but not built).
- **JHTV backers:** `data/source/Venture_Funding_-_Grouped_By_Investor.xlsx` → `npm run convert-jhtv-investors`
  → `jhtv_investors.json`.

## Known limitations and where a live feed changes things

- **Breadth is the hardest case.** A broad firm earns the full 15% sector mark from one primary overlap, and
  a firm with a large, diverse portfolio can score high on many techs at once. The saturating curve and the
  tiebreakers soften it, and the portfolio term is meant to carry the burden of rewarding focus, but a very
  broad fund remains the least discriminating input.
- **The score depends on data coverage.** Because `portfolioFit` rewards the absolute count of matching
  deals (via `credit`), a firm with only a handful of deals on file is unlikely to score high even when it
  is a strong fit, while a firm with a deep captured history has more chances to accumulate credit. In
  effect the score partly reflects how complete our data on a firm is. This is largely an artifact of
  today's uneven, hand-entered data; a complete feed removes most of it. The permanent version of the
  question — comparing a small focused firm against a large one — is best solved by making the portfolio
  term **size-aware**: score the share of a firm's deals that fit, and/or apply small-sample shrinkage so a
  2-of-2 firm cannot look like a 50-deal firm. Because the curve is isolated configuration (`PORTFOLIO_K`
  and `portfolioFit`), this is a tuning change, not a rebuild.
- **Check size is still a heuristic** (`checkSizeScore` uses field maturity as a proxy, not real round
  sizes).

The engine is already built to reward revealed behavior; its main weaknesses are consequences of
incomplete data. A live PitchBook feed puts every firm on the portfolio-led v2 path with complete, current
deal history (flowing through `PB_INDUSTRY_TO_DOMAIN` into `portfolioFit`), supplies real round-size
benchmarks for `checkSizeScore`, and keeps everything current as firms raise new funds. What remains after
that is deliberate tuning — most importantly the size-aware portfolio change — which the design already
accommodates.
