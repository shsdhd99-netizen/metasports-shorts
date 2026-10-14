# Voice audition (Oct 14, 2026): 12 takes, one script, same measures

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
