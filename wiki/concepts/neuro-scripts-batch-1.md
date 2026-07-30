---
type: concept
created: 2026-07-29
---

# Neuro — script batch 1 (first 3 Shorts)

Ready-to-produce **script + storyboard** drafts for the first three [[neuro-channel|Neuro]]
Shorts, drawn straight from the vault concept pages and built on the
[[neuro-shorts-benchmark]] rules (hook by ~2.5s, second-person "why you…" title, one
mechanism + one proof beat, ~40–45s, ~10–14 doodle scenes, kinetic captions, one CTA).

**Status: DRAFT for Cole's approval.** Nothing here is posted. Cole picks one (recommend #1),
tweaks voice, then the pipeline builds it. Each script is grounded in its concept page and
keeps that page's honesty caveats (no overclaiming). Word counts target ~40–45s at a natural
narration pace (~3 words/sec).

Storyboards are JSON so the [[neuro-production-pipeline|pipeline]] can consume them directly:
each scene has a doodle-image prompt (`visual`), the kinetic `caption`, the `vo` line, and a
`dur` in seconds. Neuro (the walking-brain mascot) appears where flagged; other scenes are
plain doodle illustrations.

---

## Script 1 — "Why you walk into a room and forget why" ⭐ recommended first
*Grounds: [[conscious-vs-subconscious]] (working memory ~7±2), the [[doorway-effect]] (event boundaries).*

**Title options:** "Why you walk into a room and forget why" · "Your brain deletes it at the
doorway" · "The doorway wipes your memory (on purpose)"

**Script (~135 words):**
> You walk into the kitchen… and completely forget why. You're not losing it — your brain did
> that *on purpose*. Here's the thing: the conscious part of your mind, the "you" that holds a
> thought, is tiny. It juggles only about **four to seven things at once**. Everything else —
> the eleven million bits your senses take in every second — runs in the background. So when
> you're holding "go get my phone" and you walk through a doorway, your brain treats that
> doorway as the end of one scene and the start of a new one. It clears the tiny workspace to
> deal with the new room… and takes your reason with it. It's called the doorway effect. The
> fix? Say it out loud, or picture the object before you move. You're just refusing to let the
> workspace get wiped. Follow for one brain thing a day.

```json
{
  "id": "neuro-001-doorway",
  "title": "Why you walk into a room and forget why",
  "concept_source": "conscious-vs-subconscious",
  "target_seconds": 43,
  "scenes": [
    {"n": 1, "dur": 3, "visual": "doodle person mid-stride walking through a doorway into a kitchen, big question mark over head", "caption": "you walk in… and forget why", "vo": "You walk into the kitchen and completely forget why."},
    {"n": 2, "dur": 3, "visual": "same person, reassuring; Neuro mascot pops in beside them giving a thumbs up", "caption": "you're not losing it", "vo": "You're not losing it — your brain did that on purpose.", "neuro": true},
    {"n": 3, "dur": 4, "visual": "tiny glowing desk labeled 'conscious mind' holding a few floating icons", "caption": "your conscious mind is TINY", "vo": "The conscious part of your mind — the you that holds a thought — is tiny."},
    {"n": 4, "dur": 4, "visual": "the desk with exactly 4-7 sticky notes on it, a counter '4–7'", "caption": "~4–7 things at once", "vo": "It juggles only about four to seven things at once."},
    {"n": 5, "dur": 4, "visual": "a firehose labeled '11,000,000 bits/sec' pouring into a background vault", "caption": "everything else runs in the background", "vo": "Everything else — eleven million bits a second — runs in the background."},
    {"n": 6, "dur": 4, "visual": "thought bubble 'go get my phone' held over the person's tiny desk", "caption": "holding: 'go get my phone'", "vo": "So you're holding 'go get my phone'…"},
    {"n": 7, "dur": 5, "visual": "doorway drawn as a film 'scene cut' clapperboard; person crossing it", "caption": "brain: new room = new scene", "vo": "…and you walk through a doorway. Your brain treats it as the end of one scene."},
    {"n": 8, "dur": 4, "visual": "the tiny desk being wiped clean by an eraser, sticky notes flying off", "caption": "it clears the workspace", "vo": "It clears the tiny workspace for the new room — and takes your reason with it."},
    {"n": 9, "dur": 3, "visual": "label card 'THE DOORWAY EFFECT' with Neuro pointing at it", "caption": "it's called the doorway effect", "vo": "It's called the doorway effect.", "neuro": true},
    {"n": 10, "dur": 5, "visual": "person saying the phrase out loud (speech bubble 'phone!') before stepping through doorway", "caption": "fix: say it out loud / picture it", "vo": "The fix? Say it out loud, or picture the object before you move."},
    {"n": 11, "dur": 4, "visual": "Neuro waving, 'follow' button doodle pulsing", "caption": "follow for one brain thing a day", "vo": "Follow for one brain thing a day.", "neuro": true}
  ]
}
```
*Honesty note (from [[conscious-vs-subconscious]]): keep it to working-memory limits + event
boundaries — both well supported. Don't dress it up with the article's pop-science "7-second
pre-decision" claims.*

---

## Script 2 — "Why you suddenly see your new car everywhere"
*Grounds: [[reticular-activating-system]] (attention filter; the honest core, not manifestation).*

**Title options:** "Why you see your new car everywhere" · "Your brain has a spam filter for
reality" · "The 'new car' illusion, explained"

**Script (~140 words):**
> You buy a blue car. Suddenly… blue cars *everywhere*. Did everyone copy you? No — the cars
> were always there. What changed is your **filter**. Your senses pull in about eleven million
> bits of information a second, but you're only *aware* of maybe forty. So your brain runs a
> gatekeeper that decides what's worth your attention — and the moment something matters to
> you, it moves to the top of the list. Buy the car, and "blue car" is now flagged as
> important, so it keeps surfacing. Same street, same cars, different filter. Scientists call
> the surprise version of this the frequency illusion. Here's the useful part: you can *aim*
> it. Pick a goal, a question, a thing to notice — and your brain starts pulling matching
> evidence out of the noise. What you focus on really does grow, because attention is
> perception. Follow for one brain thing a day.

```json
{
  "id": "neuro-002-newcar",
  "title": "Why you suddenly see your new car everywhere",
  "concept_source": "reticular-activating-system",
  "target_seconds": 44,
  "scenes": [
    {"n": 1, "dur": 3, "visual": "doodle person handed keys to a blue car at a lot", "caption": "you buy a blue car", "vo": "You buy a blue car."},
    {"n": 2, "dur": 3, "visual": "street suddenly full of blue cars, person wide-eyed", "caption": "suddenly: blue cars EVERYWHERE", "vo": "Suddenly — blue cars everywhere."},
    {"n": 3, "dur": 3, "visual": "person shrugging, Neuro shaking head 'no'", "caption": "did everyone copy you? no", "vo": "Did everyone copy you? No — the cars were always there.", "neuro": true},
    {"n": 4, "dur": 4, "visual": "a funnel/filter labeled 'your brain's filter' on the person's head", "caption": "what changed = your FILTER", "vo": "What changed is your filter."},
    {"n": 5, "dur": 5, "visual": "firehose '11,000,000 bits/sec' hitting the funnel, only a thin trickle '~40' comes out to a lightbulb 'aware'", "caption": "11M bits in → ~40 you notice", "vo": "Your senses pull in eleven million bits a second — you're aware of maybe forty."},
    {"n": 6, "dur": 5, "visual": "a doodle bouncer at a velvet rope labeled 'gatekeeper' waving items through", "caption": "a gatekeeper picks what matters", "vo": "A gatekeeper decides what's worth your attention."},
    {"n": 7, "dur": 4, "visual": "'blue car' card stamped IMPORTANT, moved to top of a list", "caption": "'blue car' = flagged important", "vo": "Buy the car, and 'blue car' is flagged important — so it keeps surfacing."},
    {"n": 8, "dur": 3, "visual": "split screen: same street twice, one dull one highlighting blue cars", "caption": "same street, different filter", "vo": "Same street, same cars, different filter."},
    {"n": 9, "dur": 3, "visual": "label card 'FREQUENCY ILLUSION', Neuro pointing", "caption": "aka the frequency illusion", "vo": "Scientists call the surprise version the frequency illusion.", "neuro": true},
    {"n": 10, "dur": 5, "visual": "person setting a target labeled 'my goal', filter now pulling matching stars out of noise", "caption": "you can AIM it", "vo": "The useful part: you can aim it. Pick a goal, and your brain pulls matching evidence from the noise."},
    {"n": 11, "dur": 3, "visual": "text 'attention = perception', Neuro nodding", "caption": "attention is perception", "vo": "What you focus on grows, because attention is perception.", "neuro": true},
    {"n": 12, "dur": 3, "visual": "Neuro waving, pulsing follow button", "caption": "follow for one brain thing a day", "vo": "Follow for one brain thing a day.", "neuro": true}
  ]
}
```
*Honesty note (from [[reticular-activating-system]]): frame as selective attention / frequency
illusion — "directing attention is directing perception." Avoid any "manifestation" or
law-of-attraction spin; the concept page is explicit about this.*

---

## Script 3 — "Why New Year's resolutions fail (and what works)"
*Grounds: [[neuroplasticity]] (myelin, efficiency machine, repetition > intensity, no magic 21 days).*

**Title options:** "Why New Year's resolutions fail" · "Your brain is fighting your new habit
— here's why" · "The '21 days' habit rule is a myth"

**Script (~145 words):**
> Every January you swear this year is different. By February… you're back. That's not weak
> willpower — it's physics in your head. Every habit you already have is a pathway your brain
> wrapped in **myelin** — a fatty coating that makes the signal fire fast and effortless. Old
> habits run on myelin superhighways. A new habit is a dirt path: slow, and it costs real
> energy every time. And your brain is an efficiency machine — thinking burns glucose, so it
> defaults to the highway. That resistance you feel? It's not failure, it's your brain saving
> fuel. Here's what actually rewires it: **repetition beats intensity.** Myelin builds layer by
> layer, so tiny consistent reps — even half-hearted ones — beat rare heroic bursts. And forget
> "21 days" — the real range is anywhere from **18 to 254 days**. Show up small, show up often.
> That's how the dirt path becomes the highway. Follow for one brain thing a day.

```json
{
  "id": "neuro-003-resolutions",
  "title": "Why New Year's resolutions fail (and what works)",
  "concept_source": "neuroplasticity",
  "target_seconds": 45,
  "scenes": [
    {"n": 1, "dur": 3, "visual": "doodle person on Jan 1 with a 'NEW ME' banner, fireworks", "caption": "every January: 'new me'", "vo": "Every January you swear this year is different."},
    {"n": 2, "dur": 3, "visual": "same person by Feb, back on the couch, banner drooping", "caption": "by February… you're back", "vo": "By February, you're back."},
    {"n": 3, "dur": 3, "visual": "Neuro shaking head, 'not willpower' crossed out", "caption": "not weak willpower", "vo": "That's not weak willpower — it's physics in your head.", "neuro": true},
    {"n": 4, "dur": 5, "visual": "a neuron pathway being wrapped in a shiny sheath labeled 'myelin'", "caption": "habits = pathways wrapped in MYELIN", "vo": "Every habit you have is a brain pathway wrapped in myelin — a coating that makes it fire fast."},
    {"n": 5, "dur": 4, "visual": "a glowing multi-lane 'myelin superhighway' with cars zooming", "caption": "old habits = myelin superhighways", "vo": "Old habits run on myelin superhighways."},
    {"n": 6, "dur": 4, "visual": "a person trudging down a muddy dirt path labeled 'new habit'", "caption": "new habit = a slow dirt path", "vo": "A new habit is a dirt path — slow, and it costs real energy every time."},
    {"n": 7, "dur": 5, "visual": "brain doodle labeled 'efficiency machine' burning a glucose battery, choosing the highway on-ramp", "caption": "brain = efficiency machine, picks the highway", "vo": "Your brain is an efficiency machine — thinking burns glucose, so it defaults to the highway."},
    {"n": 8, "dur": 4, "visual": "person feeling 'resistance' arrows, Neuro relabeling it 'saving fuel'", "caption": "resistance = saving fuel, not failure", "vo": "That resistance you feel isn't failure — it's your brain saving fuel.", "neuro": true},
    {"n": 9, "dur": 5, "visual": "myelin sheath building up in thin layers with each rep, a rep-counter ticking", "caption": "repetition > intensity", "vo": "What rewires it: repetition beats intensity. Myelin builds layer by layer."},
    {"n": 10, "dur": 4, "visual": "tiny daily checkmarks stacking up vs one giant exhausted burst", "caption": "small consistent reps win", "vo": "Tiny consistent reps beat rare heroic bursts."},
    {"n": 11, "dur": 4, "visual": "'21 days' crossed out, replaced with '18–254 days', Neuro pointing", "caption": "forget '21 days' → it's 18–254", "vo": "And forget 21 days — the real range is 18 to 254 days.", "neuro": true},
    {"n": 12, "dur": 3, "visual": "dirt path visibly upgrading into a paved highway", "caption": "show up small, show up often", "vo": "Show up small, show up often — that's how the dirt path becomes the highway."},
    {"n": 13, "dur": 3, "visual": "Neuro waving, pulsing follow button", "caption": "follow for one brain thing a day", "vo": "Follow for one brain thing a day.", "neuro": true}
  ]
}
```
*Honesty note (from [[neuroplasticity]]): keep the "18–254 days, not 21" correction — the
concept page flags the 21-day myth explicitly. Myelin-as-habit and the efficiency-machine
framing are both grounded there.*

---

## Recommendation
Ship **#1 (doorway effect)** first: the most universal "wait, that happens to me?" hook,
cleanest single mechanism, and the shortest to produce. #2 and #3 are ready as follow-ups —
three videos is enough to soft-launch the channel (matches the [[neuro-channel]] "hold until
2–3 real videos" plan). Next human step: Cole approves a topic (the standing
[[tasks/index|task]]), records/greenlights voice, and the [[neuro-production-pipeline|pipeline]]
turns the JSON into doodle scenes.

Related: [[neuro-channel]] · [[neuro-shorts-benchmark]] · [[conscious-vs-subconscious]] · [[reticular-activating-system]] · [[neuroplasticity]] · [[Neuro]] bucket.
