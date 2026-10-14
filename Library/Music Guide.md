# Music Guide (Oct 14, 2026)

> **Owner decision, Oct 14 night: NO generic background bed by default.** Not the instrumental beds, stock music or AI-generated music below. Default is clean narration; effects only where the picture makes the sound; silence is valid. A real (commercial or trending) song goes in only through the platform's own music library (route A, `Library/Sound Library.md` §2) when it strengthens the story. This guide still applies if a bed is ever used on purpose: levels, placement, licences, tests. The ElevenLabs beds stay in the library, unused.

*(Superseded the same night; see the box above.)* Music was briefly a planned part of every edit (owner decision, Oct 14 afternoon).

Evidence tiers: **[V]** measured on our files, **[S]** small-n support, **[H]** hypothesis, **[E]** external terms or practice.

## 1. Why, and what we do NOT know
- **5 of 5 old Shorts we had watched used a quiet music bed** (4 hits and the weak control). Each was trap/hip-hop, or cinematic for the emotional one, sitting about 18-20 dB under the voice. [S]
  - Source: `Research Notes/Posted Video Audit (Oct 14, 2026).md`, section 10.
- **Music did not separate hits from misses.** The 4.9K control had it too, and our 20K new Flagg Short had none. No data says music adds views. [S]
  - Music cohorts are compared in the Outcome Log. Never say music "raised views" without that data.
- **What the old hits did with music:**
  - a swell into the payoff (Kobe)
  - a riser and a clean cut on the last beat (Luka)
  - a decay to dead silence on the final word (Bronny "...son.")
- We copy those **moves**, not specific songs.

## 2. The library (`Library/Music/`; every row in `music_library.csv` with source and licence)
| File | Mood | Tempo | Speech-band share* | Source and licence | Status |
|---|---|---|---|---|---|
| `eleven_stats_01.mp3` "Clever pulse" | records, stats, paradoxes | ~92 BPM | 4% | ElevenLabs Music, generated Oct 14 on our Starter plan | used in #40 (music version); owner to approve by ear |
| `eleven_hype_01.mp3` "Trap pulse" | high-energy surprises, record chases | ~144 BPM | 2% | ElevenLabs Music | used in #21 (music version) |
| `eleven_suspense_01.mp3` "Dark build" | mysteries, reveals | ~85 BPM, builds | 0% | ElevenLabs Music | used in #41 (music version) |
| `eleven_emotional_01.mp3` "Warm piano" | legacy, feel-good, endings | ~81 BPM | 13% | ElevenLabs Music | not used yet |
| `mixkit_349_basketball_training.mp3` | hype | ~89 BPM | **44%** | Mixkit Stock Music Free License | candidate; crowds the voice band, so use bed -23 or lower |
| `mixkit_738_hip_hop_02.mp3` | stats | measured 65 BPM (my beat estimate; may be half the felt tempo) | 26% | Mixkit | candidate |
| `mixkit_282_sweet_september.mp3` | emotional | measured 152 BPM (my beat estimate; may be double the felt tempo) | 4% | Mixkit | candidate |

\* Speech-band share is the share of the track's energy between 300 and 3,400 Hz, where the narration lives. Lower leaves the voice clearer. [V, measured]

**Licences, checked Oct 14, 2026:**
- **ElevenLabs Music** (elevenlabs.io/music-terms, Exhibit A, Starter column) [E]:
  - "All online and offline commercial use permitted, except film, TV, radio, and Studio Games."
  - No attribution.
  - Individual use only.
  - Limits: 17 generated minutes and 30 downloaded minutes a month.
  - Uploading the track itself to music streaming services is prohibited; we only use it under video.
  - Generated audio is unique, so **Content ID risk is low**. Never register it in Content ID ourselves.
- **Mixkit Stock Music Free License** (mixkit.co/license) [E]:
  - Commercial use including monetized YouTube, no attribution.
  - Not for broadcast TV or radio, CDs/DVDs, or games.
  - **Content ID risk: medium.** Free library tracks are sometimes re-registered by third parties.
  - Keep the library row as proof, and check the item page shows the Free License badge before posting.
- **Not used:**
  - **Incompetech/Kevin MacLeod (CC BY 4.0):** needs a credit line, which conflicts with our no-description rule. Owner's call.
  - **Pixabay and Chosic:** blocked from the cloud (403).
  - **YouTube Audio Library:** needs Studio, which only the owner opens.
  - **Commercial songs (revised Oct 14 night; the owner is open to them):** only through the YouTube app's "Add sound" picker, added by the owner at upload (route A in `Library/Sound Library.md` §2: licensed by YouTube for Shorts). Never baked into our render without the owner's explicit yes for that video: a baked-in song gets a standard Content ID claim, and a Short over 1 minute with any claim is blocked.
- **Sound effects** (`Tools/sfx/`): the catalog says they were "copied from Downloads/music", so **their licence is unknown**. They're flagged in the Rules Audit. Replace them over time with Mixkit's free effects or ElevenLabs sound effects, and log the source.

## 3. Choosing a bed by story type
| Story type (Creative System v3 format) | Bed | The music move |
|---|---|---|
| **Paradox / record / stat** ("doesn't count", "most ever") | stats (clever pulse) | one beat of silence before the turn ("It isn't."); the music stops before the last line so the punchline lands dry |
| **Mystery to reveal** ("Is anyone taller...?") | suspense | builds under the setup; the track's own decay starts on the answer word |
| **High-energy surprise / record chase / countdown** | hype | the track's break lands under the last setup line; its re-entry hit lands on the payoff line |
| **Emotional arc / legacy / ending** (Chris Paul, Kobe) | emotional | enters soft after the hook; swells into the payoff; decays as the subject walks off |
| **Quote-led Short** (real audio from a player or coach) | any, but **drop it under the quote** (`drops`) | the quote plays dry |
| **Dry by choice** | none | only when a silence IS the story; say why in PACKAGE.md (QA warns otherwise) |

## 4. Placement and levels (implemented in `assemble.py`, from the folder's `music.json`)
```json
{"track": "Library/Music/eleven_stats_01.mp3",
 "bed_lu": -20, "gap_lift": 4,
 "drops": [{"at": 12.6, "len": 0.3}],
 "out": 19.8, "fade_out": 0.5,
 "why": "story type + the music move"}
```
| Field | Meaning | Default |
|---|---|---|
| `bed_lu` | music loudness under **speech**, relative to the voice (LU), measured on the part of the track that plays | **-20** (house range -24 to -16) |
| `gap_lift` | dB the bed rises where nobody speaks (intro, tail, pauses over 0.35 s), with 0.15 s ramps | 4 |
| `drops` | music dips out (0.06 s ramps): a beat of silence before a turn or punchline, or under a real quote | none |
| `in`, `out` | video seconds where the music starts and stops | 0 and the end |
| `start` | second of the track to start from | the loudest steady stretch |
| `hit`, `hit_on` | put a moment of the track (a re-entry hit, the decay) on a video second | none |
| `align_end` | start the track so its own ending lands on `out` | false |
| `fade_in`, `fade_out` | seconds | 0.3 and 1.2 (0.05 when the track's own ending is used) |

**Mix settings:**
- The voice is lifted to -14 LUFS first, then effects and music are mixed under it.
- With music the limiter sits at -3 dBFS, so AAC true peak stays under -1 dBTP ([V]: #21's trap bass hit -0.9 dBTP at the old -2 dBFS limit).

**Why -20:** broadcast practice puts beds 15-25 dB under dialogue, and the old Shorts sat at about -18 to -20 [E/S]. Our intelligibility test (section 5) could not find a level where words were lost, so taste and convention set the level, not the recogniser.

## 5. Tests and checks (`Library/Music/tests/`)
- **Intelligibility test** (`mix_test.py`, results in `results_main.json` and `results_stress.json`). [V]
  - Setup: the same voice take, at -14 LUFS, under each generated bed held at a constant level from -23 to -2 LU, through the phone-speaker simulation, transcribed by the speech recogniser.
  - Result: **error rate 1.7% at every level, the same as no music.**
  - Reason: these beds put almost no energy in the speech band (0-13%), and a phone speaker drops most bass anyway.
  - What it does and doesn't show: the beds do not mask words for a machine. It does not show what sounds natural to a person. **I can't hear audio**; the owner's ear decides taste.
- **Level test T2 (Oct 14 night, real mix, new voice):** #40 v4 with the bed at -12 LU (closer to CoachClank's 2.5-5 dB gap) vs the house -20 LU. [V]
  - Same render otherwise.
  - The phone simulation transcribed **every word at both levels**.
  - The speech-band margin fell from 41 dB to 33 dB.
  - It's on the Sound Check page (section 4) for the owner's ear. The house level stays -20 until the owner says "louder".
- **QA** (`qa_short.py`, on any render with music):
  - the track must be in `music_library.csv`
  - its status can't be "rejected" or "unclear"
  - `bed_lu` must sit within -24 to -16 (warning)
  - **speech-band margin:** voice vs music at 1-4 kHz, before ducking. Under 12 dB FAILs, under 18 dB warns. #40 and #41 measure 40 dB; #21 measures 27 dB.
- **Placement check** (how #40, #41 and #21 were verified): subtract the dry render from the music render to isolate the music, then read its loudness every 0.1 s at the planned drop, hit and stop times. [V]

## 6. Getting new tracks
- **Generate** (preferred: clean licence, unique audio):
  ```
  . key.sh && python Tools/music_gen.py --mood stats --seconds 30 --title "..." --out Library/Music/eleven_stats_02.mp3 --prompt "Instrumental ..."
  ```
  - Every prompt says: instrumental, no vocals, the BPM, the mood, **"sparse midrange so a narrator can talk over it"**, and how it should end.
  - Plan limit: 2 requests at once; the tool backs off and retries on "busy".
  - It writes the mp3, a JSON with the prompt, and the library row.
- **Mixkit:** download from the item's preview URL (`assets.mixkit.co/music/<id>/<id>.mp3`), add the row by hand with the item URL, then measure it (tempo, LUFS, speech-band share; the snippet is in the Oct 14 session log). Prefer tracks under 15% speech-band share.
- **After any new track:** run `mix_test.py` with it if it is busy in the mids, and get the owner's yes by ear before its status leaves "candidate".

## 7. In every production package
`PACKAGE.md` gets a **Music and sound** block:
- the track (file and title)
- source and licence (from the library row)
- the intended mood
- entry and exit points
- `bed_lu` and any drops or hits
- the effects with their seconds and why
- the QA speech-band margin

**No-music version:** render it with `assemble.py --no-music --out-name final_v3.mp4` (or similar). The original `final.mp4` is never overwritten by a music render.
