---
type: concept
kind: design
created: 2026-07-27
---

# Neuro character rig (stick-figure animation, Claude-Code-authored)

How to build expressive [[neuro-channel|Neuro]] animation **automatically with [[claude-code|Claude
Code]]** — the upgrade from video #1's flat-PNG bob to a rigged, gesturing character. Filed from
Cole's question "best way to build stick-figure animation like this automatically." Design, not
built.

## Two viable paths (pick per video)
1. **Image-per-scene (fastest, $0)** — generate one still per scene/beat with **Nano Banana 2**
   (Google Flow, free) using **`neuro.png` as the consistency reference**, and cut them to the voice.
   This is the proven viral-stickman format from the [[stickman-animation-free-ai-tutorials|tutorial
   batch]]; no rig to build. Optionally animate each still with Google Flow video (free daily credits).
2. **Articulated SVG rig (most control, most "his own")** — the code approach below. Best once the
   format is proven and Cole wants gesture/expression Nano Banana can't reliably hold.
Both keep the character consistent; the rig does it by construction, images do it via the reference.
See [[neuro-free-tool-stack]] for where each fits.

## Recommendation (path 2): an articulated **SVG rig** as a [[remotion|Remotion]] React component
The winning approach for *Claude-Code-authored* animation is a **skeletal SVG rig driven by
`frame`**, because the entire character lives in **code Claude can read, generate, and tweak from a
text script** — not in a binary/visual-tool file. It's diffable, version-controlled, and previewable
in `remotion studio`.

**Structure — nested joints.** Split Neuro into named SVG groups with a pivot (transform-origin) at
each joint; nest them so a parent rotation carries its children (shoulder → elbow → hand):
```tsx
<g transform={`translate(${x},${y}) rotate(${lean})`}>        {/* whole-body sway */}
  <Torso/>
  <g style={{transformOrigin:'shoulderR'}} transform={`rotate(${armR})`}>
    <UpperArm/>
    <g style={{transformOrigin:'elbowR'}} transform={`rotate(${elbowR})`}><Forearm/></g>
  </g>
  <g style={{transformOrigin:'neck'}} transform={`rotate(${headTilt})`}>
    <Brain pulse={pulse}/> <Eyes blink={blink}/> <Mouth open={mouthOpen}/>
  </g>
</g>
```
Every value above is just a number Claude computes from `frame`.

**Motion — a pose library + procedural idle.** Define named **poses** (each = a set of joint angles):
`idle`, `point`, `shrug`, `think`, `cheer`. Sequence them at the script's cue frames and
`spring()`/`interpolate()` between them. Layer always-on procedural motion: sine-wave idle bob/breathing,
`frame % N` **blink**, **brain-pulse** on emphasis beats. Result: the *script* drives the body —
"beat 3: Neuro points at the word" becomes `pose: point @ 90f`, and new videos animate largely
automatically.

**Mouth-sync — amplitude first.** For a cartoon, skip phoneme detection: use
`@remotion/media-utils` `getAudioData`/`visualizeAudio` to read per-frame **audio amplitude** and map
it to 3 mouth shapes (closed / small / wide). Fully automatic from the [[elevenlabs|ElevenLabs]] MP3.
**Upgrade path:** [Rhubarb Lip Sync](https://github.com/DanielSWolf/rhubarb-lip-sync) (CLI → viseme
timeline JSON) or ElevenLabs character-level timestamps for accurate visemes later.

## Getting the rig from Cole's drawing (one-time)
Convert `public/neuro.png` to a clean **layered SVG**, then split into the named joint groups:
- **Auto-trace** the PNG (`vtracer` / Inkscape / Illustrator image-trace — Claude Code can run
  `vtracer` in the repo), then hand-split; **or** redraw as parametric SVG paths matching his style.
- **Match the marker look** with SVG strokes: thick `stroke-width`, `stroke-linecap="round"`,
  `stroke-linejoin="round"`, and the brain squiggle as one path. This preserves Cole's hand-drawn
  feel — important for brand.

One rig, reused across every video.

## Why not Rive / Lottie / AI video
- **[Rive](https://rive.app):** excellent runtime + state machines, but rigs are built in a **visual
  GUI** and stored in a binary `.riv` — Claude Code can't author/tweak them from a script. Best if you
  ever want a designer-driven, super-polished rig and accept a manual tool.
- **Lottie / After Effects (bodymovin):** designer-driven; the JSON is machine-exported and huge —
  not hand-authorable by an LLM. Same objection.
- **AI image/video generation:** can't hold a consistent brand character frame-to-frame and isn't
  controllable — wrong tool for a repeatable mascot.

The SVG-rig-in-code approach is the only one where **"automatically using Claude Code" is literally
true** — Claude writes the rig, the poses, and the per-video sequencing as ordinary React + numbers.

## Recommended path
1. One-time: trace/redraw Neuro as a layered, jointed SVG component (style-matched).
2. Build a small **pose library + idle/blink/pulse** system in Remotion.
3. Add **amplitude mouth-sync**; upgrade to Rhubarb visemes only if lip-sync feels off.
4. Then per video, Claude sequences poses to the script cues — the animation step of
   [[neuro-production-pipeline]].

Do this only when Cole asks to leave the flat-PNG format (per [[neuro-channel]] the articulated SVG
is explicitly deferred until then). Related: [[remotion]], [[neuro-production-pipeline]],
[[neuro-channel]], [[Neuro]] bucket.
