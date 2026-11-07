# Posting Study (Oct 26, 2026)

**The owner's question:** what times should we post, how often, tags or no tags, is filling the 500-character tag field necessary, and does the description matter? YouTube Shorts only. Retention (viewers staying) comes first.

**Tiers:** [V] measured · [S] small sample, or seen on other channels · [H] a guess to test.

**Data pulled Oct 26, 2026, 07:51-07:55 UTC.** Public RSS feeds and yt-dlp channel lists only. Nothing on YouTube was opened, posted or changed.
- Snapshot of every upload used here (ours plus 13 channels, 238 rows): `Research Notes/Posting Study data (Oct 26, 2026).csv`
- Our retention numbers: `Research Notes/Shorts Dataset.csv` (Studio exports in `Research Notes/Studio exports/`)

---

## The answer

1. **Post time hardly matters, so pick a slot you can keep every day.**
   - YouTube's view: after a couple of weeks, videos "end up in the same place regardless of what exact hour" they went up [V, YouTube Blog Apr 2024].
   - In our 34 NBA Shorts, the posting hour showed no link to views or to "stayed to watch" [S].
   - The 13 big channels post at every hour from 1 AM to 10 PM ET, and no hour wins across them [S].
   - **News is the exception:** post it as soon as it's ready, the morning after the game. Our one day-late news Short (#63) held only 57.6% [V, n=1, `Niche Study - NBA Shorts (Oct 24, 2026).md`].
   - Keep the current slots: NBA at 11 AM ET, FC at 12 PM ET.
2. **Post once a day on each channel.**
   - Add a second NBA Short (6 PM) only when it's as strong as the first. Never post 3 in a day.
   - Our days with 2 posts did as well per post as our days with 1: median 4.1K vs 4.2K views [S, section 1d].
   - YouTube says there's no penalty for gaps, and it advises "a better video and fewer of them" [S].
3. **Spacing:**
   - Leave 6+ hours between two posts on the same channel, and never less than 4.
   - The NBA and soccer channels don't compete with each other. Still, post them at least 1 hour apart, so each one gets a clean log. [H]
4. **Tags aren't needed, and filling the 500 characters is wasted effort.**
   - YouTube Help: "tags play a minimal role in your video's discovery". The one exception is names people often misspell [V].
   - Ahmed's network and CoachClank used no tags when we checked earlier [S].
   - Use 3-5 tags (the player, a common misspelling, the team), about 100 characters. Or use none. Blank tags do no harm [H].
5. **The description doesn't matter for the Shorts feed. Leave it empty, or write one plain sentence.**
   - 90-97% of our views come from the feed, and search brings 1-9% [V, section 1f].
   - 4 of the 13 big channels leave the description empty. The rest range from 50 to 2,600 characters [S].
   - **Never paste a wall of tags into the description.** YouTube calls that spam [V].
6. **Use no hashtag in the title, or just one** (#nba, #football).
   - 7 of the 13 big channels use none, and 4 use exactly one [S].
   - YouTube says hashtags are "not required" [S]. They don't change reach.
7. **What this means for retention and the first hours:**
   - Posting hour didn't change "stayed to watch" for us. The median for each time block was 63-71% [S]. What changes it is the first seconds of the Short (see `Why NBA Views Dropped (Oct 26, 2026).md`).
   - A late post starts slowly. **Judge every Short at 72 hours, not at the next morning's check** [V, YouTube plus our #48].
   - **Never re-upload a Short to "try again".** YouTube may flag the channel for spam [V].
8. **A/B test for the next 2 weeks, one test per channel:**
   - **FC:** post at 12 PM vs 7 PM ET, on alternating days.
   - **NBA:** full tags vs no tags, on alternating days. The plan is at the end.

---

## 1. Our own data

### 1a. NBA: the hour we posted vs. results
These are our 34 NBA Shorts with an exact post time and Studio retention: Oct 3-13 and Oct 16-23. Six posts from Oct 14-16 have no recorded time.

| Posted (ET) | Shorts | Stayed (median) | Views (median) |
|---|---|---|---|
| 5-9 AM | 7 | 63.2% | 2.9K |
| 9 AM-noon | 6 | 70.6% | 5.3K |
| noon-5 PM | 8 | 66.0% | 3.8K |
| 5-9 PM | 9 | 71.1% | 2.9K |
| 9 PM-5 AM | 4 | 66.4% | 4.6K |

- **[S] There's no pattern by hour.**
  - Hours after 5 AM vs views: rank correlation 0.09. Hours after 5 AM vs stayed: 0.22. Both n=34.
  - Each block holds only 4-9 Shorts, so a 2x gap between blocks is still within chance.
- **[V] Stayed predicts views; the hour doesn't.** Stayed vs views: rank correlation 0.82 (n=34).
- **Sources:**
  - Times: `Posted Shorts - metrics (Oct 15, 2026, with Studio export).csv` (UTC, converted to ET) and the channel RSS feed.
  - Stayed: `Shorts Dataset.csv`.
  - Views: public counts on Oct 26, all from Shorts at least 60 h old (`Posting Study data (Oct 26, 2026).csv`).

### 1b. Same retention, different hour
Here the Shorts are grouped by how well they held, so retention doesn't hide a time effect.

| Stayed | Posted 5 AM-noon | Posted noon-5 AM |
|---|---|---|
| under 65% | 3.1K (n=6) | 1.8K (n=8) |
| 65-74% | 5.0K (n=3) | 5.0K (n=8) |
| 74%+ | 13.7K (n=4) | 23.8K (n=5) |

- **[S] Morning wins in one row, ties in one and loses in one, so time has no consistent effect.**
- **Source:** the same files as 1a.

### 1c. Day of the week
- **[S] Each weekday has only 3-7 Shorts, which is too few to call.**
  - Tuesday is the highest (14.9K median views, 74.5% stayed, n=6), because 3 of our 6 biggest new-era posts landed on Tuesdays: Flagg 21K, Bronny 23.6K, Threes 23.8K.
  - Thursday is the lowest (1.8K, n=3).
- Treat this as chance until the same day wins again.
- **Source:** `Posting Study data (Oct 26, 2026).csv`.

### 1d. Posts per day and spacing (NBA)
| Pattern | Shorts | Stayed | Views |
|---|---|---|---|
| Only post that day | 6 | 61.3% | 4.2K |
| Day with 2 posts | 22 | 71.0% | 4.1K |
| Day with 3 posts | 6 | 66.4% | 4.5K |
| 1st post of a 2+ day | 13 | 66.5% | 3.9K |
| 2nd post of a 2+ day | 13 | 70.9% | 4.3K |
| Nearest other post 0-6 h away | 7 | 69.4% | 3.2K |
| 6-12 h away | 20 | 67.3% | 4.1K |
| 12-24 h away | 7 | 63.5% | 5.0K |

- **[S] We see no sign that a second post the same day takes views from the first.** The second post did slightly better.
- **[S] There's a weak hint that posts under 6 h apart get fewer views** (3.2K vs 4.1-5.0K). But n=7, and their stayed % was higher, so it doesn't point one way.
- **[V] Re-posting the same Short isn't a fix:**
  - #40 was posted twice: 81.0% and 79.4% stayed, 1,515 vs 4,163 views (`Studio Analysis (Oct 17, 2026).md`).
  - The #25 re-post got 197 views (`Posted Tracker (Oct 21, 2026).csv`).
  - The first test audience is partly luck, and re-uploading risks a spam flag (section 3).
- **Source:** `Posting Study data (Oct 26, 2026).csv` (days counted in ET).

### 1e. FC (the soccer channel): only 6 posts
| Short | Posted (ET) | Nearest NBA post | Stayed | Views (Oct 26) |
|---|---|---|---|---|
| S01 cheat sheet | Wed 9:27 PM | 1.5 h before | 80.4% | 30,168 |
| S02 derby trouble | Thu 8:52 AM | 3.6 h after | 56.2% | 1,806 |
| S03 danced on line | Fri 12:52 PM | 5.1 h before | 64.7% | 14,513 |
| S06 5 goals | Sat 9:49 AM | 4.8 h after | not yet | 1,995 (46 h) |
| S04 sent off | Sun 11:06 AM | 2 min apart | not yet | 1,305 (17 h) |
| S07 Loch Ness | Mon 12:45 AM | 2 min apart | not yet | 527 (3 h) |

- **[S] Only 3 FC Shorts are old enough to judge, so there's no timing lesson yet.**
  - Both hits went up after noon (9:27 PM and 12:52 PM). But the topics differ, so that doesn't count.
- **[V] The FC gaps between our own posts were 11.4, 28.0, 21.0, 25.3 and 13.7 hours.**
- **[V] On Oct 25 and Oct 26, both channels went up within 2 minutes of each other.**
  - Too new to read. No source says one channel's post hurts the other's [H].
- **Sources:**
  - FC RSS feed: https://www.youtube.com/feeds/videos.xml?channel_id=UCIYlW84gYcChQtdys5L9pOg
  - Stayed: `Research Notes/Studio exports/Content 2026-10-17 to 2026-10-24 FC/Table data.csv`.

### 1f. Tags and descriptions in our data
- **[V] We can't test tags with our data.**
  - 46 of our 50 NBA upload packages carry tags: median 23 tags, about 477 characters by YouTube's count (`Productions/MetaSports/*/UPLOAD.md`).
  - Whether each set was actually pasted isn't logged. With no posts lacking tags to compare, there's nothing to test.
- **[V] Our descriptions are empty on 14 of the last 15 NBA Shorts and on all 6 FC Shorts** (RSS).
  - An earlier check on 6 channels found empty and filled descriptions get the same views relative to each channel's median: 1.00x vs 1.00x, n=344 vs 225 (`Round 6 - What Makes Shorts Go Viral (Oct 4, 2026).md`).
- **[S] Our title hashtags can't be judged either.**
  - All NBA posts since Oct 10 except two carry "#nba". Those posts were also better built (`Why NBA Views Dropped`), so the hashtag and the build can't be separated.
- **[V] Most of our views come from the feed, not search.**
  - Feed: 90.3%, 95.4% and 97.3%. Search: 8.8% and 1.3% (Oct 4 Studio screenshots, `Outcome Log.md`).
  - Search was 3.9% of views overall (`Rules Audit (Oct 14, 2026).md`).

### 1g. The first hours: how fast a Short takes off
- **[V] #48 "Most Missed Threes"** went up Tue 7:43 PM ET.
  - It got 25 views in the rest of that day, then 3,707 and 14,577 over the next two days.
  - Read at the next morning's check, it would have looked like a flop.
- **[V] #58 "Lakers Saved Bronny"** went up at 7:35 AM ET: 7,308 views on day 1, then 13,116 on day 2.
- **Source for both:** `Studio exports/Content 2026-10-17 to 2026-10-24 NBA/Chart data.csv`.
- **[V] FC S03** had 1.4K views at 10 h and 14.5K by day 3 (`Soccer Channel/Outcome Log.md`, RSS).
- **[V] Early stayed % moves too.** #22 showed 67.4% at a few hours old and 82.4% six days later (`Outcome Log.md`).
- **So:** read every Short at 72 h. YouTube's Analytics API also runs 48-72 h behind (`Discoveries (Oct 24, 2026).md`, Y1).

---

## 2. What 13 successful channels do

**Method:**
- Each channel's last 15 uploads come from its public RSS feed, which gives the exact publish time and current views.
- Each channel's last 60 Shorts titles come from `yt-dlp --flat-playlist`.
- For Chaz NBA, the channel feed showed only long videos, so I used his Shorts-only feed.
- I couldn't see anyone's tags: single-video pages ask this server to sign in.

### 2a. How often and when (ET)
| Channel (subs) | Shorts a week | Usual times (ET) | Most in a day |
|---|---|---|---|
| Swishyyy (21.3K) | ~6 | 7 AM, noon, 4 PM, on the hour | 2 |
| CoachClank (145K) | 1 in the last 14 days; 14 in Aug 1-27 | 1-2:30 AM (Aug) | 2 |
| Ahmed's Basketball (121K) | ~4 | ~7 AM, 12 PM, 5 PM, 10 PM | 3 |
| Ahmed's Goal (424K) | ~9.5 | ~2-5 AM, 11 AM, 4:40 PM | 3 |
| Hoopi (15.3K) | ~3.5 | 12-3:30 PM | 1 |
| DocBoo (28.3K) | ~6 | 5-6 AM | 2 |
| Chaz NBA (667K) | ~0.4 (mostly long videos) | 3-11 PM, some ~1 AM | 3 |
| Global Hoops (268K) | ~15 | 6, 8 and 10 AM sharp | 3 |
| Breakaway Clips (110K) | ~6.5 | 8:20-8:45 AM | 2 |
| Rebound Rewind (236K) | ~6.5 | news ~10 PM-3 AM; others 8 AM-4 PM | 2 |
| OFFTHEGLASSTV (60.9K) | ~9 | mostly 5-10 PM | 2 |
| TAT Futbol (299K) | ~2 (1 in the last 14 days) | 8 AM | 1 |
| GOATZVERSE (207K) | ~7 | 8-8:30 AM | 1 |

- **[S] Most of these channels post about once a day.**
  - The range runs from Chaz's rare Shorts to Global Hoops' 3 a day, 2 hours apart.
- **[S] The usual habit is a fixed slot, not a special hour.**
  - 6 of the 13 post almost always inside one 4-hour window: DocBoo, Global Hoops, Breakaway, TAT, GOATZVERSE, Hoopi.
  - Swishyyy and Ahmed's two channels repeat the same few slots.
  - Swishyyy and Global Hoops post exactly on the hour (13 of 15 and 14 of 15 uploads), which suggests scheduled uploads.
- **[S] 5-9 AM ET is the most common window: 64 of the 175 Shorts at least 48 h old (37%).**
  - A guess at why: it reaches Europe in the afternoon and the US before work [H].
- **[S] CoachClank paused for about 8 weeks (Aug 27 to Oct 22).** His first Short back has 40.8K views at 3.7 days, against a 203K median for his previous 14. That's n=1.
- **[S] Ahmed's network posts up to 3 a day.**
  - Ahmed's Goal: Oct 20, 21 and 25. Ahmed's Basketball: Oct 1, 8 and 20.
  - Our Oct 21 study found their medians fell when they ran about 3 a day for weeks (`Story Format Study - Ahmed (Oct 21, 2026).md`).
- **Sources:** `Posting Study data (Oct 26, 2026).csv`. The RSS links are `https://www.youtube.com/feeds/videos.xml?channel_id=` plus each channel ID in that file.

### 2b. Does the hour relate to views? (RSS views)
- **Method:**
  - Only Shorts at least 48 h old, n=175 across all 13 channels.
  - Each Short's views are divided by its own channel's median, so 1.0x is a normal Short for that channel.

| Posted (ET) | Shorts | Channels | Views vs channel median |
|---|---|---|---|
| 5-9 AM | 64 | 8 | 1.11x |
| 9 AM-noon | 17 | 7 | 0.59x |
| noon-5 PM | 39 | 8 | 1.10x |
| 5-9 PM | 23 | 7 | 1.00x |
| 9 PM-5 AM | 32 | 8 | 0.89x |

- **[S] No hour wins consistently.** Hour vs relative views: rank correlation -0.18 (n=175).
- **[S] The 9 AM-noon dip is mostly a few unusual posts:**
  - Global Hoops' third post of the day (10 AM).
  - Two off-schedule GOATZVERSE posts, during a week when the whole channel dropped.
  - Ahmed's Goal's 11 AM slot.
- **[S] Within single channels, the results point both ways:**
  - Global Hoops: 6 AM median 114K (n=5), 8 AM 57K (n=5), 10 AM 55K (n=4). But 6 AM is also its first post of the day, so the hour and the order can't be separated.
  - Swishyyy: 7-9 AM 72K (n=3), late morning to 1 PM 36K (n=4), 4 PM 37K (n=6). The 4 PM group includes its 977K hit.
  - Both Ahmed's channels did best in their afternoon slots. Ahmed's Goal's 4:40 PM posts: 2.3x (n=3). Ahmed's Basketball's noon posts: 2.4x (n=4).
  - Across channels, the correlation runs from -0.74 (DocBoo) to +0.73 (Hoopi). Both of those post inside a narrow window (5-6 AM; noon-3:30 PM), so their correlations rest on small time differences.
- **Caveats:**
  - Views were counted at different ages: correlation of age with relative views is 0.19.
  - RSS shows only the last 15 uploads.

### 2c. Titles and descriptions
| Channel | Hashtags in title | Description |
|---|---|---|
| Swishyyy | 0 | ~85 chars: title + 4 hashtags |
| CoachClank | 0 | empty |
| Ahmed's Basketball | 0 | empty |
| Ahmed's Goal | 0 | empty |
| Hoopi | 1 (#nba) | ~850 chars: written summary + hashtags |
| DocBoo | 0 | 5 hashtags only |
| Chaz NBA | 0 | ~430 chars: credit + social links |
| Global Hoops | 1 (#basketball) | one line + 3 hashtags |
| Breakaway Clips | 1 (#basketball) | one line + ~5 hashtags |
| Rebound Rewind | 1 (#nba) | the full script, ~1,400 chars |
| OFFTHEGLASSTV | 4 | empty |
| TAT Futbol | 0 | 277-1,814 chars, ~30 hashtags |
| GOATZVERSE | 0-4 (35% of titles) | ~320-char story text |
| **Us: NBA** | 1 on 30 of the last 48 | empty |
| **Us: FC** | 0 | empty |

- **[S] Hashtags in titles:**
  - 7 of 13 channels use none, and 4 use exactly one.
  - OFFTHEGLASSTV puts 4 in every title and does well anyway (341K median in its last 60), so hashtags aren't what decides results.
- **[S] Descriptions range from empty to 2,600 characters, and the big channels share no habit.**
- **[S] Tags weren't visible today.**
  - Earlier checks found no tags on Ahmed's network (`Ahmed's Network and a Second Channel (Oct 21, 2026).md`) or on CoachClank (`Round 2 - Findings So Far.md`, `MetaSports - Playbook.md`).
  - Those reads weren't repeated today.
- **Sources:** titles come from the yt-dlp flat lists of the last 60 Shorts. Descriptions come from RSS `media:description` (the last 15).

---

## 3. What YouTube itself says

**Posting time**
- **[V] Rene Ritchie, YouTube Creator Liaison, Apr 11, 2024:**
  - "The absolute best time to post your video on YouTube is when it best fits your schedule and your wellbeing ... after a couple of weeks or a month, videos tend to end up in the same place regardless of what exact hour of the day or night they were posted."
  - On news: "post as soon as you can."
  - On late posts: "if you post at off-hours, views might accumulate more slowly at first, so adjust your expectations accordingly."
  - https://blog.youtube/culture-and-trends/renes-top-five-on-youtube-april-11-2024-edition/
- **[S] Todd Sherman, Shorts product lead, Creator Insider, Aug 2023:**
  - On time of day: "It's not something that we think about optimizing for."
  - Quoted with a timestamp by OutlierKit; I couldn't play the video: https://outlierkit.com/resources/youtube-shorts-algorithm (video: https://www.youtube.com/watch?v=n3jsYK_-aRU&t=327s)
  - MediaPost's summary of the same interview: apart from breaking news, focus on what you post, not when. https://www.mediapost.com/publications/article/388588/
- **[S] Ritchie, Nov 2025, on holding a video back before publishing:** "Waiting 24 to 48 hours is no different than waiting 24 to 48 seconds or weeks or months." Relayed by https://digitrendz.blog/newswire/technology/82960/youtube-denies-24-48-hour-upload-delay-myth/

**How often to post**
- **[V] YouTube Help, Shorts upload schedule:** "A consistent, sustainable release schedule is critical when building and fulfilling audience expectations and maintaining your well-being." https://support.google.com/youtube/answer/13616979?co=YOUTUBE._YTVideoType%3Dshorts&hl=en
- **[S] Sherman, Aug 2023:** "If you generated a bunch of relatively lower quality videos and then posted those ... a better video and fewer of them." https://www.socialmediatoday.com/news/youtube-advice-for-shorts-creators-hashtags-algorithm/691835/
- **[S] Sherman, Aug 2023:** "There is nothing in our systems that's like when you hit the five video or 10 short threshold per day that you somehow unlock a secret." Via OutlierKit (above), t=345s.
- **[S] Todd Beaupré, YouTube growth and discovery, VidCon, Jun 2026, on gaps between uploads:** "We did a really deep study of millions of channels ... We found virtually no relationship." Relayed by Mashable/Yahoo: https://www.yahoo.com/entertainment/tv/articles/youtube-says-secret-success-not-230830752.html
- **[V] Oct 1, 2026:** YouTube now cuts the reach of channels "primarily aggregating or re-uploading other creators' clips without significant changes" (Creator Insider: https://www.youtube.com/watch?v=XS2A6aExLaA). Volume made by copying a template is a risk; volume alone isn't.

**Re-uploading**
- **[V] Ritchie, Apr 18, 2024**, on deleting and re-posting a Short that flopped: "YouTube might consider that as spam, and your channel could get flagged for spamming." https://blog.youtube/culture-and-trends/renes-top-five-on-youtube-april-18-2024-edition/

**Tags**
- **[V] YouTube Help, "Add tags":**
  - "Your video's title, thumbnail, and description are more important pieces of metadata for your video's discovery."
  - "Tags can be useful if the content of your video is commonly misspelled. Otherwise, tags play a minimal role in your video's discovery."
  - "Adding excessive tags to your video description is against our policies on spam, deceptive practices, and scams."
  - https://support.google.com/youtube/answer/146402?hl=en
  - The page names no character limit. The 500-character box is a Studio field limit, not a target.

**Descriptions and hashtags**
- **[V] YouTube Help, description tips:**
  - "Descriptions tell the YouTube algorithm and your viewers what the video is about."
  - Keywords "can help viewers find your videos more easily through search".
  - This is general advice, not Shorts-specific: https://support.google.com/youtube/answer/12948449?hl=en
- **[V] YouTube Help, hashtags:**
  - "up to three hashtags that are considered most engaging will appear by your video title."
  - "If a video or playlist has more than 60 hashtags, we'll ignore each hashtag on that content."
  - https://support.google.com/youtube/answer/6390658?hl=en
- **[S] Sherman, Aug 2023, on whether hashtags are needed:** "Are they required? No, of course not." They help when tied to an event or topic. Via OutlierKit (t=293s) and MediaPost (above).

**How a new Short gets tested**
- **[S] Sherman, Aug 2023:** "Sometimes those algorithms will go and effectively find a seed audience". Then it "may get a lot more traffic or it may taper off." (MediaPost, above)
- **[V] YouTube Help, Shorts analytics:**
  - "How many chose to view": "the percentage of times that viewers viewed your Shorts versus swiped away".
  - Studio now labels this "Stayed to watch".
  - https://support.google.com/youtube/answer/12942217?hl=en&co=YOUTUBE._YTVideoType%3Dshorts
- **[V] YouTube Help, Shorts discovery:**
  - "Shorts are ranked based on performance and viewer personalization."
  - "Focus on what your audience likes. If you do that and people watch, recommendations will follow."
  - The Subs tab shows "most recently uploaded Shorts" from channels the viewer follows. That's the only place an exact posting time obviously plays a part.
  - https://support.google.com/youtube/answer/11914225?co=YOUTUBE._YTVideoType%3Dshorts&hl=en
- **[S] Beaupré, Jun 2026, on subscribers:** "90% of the time, they see your video, they're not going to click on [it]." (Mashable/Yahoo, above)
  - So for us, the first audience is mostly strangers picked by interest, not subscribers who are online at that hour.

**Vendor studies (correlation only, not YouTube's own)** [H]
- **Buffer, Jul 2026 (~1.8M videos):**
  - Best Shorts slots: Friday 4-7 PM. Worst: 12-5 PM. Scored on engagement.
  - Source: `Discoveries (Oct 24, 2026).md` P1, https://buffer.com/resources/best-time-to-post-on-youtube/
  - Our own noon-5 PM posts were middling, not worst (1a). Competitors' noon-5 PM posts scored 1.10x (2b).
- **Adobe Express, May 2025 (24,274 Shorts):** 4 PM was the best hour. https://www.adobe.com/express/learn/blog/best-times-to-post-youtube-shorts
- **Metricool, Jul 2026 (799,718 videos):**
  - Views per Short peak at 2-4 uploads a week, but monthly totals keep rising with more posts.
  - Shorts with hashtags averaged about 10% fewer views.
  - https://metricool.com/youtube-trends/
- **vidIQ, Jul 2026 (10.2M channels, all formats):** channels posting 12+ times a month grew fastest. https://vidiq.com/research/youtube-upload-frequency-study

---

## 4. Two-week test plan (Tue Oct 27 to Mon Nov 9, 2026)

**Rules while testing:**
- One test per channel.
- News still goes out the morning after the game.
- Never re-upload a Short.
- Post Shorts in queue order. Don't save the best one for a slot.

### Test 1, FC: 12 PM vs 7 PM ET
- **Schedule:** odd dates (Oct 27, 29, 31, Nov 2, 4, 6, 8) at 12:00 PM ET. Even dates at 7:00 PM ET. That's 7 Shorts per slot.
- **Decision rule, set now:**
  - Move FC to 7 PM only if 7 PM wins on two counts: median stayed is 5+ points higher, and median 72-hour views are at least 1.5x.
  - Otherwise keep 12 PM.
- **Honest expectation:** a tie. With 7 Shorts per slot, this can only catch a big effect.

### Test 2, NBA: full tags vs no tags
- **Schedule:**
  - Odd dates: full tags, as now (the 490-character fill).
  - Even dates: leave the tags box empty.
  - Everything else stays the same: slot, title style, empty description.
- **Decision rule, set now:**
  - Measure "YouTube search" as a share of each Short's views at 7 days.
  - If tag days aren't 2+ points higher, cut tags to 3-5 (names and misspellings), or none.
  - Then drop the 490 fill from `.claude/skills/daily-run/SKILL.md` and `Tools/tags_fit.py`'s default. That's the owner's call.

### What to log on every post (both channels)
| What | When | Where |
|---|---|---|
| Exact publish time (ET) | automatic | channel RSS feed (the daily run can read it) |
| Test arm (12 PM / 7 PM, or tags / no tags) | at posting | Hub card note |
| Tag characters, title hashtags, description yes/no | at posting | Hub card |
| Hours since the last post on this channel, and since the other channel's nearest post | automatic | RSS |
| Copyright column clear? | 1 h | Studio |
| Views, stayed to watch % | 24 h and 72 h | Studio, Content > Shorts |
| Avg % viewed, "YouTube search" % of views, subs | 7 days | Studio, or the Sunday export |
| Views | 7 days | Studio or RSS |

**Once, this week:** screenshot Analytics > Audience > "When your viewers are on YouTube" and "Top geographies" for each channel. We have neither on file. If most FC viewers are in Europe, noon ET is already their evening.

**Where to write it:** NBA results go in `Research Notes/Outcome Log.md`, FC results in `Soccer Channel/Outcome Log.md`. Compare Shorts at the same age (72 h). A 9 PM post is only about 10 hours old at the 6:41 AM run.

---

## 5. Limits
- **Our NBA times:** 37 posts have exact times. The six posts from Oct 14-16 don't, and the 3 newest are too young for views or stayed.
- **Our NBA views:** these are public counts on Oct 26, at different ages (all at least 60 h old). The Oct 3-13 counts are rounded.
- **Competitors:**
  - RSS shows only each channel's last 15 uploads, and views were counted at different ages.
  - Channels that always post at the same hour can't show an hour effect.
- **What I couldn't see:**
  - Competitors' tags: single-video pages are blocked from this server.
  - Anyone's "stayed to watch" except ours.
  - Our audience's countries and active hours.
- **Views here are public views,** which count every replay. Engaged views, which YouTube uses for pay, are about 54% of them for us (`Shorts Mechanics and Policy (Oct 24, 2026).md`).
