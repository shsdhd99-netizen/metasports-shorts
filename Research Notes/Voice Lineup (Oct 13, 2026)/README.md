# Voice lineup (Oct 13, 2026): fair, blind, same script
Page for the owner (phone): https://claude.ai/artifact/Y9P8QRytak2ikDRfMDqdj2 (private; blind numbers, names behind a "reveal").
Listening task: phone speaker, normal volume, play all five, reply with one number or "none".

## What was wrong with the Oct 5 comparison (VERIFIED, measured today)
- **Loudness was not matched.** The clone samples (A/B/C, 1-4) sat at -28.7 to -29.8 LUFS; the premade v3 samples at -16 to -24.7 LUFS. A 5-14 dB gap biases any listening test (louder usually sounds "better").
- **Scripts were not identical.** The clone samples said "players", the premade ones "guys"; the s2 clips were 8.5 s excerpts, the others 14-22 s.
- **The two "tight" samples recommended to the owner had damaged words.** Whisper heard "198" as "190" (charlie_v3_tight) and "198. 11" as "1-9-11" (liam_v3_tight). The untrimmed takes read "198" correctly. Cause: Tools/voice_fx.py cut wherever the TTS timestamps said there was a pause, and the timestamps can end early. Fixed Oct 13 (cuts only inside measured silence); re-trimmed takes read "198" correctly with the same pace gain.

## This lineup (gen_lineup.py; ~412 characters per take, 4 takes = ~1,650 ElevenLabs characters)
Same text for all: the #19 Flagg narration without the quote clips (text.txt). Edges trimmed, 0.15 s lead-in, each take gain-matched to -16 LUFS (all within -16.4 to -16.9 after limiting).
Slots were shuffled (seed 13); see lineup.json for the key. Every take was transcribed with whisper: all words correct (only spellings like "Mark Stein" / "Flag's" from the recogniser).

| Slot | Voice | sec | wpm (whisper) | HNR dB |
|---|---|---|---|---|
| 1 | Clone, setting C (eleven_multilingual_v2, speed 1.2, stability .65, similarity .7) | 15.0 | 307 | 7.7 |
| 2 | Posted #19 voice (old clone settings, spliced pieces) = what ran in the 20.4K Short | 17.5 | 263 | 6.9 |
| 3 | Liam premade, eleven_v3, pauses trimmed (fixed tool) | 25.4 | 181 | 8.2 |
| 4 | Adam premade, eleven_v3, pauses trimmed | 25.3 | 176 | 9.1 |
| 5 | Charlie premade, eleven_v3, pauses trimmed | 25.2 | 178 | 10.3 |

Objective notes (not taste): the v3 voices make the same 70 words ~8-10 s longer, so their scripts must be ~25% shorter to keep a 22-25 s Short. HNR (clarity) cannot measure naturalness; wpm here is whisper words / speech time, not the same method as the older 265-309 "CoachClank" figure (words / video length), so do not compare those numbers directly.
Decision rule: no bulk re-record until the owner names a slot. If the owner picks 2 (the posted voice), keep the current pipeline and fix only defects.
