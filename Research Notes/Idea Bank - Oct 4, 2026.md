# Idea Bank - Oct 4, 2026

*Researcher output, no uploads, no commits. 35 ideas (25 fresh-news, 10 refreshed old hits) ranked by score, with a formats-and-evidence table first. Machine-readable twin: `Research Notes/idea_bank.json`. Today is Oct 4, 2026; the 2026-27 preseason started Oct 3; opening night is Oct 20.*

## 0. How this was measured, and what could not be

- **View counts are real public YouTube numbers** pulled with `yt-dlp` on Oct 4, 2026: Shorts tabs of @NBA, @espn, @BleacherReport, @HouseofHighlights, @overtime, @AhmedsBasketball, @CourtsideFilms (first 120 each), per-Short dates for each channel's top Shorts, plus the Round 5 full metadata files for Coach Clank (148 Shorts since Oct 4 2025), Hoop Facts (100), Hoops Lore (66), Ahmed's (100), Courtside (77). REBOUND (@rebound) returned 59 Shorts but they are dated 2022-23 (not the last 12 months), so they are used for format evidence only and are labelled 'older'.
- **Not measured:** TikTok and Instagram Reels (yt-dlp is blocked or rate limited; vidIQ has 4 credits and a call costs 5). Anything said about TikTok/Reels below is a hypothesis. @HoopFacts / @HoopsLore have no Shorts tab at those handles; their numbers come from the Round 5 files.
- **Recent Shorts are still accumulating views.** Anything posted in the last two weeks (the news-reaction examples) will keep rising; the older ones are final.
- **Footage:** YouTube downloads are blocked here, so YouTube is preview-frame only (`Tools/yt_sheet.py`). X is login-walled from this machine: I name the official accounts and the specific posts I could see quoted in articles, but did not open post pages, so run `Tools/x_clip.py` to find the exact post. archive.org identifiers below were all returned by the archive.org search API today (they exist), but they are broadcasts owned by the NBA or TV networks, not public domain: use short, transformed clips.
- **Evidence labels:** PROVEN = number pulled today; SUPPORTED = several sources; HYPOTHESIS = my reading. Facts marked VERIFY were not confirmed today and must be checked before voicing.

## 1. What the data says before the formats

1. **The big official accounts are a poor benchmark and a poor thing to copy.** Median Short in the latest ~120 uploads: @NBA (24.5M subs) 31.5K, @espn (14.6M) 12K, @HouseofHighlights (17.7M) 29.5K, @overtime (4.0M) 23K, @BleacherReport (5.05M) 77K. Their hits are one-off moments (HoH 'SGA COOKED Jared McCain in a race' 1.70M, Sep 30; NBA 'AJ Dybantsa light-up kicks' 956K, Sep 28). **Reposting news clips is a speed game we cannot win; explanation and concept is where small channels win.**
2. **Concept channels have medians 5-15x higher:** Coach Clank median 511K (first 48 Shorts, Jun-Aug 2026) and 421K over 145 (Round 5); Courtside Films 267K; Ahmed's 78K at only 121K subs.
3. **Rule / ban / 'caught' / ref titles are the best-evidenced topic** (2.49x relative views, n=26, Round 5), confirmed again below in the last 12 months: Coach Clank 'This Referee Mistake Confused Everyone' 7.2M, 'The Unwritten Triple Double Rule' 6.45M, 'Banned Jersey Number' 3.7M.
4. **Variance inside a format is huge**: 'The NBA's Unwritten Rule' got 610K while 'The Unwritten Triple Double Rule' got 6.45M. The *specific, visual* version wins; the vague version does not.

## 2. Formats table, with evidence

Views are public counts on Oct 4, 2026. Date is the upload date. 'older' means the sample is 2022-23.

| # | Format | Examples with views (Oct 4 2026) | Why it worked |
|---|---|---|---|
| 1 | **Rule / ban / 'nobody explained it'**<br>The title promises a fact the viewer did not know and can repeat. One rule, one example play, a payoff line. | Coach Clank, The Unwritten Triple Double Rule: **6.45M** (Jul 11 2026, 25 s) [h9BkqCMpTgI](https://www.youtube.com/shorts/h9BkqCMpTgI)<br>Coach Clank, Banned Jersey Number: **3.70M** (Jun 4 2026, 22 s) [Av6BKn-T5b8](https://www.youtube.com/shorts/Av6BKn-T5b8)<br>Coach Clank, Why Did the NBA Ban Black Masks?: **0.93M** (Mar 26 2026, 28 s) [nGBYSZd-5Uk](https://www.youtube.com/shorts/nGBYSZd-5Uk)<br>REBOUND, 3 NBA Rules You Didn't Know Exist.. (older): **36M** (2022-23) [1sPFMx2RSn8](https://www.youtube.com/shorts/1sPFMx2RSn8)<br>REBOUND, 3 Accessories BANNED in the NBA.. (older): **12M** (2022-23) [49k2JafbfXo](https://www.youtube.com/shorts/49k2JafbfXo)<br>REBOUND, 3 WEIRDEST Bans In NBA History.. (older): **12M** (2022-23) [Oq4KznewexI](https://www.youtube.com/shorts/Oq4KznewexI) | Gives the viewer a 'did you know' to share; the rule is a one-second concept. Counter-example: 'The NBA's Unwritten Rule' 610K and 'Crazy Basketball Rule No One Knows About' 484K (vague = 10x lower). |
| 2 | **Ref / officiating ('how did they miss this')**<br>Show the play, then the rulebook line that explains (or fails to explain) the call. | Coach Clank, This Referee Mistake Confused Everyone: **7.16M** (Mar 27 2026, 29 s) [8377DiUYr0M](https://www.youtube.com/shorts/8377DiUYr0M)<br>Coach Clank, How Did The Refs Miss THIS?!: **2.63M** (Jun 14 2026, 20 s) [gMQA12WZrws](https://www.youtube.com/shorts/gMQA12WZrws)<br>Coach Clank, This Wasn't a Travel!: **1.86M** (May 12 2026, 17 s) [rglYkdYB9sY](https://www.youtube.com/shorts/rglYkdYB9sY)<br>REBOUND, NBA Ref CAUGHT CHEATING.. (older): **10M** (2022-23) [2CYXb5s3cSI](https://www.youtube.com/shorts/2CYXb5s3cSI) | Everyone has an opinion about refs, so the comments argue (replays count as views since Mar 2025). Risk: if the rule explanation is wrong the comments punish it. |
| 3 | **'Why does nobody ...?' mystery**<br>A question about something the viewer has seen but never questioned. | Coach Clank, Why No One Shoots Underhand: **10.92M** (Jun 23 2026, 25 s) [duwsceT6GCs](https://www.youtube.com/shorts/duwsceT6GCs)<br>Coach Clank, Why Do They Do This?: **1.85M** (May 14 2026, 14 s) [rOtI0AXUII0](https://www.youtube.com/shorts/rOtI0AXUII0)<br>Coach Clank, Why Kobe Didn't Like His Teammates: **1.01M** (Jul 27 2026, 21 s) [P7ObHXAGgfU](https://www.youtube.com/shorts/P7ObHXAGgfU)<br>Coach Clank, Why Wemby Hates Gatorade: **0.98M** (Jun 8 2026, 22 s) [mCaN6xhDb3s](https://www.youtube.com/shorts/mCaN6xhDb3s) | Open loop in the first 2 s. 'Why/How/What/Did' openers show 1.64x relative views (n=28, Round 5). |
| 4 | **Size / number gap**<br>Two numbers or two bodies side by side, understood in one second. | Coach Clank, 6'8 vs 7'9: **30.87M** (Jun 10 2026, 15 s) [ViynHMEfThQ](https://www.youtube.com/shorts/ViynHMEfThQ)<br>Coach Clank, 4'5 Player vs 6'8 Player: **2.75M** (May 20 2026, 25 s) [qU0mTvebvI0](https://www.youtube.com/shorts/qU0mTvebvI0)<br>Courtside Films, 5-Foot 8th Grader Starting Varsity!: **5.24M** (Dec 30 2025, 21 s) [XdIlPYFS9-k](https://www.youtube.com/shorts/XdIlPYFS9-k)<br>Courtside Films, This kid is listed at 6'11 328 pounds: **3.62M** (Jun 3 2026, 98 s) [EJawLfzuQ-E](https://www.youtube.com/shorts/EJawLfzuQ-E)<br>Coach Clank, Wemby's Height is Unfair: **0.50M** (Jul 6 2026, 19 s) [LjKx8uHZye4](https://www.youtube.com/shorts/LjKx8uHZye4) | Visual, no explanation needed. Note the spread: a stranger pair got 30.9M, a Wemby height Short got 0.5M: the gap has to be new, not a famous player's known height. |
| 5 | **'Caught' / trick / loophole**<br>Someone got away with something, or a trick the viewer can retell. | Coach Clank, Missing a Free Throw on Purpose?: **10.50M** (Mar 25 2026, 22 s) [DuIHh-R6Anw](https://www.youtube.com/shorts/DuIHh-R6Anw)<br>Coach Clank, The Glitch Shot Guy: **5.74M** (Mar 31 2026, 18 s) [njpY4Sy4eOM](https://www.youtube.com/shorts/njpY4Sy4eOM)<br>Coach Clank, He Tricked the Crowd: **1.75M** (Jun 28 2026, 29 s) [KVXetjn4GvI](https://www.youtube.com/shorts/KVXetjn4GvI)<br>REBOUND, NBA Players CAUGHT CHEATING.. (older): **42M** (2022-23) [ogpXVzy9A9U](https://www.youtube.com/shorts/ogpXVzy9A9U)<br>REBOUND, Lamelo was CAUGHT CHEATING.. (older): **12M** (2022-23) [G5pKUe7rmt0](https://www.youtube.com/shorts/G5pKUe7rmt0) | A 'loophole' story has a built-in twist. Only post with a verified source; 'caught cheating' on a real person needs a primary-source clip. |
| 6 | **Petty / funny / troll moment**<br>A player does something small, human and funny; one-line setup. | Coach Clank, Jimmy Butler Trolling the NBA: **7.59M** (Mar 23 2026, 23 s) [5dsi4C1hg1Y](https://www.youtube.com/shorts/5dsi4C1hg1Y)<br>Coach Clank, He Has the Best Job Ever: **7.05M** (Jun 25 2026, 17 s) [JGcnOe_wn6k](https://www.youtube.com/shorts/JGcnOe_wn6k)<br>Coach Clank, Westbrook Exposed Giannis: **1.46M** (Jul 1 2026, 17 s) [IBVraaIuqTU](https://www.youtube.com/shorts/IBVraaIuqTU)<br>Bleacher Report, Bam didn't have to do Giannis like that: **1.00M** (Sep 2026 (last 10 days)) [_LkYKNe2SdY](https://www.youtube.com/shorts/_LkYKNe2SdY)<br>House of Highlights, Bam put Giannis in the WEIGHT ROOM: **0.64M** (Sep 30 2026, 13 s) [a69PjGZytTM](https://www.youtube.com/shorts/a69PjGZytTM) | Short, shareable, tag-a-friend. Big accounts post these within hours, so we only win by adding a number or a context line. |
| 7 | **One-second spectacle / oddity**<br>A trick shot, a record hoop, an impossible-looking moment. | Coach Clank, The Battle for the World's Highest Basketball Shot: **14.55M** (Mar 29 2026, 28 s) [9hQez2sHAHM](https://www.youtube.com/shorts/9hQez2sHAHM)<br>Coach Clank, He Never Misses a Shot: **10.10M** (Jun 6 2026, 25 s) [Xry25aRK_pE](https://www.youtube.com/shorts/Xry25aRK_pE)<br>Coach Clank, World's Largest Basketball Hoop: **5.52M** (Jun 1 2026, 15 s) [cR53H0MpzJs](https://www.youtube.com/shorts/cR53H0MpzJs)<br>Coach Clank, Is It Possible to Dunk on a 13 Ft Hoop?: **5.70M** (May 24 2026, 23 s) [JaSpIrcHADc](https://www.youtube.com/shorts/JaSpIrcHADc) | Needs original footage of an oddity. Place and record oddities (Hinkle Fieldhouse, 9,100 seats) fit; we cannot make the footage ourselves. |
| 8 | **'200 IQ' smart-play**<br>A clever small play, narrated as genius. | Coach Clank, 200 IQ Defense: **11.97M** (May 22 2026, 20 s) [dKi-JHzMpFw](https://www.youtube.com/shorts/dKi-JHzMpFw)<br>Coach Clank, 200 IQ LaMelo: **11.72M** (May 27 2026, 54 s) [vtG5sL5lgXg](https://www.youtube.com/shorts/vtG5sL5lgXg)<br>Coach Clank, Chris Paul Has 200 IQ: **1.59M** (Jul 5 2026, 26 s) [fv5aBKe_LKE](https://www.youtube.com/shorts/fv5aBKe_LKE)<br>Coach Clank, 200 IQ Inbounds Play: **0.37M** (Aug 11 2026, 19 s) [3E_YA1iiPIE](https://www.youtube.com/shorts/3E_YA1iiPIE) | 'IQ' titles 2.22x (n=8). Needs a real clip of a clever play; hard to pre-plan. |
| 9 | **Old clip / old story resurfaces**<br>A years-old story re-told in 15-60 s with a new hook. | Hoops Lore, Iman Shumpert details the Carmelo-KG fight (132 s): **9.40M** (Jan 31 2026) [PylIR0jvwTk](https://www.youtube.com/shorts/PylIR0jvwTk)<br>Hoops Lore, Dwyane Wade reveals how the Miami Big 3 happened (148 s): **4.80M** (Mar 4 2026) [4yATkra3gCU](https://www.youtube.com/shorts/4yATkra3gCU)<br>Hoop Facts, When The Spurs Memed Shaq (19 s): **2.29M** (Aug 12 2026) [IL8VacaqemY](https://www.youtube.com/shorts/IL8VacaqemY)<br>Hoop Facts, Anthony Davis Is A Liar?! (15 s): **0.95M** (May 20 2026) [UbRoTTzyXsE](https://www.youtube.com/shorts/UbRoTTzyXsE)<br>Courtside Films, LeBron, Kobe and D-Wade in their athletic primes (2008): **2.22M** (Jul 4 2026) [FUkrMAyBjRI](https://www.youtube.com/shorts/FUkrMAyBjRI) | Nostalgia/archive does pull. Caution: Hoops Lore's hits are other people's long interviews, the 'reused content' shape YouTube's inauthentic-content policy targets. Re-tell with our own research and voice. |
| 10 | **Then vs now / ladder**<br>The same thing across years, ages or eras. | Courtside Films, Best Dunk At Each Height! 5'5 to 8'0 (116 s): **2.71M** (Nov 1 2025) [s8hMXPGH0OY](https://www.youtube.com/shorts/s8hMXPGH0OY)<br>Courtside Films, The Most Unique Hooper Each Year (144 s): **1.61M** (Jun 8 2026) [dgNxUjH4Arg](https://www.youtube.com/shorts/dgNxUjH4Arg)<br>Courtside Films, Best Player Each Year! 1st Grade to 12th Grade: **1.44M** (May 23 2026) [-IUTnmDvAHE](https://www.youtube.com/shorts/-IUTnmDvAHE)<br>Bleacher Report, LeBron is all about winning in year 24: **0.63M** (Sep 28 2026, 41 s) [Z4lF0jRdIrQ](https://www.youtube.com/shorts/Z4lF0jRdIrQ) | Weakest-evidenced of the lanes for 20-30 s stories: the strong ladder Shorts are 100+ s montages. We only use then-vs-now when a number gap or rule is the hook. |
| 11 | **List stories ('players/teams who ...')**<br>A 60-70 s list with AI/archival images. | Ahmed's, NBA teams that spent everything to keep their star but lost him: **0.78M** (Aug 12 2026, 66 s) [wKNBA6sbcik](https://www.youtube.com/shorts/wKNBA6sbcik)<br>Ahmed's, Players who were absolute cheat codes in NBA 2K: **0.56M** (Aug 21 2026) [N_i463sjSK8](https://www.youtube.com/shorts/N_i463sjSK8)<br>Ahmed's, NBA players who showed up unrecognizable after one summer: **0.48M** (Aug 26 2026) [NgmDFtFKa_A](https://www.youtube.com/shorts/NgmDFtFKa_A)<br>Ahmed's, NBA teams that added too much talent and got worse: **0.43M** (Sep 2 2026) [g2jg4HMfIv8](https://www.youtube.com/shorts/g2jg4HMfIv8) | Reliable 5-10x of channel median (78K), but small absolute numbers and our Round 5 notes already show contract/list stories flatten. Use as a secondary format. |
| 12 | **Real-time news reaction (big accounts)**<br>A quote or clip from a news event, posted within hours. | House of Highlights, SGA COOKED Jared McCain in a race: **1.70M** (Sep 30 2026, 11 s) [95sRxEOOZ4A](https://www.youtube.com/shorts/95sRxEOOZ4A)<br>House of Highlights, Get BRO in the LEAGUE: **1.58M** (Sep 29 2026, 8 s) [6uKhJ1mR96s](https://www.youtube.com/shorts/6uKhJ1mR96s)<br>NBA, AJ Dybantsa rocking Player Exclusive light up kicks at media day: **0.96M** (Sep 28 2026, 8 s) [NtPkddYTLG0](https://www.youtube.com/shorts/NtPkddYTLG0)<br>Bleacher Report, Wemby has many secret talents: **0.67M** (Sep 30 2026, 23 s) [Wh19WV5lYGc](https://www.youtube.com/shorts/Wh19WV5lYGc) | Fresh and fun, but dominated by accounts with millions of subs and the rights to the clip. Our use of it: only when we add a verified number or rule (see ideas). Their median is still only 12K-77K. |

**Best-evidenced three (for the channel):** (1) Rule/ban/'nobody explained' (REBOUND 12-36M older; Coach Clank 0.9-6.5M in 2026; 2.49x relative views), (2) Ref/officiating 'how did they miss this' (Coach Clank 1.9-7.2M, three in 90 days), (3) 'Why does nobody ...?' mystery (Coach Clank 10.9M, 1.9M, 1.0M; 1.64x for Why/How/What/Did openers).

TikTok/Reels: a search for viral basketball formats returned only vendor listicles (e.g. text-story videos at 2-15M views from small accounts; ShortSync, Clippie) and one Instagram 'viral basketball' tag page; none tied to the NBA story niche. HYPOTHESIS: the same rule/oddity concepts travel to Reels/TikTok with the same cut; we cannot show numbers.

### 2b. Baselines used (Oct 4, 2026)

| Channel (subs) | Sample | Median views | Best recent Short |
|---|---|---|---|
| Coach Clank (145K) | first 48 (Jun-Aug 2026) / 148 since Oct 2025 | 511K / ~421K | 6'8 vs 7'9, 30.87M (Jun 10 2026) |
| Courtside Films (804K) | 120 | 267K | NBA Players Best Dunk From HS, 8.34M (Jan 14 2025) |
| Ahmed's Basketball (121K) | 120 | 78K | NBA teams that spent everything to keep their star but lost him, 0.78M |
| Bleacher Report (5.05M) | 120 | 77K | Bam didn't have to do Giannis like that, 1.00M |
| NBA (24.5M) | 120 | 31.5K | AJ Dybantsa light up kicks, 0.96M |
| House of Highlights (17.7M) | 120 | 29.5K | SGA cooked McCain in a race, 1.70M |
| Overtime (3.95M) | 120 | 23K | Most unfair matchup ever, 0.77M |
| ESPN (14.6M) | 120 | 12K | A'ja Wilson heated exchange with a fan, 0.30M |
| Hoop Facts (51K) | 100 | 42K | When The Spurs Memed Shaq, 2.29M |
| Hoops Lore (16K) | 66 | 36K | Iman Shumpert on Melo-KG fight, 9.40M (132 s) |
| REBOUND (3.4M), older | 59 | 775K | NBA Players CAUGHT CHEATING.., 42M (2022-23) |

## 3. Overlap check (topics already made; do NOT repeat)

Made or scripted in this repo: Jordan push-off, NBA push-off four stars, flopping crackdown, Kawhi/Clippers penalties, Duren contract, LeBron pay cut, LeBron Sixers media day / helicopter, Adams GTA, Heat Vice City / Giannis vs Bucks; also Batch 2: free-throw line, Wemby unanimous vote, Bucks Giannis trade, Sixers superteam, corner three shorter, SGA 14-man club, Kyrie, 'NBA did LeBron's schedule on purpose' (#9), '53 Years for One Banner' (#10), Flagg height. Ideas below that sit near those are flagged 'follow-up angle' or 'overlap' in their risk line.

## 4. The 35 ideas, ranked by score

Score = my 1-5 view of viral potential tied to evidence above. 'Fresh' = tied to a news hook of the last 7 days; 'Old refresh' = a hit from the last 12 months re-angled. Window = post by.

| Rank | Score | Type | Title | Lane | Post by |
|---|---|---|---|---|---|
| 1 | 5 | fresh | How Close Is Jokic To Westbrook's Record? 🤯 | spectacle (record chase) + rule-style number gap | Post by Oct 19 (before opening week); re-run as 'five away' when he is at 204. |
| 2 | 4 | fresh | How Is A Screen Suddenly Illegal Now? 🧱 | rule/ban/caught | Post by Oct 20 (opening night; refs will be talked about all week). |
| 3 | 4 | fresh | Why Can't Teams Win Back-To-Back Lotteries? 🎰 | rule/ban/caught | Post by Oct 20; evergreen through December tanking talk. |
| 4 | 4 | fresh | Why Is The NBA Cup At Hinkle? 🏟️ | spectacle/oddity | Post by Oct 30 (Cup tips off) or Dec 4. |
| 5 | 4 | fresh | Did Kawhi Already Beat LeBron's Sixers? 😳 | then-vs-now | Post by Oct 20 or on the first Kawhi appearance, whichever is first. |
| 6 | 4 | old refresh | Why Do Big Men Never Shoot Underhand? 😳 | oddity / why-nobody | Evergreen; best before Oct 20. |
| 7 | 4 | old refresh | Why Can No NBA Player Wear 6? 🔢 | rule/ban/caught | Evergreen; best the week of Oct 12 (new numbers/uniform talk). |
| 8 | 4 | old refresh | How Many Steps Can Giannis Legally Take? 👣 | rule/ban/caught | Post by Oct 21 (Heat opener). |
| 9 | 4 | old refresh | Is LeBron A Point Guard At 41? 😳 | oddity / number gap | Post by Oct 20 (Sixers opener at Knicks). |
| 10 | 4 | old refresh | What Can't NBA Players Wear On Court? 🚫 | rule/ban/caught | Post by Oct 14. |
| 11 | 3 | fresh | What Is A Straight-Line Pathway Foul? 🛣️ | rule/ban/caught | Post by Oct 20. |
| 12 | 3 | fresh | Why Is Giannis Afraid Of Iguanas? 🦎 | petty/funny | Post by Oct 8 (media day story ages out). |
| 13 | 3 | fresh | Why Did Wemby Turn Down $50 Million? 😳 | then-vs-now / number gap | Post by Oct 20. |
| 14 | 3 | fresh | Why Do Eight Teams Get Extra Jerseys? 👕 | oddity / number gap | Post by Oct 12; refresh on first wear. |
| 15 | 3 | fresh | Why Did Ja Morant Drop Number 12? 🔢 | oddity | Post by Oct 8. |
| 16 | 3 | fresh | What Did Dybantsa Say About Pressure? 😳 | petty/funny | Post by Oct 10. |
| 17 | 3 | fresh | Did DeMar DeRozan Forget His Own Seasons? 😭 | petty/funny | Post by Oct 8. |
| 18 | 3 | fresh | He Is Playing His 24th NBA Season 👑 | then-vs-now | Post by Oct 10. |
| 19 | 3 | fresh | Did Portland Just Build Five Starting Guards? 😳 | oddity | Post by Oct 19. |
| 20 | 3 | fresh | Did Cooper Flagg Lose To A Timer? 😭 | petty/funny | Post by Oct 8. |
| 21 | 3 | fresh | Did Josh Hart Just Roast Brunson's SNL? 😭 | petty/funny | Post by Oct 12. |
| 22 | 3 | fresh | How Rare Is A 100-100 Season? 🤯 | spectacle/oddity | Post by Oct 20. |
| 23 | 3 | fresh | He Had 7 Assists In 14 Minutes 😳 | spectacle | Post by Oct 6. |
| 24 | 3 | fresh | How Wilt's Last Game Crowned The Knicks 🏆 | then-vs-now | Post Oct 19-20. |
| 25 | 3 | old refresh | How Big Is The NBA's Height Gap? 💀 | size gap | Post by Oct 20. |
| 26 | 3 | old refresh | What Did The Spurs Do To Shaq? 🤣 | petty/funny | Post by Nov 20. |
| 27 | 3 | old refresh | How Did Miami Land Another Superstar? 🔥 | then-vs-now | Post by Oct 21. |
| 28 | 3 | old refresh | Why Did Isiah's Pistons Walk Off Early? 😳 | petty beef | Post by Oct 19. |
| 29 | 3 | old refresh | Did Stacking Stars Ever Actually Backfire? 😳 | then-vs-now | Post by Oct 20. |
| 30 | 2 | fresh | What Happens If Rookies Miss This Deadline? ⏰ | rule | Post Oct 15-18. |
| 31 | 2 | fresh | Did Castle Really Ask Wemby About Aura? 😭 | petty/funny | Post by Oct 8. |
| 32 | 2 | fresh | Why Is Opening Day At 3 PM? ☀️ | oddity | Post Oct 19. |
| 33 | 2 | fresh | What Did Minnesota Pay For LaMelo? 🤯 | number gap | Post by Oct 15. |
| 34 | 2 | fresh | Did A Cat Just Steal Media Day? 🐱 | oddity | Post by Oct 8. |
| 35 | 2 | fresh | Why Did LeBron Almost Join Golden State? 🤯 | oddity | Post by Oct 12. |

### 1. How Close Is Jokic To Westbrook's Record? 🤯  (score 5, fresh)

- **Name:** Jokic vs Westbrook triple-double record  
- **Lane:** spectacle (record chase) + rule-style number gap  |  **Format:** Unwritten triple-double rule + record gap
- **8-word concept:** Jokic needs eleven triple-doubles to pass Russell Westbrook
- **Hook (first 6 spoken words):** "Jokic is eleven triple-doubles from history."
- **News hook:** Preseason started Oct 3; Jazz-Nuggets Oct 4 in Boulder; opener Oct 20-21
- **Argument / number gap:** 198 vs 209 regular-season triple-doubles (11 apart). He had 34 last season, so at that pace he passes Westbrook around game 20-22.
- **Facts to verify (source hints):**
  - Basketball-Reference career regular-season leaders: Westbrook 209, Jokic 198, Oscar 181, Magic 138, LeBron 125 (https://www.basketball-reference.com/leaders/trp_dbl_career.html). Re-check the morning you voice it; one search snippet said Westbrook 207 in an older source.
  - Combined regular season + playoffs: Jokic tied Westbrook at 221 on Apr 27, 2026 (https://gazette.com/2026/04/27/nikola-jokic-ties-nba-record-for-career-triple-doubles/).
  - NBA.com Starting 5 (Oct 2): Jokic led the league with 34 triple-doubles last season and the Nuggets lost in the first round (https://www.nba.com/news/starting-5-october-2-2026). Verify 34 on BBRef.
  - ESPN player page: 65 games, 27.7 pts / 12.9 reb / 10.7 ast in 2025-26 (https://www.espn.in/nba/player/_/id/3112335/nikola-jokic). Pace math: 34 in 65 = 52% of games.
  - Nuggets opener date and first 20 games: check the schedule (https://www.nba.com/news/2026-27-schedule-team-by-team-index).
- **Footage plan:** Nuggets X (@nuggets) and @NBA triple-double highlight posts; preview frames from NBA YouTube Jokic triple-double Shorts. Jazz at Nuggets preseason game was Oct 4 (Boulder) per NBA.com Starting 5; official clip on the Nuggets feed after the game. No archive.org footage needed (cards for the two totals).
- **Risk:** Numbers move every game, so re-verify the morning you post. Standard NBA-footage copyright (keep real clips short, transformed with a number card). Do not say he 'will' pass by a date; say 'at his pace'.
- **Freshness window:** Post by Oct 19 (before opening week); re-run as 'five away' when he is at 204.
- **Score 5/5 because:** Proven format: CoachClank 'The Unwritten Triple Double Rule' 6.45M (Jul 11 2026, https://www.youtube.com/shorts/h9BkqCMpTgI); rule/record-gap titles run 2.49x channel median; the numbers are verified and fresh.
- **Pinned comment:** Does Jokic pass Westbrook before Christmas: yes or no?

### 2. How Is A Screen Suddenly Illegal Now? 🧱  (score 4, fresh)

- **Name:** Screens: new 'illegal screen' emphasis  
- **Lane:** rule/ban/caught  |  **Format:** Rule nobody explained + ref/officiating
- **8-word concept:** Refs now whistle screeners doing more than blocking
- **Hook (first 6 spoken words):** "The NBA just redefined the screen."
- **News hook:** NBA points-of-emphasis video, released late Sept
- **Argument / number gap:** Old understanding: a screen is legal if you stand there. New: screeners get penalized when they do 'more than just get in the defender's way'.
- **Facts to verify (source hints):**
  - Bleacher Report: points of emphasis for 2026-27 include 'screeners are being properly penalized when they do more than just get in the defender's way' (https://bleacherreport.com/articles/25504531-nba-drops-video-announcing-new-points-emphasis-referees-during-2026-27-season).
  - ESPN on the same guidelines (https://espn.com/nba/story/_/id/50063714/nba-issues-new-guidelines-instructs-refs-crack-push-offs). Watch the NBA's own video and write down the exact screen examples (players, game dates).
  - Official rulebook wording on illegal/moving screens (NBA rulebook, screening section) to quote one line.
  - Check Productions 14 (four stars), 11 (Jordan) and 17 (flopping) scripts: they used the same video for push-offs and flops, so this Short must use a different clip and the screen examples only.
- **Footage plan:** The NBA's official points-of-emphasis video (posted on @NBA on X, per BR; same source our Shorts 11/14/17 used, so the clips already exist in those production folders, which we must not edit; re-download into the new folder). YouTube NBA channel preview frames as backup.
- **Risk:** Overlap with three made Shorts from the same video: vary the structure (one screen play, one rule line, one question). Verify each example is a screen, not a push-off.
- **Freshness window:** Post by Oct 20 (opening night; refs will be talked about all week).
- **Score 4/5 because:** Rule/ban/'caught' titles = 2.49x relative views (n=26, Round 5); Clank 'This Referee Mistake Confused Everyone' 7.2M (Mar 27 2026, https://www.youtube.com/shorts/8377DiUYr0M).
- **Pinned comment:** Should the screener or the defender get the foul?

### 3. Why Can't Teams Win Back-To-Back Lotteries? 🎰  (score 4, fresh)

- **Name:** New 3-2-1 draft lottery  
- **Lane:** rule/ban/caught  |  **Format:** Rule nobody explained + sounds fake but true
- **8-word concept:** New NBA lottery bans back-to-back number-one picks now
- **Hook (first 6 spoken words):** "The NBA made losing less valuable."
- **News hook:** 3-2-1 lottery approved May 28; season about to start
- **Argument / number gap:** The three worst teams now get 2 balls; the seven teams just above them get 3. 16 teams now enter (was 14).
- **Facts to verify (source hints):**
  - NBA.com release May 28, 2026: '3-2-1 Lottery' expands lottery from 14 to 16 teams and flattens odds (https://pr.nba.com/nba-board-of-governors-approves-new-draft-lottery-system-to-address-tanking).
  - CBS explainer: bottom three get two balls, seven non-playoff teams get three, 9-10 seeds get two, 7-8 play-in losers get one; no team can win No. 1 in consecutive years; no top-5 pick three years running (https://www.cbssports.com/nba/news/nba-new-draft-lottery-system-tanking/). Search snippets conflicted on when it takes effect (2027 draft vs backdated to 2026 per The Athletic, https://www.nytimes.com/athletic/7315465/2026/05/28/nba-board-of-governors-tanking-lottery-draft-changes): confirm on pr.nba.com.
  - The Wizards took AJ Dybantsa No. 1 in 2026 (https://www.nba.com/news/nba-news).
  - The 'ball' counts above come from a search summary; confirm in the NBA release before voicing.
- **Footage plan:** NBA lottery show clips (NBA YouTube previews; ESPN); Dybantsa/Wizards official posts for the hook; graphics for the ball counts. No archive.org needed.
- **Risk:** Conflicting reports on effective date and ball counts; one primary source (pr.nba.com) must settle it. Complicated; keep to ONE gap (2 balls vs 3).
- **Freshness window:** Post by Oct 20; evergreen through December tanking talk.
- **Score 4/5 because:** Rule lane 2.49x; 'sounds fake but true' number gap (worse record = fewer balls) is a one-second concept like Clank's top 25.
- **Pinned comment:** Does this stop tanking or just move it?

### 4. Why Is The NBA Cup At Hinkle? 🏟️  (score 4, fresh)

- **Name:** NBA Cup final in Hinkle Fieldhouse  
- **Lane:** spectacle/oddity  |  **Format:** One-second oddity (place) + size gap
- **8-word concept:** NBA Cup final leaves Vegas for 1928 gym
- **Hook (first 6 spoken words):** "NBA Cup final: a 9,100-seat gym."
- **News hook:** Cup draw/Cup starts Oct 30
- **Argument / number gap:** About 9,100 seats and a building from 1928 hosting an NBA final.
- **Facts to verify (source hints):**
  - Final is Dec 11, 2026 at Butler's Hinkle Fieldhouse, first Cup final outside Las Vegas (https://www.espn.com.au/nba/story/_/id/49230290/butler-hinkle-fieldhouse-host-year-nba-cup-final).
  - ~9,100 seats; hosted at least six presidents; the 1954 Milan-Muncie Indiana title game that inspired 'Hoosiers' was played there and the movie used it for its title game (AP, https://www.boston25news.com/sports/butlers-iconic/EAFFR63B2U4TLOLRTEWE6Q5INE).
  - Opened 1928 (https://iuhoosiers.com/news/2026/7/24/mens-basketball-indiana-sets-exhibition-series-against-butler).
  - Cup group play Oct 30 - Nov 27; quarterfinals Dec 4-5; semis Dec 8-9 (https://www.espn.com/nba/story/_/id/49577473/2026-nba-season-tournament-cup-format-highlights-updates).
  - Compare capacity with T-Mobile Arena (look up the number; do not guess).
- **Footage plan:** @NBA post of the group draw (July 1 2026, pic.twitter.com/OiBSSVkxpm, quoted in the ESPN piece); Butler/Hinkle official posts; NBA YouTube. No clean archive.org Hinkle item found (searched Oct 4). Do NOT use the Hoosiers movie clip (copyright).
- **Risk:** Low. Copyright if using the movie; use stills/NBA posts only. 'High school gym' is wrong: it is a college arena that hosted high-school finals.
- **Freshness window:** Post by Oct 30 (Cup tips off) or Dec 4.
- **Score 4/5 because:** Place-oddity lane: Clank 'World's Largest Basketball Hoop' 5.5M (Jun 1 2026, https://www.youtube.com/shorts/cR53H0MpzJs); Courtside high-school-gym content 5-8M. Indirect evidence.
- **Pinned comment:** Should every NBA final be in a college gym?

### 5. Did Kawhi Already Beat LeBron's Sixers? 😳  (score 4, fresh)

- **Name:** Kawhi's shot vs LeBron's new Sixers  
- **Lane:** then-vs-now  |  **Format:** Then vs now + sounds fake but true
- **8-word concept:** Kawhi's four-bounce shot once eliminated LeBron's new Sixers
- **Hook (first 6 spoken words):** "Kawhi eliminated LeBron's new team already."
- **News hook:** Kawhi to Raptors, LeBron to Sixers, Raptors debut pending
- **Argument / number gap:** 2019: Kawhi's buzzer-beater ended Philadelphia's season. 2026: he is back with Toronto and LeBron is a Sixer.
- **Facts to verify (source hints):**
  - Kawhi was traded Clippers to Raptors this summer (https://www.si.com/nba/thunder, power rankings Sep 14; Hoops Rumors 'Clippers To Trade Kawhi Leonard To Raptors').
  - Kawhi sat out the Oct 3 Heat-Raptors game per ClutchPoints headline; debut still pending (https://clutchpoints.com/nba/nba-stories/nba-news-giannis-playing-kawhi-leonard-out-heat-raptors-preseason-clash).
  - VERIFY (from memory, not found today): May 12, 2019 Game 7 ECSF, Raptors 92-90 over the Sixers, four bounces, first Game 7 buzzer-beater in NBA history. Use NBA.com/Basketball-Reference.
  - LeBron joined the Sixers (ESPN, https://www.espn.com/nba/story/_/id/49226472/lebron-james-informs-lakers-plans-play-elsewhere-2026-27). Find when Sixers play Raptors in 2026-27 (NBA.com team index).
  - This is NOT the Clippers-penalty angle (excluded); keep it to Toronto/Philadelphia.
- **Footage plan:** NBA YouTube 'Kawhi Game 7 buzzer beater' preview frames; @Raptors and @sixers on X for current clips; archive.org: no 2019 item verified (searched), so YouTube frames only.
- **Risk:** 2019 footage is NBA-owned: 3-4 s max with transformation. LeBron/Sixers content already made twice; this must open on Kawhi.
- **Freshness window:** Post by Oct 20 or on the first Kawhi appearance, whichever is first.
- **Score 4/5 because:** Then-vs-now with a hook two fan bases argue about; BR 'LeBron is all about winning in year 24' 632K (Sep 28) and HoH 'Sixers are reviving point forward LeBron' 348K show audience for LeBron/Sixers.
- **Pinned comment:** Which was crazier: Kawhi's shot or LeBron joining Philly?

### 6. Why Do Big Men Never Shoot Underhand? 😳  (score 4, old refresh)

- **Name:** Underhand free throws: new angle  
- **Lane:** oddity / why-nobody  |  **Format:** Why-mystery (Why No One Shoots Underhand)
- **8-word concept:** Underhand free throws work, yet nobody shoots them
- **Hook (first 6 spoken words):** "Rick Barry shot ninety percent underhand."
- **News hook:** Opening week; free-throw talk
- **Argument / number gap:** A near-90% career free-throw shooter vs today's worst free-throw shooters.
- **Facts to verify (source hints):**
  - Evidence: CoachClank 'Why No One Shoots Underhand' 10.9M, 25 s, Jun 23 2026 (https://www.youtube.com/shorts/duwsceT6GCs).
  - VERIFY Rick Barry's career free-throw % (about 89.3%) on Basketball-Reference.
  - New angle: name the 2025-26 worst free-throw shooter among starters (BBRef leaders page) and compare. Do not guess names.
  - Our own earlier underhand Short got 73K (Round 4 note). Copy-check our channel and Clank's before writing.
- **Footage plan:** Rick Barry archive footage: check archive.org (not verified today); YouTube preview frames; NBA clips of the chosen player at the line.
- **Risk:** Clank already did it; we already did it. Only worth making with a NEW named player and number.
- **Freshness window:** Evergreen; best before Oct 20.
- **Score 4/5 because:** 'Why' openers 1.64x; this exact concept = 10.9M for Clank, but crowded.
- **Pinned comment:** Would you shoot underhand to fix your free throws?

### 7. Why Can No NBA Player Wear 6? 🔢  (score 4, old refresh)

- **Name:** Why can nobody wear number 6  
- **Lane:** rule/ban/caught  |  **Format:** Rule/ban + sounds fake but true
- **8-word concept:** The NBA retired number six for everyone, forever
- **Hook (first 6 spoken words):** "Nobody new can ever wear six."
- **News hook:** Ja number change, Specter uniforms
- **Argument / number gap:** One number removed from the whole league.
- **Facts to verify (source hints):**
  - VERIFY on NBA.com: Aug 2022, NBA and NBPA retired Bill Russell's No. 6 league-wide; players already wearing it could keep it.
  - VERIFY Russell's 11 titles and who was grandfathered.
  - Clank 'Banned Jersey Number' 3.7M (Jun 4 2026, https://www.youtube.com/shorts/Av6BKn-T5b8) may be this story: run copy-check first.
  - Fresh hook: Ja Morant switched 12 to 1 (ESPN, https://www.espn.com/nba/story/_/id/49252695/ja-morant-portland-trail-blazers-nba-switches-changes-jersey-number-12-1) and the new Specter uniforms (ESPN, https://www.espn.com/nba/story/_/id/49885469/nba-nike-specter-uniforms-2026-knicks-lakers-celtics-warriors-pistons-76ers-hawks-kings).
- **Footage plan:** archive.org item 'We_Are_Boston_-_Bill_Russell' (2008, found today); Celtics X; NBA YouTube Russell tribute previews.
- **Risk:** Copy-check could return TAKEN. archive.org item is a TV documentary (rights unclear).
- **Freshness window:** Evergreen; best the week of Oct 12 (new numbers/uniform talk).
- **Score 4/5 because:** Banned-number Short = 3.7M; rule/ban lane = 2.49x.
- **Pinned comment:** Which number should the NBA retire next?

### 8. How Many Steps Can Giannis Legally Take? 👣  (score 4, old refresh)

- **Name:** Gather step explained with Giannis  
- **Lane:** rule/ban/caught  |  **Format:** Ref/officiating + rule nobody explained
- **8-word concept:** Gather step explained using Giannis' famous long strides
- **Hook (first 6 spoken words):** "Giannis takes two steps, sometimes three."
- **News hook:** Giannis Heat debut
- **Argument / number gap:** Steps people count (3-4) vs steps the rule allows.
- **Facts to verify (source hints):**
  - Evidence: Clank 'This Wasn't a Travel!' 1.86M (May 12 2026, https://www.youtube.com/shorts/rglYkdYB9sY); 'LeBron Didn't Travel!' 625K; 'This Referee Mistake Confused Everyone' 7.2M.
  - VERIFY the gather-step and zero-step wording in the NBA rulebook (travelling section) and the league's 2019 clarification.
  - Giannis made his Heat preseason debut Oct 3 (BR, https://bleacherreport.com/articles/25506277-giannis-makes-heat-preseason-debut-after-bucks-trade-final-box-score-stats-highlights): pick one drive from the game.
  - Heat opener Oct 21 vs Minnesota (same BR article).
- **Footage plan:** Heat X (@MiamiHEAT) clips of the debut; NBA's own 'rule explained' videos; YouTube previews.
- **Risk:** Rule nuance: wrong interpretation gets pile-on comments. Do not call a specific play 'a travel' without the rule text.
- **Freshness window:** Post by Oct 21 (Heat opener).
- **Score 4/5 because:** Travel/ref Shorts 0.6-7.2M for Clank; Giannis is the most-searched new-team star.
- **Pinned comment:** Is Giannis traveling or is the rule broken?

### 9. Is LeBron A Point Guard At 41? 😳  (score 4, old refresh)

- **Name:** LeBron: point guard at 41  
- **Lane:** oddity / number gap  |  **Format:** Ladder / then-vs-now
- **8-word concept:** LeBron averaged 7.2 assists while scoring a career-low
- **Hook (first 6 spoken words):** "LeBron averaged seven assists at forty-one."
- **News hook:** Sixers scrimmage Oct 3, opener Oct 20
- **Argument / number gap:** 20.9 points (fewest since rookie year) but 7.2 assists; 125 career regular-season triple-doubles (5th).
- **Facts to verify (source hints):**
  - AP/NBA.com May 12 2026: 20.9 ppg, 7.2 apg, 6.1 rpg, 33.2 mpg, 31.7% from three; oldest player ever with a triple-double (https://www.nba.com/news/lebron-james-undecided-on-future-after-playoff-loss).
  - BBRef: LeBron 125 regular-season triple-doubles, 5th (https://www.basketball-reference.com/leaders/trp_dbl_career.html).
  - Sixers open scrimmage Oct 3: 'balling, babysitting' (StatMuse headline list, https://www.statmuse.com/nba); NBA.com recap https://www.nba.com/news/lebron-james-76ers-open-scrimmage.
  - Evidence: Clank 'Is LeBron Selfish?' 5.65M (Apr 5 2026, https://www.youtube.com/shorts/mPsk3t7Md3Q), 'When LeBron Decided to Stop Passing' 1.05M.
- **Footage plan:** @sixers on X (scrimmage clips); ESPN Short 'Imagine catching a lob from LeBron on Day 1' (via sixers/TT, https://www.youtube.com/shorts/a1s-Zp0cRXE, 40K) shows official clips exist.
- **Risk:** LeBron pay cut / media day / helicopter Shorts are already made; keep this on passing numbers only.
- **Freshness window:** Post by Oct 20 (Sixers opener at Knicks).
- **Score 4/5 because:** LeBron 'selfish/passing' debate = 5.65M for Clank.
- **Pinned comment:** Is LeBron better as a passer now than a scorer?

### 10. What Can't NBA Players Wear On Court? 🚫  (score 4, old refresh)

- **Name:** Three things NBA players can't wear  
- **Lane:** rule/ban/caught  |  **Format:** Rule/ban list (REBOUND)
- **8-word concept:** Three accessories the NBA actually bans on court
- **Hook (first 6 spoken words):** "Three things NBA players can't wear."
- **News hook:** Specter + Standard Issue launch
- **Argument / number gap:** Sounds free-form, actually tightly regulated.
- **Facts to verify (source hints):**
  - REBOUND '3 Accessories BANNED in the NBA..' 12M (https://www.youtube.com/shorts/49k2JafbfXo; sample dates 2022-23, so format evidence, not recent).
  - Clank 'Why Did the NBA Ban Black Masks?' 930K (Mar 26 2026, https://www.youtube.com/shorts/nGBYSZd-5Uk); 'Asking for Players Arm Sleeves' 1.1M (Apr 4).
  - VERIFY every item in the NBA uniform/equipment rules (headbands, undershirt colours, masks, logos, sleeves) before voicing.
  - 2026 hook: Nike Specter fifth jerseys + Standard Issue warmups for all 30 teams (https://www.espn.com/nba/story/_/id/49885469/nba-nike-specter-uniforms-2026-knicks-lakers-celtics-warriors-pistons-76ers-hawks-kings).
- **Footage plan:** NBA/team X posts of players in masks/headbands; NBA YouTube previews; stills only for the rule text.
- **Risk:** Needs 3 verified items; one wrong claim sinks it. List format = 25-30 s.
- **Freshness window:** Post by Oct 14.
- **Score 4/5 because:** Bans lane has the highest ceiling in our data (REBOUND 12M-36M; Clank 0.9-3.7M).
- **Pinned comment:** What should the NBA ban next?

### 11. What Is A Straight-Line Pathway Foul? 🛣️  (score 3, fresh)

- **Name:** Straight-line pathway foul  
- **Lane:** rule/ban/caught  |  **Format:** Rule nobody explained
- **8-word concept:** Bump a cutter off his path, get whistled
- **Hook (first 6 spoken words):** "The NBA now protects your pathway."
- **News hook:** Points of emphasis
- **Argument / number gap:** Both offense and defense now have a protected 'straight line'; bumping a player off it is a foul.
- **Facts to verify (source hints):**
  - BR: 'Contact on straight-line pathway plays should warrant a foul' and off-ball defenders should have 'the necessary space to move around the perimeter and into the paint' (https://bleacherreport.com/articles/25504531-nba-drops-video-announcing-new-points-emphasis-referees-during-2026-27-season).
  - Round 4 note (Research Notes/Round 4) says offense and defense both keep the right to a direct path and both can be fouled for bumping; re-read ESPN (https://espn.com/nba/story/_/id/50063714/nba-issues-new-guidelines-instructs-refs-crack-push-offs) for exact wording.
  - Find ONE vivid example play in the NBA video; without it the Short is abstract.
  - Confirm this angle is not already inside Production 14 or 11.
- **Footage plan:** Same official NBA video on X (@NBA). Backup: YouTube previews.
- **Risk:** Abstract rule; weak spectacle. Without one clear example clip, skip. Overlap with screens idea; do not post both the same day.
- **Freshness window:** Post by Oct 20.
- **Score 3/5 because:** Rule lane is proven (2.49x) but this one is abstract; REBOUND '3 NBA Rules You Didn't Know Exist' 36M (older, 2022-23) shows the lane ceiling, not this topic.
- **Pinned comment:** Is the straight line fair to defenders?

### 12. Why Is Giannis Afraid Of Iguanas? 🦎  (score 3, fresh)

- **Name:** Iguanas vs Giannis  
- **Lane:** petty/funny  |  **Format:** Petty/funny player moment
- **8-word concept:** Giannis threatens to leave his pool over iguanas
- **Hook (first 6 spoken words):** "Iguanas might make Giannis move out."
- **News hook:** Giannis first Miami weeks
- **Argument / number gap:** A 10-time All-Star ready to move out of a house for a lizard.
- **Facts to verify (source hints):**
  - NBA.com: at Heat media day (Sep 28) Giannis said 'If the iguanas keep on coming, I'll probably move, maybe get an apartment. No pools, no grass'; called iguanas 'scary', not cute (https://www.nba.com/news/giannis-begins-new-chapter-in-miami).
  - He posted about it over the weekend (same source). Find the post.
  - Do not repeat Heat Vice City angle; this is new.
- **Footage plan:** Heat X media-day video; Giannis's own post (verify account/permission); NBA.com article for the quote card.
- **Risk:** Social posts may be removed; fall back to the official media-day clip.
- **Freshness window:** Post by Oct 8 (media day story ages out).
- **Score 3/5 because:** Petty/funny lane: Clank 'Jimmy Butler Trolling the NBA' 7.6M, 'He Has the Best Job Ever' 7.05M; HoH 'Bam put Giannis in the WEIGHT ROOM' 637K (Sep 30).
- **Pinned comment:** Would you move out because of iguanas?

### 13. Why Did Wemby Turn Down $50 Million? 😳  (score 3, fresh)

- **Name:** Wemby took less money  
- **Lane:** then-vs-now / number gap  |  **Format:** Number gap
- **8-word concept:** Wemby chose $252M over the $303M supermax offer
- **Hook (first 6 spoken words):** "Wemby said no to fifty million."
- **News hook:** Spurs open Oct 20
- **Argument / number gap:** $252M (25% max) vs $303M (30% supermax), about $50M difference.
- **Facts to verify (source hints):**
  - ESPN Jul 10 2026: five-year, $252M max rookie-scale extension, player option in year five; 25% max instead of 30% supermax escalators to $303M; could save the Spurs roughly $50M (https://www.espn.com/nba/story/_/id/49328757/sources-spurs-victor-wembanyama-reach-252-million-max-extension).
  - Hoops Rumors lists ~$255.2M; reconcile before voicing (https://www.hoopsrumors.com/2026/07/2026-27-nba-contract-extension-tracker.html).
  - Third-largest rookie extension; Cade Cunningham and Evan Mobley $269M each (same ESPN).
  - Spurs open Oct 20 vs OKC (9:30 pm ET NBC).
- **Footage plan:** @wemby post Jul 10 2026 ('Spurs family, I'm here to stay. Whatever it takes'); @spurs on X; NBA YouTube previews.
- **Risk:** Contract lane is our weakest in evidence; July news is not fresh. Needs a fresh hook (opening night).
- **Freshness window:** Post by Oct 20.
- **Score 3/5 because:** Wemby content sells (BR 'Wemby has many secret talents' 665K, Sep 30) but contract Shorts are flat on Ahmed's (Round 5); a clear $ gap helps.
- **Pinned comment:** Would you take $50M less to win?

### 14. Why Do Eight Teams Get Extra Jerseys? 👕  (score 3, fresh)

- **Name:** Specter: eight teams, 53 of 84 titles  
- **Lane:** oddity / number gap  |  **Format:** Sounds fake but true (numbers)
- **8-word concept:** Eight old teams hold 53 of 84 titles
- **Hook (first 6 spoken words):** "Eight teams got a brand-new jersey."
- **News hook:** Specter announced Sep 9-10
- **Argument / number gap:** 8 of 30 teams own 53 of 84 titles.
- **Facts to verify (source hints):**
  - ESPN Sep 10: Knicks, Celtics, Lakers, 76ers, Warriors, Pistons, Hawks, Kings get 'Specter' uniforms; those franchises combined for 53 of 84 titles (https://www.espn.com/nba/story/_/id/49885469/nba-nike-specter-uniforms-2026-knicks-lakers-celtics-warriors-pistons-76ers-hawks-kings).
  - Joins Association, Icon, Classic, Statement and City editions; wear dates not announced (same).
  - Dark base, Swoosh centred, name below the number (https://www.colorwaysports.com/stories/nba-specter-edition-jerseys-2026-27).
  - Nike 'Standard Issue' collection shown Sep 9 in Brooklyn for all 30 teams' warmups.
- **Footage plan:** Team and NBA X posts of the uniforms (images); ESPN photos are licensed, so use team posts only.
- **Risk:** Photos rights; opinion on design is subjective. Better when the first team wears it.
- **Freshness window:** Post by Oct 12; refresh on first wear.
- **Score 3/5 because:** Jersey/uniform Shorts: 'Banned Jersey Number' 3.7M; number gap 53/84 is one-second.
- **Pinned comment:** Which Specter jersey is the best?

### 15. Why Did Ja Morant Drop Number 12? 🔢  (score 3, fresh)

- **Name:** Ja Morant gives up number 12  
- **Lane:** oddity  |  **Format:** Banned jersey number (adjacent)
- **8-word concept:** Ja leaves 12 for number 1 in Portland
- **Hook (first 6 spoken words):** "Ja Morant just dropped his number."
- **News hook:** Ja Portland debut
- **Argument / number gap:** One digit change after his whole career.
- **Facts to verify (source hints):**
  - ESPN: Ja Morant switches from 12 to 1 with Portland (https://www.espn.com/nba/story/_/id/49252695/ja-morant-portland-trail-blazers-nba-switches-changes-jersey-number-12-1).
  - NBA YouTube Short 'Still Call 12' about his new number, 373K views (https://www.youtube.com/shorts/2MHpWBIpn-w).
  - Traded Memphis to Portland for Jerami Grant and Kris Murray (https://basketnews.com/news-250872-ja-morant-reaction-on-shocking-blazers-trade-revealed-per-nba-insider.html).
  - REASON not found today: find the actual reason before scripting; if it is bland, skip.
- **Footage plan:** @NBA video 'Still Call 12'; @trailblazers on X.
- **Risk:** No reason known; the NBA already owns the clip (373K).
- **Freshness window:** Post by Oct 8.
- **Score 3/5 because:** Number-change content: 'Banned Jersey Number' 3.7M, but the reason is unknown.
- **Pinned comment:** Which jersey number suits Ja best?

### 16. What Did Dybantsa Say About Pressure? 😳  (score 3, fresh)

- **Name:** Dybantsa says 'None' to pressure  
- **Lane:** petty/funny  |  **Format:** Petty/funny quote
- **8-word concept:** Number one pick answers pressure question with 'None'
- **Hook (first 6 spoken words):** "Asked about pressure, Dybantsa answered: none."
- **News hook:** Wizards preseason
- **Argument / number gap:** Top pick, one-word answer.
- **Facts to verify (source hints):**
  - NBA.com media-day live blog: asked about pressure as No. 1 pick, Dybantsa said 'None.' (https://www.nba.com/news/live-updates-2026-nba-media-days).
  - Wizards took him No. 1 (https://www.nba.com/news/wizards-take-aj-dybantsa-no-1-2026-draft); roster includes Trae Young and Anthony Davis (FOX Sports, https://www.foxsports.com/nba/aj-dybantsa-player).
  - NBA YouTube Short of Dybantsa's light-up kicks hit 956K in 8 s (https://www.youtube.com/shorts/NtPkddYTLG0): audience exists.
  - Get the full question and context.
- **Footage plan:** @WashWizards on X; @NBA media day clip.
- **Risk:** One-word quote may lack a story. Need the clip with the question.
- **Freshness window:** Post by Oct 10.
- **Score 3/5 because:** Short quote concept; official NBA Dybantsa Short = 956K.
- **Pinned comment:** Is 'none' confidence or denial?

### 17. Did DeMar DeRozan Forget His Own Seasons? 😭  (score 3, fresh)

- **Name:** DeRozan can't count his seasons  
- **Lane:** petty/funny  |  **Format:** Petty/funny quote
- **8-word concept:** DeRozan can't count his eighteen seasons on fingers
- **Hook (first 6 spoken words):** "DeMar was asked how many seasons."
- **News hook:** Media day
- **Argument / number gap:** 18th season, cannot count it.
- **Facts to verify (source hints):**
  - NBA.com media-day live blog: 'I can't... I'll be honest, I can't.' (https://www.nba.com/news/live-updates-2026-nba-media-days).
  - NBA YouTube Short on 'Year 18 for DeMar' 408K (https://www.youtube.com/shorts/a1_8z2lo23w).
  - Verify his team (live blog says Nuggets) and 18th season (drafted 2009).
- **Footage plan:** @NBA YouTube/X clip; team X.
- **Risk:** Official NBA already posted (408K); we only win by adding the number context.
- **Freshness window:** Post by Oct 8.
- **Score 3/5 because:** Funny quotes on NBA channel: 408K-956K.
- **Pinned comment:** How many seasons can YOU name from memory?

### 18. He Is Playing His 24th NBA Season 👑  (score 3, fresh)

- **Name:** LeBron season 24 vs Kobe's 20  
- **Lane:** then-vs-now  |  **Format:** Ladder / then-vs-now
- **8-word concept:** LeBron's 24th season outlasts Kobe's entire twenty-year career
- **Hook (first 6 spoken words):** "Kobe played twenty. LeBron's playing twenty-four."
- **News hook:** Sixers debut
- **Argument / number gap:** 24 seasons vs Kobe's 20 (verify).
- **Facts to verify (source hints):**
  - ESPN: LeBron returning for unprecedented 24th season (https://www.espn.com/nba/story/_/id/49226472/lebron-james-informs-lakers-plans-play-elsewhere-2026-27).
  - AP: record 23rd season ended May 2026; passed Parish for games played (https://www.nba.com/news/lebron-james-undecided-on-future-after-playoff-loss).
  - NBA YouTube 'LeBron's Kobe Year - a new challenge' 688K (https://www.youtube.com/shorts/A9hgTUJGtc8, Sep 28): watch it to see what 'Kobe Year' means.
  - Kobe played 20 seasons (verify).
- **Footage plan:** @NBA video; @sixers.
- **Risk:** LeBron media day is excluded: use only the seasons-gap angle.
- **Freshness window:** Post by Oct 10.
- **Score 3/5 because:** LeBron year-24 post got 632K (BR, Sep 28).
- **Pinned comment:** Will LeBron play season 25?

### 19. Did Portland Just Build Five Starting Guards? 😳  (score 3, fresh)

- **Name:** Portland's five guards  
- **Lane:** oddity  |  **Format:** Sounds fake but true
- **8-word concept:** Portland now owns Ja, Dame, Jrue, Scoot, Shaedon
- **Hook (first 6 spoken words):** "Portland has five guards, one ball."
- **News hook:** Blazers media day, deadline
- **Argument / number gap:** 5 guard-sized stars, 1 ball; Scoot's extension deadline Oct 19.
- **Facts to verify (source hints):**
  - Basketnews: backcourt is Jrue Holiday, Scoot Henderson, Shaedon Sharpe, Damian Lillard (recovered) plus Ja Morant (https://basketnews.com/news-250872-ja-morant-reaction-on-shocking-blazers-trade-revealed-per-nba-insider.html).
  - Lillard enters as Portland's all-time leading scorer with 19,376 points (NBA.com live blog).
  - Scoot Henderson eligible for a rookie extension until Oct 19, 5 pm CT (Hoops Rumors).
  - New coach Micah Nori.
- **Footage plan:** @trailblazers X; NBA YouTube.
- **Risk:** Roster may change; verify Dame and Scoot status.
- **Freshness window:** Post by Oct 19.
- **Score 3/5 because:** Sounds-fake-true roster oddity.
- **Pinned comment:** Who sits first?

### 20. Did Cooper Flagg Lose To A Timer? 😭  (score 3, fresh)

- **Name:** Flagg vs the timer  
- **Lane:** petty/funny  |  **Format:** Petty/funny moment
- **8-word concept:** Flagg tried stopping a timer at one second
- **Hook (first 6 spoken words):** "Flagg missed the timer by milliseconds."
- **News hook:** Mavs media day
- **Argument / number gap:** Rookie of the Year, one-second challenge.
- **Facts to verify (source hints):**
  - Mavs media day Sep 25: Flagg tried to stop a timer at exactly 1.00 while Naji Marshall cut a banana (ESPN media day recap; single source, Round 4).
  - Need the clip and the exact result before voicing.
  - Flagg was Rookie of the Year (NBA.com Cup schedule).
- **Footage plan:** @dallasmavs X.
- **Risk:** Single source for detail.
- **Freshness window:** Post by Oct 8.
- **Score 3/5 because:** Small funny rookie moment.
- **Pinned comment:** Can you stop it at 1.00?

### 21. Did Josh Hart Just Roast Brunson's SNL? 😭  (score 3, fresh)

- **Name:** Hart on Brunson's SNL  
- **Lane:** petty/funny  |  **Format:** Petty/funny quote
- **8-word concept:** Josh Hart says Brunson has no acting future
- **Hook (first 6 spoken words):** "Josh Hart reviewed Brunson's SNL hosting."
- **News hook:** Knicks media day
- **Argument / number gap:** Champion teammate roasting hosting gig.
- **Facts to verify (source hints):**
  - Hart: 'I think his performance was fine. I don't think he has a future in acting.' (https://sports.yahoo.com/articles/josh-hart-gives-hilarious-honest-143000754.html).
  - Brunson first Knick to host SNL (season 52 premiere).
  - Knicks banner night Oct 20.
- **Footage plan:** @nyknicks; NBC SNL clips = high copyright risk.
- **Risk:** NBC copyright.
- **Freshness window:** Post by Oct 12.
- **Score 3/5 because:** Funny teammate roast.
- **Pinned comment:** Rate Brunson's SNL 1-10.

### 22. How Rare Is A 100-100 Season? 🤯  (score 3, fresh)

- **Name:** Barnes 100 steals 100 blocks  
- **Lane:** spectacle/oddity  |  **Format:** Sounds fake but true
- **8-word concept:** Scottie Barnes joined an almost empty steals-blocks club
- **Hook (first 6 spoken words):** "Barnes did what almost nobody has."
- **News hook:** Raptors
- **Argument / number gap:** 100+ steals and 100+ blocks.
- **Facts to verify (source hints):**
  - NBA.com Starting 5: Barnes recorded 100+ blocks and steals last season (https://www.nba.com/news/starting-5-october-2-2026).
  - Do NOT name others until checked on Basketball-Reference.
  - Raptors preseason: Kawhi and Barnes.
- **Footage plan:** @Raptors X.
- **Risk:** Needs a verified list.
- **Freshness window:** Post by Oct 20.
- **Score 3/5 because:** Stat oddity.
- **Pinned comment:** Is Barnes underrated?

### 23. He Had 7 Assists In 14 Minutes 😳  (score 3, fresh)

- **Name:** Giannis 7 assists in 14 minutes  
- **Lane:** spectacle  |  **Format:** News reaction with a number
- **8-word concept:** Giannis played point forward in his Heat debut
- **Hook (first 6 spoken words):** "Giannis had seven assists before halftime."
- **News hook:** Oct 3 debut
- **Argument / number gap:** 7 assists, 9 points in 14 minutes.
- **Facts to verify (source hints):**
  - BR first-half box: 14 min, 9 pts (3-3 FG), 4 reb, 7 ast, 2 TO; Heat led 76-55 (https://bleacherreport.com/articles/25506277-giannis-makes-heat-preseason-debut-after-bucks-trade-final-box-score-stats-highlights).
  - Final score not in that article.
  - Compare his career-high assists (verify).
- **Footage plan:** @MiamiHEAT clips.
- **Risk:** News cycle ends fast.
- **Freshness window:** Post by Oct 6.
- **Score 3/5 because:** Giannis demand.
- **Pinned comment:** Is Giannis a point forward now?

### 24. How Wilt's Last Game Crowned The Knicks 🏆  (score 3, fresh)

- **Name:** Wilt's last game crowned the Knicks  
- **Lane:** then-vs-now  |  **Format:** Old clip resurfaces
- **8-word concept:** Wilt's final game was the Knicks' last clincher
- **Hook (first 6 spoken words):** "Wilt's last game crowned the Knicks."
- **News hook:** Banner night Oct 20
- **Argument / number gap:** 1973 vs 2026: 53 years.
- **Facts to verify (source hints):**
  - archive.org item: 1973 NBA Finals Game 5 Knicks at Lakers, 'Chamberlain's last game' (https://archive.org/details/nba-1973-playoff-finals-lakers-vs-knicks-game-5-chamberlains-last-game).
  - NBA.com: Knicks raise first banner since 1973 on Oct 20 (https://www.nba.com/news/2026-27-schedule-announced).
  - Verify Game 5 clinched the series and that it was Wilt's last game.
- **Footage plan:** archive.org item above; also 'youtube-ZiWzpL_bxKM' Knicks first title.
- **Risk:** NBA-owned broadcast; clip short. Overlaps Batch 2 #10 (53 Years).
- **Freshness window:** Post Oct 19-20.
- **Score 3/5 because:** Archive nostalgia: Courtside 2008 Olympics Short 2.2M.
- **Pinned comment:** Which Knicks title do you remember?

### 25. How Big Is The NBA's Height Gap? 💀  (score 3, old refresh)

- **Name:** Height gap: Wemby vs Kawamura  
- **Lane:** size gap  |  **Format:** Size gap (6'8 vs 7'9)
- **8-word concept:** Wembanyama at 7'4 stands over Kawamura at 5'7
- **Hook (first 6 spoken words):** "Twenty-one inches separate these two players."
- **News hook:** Season opener
- **Argument / number gap:** 7'4 vs 5'7 = 21 inches.
- **Facts to verify (source hints):**
  - Clank '6'8 vs 7'9' 30.9M (Jun 10 2026, https://www.youtube.com/shorts/ViynHMEfThQ, 15 s).
  - Clank '4'5 Player vs 6'8 Player' 2.75M (https://www.youtube.com/shorts/qU0mTvebvI0).
  - Wemby listed 7'4 (Spurs) / 7'5 (NBA bio) - verify (Round 4).
  - Kawamura team and height: verify (Round 4 flagged conflicting reports).
  - Flagg height Short already made; keep distinct.
- **Footage plan:** NBA/team X; YouTube previews.
- **Risk:** Heights conflict; team conflict.
- **Freshness window:** Post by Oct 20.
- **Score 3/5 because:** Size-gap top hit 30.9M, but Wemby-height Shorts ~0.5M.
- **Pinned comment:** Who wins one-on-one?

### 26. What Did The Spurs Do To Shaq? 🤣  (score 3, old refresh)

- **Name:** Spurs memed Shaq  
- **Lane:** petty/funny  |  **Format:** Old clip resurfaces
- **8-word concept:** An old Spurs-Shaq meme resurfaces before Lakers-Spurs Cup
- **Hook (first 6 spoken words):** "The Spurs once memed Shaquille O'Neal."
- **News hook:** Cup Nov 27
- **Argument / number gap:** Unknown until clip watched.
- **Facts to verify (source hints):**
  - Hoop Facts 'When The Spurs Memed Shaq' 2.29M, 19 s, Aug 12 2026 (https://www.youtube.com/shorts/IL8VacaqemY).
  - Lakers at Spurs Cup game Nov 27 (NBA.com).
  - Watch frames first (Tools/yt_sheet.py).
- **Footage plan:** YouTube previews only.
- **Risk:** Story unverified.
- **Freshness window:** Post by Nov 20.
- **Score 3/5 because:** 2.29M in 19 s.
- **Pinned comment:** Best Shaq meme?

### 27. How Did Miami Land Another Superstar? 🔥  (score 3, old refresh)

- **Name:** Heat Big Three story + Giannis  
- **Lane:** then-vs-now  |  **Format:** Old clip resurfaces (interview)
- **8-word concept:** Wade's 2010 Big Three story mirrors Giannis's arrival
- **Hook (first 6 spoken words):** "Miami has done this before. Twice."
- **News hook:** Heat opener
- **Argument / number gap:** 2010 vs 2026.
- **Facts to verify (source hints):**
  - Hoops Lore 'Dwyane Wade Reveals How the Miami Big 3 Actually Happened' 4.8M, 148 s (Mar 4 2026, https://www.youtube.com/shorts/4yATkra3gCU).
  - Giannis traded Jun 22 2026 (BR).
  - Use original sources, not the repost.
- **Footage plan:** @MiamiHEAT.
- **Risk:** Reused interview policy risk.
- **Freshness window:** Post by Oct 21.
- **Score 3/5 because:** 4.8M for interview reveal.
- **Pinned comment:** Was 2010 or 2026 bigger?

### 28. Why Did Isiah's Pistons Walk Off Early? 😳  (score 3, old refresh)

- **Name:** Pistons walked off in 1991  
- **Lane:** petty beef  |  **Format:** Old clip resurfaces / petty beef
- **8-word concept:** Pistons walked off before the 1991 final buzzer
- **Hook (first 6 spoken words):** "The Pistons refused to shake hands."
- **News hook:** Pistons opener
- **Argument / number gap:** Bad Boys swept, left early.
- **Facts to verify (source hints):**
  - archive.org 'youtube-395kV56gsdA' May 27 1991 'The Infamous Walk-Off'.
  - Verify seconds left and who stayed.
  - Pistons open Oct 20 vs Celtics.
- **Footage plan:** archive.org item.
- **Risk:** NBA-owned footage.
- **Freshness window:** Post by Oct 19.
- **Score 3/5 because:** Petty beef; thin Shorts evidence.
- **Pinned comment:** Was it disrespect?

### 29. Did Stacking Stars Ever Actually Backfire? 😳  (score 3, old refresh)

- **Name:** Stacking stars backfires  
- **Lane:** then-vs-now  |  **Format:** List (Ahmed's)
- **8-word concept:** Teams that added stars sometimes won fewer games
- **Hook (first 6 spoken words):** "Adding stars can make teams worse."
- **News hook:** Superteams
- **Argument / number gap:** Names vs wins.
- **Facts to verify (source hints):**
  - Ahmed's 'NBA teams that added too much talent and got worse' 434K, 66 s (Sep 2 2026, https://www.youtube.com/shorts/g2jg4HMfIv8).
  - Verify examples on BBRef.
  - Sixers, Heat, Raptors all stacked.
- **Footage plan:** YouTube previews; cards.
- **Risk:** Needs 3 verified cases.
- **Freshness window:** Post by Oct 20.
- **Score 3/5 because:** 434K for a 121K channel.
- **Pinned comment:** Which team stacks worst?

### 30. What Happens If Rookies Miss This Deadline? ⏰  (score 2, fresh)

- **Name:** Rookie extension deadline Oct 19  
- **Lane:** rule  |  **Format:** Rule explainer
- **8-word concept:** Miss October 19, rookies hit restricted free agency
- **Hook (first 6 spoken words):** "One deadline decides these rookies' futures."
- **News hook:** Deadline Oct 19
- **Argument / number gap:** Sign by Oct 19 5 pm CT.
- **Facts to verify (source hints):**
  - Hoops Rumors: eligible until day before opener (https://www.hoopsrumors.com/2026/07/2026-27-nba-contract-extension-tracker.html).
  - Unsigned per search: Brandon Miller, Scoot Henderson, Dereck Lively II, Bilal Coulibaly - verify current.
  - Signed: Wemby, Amen Thompson, Keyonte George, Ausar Thompson (Jul 15).
- **Footage plan:** Team X; cards.
- **Risk:** Status changes daily.
- **Freshness window:** Post Oct 15-18.
- **Score 2/5 because:** Contract lane weakest.
- **Pinned comment:** Who gets paid?

### 31. Did Castle Really Ask Wemby About Aura? 😭  (score 2, fresh)

- **Name:** Castle asks Wemby about aura  
- **Lane:** petty/funny  |  **Format:** Funny moment
- **8-word concept:** Spurs teammates joke about Wemby's aura, media day
- **Hook (first 6 spoken words):** "Wemby was asked about his aura."
- **News hook:** Media day
- **Argument / number gap:** n/a
- **Facts to verify (source hints):**
  - NBA.com live blog: Stephon asking Wembanyama 'You see your aura bro?' (verify which Stephon).
  - Find the Spurs post.
- **Footage plan:** @spurs.
- **Risk:** Unclear context.
- **Freshness window:** Post by Oct 8.
- **Score 2/5 because:** Small funny.
- **Pinned comment:** What is Wemby's aura?

### 32. Why Is Opening Day At 3 PM? ☀️  (score 2, fresh)

- **Name:** Opening day at 3 PM  
- **Lane:** oddity  |  **Format:** Oddity
- **8-word concept:** NBC tripleheader begins with a rare afternoon opener
- **Hook (first 6 spoken words):** "The NBA season starts in daylight."
- **News hook:** Opener
- **Argument / number gap:** 3 pm vs usual night.
- **Facts to verify (source hints):**
  - ESPN: Celtics-Pistons 3 pm ET Oct 20, then 76ers at Knicks 7, OKC at Spurs 9:30 (https://www.espn.ph/nba/story/_/id/49471934/nba-full-schedule-2026-2027-games-watch-faq-rivalries-matchups).
  - Verify 'rare'.
- **Footage plan:** NBC Sports X.
- **Risk:** Low interest.
- **Freshness window:** Post Oct 19.
- **Score 2/5 because:** Weak concept.
- **Pinned comment:** Do you watch at 3?

### 33. What Did Minnesota Pay For LaMelo? 🤯  (score 2, fresh)

- **Name:** LaMelo trade haul  
- **Lane:** number gap  |  **Format:** Number gap
- **8-word concept:** Hornets got Reid plus seven picks for LaMelo
- **Hook (first 6 spoken words):** "Charlotte got seven picks for LaMelo."
- **News hook:** Wolves preseason
- **Argument / number gap:** Reid + 7 picks.
- **Facts to verify (source hints):**
  - Basketnews: Reid, 2033 unprotected 1st, three 1st swaps 2028-30, three 2nds (https://basketnews.com/news-250560-lamelo-ball-trade-to-timberwolves-full-details-revealed.html).
  - LaMelo 20.1 pts, 7.1 ast in 72 games.
  - Same format as Kawhi-picks Short (made).
- **Footage plan:** @Timberwolves.
- **Risk:** Format fatigue.
- **Freshness window:** Post by Oct 15.
- **Score 2/5 because:** Trade lane weak.
- **Pinned comment:** Win or lose trade?

### 34. Did A Cat Just Steal Media Day? 🐱  (score 2, fresh)

- **Name:** Pelicans cat at media day  
- **Lane:** oddity  |  **Format:** Oddity
- **8-word concept:** A cat showed up at Pelicans media day
- **Hook (first 6 spoken words):** "The Pelicans had a surprise guest."
- **News hook:** Media day
- **Argument / number gap:** n/a
- **Facts to verify (source hints):**
  - NBA.com live blog: 'best media day ever 🐱'.
  - Details unknown; find Pelicans post.
- **Footage plan:** @PelicansNBA.
- **Risk:** Unknown details.
- **Freshness window:** Post by Oct 8.
- **Score 2/5 because:** Weak evidence.
- **Pinned comment:** Name the cat.

### 35. Why Did LeBron Almost Join Golden State? 🤯  (score 2, fresh)

- **Name:** LeBron Warriors prediction  
- **Lane:** oddity  |  **Format:** Sounds fake but true
- **8-word concept:** Betting market had LeBron going to Golden State
- **Hook (first 6 spoken words):** "Everyone expected LeBron in Golden State."
- **News hook:** LeBron
- **Argument / number gap:** 70% vs outcome.
- **Facts to verify (source hints):**
  - KalshiHoops X post via socialpruf (https://socialpruf.com/x/KalshiHoops): over 70% chance - verify date.
  - Outcome Sixers (ESPN).
  - ESPN Short 'LeBron almost went WHERE?!' 61K (https://www.youtube.com/shorts/Va-pjAkop8A).
- **Footage plan:** X posts.
- **Risk:** Gambling/prediction-market content policy risk.
- **Freshness window:** Post by Oct 12.
- **Score 2/5 because:** Low evidence.
- **Pinned comment:** Where did you think?

## 5. Footage sources actually found

- **X (official posts quoted by articles, not opened):** @NBA group-draw post for the Cup (Jul 1 2026, pic.twitter.com/OiBSSVkxpm); @HoustonRockets uniform reveal (Jun 4 2026, pic.twitter.com/Aj0OmxTsnw); @wemby extension post (Jul 10 2026, text quoted by ESPN). Team accounts to search for media-day and preseason clips: @MiamiHEAT, @Raptors, @nyknicks, @sixers, @spurs, @dallasmavs, @trailblazers, @WashWizards, @Timberwolves, @nuggets, @PelicansNBA.
- **Official YouTube Shorts (preview frames only):** NBA 'Still Call 12' (2MHpWBIpn-w), 'Year 18 for DeMar' (a1_8z2lo23w), Dybantsa kicks (NtPkddYTLG0), 'LeBron's Kobe Year' (A9hgTUJGtc8); BR 'Wemby secret talents' (Wh19WV5lYGc); ESPN 'LeBron almost went WHERE?!' (Va-pjAkop8A).
- **archive.org items (search API returned them Oct 4; rights belong to the broadcaster):** 1973 NBA Finals Game 5 Knicks at Lakers, Chamberlain's last game (`nba-1973-playoff-finals-lakers-vs-knicks-game-5-chamberlains-last-game`); 1970 NBA Finals Gm 5 highlights (`1970-nba-finals-gm.-5-lakers-vs.-knicks-highlights`); Knicks capture first title (`youtube-ZiWzpL_bxKM`); 1991 Bulls-Pistons 'Infamous Walk-Off' (`youtube-395kV56gsdA`); Bulls at Knicks 1995 Jordan 'Double Nickel' (`dvd-transfer-87`); 1994 ECSF Game 7 Bulls-Knicks partial (`dvd-transfer-217`); 1998 Finals Game 6 (`1998nbafinalsgame6`); 1988 Dunk Contest (`youtube-_MuOx4_oHoE`, `dvd-transfer-168`); 2000 All-Star Weekend (`dvd-transfer-149`); Kobe 81 (`KobeBryant81PointLegend`); We Are Boston: Bill Russell (`We_Are_Boston_-_Bill_Russell`); Dream Team 1992 replays (`youtube-tQp8ulkbflY` and others). Not found: Hinkle Fieldhouse, 2019 Kawhi shot, Rick Barry.

## 6. Source URLs used for the news hooks

- https://www.nba.com/news/2026-nba-canada-series-everything-to-know
- https://www.nba.com/news/starting-5-october-2-2026
- https://www.nba.com/news/live-updates-2026-nba-media-days
- https://www.nba.com/news/giannis-begins-new-chapter-in-miami
- https://bleacherreport.com/articles/25506277-giannis-makes-heat-preseason-debut-after-bucks-trade-final-box-score-stats-highlights
- https://bleacherreport.com/articles/25504531-nba-drops-video-announcing-new-points-emphasis-referees-during-2026-27-season
- https://espn.com/nba/story/_/id/50063714/nba-issues-new-guidelines-instructs-refs-crack-push-offs
- https://www.nba.com/news/2026-27-schedule-announced
- https://www.espn.com/nba/story/_/id/49577473/2026-nba-season-tournament-cup-format-highlights-updates
- https://www.espn.com.au/nba/story/_/id/49230290/butler-hinkle-fieldhouse-host-year-nba-cup-final
- https://www.espn.com/nba/story/_/id/49885469/nba-nike-specter-uniforms-2026-knicks-lakers-celtics-warriors-pistons-76ers-hawks-kings
- https://www.espn.com/nba/story/_/id/49328757/sources-spurs-victor-wembanyama-reach-252-million-max-extension
- https://www.basketball-reference.com/leaders/trp_dbl_career.html
- https://gazette.com/2026/04/27/nikola-jokic-ties-nba-record-for-career-triple-doubles/
- https://pr.nba.com/nba-board-of-governors-approves-new-draft-lottery-system-to-address-tanking
- https://www.cbssports.com/nba/news/nba-new-draft-lottery-system-tanking/
- https://www.hoopsrumors.com/2026/07/2026-27-nba-contract-extension-tracker.html
- https://basketnews.com/news-250560-lamelo-ball-trade-to-timberwolves-full-details-revealed.html
- https://basketnews.com/news-250872-ja-morant-reaction-on-shocking-blazers-trade-revealed-per-nba-insider.html
- https://www.espn.com/nba/story/_/id/49226472/lebron-james-informs-lakers-plans-play-elsewhere-2026-27
- https://www.nba.com/news/lebron-james-undecided-on-future-after-playoff-loss
- https://clutchpoints.com/nba/nba-stories/nba-news-giannis-playing-kawhi-leonard-out-heat-raptors-preseason-clash
- https://sports.yahoo.com/articles/josh-hart-gives-hilarious-honest-143000754.html
- https://socialpruf.com/x/KalshiHoops
- https://www.espn.ph/nba/story/_/id/49471934/nba-full-schedule-2026-2027-games-watch-faq-rivalries-matchups

Caveat on sourcing: the results come from search snippets and summaries of those pages; confirm each number on the page itself before voicing (that is what the 'verify' lines are for).