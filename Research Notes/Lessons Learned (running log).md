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

## Oct 14, 2026 (critic passes on #40 and #41)
- [V, n=2] The independent critic found defects that QA can't measure: words over the wrong picture (#40's "No look" over the catch), a doctored image (#41's pasted Clippers logo), a quote voiced as fact without its hedge ("probably"), and a team's colours under another team's name. **Rule:** every build gets Critic v2 on the export before "ready".
- [V] Say a number next to a word that sounds like one, and it's misheard: "three hundred and fifty threes" was heard as "353s" twice. **Rule:** never put a spoken number directly before "threes", "fours" or "twos"; reword ("Three-point tries: three hundred and fifty").
- [V] When sources disagree on a stat (Sharp's FT%: 39.3 / 41.5 / 42.9%), don't voice it; use the fact every source agrees on (0 G League threes).
- [S] A one-number answer card that reveals in two steps (350 first, then 0 on "zero") keeps the payoff from showing before the line. Retention effect unknown (HYPOTHESIS).
- [V] YouTube downloads are bot-blocked from the cloud; X posts still work. Plan footage from X/NBA posts.

## Oct 14, 2026 (posted-video audit, Rules Audit, voice audition, three critic passes)
Tiers: [V] verified on our files or data, [S] supported by our numbers (small n), [H] hypothesis.
- [S, n=102] **Distribution moved, not just craft.** Old-era median 29.8K vs 2.8K for the 15 Oct 5-13 posts. Same-week old-era controls and retention curves show several new Shorts held viewers as well as old winners. Don't blame every drop on the edit. (Posted Video Audit, sections 2-4.)
- [S] Avg % viewed tracks views (Spearman +0.52 new / +0.45 old); narration pace +0.50; likes don't predict views. Every 20K+ Short opened its retention curve at a ratio of 1.74 or more. Retention is close to necessary, not sufficient: LeBron's 23rd season held well and got 5.3K (a saturated topic).
- [S] Length showed no effect. Old Shorts under 18 s had the best median (32.8K). The 21 s floor was retired; length follows the story.
- [V] **#39 post-mortem (posted before any critic):** stand-in shots under "record 2" and "record 3" showed scorebugs naming other opponents; 3.8 s of a 320x240 press conference sat at the 3 s swipe spot; one line ran at 360 wpm. **Rules:** a stand-in shot never shows another opponent's scorebug; an archive shot gets 1 s, then move on; run Critic v2 before posting day, never after.
- [V] **Spoken numbers:** the voice read "810" as "eight-ten". Script braces `{810|eight hundred and ten}` show digits in captions and force the spoken form. Use them for every number that could be read two ways.
- [V] **Replays anywhere, not just neighbours:** the old QA only caught identical neighbouring shots, so three exact replays shipped (#21 ×2, #30). `qa_short.py` now warns on any overlap over 0.3 s of the same clip in different shots (except the loop and shots marked `"replay": true`).
- [V] **One-frame flashes come from the clip's own cuts** (a3's first frame, a1's cut at 1.70 s). Check frames at 30 fps around every cut, not 10 fps.
- [V] **"Wembanyama" respelling backfired:** "wem-bun-YAH-muh" was transcribed "Wembun Yama" in 9 of 9 takes; the plain spelling was heard right. Keep "Yoki-ch" for Jokic. Don't respell a name without a recogniser check.
- [V] **Voice:** only our clone reads at house pace natively (245-268 wpm); premade voices read 136-184 wpm at the same setting. Flash is the flattest and least intelligible on a phone. No migration; the owner's ear decides naturalness.
- [S] Hype framing loses to a visible number on the same player: old Flagg (hype) 4.9K vs new Flagg (height number) 20.6K.
- [V] Some old QA FAILs blocked good builds without evidence (21 s floor, 3 cuts in 3 s, b-roll/card caps, forced loop). They're warnings now. A rule needs a dated source and a result, or it is a test, not a gate (Rules Audit).

## Oct 14, 2026 (later): old videos, footage sourcing, music, voice emphasis
- [S, n=5] **The old hits' toolkit (music, colour captions, effects, fast cuts) was also in the weak old Short.** It was the house style, not the reason for the hits. What the hits had and the miss didn't:
  - a concrete question or event hook
  - the exact moment under nearly every line
  - the broadcast scorebug kept as proof and circled
  - escalation
  - an answering punch line
- [V] **Measure; don't trust AI estimates.** vidIQ guessed 160-185 wpm for old Shorts; timed transcripts measured 182-212. Our new posts already run faster (median 243). Don't push faster.
- [V] **Publicly viewable isn't free to use.** #41's "Dallas" still was an Imagn agency photo taken from a news post. Replaced with broadcast footage of the same player. Log every source; no agency photos.
- [V] **Lost downloads can be recovered.** For clips cut before logging existed, matching small grey thumbnails against each candidate post (several crops and zooms, then a 15 fps refine) found the exact post and second for 28 of 40 clips.
- [V] **A clip's own scene change becomes a one-frame flash** at the end of a shot (#41's new Dallas clip: the source cut at 10.4 s). Run scene detection on the source (`ffmpeg scdet`) and end the clip before the cut.
- [V] **Music beds generated with "sparse midrange" in the prompt** put 0-13% of their energy in the speech band; the Mixkit tracks we tried put 4-44% there. Even at -2 LU the speech recogniser lost no words in the phone simulation. So the recogniser can't set the level; convention (-20 LU) and the owner's ear do.
- [V] **One fixed music gain is wrong.** Tracks differ by 7 dB (-12 to -19 LUFS). Set the bed relative to the voice on the measured stretch that plays.
- [V] **Verify music placement by subtraction:** the music render minus the dry render leaves only the music. Read its level at the planned drop, hit and stop.
- [V] **A bass-heavy bed can push true peak over -1 dBTP after AAC** (#21: -0.9). Music renders limit at -3 dBFS.
- [V] **Our voice reads numbers flat** (number words -0.4 to +0.2 dB vs other words). "..." adds about 0.05 s of pause, and expressive settings don't lift numbers. Emphasis has to come from the edit.
- [V] **Workarounds for blocked access get refused, and should be.** Pulling YouTube preview frames through the embed player was denied. Use the owner's connected vidIQ, X, or the PC.
- [V] **A slowed quote shot drifts out of lip sync** (#38: the clip was 0.36 s short, so the editor played it at 1.094x while LeBron's real audio ran at 1.0x; his lips trailed by up to 0.29 s). QA passed it. **Rule:** a "quote" shot must play at 1.0x; re-cut the clip to cover the whole shot. `qa_short.py` now FAILs it.
- [V] **The critic caught what QA can't:** #38's premise was a retell (the quote led every Sep 28 story; our #18 used it). Polishing (music, logs) doesn't rescue a retold premise. Run Critic v2 before investing in a Short's edit.
- [V] **Search engines barely index X posts** (`site:x.com` returned none for #42's moments). Finding footage for older moments needs the owner's X links or the PC (YouTube). Park the idea rather than fake the shot.
