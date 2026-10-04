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

## Open tests (waiting on the user's analytics in 1-3 days)
question vs number hook; hook headline vs none; music vs none; ALL CAPS vs Clank captions; rule vs contract vs funny lane. Read "Viewed vs swiped away" at 24 h: 70%+ good, <60% rewrite the first 2 s.
