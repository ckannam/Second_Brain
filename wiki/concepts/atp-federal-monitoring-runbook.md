---
type: concept
category: runbook
created: 2026-11-08
about: "[[atp-federal-funding-landscape]]"
---

# ATP Federal Funding — Monitoring Runbook (the recurring `@cloud` check)

The **reusable procedure** behind the recurring `@cloud` task *"Monitor the monthly DSIP + AFWERX
pre-release (first Wednesday)"* in `tasks/index.md`. The [[atp-federal-funding-landscape]] page is the
**strategic map** (a point-in-time analysis); this page is the **runbook** — what to actually check
each cycle, where, with which keywords, and what counts as a hit. It exists because the Oct 4, Oct 11,
and Nov 8 2026 monitoring passes each re-derived the same steps from scratch; this captures them once
so every future first-Wednesday run is a fill-in-the-blanks execution, not a re-invention.

> **Scope:** this is the *watch-and-flag* procedure only. Deciding whether to submit to anything it
> surfaces is a Cole/Jaylen `@human` call — the runbook never commits ATP to an action.

## Cadence

**Run on the first Wednesday of each month** (when DSIP pre-releases the next SBIR/STTR cycle and
AFWERX posts Focused Open Topics on the same schedule). A mid-cycle run is fine; the first Wednesday
is the moment new topics appear and the topic-author (TPOC) contact window opens.

## The four surfaces to check

1. **DSIP (dodsbirsttr.mil)** — the month's SBIR/STTR release. Capture: release number, pre-release /
   open / close dates, topic count + component split, and **whether any topic matches ATP's lane**
   (keyword list below). DSIP **blocks automated access**, so expect to work from secondary indexers
   and **flag every claim for direct human verification** before the TPOC window closes.
2. **AFWERX Focused Open Topics** — same first-Wednesday cadence. Is there a **human-performance /
   readiness** FOT open? (As of Nov 2026, AFWERX's "Agile Combat & Readiness" focus has been
   manufacturing/logistics, not physical human performance — so a human-performance FOT is the signal
   worth escalating.)
3. **xTech (xtech.army.mil)** — any open open-topic prize competition (xTech|Search, xTech|Kinetic,
   etc.), its deadline, and — after a deadline passes — the **semifinalist announcement**. xTech is
   *not* on DSIP; submissions go through its own portal.
4. **SOCOM standing BAA (FY23–FY28, biomedical + human performance)** — the rolling, always-open
   vehicle (discovery@socom.mil). Check only for material changes; it is ATP's most direct standing
   mission-fit and is independent of the monthly cycle.

## Lane keywords (what counts as an ATP hit)

Search each surface for: **musculoskeletal / MSK · aircrew readiness · human performance · 711 HPW /
Human Performance Wing · biomechanics · markerless (pose/motion capture) · wearables / physiological
monitoring · injury risk / training load · sports medicine · strength & conditioning**. A topic is a
**hit worth escalating** only if it reads as *commander-facing readiness / availability monitoring*,
**not** clinical/rehab medicine (the [[atp-competitive-analysis]] wellness-safe reframe — which is
also what keeps ATP clear of xTech's Army-medical-command exclusion).

## Output each run

- Append a dated **`### 🔁 DSIP + AFWERX monitoring note — YYYY-MM-DD`** section to
  [[atp-federal-funding-landscape]] with the verified findings, and mirror the headline into §6 Caveats
  under "Independently ✅verified (web, YYYY-MM-DD)".
- Add a `⏳ progress YYYY-MM-DD` line to the task in `tasks/index.md`.
- **Flag, don't file, the unverifiable.** Where DSIP was inaccessible, write the finding as
  secondary-sourced and name the exact direct-verification step + its deadline (so a human can close
  it). Resolve prior-run "unknowns" explicitly when a later run confirms or dismisses them
  (e.g. Nov 8 resolved the Oct-11 "ARM27BX01-DP001" unknown as an EW topic, out of lane).

## Standing watchlist (carry forward each run)

| Vehicle | Type | Status as of 2026-11-08 |
|---|---|---|
| DSIP monthly SBIR/STTR | First-Wed release | FY27 R2 open Dec 2 (due Jan 6 2027); no HPW topic so far |
| AFWERX Focused Open Topics | First-Wed, as posted | No human-performance FOT open |
| xTech\|Search 10 | Prize comp (closed Oct 19) | Semifinalists pending — watch xtech.army.mil |
| 711 HPW CHEERS | Rolling white papers → Sep 30 2027 | Open; ATP's first AF artifact |
| SOCOM BAA (biomedical + HP) | Rolling FY23–FY28 | Open; most direct mission fit |
| ARL Foundational Research BAA | Rolling → Nov 20 2027 | Open; moderate fit |

Update this table in place each run (don't append a second copy).

Related: [[atp-federal-funding-landscape]] · [[atp-competitive-analysis]] · [[athletic-training-portal]]
· [[atp-nc-nondilutive-funding]] · [[xtech-search]] · [[Barbara Knight]] · [[vault-autoresearch]]
