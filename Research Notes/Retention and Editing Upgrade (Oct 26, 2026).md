# Retention and editing upgrade (Oct 26, 2026)

**The owner's words:** "we need to figure out the key to retention" and "find how to improve editing, it's holding us back a lot".

**Scope:** YouTube Shorts only, both channels. Nothing was posted. YouTube Studio was not opened. No tool or skill file was changed; the pipeline changes below are proposals for the session that owns `Tools/`.

**Tiers:**
- **[V]** measured (our files, our Studio exports, or an official YouTube page)
- **[S]** small sample, or seen in competitor frames
- **[H]** hypothesis

**Short source names used below:**
- **WD** = `Research Notes/Why NBA Views Dropped (Oct 26, 2026).md`
- **NEW** = new cuts computed today from `Research Notes/Shorts Dataset.csv` plus each posted Short's `shots.json` and `words.json` in `Productions/MetaSports/` (method at the end)
- **SW** = `Research Notes/Channel Study - Swishyyy (Oct 26, 2026).md`
- **NS** = `Research Notes/Niche Study - NBA Shorts (Oct 24, 2026).md`
- **R7 / R8** = `Research Notes/Round 7 - Viewer Retention Deep Dive (Oct 4, 2026).md` / `Round 8 - Editing Styles and Caption Testing (Oct 5, 2026).md`
- **FRAMES** = YouTube's auto-frames `https://i.ytimg.com/vi/<ID>/maxres1.jpg` to `maxres3.jpg` and `oar2.jpg`, pulled Oct 26 for the 55 Shorts in the appendix

---

## The key to retention (best current answer)

1. **The first few seconds decide reach.**
   - "Stayed to watch" tracks views: Spearman 0.70 (n=37). [V] WD
   - All 6 of our 10K+ new-era Shorts held 74% or more. [V] WD
   - YouTube's Shorts lead, on Shorts that flop: "the percentage of people that swiped away was just like much higher." [V, quoted by Elite Content Marketer](https://www.elitecontentmarketer.com/get-more-youtube-views-for-free)
2. **Open on one real moment and hold it.**
   - Our Shorts with 3 or fewer shots in the first 5 s held **78.4%** stayed. With 4 or more: **66.5%** (n=10 vs 27). [V] NEW
3. **Show the thing, big. Put the proof on the footage.**
   - No card: 72.6% stayed. Any card: 66.1%. [V] WD
   - The winners showed no full-screen stat card or article screenshot in any of 165 frames. [S] FRAMES
   - The closest things were Ahmed's big words over photos, and one tweet floated over a Chaz clip.
   - When they put wide footage on a blurred fill, they crop it to about 3:4, so the players stay big. [S] FRAMES
4. **Say the hook in one short line.**
   - Line 1 of 11 words or fewer: 72.6% stayed. Longer: 62.2% (n=25 vs 12). [V] NEW
5. **The subject still matters more than polish.** Editing is the gate, not the engine.
   - CoachClank's edit style is the same on its 17K Shorts and its 33M ones. [S] FRAMES
   - Our first 3 soccer stories had near-identical edit stats and held 80.4%, 64.7% and 56.2%. [S] (soccer section below)
6. **Once people stay, they mostly finish.**
   - New-era average % viewed: 92%. [V] WD
   - Our main leak is the opening, not the middle.
7. **Most "retention hacks" showed nothing in our data** (n=37, no detectable effect) [S] NEW:
   - forcing a loop
   - a sound effect at 0.0 s
   - push-ins
   - words over footage

---

## 1. What separates our high-retention Shorts (our data)

### 1a. Numbers already computed (37 posted NBA Shorts, Oct 3-23, medians) [V] WD
| Edit choice | With it | Without it |
|---|---|---|
| 2 or fewer shots in the first 3 s | 75.0% stayed, 7.8K views (n=7) | 67.5%, 3.1K (n=30) |
| No card anywhere | 72.6%, 6.1K (n=17) | 66.1%, 3.4K (n=20) |
| No card in the first 4 s | 72.0%, 5.0K (n=28) | 63.2%, 1.9K (n=9) |
| 15 shots or fewer | 75.0%, 6.1K (n=13) | 66.4%, 3.1K (n=24) |
| Average shot 1.8 s or longer | 75.0%, 4.2K (n=11) | 66.4%, 3.7K (n=26) |
| Line 1 finished by 3.0 s | 71.1% (n=23) | 62.2% (n=14) |

**No link found [V] WD:**
- speaking pace (rho 0.10)
- word count (-0.08)
- how many numbers are spoken (0.15)
- length vs stayed (-0.09)
- frame 1 a face vs an action shot (70.6% vs 68.4%)

### 1b. New cuts (same 37 Shorts) NEW
"p" is a permutation test on the difference in medians: a smaller p means the gap is less likely to be chance.

| Edit choice | With it | Without it | Read |
|---|---|---|---|
| **3 or fewer shots start in the first 5 s** | **78.4%, 6.1K (n=10)** | 66.5%, 2.9K (n=27) | **p=0.002 [V]** |
| First shot 2.0 s or longer | 77.6%, 14.2K (n=6) | 68.4%, 3.4K (n=31) | p=0.06 [S] |
| Line 1 of 11 words or fewer | 72.6%, 5.7K (n=25) | 62.2%, 2.8K (n=12) | p=0.006 [V] |
| A real-voice quote shot | 67.5% (n=14) | 71.1% (n=23) | p=0.45, no effect [S] |
| Push-in on 30%+ of shots | 74.0% (n=7) | 69.6% (n=30) | p=0.46, no effect [S] |
| Words-over-footage overlay | 71.5% (n=7) | 68.9% (n=30) | p=0.67, no effect [S] |
| Sound effect in the first 0.5 s | 66.4% (n=16) | 71.5% (n=21) | p=0.28; no gap within either build period [S] |
| Loop (last clip = first clip) | 66.2% (n=27) | 73.8% (n=10) | the gap is the build period: Oct 14-23 builds 73.7% vs 73.8% [S] |

**Rank correlations with stayed (n=37) [V] NEW:**
- shots in the first 5 s: **-0.48**
- first-shot length: +0.25
- push-in share: +0.10
- number of quote shots: -0.04

**Does it hold inside each build period?** It does for the opening (3 or fewer shots in the first 5 s) [S] NEW:
- Oct 3-13 builds: 73.2% vs 65.9% (n=2 vs 19)
- Oct 14-23 builds: 78.4% vs 71.5% (n=8 vs 7)

**Quote shots inside the Oct 3-13 builds:** 67.5% with one vs 60.4% without (n=12 vs 9). So real voices are not harmful. They are just not proven. [S] NEW

### 1c. Topic lane (39 new-era NBA Shorts, `Research Notes/Shorts Dataset.csv`) [S]
| Lane | n | Median stayed | At 74%+ |
|---|---|---|---|
| Record superlative (#42 format, records) | 6 | 78.6% | 4 |
| Human / family / lookalike | 4 | 74.9% | 2 |
| Size / curiosity | 2 | 74.4% | 2 |
| Same-day news | 3 | 71.5% | 1 |
| Contract / money | 3 | 69.4% | 1 |
| "A star did a thing" (helicopter, GTA, Vice City, rugby) | 4 | 66.1% | 0 |
| Future question / record chase | 3 | 63.7% | 0 |
| Rule / policy / technicality | 11 | 63.1% | 3 |

- **The "watchable moment" lane is untested for us.**
  - By my reading, only #49 (lookalike, 77.4%) and #63 (three technicals, 57.5%) were moments you can watch. [S] `Research Notes/Shorts Dataset.csv`
  - At Swishyyy, moments get about 1.8x an explainer's median in their newest 101 Shorts. [V] SW

### 1d. What we can't measure yet
- **Music:** every new-era NBA Short had none. [V] WD
  - All 5 old-era hits we watched had a bed. [S] WD
- **Caption style:** every new-era post used the house ALL-CAPS style. [V] `Research Notes/Shorts Dataset.csv`
- **Voice:** Alex vs the clone is confounded with time and format. No claim.

### 1e. Soccer check (n=3, Studio export Oct 17-24) [S]
| Short | Stayed | Views | Shots in first 3 s / 5 s | Card share |
|---|---|---|---|---|
| S01 cheat sheet in sock | 80.4% | 30.1K | 2 / 4 | 17% |
| S03 danced on the line | 64.7% | 1.6K (14K by Oct 26) | 2 / 4 | 6% |
| S02 trouble before a derby | 56.2% | 1.3K | 2 / 4 | 11% |

- Sources:
  - `Research Notes/Studio exports/Content 2026-10-17 to 2026-10-24 FC/Table data.csv`
  - `Soccer Channel/Outcome Log.md`
  - each Short's `shots.json` under `Soccer Channel/Productions/`
- **The edit was the same and the results weren't.**
  - The winner had the most card time.
  - What differed was the subject: one person, one trick, a singular title.

---

## 2. How the winners are edited (55 Shorts, 165 auto-frames) [S]

**What I looked at:**
- **The Shorts:**
  - 10 each from @swishyhoopz, @HoopiverseYT, @CoachClank and @AhmedsGoal: the 7 most-viewed and 3 least-viewed of each channel's newest ~120, skipping the newest 5
  - 5 Shorts of 1M+ views each from @docbooo, @ChazNBA and @breakawayclips
- **The frames:** YouTube's frames at about 25%, 50% and 75% of each Short, cropped to the vertical centre.
- **The listings:** `yt-dlp --flat-playlist`, Oct 26.

**Hard limits:**
- **Frame 1 is not visible.**
  - The cover (`oar2.jpg`) matched the 50% frame on all 55 Shorts. [V for this sample]
  - On the 5 Breakaway covers the picture is the same but squeezed sideways.
  - So nothing here says what frame 1 shows.
- **No sound.** Music, voice and real game audio are unknown.
- **Replays can't be confirmed from three stills.** "One event" below means all three frames show the same event.

### 2a. Channel by channel
| Channel (median views, Shorts read) | All 3 frames show one event | Captions |
|---|---|---|
| Swishyyy (41K, 203) | tops 5/7, lows 2/3 | white bold italic ALL CAPS, 2-3 words, mid-frame (10/10) |
| Hoopiverse (39K, 132) | tops 0/7 (themed compilations), lows 0/3 | tops: coloured lowercase mid-frame, or white CAPS lower third; lows: one word, yellow/white CAPS, lower third |
| CoachClank (511K, newest 400) | tops 4/7, lows 2/3 | small white sentence case, mid-frame (10/10) |
| Ahmed's Goal (263.5K, newest 400) | 0/10 (story montage) | small white sentence case, mid-frame (10/10) |
| DocBoo (31K, newest 400) | 2/5 (the other 3 string one star's moments from several games) | no running captions; one-word labels (ROOKIE, UNFAZED, REVENGE) |
| Chaz NBA (146K, 281) | 5/5 | one text box with the quote or the premise |
| Breakaway (147.5K, 332) | 5/5 | one joke line with 😭, the same for the whole Short |

| Channel | Graphics on screen | Framing |
|---|---|---|
| Swishyyy | one big number overlay; 0 cards | native vertical phone or creator video (9/10) |
| Hoopiverse | tops: *sound tags*, year tags, height numbers, a ✅ and a 😭 sticker; lows: red arrows (2/3), a SUBSCRIBE button + 😍 (1/3) | tops: a crop over a blurred fill; **lows: black bars (3/3)** |
| CoachClank | broadcast scorebug kept (3), *action* tags (3), 0 cards | broadcast cropped to about 3:4 over blur (3), tight crop (3), phone vertical (4) |
| Ahmed's Goal | big words over photos (FAILED TO PAY, 234 CAPS 146 GOALS, ZION) on 3 tops; a face-cam split screen on 2 (1 top, 1 low) | photos and cut-outs, full frame |
| DocBoo | *OHH YEAH*-style tags; scorebug kept (1) | broadcast in black bars, tight zoom on faces |
| Chaz NBA | a tweet screenshot (1), split-screen comparison (2) | fan phone video (3), broadcast close-up (2) |
| Breakaway | movie or meme cutaways (5/5) | phone video (5/5) |

Sources: FRAMES; listings at `https://www.youtube.com/@<handle>/shorts` (Oct 26).

### 2b. What the frames show [S]
- **No stat cards or article screenshots like ours. No emoji on a face.**
  - The closest things: Ahmed's big words over photos and club crests, and one tweet floated over a Chaz clip.
  - 0 of 165 frames had an emoji sticker on a face.
  - Emoji stickers appeared in 3 Hoopiverse Shorts. One of them is a 2.3K flop with a SUBSCRIBE graphic.
  - Breakaway puts 😭 inside the caption line instead.
- **The picture is the event.**
  - 12 of the 15 1M+ Shorts stay on one event across all three frames, sometimes with a meme cutaway. DocBoo's other 3 string one star's moments from several games.
  - The clearest same-shot cases:
    - CoachClank "6'8 vs 7'9" (33M): one broadcast shot at 25%, 50% and 75%, with the scorebug kept
    - "200 IQ Defense" (11M): the same possession at 50% and 75%
    - DocBoo "KG Finally Met His BIGGEST Fan" (5.9M): the same fan shot at 25% and 50%
- **They show the same act twice.**
  - CoachClank "He Didn't Have To Do That" (25M) shows several players doing the usual thing, then the one who didn't.
  - Swishyyy's Paul George Short (4.7M) shows the original streetball move and then the copy.
- **Wide footage is cropped, never shrunk.**
  - 0 of 55 showed a full-width 16:9 strip over a big blur.
  - When they use a blurred fill, the footage is about 3:4 to 4:5 and fills roughly 60-80% of the height (visual estimate).
- **Real sounds get named on screen.** 8 Shorts caption a sound or action in asterisks: *Laugh*, *CRYING*, *Booing himself*, *OHH YEAH*, *TROLLS ROOKIE*, *Intrusive thoughts win*, *LeCereal everywhere*, *thinks about it*.
  - 3 Chaz Shorts box the real words ("Luka: 'What'd you say…'"). The other 2 carry a premise line.
  - This suggests the real audio plays at those points. [H, can't hear]
- **Caption style is not a pattern.** The narrated hit-makers split three ways:
  - Swishyyy: bold italic CAPS
  - CoachClank and Ahmed: small white sentence case
  - Hoopiverse: coloured lowercase

### 2c. Tops vs lows on the same channel [S]
- **CoachClank:** the edit is the same; the topic differs.
  - Its lows (17-24K) are a dunking-injury montage, a jumbotron fan and a baby's first steps.
  - That matches its weak lane (wholesome fan moments). [S] NS
- **Ahmed's Goal:** the edit is the same; the name differs.
  - Tops: Ronaldo, Vinícius, Van Dijk.
  - Lows (27-43K): Blackburn players, Florin Bratu, an Ødegaard "best start?" question.
- **Swishyyy lows show edit problems as well as topic:**
  - a static wide shot with small players (5.2K)
  - a talking set-up with no action in any frame (9K)
  - a mascot compilation across arenas (1.3K)
- **Hoopiverse lows show both kinds of problem:**
  - generic hype ("the new Michael Jordan?") and news recaps
  - black bars, one-word yellow CAPS
  - red arrows and a SUBSCRIBE graphic

---

## 3. What YouTube and creators say (web, Oct 26)

### 3a. YouTube (official, or a YouTube employee on the record) [V]
- **The metric:**
  - "Stayed to watch" is "the percentage of times that viewers stayed to watch past the initial seconds of a Short."
  - YouTube publishes no threshold.
  - Sources: [YouTube Help](https://support.google.com/youtube/answer/12942217); [Prepublish summary](https://prepublish.ai/blog/viewed-vs-swiped-away-youtube-shorts)
- **How the feed decides:** in the Shorts feed the system starts the video and sees "if someone watches (retention) or leaves (swipes away)." (Rene Ritchie, [YouTube Blog, Apr 4 2024](https://blog.youtube/creator-and-artist-stories/renes-top-five-march-4-2024/))
- **Flops:** "the percentage of people that swiped away was just like much higher."
  - Todd Sherman, Creator Insider, Dec 2024 ([video](https://www.youtube.com/watch?v=_tWy-_otnUc); quote as transcribed by [Elite Content Marketer](https://www.elitecontentmarketer.com/get-more-youtube-views-for-free))
- **Length:**
  - No length gets a boost; ask how long the story needs. (Sherman, as summarised by [TechCrunch, Aug 2023](https://techcrunch.com/2023/08/25/youtube-demystifies-the-shorts-algorithm-views-and-answers-other-creator-questions/))
  - The feed groups videos of similar length. (Sherman, as reported by [PPC Land, Jan 2025](https://ppc.land/youtube-shorts-product-lead-discusses-strategy-and-metrics/); second-hand [S])
- **Loops:**
  - For very short clips, "looping is beneficial because you really need more than one watch". A 60 s video has "a beginning, a middle, and an end… and typically, you don't want to loop those quite as much." (Sherman, [The Verge, Nov 2022](https://www.theverge.com/2022/11/7/23444530/youtube-shorts-tv-app-tiktok))
  - Engaged views (the basis for pay) exclude loops. ([YouTube Help Community, Mar 26 2025](https://support.google.com/youtube/thread/333869549/a-change-to-how-we-count-views-on-shorts?hl=en); Rene Ritchie via [Podcast News Daily, Aug 2026](https://www.podcastnewsdaily.com/news/youtube-clarifies-what-counts-toward-new-creator-monetization-thresholds/article_9275daef-df2a-4924-99a6-50972dc251bb.html))
- **What it means for us:**
  - The swipe is the gate.
  - Length is free.
  - A loop adds public views but not paid ones, and only pays off on very short clips.

### 3b. Creators and analysts with numbers [S]
- **Paddy Galloway** (33 channels, 5,400 Shorts, 2023):
  - Viewed under 60% "rarely performed well"; the best were 70-90%.
  - A high viewed % didn't guarantee success.
  - Counted before the Mar 2025 view change. ([thread](https://threadreaderapp.com/thread/1646898356419981315.html))
- **Jenny Hoyos** ([Creator Science podcast, Oct 2023](https://podcast.creatorscience.com/jenny-hoyos)):
  - The average "scroll through rate" (viewed vs swiped) "is, like, 70%"; hers is about 85%.
  - Under 30 s, a Short "has to have over a 100% retention or else it's not gonna take off".
  - But one of her Shorts had "70% retention on the first 100 k views" and still reached 10M.
  - Her own channel's numbers, so opinion backed by data.
- **Hoyos's trim** (via [Elite Content Marketer](https://www.elitecontentmarketer.com/get-more-youtube-views-for-free)): she cut a final second where retention fell from 70% to 45%; retention "went from 83% to 88% and the video went flying". n=1 anecdote.
- **The hook:** "you have one second to hook someone"; her formula is shock, intrigue, satisfy. (Hoyos, [YouTube Blog, Jan 2025](https://blog.youtube/creator-and-artist-stories/youtube-shorts-deep-dive/))

### 3c. Opinion or vendor claims with no method shown [H]
- "Word-by-word captions tripled watch time" (40 Shorts, a caption-tool vendor). [VidNo](https://vidno.ai/blog/word-by-word-caption-generator-shorts)
- Karaoke captions beat block captions. [QuickReel](https://quickreel.io/blog/caption-style-ab-test-at-scale)
- 86.6% of "high performers" had animated captions (vendor, correlational). [Reviral](https://reviral.ai/blog/viral-short-form-data-report-2026)
- Seamless loops raise watch time. [vidIQ](https://vidiq.com/blog/post/double-youtube-watch-time-looping-shorts/), [Fastlane](http://www.usefastlane.ai/blog/youtube-shorts-algorithm-2026)
- **Verdict:** none of these is a test we can trust. Our own winners and our competitors' hits don't share a caption style (section 2b).

---

## 4. Editing changes, ranked by expected impact

### 1. Hold the opening moment (the 5-second rule). Impact: high. Effort: S
- **Do:**
  - Frame 1 is the event line 1 talks about.
  - Shot 1 runs 2.0 s or more.
  - 3 or fewer shots start in the first 5 s.
  - No cut inside line 1.
- **Evidence:**
  - 3 or fewer shots in 5 s: 78.4% vs 66.5%, p=0.002. [V] NEW
  - 2 or fewer in 3 s: 75.0% vs 67.5%. [V] WD
  - First shot of 2 s or more: 77.6% vs 68.4%. [S] NEW
  - #42 held one play for its first 5 s and got 84.3%. [V, n=1] `Library/THE 42 FORMAT.md`
  - 12 of the 15 1M+ Shorts stay on one event. [S] FRAMES
- **Pipeline:**
  - `Tools/qa_short.py` (NBA profile): add soft checks "4+ shots before 5.0 s" and "shot 1 under 2.0 s". Today it only counts the first 3 s.
  - `Tools/anchor_shots.py`: never place an anchor cut inside the first sentence.
  - Cuts plan: give shot 1 a `len` that covers line 1.

### 2. Replay the moment instead of cutting to filler. Impact: high to medium. Effort: S
- **Do:** show the key play again, closer and slower (and from a second angle if the source has one), under the "why" line.
- **Evidence:**
  - #42 showed one play twice in its first 5 s (0-2.7 s, then 2.7-5.2 s with a stronger push-in). [V] `Library/THE 42 FORMAT.md`
  - Swishyyy's frame sets show angles or replays of one event (52 of their 60 newest). [S] SW
  - The same act shown twice at CoachClank and Swishyyy (2b). [S]
  - No direct test of a replay exists. [H for size]
- **Pipeline:**
  - New cuts-plan key: `"replay_of": "A01"` with the existing `"zoom": 1.3` and `"speed": 0.5` (both in `Tools/broll.py cut`).
  - `Tools/cut_list.py` copies `src`/`at` from the named shot and writes `"replay": true` into `shots.json`.
  - `qa_short.py` already exempts `"replay": true` from its "footage shown twice" warning. `cut_list.py` doesn't pass that flag through today; it only copies `anchor`, `lead` and `shot_zoom`.

### 3. Fill the frame on wide plays. Impact: medium. Effort: S
- **Do:** crop wide broadcast to about 3:4 over the blur, so the play fills about 75% of the height. Don't use a full-width 16:9 strip.
- **Evidence:**
  - 0 of the 55 sampled Shorts used a full-width strip; CoachClank, Hoopiverse and DocBoo crop. [S] FRAMES
  - Our drafts, measured [V] (source sizes in `src/`):
    - #70's 1920x1080 plays render at 1080x608, which is 32% of the height
    - #69's square source renders at 56%
  - No retention data yet: blurfit is only in unposted NBA drafts. [H]
- **Pipeline:**
  - `Tools/broll.py cut --blurfit` gets a new `--blurfit-aspect 0.75`: crop the sides at `--x`, then scale to 1080 wide (1080x1440).
  - Today blurfit keeps the whole 16:9 frame, and `--zoom` crops all four edges equally.
  - Cuts-plan key: `"fit": "3:4"`.
  - QA warning when a foreground is under 55% of the height.

### 4. Proof on the footage, no cards. Impact: high (already applied). Effort: done
- **Do:**
  - Numbers go over the play with `overlay`.
  - Circle the broadcast's own scorebug.
  - No stat, article or screenshot cards.
- **Evidence:**
  - Any card: 66.1% vs 72.6%. A card in the first 4 s: 63.2% vs 72.0%. [V] WD
  - 0 full-screen cards in 165 winner frames. [S] FRAMES
- **Pipeline:**
  - Already in place: the `"overlay"` key (`Tools/overlay.py`), `broll.py circle`, and QA failing any card in the first 4 s (Oct 26).
  - Keep it.

### 5. A real-audio burst at the peak. Impact: medium (untested). Effort: S to M
- **Do:** let the crowd, the call or the player's own words play for 1-2 s while the voice stops.
- **Evidence:**
  - 11 of the 55 sampled Shorts (10 of them hits) caption a real sound or quote on screen. [S] FRAMES
  - Voice changes keep triggering attention where repeated effects fade. [Supported mechanism] R7
  - Our quote shots show no effect overall (67.5% vs 71.1%), but 67.5% vs 60.4% inside the Oct 3-13 builds. [S] NEW
- **Pipeline:**
  - Reuse `Tools/splice_voice.py`: a `{"quote": "src/<clip>.mp4", "from": x, "to": y}` piece already puts real clip audio into `voice.mp3` and `words.json`.
  - Mark that shot `"kind": "quote"` so QA checks it plays at 1.0x.
  - Today `broll.py cut` strips audio (`-an`), so there is no other route.

### 6. Slow motion and a punch-in, only on the replay. Impact: low to medium. Effort: S (exists)
- **Evidence:** push-ins on 30%+ of shots showed no effect: 74.0% vs 69.6%, p=0.46. [S] NEW
- **Do:** use them to make the replay read as a replay, not as decoration.
- **Pipeline:** the cuts-plan keys `"speed": 0.5` and `"shot_zoom": 0.08` already exist.

### 7. A freeze with a circle at the key instant. Impact: low. Effort: M. Test only
- **Do:** freeze the key frame for 0.5 s or less and circle the detail.
- **Evidence:**
  - Our old hits circled the scorebug. [S] WD
  - Red arrows show up in 2 of 3 Hoopiverse lows. [S] FRAMES
  - The signal is mixed. [H]
- **Pipeline:**
  - New `"freeze": 0.5` key (an ffmpeg `tpad` clone of the last frame) plus `broll.py circle`.
  - QA fails frozen footage over 0.6 s, so add a `"freeze": true` exemption.

### 8. A premise or quote text box for 0-3 s. Impact: unknown. Effort: S. Needs the owner's OK
- **Evidence:**
  - All 10 of the Chaz and Breakaway 1M+ Shorts carry one text box. [S] FRAMES
  - #19 (premise line) got 20.4K. [S, n=1] `Research Notes/Outcome Log.md`
  - The owner removed top text on Oct 4. `Research Notes/Lessons Learned (running log).md`
- **Pipeline:** an `"overlay"` on shot 1 with `y` about 300, `start` 0, `end` 3.

### 9. A music bed. Impact: unknown. Effort: S
- **Evidence:**
  - Unmeasurable for us: no new-era NBA Short had music. [V] WD
  - Ahmed runs a quiet bed. [S] NS
- **Pipeline:** `music.json` in `Tools/assemble.py`, at -20 LU.

### Not worth building [S]
- **Emoji-on-face stickers:** 0 of 165 winner frames.
- **A caption restyle:** the winners don't share a style.

---

## 5. What to stop doing

| Stop | Why |
|---|---|
| 4 or more shots in the first 5 s; cutting inside line 1 | 66.5% vs 78.4% stayed [V] NEW |
| Cards, article screenshots, stat panels | 66.1% vs 72.6% [V] WD |
| Opening on a reaction face or a photo when the event exists on video | Our data shows no face-vs-action gap (70.6% vs 68.4%) [V] WD, so the rule is "frame 1 = what line 1 is about" [H] |
| A full-width 16:9 strip over a big blur for plays | 0 of the 55 sampled Shorts did it; players are tiny on a phone [S] |
| Forcing the last clip to match the first (loop) | No gain within either build period; loops don't count as engaged views [S] NEW, [V] YouTube |
| A sound effect at 0.0 s as a habit | No gap within either period [S] NEW |
| Illustrative filler to meet clip-count rules | It cut away from the moment; those gates are already warnings [V] WD |
| Arrows, SUBSCRIBE graphics, emoji stickers | Seen on Hoopiverse's 2-3K flops, not on its hits [S] FRAMES |
| Retelling a moment as a montage of other clips | 12 of 15 Shorts at 1M+ stay on one event [S] FRAMES |
| Spending edit time on caption style | No pattern among winners; no test of ours yet [S] |

---

## 6. A/B tests to run next

**Rules** (from R8 and the Oct 14 "one test at a time" decision in `Research Notes/Outcome Log.md`):
- One variable per test.
- 3 pairs of comparable stories in the same lane, posted on different days at the same time.
- Read at 48 h and 7 days.
- Call a winner only if it wins on stayed % and average % viewed in 3 of 3 pairs, with a mean gap of 4 points or more.
- One pair proves nothing.

| Order | Test | Why it's next |
|---|---|---|
| 1 | Replay of the key moment (closer, 0.5x) vs no replay, in the moment lane | Untested, cheap, high upside (change 2) |
| 2 | 3:4 fill vs full-width blurfit on wide plays | #69 and #70 already use full-width strips (change 3) |
| 3 | A 1-2 s real-audio burst at the peak vs voice only | Mixed signal in our data (change 5) |
| 4 | A music bed at -20 LU vs none | Already proposed in WD; unmeasured |
| 5 | A premise text box for 0-3 s vs none | Needs the owner's OK (change 8) |

**Not an edit test, but run it alongside:** the moment lane vs the explainer lane, as about 2 posts in 3 vs 1 in 3 (SW). It's the biggest open topic question.

**Log these for every Short** (new columns for `Research Notes/Outcome Log.md`):
- shots starting in the first 5 s; first-shot length
- frame 1, in words
- replay (y/n, at which second)
- fit: full crop, 3:4, or 16:9 strip
- real-audio burst (y/n, seconds)
- music (y/n, LU)
- cards (count)
- line 1 word count and end time
- lane: moment, explainer, record or news
- stayed % at 48 h; average % viewed at 48 h
- views at 48 h and 7 days
- the second of the biggest drop on Studio's retention curve

**Target** (a goal, not a measurement): half of all NBA posts at 74%+ stayed. Today: 13 of 40. [V] WD

---

## 7. Applying it to today's two drafts [H]

**#70 Barkley:**
- Frame 1 is Chuck laughing (B01, 0-2.73 s).
- The actual moment comes later: the "Who he play for?" graphic (B02 at 2.73 s, B03 at 4.40 s), his "Chicago Bulls" answer (B04, 7.33 s) and his laugh (B05, 8.77 s).
- The graphic shots play as 1080x608 strips over blur; the answer and the laugh are full-frame crops. (`shots.json`, `cuts_plan.json`, `src/`)
- **Try:** open on the answer and his reaction, cropped 3:4 and held 2 s or more. Then replay his face-palm slowed under "and he still failed the test".

**#69 Luka (v2):**
- Frame 1 is Luka's face.
- The 52-point play arrives at 2.35 s as a square at 56% of the height.
- Three star photos follow, starting at 4.78, 6.87 and 7.56 s. (`shots.json`, `cuts_plan.json`)
- **Try:** open on one of his late threes, cropped 3:4. Replay it before "10 of 11".

---

## How the new numbers were made
- **NEW:**
  - The same 37 posted NBA Shorts and the same folder matching as WD (`Research Notes/Shorts Dataset.csv`, `Research Notes/Posted Tracker (Oct 21, 2026).csv`).
  - From each `shots.json`: shot starts, `zoom`, `kind`.
  - From `words.json`: line 1 ends at the first `.`, `?` or `!`.
  - From `sfx.json`: the first effect time.
  - Folder checks: `_splice` or `plan.json` quotes; `_ov` or `fx.json` overlays.
  - Medians compared with a 20,000-shuffle permutation test (seed 1).
  - Build periods split at Oct 13.
- **FRAMES:**
  - The 7 most-viewed and 3 least-viewed of each channel's newest ~120 Shorts (positions 6-125 in the listing). For DocBoo, Chaz and Breakaway, their 5 newest 1M+ Shorts.
  - `maxres1-3` cropped to the centre 405x720, tiled with the cover, and read by eye.
  - An automatic "sharp area" measure was tried and dropped: smooth floors and skies fooled it.
- **Correlation, not experiment.**
  - Edit choices travel with topics, and the Oct 14-23 builds also had better topics. WD
  - Views are public listing counts (lifetime, rounded).

---

## Appendix: the 55 Shorts (views from the Oct 26 listing; frames 25/50/75%)

**Swishyyy (@swishyhoopz)**
| ID | Views | What the frames show |
|---|---|---|
| d5x3OWzYXuk | 29M | creators' 100-point-shot challenge; a big "38" overlay |
| bIguG3vwyyA | 21M | giant hoop, 3 angles of one place |
| 3t8CgLqVXGo | 8.6M | signed-ball prank, selfie video |
| i1RMk1kO3fs | 7.4M | rooftop hoop, first-person view |
| 5tR4NKMv6fc | 4.7M | the streetball move, then Paul George copying it |
| M5GAyGKBYlQ | 3.9M | compilation; quotes as captions |
| 2sVHWqaKxOw | 3.7M | warm-up rim fix, fan video |
| kZyLMFJvRwc | 1.3K | mascot compilation |
| bOLdMQtQWw8 | 5.2K | one static wide angle, small players |
| zJCD7aZldrs | 9K | talking set-up, no action visible |

**Hoopiverse (@HoopiverseYT)**
| ID | Views | What the frames show |
|---|---|---|
| kSzkATMdObU | 3.8M | lookalikes; *Laugh* |
| LcjoLEAahE0 | 2.2M | Steph and his daughter; year tags |
| IRHtiCDZKvY | 1.9M | ball-spin compilation; ✅ sticker |
| M2tGuniYJEE | 1.3M | interviews, an AI-aged LeBron; *CRYING* 😭 |
| 3WqtSJ-ysx0 | 1.3M | Wemby photos; height numbers |
| 0nKK2HFhJqM | 1.3M | candid warm-up clips |
| QEHWgLfqJ5g | 1.3M | Curry, broadcast |
| FvylxxWupL8 | 2.3K | SUBSCRIBE + 😍, red arrow |
| sUmpj7Zcwfw | 2.3K | "new MJ" hype; red arrow; black bars |
| BVD17I-3HlY | 3.0K | news recap; black bars |

**CoachClank (@CoachClank)**
| ID | Views | What the frames show |
|---|---|---|
| ViynHMEfThQ | 33M | one shot at all 3 points; scorebug; quoted words |
| keHURX3t594 | 25M | the usual act, then the exception |
| P9NU5zJ7QbM | 21M | one game; scorebug |
| _2EQIFjNFoc | 12M | prank compilation |
| vtG5sL5lgXg | 11M | one hallway moment |
| dKi-JHzMpFw | 11M | the same possession at 50% and 75% |
| duwsceT6GCs | 10M | free throw, fans, Shaq |
| K0Dm027QAxY | 17K | dunk-injury montage |
| W1aPwZ4EQkw | 22K | jumbotron fan |
| hOewApOBEtE | 24K | a baby's first steps |

**Ahmed's Goal (@AhmedsGoal)**
| ID | Views | What the frames show |
|---|---|---|
| AoV5iZoZSms | 1.9M | split screen with a face-cam; "234 CAPS 146 GOALS" |
| uR2PUrwHOac | 1.9M | cut-outs; "FAILED TO PAY" |
| Q18qPxmlOQc | 1.3M | photos |
| waFSdP7r2LQ | 1.2M | cut-out, money collage, "ZION" |
| abQSSSvjf4o | 1.2M | photos plus game footage |
| wNgfPJN_rsw | 1.0M | photos |
| jwAzNLmoMIw | 958K | photos, money collage |
| pikPZztC8t0 | 27K | lesser-known players |
| ftQbprqW7Rc | 30K | face-cam split, lesser-known names |
| VEvC4nExSyM | 43K | question title, photos |

**1M+ moment Shorts**
| Channel | ID | Views | What the frames show |
|---|---|---|---|
| DocBoo | nNuQs1RSTtc | 4.9M | ROOKIE / *TROLLS ROOKIE* labels |
| DocBoo | -Sz0vn5wuAU | 2.2M | tight face zooms; scorebug |
| DocBoo | Z4CLxSYnHo0 | 1.2M | UNFAZED / REVENGE |
| DocBoo | MNa-A2EpoNU | 5.9M | fan shot twice, then KG |
| DocBoo | 6UT3SuBY_6U | 2.0M | *OHH YEAH* |
| Chaz | ijawyPTfrxY | 1.5M | one clip; "mid game btw" + tweet |
| Chaz | 6zqYJaHe06w | 1.8M | bench moment; text box |
| Chaz | lx4a-wacwok | 1.7M | Luka's quote in a red box |
| Chaz | FGFFFBB0pZU | 1.0M | close-up held; split screen |
| Chaz | vvboTeTZGmY | 1.0M | one moment; quote |
| Breakaway | EIXKT_N3sL8 | 1.3M | play + movie cutaway |
| Breakaway | zgqxs-ZnUZA | 1.1M | lookalikes + Shaq/Kobe photo |
| Breakaway | RaKs4DoP27E | 2.8M | shot + meme edit |
| Breakaway | kZ_2mVP4qQA | 6.0M | street shot + LeBron cutaway |
| Breakaway | qzM_TLfFvf8 | 1.7M | crossover + Loki cutaway |
