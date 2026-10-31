# Voice audition round 5 (Oct 19, 2026): the Creator plan, Eleven v4, on #42's script

**Owner, Oct 19:** "I just got a new ElevenLabs subscription, the Creator one. Analyze what that does, go back on all the ElevenLabs research, cloning etc. Spend time working on the most optimal voice, test using shorts instead of waiting for my approval."

## 1. What the Creator plan gives us (read from the API today, not from memory)
- `/v1/user/subscription`:
  - tier `creator`, **121,224 credits/month** (0 used at the start); about 250 Shorts of narration at about 475 characters each, or about 25 full test rounds
  - 30 voice slots (3 used before today)
  - instant voice cloning: yes
  - **Professional Voice Cloning: yes, 1 slot**
  - higher-quality output (192 kbps mp3, now the default in `voiceover.py`)
- `/v1/models`:
  - **Eleven v4** and **v4 Turbo** are available (released Sept 28, 2026; never tested by us before today)
  - v4 docs: better clone accuracy and audio tags, **no Speed or Style slider**, Stability and Similarity only
- **Voice design** (text-to-voice) works on this plan. We designed and saved **"MetaSports Designed Narrator v1"** (`ZDWTvr6sH1FkK9WLbGNF`): owned by the account, no notice period, nobody else's voice.
- **Professional Voice Clone: not used.** ElevenLabs makes the speaker verify their own voice. Our only long clone source is the old channel narration (about 9 minutes), and its speaker can't do that verification. The slot is the right tool only if the owner (or a voice actor with a contract) records about 30+ minutes. We never clone a real person's voice without their consent (that includes CoachClank's narrator).

## 2. What earlier rounds found (Oct 5-15) and what changed
- **Rounds 1-4** (all on multilingual v2):
  - Alex won on pitch variety, consistency, clarity and names
  - our clone (pham v2) stayed as the backup
  - v3 was rejected as "too slow"
- **Since then:**
  - Alex's Shorts include our two best new posts: #42 (84.3% stayed, 25K) and #44 (10K)
  - **Alex is the most-used voice in the ElevenLabs library** (3.7 billion characters in the last year, 1.2 million clones, from `/v1/shared-voices` today), so thousands of channels sound like us
  - v4 is new

## 3. Round 5 method
- **Script:** **#42's exact script** (475 characters, numbers spoken in full).
- **Takes:** 11 voice × model takes, plus a second take of each finalist.
- **Measures:** the same code as rounds 1-4 (`../Voice Audition (Oct 14, 2026)/audition.py`):
  - pace
  - words heard right through a **phone-speaker simulation** (faster-whisper)
  - pitch variety, loudness variety
  - HNR / jitter / shimmer
  - pauses over 0.3 s
  
  Added: speaker similarity (resemblyzer) to the posted #42 voice and to **CoachClank's narration** (one TikTok sample with music underneath, so it's a rough reference).
- **Pace:** v4/v3 read about 150 wpm with long pauses and have no speed control. So stage 2 (`audition5_norm.py`, no credits) trims pauses to 0.18 s and stretches every take to the **#42 control's length (214 wpm)**. Voices are compared **at the same pace**.
- **Gates (set before the results):**
  - HNR ≥ 7.0, jitter ≤ 3.4, shimmer ≤ 12.5
  - pitch variety ≥ 4.5 semitones
  - phone-test word errors no more than 3 points worse than the control
  
  The 16.7% shared floor is the recogniser writing "2024"/"Kobe's" differently, the same in every take.
- **CoachClank's pace for reference:** 240-303 wpm across 20 of his Shorts (caption timings; median about 270). #42 itself ran at about 214 (written words; about 194 counting each spoken number word).
- **Credits used:** about 7,500 of 121,224.

## 4. Results at equal pace (`results5_norm.json`; raw takes in `results5.json`)
| Take | Raw wpm | Stretch | Phone WER % | Pitch var. | Loud var. | HNR | Jitter | Shimmer | Pauses > 0.3 s | Sim. to #42 voice | Sim. to CoachClank |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Alex, multilingual v2, speed 1.2 (CONTROL: the #42 and #44 voice) (t1) | 214 | x1.0 | 16.7 | 5.11 | 3.33 | 8.6 | 2.75 | 11.07 | 5.0 | 0.991 | 0.696 |
| Alex, multilingual v2, speed 1.2 (CONTROL: the #42 and #44 voice) (t2) | 216 | x1.0 | 16.7 | 5.42 | 3.27 | 9.1 | 2.61 | 11.03 | 5.0 | 0.981 | 0.71 |
| Alex, Eleven v3 (t1) | 154 | x1.346 | 15.2 | 5.35 | 2.54 | 7.9 | 3.23 | 11.85 | 6.0 | 0.909 | 0.711 |
| Alex, Eleven v3 (t2) | 169 | x1.248 | 16.7 | 4.83 | 2.1 | 8.4 | 3.02 | 10.57 | 3.0 | 0.922 | 0.7 |
| Alex, Eleven v4 (t1) | 153 | x1.342 | 16.7 | 5.07 | 3.8 | 8.3 | 2.93 | 12.74 | 6.0 | 0.956 | 0.672 |
| Deuce - Sports Podcast (library, young American), v2, speed 1.2 (t1) | 184 | x1.0 | 30.3 | 2.47 | 4.3 | 12.5 | 2.07 | 10.19 | 8.0 | 0.632 | 0.66 |
| Deuce, Eleven v4 (t1) | 150 | x1.288 | 16.7 | 3.67 | 4.62 | 11.3 | 2.5 | 12.99 | 5.0 | 0.634 | 0.648 |
| pham v2 (our clone of the old channel narration), v2, speed 1.1 (t1) | 216 | x1.0 | 22.7 | 5.05 | 2.72 | 9.1 | 2.64 | 9.65 | 4.0 | 0.778 | 0.753 |
| pham v2 clone, Eleven v4 (t1) | 178 | x1.183 | 22.7 | 4.66 | 2.48 | 9.2 | 2.83 | 9.54 | 3.0 | 0.746 | 0.751 |
| Liam - Viral Short-Form (library, 443M chars/yr), v2, speed 1.2 (t1) | 231 | x1.0 | 16.7 | 3.45 | 3.79 | 10.4 | 2.72 | 10.0 | 8.0 | 0.675 | 0.647 |
| Liam - Viral Short-Form, Eleven v4 (t1) | 153 | x1.28 | 21.2 | 4.16 | 3.62 | 9.9 | 3.07 | 11.08 | 6.0 | 0.676 | 0.634 |
| Ninja - Engaging Sports (library, young American), Eleven v4 (t1) | 151 | x1.234 | 16.7 | 4.35 | 5.89 | 9.4 | 2.08 | 10.81 | 2.0 | 0.727 | 0.671 |
| Ninja - Engaging Sports (library, young American), Eleven v4 (t2) | 152 | x1.25 | 16.7 | 4.56 | 5.98 | 9.2 | 2.4 | 11.11 | 2.0 | 0.728 | 0.681 |
| our designed voice (text-to-voice, owned by the account), Eleven v4 (t1) | 151 | x1.265 | 18.2 | 4.94 | 3.92 | 9.8 | 3.05 | 10.25 | 4.0 | 0.744 | 0.664 |
| our designed voice (text-to-voice, owned by the account), Eleven v4 (t2) | 153 | x1.247 | 16.7 | 5.12 | 3.83 | 9.9 | 3.03 | 10.76 | 5.0 | 0.752 | 0.668 |
**Against the gates:**
- **PASS, both takes:**
  - **Alex v2** (control): pitch 5.1 / 5.4, HNR 8.6 / 9.1
  - **Designed Narrator v1 on v4**: pitch 4.9 / 5.1, HNR 9.8 / 9.9 (the cleanest of the passers), loudness variety 3.8-3.9 (a little more lift than Alex's 3.3); jitter 3.0 is close to the gate because of the x1.25 stretch
- **Pass with a risk:** Alex v3. It needs x1.25-1.35, which is too much stretch, and it has the flattest loudness (2.1-2.5).
- **Fail:**
  - Alex v4: shimmer 12.7 after the stretch
  - Liam "Viral Short-Form": flat pitch (3.5-4.2)
  - Deuce: flat pitch, plus 30% WER on v2
  - our clone: v2 and v4 both +6 WER (misheard words)
  - Ninja: pitch 4.35-4.56, borderline; loudness swings 5.9 dB, which may read as shouty

## 5. Decision (made without waiting for approval, as asked)
**The measures tie Alex and the designed voice.** Measures can't decide a tie, so the next step is a test on real posts, which is what CoachClank's results are built on: one format, change one thing, read the numbers.
- **Primary stays Alex v2 for now.** It is the voice on our two best new Shorts, and switching on a tie would throw away evidence.
- **The live A/B:**
  - the next 4 THE #42 FORMAT posts **alternate Alex / Designed v4** (Alex, Designed, Alex, Designed)
  - same format, same edit rules
  - every draft is rendered in both voices, so the order never waits on a re-voice
- **Read:**
  - "stayed to watch" from the weekly Studio export
  - engaged ratio and retention curves from the daily API pull
- **Switch rule (pre-registered):**
  - the designed voice becomes primary if its 2 posts average **≥ 3 points more "stayed"** than Alex's 2, with average % viewed not worse
  - otherwise Alex stays and the designed voice is retired
- **Profiles:** `voice_config.json` → `primary` (Alex v2) and `designed_v4` (eleven_v4, target 214 wpm, pauses 0.18 s, stretch up to x1.3). Use `voice_take.py ... -- --voice designed_v4`.

**What I can't do:** listen. Nothing here says which voice sounds better to a person. The owner's ear can overrule at any time, and the live A/B is the real judge.
