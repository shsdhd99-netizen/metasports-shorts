# Channels like Swishyyy: who wins in sports Shorts and why (Oct 26, 2026)

**The owner asked (Oct 26):** "find out similar channels to the one i linked (ai voice viral shorts in nba, nfl, soccer etc). research why theyre successful, the tendencies they use to grow, and how to effectively learn from them". Then: "factor youtube shorts mainly... we need to figure out the key to retention".

**What I did:**
- Found channels through YouTube's own Shorts hashtag pages (#nba, #nfl, #soccer, #football, #sportsshorts and 20 more), plus our earlier competitor lists.
- Pulled every Short's title and view count for 61 channels (`yt-dlp --flat-playlist`).
- Pulled channel start dates and recent posting rates from YouTube's RSS feeds.
- Looked at YouTube's auto-frames (cover plus 25/50/75% frames) for about 70 Shorts across 16 channels.
- Data: `Research Notes/Similar Channels data (Oct 26, 2026).csv`. The daily research task now watches `Research Notes/Competitor Watchlist.csv`.

**What I could not do:** watch or hear any of them. So "AI voice" is a guess from on-screen captions that follow speech. Hashtag pages show what's already viral, so this sample leans toward winners.

**Tiers:** [V] measured · [S] seen in frames, small sample · [H] a guess.

## 1. The short answer
1. **There are three kinds of winning sports Shorts, and only one uses a voice.** [V/S]

   | Family | Examples | Typical Short (median of channels' newest-30 medians) | Voice? |
   |---|---|---|---|
   | **Game or countdown device**: ranking 1/10 to 10/10, "last one is crazy", player-elimination games | roycebball, SparkBalls, Ftblpranz, footballgoat7, TAT_futbol | **180K** | Mostly no |
   | **Reposted clip + one funny caption** | ChazNBA, breakawayclips, GlobalHoopss, OffTheGlassTelevision, docbooo | 86K | No |
   | **Narrated story, explainer or moment** (our family) | Swishyyy, Hoopiverse, CoachClank, Ahmed's x3, Rebound Rewind | 76K | Yes |

   The narrated family has the best *all-time* hit rate (62% of Shorts at 100K+), but its newest Shorts are weaker than its old ones on most channels. Ahmed's Goal is at 276K all-time and 110K for its newest 30. CoachClank is at 505K and 203K.
2. **Every family puts the event on screen in second 1.** No channel in this sample opens on a title card, a stat graphic or a talking head explaining what's coming. [S]
3. **The biggest growth this year came from formats with a built-in reason to stay to the end:**
   - **Elimination games** (soccer): a row of player faces at the top gets crossed out one by one. Ftblpranz started May 2026 and has 188K subscribers; footballgoat7 started Jan 2026 and has 243K; top Shorts 46M and 84M.
   - **Rankings** (roycebball, started Apr 2026): 57K subscribers from only 32 Shorts, median 390K.
   - **"Last one is crazy" compilations** (SparkBalls): 18 Shorts, median 245K, top 52M.

   [V for the numbers; H that the device is *why*: within channels, titles that promise an ending do no better than the channel's own median (0.76x, n=92), so the device works at the format level, not as title wording.]
4. **Narrated channels that grow are moment-first.** [S]
   - Swishyyy and Hoopiverse narrate over one viral clip: a kid, a fan, a creator's challenge, a funny NBA moment.
   - Captions are short and centred. Hoopiverse adds emoji stickers on faces and a year tag ("2023").
   - Swishyyy's three biggest (29M, 21M, 8.6M) are other creators' challenge videos (100-point shot, giant hoop, signed-ball prank) retold with a voice.
5. **Posting rate doesn't explain who wins.** [V]
   - IvyValee posts about 11 a day (60K subscribers in 3 months), and so does HermeticHoops (55K after 10 years, median 32K).
   - roycebball posts about twice a week and has the best median in NBA.
   - Swishyyy posts about 1 every 2 days.
6. **Titles barely matter.** This repeats our earlier finding. Across 25,000 Shorts on 37 sports channels, measured against each channel's own median: [V]
   - question titles: 1.01x
   - "This/These/The ...": 1.06x
   - "When ...": 1.22x
   - "Part N" series: 1.21x
   - "POV": 1.53x (n=24, too small)

## 2. What this means for retention (the key)
"Stayed to watch" is decided by **whether the first second already shows the thing**. "Average % viewed" is decided by **whether the viewer knows something better is still coming**.

The winners handle both, in different ways:

| Device | How it holds people | Seen on | Can we use it? |
|---|---|---|---|
| The event itself at 0.0 s | Nothing to wait for; the viewer is already watching it | all | **Yes, already our rule (Oct 26)** |
| A visible countdown or progress row (faces crossed out, 1/10 to 10/10, "#3... #2... #1") | The viewer can see how far the Short has to go, and that the best is last | Ftblpranz, footballgoat7, roycebball, PrimeTime | **Yes**: "top 3" moment Shorts with a 3-2-1 counter in a corner |
| "Last one is crazy" (a promise made at 0 s, paid at the end) | An open loop | SparkBalls, TAT_futbol | **Yes**, spoken in line 1: "Wait for the third one." [H] |
| A replay of the key second (slow motion, a second angle) | Rewards people who stay; gives a reason to rewatch | Swishyyy (the 25/50/75% frames are often the same event from another angle) | **Yes**: new tool option (see the editing note) |
| One funny caption that reframes the clip | The joke lands at the payoff | breakaway, GlobalHoops, OffTheGlass | Partly: our narration's last line does this |
| Story with turns every 8-12 s | Each turn is a new promise | Ahmed's, CoachClank | Soccer channel, yes |

## 3. Channels to learn from (our watchlist)
| Channel | Sport | Format | Subscribers | Shorts | Median | Newest-30 median | Started |
|---|---|---|---|---|---|---|---|
| @roycebball | NBA | face-cam ranking 1/10 to 10/10 | 56.6K | 32 | 390K | 559K | Apr 2026 |
| @SparkBalls | NFL | "last one is crazy" compilations with a reaction cutout | 31K | 18 | 245K | 245K | 2019 (new format) |
| @Ftblpranz | Soccer | player-elimination game | 188K | 143 | 196K | 138K | May 2026 |
| @footballgoat7 | Soccer | player-elimination game | 243K | 159 | 180K | 93K | Jan 2026 |
| @ChazNBA | NBA | reposted fan/IG clip with a header | 667K | 281 | 146K | 197K | 2017 |
| @breakawayclips | Basketball | meme clip with one caption | 110K | 332 | 148K | 106K | Dec 2025 |
| @CoachClank | NBA | narrated story | 145K | 433 | 505K | 203K | 2022 |
| @ReboundRewind | NBA | narrated explainer | 236K | 740 | 153K | 132K | 2019 |
| @AhmedsGoal | Soccer | narrated story | 424K | 1,370 | 276K | 110K | (2013 account) |
| @HoopiverseYT | NBA | **narrated moment** (closest to Swishyyy) | 15.3K | 132 | 39K | 73K | 2023 |
| @docbooo | NBA | clip edit with top text | 28.3K | 724 | 27K | 72K | 2017 |
| @swishyhoopz | NBA | **narrated moment** | 21.3K | 203 | 41K | 65K | Aug 2025 |

Not useful for us (non-sports, AI skits, religious or prank pages that happened to be tagged #sports): KaajuFact, stupingers, akcreativeknowledge, SGFactree07, SuNon99, OhSoFact.

## 4. What we should do (proposed, in order)
1. **Keep narrated moment Shorts as the NBA core**, built to the Oct 26 calm-cut rules (#69 v2, #70).
2. **Add one "countdown" format per week on each channel** (a test, not a switch):
   - NBA: "3 times [star] [did X]" with a visible 3-2-1 in a corner, the best one last, voice over each.
   - Soccer: "3 players who [did X]".
   - It's our version of roycebball and the elimination games, which are the fastest-growing formats in the sample.
3. **Replay the key second.** Every moment Short shows the moment, then a slower or closer replay, just before the payoff line.
4. **Say the promise in line 1 when there is one:** "wait for his reaction", "the last one is the worst". Test it against the plain opener. Title wording doesn't matter; the spoken promise might [H].
5. **Don't copy the reposted-clip family wholesale.**
   - It has no voice or original value, which puts it at risk under YouTube's reused-content policy.
   - Our edge is the narration that adds who, why and the payoff.

## 5. Caveats
- The sample comes from hashtag pages and our lists, so it leans toward channels that already have viral Shorts.
- Subscriber growth per month assumes the channel was active since its start date.
- Format families are classified from titles and 4 frames per Short, not by watching.
- "AI voice" can't be confirmed without listening. The Gemini watcher (`Tools/yt_watch.py`) can confirm it once the owner adds the free key.
