# Editing and Sound Standards (canonical; Oct 15, 2026)

**What this covers:** how a MetaSports Short is cut, moved, captioned, paced and mixed, and the QA gate that checks it.
- **Footage sourcing:** `Library/B-roll Sourcing Guide.md`.
- **Music rights:** `Library/Sound Library.md`.
- **Story and script:** `MetaSports - Playbook.md` (Winning Formula) and `Tools/script_critic.md`.

Where an older Playbook section (§5) disagrees, this page wins.

**Evidence tiers:**
- **[V]** measured on our files
- **[S]** small-n support
- **[E]** external
- **[H]** house choice or hypothesis

**Limit, said once:** I can't hear audio. Sound standards are set and checked by measurement; the owner's ear is the final check.

## 1. B-roll sequencing
1. **Frame 1 is the subject of line 1, doing the thing line 1 claims.**
   - Never a card or screenshot in the first 3.5 s.
   - [S] Our 4 most-viewed October posts had none before 7 s. CoachClank's top scripts point at the clip on screen ("This has to be the funniest way to end a game").
2. **One shot per claim, cut on the word that names the new thing.**
   - Set `anchor` in shots.json to that phrase; `anchor_shots.py` places the cut on the word.
   - The viewer sees the proof as they hear the claim.
3. **The order inside a beat:**
   1. the exact moment
   2. the subject's reaction or face
   3. a wide or context shot
   4. a card, only when no footage proves the number
4. **Hold the payoff shot longest** (1.5-2.8 s) and end 0.15-0.4 s after the last word. [S]
5. **Never the same footage twice**, under any file name.
   - `qa_short.py` catches the same file; `footage_qc.py` catches the same frames under another name (b7L/b7M, a1/a1_df).
   - A deliberate replay is marked `"replay": true`.
6. **A source's own cut inside a shot must stay on the same subject and game.**
   - `footage_qc.py` lists internal cuts with times.
   - #21's a3 montage cuts from a Kings game to a Warriors game at 1.8 s: fine under "Westbrook…", wrong under a line about one game.
7. **Shot length:** no fixed average (the Rules Audit found none that separated winners).
   - Footage shots up to 3.6 s, quotes up to 4.5 s.
   - Nothing under 0.6 s except a deliberate flash cut.

## 2. Keyframes and motion
| Move | When | Setting | Why |
|---|---|---|---|
| **Push-in** (`"zoom"` in shots.json) | stills, cards, and static footage (bench, face, interview) only | 2-5% over the shot, **at most 4% per second** (`footage_qc.py` warns above it) | Subtle movement keeps a static shot alive. On fast action it stacks motion on motion [H] |
| **Hard cut** | between every shot | — | Our old hits and CoachClank's watched TikToks are hard-cut. No dissolves, spins, glitches or whip transitions [S] |
| **Circle / ring** (`broll.py circle`) | on the number, clock, shoe or hand the line names | drawn on in about 0.2 s, held while it's named | Proof you can see [S] |
| **Shake or zoom-punch effects** | never | — | Reads as filler; makes small text unreadable [H] |

**Safe areas (1080x1920):**
- Keep faces, circles and the key action inside **x 60-950, y 250-1500**.
- The Shorts UI covers:
  - the bottom ~22% (title, channel, sound)
  - the top ~8%
  - **a right-hand column from x≈950, about 45-90% of the height** (like, dislike, comment, share)

## 3. Captions
| Item | Standard | Checked by |
|---|---|---|
| **Look** | white Montserrat Black caps, size 86, black outline 6, centred at y=1185 (62%), 2-3 words per card, a 90 ms pop from 86% to 100% | `captions.py` "metasports" style |
| **Accuracy** | **the approved script, word for word.** Names spelled as in the script; respellings live only in `pronunciation.json` | `export_check.py` (any difference = FAIL) |
| **Timing** | every word on screen while it's said; no card under 0.25 s; no overlaps | `export_check.py` |
| **Width** | **at most 820 px.** Centred, a wider line passes x=950, into the button column. `captions.py` now shrinks a long card to fit (Oct 15). Before that, cards like "TWENTY-SEVENTH GAME" ran 867 px | `export_check.py`, measured with the real font and calibrated on a burned frame |
| **Emphasis** | colour (red/green) only on the 1-2 words that carry the story, on at most 35% of cards; never two coloured cards in a row | `captions.py` `limit_colors` |
| **No hook headline text** | owner's rule | `assemble.py` (disabled) |

## 4. Pacing
- **The voice runs from 0.0 s.**
  - No dead air over 0.6 s inside the speech (`qa_short.py`).
  - The pause cap in the voice is 0.38 s.
- **Length:** whatever the story needs. Studio export: no link to views in 22-33 s [V].
- **One beat per line.** If a line has no new picture, it probably has no new information either: cut the line, not the picture.
- **Silence as a move:** a 0.25-0.4 s gap before the payoff line is the only planned pause [S: our old hits' music drops].

## 5. Sound
| Layer | Standard | Checked by |
|---|---|---|
| **Voice** | -14 LUFS integrated (±1.5), compressor 2.5:1 before the lift, true peak at or under -1 dBTP; **no clipped samples** | `qa_short.py` (loudness, true peak), `export_check.py` (clipping in voice.mp3 and the export) |
| **Background music** | **none by default** (owner, Oct 14). A real song only through the platform's library, added by the owner in the app (`Sound Library.md` §2) | `qa_short.py` warns if a bed is baked in |
| **Sound effects** | **0-3 per Short, only where the picture makes the sound** (a swish on a make you see, a whistle you see, a horn at a buzzer) or one soft whoosh into a proof card. Never as decoration; never the vine boom | the human check against the frame sheet |
| **Effect level** | Start at the catalog gain (`Tools/sfx/catalog.json`, -8 to -15 dB on peak-normalised files). Place effects in a gap between words or under a vowel, never on a name or number | [V] Oct 1 measurement: at 4 dB lower, effects added under 1 dB and were inaudible under the voice. The owner's ear decides |
| **Broadcast audio** | never under narration (commentary or crowd from the clip) | clips are cut without audio |

## 6. The QA gate (run all three; `qa_short.py --full` runs them together)
| What can go wrong | Automatic check | Human check | Calibration and limits |
|---|---|---|---|
| **Mismatched b-roll** (wrong player, game, season) | `footage_qc.py` lists internal cuts; `qa_short.py` FAILs any clip without a verified `sources.csv` row | Look at every used second against the line: player, uniform, scorebug, arena, season | Pixels can't tell a wrong jersey. This stays a human step |
| **Blurry or low-res footage** | `footage_qc.py`: **upscale factor** from the logged source size and crop (warn over 2.0x, FAIL over 3.0x) and **softness** (edge contrast under 35% of the Short's median) | Look at flagged shots | A pixel-only upscale test was tried and **dropped**: on our compressed clips it couldn't tell 1.8x from 2.7x. The factor comes from the log or reads "unknown", never a guess |
| **Duplicates** | `qa_short.py` (same file), `footage_qc.py` (same frames, any file) | — | dHash, 2+ matching frames |
| **Dead air** | `qa_short.py` (over 0.6 s inside the speech = FAIL) | — | — |
| **Caption timing and spelling** | `export_check.py` | — | Exact text match to `script.txt` |
| **Voice clipping and volume** | `export_check.py` (clipped runs), `qa_short.py` (loudness, true peak), `voice_check.py` (per-word level jumps) | The owner's ear | — |
| **Excessive motion** | `footage_qc.py`: busiest 10% of our clips (p90 frame change over 38) and push-ins over 4%/s | Look at flagged shots | Calibrated on 51 clips from #21, #36, #39, #40, #41 (median p90 17-20) |
| **Wrong scorebugs and context** | none (pixels) | The verify step: the scorebug must match the line or be cropped (`B-roll Sourcing Guide.md` rule 3) | Human only |
| **Weak opening** | `script_lint.py` (number-led, list-like, claim-less first line); `qa_short.py` (first word by 0.4 s, action footage in the first 3 s, no early card) | Script Critic v3 Hook score | Studio export: stayed-to-watch +0.77 with views |
| **Black frames, gaps, flashes** | `qa_short.py` (black, frozen footage, held frames), `footage_qc.py` and `deflash.py` (one-frame flashes) | Frame sheet around every cut | — |
| **Export vs approved script and timeline** | `export_check.py`: captions = script; local speech-to-text of the export vs the script (numbers folded); picture and sound the same length; shots in order; 1080x1920 | Watch the render once at full speed | Speech-to-text mishears names ("Bouser" for Boozer), so word differences are "listen for", and only a low match fails |

**First run of the new checks (Oct 15), on the two ready drafts:**
- **#21 v5:**
  - Shot 2 (a1L) comes from a **640x640 post: 3.0x upscale** (warn). The log shows it's the NBA's own tribute post; a larger copy hasn't been searched for yet.
  - The widest caption ran 867 px (now auto-fit for future renders).
  - Two shots flagged busy (a fast dunk montage, a pan).
  - 2 shots flagged soft (a2, b4c).
  - Export speech matches the script at 98%; the differences are speech-to-text mishearing "Nikola" and the hyphenated "twenty-seventh".
- **#36 v2:**
  - Shots 8 and 10 (a1_df, a1bj: the 2007 LeBron close-up) are **soft**. A look at the frame confirms it: a dim, blurry archive close-up. Swap it if a sharper 2007 Finals shot exists.
  - One internal cut (e1bg_df) is the same game, as already logged.
  - The widest caption ran 861 px.
  - Export speech matches at 97% ("Bouser" for Boozer).
- Neither draft FAILs. The warnings are in their CHANGES.md as to-dos.

## 7. Voice (current state; testing continues)
- **Default A (Alex), backup F (pham v2, fixed settings).** The owner picks between the two real edits of #21 v5 and #36 v2 in the Hub.
- **New drafts are voiced in A.** An F twin is made when credits allow, so the owner's choice is always between real edits.
- **Every take** goes through `voice_take.py` (best of N; gate on HNR, jitter, shimmer and pitch variety per voice), then `voice_check.py`.
- Research: `Research Notes/Voice Audition (Oct 14, 2026)/README.md`.
