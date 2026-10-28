# Lessons learned (running log). Read this before making any Short.

Updated 2026-10-10 after the Studio screenshots in Downloads\New folder. The Oct 4 section below is the early read. The Oct 10 section wins where they disagree. Existing cuts are ranked in `Refinement Backlog (Oct 10, 2026).md`. Posted files stay as they are. Short 27 has an unvoiced replacement script. It is not a new render.

## The user's standards (never make them say these again)
- First 1-3 seconds must be extremely strong: real, moving, story-specific footage plus the name/number line at 0.0 s. Captions only. No headline text at the top (the user removed it again on 2026-10-04). Never set ALLOW_HOOK_TEXT.
- Sound: four different files from `Tools/sfx`, at the gains in `catalog.json`, none in the first second, none twice, none within 1.5 s, and only where the picture shows that sound. A vine boom on the open is the mistake, not the default. If a fourth effect would be a lie, ship three.
- The spoken name and the readable jersey have to be the same person. Round 4 proved the swipe: Giddey on screen during "he watched," a different player during "Spurs center," Walsh 27 during Siakam's "is not a flop," and Ingram, Dick, and Ballmer named over empty floor. Empty floor under a name is a fail. The wrong player is a fail. A still of the right player, under a second, beats the wrong player.
- A sound is legal only when the frame shows it. Swish: the ball goes through the net. Dribble: the ball is bouncing, not held in both hands. Punch: a body is hit, not a reach at a loose ball. Whistle: a whistle is at the mouth. Camera: a mic or a camera is on that person. Pop: a banner or graphic appears on that cut. Thud: someone is falling or already down, not both players still in the air.
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
- A `boom` at 0.0 s, gain -12, on every Short, plus the same whoosh and click. Round 1 measured that recipe. Round 7: the first second is voice only, and the same effect twice stops working. Sports editors whoosh a zoom and swish a made shot, then delete the ones that do not match.
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
- #03 Wemby, #12 Duren, #18 helicopter, and #22 number 6 are uploaded. Do not recut them. The Oct 4 3:20pm Studio read is in `Research Notes/Outcome Log.md`.

## What the channel has actually done (Oct 4, 3:20pm, n=4, grain of salt)
- Wemby, 0:24: 26,677 views, 80.1% stayed, average view 0:25, watch time 7.5 hours more than usual, +15 subs. Studio says the view count is inside a wide usual band (4,600–30,700), and the curve flattened after day 1. This is the retention winner, not a proven viral breakout.
- Duren, 0:33, contract: 2,407 views, 1.4K less than usual, 67.5% stayed, average view 0:22. The extra length was not watched.
- Helicopter, 0:27: 1,401 views, 7.8K less than usual, 60.1% stayed, 39.9% swiped. Studio's own line: views are lower than usual and more viewers swiped away.
- Number 6, 0:26, a few hours old: 1,886 views, about the same as usual, 67.4% stayed, average view 0:23, 419 views in the last hour. Do not judge this lane until it is a day old.
- Once a viewer stays, they give about 21–25 seconds on every one of these. The feed decides from the swipe. Feed is 90–97% of views. Search did not save the contract short.
- New target: 22–26 seconds, open on the moving unbelievable play, and treat 80% stayed as the bar that earned watch time. Under 65% stayed is the helicopter result. 67% is not a win.
- Do not lead with a contract, a salary, or a star doing something today. Those are the two videos Studio marked below usual. Referee-rule shorts are still untested on this channel, so Short 11 remains the next post. A still photo in the first second is now a known risk, because the weak Studio thumbnails were faces and the winner's was in-game.

## Open tests
Number 6 after a full day. Short 11, the first posted referee rule. Question vs number hook. Retention curves, once Studio finishes them. Read stayed-to-watch before views.

## What the Oct 10 Studio screenshots changed
Read about 10:56am on 2026-10-10 from `C:\Users\Admin\Downloads\New folder`. Screenshot `105725.png` is 5 by 5 pixels and has no data. No Reach tab is in the folder. End-screen click rate is 0.0% on every video that shows it. Hype is 0. Do not recut a posted file from this read.

The two that reached the channel's normal view band are still the Wemby vote (about 26,000 public on Oct 5, 80.1% stayed) and number 6. Number 6, six days later: 82.4% stayed, 17.6% swiped, average view duration 0:30 on a 0:26 video. That early 67.4% stayed figure was too soon. The jersey lane is a retention winner. Its new view count is not on these screenshots.

The only new short that joined them on views is How Tall Is Cooper Flagg Really, Oct 6: 19K views, 4 comments, 73.5% stayed, 26.5% swiped, average view 0:23 on a 0:22 video. The frame shows the bodies, so the height is visible.

Content-page views for the rest, same screenshot: Flopping 5.1K (Oct 8), Adams GTA 5.9K (Oct 5), Bronny's spot 5.7K (Oct 5), pay cut 2.8K (Oct 9, one day old), Vice City 2.7K (Oct 7), NBA Final 2.3K (Oct 5), Bronny got better 1.9K (Oct 6), rugby 1.7K (Oct 9), Kawhi 1.5K (Oct 8), four stars 1.5K (Oct 7). Jordan's card shows 34 views. That card has no engagement page here, so 34 is not a retention result and the cause is not in the folder.

Stay and average view, where the engagement tab was opened:
- Number 6: 82.4% stayed, 0:30 on 0:26.
- Flagg: 73.5%, 0:23 on 0:22.
- Pay cut: 71.8%, 0:24 on 0:24, 1.5K engaged, 10.2h, "about the same as usual." One day old. A salary short can hold. Duren remains the contract that did not.
- Flopping: 69.4% on the bar, 68.9% on the card, 0:23 on 0:29.
- Bronny's spot: 68.4%, 0:28 on 0:29.
- Adams: 66.2%, 0:21 on 0:23.
- Helicopter, updated from the Oct 4 read: 65.9% stayed, 0:24 on 0:27. It was 60.1% when it was hours old. Still not a winner.
- Vice City: 65.5%, 0:20 on 0:26.
- Bronny got better: 63.7%, 0:17 on 0:25.
- Four stars: 63.2%, 0:28 on 0:24. Stayers replayed it. 1.5K views. Replay did not buy distribution.
- Rugby: 54.8%, 0:19, 340 engaged, 2.0h. One day old, and the swipe is already bad.
- NBA Final: 51.5%, 0:16 on 0:23.
- Kawhi: 48.4%, 0:20 on 0:23. Worst swipe in the set.

What to do on the next short, and not on a posted file:
- Second 0 is a person, moving, and the fact is visible on that person. Number 6 shows the jerseys. Flagg shows the bodies. The NBA Final opens on a wide gym and lost half the audience. A place oddity is not the same shape as a body fact.
- 80% stayed is still the replay bar. Number 6 is now the example, at 82.4%. Under 55% stayed is the Final and the rugby short. 65% is still not a win.
- Average view duration should reach the length of the short. 0:16 and 0:17 mean the middle was not watched.
- Do not lead with a pick count, a wide building, or "a star trained today." A salary hook is still not the next test. The pay cut held for one day and has not earned a second salary short.
- A face on the content card did not, by itself, decide the result. Flopping's card is a face and it stayed near 69%. Do not recut a thumbnail from that theory.
- Music stays off until one future short tests it. The retention winners have no music bed in this log. Adding music to every short would change every variable at once.
- Voice stays on the existing check: script match, pronunciations, no doubled words, about -14 LUFS. These screenshots do not show a new voice defect.
- Post two in a day only when the second is a different visible-fact story. These screenshots have no clock time, so no new best hour. Do not add a third.
- Before a file is called postable: play it once, confirm second 0, the name on the jersey, each sound, no top headline, the payoff is the last line, and `qa_short.py` prints PASS.

## Research gate (Oct 10)

The full note is `Research Notes/Round 9 - Topic Selection (Oct 10, 2026).md`. The writing and production gate is `Research Notes/Creation Process (Oct 10, 2026).md`. A copy-check that prints FRESH is not a yes. On Oct 10 the exact title "Why No One Shoots Underhand" came back empty while Coach Clank's Short of that title had 10,917,660 views.

Before a script is saved into `Productions`: name the moving clip for second 0, make the last line pay the first eight words with a fact, delete any sentence that does not add one, stay out of the last seven days' family, and lock every fact to a page opened that day. The posted number 6 cut ends on a consequence. The older script in that folder ends on a question. Use the posted ending. The next package is `Research Notes/Next Short - He Signed The Wrong Number.md`. Do not voice it before Oct 12, and do not voice it at all if the autograph clip's 12 is unreadable. Not another referee short until Bad Boys has a stayed% read.

## Cloud copy (merged Oct 14)

The section below is the cloud session's lessons log. It is kept after the PC log. Where they disagree, check the dated source, not the order.

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
- [V] **Measure; don't trust AI estimates.** vidIQ guessed 160-185 wpm for old Shorts; caption timings said 182-212 (n=3); the old Shorts' own voice recordings measured **206-252, median 220** (n=12, the most accurate; corrected Oct 14 night). Our posts ran 243 median and the old production voice 259-267 on our scripts: too fast. The house voice now reads 220-230.
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

### Oct 14, 2026 (night): winning formula and voice overhaul
- [V] **The old voice was a copy of a copy.** The clone was trained on our old Shorts' narration, which was itself TTS, with a high noise floor (-20 to -23 dB in the pauses). A clone can't sound cleaner than its source.
- [V] **Light denoise on clean TTS removes the consonants.** On #40 it cut about two thirds of the energy above 5 kHz (the s/t/f detail) and only "improved" HNR by removing it. HNR is a poor proxy for naturalness. TTS now gets no denoise.
- [V] **Speed settings creep.** "Auto" speed 1.15-1.2 plus a stretch put the clone at 259-267 wpm, above every old hit (206-252). At 1.15 one take's pitch variety fell to 3.8 semitones. Check wpm on every take; don't stretch.
- [V] **A new voice changes the footage plan.** At 220 wpm the same script runs 2-6 s longer. #21 went 16.8 → 23.0 s and needed 3 longer clips and 2 split shots. Re-anchor shots, retime music (`retime.py`), and check for held frames.
- [V] **A more dynamic voice renders quieter.** Its peaks hit the limiter (#21: -15.6 LUFS). A gentle compressor before the loudness lift fixed it (-14.9).
- [V] **Library voices can add long pauses** (Alex: 0.8-1.25 s after some sentences). Cap silences only (`max_pause` 0.38 s), never cut speech.
- [V] **The speech recogniser can't judge Y vs J** ("Jokic" plain or "Yokitch" both come back "Jokic"). Respellings are an ear decision; a respelling that comes back as the real name ("Yokitch" → "Jokic") beats one that doesn't ("Yoki-ch" → "Yokeech").
- [V] **A word-error difference can be spelling, not hearing.** T2's 8.1% vs 2.7% was "pre-season" vs "preseason"; both transcripts had every word. Read the transcript before trusting a WER.
- [V] **Using a library voice through the API adds it to "My Voices"**, which also gives us its notice period if the owner withdraws it (Alex 90 days, Jon and Lucan 730).
- [V] **Creator data beats creator anecdotes.** CoachClank's 20-62 s Shorts beat their under-20 s ones 2.8× on median views (n=145), in both halves of their history. Our own new posts are all 21-29 s, so length isn't what separates our winners from our losers.
- [V] **TikTok profile pages and YouTube both refuse this server for listing or watching videos** (Oct 14). Known video URLs still play through the browser. Ask the owner for links rather than working around a block.
- [S] **The difference between our old hits and new posts is the storytelling, not the voice.** Same voice (0.93-0.95); the old scripts had flowing sentences, a turn and a reframe. Story voice is now house style.

### Oct 14, 2026 (late night): new stats, a strict script critic, voice round 4
- [V] **Our scoring rubric ran backwards twice.** Round 3 (Oct 5) and Creative System v3: #40 scored 63 (top) and got 655 views; #39 scored 46 and got 4.0K. A rubric that scores craft can't see a weak premise. Script Critic v3 scores the premise first and may reject.
- [S] **Technicalities flop.** The bottom 6 new-era posts were rule or bookkeeping technicalities, niche players or retells (38 to 1.6K). The top 4 had a famous subject and a fact you'd retell, three with the subject's own words or family (9.8K-31K). n=22, correlation only.
- [V] **A hook that oversells loses the viewer.** #41 "taller than Wembanyama" delivered an unknown G Leaguer: 1.6K views.
- [V] **Check clone training data.** "pham v2" was trained on the same recording 3 times at different lengths. De-duplicating it and making a new instant clone gave a *flatter* voice (pitch variety 3.7 vs 4.7). The limit is the 5 minutes of old TTS source, not the settings.
- [V] **The same voice can go flat on one take** (F: 4.66 then 3.81 semitones). `voice_take.py` now gates on pitch variety per voice.
- [V] **One-frame flashes hide in source clips** (washed-out single frames in b7L, a1, c_34, e1bg, k2bg). qa_short can't see them. `Tools/deflash.py` finds and replaces them; run it on every new clip.
- [V] **A slower, natural read needs about 25% more footage.** Plan 1 clip per line, and split long lines before rendering.
- [V] **Metricool shows channel-level daily views, but its per-video sync can lag days after a reconnect.** Don't promise per-video retention from it.

### Oct 15, 2026: the YouTube Studio export (audit §13)
- [V] **"Stayed to watch (%)" is the number that tracks views:** Spearman +0.77, n=20 new-era Shorts. Every Short at 73%+ got 4.0K-31.8K; every Short under 60% got 1.4K-4.8K. Read it first at 48 h. Target 70%+.
- [S] **High-stay first lines make one absolute, curious claim about a famous name**, in one sentence ("Only two NBA players…", "Every Defensive Player of the Year…", "never… until LeBron and Bronny"). Low-stay first lines open with a number, a stat line, a penalty list, or a player casual fans don't know. Correlation: the topic drives both.
- [V] **Length in 22-33 s doesn't predict views** (-0.05). Stop trimming for its own sake.
- [V] **Views arrive in week 1, then stop** (#22: 17,206, then 9). The 7-day read is the result; there is no long tail to wait for.
- [V] **Our own ready script failed the new hook anchor.** #21 v5 put the surprise in sentence 2 (about 4.8 s). Run the hook check on every script, ready ones included.
- [V] **The export is a window, not lifetime.** Old-era Shorts show single-digit window views; compare them on lifetime numbers only.

### Oct 15, 2026 (later): competitor scripts, QA and the build
- [S] **Same topic, different script:** CoachClank's "Why no one shoots underhand" (10.9M, 25x their norm) opened on a scene, asked the viewer's question out loud at 6 s, used 1 number and ended on Shaq's reason. Our #29 (1.4K) opened on a niche player's stat and used 8 numbers.
- [S] **CoachClank's top scripts end on a person** (a reaction or the subject's own words): 5 of 9, vs 1 of 5 at their median. A turn word ("But") is common at every level: table stakes.
- [V] **YouTube captions can be read legitimately** through a search provider's page fetch (`youtube.com/shorts/<id>`), even though downloads are blocked here. Coverage is partial: 26 of 32 tried.
- [V] **A pixel-only "is this upscaled?" test doesn't work on our compressed clips.** Take the blow-up factor from the logged source size instead.
- [V] **Caption width:** cards like "TWENTY-SEVENTH GAME" ran 867 px and touched the Shorts button column. Measure with the real font (libass draws about 0.745 of PIL's em width); auto-fit now.
- [V] **Speech-to-text formatting causes false REDOs** ("$8 million" for "eight million dollars", "won 98" for "one ninety-eight"). Check the word's energy before re-voicing; the checkers now handle both.
- [V] **A source's own cut a frame or two into a clip flashes the previous scene.** `footage_qc.py` lists internal cuts; start the cut 0.1-0.15 s later.
- [S] **When the key moment was never filmed** (#44's bag-carrying), put the reporter's exact words on screen as a quote card with attribution, and keep footage of the subject from the same trip. Don't stage a stand-in.
- [V] **Ask what's posted before revising.** #21 v6 was built after the owner had already posted #21. Check the channel or ask first.

### Oct 15, 2026 (overnight, on the PC): voice test #42 and the #36 footage check
- [V] **A sharpness number cannot rank two different sources.** Laplacian variance said the Cobwebs clip (interlaced, combing, pink cast) was *sharper* than the official NBA clip, because combing, noise and compression blocks add fake edge energy. A first comparison also mixed a downscale with an upscale. Side-by-side crops at the same magnification showed the opposite: use the number only to compare shots inside one Short, and look at the pixels for anything else.
- [V] **A REDO on the last word can be a tail artifact.** `voice_check` flagged Alex's final "times." at 0.87 s (alignment), but the raw envelope showed a 0.25 s word, a faint tail near -45 dBFS, then silence. Check the envelope before regenerating, and trim the tail in the render.
- [V] **`voice_check`'s wpm counts a digit group as one word.** "15,541" is one token, so #42 showed 163 and 169 wpm; counted on the 81 spoken words it is 210 and 217. Use the spoken-word count when a script has `{15,541|...}` braces.
- [V] **Takes to pass the voice gate, three A/F pairs (#21, #36, #42):** Alex 3, 2, and not passed on its one take; pham v2 1, 2, 1. At about 476 characters a take and 2,596 characters left until Nov 8, a first-take pass is worth real money. Small sample.
- [V] **`voice_check`'s verdict word moves between runs.** #36 `_v2` is stored as PASS with "he" dropped; the same file re-run today heard "He" and gave a false REDO ("One LeBron" heard as "won LeBron", which the "won 98" fix only handles before a digit). Read the mismatch list, not the verdict.
- [V] **ElevenLabs' "characters used" counter lags a take or two.** It read the old number right after the first take and one take behind after the second; re-check after about 20 seconds before concluding anything about spend.
- [V] **On the PC the voice tools need `py -3`**: plain `python` is 3.12 without `faster-whisper`, `scipy` or `parselmouth`, and `voice_take.py` imports `parselmouth` before it does anything (it failed before any paid call). Rehearse the whole measurement chain on a copy of an existing voice before a paid take.
- [V] **Letterbox bars are not always symmetric.** The NBA archive video is a 4:3 picture inside 1280x720, with the picture at x=167-1120 and a dark fade on both edges. Run `cropdetect` and check the edge columns of the cut clips (`left6` should not be 0).

### Oct 19, 2026 (cloud): #52 and #53
- [V] **A push-in on a 720p shot can cross the blow-up limit.** #53's first shot at crop zoom 1.1 plus `"zoom": 0.08` measured 3.17x and failed QA; crop zoom 1.0 plus the same push is 2.88x. Count the push in the blow-up.
- [V] **Broadcast lower thirds can name real people.** #53's "miss his next shot" clip carried the game's three referees by name; under a betting line that reads as an accusation. Blur the strip (`boxblur` on that band) or pick another clip, and look at the bottom 15% of every broadcast frame.
- [V] **On a betting story, keep identifiable bystanders off the betting lines.** Wide shots with unreadable numbers for the generic rule lines; the named subject only on the lines about him; say in `notes.md` when a shot is the subject in a different game.
- [V] **Documentary sources hide cuts from `scene` detection.** ffmpeg's `select=gt(scene,0.25)` found nothing, but `qa_short` flagged a cut 0.07-0.1 s in; frame-by-frame sheets showed a hard cut between two similar shots. Trust the QA flag and move the in-point.
- [V] **Re-timing sound effects to a second voice can break the 1.5 s spacing.** #52's Alex render moved the riser to 1.38 s before the pop; nudge the effects onto the overlay times again and re-check the spacing.

### Oct 20, 2026 (cloud): first WNBA Shorts (#59, #60)
- [V] **WNBA video on wnba.com and the NBA content API is a protected stream (no MP4 files).** Use official/news posts on X instead (WNBA, team accounts, NBA, NY Post); `x_clip.py` gets 720p-1080p.
- [V] **Many short shots drift in the ffmpeg engine.** Each shot rounded up to a whole frame; 15 shots put the picture 0.11 s past the voice (QA FIX). `assemble.py` now snaps shot edges to the 30 fps grid.
- [V] **Highlight reels hide dissolves.** A close-up in the WNBA reel dissolved into the next play 0.65 s in; a frame-difference check missed it. Look at the last frames of every reel cut, not only the first.
- [V] **A team's own reel can carry a burned-in stat graphic.** The Aces' Wilson reel had a full-height stat column; crop the clear side (608x1080 at x=472) rather than show conflicting numbers under ours.
- [S] **Overlays at y=1340 collide with the caption band.** Use y 300-330 above, or y 1480+ below the captions.


### Oct 21, 2026 (cloud): second QA of all drafts (#52, #59-#65)
- [V] **A viral moment's open lane can close in under 12 hours.** #65 (LeBron vs a Knicks fan) was FRESH at build time on Oct 21 morning; by 16:00 UTC Chaz NBA had 546K views on the clip with LeBron's real audio. Re-run `copy_check.py` on the morning of posting, not only at build.
- [V] **"Tonight" in a script ages before it posts.** #62 was voiced on game night ("Tonight, the Garden chanted"); posting the next day would be wrong. Write time-free wording ("On opening night") unless it will go up within hours.
- [V] **Check footage across Shorts, not only within one.** #63 and #64 used the same Wemby bench close-up (the same post, same in-point); QA only checks inside a Short. Compare `sources.csv` in/out points between Shorts from the same game.
- [V] **`broll.py cut` rewrites the source-log row for that clip name.** Re-cutting an existing clip (S10) replaced its verified row with a bare unverified one and QA failed ("clips missing" / "not verified"). After a re-cut, re-check `sources.csv`, or cut to a new clip name.
- [V] **The ending can show the payoff instead of looping.** #64's "with one basket" ran over a miss (the loop shot); the line's own image (his only basket, ESPN clip) is the stronger end. QA's loop check is only a warning.
- [V] **ESPN's game-summary clips include tight face close-ups.** "Victor Wembanyama invites Chet Holmgren to a block party" had a clean 1.3 s front-on close-up, better than any X post for frame 1.
- [V] **The name FIX in export speech-to-text clears with a names hint.** faster-whisper small.en heard "Kendrick"/"the Aaron"; with `initial_prompt` listing the players it heard "Kenrich"/"De'Aaron". Use that to tell a mispronounced voice from a mis-heard name.
- [V] **Two effects 1.05 s apart: the renderer silently drops the second.** #62's UPLOAD listed a camera click that never played. Read assemble's "sound effect skipped" lines and keep the sheet honest.

## Oct 21, 2026: Ahmed's network study and the soccer channel (two story Shorts built)
- **[V] Ahmed's network** (Goal 424K subs, Basketball 121K, Business 86.6K; 1.32B views) runs one format on three niches: a 60-80 s story, the title read as line 1, a turn every 8-12 s, a payoff number, centred TikTok Sans captions and a quiet bed. Full study: `Research Notes/Story Format Study - Ahmed (Oct 21, 2026).md`.
- **[V] For NBA:**
  - money and contract stories are their weakest Basketball theme too (93K vs 159K median);
  - 3 a day lowered their medians;
  - their first picture holds about 2.5 s.
  The Playbook has the evidence-tiered list (section "Oct 21, 2026"). THE #42 FORMAT stays first.
- **[V] Dates in a script need the source's own timeline.** "The night before the derby" was wrong: the fire was at 1 a.m. on the day before. Caught before rendering.
- **[V] When sources disagree on who did what** (FIFA vs Reuters on who wrote Lehmann's note), write the line so it is true under both versions.
- **[V] White captions on light cards are unreadable.** Keep graphics above y=890 when the captions are centred at y=960.
- **[V] Story-format QA profile:** `qa_short.py` uses 58-88 s and allows archive blow-up up to 6x (as a warning) for folders under `Soccer Channel/`. The NBA rules are unchanged.
- **Soccer channel memory** lives in `Soccer Channel/` (START HERE, Playbook, Lessons Learned, Idea Bank, Outcome Log). The skill is `/story-short`.

## Oct 26, 2026: why the NBA views dropped (owner: "i think its editing and bad retention rules")
- **[V] It's us, not the niche.** Old era median 29K; new era 3.9K. Over the same months Ahmed's Basketball fell about 40%, not 90%, and our own new-era hits (#22, #03, #58, #48, #19) still got 21-32K. Full write-up: `Research Notes/Why NBA Views Dropped (Oct 26, 2026).md`.
- **[V] The gate is "stayed to watch",** and only 13 of 40 new-era Shorts reached 74%.
- **[V] Our own editing rules lined up with the misses** (37 posted Shorts with edit files):
  - 3+ shots in the first 3 s: 67.5% stayed vs 75.0% for 2 or fewer.
  - Any card: 66.1% vs 72.6% without.
  - A card in the first 4 s: 63.2% vs 72.0%.
  - 16+ shots: 66.4% vs 75.0% for 15 or fewer.
  - Pace, word count and how many numbers are spoken showed no link.
- **Changed:**
  - QA, NBA profile: more than 2 shots in the first 3 s warns; a card in the first 4 s FAILS; card share over 10% warns; shots may run up to 6 s; the 6-clip and 35%-per-clip gates are warnings.
  - `cloud-short` SKILL: the "OCT 26 EDITING RULES" box at the top.
- **Lesson about rules:** several of these came from competitor averages or n=1, and became FAIL gates without our own data. A rule becomes a gate only after our own numbers back it.

## Oct 26, 2026: Swishyyy (@swishyhoopz), the owner's pick
- **[V]** 203 Shorts, 21.3K subs, median 41K.
- **[V] Moments you can watch beat explainers.** Moments: median 48K overall and 78K in the newest 101, with all 18 of the 1M+ hits. Explainers, history and stats: 36K and 44K, with zero 1M+.
- **[V]** Their weakest Shorts are history and stat narratives, which is our new-era lane. Several of their topics are the same as our old-era hits.
- **Changed:** both skills now put "one moment you can watch" first (about 2 in 3 NBA Shorts). Write-up: `Research Notes/Channel Study - Swishyyy (Oct 26, 2026).md`.

## Oct 27, 2026: Gemini watch study, hits vs misses on the same channel ([S], n about 10 per group per channel)
- **[S] The editing basics don't separate hits from misses.** On Swishyyy, Hoopiverse and Ahmed's Goal, top and bottom Shorts had the same opening: 2 shots in the first 3 s, about 3 in the first 5 s, the subject on screen in second 1, no cards (NBA) and a line 1 of about 11 words. They are the entry ticket.
- **[S] The subject separates them.**
  - **NBA hits:** spectacle, kids, family, size and the biggest legends.
  - **NBA misses:** history and trivia explainers, and fan-only personality bits about current role players.
  - **Soccer hits (Ahmed's Goal):** megastars in a current controversy.
  - **Soccer misses:** "Players who..." lists of lesser names.
- **Changed:** the daily-run research step now applies a "stranger test" when it picks a story. Write-up: `Research Notes/Watch Study/Findings (Oct 27, 2026).md`.

## Oct 27, 2026 (evening): formats and scripts, about 180 Shorts ([S])
- **[S] News takes lose on every narrated channel:** "Is X about to...?", "are they doomed?" and injury or money questions. So do sentimental fan moments.
- **[S] Lists with a clever frame win on the explainer channels.** Rebound Rewind: 7 of 10 hits are lists, 0 of 10 misses.
- **[S] Scripts:**
  - In NBA hits, line 1 is a bold claim or the scene: a number in 11% vs 23% of misses, a question in 15% vs 21%.
  - Hits end on a twist or a punchline: 64% vs 52%.
  - No hit asks for a follow.
- **[S] Length doesn't differ within a channel.** Correction: the Oct 27 afternoon remark that "hit scripts are shorter" came from mixing channels.
- **Changed:** the daily-run research step (news takes out, lists with a frame in, the script rules). Write-up: `Research Notes/Watch Study/Formats and Scripts (Oct 27, 2026).md`.

## Oct 28, 2026: owner direction, repurpose proven topics
- **Owner:** "that is a known formula that works, repurposing already winning topics into your own formula."
- **Standing method:**
  - Take a topic that already won big on a competitor (the Script Library, the watch studies).
  - Find our own angle and payoff, and write our own script from sources.
  - Build it with official or original footage. Never retell their exact story or reuse their footage.
- **First two:** #74 underhand free throws (Wilt) and S15 Coutinho 8-2.
- Skip topics that are other creators' content (TikTok challenges): that footage isn't ours to use.

## Oct 28, 2026: footage and tooling
- [V] Champions League goal clips from beIN Sports, ESPN and TRT on X return HTTP 403 on download (protected media). Don't work around it.
  - CBS Sports Golazo posts (the US rights holder) and highlight reposts did download.
- [V] A dark broadcast close-up (a manager in a black jacket on a dark bench) fails qa_short's "frame 1 is lit".
  - Photos made into push-in clips work well as frame 1 when the background isn't darkened (Tools: the S16 `src/still_*.mp4` recipe).
- [V] A still photo shown twice in a row, or two near-static wide shots from one clip, fail "same footage". Cut to a close-up of the same person instead.
- [H] An evergreen story is stronger when the subject's own words contradict each other on camera (#76 Pierce, 2019 vs 2026) than when a rumour is told as fact.
