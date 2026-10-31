# Voice audition (Oct 14, 2026): 12 takes, one script, same measures

> **CURRENT DECISION (Oct 14, late night; Part 4).** The owner shortlisted **A (Alex)** and **F (our old voice "pham v2", fixed settings)**. Both are rendered on two real Shorts (#21 v5, #36 v2) for the owner's final pick. Until then the default stays A and F is the backup. A new Pham clone was made and tested; it was **not** better. Earlier decision text follows.
> - **Primary:** Alex (ElevenLabs Voice Library `yl2ZDV1MzN4HbQJbMihG`), multilingual_v2, speed 1.2, stability .5, similarity .75, no denoise, no stretch, pauses capped at 0.38 s.
> - **Backup:** our clone "pham v2" with fixed settings (speed 1.1, stability .5, no denoise).
> - **Where it lives:** `Tools/voice_config.json` (the only place to change the voice) and `Tools/pronunciation.json`.
> - **Tested on 3 real Shorts:** #40, #41, #21 v4, all QA PASS.
> - **Oct 15 (overnight): a third A/F pair on a new Short, #42, one take each** (Alex and pham v2, the owner's cap). Numbers and reading: Part 5 below. The owner has still not picked; the default is unchanged.
> - **Waiting on the owner's ear:** Sound Check round 3. Until the owner answers, the old-voice versions stay the ready ones.

**Status:** the takes were actually generated and measured today.
- I cannot hear audio. Every number below comes from the speech recogniser (faster-whisper "small", the same one `voice_check.py` uses) and from Praat (`parselmouth`).
- **Naturalness and energy are NOT scored here.** Only the owner's ear can judge them (see "Owner listening task").

**Earlier lineup:** `Research Notes/Voice Lineup (Oct 13, 2026)/` (5 voices on the Flagg script; no pick yet). This audition adds three things:
- a script with a real hook, context and payoff and hard names
- a phone-speaker simulation
- prosody and name measures

**Script** (true facts from the #41 package; about 400 characters):
> Victor Wembanyama is not the tallest man in this story. Jamarion Sharp is listed seven-foot-five, and he's never played an NBA game that counts. Dallas cut him twice. The Clippers cut him in September. Even Nikola Jokic and Giannis Antetokounmpo never faced him in a game that counts. So what's missing? Three-point tries last season: Wembanyama, three hundred and fifty. Sharp, in the G League: zero.

- Hook (energetic): line 1.
- Context (conversational): lines 2-5.
- Payoff: the last 2 lines.
- Names: Wembanyama ×2, Jamarion Sharp, Nikola Jokic, Giannis Antetokounmpo.
- Respelled takes use the pipeline's method: "wem-bun-YAH-muh" and "Yoki-ch".

**Provider:** ElevenLabs, plan "starter".
- Characters used this cycle after the audition: 15,098 of 52,087 (the audition used about 4.75K).
- Checked Oct 14, 2026.
- Code: `audition.py`. Data: `results.json`. Audio: `takes/*.mp3` (raw), `*_lufs16.mp3` (loudness-matched for listening), `*_phone.wav` (phone simulation).

**Phone simulation:** 300-3,400 Hz band, 8 kHz resampling, −4 dB, pink noise at amplitude 0.03. Then transcribed.

## Results
| Take | Voice (ID) | Model | Settings | Length | Words/min | Errors, non-name words (clean / phone) | Wembanyama heard as the name? | Pitch variety (semitones) | Loudness variety (dB) | Voice clarity (HNR dB) | Pauses over 0.3 s |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **A** production | clone "pham v2" `GDS7e7WiI4GqkoRxZAFG` | multilingual_v2 | speed 1.15, stability .65, similarity .7 | 17.2 s | **245** | 0 / 2.1% | no ("Wembun Yama") | 4.88 | 2.71 | 8.7 | 2 |
| A2, same, take 2 | same | same | same | 16.6 s | 255 | 0 / 2.1% | no | 4.49 | 2.87 | 8.4 | 2 |
| **A3**, same, names not respelled | same | same | same | 17.2 s | **246** | 2.1 / 2.1% | **yes** | 4.54 | 3.00 | **9.0** | 4 |
| B, clone, more expressive | same | multilingual_v2 | stability .45, style .35, speed 1.15 | 15.7 s | 268 | 2.1 / 2.1% | yes | 4.18 | 2.49 | 9.1 | 2 |
| C, clone on v3 | same | eleven_v3 | stability .5 (v3 has no speed control) | 23.0 s | 184 | 0 / 2.1% | no | **5.35** | 2.52 | 8.8 | 8 |
| D, older clone "Pham" | `H2ovX6h6fD6dmyrg5SkI` | multilingual_v2 | production | 18.2 s | 231 | 2.1 / 2.1% | no | 4.46 | 2.76 | 8.6 | 4 |
| E, clone on Flash (half price) | clone | eleven_flash_v2_5 | production | 18.7 s | 226 | 2.1 / **6.2%** | no | **3.69** (flattest clone) | 3.35 | 8.0 | 7 |
| F, Liam premade | `TX3LPaxmHKxFdv7VOQHJ` | multilingual_v2 | speed 1.15, stability .5, similarity .75 | 23.4 s | 181 | 2.1 / 0% | no | 3.78 | 3.69 | 7.6 | 9 |
| G, Liam premade on v3 | same | eleven_v3 | stability .5 | 30.6 s | **136** | 0 / 2.1% | no | **6.24** | **5.44** | 11.0 | 10 |
| H, Chris premade | `iP95p4xoKVk53GoZ742B` | multilingual_v2 | as F | 29.9 s | 141 | 0 / 2.1% | yes | 4.27 | 6.41 | 10.3 | 10 |
| I, Eric premade | `cjVigY5qzO86Huf0OWal` | multilingual_v2 | as F | 24.4 s | 173 | 2.1 / 0% | no | 3.53 | 3.65 | 16.0 | 8 |
| J, Charlie premade | `IKne3meq5aSn9XLyUdCD` | multilingual_v2 | as F | 23.7 s | 179 | 0 / 0% | no | 4.38 | 4.21 | 11.4 | 9 |

## Rubric (1-5 each; same rubric for every take; the measures only, not taste)
**What the five scores mean:**
- **Pace fit:** words per minute, natively, against the house range of 247-289.
- **Phone intelligibility:** errors on non-name words through the phone simulation.
- **Prosody:** pitch variety in semitones.
- **Names:** is "Wembanyama" heard as the real name?
- **Clarity:** HNR.

| Take | Pace fit | Phone intelligibility | Prosody | Names | Clarity | **Total /25** | Naturalness and energy |
|---|---|---|---|---|---|---|---|
| **A3** clone, production settings, plain names | 5 | 5 | 4 | 5 | 4 | **23** | owner's ear |
| B clone, expressive | 5 | 5 | 3 | 5 | 4 | 22 | owner's ear |
| A clone, production settings (current) | 5 | 5 | 4 | 3 | 3 | 20 | owner's ear |
| G Liam v3 | 1 | 5 | 5 | 3 | 5 | 19 | owner's ear |
| H Chris | 1 | 5 | 3 | 5 | 5 | 19 | owner's ear |
| C clone v3 | 2 | 5 | 5 | 3 | 3 | 18 | owner's ear |
| D older clone | 4 | 5 | 3 | 3 | 3 | 18 | owner's ear |
| J Charlie | 2 | 5 | 3 | 3 | 5 | 18 | owner's ear |
| I Eric | 2 | 5 | 2 | 3 | 5 | 17 | owner's ear |
| E clone Flash | 4 | 4 | 2 | 3 | 2 | 15 | owner's ear |
| F Liam | 2 | 5 | 2 | 3 | 2 | 14 | owner's ear |

## What the evidence supports (and what it doesn't)
1. **Keep the current voice and model; no migration.** [V measures]
   - The clone "pham v2" on multilingual_v2 is the only voice that reads at the house pace natively (245-268 wpm).
   - Every premade voice reads at 136-184 wpm at the same speed setting. Using one would mean a 25-45% shorter script or heavy time-stretching, which lowers quality.
   - Our posted data puts faster narration with more views (Spearman +0.50, n=16; Posted Video Audit, section 3).
   - Take-to-take consistency is good (A vs A2: 0.6 s apart, the same intelligibility).
   - **Fallback:** the older clone "Pham" (`H2ovX6h6fD6dmyrg5SkI`, take D), 231 wpm, similar measures.
2. **Change the Wembanyama respelling.** [V measures, n=1 take each; the owner's ear confirms]
   - With "wem-bun-YAH-muh", the recogniser heard "Wembun Yama" in 9 of 9 respelled takes.
   - With the plain spelling it heard "Wembanyama" (A3, B, H), which suggests a standard-sounding name.
   - Today's #41 v2 carries the respelling (the recogniser heard "Wembun-Yama").
   - **New default:** plain "Wembanyama". **Keep** "Yoki-ch" for Jokic: the plain spelling risks "Joe-kick", and the recogniser can't tell the difference.
   - **Antetokounmpo** comes out mangled in transcripts either way (the recogniser's limit). Prefer "Giannis" alone in scripts.
3. **Don't use Flash to save credits.** It is the flattest clone (pitch variety 3.69) and has the worst phone intelligibility (6.2%).
4. **"Expressive" settings (B)** are faster (268 wpm), but no more varied in pitch (4.18 vs 4.5-4.9). There's no measured gain, so it's not a default; the owner's ear can overrule.
5. **v3 voices (C, G)** are the most varied in pitch and loudness, which may sound most human. But they are 26-45% slower, and v3 has no speed control.
   - **TEST** one only for a slow, emotional story where pace matters less (e.g. a "legend's ending" Short like Chris Paul's).
   - Not a default.

## Owner listening task (the one thing only you can do; about 2 minutes)
On a phone speaker, play these loudness-matched files in `takes/`:
- `A_clone_prod_lufs16.mp3`
- `A3_clone_raw_names_lufs16.mp3`
- `B_clone_expressive_lufs16.mp3`
- `C_clone_v3_lufs16.mp3`
- `G_liam_v3_lufs16.mp3`

Answer two questions:
1. Which sounds most like a person talking to you?
2. In A vs A3, which "Wembanyama" (at 0-2 s) is right?

Until you answer, production stays on take A3's setup: the clone, multilingual_v2, speed 1.15, plain "Wembanyama".

## Part 2 (Oct 14, later): emphasis, pauses, and the voice with music
**Why:** vidIQ's descriptions said the old hit Shorts stressed every number and paused about 0.4 s before the final word (Posted Video Audit, section 10). Do ours? *(Correction, Oct 14 night: the measured old recordings deliver numbers just as flat, -1.3 to +0.8 dB; audit §11. So flat numbers are not why the new Shorts underperform.)* Code: `emphasis_test.py`. Results: `emphasis_results.json`. Takes: `takes/E_*.mp3` and `E_*_lufs16.mp3`. About 1.9K characters.

**1. Our narration does not stress the numbers.** [V] Number words vs the other content words, measured on the voice tracks of the 4 ready Shorts:

| Short | Number words | Loudness vs other words | Pitch vs other words |
|---|---|---|---|
| #40 Jokic pass | 11 | -0.4 dB | -2.7 semitones |
| #41 Sharp | 7 | -0.2 dB | +2.7 |
| #21 Jokic record | 14 | -0.1 dB | +0.8 |
| #38 LeBron promise | 13 | +0.2 dB | -0.2 |

The numbers are delivered as flat as the words around them, sometimes quieter.

**2. Text and settings don't fix it** (#40's script, 4 takes, same voice):

| Variant | Pause before "Not eighty-one" | Number loudness vs other words | Words/min |
|---|---|---|---|
| V0 production settings | 0.18 s | -0.5 dB | 289 |
| V1 "..." before the punchline | 0.22 s | -0.7 dB | 289 |
| V2 expressive (stability .45, style .35) | 0.16 s | -1.2 dB | 296 |
| V3 both | 0.24 s | 0.0 dB | 305 |

- "..." adds only about 0.05 s; nowhere near the old 0.4 s beat.
- The expressive setting doesn't lift the numbers either.
- Word error rate was the same for all four (16.2%, from the name spelling).

**3. With music:** the beds in `Library/Music/` cost no words even at -2 LU in the phone simulation. See `Library/Music Guide.md` §5.

**What this means for production** (rules go into Creative System v3 §5-6):
- **Emphasis must come from the edit, not the voice:**
  - put a real pause before the payoff line (cut silence in, 0.3-0.4 s)
  - drop the music for that beat
  - colour the number in the captions
  - circle it on screen
- **Test, not proven:** one cut-in 0.35 s pause before the final line (Outcome Log). The old hit that used it is one Short.
- **eleven_v3** (the most varied pitch in part 1) understands CAPITALS and audio tags for emphasis, but reads 26-45% slower with no speed control. It remains a TEST for an emotional story only.

**Owner's ear (still open):** the listening page has the 5 finalists, the music beds, and every ready Short with and without music.

## Part 3 (Oct 14, night): why the voice sounded wrong, round 2-3 auditions, the decision
**Owner's brief:** the voice is a major problem; fix it, choose one, stop switching.

### A. Diagnosis of the old setup [V unless marked]
1. **It is a copy of a copy.**
   - The clone "pham v2" was trained on recordings of our old Shorts' narration, which was itself TTS (`clonesrc/`, audit §11).
   - Those training files have a high noise floor in the pauses (-20 to -23 dB under the speech) and HNR 7.8-8.3.
   - The clone can't sound cleaner than its source.
2. **Pushed too fast.**
   - Production ran the clone at native speed 1.15-1.2 (auto) plus up to 1.08x stretch.
   - On our Curry script that is **265-267 wpm**. The old hits ran 206-252 (median 220).
   - At 1.15 one take's pitch variety fell to 3.8 semitones (flat).
3. **Denoise dulled it.**
   - The "light" FFT denoise removed about two thirds of the voice's energy above 5 kHz (the s, t, f sounds). #40: 1.69% → 0.56% above 5 kHz; 99% roll-off 6.2 → 4.0 kHz.
   - It raised HNR (8.2 → 9.0) only by removing that detail. TTS has no room noise to remove.
4. **Held back.** Stability .65 trades expression for steadiness.
5. **Not the cause** (audit §11): the delivery of numbers. The old hits were just as flat.

**Fixing the clone works on paper.** "Old voice, fixed" = speed 1.1, stability .5, no denoise:
- reads 224-232 wpm
- pitch variety 4.6-5.1
- consistent (0.98)
- *closer* to the old narration than the production settings (0.969 vs 0.95)

It is the **backup**.

### B. Round 2: 9 Voice Library voices
- Same script (REF) and measures; `audition2.py`, `results2.json`, `results2_extra.json`.
- At speed 1.1 they read 154-196 wpm.
- **Alex led:**
  - WER 0 / 1.7%
  - all 5 names heard right
  - pitch variety 5.36 (the most of the steady voices)
  - numbers +0.87 dB over other words (the only voice that lifts them)
- Lucan Rook and Jon followed.

### C. Round 3: finalists at the real pace, two scripts, two takes (`audition3.py`, `results3.json`, `results3_consistency.json`; about 6K characters)
| Voice | Settings | wpm (REF / story t1, t2) | Pitch var. (st) | Loudness var. (dB) | Pauses > 0.3 s (story) | Take-to-take similarity | Similar to old narration |
|---|---|---|---|---|---|---|---|
| Old voice as it was (P0) | clone, 1.15, stab .65 | 245 / 265, 267 | 4.88, 3.80 | 2.9, 2.6 | 0, 0 | 0.983 | 0.95 |
| Old voice, fixed (P1) | clone, 1.1, stab .5 | 237 / 224, 232 | 4.62, 5.05 | 2.9, 2.8 | 1, 0 | 0.980 | 0.969 |
| **Alex (X1)** | 1.2, stab .5 | 224 / 229, 226 | 4.90, 5.39 | 3.3, 3.6 | 1, 1 | **0.990** | 0.719 |
| Lucan Rook (X3) | 1.2, stab .5 | 227 / 227, 225 | 4.69, 4.75 | 4.3, 4.9 | 9, 8 | 0.976 | 0.706 |
| Jon (X4) | 1.2, stab .5 | 215 / 217, 211 | 3.84, 3.86 | 3.4, 3.3 | 7, 8 | 0.991 | 0.636 |
| Alex on eleven_v3 (X5) | v3 | 184 (REF) | 5.27 | 2.9 | — | — | — |

- Story script = our own Curry Kobes Short (30.8K).
- Every take was heard right, apart from "Kobes" written as "Kobe's", which counts as the 3.9% "error" in every row.
- **Names test** (`names_test.py`, `names_results.json`): Alex read 12 hard names, plain and respelled.
  - The recogniser heard the right name in both versions ("Yokitch" → "Jokic", "Dontchitch" → "Dončić").
  - It can't tell a Y from a J (an onset-noise check, `onset_check.py`, was too noisy to rely on). So the sound is the owner's call.
- **Licence and terms** (API, Oct 14) [E]: rate 1.0 (normal credits).
  - Notice period: Alex 90 days, Lucan and Jon 730 days.
  - Using a library voice through the API adds it to "My Voices" (all 9 auditioned voices are now there), so the notice period protects us if its owner withdraws it.
  - **Commercial use: not confirmed from ElevenLabs' own terms in this run.** Their Voice Library terms page couldn't be reached (404); third-party guides say every paid plan includes a commercial licence. **Owner to-do:** open ElevenLabs → Voice Library → Alex and check the licence shown on the voice before the first post with it.

### D. The decision
**Primary: Alex.** It is the only voice that is, at once:
- in the old hits' pace range at its native speed (no stretch)
- the most varied in pitch and loudness without extra pauses
- the most consistent take to take
- the clearest on names and numbers

**Backup: our clone, fixed.**
- It can't be withdrawn.
- It is the old channel voice, if the owner prefers it.

**Not chosen:**
- **Jon:** cleanest sound, but the flattest pitch and many pauses.
- **Lucan:** least consistent, 8-9 pauses.
- **v3:** too slow.

**Untested outside ElevenLabs:**
- Other providers (OpenAI, Google, Azure voices) need new accounts and keys we don't have.
- ElevenLabs is already paid and has the largest library.
- Say so if you want them tried.

**Real-Short test (done):** #40, #41 and #21 re-voiced (`Productions/…/_v4/CHANGES.md`).
- 220-227 wpm, 23-24 s
- QA PASS
- the music hits are still on their words

**What I can't judge:** whether Alex sounds more human than the old voice. Sound Check round 3 asks the owner.
- If the owner picks another voice, change `voice_config.json` once, and only then.

### E. The house voice spec (for every Short from now on)
| Item | Setting |
|---|---|
| Provider, voice, model | ElevenLabs, Alex `yl2ZDV1MzN4HbQJbMihG`, eleven_multilingual_v2 |
| Settings | speed 1.2, stability 0.5, similarity 0.75, style 0, speaker boost on |
| Script format | plain sentences; numbers as words where the reading matters (`{1,301|thirteen hundred and one}`); no "..." (adds 0.05 s); no respellings in scripts: names go in `pronunciation.json` |
| Pronunciation | `Tools/pronunciation.json`: Yokitch, Dontchitch, Nurkitch, Bogdanovitch, Shengoon, Valanchoonas. Never respell Wembanyama. A new hard name gets a one-line test first |
| Processing | no denoise, no stretch; silences between words capped at 0.38 s (silence only, never a syllable); in the render, a 2.5:1 compressor above -20 dBFS, then the lift to -14 LUFS |
| Gate (`voice_take.py`) | voice_check has no REDO issue; HNR ≥ 7.0, jitter ≤ 3.4, shimmer ≤ 12.5 (Alex's measured range: HNR 7.6-8.7, shimmer 10.6-12.2) |
| Pace | 210-235 wpm expected; QA warns outside 200-265 |
| Cost | about 1 credit per character: about 500 per Short per take. Starter plan, 52,087 a month; 32.7K used on Oct 14 (resets Nov 8) |

## Part 4 (Oct 14, late night): A vs F vs every Pham option, a new clone, and real edits
**Owner's brief:** A and F sound best; also improve Pham, try a new Pham clone, and test in real Short edits.
- **A** and **F** are the round 3 page's labels:
  - A = Alex `yl2ZDV1MzN4HbQJbMihG`
  - F = pham v2 `GDS7e7WiI4GqkoRxZAFG` at speed 1.1, stability .5, similarity .75, no denoise
- **Round 1's labels were different** (A = the clone's production settings; F = the premade "Liam"). If the owner meant round 1's F, say so.

### What the Pham voices are [V, ElevenLabs API]
- **"Pham"** `H2ovX6h6fD6dmyrg5SkI`: an instant clone (category "cloned"), made Jan 8, 2026 from **one 27 s recording**.
- **"pham v2"** `GDS7e7WiI4GqkoRxZAFG`: an instant clone, Jan 8, 2026, from 4 files.
  - **Three of the four are the same recording cut at different lengths** (correlation 1.0): the first 79 s went in 3 times and the next 91 s twice.
  - Unique audio: about 293 s.
- **Plan:** Starter allows instant clones, not professional ones (that needs Creator or above).

### The new clone [V]
- **"Pham v3 (cloud candidate Oct 14)"** `61QfR1QEcJUskHn8yioH`, created tonight through the API. No verification was required.
- **Training:** the same recordings, de-duplicated (one copy each, 255 s + 26 s), pauses trimmed to 0.35 s, loudness-normalised. ElevenLabs' noise removal was off: the source is clean.
- The originals ("Pham", "pham v2") are untouched.

### Round 4 (`audition4.py`, `results4.json`, `results4_consistency.json`; 10 takes, about 5.6K characters)
- **Script:** #21's rewritten v5 (a hook, two names, numbers, a payoff). Two takes per voice. Names through `pronunciation.json` (Jokic → "Yokitch").

| Voice | wpm (t1, t2) | Pitch variety | Loudness variety | Take-to-take | Like the old narration | Longest pause |
|---|---|---|---|---|---|---|
| **A Alex** | 227, 227 | **4.97, 5.24** | 3.31, 3.33 | **0.989** | 0.738 | 0.32 s |
| **F pham v2, fixed** | 220, 236 | 4.66, **3.81** | 3.30, 2.93 | 0.973 | 0.954 | 0.38 s |
| Pham as used until today (pham v2, 1.15, stab .65) | 262, 272 | 4.90, 4.35 | 2.79, 2.90 | 0.992 | 0.960 | 0.28 s |
| Original "Pham" (fixed settings) | 205, 207 | 4.44, 4.60 | 3.16, 2.61 | 0.982 | 0.966 | 0.46 s |
| **NEW "Pham v3"** (fixed settings) | 228, 238 | **3.68, 3.83** | **2.23, 2.18** | 0.979 | 0.915 | 0.34 s |

- Error rates sit at 9.8-14.6% for every voice. That comes from number words ("one ninety-eight" written as "198") and the respelled "Yokitch". All transcripts read correctly.

**Reading it:**
- **A** is the most expressive and the steadiest.
- **F** is the channel's own voice and the cleanest-sounding, but one take in two goes flat.
  - `voice_take.py` now rejects flat takes: a pitch gate per voice, 4.5 for A and 4.2 for F.
- **Today's production Pham** is simply too fast.
- **The original Pham** is slow, with more pauses.
- **The new clone is the flattest of all five.** De-duplicating the recordings did not make it livelier, so **it is not adopted** (kept in `voice_config.json` as `pham_v3_test` for reference).
- **What "improving Pham" turned out to mean:** the fixed settings on the existing pham v2, which is F, plus no denoise, no stretch, the pause cap and the dictionary. Not a new clone.

### Real edits (the owner's comparison)
- **#21 v5:** `_v5` (A) and `_v5_F` (F).
- **#36 v2:** `_v2` (A) and `_v2_F` (F).
- Same script, footage and edit; no music. All QA PASS. Both are in the Hub cards.
- I can't hear them. **The owner's one-word answer (A or F) sets `voice_config.json` "default"**, and then no more switching.

### What would still be worth trying (not done)
- A **professional** clone of the original narrator would need the Creator plan and about 30+ minutes of clean recordings of one consistent voice.
- We only have about 5 minutes, and it is itself old TTS output. So a better Pham clone is limited by the source, not the settings.

## Part 5 (Oct 15, overnight, on the PC): A vs F on a new Short, one take each
**Owner's brief (Oct 15):** keep testing Alex against pham v2 on one new Short, one take in each voice, no third take, no Pham v3, default unchanged, #36 not re-voiced.
- **Short:** #42 "Who Has Missed The Most Shots Ever" (the approved script, 81 spoken words, no voice before). Files: `Productions/MetaSports/2026-10-14 42 .../_v1` (A) and `_v1_F` (F). Full write-up: `VOICE_AB (Oct 15, 2026).md` in that folder.
- **Spend:** 952 characters (2 x 476). Used 48,539 -> 49,491 of 52,087; **2,596 left**, resets Nov 8.
- **Measured with `voice_take.py --takes 1` and `voice_check.py` (local whisper), plus a throwaway envelope check:**

| Measure | A Alex | F pham v2 |
|---|---|---|
| Length | 23.47 s | 22.68 s |
| Real pace (81 spoken words) | 210 wpm | 217 wpm |
| `voice_check` | REDO (one flag: final word "times." 0.87 s) | CHECK (no issue) |
| HNR / jitter / shimmer | 8.9 / 2.52 / 10.76 | 10.1 / 2.36 / 9.46 |
| Pitch variety (semitones) | 4.80 | 4.66 |
| Loudness variety (dB SD) | 3.22 | 2.64 |
| Numbers vs other words (loudness) | 0.0 dB | -0.9 dB |
| Gate (`voice_take`) | FAIL, on that one flag | PASS |

- **The flag on Alex is a tail effect:** the word is about 0.25 s at -18 dBFS, followed by a faint tail near -45 dBFS and silence. Trim the tail in the render; no new take needed.
- **Alex's soft spot is small words** (one "The" not heard, one "the" at -13 dB). **pham v2 is cleaner and steadier;** Alex is a little more varied and ends harder. Neither lifts the numbers, so emphasis still has to come from the edit.
- **Takes to pass the gate over three pairs (#21, #36, #42):** Alex 3, 2, not passed on its one take; pham v2 1, 2, 1. With 2,596 characters left, first-take passes matter.
- **Still the owner's call, by ear:** A or F. One word sets `voice_config.json` `"default"`.
