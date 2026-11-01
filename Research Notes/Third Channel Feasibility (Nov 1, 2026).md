# Third channel feasibility: NFL, GTA 6, or neither (Nov 1, 2026)

Tiers: [V] measured or from a linked source, [S] small sample, [H] a guess, [U] unverified. Public view counts come from `yt-dlp --flat-playlist` on the newest 60 Shorts of each channel, pulled Nov 1, 2026. Subscriber counts come from one single-video yt-dlp call. `Research Notes/Account 2/GTA6 Plan.md` did not exist in this branch when I wrote this; this note does not plan GTA 6 content.

## 0. Answer
**Do not start a third channel this week.** The evidence says our limit is premise quality and a fragile daily pipeline, not spare capacity. If the owner still wants one, the better candidate is **NFL as a narrated odd-story channel, not GTA 6**, and only as a 14-day test paid for by cutting weak FC slots (net zero extra voice and Claude spend). GTA 6 is a news-hype lane with a hard change point at Nov 19 and a footage policy that conflicts with monetisation. Conditions and kill rule are in section 6.

## 1. Real marginal cost in our pipeline terms
| Resource | What the repo says | A 3rd channel adds |
|---|---|---|
| ElevenLabs characters | About 3K credits per Short with 2 takes (`CLOUD STATE - read this first.md`: "fits about 1 soccer Short a day (about 3K credits each with 2 takes)"). Owner: about 80K left of 121K, resets Nov 8. The Nov 1 Daily Log says 83,440 left "until Nov 19": the two dates disagree [U], check with `voiceover.py --check`. `UPLOAD SCHEDULE.md`: "about 2 Shorts a day total on the current plan" | 1 Short a day is +3K/day on a base of about 6K/day (+50%). 80K lasts about 13 days at today's rate, about 9 days with a third channel at 1/day. Music beds bill here too |
| Claude weekly usage | **Not recorded anywhere in the repo** [U]: no log line gives % per Short or per daily run. Only proxy: a Claude session with the key finishes a waiting Short "in about 20 minutes" (`UPLOAD SCHEDULE.md`) | +50% on Short-making, plus research, fact-check and copy-check per story, plus a footage source to build for NFL (section 2). The 50% weekly ceiling in `C:\Users\Admin\AGENTS.md` is the binding limit and its latest reading is stale (62% on Oct 2) |
| Review time (owner) | About 5 min per Short to post (`Posting Roadmap - Oct 2026.md`). Auto-scheduling Mode B is chosen but needs `yt_auth.py` per channel | A third `yt_auth.py` sign-in, a Hub, a brand kit and a third Monday Studio export. Approvals only, but a third set |
| Daily-run slots | Two scheduled runs: 3:17 AM NBA, 4:23 AM FC (`UPLOAD SCHEDULE.md`) | A third run, or one run making two channels. Runs without the ElevenLabs key finish only the script: Oct 30 to Nov 1 produced #80, #82, S19, S20 as scripts only (`Research Notes/Daily Log.md`). The two existing runs are already fragile |
| Owner attention | Two channels, two Hubs, TikTok/IG paused | One more of everything, plus new-account setup |
| Footage sourcing | NBA: ESPN game-summary `videos` give direct MP4s (`CLOUD STATE`) | NFL: **the ESPN equivalent returned nothing in my test** (section 2) |

**Verdict on cost:** the voice cost is affordable only if something else is cut. The Claude-usage cost is unmeasured, so the first step of any test is to read the weekly % before and after a week of two-channel running [U].

## 2. NFL option
**Market (flat-playlist, newest 60 Shorts unless noted, Nov 1).**
| Channel | Subs | Format | Median views | Newest-20 median | Max |
|---|---|---|---|---|---|
| FieldFlix | 498K | Narrated odd-story ("Why NFL Player Covers Himself In Sticky Stuff", "A Girl Got BANNED By The NFL") | **283K** | 470K | 2.8M |
| TK Twelve | n/a | Short NFL takes and fun facts | 21K | 20.5K | 150K |
| NFL (official) | n/a | League clips | 25K | 14K | 1.7M |
| Stark Raving Sports | n/a | Mixed sports explainers | 13K | 12.5K | 751K |
| Touchdown Rewind | 10.1K | NFL lists and news (n=36) | 8.5K | 8.9K | 135K |
| The Gridiron | n/a | NFL (n=23) | 3.5K | 3.5K | 34K |

- Our Oct 26 study found only compilation and meme NFL channels at scale (`Similar Channels data (Oct 26, 2026).csv`: SparkBalls 245K median, OFFTHEGLASSTV 157K, NFL Gridiron Unscripted 59K). FieldFlix is the first narrated NFL channel I found, and the closest match to our FC goalkeeper pattern (an odd person, object or rule in the title). One channel [S].
- **Saturation:** small NFL story channels (Touchdown Rewind, The Gridiron) sit at 3-9K, about NBA-channel level. A new channel's likely range is 3-9K unless the premise is FieldFlix-grade [S]. FieldFlix's newest 20 are above its 60-Short median, so the lane is not decaying [S].
- This mirrors our own data: premise matters more than niche (FC goalkeeper 15-30K vs everything else 1-3K; `Soccer Topic Study (Nov 1, 2026).md`).

**Season timing [V].** Today is Week 8 (about Oct 29 to Nov 2, 14 games, 4 teams on bye per [nflplayoffpass.com](https://nflplayoffpass.com/nfl-week-8-schedule/); the ESPN scoreboard API also reports week 8). Super Bowl LXI is Feb 14, 2027 ([Wikipedia](https://en.wikipedia.org/wiki/Super_Bowl_LXI), [AOL](https://www.aol.com/articles/super-bowl-lxi-feb-14-170600490.html)). End date of the regular season [U]. Evergreen odd-story Shorts do not need the season, but views rise in season.

**Rights risk.**
- No NFL Shorts-specific policy found [U]. The league has a takedown history: it asked YouTube to remove more than 3,000 clips, and had Twitter disable highlight links in 2015 ([Harvard Berkman](https://cyber.harvard.edu/node/93586), [FierceVideo](https://www.fiercevideo.com/online-video/sports-fans-roil-twitter-after-it-pulls-accounts-due-to-copyright-complaints-over)). The NBA is known for tolerance ("highlights are marketing", [Awful Announcing](https://awfulannouncing.com/tag/nba-highlights)); the NFL is not.
- The NFL's sanctioned route is the **Access Pass** program: selected creators and ex-players get approved footage, live game footage excluded ([Digiday](https://digiday.com/marketing/the-nfl-gives-creators-access-to-its-archives-for-content-creation-with-pre-approved-footage/), [Tubefilter](https://www.tubefilter.com/2025/01/28/the-nfl-is-turning-ex-players-into-media-moguls-on-youtube/amp/)). A faceless AI-voice channel is unlikely to be picked [H].
- **Our sourcing equivalent does not exist yet.** I tested the ESPN summary endpoint for NFL on one completed Week 7 game (event 401873010): it returned 0 videos [S, n=1]. Until another source is proven, the NFL channel has no verified footage supply. That alone blocks a start.
- YouTube side: strikes are the danger (3 in 90 days ends the channel and linked channels); claims alone cost revenue or countries (`Shorts Mechanics and Policy (Oct 24, 2026).md`). Use a separate Google identity so a strike cannot touch the NBA/FC channels [H].

**News-cycle fit.** NFL plays Thursday, Sunday, Monday; our NBA run does "last night's games" every morning. NFL news Shorts would cluster Mon-Tue and need the clip supply above. Evergreen odd stories (FieldFlix style) fit the FC model better than news.

## 3. GTA 6 option
- **Launch date [V]:** November 19, 2026, reaffirmed on Take-Two's August 2026 earnings call, no delay ([Shacknews](https://www.shacknews.com/article/149250/gta-6-release-date-confirmed), [Insider Gaming](https://insider-gaming.com/gta-6-release-date-has-not-changed-take-two-ceo/), [Vice](https://www.vice.com/en/article/take-two-ceo-confirms-gta-6-wont-be-delayed-again-and-teases-next-trailer-date/)). I found nothing newer than August; re-check after the next earnings call [U]. That is 18 days from today. Platforms: PS5 and Xbox Series X|S; PC not announced in those articles.
- **Market (flat-playlist, Nov 1):**

| Channel | Subs | Format | Median (60) | Newest-20 | Max |
|---|---|---|---|---|---|
| TGG | 2.29M | GTA 6 commentary and theory | 174K | 156K | 2.1M |
| T5G | n/a | News and easter eggs | 60K | 81.5K | 3.6M |
| Bombastic | n/a | Clips and reactions | 46K | 25K | 1.7M |
| JANTSUU | n/a | n=7 | 112K | 112K | 239K |
| Wanted Level | n/a | Small GTA 6 channel | **1.7K** | 1.65K | 5.7K |
| This is GTA | n/a | n=10 | 1.2K | 1.2K | 2.5K |

  Relevance-ranked search for "gta 6 shorts" shows a median above 1M [S, n=9, biased to winners]. The market is bimodal: established channels at 50-170K, new small channels at 1-2K. A new channel with no audience looks like Wanted Level, not TGG [S].
- **Rights:** Rockstar's policy ([support.rockstargames.com](https://support.rockstargames.com/articles/200153756/rockstar-games-video-policy); "last updated January 10, 2025" is from a search summary, my two page fetches timed out [U]) tolerates occasional non-commercial fan use and defines non-commercial as not earning money from the game footage. Take-Two reserves takedown at any time and has hit mod projects and money-glitch videos ([80.lv](https://80.lv/articles/take-two-takes-down-gta-vice-city-nextgen-edition-mod-youtube-channel), [GameStar](https://www.gamestar.de/artikel/gta_online,3274816.html)). That conflicts with a channel built for YPP. Allowed footage today: Rockstar's own trailers and press screenshots; gameplay exists only after Nov 19; leaked material is the takedown magnet [H].
- **Post-launch decay [H, no source]:** launch-news spike, then a drop as content turns to gameplay clips where high-volume gameplay creators dominate. Our edge (narrated stories over real archive footage) does not transfer to a game.
- **Fit to our pipeline:** none of our proven craft (a real event, fact-check, broadcast footage) applies. The Account 2 plan covers content separately.

## 4. Putting the same resources into the two channels instead
- **Premise, not volume.** FC: every goalkeeper-in-a-shootout Short is 15-30K, every other is 1-3K [V, n=12]; the script template is identical in hits and flops (`Soccer Script Craft`). Competitors' newest fifth is below their own median on most channels, so do not copy volume (`Soccer Topic Study` recency check).
- **NBA:** last-30 median about 6.9K; present-day named-star-plus-odd-detail stories win (Bronny 27K, #72 24K, Boozer 19K); the history test lost (#78 Rodman 2.9K); music is not decisive (`Rodman and Music Test`).
- **Capacity already tight:** runs without the key produced scripts only three days in a row; cloud push and network failures are recorded in `CLOUD STATE`; the 50% ceiling binds; ElevenLabs allows about 2 Shorts a day.
- **Untested FC lanes with positive priors:** fan/kid and family stories (1.53 channel-balanced), "When..." titles. These cost nothing extra and could lift the 1-3K floor.
- **Compounding:** FC has about 130 subs; each hit adds subscribers to an existing account. A third account restarts at zero.

## 5. Honest read
- A third channel pays only if its premise supply is FieldFlix-grade (one odd detail per story). We have one proven premise lane (FC goalkeeper) and none for NFL.
- NFL: strong market evidence (one channel), real rights risk, no verified footage source. GTA 6: loud, short window, unfavourable policy, a craft we have not shown.
- The first 14 days would pay full setup cost while the pipeline already misses days.

## 6. Recommendation and decision rule
**Default: do not start. Spend the next 14 days on the two channels** (FC goalkeeper series, two fan/kid tests, NBA present-day star stories) and read the weekly usage % at the start and end so a Short's Claude cost becomes a number.

**Start the NFL test only if all are true:**
1. Weekly Claude usage is below 35% at the start, from a fresh reading (this session had no usage tool; AGENTS.md's number is stale).
2. Auto-scheduling is live for both channels (`yt_auth.py` done) and the last 5 daily runs each finished with voice (no "key: MISSING").
3. At least 3 FC goalkeeper Shorts posted after Nov 1 average 9K+ (the lane is real), or the owner knowingly accepts spending on an unproven lane.
4. A named NFL footage source is proven on 5 distinct stories (not ESPN `videos`, which returned 0), with the strike risk accepted by the owner in writing.
5. ElevenLabs balance and reset date are checked (the Nov 8 vs Nov 19 conflict).

**14-day test design:** new channel on a separate Google identity, 7 Shorts (one every other day, 40-55 s), all FieldFlix-style "odd detail in the title" stories on the FC template (one object, one hidden fact, an undercut), no season news. Cost cap: 21K ElevenLabs characters and no new daily run, just one 20-minute Claude session every other day. Read views at 72 h, not day 0 (`UPLOAD SCHEDULE.md` rule 4).
- **Pass (continue):** median of the 7 at least 8K, or 2 of 7 at 15K+ (the FC hit bar), and at least 100 new subscribers.
- **Kill (stop on day 14, or day 10 once 5 Shorts are out):** median under 3K and under 50 subscribers, or any copyright strike, or a footage claim on 2 of the first 4. No second try with the same format; never delete or re-upload (rule 5).
- **Ambiguous (3-8K median, 50-100 subs):** one more batch of 7, then decide on the same bars; no further extension.

**What to stop to pay for it (net zero extra voice and Claude spend):**
1. Hold FC non-goalkeeper, non-fan stories (S09 type, money/transfer, Messi-name-led): their voice budget goes to the NFL Shorts.
2. No second daily posts on NBA until the weekly reading is fresh (the 2nd post did no worse, but costs the same voice credits; `Posting Study`).
3. No more music tuning, history-story series, or research rounds on editing (Editing Study: top-half and bottom-half edits are nearly identical).

**GTA 6:** do not start. If the owner insists, wait until after Nov 19, re-check the Take-Two earnings call and Rockstar's policy page first. Pre-launch trailer news for a new account is a 1.7K-median lane [S] and a policy risk for any channel aiming at monetisation.

## Sources
[Shacknews](https://www.shacknews.com/article/149250/gta-6-release-date-confirmed) · [Insider Gaming](https://insider-gaming.com/gta-6-release-date-has-not-changed-take-two-ceo/) · [Vice](https://www.vice.com/en/article/take-two-ceo-confirms-gta-6-wont-be-delayed-again-and-teases-next-trailer-date/) · [Rockstar policy](https://support.rockstargames.com/articles/200153756/rockstar-games-video-policy) · [80.lv](https://80.lv/articles/take-two-takes-down-gta-vice-city-nextgen-edition-mod-youtube-channel) · [GameStar](https://www.gamestar.de/artikel/gta_online,3274816.html) · [Wikipedia Super Bowl LXI](https://en.wikipedia.org/wiki/Super_Bowl_LXI) · [nflplayoffpass Week 8](https://nflplayoffpass.com/nfl-week-8-schedule/) · [Digiday Access Pass](https://digiday.com/marketing/the-nfl-gives-creators-access-to-its-archives-for-content-creation-with-pre-approved-footage/) · [Tubefilter](https://www.tubefilter.com/2025/01/28/the-nfl-is-turning-ex-players-into-media-moguls-on-youtube/amp/) · [Harvard Berkman](https://cyber.harvard.edu/node/93586) · [Awful Announcing](https://awfulannouncing.com/tag/nba-highlights). Repo: `Soccer Topic Study`, `Soccer Script Craft`, `UPLOAD SCHEDULE.md`, `Rodman and Music Test`, `Editing Study`, `Similar Channels (Oct 26, 2026)`, `Shorts Mechanics and Policy (Oct 24, 2026)`, `CLOUD STATE - read this first.md`, `Research Notes/Daily Log.md`.
