# Lessons learned (running log). Read this before making any Short.

Updated 2026-10-04 after Shorts #11-#15 and the LeBron redo.

## The user's standards (never make them say these again)
- First 1-3 seconds must be extremely strong: real, moving, story-specific footage plus the name/number line at 0.0 s.
- Real clips and real b-roll, not talking heads or text cards. A single talking-head clip for 30 s got "this sucks, swipe in 3 s" (#15 v1).
- Scripts flow and pay off; no repetition. House style: ALL CAPS captions, red/green accents.
- Never upload or publish. The user posts. Chat short, plain English, phone-friendly. Key never in chat/commits.
- Each Short goes into the Hub (title, pinned comment, tags 440-490 chars, no description) and is pushed to `main-329h3w`.

## What works (evidence in this project)
- Find the FRESH, visual news first (Oct 2: Heat "Night in Vice City" x GTA 6 had official reveal video on X). A story with great official footage beats a clever script with none.
- Rule/ban/"caught" and funny-quote lanes; titles 5-7 words with one 😳/😭/💀 emoji.
- Real quote bursts (<=4 s) spliced between narration (`Tools/splice_voice.py`), not long raw interviews.
- Official X accounts give the cleanest footage (`Tools/x_clip.py`). Search with WebSearch `allowed_domains: x.com`; many tweets have no video: try 5-8 links in one call, the one with video is usually the brand/team account (GTASeries, team accounts).
- Square sources: crop with `--x`; if text spans the width (posters), blur-fit it on a 9:16 background and lift it above the caption band.
- Hook headline (`--hook-text`) must be <= 14 characters per line or it clips ("HEAT BECOME|VICE CITY").
- A dull white-page evidence card is worse than b-roll. Keep cards <= 2 s and <= 25% of runtime.

- Auto-transcription mishears names (Milwaukee -> 'Madrid'): override with `text` in the splice plan. Source videos often have burned-in subtitles: crop them out (`broll.py cut --zoom 1.25 --y 0.0`) or they clash with our captions.
- A 'first time ever' angle (Giannis vs the team that drafted him) + a second fresh hook (Vice City night) made #16; look for two news items that collide.

## Mistakes to never repeat
- Building around one clip (#15 v1: 44-100% talking head).
- Opening on a filler word ("So", "Look", "That's"), or on an interview line.
- Cards 3+ s long (#11, #12, #13 had them; remade with cut-aways, loops added).
- Lifting the final mix instead of the voice (made effects loud). Lift the voice first.
- Parsing ffmpeg astats for music start (nonsense); use numpy loudness windows.
- Forgetting `kind` in shots.json (the gate needs it). Shell `$` in covers: single quotes.
- Trusting one source on contracts: two reports disagreed on Duren; use "reportedly".
- Hub: in-page `<a href>` downloads do not work; use `downloads.save`. Assets must be in the scratchpad to upload. `ArtifactData` writes need `if_version`.
- Cloud: no GPU (assemble falls back to CPU, prints a harmless nvenc error); YouTube download blocked (use X, archive.org, preview frames, PC cut manifest).

## The gate (Tools/qa_short.py): all must pass before delivery
voice at 0.0-0.4 s, non-filler first word, 3+ shots and real action in first 3 s, no shot over 3 s (quotes 4), avg <= 1.9 s, no clip over 35%, 6+ clips, talking head <= 45%, b-roll >= 35%, cards <= 25%, loops, -14 LUFS. Old Shorts: add `--infer-kinds`.

## Status of earlier Shorts vs the gate
- #14 passes as made. #13 and #12 v2 remade (shorter cards, cut-aways, loop) and now pass; #15 rebuilt and passes.
- #11 (Jordan) and LeBron v6/v7 were not remade: their source clips are not in the repo (they came from the PC). Failures were small (two 3.2-3.4 s cards, no loop). To remake: re-fetch footage and rerun with the gate.

## Posted so far (do not rework these)
- Duren (#12) and the Wembanyama Short are already uploaded (user, Oct 4). Results from the user due within 36 hours of Oct 4. Do not spend time on them; spend it on NEW Shorts.

## First real results (Oct 4, user's Studio, n=2)
- #03 Wembanyama 'How Did Nobody Vote Against Wemby?' (24 s, record/rule oddity): 79.5% stayed, 100.3% avg viewed, 20.6K views in ~10 h, rank 2 of 10. #12 Duren (33 s, contract): 63.0% stayed, 59.7% avg viewed, 1.5K views in 5.5 h, rank 8 of 10.
- Formula to copy: universal-rule hook -> 'Until X' -> 'not even the crazy part' escalation -> short list payoff, ends on the payoff (no question), ~24 s. Contract/trade stories are the weak lane for this channel. Prefer one-fact record/oddity Shorts of 22-28 s.
- Do not assume longer is better: our own two results go the other way (confounded).

## Open tests (waiting on the user's analytics in 1-3 days)
question vs number hook; hook headline vs none; music vs none; ALL CAPS vs Clank captions; rule vs contract vs funny lane. Read "Viewed vs swiped away" at 24 h: 70%+ good, <60% rewrite the first 2 s.

## Oct 5, 2026 - Critique Round 2 (14 queued Shorts)
- 4 of 14 hooks were false or stale when checked against a primary source (#17 flop technical exists since 2023-24; #22 two players wear six; #15 date order; #16 unrevealed jersey). Rule: before the hook, write 'what is actually new' and the dated source in notes.md. (SUPPORTED: 4 of 14 found by two independent critics.)
- Use the quote burst that IS the payoff; never orphan or narrate a quote (found in #15, #17, #24, #16).
- Pay off the setup, not a prediction; debate question goes in the pinned comment. First result after rebuild: #22 (payoff ending, corrected 'two') ~29K views in ~1 day, best of the last 7 (HYPOTHESIS: views only, n=1).
- Free stats via yt-dlp work in the cloud; vidIQ free plan is credit-limited.

## Oct 13, 2026 - first full week of posting (15 Shorts)
- Reach is not fixed by editing polish alone: 15 Shorts posted Oct 5-13 have a median of ~2.8K views against 21.5-30K before. Only #19 (Flagg height, 20.4K) broke out; #22 (31.8K) and #03 (27.0K) came just before. (PROVEN numbers, HYPOTHESIS cause.)
- Avg % viewed of 100%+ was in all 3 Shorts above 19K views but also in 2 that stayed under 3.4K (#14, #01). Retention is close to necessary for a breakout, not sufficient; the first-second swipe decision (topic, first frame, title) is the other half (SUPPORTED, n=16).
- Re-doing an old winner by topic name (underhand, 73K before) did 1.0K. Pick NEW angles with one checkable fact on a famous name, not repeats (HYPOTHESIS, n=1).
- Do not let the daily-stats routine sit unread: run it, log the numbers, then continue.


## Oct 13, 2026 - handoff audit lessons (verified unless marked)
- Our own tools produced two silent defects that no QA caught: assemble.py looped any clip shorter than its shot (22 of 27 folders, incl. posted #19/#23/#13/#29/#35), and pause trimming cut syllables ("198" -> "190"). Both fixed and now gated. Lesson: every new tool output gets a measured check (speech recognition on audio, frame strips on video) before it is shown to the owner.
- A listening test is only fair at matched loudness and identical text: the Oct 5 samples differed by 5-14 dB.
- The pre-publication critic score predicted views BACKWARDS (rho -0.63, n=14). Judge the premise in second 1 before polish (Tools/critic_v2.md). (SUPPORTED, small n)
- Retelling a story a bigger channel owns (underhand: CoachClank 10M) failed again at 1.0K, exactly as the Sep Playbook rule said. Check rules before building, not after.
- HOLD decisions can be too cautious: #23 (held for the Oct 21 cut) was posted anyway and got the best like rate (3.38%). (n=1)
