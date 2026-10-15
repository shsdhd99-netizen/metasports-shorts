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
