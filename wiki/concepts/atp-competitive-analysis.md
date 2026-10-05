---
type: concept
category: analysis
created: 2026-09-27
about: "[[athletic-training-portal]]"
---

# ATP Competitive Analysis (athlete-biometrics injury-prevention)

**Audience:** ATP internal strategy (Jaylen + team). Frank, warts-and-all. Purpose: sharpen
positioning, GTM, and the honest answer to "where does ATP actually win, and where must it
clear a bar someone has already set?" Built on the method in the sector-specific competitive
-analysis guide (four-ring map + capability matrix + **evidence audit** + **regulatory posture**
+ **data-rights audit** + Five Forces + honest 2×2). Companion to [[athletic-training-portal]]
and the [[dorm room fund]] pick.

> **Data note.** Figures below are web-sourced (Sept 2026) and cited inline; nothing is invented.
> **Funding/valuation for Zone7, Svexa, Kitman, Hudl, Teamworks is now confirmed from PitchBook**
> (via Cole, Sept 2026 — see §3a); other private-player funding lines remain public-source placeholders.
> Duke's Euromonitor / IBISWorld / Capital IQ and practitioner interviews are flagged as manual follow-ups.

---

## 0. Executive summary — where ATP wins and where it's behind

**What ATP is:** a **single-smartphone-camera, markerless-pose** platform that steps through
footage to pull ~18 goniometric joint-angle measures, builds an **individualized baseline**, and
flags mobility/symmetry/movement-quality **deviations over time** — college-first (Duke football,
baseball, wrestling; NCCU track), FERPA-oriented, NC-incorporated, with a **Navy SBIR** ("Aircrew
Readiness Fingerprint") second front. See [[athletic-training-portal]].

**Where ATP genuinely wins (defensible wedges):**
1. **Truly phone-only, zero-setup capture.** ATP needs *one* camera. The academic free option
   ([[OpenCap]]) needs **two+** phones; the FDA-cleared incumbent ([[DARI Motion]]) and
   [[Kinetisense]] lean on dedicated sensors/capture stations. Lowest friction wins the sideline.
2. **College-native + FERPA-first + longitudinal baseline framing.** The NCAA's **Dec 15, 2025**
   performance-technology guidance now *requires schools to have a written data plan* — ATP can be
   the compliance-native default while consumer/pro-first players retrofit.
3. **Founder–market fit.** Jaylen (ex-Duke football + BME) embedded in Duke Athletics; advisors
   Dickens (military sports med) and Luck (Duke BME biomechanics) map directly onto the SBIR bet.
4. **DoD/SBIR wedge** = non-dilutive capital + a second market **[[Oura]]/Sparta already proved**
   exists (Trinsic serves government incl. US Air Force). *(Keep confidential per DRF flag.)* The full
   federal-customer map beyond the Navy SBIR — xTech|Search 10, the 711th HPW, SOCOM/POTFF, MTEC — is
   its own analysis at **[[atp-federal-funding-landscape]]** (Oct 2026).

**Where ATP must clear a bar someone else already set:**
- **Evidence.** The whole field is thin (see §4), but **[[DARI Motion]] holds "the world's only
  FDA-cleared markerless motion analysis"** and validates *kinetics*, not just kinematics. ATP has
  neither clearance nor a prospective validation yet. This is simultaneously ATP's biggest gap and
  its biggest opportunity (§4, §10).
- **The "predict injuries before they happen" claim is FDA device-line risk.** This is exactly the
  language that got **WHOOP** a warning letter (§5). De-risk the wording now.
- **Scale/funding gap is stark.** Closest direct rival **[[Uplift Labs]]** hit ~20,000 athletes
  across MLB/NBA/NCAA in 2025; WHOOP is a $10.1B company; Catapult books $140M revenue. ATP is
  pre-seed with pilots. Buyer power in elite team sport is brutal (§7).

**One-line strategy:** *Don't out-feature Catapult/Kitman. Own "one phone, zero setup, your own
baseline over time," make college/NCAA/FERPA compliance a moat, and win the evidence war nobody
else has won (external validation) — that combination is ATP's, and Cole's, real edge.*

---

## 1. The four-ring competitor map

Injury-prevention biometrics is not one list. ATP competes in four concentric rings, and the
mistake would be benchmarking only Ring 1.

| Ring | Players | Why they compete with ATP |
|---|---|---|
| **1 — Direct: movement analysis / injury-risk AI** | [[Uplift Labs]], [[DARI Motion]], [[Kinetisense]], [[OpenCap]], [[Zone7]], [[Kitman Labs]], [[Svexa]] | Same job-to-be-done: "tell me who's at risk and what to change" from movement/biometric data |
| **2 — Data-capture platforms moving up-stack** | [[Catapult]], [[Kinexon]], STATSports, Polar, Firstbeat, K-Sport/SPT | They own the sensor data + the team relationship and add analytics on top |
| **2b — Athlete ops / video / engagement platforms (own the relationship)** | [[Teamworks]] ($1.5B, Durham NC), [[Hudl]] ($900M, video-to-insight), [[Kitman Labs]] (EMR) | Own the athlete record, video, and workflow — the layer that actually captures value & the realistic acquirers |
| **3 — Consumer/prosumer wearables → teams** | [[WHOOP]], [[Oura]], Garmin, Apple | Win athletes directly; HRV/sleep/recovery commoditizing; build enterprise/team tiers |
| **4 — Substitutes / status quo** | In-house sports scientists, Excel/R/Python, AMS ([[Teamworks]], Smartabase/Fusion Sport, EDGE10), force plates (Hawkin), lab mocap (Theia, Simi), **[[OpenCap]] (free)** | "Do nothing new" is the most common competitor in team sport |

**ATP's true peer set is Ring 1's markerless-video sub-cluster** — Uplift, DARI, Kinetisense,
OpenCap — because they share ATP's core mechanism (camera → pose → joint angles). Zone7/Kitman are
adjacent (they *ingest* data or run the medical record, they don't capture movement from video).

---

## 2. Ring 1 in detail — ATP's real rivals

### The markerless-video cluster (share ATP's mechanism)

- **[[Uplift Labs]]** — *the one to watch.* AI 3D motion capture from an **iPhone**; markets
  "replaces $50,000 motion-capture labs at 90% lower cost." Scaled to **~20,000 athletes in 2025**,
  serving pro teams across **MLB, NBA, and NCAA**; algorithms "identify high-risk patterns before
  injury." Named to **Fast Company's Most Innovative Companies 2026**. → Same pitch as ATP, further
  along, better funded. ATP must differentiate on **single-camera + college/FERPA + baseline-
  longitudinal + DoD**, not on generic "AI movement analysis."
- **[[DARI Motion]]** — *the regulatory-moat incumbent.* "The world's **only FDA-cleared** markerless
  motion analysis," delivering validated **3D kinematics AND kinetics** with no sensors/markers/force
  plates (built on Captury software); ~5-min assessment, results to cloud in <20s. Used by the **NFL**
  and by hospitals for post-surgical / neuro / ortho rehab. → DARI already holds the two things ATP
  lacks: FDA clearance and validated force/kinetics. Study cheaply, learn from their claims discipline.
- **[[Kinetisense]]** — "world's first patented markerless motion capture," **single front-facing 3D
  sensor**; KAMS screens **12 evidence-based movements in 3 minutes**, tri-planar. Sells into clinics,
  **student-athletes, and school districts**. → Closest analog to ATP's screening UX; note their
  "evidence-based movements" framing and clinic/education GTM.
- **[[OpenCap]]** — *free substitute.* Open-source, Stanford (Delp lab), released 2023;
  **2,000+ researchers**, tens of thousands of trials. Estimates 3D kinematics/dynamics from **2+
  smartphones**. Founders (Uhlrich, Falisse) spun out a commercial company. → The "why pay?" anchor
  and a credibility bar. ATP's answer: single-camera, turnkey, compliant, coach-facing (not a research
  tool needing two tripods and OpenSim expertise).

### The analytics/medical-record adjacents

- **[[Zone7]]** — AI **injury-risk forecasting**, explicitly **device-agnostic** (ingests others'
  data). ~30+ pro franchises (Liverpool, Napoli, LAFC). **PitchBook: raised $10.70M lifetime** across
  7 deals — the meaningful round was an **$8.20M Early-Stage VC (Jun 2021, 11 investors)** atop a $2.5M
  seed (2019); post-money undisclosed; only **24 employees (2025)**; HQ Newark, DE. **Acquired by
  [[Svexa]] 12-Apr-2024** — and Svexa is itself tiny (**$6.61M raised**, latest a $3.75M Later-Stage
  round Aug 2026). Zone7's **"Predicting and mitigating athlete injury risk" patents (CPC G16H50/30,
  family 77747997) are all now _Inactive_** — the category leader let its IP lapse. Validation is
  **retrospective across 11 football teams and explicitly "not intended as peer-reviewed research."**
  → The purest "prediction" claim in the space, a template for how *not* to overclaim — and living
  proof (see §3a) that a **standalone injury-predictor is a hard venture business**.
- **[[Kitman Labs]]** — performance-medicine **EMR + intelligence platform ("iP")**; wins **league-
  wide** deals (Premier League EPPP academies, USL Championship, UFL, RFU/Premiership Rugby) and is used
  across NFL/NBA/MLS/NWSL/NCAA; "2,000+ organizations." **PitchBook:** founded **2012, Dublin**; CEO
  **Stephen Smith** (co-founders Jason Cowman, Iarfhlaith Kelly); **$82.3M raised** incl. a **$52.23M
  Series C led by Guggenheim Investments (Nov 2021, post-money $146.14M)**; other backers BlueRun
  Ventures, Crescent Cove; 180 employees. **Itself a consolidator — acquired Presagia Sports and The
  Sports Office** (athlete-data-management SaaS), and PitchBook's VC Exit Predictor tags it **M&A /
  93% success probability**. → Owns the *medical record and league procurement*, a layer ATP doesn't
  touch — the clearest **integration-partner / acquirer** in the space, not a head-to-head. Its buy-side
  history (buying the athlete-data layer) is the template for how ATP could get acquired.

---

## 3. Capability matrix (the core artifact)

Grade honestly. Columns that matter: capture mechanism, device-agnostic?, output (descriptive →
predictive), primary market, **evidence**, **regulatory status**, **data governance posture**.

| Player | Capture | Device-agnostic? | Output altitude | Primary market | Evidence grade | Regulatory | Data governance |
|---|---|---|---|---|---|---|---|
| **ATP** | **1 phone camera**, markerless pose → ~18 joint angles | Own capture | Descriptive baseline → *aspiring* predictive | **College** (+ DoD) | ⚠️ None published yet | Wellness (uncleared) | **FERPA-first**, de-identified |
| Uplift Labs | iPhone, 3D markerless | Own capture | Predictive ("high-risk patterns") | Pro + NCAA | Vendor/testimonial | Wellness | Team-held |
| DARI Motion | Markerless, kinematics **+ kinetics** | Own capture | Descriptive + clinical | Pro + **clinical/hospital** | Validated + **FDA-cleared** | **FDA-cleared** | Clinical (HIPAA-side) |
| Kinetisense | Single 3D sensor | Own capture | Screening + descriptive | **Clinics, schools** | "Evidence-based" (vendor) | Clinic-grade | Clinic-held |
| OpenCap | 2+ phones | Own capture (open) | Research kinematics/dynamics | **Academia** (free) | **Peer-reviewed (research)** | N/A (research) | Researcher-held |
| Zone7 | **None** (ingests) | ✅ Device-agnostic | **Predictive** forecast | Pro football | Retrospective, not peer-reviewed | Wellness | Ingests club data |
| Kitman Labs | Ingests + EMR | ✅ | Descriptive + EMR ops | **Leagues/pro** | Vendor ("30–50%") | EMR (medical) | League/club EMR |
| Catapult | GPS/IMU + video | Own hardware | Descriptive load + video | **Pro teams** | Practitioner-accepted | Wellness | Team-held |
| WHOOP | Wrist strap | Own hardware | Recovery/HRV; ECG | **Consumer** → teams | FDA-cleared ECG; BPI saga | **FDA-cleared ECG** | Athlete-owned (NFLPA) |
| Oura | Ring + Trinsic | Ring + ingests | Recovery + enterprise | **Consumer + gov/enterprise** | Mixed | Wellness | Enterprise/gov |

**Read-out:** ATP's row is strong on *capture friction* (one phone) and *governance* (FERPA-first),
weak on *evidence* and *regulatory* — the two columns VCs and athletic-department buyers probe hardest.

---

## 3a. Funding & valuation snapshot (PitchBook, via Cole — Sept 2026)

| Company | Layer | Total raised | Post-money val | Employees | HQ |
|---|---|---|---|---|---|
| **[[Zone7]]** | Injury-prediction AI | **$10.70M** (7 deals; $8.2M Early-Stage Jun-2021) | undisclosed | 24 (2025) | Newark, DE |
| **[[Svexa]]** (Zone7's acquirer) | Injury-prediction / sports-science | **$6.61M** (latest $3.75M Later-Stage Aug-2026) | ~7 core team | — |
| **[[Kitman Labs]]** | Performance-medicine EMR + intelligence | **$82.30M** | $146.14M (Nov-2021) | 180 (2024) | Dublin, IE |
| **[[Hudl]]** | Video analysis + data | **$227.64M** | $900.00M (May-2021) | 3,500 (2026) | Lincoln, NE |
| **[[Teamworks]]** | Athlete engagement / ops | **$485.96M** | **$1.50B** (Feb-2026); PitchBook est **$1.73B** (Sep-2026) | 680 (2026) | **Durham, NC** |
| **[[Kinexon]]** | Hardware tracking (UWB) + platform | **$147.69M** ($130M Later-Stage round; Red Bull/BMW i/THL) | undisclosed | 218 (2026) | Munich, DE |

*ATP's two closest rivals, **[[Uplift Labs]]** and **[[DARI Motion]]**, have **thin PitchBook coverage**
(early/undisclosed) — they stay on public-source estimates (Uplift: ~20K athletes 2025, MLB/NBA/NCAA;
DARI: FDA-cleared, NFL + hospitals). Catapult is public (ASX: FY26 rev US$140.7M); WHOOP $10.1B; Oura
private-large — see §9. **PitchBook pass complete (Cole, Sept 2026).***

> **The single clearest strategic signal in the whole analysis:** capital and valuation **concentrate
> in the platform / EMR / engagement layer, not in standalone injury prediction.** The two pure-play
> predictors combined — Zone7 ($10.7M) + its acquirer Svexa ($6.6M) — raised **≈ $17M lifetime** and
> exited at an undisclosed (small) price, while Teamworks ($486M / **$1.5B**), Hudl ($228M / $900M),
> and Kitman ($82M) — the players who **own the athlete relationship, record, video, or ops** — captured
> the money. **Implication for ATP:** an injury-*predictor* that stays a point solution is a hard venture
> business. ATP should either (a) build toward **owning a relationship/record** (the college athlete's
> longitudinal movement baseline *is* a candidate for that), or (b) deliberately position as the best
> **wedge/feed into — and acquisition target for —** a Teamworks / Hudl / Kitman / Catapult. Note
> **Teamworks is a ~$1.7B company in Durham, ATP's own backyard** (founded 2006; CEO/co-founder **Zach
> Maurides**, zmaurides@teamworks.com; backers General Catalyst, Delta-v, Hg), and it is a **serial
> data/analytics acquirer — it has already bought Pro Football Focus (PFF) and Sportlogiq.** ATP is
> a Durham-based sports data/analytics company; that makes Teamworks the **single most natural future
> acquirer**, and one Jaylen/Cole can build a real relationship with locally. Note Teamworks' predicted
> exit is **IPO (98%)** — i.e., it's the acquirer *building toward a public offering by rolling up the
> data layer*, not itself a target. Separately, Zone7's core injury-prediction **patents are now
> _Inactive_**, so the IP space isn't locked up (freedom-to-operate is open) — but that also confirms
> **patents are not the moat here; evidence, data, and distribution are.**

---

## 4. Evidence-quality audit (ATP's, and Cole's, comparative advantage)

The sector is judged on **evidence more than features**, and the published field is young and uneven:

- **Scientific Reports 2026 meta-analysis** (10 models): pooled **sensitivity 0.79, specificity
  0.71, diagnostic odds ratio ~9.02** — but **external validation was absent in *all* included
  studies.** (nature.com/articles/s41598-026-59571-y)
- **BJSM 2025 scoping review (Leckey et al., UCD):** methodologically uneven; a large share of
  studies assessed only a single model. (pubmed.ncbi.nlm.nih.gov/39613453/)
- Markerless-mocap **clinical-readiness** is itself still being scoped (arXiv 2609.18667;
  OpenCap validation scoping review, Frontiers Digital Health 2026).

**Grading rubric to apply to every competitor (PROBAST + Zone7's own buyer checklist):**
which population/environment was studied? how many injury incidents in the dataset? what inputs?
test/train leakage? peer-reviewed *prospective* vs. retrospective vs. white paper vs. testimonial?

- **DARI Motion:** validated + **FDA-cleared** → highest bar in the cluster.
- **OpenCap:** **peer-reviewed** (but research-grade, not a commercial injury predictor).
- **Zone7:** retrospective, **self-described as not peer-reviewed**.
- **Kitman:** "30–50% injury reduction" is **self-reported** unless independently published.
- **Uplift / ATP:** vendor/anecdotal so far.

> **The strategic opening:** external validation is **absent in the entire literature**. A single
> **prospective, externally-validated** study — feasible for ATP given Jaylen's BME background,
> Duke research access, the signed pilots (built-in cohorts), and advisors Dickens/Luck — would put
> ATP **ahead of literally everyone on the evidence axis**, the axis that actually closes elite
> buyers and investors. This is the highest-leverage non-obvious move in the whole analysis.

---

## 5. Regulatory posture (now a competitive variable)

The line is the FDA's **"General Wellness: Policy for Low Risk Devices."** Cross it — by making a
diagnostic/predictive medical claim — and you become a regulated device.

- **The WHOOP cautionary tale:** FDA issued a warning letter (**Jul 14, 2025**) that WHOOP's Blood
  Pressure Insights was an *uncleared medical device*; 6 months of industry debate; FDA released
  **updated General Wellness guidance Jan 6, 2026** and then **closed the warning letter** after
  WHOOP modified product + labeling. A single phrase ("medical-grade") is what tipped intended use.
- **DARI** sits on the cleared side (moat). **WHOOP** has an FDA-cleared **ECG**.
- **ATP implication:** "record an athlete and **predict injuries before they happen**" is precisely
  the kind of claim that reads as *diagnosis/prevention of disease* → device territory. **Recommend:**
  frame as **movement-quality / mobility monitoring that flags deviations from an individual's
  baseline** (wellness-safe), avoid diagnostic/predictive-medical language in marketing and contracts
  now, and treat a **510(k)/De Novo path as a later moat** (DARI proves it's worth having) rather than
  an accidental trap. Watch FDA 510(k) + warning-letter databases for competitors hiring clinical/
  regulatory staff — that's the tell that someone is going for clearance.

---

## 6. Data-rights audit (shapes go-to-market)

Who owns and controls the athlete data decides *how you sell*, and it splits sharply by segment:

- **College (ATP's lane):** athletic-department wearable/video data is generally **FERPA**-governed,
  **not HIPAA**. The **NCAA CSMAS approved performance-technology guidance on Dec 15, 2025** —
  explicitly covering **cameras, software, and apps** — and now expects schools to keep a **written
  plan** for how they educate, manage, protect, purchase, and improve performance-tech data (full
  consensus statements early 2026). College athletes have **no union**.
  → **ATP should build the NCAA-required "written plan" into the product** (consent flows, retention,
  role-based access, opt-out of AI/ML training — several of which ATP's privacy notice already
  gestures at). Compliance-as-a-feature is a wedge consumer/pro-first rivals under-serve.
- **Pro (if ATP expands up):** NFL/NBA/MLB/WNBA/NWSL **CBAs** govern consent, confidentiality,
  commercial-use limits, and bar using biometric data in contract talks; MLB/NBA use **joint
  committees to approve devices**. Getting on an approved-device list is a gate.
- **Cross-cutting:** FTC Health Breach Notification Rule; **state biometric laws** (TX caps storage
  at ~1 year; CA opt-out rights; WA "My Health My Data"); GDPR for any European clubs.
- **Local asset:** Duke's **Deep Tech "No Pain, No Privacy" (Aug 2026)** essay on athletic wearables
  + consent is unusually on-point — a resource *and* a potential contact for Cole. (deeptech.duke.edu)

---

## 7. Porter's Five Forces for this niche

- **Buyer power — HIGH.** Only a few hundred elite teams; long sales cycles; **league-wide
  procurement** (Kitman–USL/UFL/EPPP) locks out entrants at the top. *ATP's answer: go college/
  broad-access first, where the buyer is a department, not a league office.*
- **Supplier power — MODERATE.** Sensor OEMs and data owners (Catapult, STATSports) control the
  pipe — but ATP's camera-only capture **needs no sensor supplier**, which is a structural advantage.
- **Substitutes — STRONG.** In-house staff + spreadsheets + free **OpenCap**. "Do nothing new" wins
  a lot. ATP must beat *status quo*, not just other vendors (April Dunford's point).
- **New-entrant threat — HIGH at the software layer** (where ATP and Uplift live), low at hardware.
  Camera + pose models are increasingly commoditized → moat must come from **evidence, compliance,
  data/baseline network effects, and distribution**, not the pose pipeline itself.
- **Rivalry — INTENSIFYING via M&A.** Catapult bought Perch + IMPECT; Oura bought Sparta; Svexa
  bought Zone7. Consolidation sets the bar and hints at ATP's likely exit paths (acquisition by a
  Kitman/Catapult/Oura-type).

---

## 8. Positioning 2×2 (honest axes — no magic quadrant)

**X-axis:** descriptive load/monitoring → **predictive/prescriptive injury risk**
**Y-axis:** requires dedicated hardware/lab/multi-device → **single phone, zero hardware**

```
 single phone / zero-hardware
              ▲
      OpenCap*│         Uplift Labs
              │        •      • ATP (today: baseline/descriptive,
              │                    aspiring predictive →)
    ──────────┼──────────────────────────────►
  descriptive │                    predictive
              │  Catapult•   •Zone7 (agnostic software)
     Kitman•  │  Kinexon•
   DARI•      │  •Kinetisense
              │  (hardware/sensor + clinical)
       dedicated hardware / lab / multi-device
   *OpenCap needs 2+ phones → mid on the Y-axis, research-only on X
```

- **ATP's honest spot:** top area (phone-only) but **mid on X** — today it's a baseline/mobility
  *monitor* marketed as injury *prediction*. **Uplift is the nearest neighbor.** The credible path is
  to move *right* (toward validated prediction) **via the evidence study (§4)** while staying at the
  top (phone-only) and defending with college/FERPA/DoD — not to claim the top-right by construction.

---

## 9. Business model, pricing & go-to-market comparison

- **Benchmark to beat (pro SaaS):** **Catapult FY26** — revenue **US$140.7M** (+19%), ACV **US$134M**
  (+28% cc), **ACV retention 96.1%** (3.9% churn), **ACV per pro team >US$30K** (+10%), EBITDA
  US$24.7M (17.6% margin). Hardware+SaaS, sticky, expensive. (fool.com.au; ministryofsport.com)
- **Consumer/enterprise scale:** **WHOOP** — **$575M Series G at $10.1B** (Mar 31 2026; Collaborative
  Fund lead; QIA, Mubadala, Mayo, Abbott, athlete LPs), 2.5M+ members, $1.1B bookings run-rate
  (+103%), IPO next. **Oura** — ring + **Trinsic** enterprise/**government** platform (Sparta acq.
  Oct 2024; exited force plates end-2024). (hlth.com; techcrunch.com; ouraring.com)
- **GTM archetypes:** top-down **league** deals (Kitman) · land-and-expand **pro-team** (Catapult
  added 576 pro teams in a year) · **athlete/union-led** (WHOOP–NFLPA, players own data) · **consumer
  brand + athlete investors** (WHOOP) · **integration/distribution** (Kitman ecosystem).
- **ATP's GTM (recommended):** **college land-and-expand** priced to an athletic-department budget
  (not a $30K/team pro ACV), compliance-native, seeded from Duke/NCCU pilots → conference peers;
  **DoD/SBIR as parallel non-dilutive revenue**. Avoid the pro-league procurement wall until evidence
  + clearance are in hand.

---

## 10. Where ATP fits + strategic recommendations

1. **Own the wedge, don't out-feature the incumbents.** ATP's defensible claim is *"one phone, zero
   setup, your own baseline tracked over time"* — not "more analytics than Catapult." YAGNI on
   breadth; depth on the single-camera longitudinal baseline.
2. **Make college/NCAA/FERPA compliance a moat.** Build the NCAA-required **written data plan** into
   the product; be the compliance-native default while Uplift/consumer players retrofit. This is a
   real barrier the December 2025 guidance just created.
3. **Win the evidence war (highest leverage).** Run a **prospective, externally-validated** study off
   the signed pilots. External validation is *absent in the entire literature* — clearing it would put
   ATP ahead of Uplift, Zone7, and Kitman on the axis buyers actually weight. Uniquely feasible given
   Jaylen's BME + Duke access + advisors Dickens/Luck. **This is the recommendation to act on first.**
4. **Discipline the injury-*prediction* language now.** Reframe to wellness-safe "movement-quality /
   deviation-from-baseline monitoring" to avoid the WHOOP trap; scope a **510(k)/De Novo** path as a
   *future* moat (DARI shows clearance is a durable advantage), not an accident.
5. **Treat DoD/SBIR as strategic capital + a proven second market.** Oura/Sparta's government traction
   confirms demand; SBIR is non-dilutive and dual-use. Keep specifics **confidential** (DRF flag).
6. **Build to be acquired (or to become the platform) — and cultivate Teamworks first.** Three
   independent PitchBook signals say the exit is acquisition by a relationship-owning platform: Kitman
   (M&A 93%, already bought Presagia + The Sports Office), Kinexon (M&A 68%), and Zone7 (exited to
   Svexa). The standout is **[[Teamworks]]** — a ~$1.7B, IPO-track (98%) Durham roll-up that has already
   acquired **PFF and Sportlogiq** (the data/analytics layer). ATP is a Durham sports-data company →
   Teamworks is the most natural acquirer *and* a local relationship worth building now. Meanwhile watch
   **[[Uplift Labs]]** as the direct rival; the realistic ATP exit is a platform that owns the team
   relationship but lacks turnkey single-camera capture + a validated college/defense footprint.

**Biggest risks:** (a) Uplift out-executes on the same phone-based pitch with more capital;
(b) ATP gets classed as a *feature* by a Catapult/Kitman that owns the data pipe and EMR;
(c) an over-strong "predict injuries" claim draws FDA attention before ATP is ready;
(d) elite-team buyer power + league procurement stalls revenue if ATP chases pro before college scales.

---

## 11. Sources & Cole's manual follow-ups

**Cited web sources (Sept 2026):**
Catapult FY26 — [fool.com.au](https://www.fool.com.au/2026/05/20/catapult-sports-reports-record-revenue-in-fy26/),
[ministryofsport.com](https://ministryofsport.com/catapult-sports-ltd-record-usd141m-revenue-as-operating-profit-surges-67-per-cent/) ·
WHOOP Series G — [hlth.com](https://hlth.com/insights/news/whoop-secures-575m-series-g-round-reaching-10-1b-valuation-2026-04-01),
[techcrunch.com](https://techcrunch.com/2026/03/31/whoop-valuation-10b-series-g-fundraise/) ·
WHOOP FDA — [medtechdive.com](https://www.medtechdive.com/news/fda-drops-whoop-warning-letter-over-blood-pressure-feature/823652/),
[FDA warning letter](https://www.fda.gov/inspections-compliance-enforcement-and-criminal-investigations/warning-letters/whoop-inc-709755-06172026) ·
Uplift Labs — [uplift.ai](https://www.uplift.ai/) ·
DARI Motion — [darimotion.com](https://darimotion.com/) ·
Kinetisense — [kinetisense.com](https://www.kinetisense.com/) ·
OpenCap — [opencap.ai](https://www.opencap.ai/), [Frontiers scoping review 2026](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.1882536/full) ·
Zone7 — [zone7.ai validation](https://zone7.ai/case-studies/validation-study/), [svexa.com](https://svexa.com/) ·
Kitman Labs — [kitmanlabs.com](https://www.kitmanlabs.com/) ·
Oura/Sparta — [ouraring.com](https://ouraring.com/blog/oura-acquires-sparta-science-to-expand-enterprise-capabilities/) ·
Evidence — [Sci Reports meta-analysis](https://www.nature.com/articles/s41598-026-59571-y),
[BJSM scoping review](https://pubmed.ncbi.nlm.nih.gov/39613453/) ·
NCAA guidance — [ncaa.org](https://www.ncaa.org/news/2025/12/11/media-center-performance-technology-guidance-approved-by-csmas.aspx) ·
Duke Deep Tech — [deeptech.duke.edu](https://deeptech.duke.edu/blog-post/no-pain-no-privacy-athletic-wearables-and-limits-consent/)

**Cole's manual follow-ups (I can't reach these):**
- **PitchBook — DONE (Sept 2026):** Zone7, Svexa, Kitman, Hudl, Teamworks, Kinexon confirmed in §3a;
  Uplift Labs + DARI Motion have thin PitchBook coverage (left on public estimates). No further pull needed.
- **Duke databases:** Euromonitor Passport (Sports module), IBISWorld, Capital IQ, BCC Research for
  market sizing; Factiva/ABI-INFORM for SBJ/SportTechie archives.
- **Primary evidence:** SPORTDiscus/Scopus/PubMed deep-dive per competitor ("[company] validity
  reliability injury"); FDA 510(k) + De Novo databases for each player's clearance status.
- **Voice of customer:** interview 5–10 practitioners (Duke Athletics is on campus; JHTV network) +
  G2/app-store reviews + job postings (clinical/regulatory hires = FDA-path signal).
- **Ecosystem reports:** SportsTechX *Global SportsTech Ecosystem Report 2026*, Drake Star, PEAK.

Related: [[athletic-training-portal]] · [[atp-federal-funding-landscape]] · [[dorm room fund]] · [[capital-strategy]] · [[Job Search]] · [[cole]]
