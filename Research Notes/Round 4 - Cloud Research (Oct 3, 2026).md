# Round 4: what makes Shorts get watched, and 10 new ideas (Oct 3, 2026)

*Done in the cloud session. Numbers are public view counts pulled with yt-dlp on Oct 3, 2026 (CoachClank's last 150 Shorts, REBOUND 59, Ahmed's Basketball 60, Courtside Films 60, plus your own 80). Medians, so one freak hit can't skew them. Web sources are linked at the end.*

## The 6 findings that change what we make

1. **Rules, bans and "caught" stories are the strongest topic by far.** On REBOUND (median 775K), the 13 Shorts about rules, bans, cheating or referees have a median of **7.7M**, a 10x lift ("NBA Players CAUGHT CHEATING" 42M, "3 NBA Rules You Didn't Know Exist" 36M, "3 WEIRDEST Bans In NBA History" 12M). On CoachClank rule/ref Shorts run 617K vs 448K overall. Our #11 (Jordan push-off vs the new rule) is in this lane. Contracts and trades are not: Ahmed's contract/trade Shorts sit at 105K vs 93K overall, flat. **Treat #12 Duren and #13 Kawhi as the weak lane and expect them to land near the channel median.**
2. **CoachClank's top 25 are spectacles, not news.** Top: "6'8 vs 7'9" 30M (15 s long), "He Didn't Have To Do That" 21M, "He Was Playing By Himself" 21M, "The Battle for the World's Highest Basketball Shot" 14M, "NBA Rookie Pranks" 12M, "200 IQ LaMelo" 11M. None is a contract or trade story. The pattern: one human oddity you understand in 1 second (a size gap, a prank, a trick, a rule that sounds fake).
3. **Titles: 5-7 words win** (554K median vs 225K for 8+ and 242K for 4 or fewer). Emoji help (553K vs 282K). **The 🤔 emoji is the worst performer in this sample (78K, n=5). 💀 and 😳 are the best (7.7M with 9 uses, driven by outliers; 609K).** Starting with Why/How/What/Did/Is gets 792K vs 419K. Question marks were mixed (276K vs 480K here, 847K vs 480K across 432 Shorts earlier), so keep testing, but stop ending titles in 🤔.
4. **Your own best Shorts match this.** Top 12 of your 80: all 16-29 s, all rule/oddity/"why" topics (underhand free throws 73K, "Is it possible to dunk without jumping" 56K, Luka "200 IQ" 54K, airless basketball 44K). Your worst were AI memes and fights.
5. **The algorithm now judges one thing first: did they stay or swipe.** Benchmarks across sources: 70-90% "Viewed" is the best range, under 60% rarely gets pushed; under 25-30% swipe-away in the first 3 s is the target; roughly 65% average retention for Shorts under 30 s. Rewatches count (above 100% is a strong signal), so a loopable ending matters. Paddy Galloway's study of 3.3B Shorts views found the same VVSA bands.
6. **Policy risk to watch:** YouTube's "inauthentic content" rule (since July 15, 2025) demonetises mass-produced, repetitive, template-style videos. AI narration alone is allowed. Our protection is real value per Short: our own research, our own opinion line, verified numbers, transformed clips. Don't let every Short become the same template; vary structure (rule explainer, list, scene, size gap).

## What I implemented and tested today

| Change | Why | Status |
|---|---|---|
| Number or question in the first 3 words, new image about every second until 5 s, slow punch-in on shot 1 | first-3-seconds data above | in every Short since LeBron v5; skill updated |
| **Audio fix:** voice lifted to -14 LUFS first, effects mixed under it | effects were louder than a quiet voice (the vine-boom complaint, the Jordan chat's audio bug) | fixed in `assemble.py`; all finals re-rendered |
| Boom removed, 2-5 effects only, each tied to something on screen | complaints + niche norm | done |
| **Hook headline** (`--hook-text "10 PICKS\|FOR KAWHI?"`, or `hook.txt`) | curiosity-gap text in the first 0.3-0.8 s is the most-cited scroll stopper | built and tested on Kawhi (`final_hooktext.mp4`); needs an A/B vs the plain cut |
| **Auto push-in** (`--auto-zoom 0.06`) on every footage shot | nothing should sit still for more than ~1.5 s | built and tested on Kawhi |
| Music under the voice (`--music`), ducked, -21 dB, whole mix at -14 LUFS | you asked for a music test | built; commercial tracks may be claimed by Content ID |
| Evidence cards (red box timed to the word) larger and above the caption band | readability on a phone | `Tools/card.py` |
| Free "second pair of eyes" for clip timing: `Tools/yt_sheet.py` (YouTube preview frames) | vidIQ credits are gone | done |

## What to test next (one variable at a time, 3 repeats each)

| Test | A | B | Read at 24 h |
|---|---|---|---|
| Hook wording | number first ("92% pay cut...") | question first ("Did LeBron...") | Viewed vs Swiped Away |
| Hook headline | plain cut | headline over first 2 s | Viewed vs Swiped Away |
| Music | none | quiet music under voice | average % viewed |
| Captions | ALL CAPS red/green (house style) | CoachClank white sentence case | average % viewed |
| Topic lane | rule/oddity | contract/trade | views at 48 h |
| Length | 22-28 s | 30-40 s | average % viewed and views |

## Visual upgrades still to try (not built yet)
- **Loop ending:** last frame matches the first frame (same shot or same motion) so the Short replays. Cheap to do on rule/oddity Shorts.
- **Mid-video re-hook text** around 40-50% ("But here's the part nobody mentions"), shown as 1-line overlay.
- **Cut on the beat** when music is used; switch the music energy once mid-video.
- **Real action first:** the hook shot should be motion or a face, never a card. Cards come after 4 s.
- **Fewer talking-head-style stills:** avoid shots that repeat (Duren v1 repeated the same clips and cards; v2 fixed it).

## Mistakes to not repeat (from today)
- Contract and trade topics are the lowest-ceiling lane. Use them only when there is a rule, a number gap or a funny detail to hang a hook on.
- Voiced scripts need every sentence sourced. A chat's first Duren v2 draft contained three unsourced details (monthly weigh-ins, "9 points vs Orlando", "90 minutes before the deadline"); they were removed before voicing.
- A quiet raw voice (about -27 LUFS) made every effect too loud. Always lift the voice first.
- Never send an API key between chats. Keys go in the cloud environment's settings only (and the one pasted in chat should be rotated).
- Asset links opened outside the app show "not found"; downloads must use the in-app Download button or the file sent in chat.

## 10 ideas (ranked by lane strength; "verified" = checked against 2+ sources today, copy-check = nobody big has told it)

1. **The NBA's new "straight-line pathway" rule** (rule lane). Title: *The New NBA Rule Nobody Explained 😳*. Hook: "The NBA just said you're allowed to bump a player, but only if he's doing one thing." Facts (ESPN, Sept 29-30): offensive and defensive players both have the right to stay on a direct path to the basket; both can be called for a foul if they go out of their way to bump the other off that path; part of four points of emphasis with push-offs, screens and off-ball contact. Footage: NBA's points-of-education video on X (id 2104962344031772863). Verified, copy-check FRESH.
2. **Steven Adams: "GTA VI will make the whole league plummet in November"** (funny + dated stakes). Title: *NBA Player Says GTA 6 Will Ruin November 😭*. Facts: Rockets media day; GTA VI releases Nov 19; Adams: league-wide performance, coaching and scouts "horrendous, just for November", back up in December (Newsweek, Bleacher Report, Yahoo, ClutchPoints). Footage: Rockets or NBA clip on X. Verified, copy-check FRESH.
3. **Josh Hart roasts Brunson's SNL** (funny, Knicks champions). Title: *Josh Hart Destroyed Brunson's SNL 😭*. Facts: Brunson was the first Knick to host SNL (season 52 premiere); Knicks teammates in the monologue; Hart at media day: "I think his performance was fine. I don't think he has a future in acting." (ESPN, NBA.com, Yahoo). Footage: Knicks/NBA X posts. Verified, copy-check FRESH.
4. **Giannis and Bam do the Dragon Ball "fusion"** (funny, 12-18 s quick moment). Title: *Giannis Just Fused With Bam 💀*. Facts: Heat media day Sept 28; compared themselves to Goku and Vegeta; Giannis: Bam is "one of the best two-way players in the league. He never takes days off." (NBA.com Starting 5, The Source). Footage: Complex / Fanatics posts on X. Verified, copy-check not run yet.
5. **Cooper Flagg fails the "stop the timer at 1.00" challenge** (funny, quick moment). Title: *Cooper Flagg Lost To A Timer 😭*. Facts: Mavericks media day Sept 25; Flagg tried to stop a timer at exactly one second while Naji Marshall cut a banana, and it didn't go as planned (ESPN media day recap). Single-source detail: confirm on the clip before voicing. Copy-check FRESH.
6. **7'4 vs 5'7: the NBA's biggest height gap** (size lane, the 30M "6'8 vs 7'9" pattern). Title: *The Biggest Height Gap In The NBA 💀*. Facts to confirm first: Wembanyama listed 7'4 by the Spurs roster, 7'5 in the NBA bio (SI); Yuki Kawamura 5'7 is the shortest player entering 2026-27 (LiveScore), but sources disagree on his team (Chicago vs Memphis) and on whether they share a court this season. **Needs checking before scripting.**
7. **Giannis and Kawhi both debut tonight (Heat vs Raptors, Quebec City, Oct 3, 7 PM ET)** (time-sensitive). Title: *Giannis vs Kawhi: Who Debuted Better? 😳*. Make it only after the box score (check tomorrow morning for one real moment: a dunk, a stat line, a crowd reaction). Source for the game: NBA.com Starting 5 (Oct 2).
8. **"53 Years for One Banner" (already scripted as #10 in Batch 2)** is the best-timed Short for opening night, Oct 20: the Knicks open the season as champions for the first time in over 50 years. Keep it for Oct 18-20; make it a rule/oddity hook ("the longest title drought in NY sports history, ended") only if the claim is verified.
9. **LeBron is Maxey's workout partner** (funny, uses the Sixers audience). Title: *Maxey Flipped LeBron's Workout Joke 😭*. Facts: at media day Maxey joked he is not LeBron's workout partner; LeBron is his workout partner (NBA.com Starting 5); LeBron cited Maxey as a key factor in signing (ESPN video). Verified from the NBA.com recap; get the clip.
10. **Jimmy Butler's media-day looks through the years** (funny, photo-driven). Title: *Jimmy Butler's Media Day Hair Is Insane 💀*. Facts: ESPN published a gallery "From 'emo Jimmy' to ombre faux locs: Jimmy Butler's media day looks through the years" and highlighted his earrings this year. Needs licensed/official images; use only official team or NBA posts. Lowest priority.

## Sources
- [YouTube Shorts algorithm 2026 (vidIQ)](https://vidiq.com/blog/post/youtube-shorts-algorithm/) · [Shorts Retention Curve Playbook](https://aibrify.com/blog/youtube-shorts-retention-curve-playbook) · [Paddy Galloway, 3.3 billion views study](https://x.com/PaddyG96/status/1646898356419981315) · [Hook formulas (OpusClip)](https://www.opus.pro/blog/youtube-shorts-hook-formulas)
- [YouTube inauthentic content policy explained](https://newmoneymatrix.org/youtube-inauthentic-content-policy-explained/) · [AI voice policy 2026](https://narrationbox.com/blog/youtube-ai-voice-policy-explained-clearly)
- [ESPN: NBA push-off crackdown and points of emphasis](https://espn.com/nba/story/_/id/50063714/nba-issues-new-guidelines-instructs-refs-crack-push-offs) · [Rockets' Steven Adams on GTA VI (Newsweek)](https://www.newsweek.com/sports/nba/rockets-steven-adams-goes-viral-for-hilarious-gta-vi-comment-12478491) · [Josh Hart on Brunson's SNL (Yahoo)](https://sports.yahoo.com/articles/josh-hart-gives-hilarious-honest-143000754.html) · [NBA.com Starting 5, media day](https://www.nba.com/news/starting-5-september-29-2026) · [NBA.com Starting 5, preseason](https://www.nba.com/news/starting-5-october-2-2026) · [ESPN media day recap](https://www.espn.com/nba/story/_/id/50023689/nba-2026-media-day-sights-sounds-highlights)
- Channel numbers: yt-dlp public listings of @CoachClank, @rebound, @AhmedsBasketball, @CourtsideFilms (Oct 3, 2026).
