---
type: entity
category: tool
---

# ElevenLabs

AI voice-generation tool. Produces the voiceover for the [[neuro-channel|Neuro]] channel via a
custom **"Neuro"** voice (settings: stability 50, similarity boost high). Cole pastes the approved
script, downloads the MP3, and drops it in `public/neuro-voice.mp3`.

**The audio drives all timing** — captions and scene cues in the [[remotion|Remotion]] composition
are keyed to frame numbers derived from the MP3's exact duration, so the build step always starts
by running `ffprobe` on the incoming file.
