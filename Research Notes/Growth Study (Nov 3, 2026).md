# Growth Study: how the three feeds rank Shorts, and what we change (Nov 3, 2026)

Owner, Nov 3: "study how the algorithms work, how to properly gain views and traction, and any tips, tricks, or edits ... look at other
creator videos, transcripts, and competitors." This adds to, and does not repeat, `TikTok and Instagram Playbook (Oct 25, 2026).md`
(payouts, originality rules, posting) and `Shorts Mechanics and Policy (Oct 24, 2026).md` (YouTube's Oct 1 2026 originality change,
the 48-hour life of a Short). Tiers: **[V]** a platform employee on the record, or our own numbers; **[S]** several creators/studies agree;
**[H]** one creator or my inference.

## Sources read today
| Source (date) | Who | Used for |
|---|---|---|
| [Creator Insider: "YouTube Shorts Algorithm Explained"](https://www.youtube.com/watch?v=n3jsYK_-aRU) (Aug 2023) | Todd Sherman, YouTube Shorts product lead | YouTube mechanics [V] |
| [Creator Insider: Shorts with Jenny Hoyos and Todd Sherman](https://www.youtube.com/watch?v=_tWy-_otnUc) (Dec 2024) | YouTube + top Shorts creator | YouTube mechanics [V], craft [S] |
| [Jay Clouse: Jenny Hoyos interview](https://www.youtube.com/watch?v=As7abwNhG7Y) (Oct 2023, 5M views) | Shorts creator | scripting and editing [H/S] |
| [Build Your Tribe: Head of Instagram](https://www.youtube.com/watch?v=b_MGyd8TKdQ) (Apr 2025) | Adam Mosseri | Instagram ranking [V] |
| [Mike Yanda: new TikTok creators](https://www.youtube.com/watch?v=MGIBt_2zdaA) (Feb 2025) | TikTok coach | TikTok practice [H] |
| [Alex Hormozi: social strategy for 2026](https://www.youtube.com/watch?v=dMZ-n2KSlxE) (Oct 2025) | business creator | volume/targeting [H] (mostly about selling, little used) |
| TikTok profiles of 14 competitors via yt-dlp (today) | our measurement | cross-platform numbers [V] |
| Web check for changes since Oct 25 ([iMore](https://www.imore.com/tiktok-says-its-making-algo-changes-keep-you-pages-fresh), [ttcalculator](https://ttcalculator.net/blog/tiktok-algorithm-changes-2026/), [SocialPilot IG](https://www.socialpilot.co/?p=563048), [Creatorflow](https://creatorflow.so/blog/instagram-algorithm/), [ppc.land](https://ppc.land/youtube-creators-report-drops-in-shorts-viewership-after-september-algorithm-change/), [OutlierKit](https://outlierkit.com/resources/youtube-shorts-algorithm/)) | press and blogs | **no confirmed algorithm change on any platform since Oct 25**; blog claims marked [H] |
Transcripts (auto-captions) and the extracted claims with quotes: `Growth Study (Nov 3, 2026)/transcripts/`, `/claims/`. Two more
(Creator Insider "YouTube Algorithm 2026", Paddy Galloway's Beluga breakdown) were rate-limited by YouTube today: fetch next run.

## 1. What actually decides reach (all three feeds work the same way at the core)
- **A new video goes to a small test audience; its stay/swipe and watch behaviour decide whether it widens.** YouTube: a "seed audience" [V, Sherman 2023];
  TikTok: practitioners describe 200-300 first viewers ("200 view jail") [H]; Instagram: Trial Reels go to non-followers first [S].
- **YouTube's #1 number is "viewed vs swiped away".** Sherman (Dec 2024): when a Short fails, "the percentage of people that swiped away was just much
  higher." Hoyos: likes/comments/shares "didn't really affect video performance" on her channel; stay rate, retention and watch time did [V+S].
  Matches our own data (stayed vs views, rank correlation 0.82, Posting Study) [V].
- **YouTube adjusts for length, and asks viewers if they valued it.** "Independent of duration figure out if somebody really enjoyed the video ... normalise
  for duration"; "did they value it afterwards?" (surveys) [V, Dec 2024]. So a longer Short is not punished for a lower %, and clickbait that disappoints is.
- **YouTube groups fast punchy Shorts and slower longer ones in the feed** ("coherence around the Feed") [V, Dec 2024]. A channel that is consistent in pace
  is easier to place.
- **Instagram's top signals: DM sends and watch time**; total watch time counts, so longer videos aren't penalised for a lower % [V, Mosseri Apr 2025].
  Instagram reads the **caption most heavily** to understand a Reel ("disproportionately looking at the caption relative to the video relative to the audio") [V].
  **Hashtags are "not an important thing for reach"** [V]. Originals are swapped in ahead of aggregator re-posts [V].
- **Myths the platforms deny [V]:** posting time (YouTube: "No, it's not something that we think about optimizing for"; matches our Posting Study);
  a daily-volume threshold that "unlocks" reach; custom thumbnails mattering for Shorts reach (feed traffic is ~all of it); replying to DMs to boost a post;
  Instagram suppressing reach to sell ads. **Deleting and re-posting a flop risks being "seen as spam"** (Sherman) [V]: our rule already forbids it.

## 2. Craft that the evidence supports (hooks, scripts, edits)
- **One second to hook, and the first frame must make sense with the sound off** (Hoyos 2023 and 2024; Yanda) [S]. We already require frame 1 = the moment
  line 1 is about.
- **Hook + foreshadow inside 3 s**: line 1 = the shock/situation, line 2 = what this will be about or how it ends (Hoyos: "a hook and then I foreshadow ...
  two lines ... 3 seconds or less") [S]. Our hooks are mostly one line; the foreshadow is often missing.
- **"But / therefore", not "and then"** between beats (Hoyos) [S]; this is our "turn every 8-12 s" rule said another way.
- **Write the last line first** so the ending lands and loops (Hoyos) [S]; we already end on the payoff.
- **Simple words: about a 5th-grade reading level** (Hoyos runs every script through a readability checker; one jargon word moved hers from grade 5 to 8) [H].
  Not checked by our tools today: **added to `script_lint.py`** (below).
- **Cut the dead last second**: one second of silence at the end took a Short from 83% to 88% retention (Hoyos) [H]; our QA already checks "sound has died
  away" and nothing after the payoff.
- **No call to action at the end; end abruptly** (Yanda; our rule) [S].
- **Keyword in the first seconds, on screen and in the caption** for TikTok search (Yanda) [H]: our captions are burned in, and line 1 names the star.

## 3. What competitors show on TikTok (measured today, last 30 posts each)
| Creator | YouTube median (our watchlist) | TikTok median | TikTok length |
|---|---|---|---|
| Ahmed's Goal | 137.5K | 64.3K (0.47x) | 70 s median, 29/30 over 60 s |
| Ahmed's Basketball | 74K | 18.0K (0.24x) | 72 s, 30/30 over 60 s |
| Ahmed's Business | n/a | 10.4K (max 1.2M) | 79 s, 30/30 over 60 s |
| ChazNBA | 198.5K | 21.2K (0.11x) | 21 s |
| Hoopiverse | 77K | 189 (abandoned) | 58 s |
| NBA (league) / House of Highlights | n/a | 84K / 144K | 12-13 s raw clips |
Raw data: `Growth Study (Nov 3, 2026)/tiktok_competitors.tsv`. CoachClank, Swishyhoopz, breakawayclips and roycebball have no usable TikTok.
- **[V] For sports-story creators, TikTok is a 0.1-0.5x add-on to YouTube, not a second main stage.** Cross-posting the same file is worth it because it costs
  nothing; building TikTok-only edits is not, until the numbers say so.
- **[V] Ahmed makes every TikTok version just over 60 s.** TikTok's Creator Rewards only pay for videos over 1 minute (Oct 25 Playbook). Our Shorts are 17-59 s, so
  they will earn nothing on TikTok as they are; that only matters after 10K followers (CRP entry), so it's a later decision.
- **[V] Highlight accounts win TikTok with 12-13 s raw clips**; that's the league's own lane. Our edge is the story, so we don't copy it.

## 4. What we change now (done today unless marked)
1. **Cross-post captions lead with the keywords and use the Short's own tags as hashtags** (Instagram reads the caption most; TikTok search uses it).
   `Tools/crosspost.py`: caption = title + question, then 3 hashtags from the card's own tags (e.g. #dennisrodman #mavericks) + 1 channel tag, instead of
   the same 4 generic tags on every post. Hashtags are kept few: Instagram says they hardly matter.
2. **Readability check in `script_lint.py`**: flags a script above about grade 6 (Flesch-Kincaid) and lists its longest words, so a jargon word gets swapped
   for a plain one before voicing.
3. **Hook + foreshadow** becomes a script check to try (not yet a rule): line 2 tells the viewer what the ending will be about. To test on 4+ Shorts, judged at 72 h.
4. **Experiment (one variable): NBA length 30-35 s vs our usual 18-25 s.** Hoyos [H] says under 30 s needs 100%+ retention to take off; YouTube says it
   normalises for length [V]. Our data: 20-30 s = 1.11x median (n=25), 30-45 s n=1 (a guess). Log `length` in Experiments.csv; decide after 4 each.
5. **TikTok: 1-3 posts a day, no time-of-day fuss, reply to early comments** [H/S]; posting time doesn't matter on any platform [V].
6. **Later (owner):** TikTok 60 s+ versions for Creator Rewards once an account is near 10K followers; Instagram Trial Reels to test hooks on non-followers.

## 5. What I'd ignore
- "Post 5+ a day to unlock the algorithm" (YouTube: no such threshold [V]). "Post-and-ghost" / "engage before posting" tricks (TikTok coach and Mosseri both: no effect).
- Blog numbers like "sends are worth 3-5x likes" or "originals get 40-60% more reach": no primary source (Instagram never published a multiplier).
- Hormozi's volume-funnel advice: it's for selling a business, not for a story channel.
