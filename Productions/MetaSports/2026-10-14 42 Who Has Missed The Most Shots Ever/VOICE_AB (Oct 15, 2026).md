# #42 voice test: Alex (A) against pham v2 (F), one take each (Oct 15, 2026, overnight)

**Owner's rules, all kept:** one new Short; one take in each voice; no third take; `voice_config.json` untouched (default is still `primary` = Alex); Pham v3 not used; #36 not re-voiced.

**Spend:** 2 takes x 476 characters = 952. ElevenLabs "used" went 48,539 -> 49,491 of 52,087, so **2,596 characters are left** (resets Nov 8). No other credits were used: `voice_check.py` ran on local whisper, not Scribe.

**Script:** the approved `script.txt`, unchanged (Script Critic Log: PASS 34/45; it was blocked only on footage). 81 spoken words.

## Where the files are
| Folder | Voice | Settings (from `voice_config.json`) |
|---|---|---|
| `_v1/` | **A = Alex** `yl2ZDV1MzN4HbQJbMihG` (profile `primary`) | multilingual_v2, speed 1.2, stability .5, similarity .75 |
| `_v1_F/` | **F = pham v2** `GDS7e7WiI4GqkoRxZAFG` (profile `backup`) | multilingual_v2, speed 1.1, stability .5, similarity .75 |

Each folder holds `voice.mp3` (pauses capped at 0.38 s, 0.3 s tail pad), `voice_raw.mp3` (the API output, untouched), `words.json`, `captions.srt`, `voice_take.json`, `voice_check.json`, and the script it was made from. Both versions stay on disk. Nothing is rendered: there is no footage cut yet, so there is no video to compare.

## Measured (I cannot hear audio; the owner's ear decides)
| Measure | A Alex `_v1` | F pham v2 `_v1_F` |
|---|---|---|
| Length of `voice.mp3` | 23.47 s | 22.68 s |
| Real pace (81 spoken words over the speech) | 210 wpm | 217 wpm |
| `voice_check` verdict | **REDO** (one flag, see below) | CHECK (notes only, no issue) |
| Numbers heard right (15,541 / 14,481 / 51% / 45 / 31,502) | all | all |
| Words the recogniser did not hear | "The" at 7.3 s (before "old record"); a very quiet "the" (-13 dB) at 12.6 s | none |
| Clarity, HNR (gate) | 8.9 dB (>= 7.0) | 10.1 dB (>= 7.6) |
| Jitter (gate <= 3.4) | 2.52 | 2.36 |
| Shimmer (gate) | 10.76 (<= 12.5) | 9.46 (<= 11.5) |
| Pitch variety, semitones (gate) | 4.80 (>= 4.5) | 4.66 (>= 4.2) |
| Loudness variety, SD of word level | 3.22 dB | 2.64 dB |
| Numbers against other words, loudness / pitch | 0.0 dB / +0.3 st | -0.9 dB / -0.8 st |
| Pauses over 0.3 s | none (longest 0.17 s) | none (longest 0.06 s) |
| Loudest 50 ms in the last word "times." | -17 dBFS | -26 dBFS |
| `voice_take` gate | FAIL (only because of the REDO flag) | PASS |

## Reading it
- **Alex's one REDO flag is a tail effect, not a stretched word.** `voice_check` flagged the last word "times." because the alignment gives it 0.87 s. The audio says otherwise: the word itself is about 0.25 s at -18 dBFS, then a faint decay near -45 dBFS for about 0.35 s, then near-silence. If A is picked, trim that tail in the render (free). No new take is needed. I did not regenerate, because of the one-take cap.
- **Alex's small words are the soft spot.** The recogniser missed one "The" and one "the" sits at -13 dB. On #36 `_v2` the earlier check said Alex dropped "He"; a re-run today on the same file heard it, so this is "sometimes", not "always".
- **Pham v2 is the cleaner and steadier take** (higher HNR, lower jitter and shimmer, no flags). **Alex is a little more varied** (loudness 3.2 vs 2.6 dB, pitch 4.8 vs 4.7 st) and lands the closing word harder (-17 vs -26 dBFS). Pham's last word trails off.
- **Neither voice lifts the numbers.** Alex is flat (0.0 dB), Pham dips (-0.9 dB). The earlier finding stands: emphasis has to come from the edit (a real pause before the payoff, the number coloured in the captions).
- **Neither take has the 0.2 s beat before "No."** that PACKAGE.md asks for (Alex 0.08 s, Pham about 0). Cut it in at assembly.
- **`voice_check` shows 163 and 169 wpm for these takes.** That is an artefact: it counts "15,541" as one word. The real pace is 210 and 217 wpm, inside the expected 210-235 range.

## The three A/F pairs so far
| Short | Alex: takes to pass / wpm / pitch SD / HNR | pham v2: takes to pass / wpm / pitch SD / HNR |
|---|---|---|
| #21 v5 | 3 / 224 / 4.63 / 8.2 | 1 / 215 / 4.62 / 8.3 |
| #36 v2 | 2 / 215 / 5.25 / 8.9 | 2 / 224 / 4.95 / 9.4 |
| #42 v1 (one take each) | not passed on its one take / 210 (real) / 4.80 / 8.9 | passed on its one take / 217 (real) / 4.66 / 10.1 |

Cost point for the decision: at about 476 characters a take, Alex has needed 2, 3 and 2+ takes to pass the gate; pham v2 has needed 2, 1 and 1. With 2,596 characters left until Nov 8, a voice that passes on the first take is worth roughly an extra Short. Three pairs is a small sample, and two of Alex's three failures were recogniser quirks on the last words rather than a bad read.

## What only the owner can do
Listen to both `voice.mp3` files, and pick **A or F** in one word. The three places that tell them apart: the opening line (0-3 s), the three big numbers (about 3-5 s, 7-9 s, 20-22 s), and the closing "...thirty-one thousand, five hundred two times." (about 19-23 s). Then set `"default"` in `Tools/voice_config.json` once, and stop switching.

## Not done
No render, no captions burn, no music, no `qa_short.py`. The footage is partly in hand (see PACKAGE.md, "PC footage"): the LeBron airball is cut-ready, the Kobe fadeaway is not cut.
