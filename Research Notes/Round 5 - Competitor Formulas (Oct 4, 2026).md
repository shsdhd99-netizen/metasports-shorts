# Round 5: What the winners do, and what we should add (Oct 4, 2026)

*Cloud session. Goal: learn how to make the most viral Short possible, not just copy one channel. Evidence labels used everywhere below:*
- **PROVEN** = official YouTube statement, or numbers I computed today from public channel data (observational, so "proven" means "the pattern is really in the data", not "it causes views").
- **SUPPORTED** = several credible sources, or our own earlier measurements on a small sample.
- **HYPOTHESIS** = plausible, comes from vendor blogs or my reading of frames, needs an A/B test.

*Data pulled today: yt-dlp public listings plus per-video metadata (views, duration, upload date, likes, comments, title) for 6 channels, 570 Shorts. Cover frames of ~30 top Shorts viewed by eye. vidIQ has 4 credits left (a call costs 5), so it was not used. YouTube downloads are blocked, so I could not watch or hear any Short. Anything about audio, music or animation of a competitor is therefore unverified.*

---

## 0. Read this first: where earlier notes lacked evidence

| Earlier claim in our repo | Status |
|---|---|
| "Post 6-11 AM ET" (Round 3) | Only observational, from CoachClank's own history, not controlled for topic. YouTube's Shorts lead says creators "should not worry about when they post as much as what they post" except for breaking news ([MediaPost](https://www.mediapost.com/publications/article/388588/youtube-shorts-product-lead-offers-insights-for-creators-and-brands/)). Keep as a cheap habit, label HYPOTHESIS. |
| "Average shot <= 1.9 s" gate | **No evidence found that faster is better.** Round 3 measured CoachClank's biggest Shorts at a new shot every 2.0-4.7 s. Our gate is faster than the channel we copy. One vendor says under 1.2 s "reads as noise" ([aibrify](https://aibrify.com/blog/youtube-shorts-retention-curve-playbook), vendor blog, HYPOTHESIS). Needs an A/B test. |
| "Boom sound on the hook word" | No evidence anywhere. Already removed in Round 4. |
| "Swipe-away under 25-30% in 3 s", "70-90% Viewed is best" | The 70-90% band is real but comes from one study (Paddy Galloway, 33 channels, 5,400 Shorts, Apr 2023, [thread](https://threadreaderapp.com/thread/1646898356419981315.html)), before the Mar 2025 view-count change. The 25-30% figure is from vendor blogs. Use as a yardstick, not a law. |
| "Never post 3 a day" | Based on n=3 days. Not evidence. |
| Round 4: "emoji 🤔 worst" | n=5. Too small to act on. |
| Contracts/trades are a weak lane | SUPPORTED (Ahmed's contract Shorts flat; Clank's bottom 15 are wholesome fan stories, see section 2). Not tested on our own channel yet. |
| Round 2 listed ItsBobbyFinn, NBA Storytime, Hoops Stories as "other AI NBA story channels" | **Wrong.** Titles pulled today show Bobby Finn is a general "that's why" comedy channel (top Short is about English spelling, 11M), NBA Storytime posts cat and funny-clip stories ("She mistakenly stepped on her cat"), Hoops Stories posts France/geography news. Do not use their numbers as NBA benchmarks. |
| REBOUND benchmark (775K median) | The 59 Shorts yt-dlp returns are dated Apr 2022 to Jul 2023, not recent. Fine for topic lanes, not for current style. |

---

## 1. Channel table (what each does, measured today)

Median and top-10% from the last 59-150 Shorts the public tab returns. "Top 10%" = the best tenth of that sample (n shown). Likes per 1,000 views are almost identical for top and rest in every channel, so engagement rate does not separate winners.

| Channel (subs) | n | Median views | Top 10% median | Cadence in sample | Typical length | Title style | Caption style seen in cover frames | Lane / format |
|---|---|---|---|---|---|---|---|---|
| **CoachClank** (145K) | 145 | 421K | 10.7M (n=14) | 5.9/wk | top 10% median 22 s vs rest 19 s; 21-30 s bucket 848K vs <=20 s 291K | 2-6 words, no hashtag, 64% have emoji, empty description | white, sentence case, medium-bold sans, ~3-4 words, centred at ~50% height, thin shadow, 16:9 footage on blurred 9:16 | one-second oddities, size gaps, "200 IQ", petty/funny players, rules |
| **REBOUND** (3.4M, old sample) | 59 | 775K | 28.1M (n=5) | 0.9/wk | top 53 s vs rest 35 s | ALL-CAPS word + ".." ("NBA Players CAUGHT CHEATING..", "3 NBA Rules You Didn't Know Exist..") | lowercase bold, one word at a time, centred, green highlight on key word, thick black outline | rules, bans, "caught", lists of 3 |
| **Courtside Films** (804K) | 100 | 266K | 4.4M (n=10) | 1.3/wk | ~65 s, no length effect | "TOP 10 ... OF ALL-TIME!", digits in 80% of top titles | no word captions; the title sits on screen as a static bold caps block for the whole video | countdown compilations, dunks, high school |
| **Ahmed's Basketball** (121K) | 99 | 87K | 456K (n=9) | 11.9/wk | ~69 s | 10 words, no emoji, sentence like "NBA teams that spent everything to keep their star but lost him anyway" | white sentence case, centred ~50%, thin, same as Clank; AI-style images mixed with archive photos | list stories "players who..." |
| **Hoop Facts** (51K) | 100 | 42K | 473K (n=10) | 4.3/wk | top 10% median 57 s vs rest 60 s: length did not matter, but its two biggest are 15-20 s | 80% carry "#nba" in the title | ALL CAPS, 1-3 words, white with yellow on the key number or name, ~50% height | fact lists, "When The Spurs Memed Shaq" (2.3M, 19 s) |
| **Hoops Lore** (16K) | 66 | 36K | 2.3M (n=6) | 1.8/wk | top 10% 82 s vs rest 64 s | very long (14-15 words), interview quote + question + emoji | ALL CAPS, 2-3 words, white/orange with brown outline, channel watermark under it | reposted podcast/interview clips with story titles ("Iman Shumpert details the fight between Carmelo and KG", 9.3M) |

Notes:
- The top tenth of every channel is 5x to 63x its own median. The top 10% of a channel differs from its median mainly in **topic and concept**, not in length, caption look or posting rate (cadence: Ahmed's posts twice as often as Clank and has one fifth of the median).
- Hoops Lore's hits are other people's long interviews cut down. That is exactly the "reused content" shape YouTube's policy targets, so I do not recommend copying it.

---

## 2. What separates a channel's top 10% from its median (computed today)

Pooled across the 6 channels with each Short's views divided by its own channel's median (so channel size cancels). n = Shorts with the feature; "vs" = everything else.

| Feature | Relative views (with vs without) | n | Label |
|---|---|---|---|
| Title about a **rule / ban / illegal / cheat / caught / unwritten** | **2.49x vs 0.98x** | 26 | PROVEN (pattern), mostly REBOUND; matches Round 4 |
| Title starts with Why / How / What / Did / Is / Does / Can | **1.64x vs 1.00x** | 28 | PROVEN (pattern) |
| Title contains "IQ" (Clank) | 2.22x | 8 | small n |
| Title starts He / She / They | 1.23x | 21 | small n; in Clank alone He-titles 632K vs 420K (n=18) |
| Title 5-7 words | 1.21x vs 0.95x | 262 | PROVEN (pattern) |
| Any emoji | 1.10x vs 0.98x | 189 | weak |
| Contains a digit | 1.04x vs 1.00x | 124 | no effect |
| Hashtag in title | 0.99x vs 1.00x | 133 | no effect; we already use none |
| Empty description | 1.00x vs 1.00x | 344 | no effect; we already use none |
| Question mark | 0.95x vs 1.01x | 83 | no effect (Clank alone 276K vs 481K, n=16: worse) |
| "vs" in title | 0.72x | 20 | negative, except Clank's one 30M hit |
| Length <=20 s | 0.83x vs 1.03x | 113 | PROVEN (pooled) |
| Length 21-34 s | 1.06x | 103 | PROVEN (pooled) |
| Length 35-60 s | 0.83x | 119 | confounded by channel mix, ignore |

CoachClank only (n=148, I read the whole top 25 and bottom 15):
- **Title opens with a player name:** 237K vs 494K median (n=20). Top titles open on an action or a claim: "He Didn't Have To Do That", "He Was Playing By Himself", "Why No One Shoots Underhand", "Missing a Free Throw on Purpose?". **Our own `/cloud-short` skill says titles should start with "a question, number or name". Name-first is the weakest Clank pattern. HYPOTHESIS to test.**
- **💀 in title:** median 7.7M vs 0.4M (n=9, driven by a few hits). 😭 shows no lift (401K vs 477K, n=15).
- **Top 25:** every one is a concept you understand in one second (size gap, a trick, a rule, a petty act). **Bottom 15 (8K-42K):** generic wholesome or fan stories ("Baby Takes Her First Steps at a Game", "Crowd Cheers for Fan", "Nicest NBA Player Ever", "Fan Thinks He Won $10,000!") and a vague "Worst Referee Mistake Ever". Specific weird beats generic nice.
- **Length:** <=20 s 291K (n=82), 21-30 s 848K (n=52), 31-45 s 999K (n=9), 46-61 s 5.9M (n=2). Same direction as Round 3.
- **Comments per 1,000 views:** top 10% 0.06 vs rest 0.16; likes per 1,000 equal (13.1 vs 12.9). Comments do not drive reach (Galloway also found no strong link for likes, shares or comments).

---

## 3. The winning formulas (ranked by how much evidence they have)

1. **Pick the right idea (biggest lever).** Rules, bans, "caught", size gaps, tricks and 1-second oddities beat everything else; generic nice-guy and fan stories are the floor. PROVEN (above) and echoed by vendor lists of viral sports hooks (rule-because-of-one-player, stats fans can argue about; [air.io](https://air.io/en/youtube-hacks/13-types-of-shorts-that-always-go-viral-with-examples), SUPPORTED).
2. **A title that states the weird thing in 5-7 words, opening on an action or "Why/How/What/Did".** PROVEN (pattern).
3. **Stay watched, not just opened.** YouTube's own Studio now reports "Viewed vs swiped away" and "shown in feed" ([YouTube Help](https://support.google.com/youtube/answer/12942217)); the study behind the 70-90% band is Galloway's ([thread](https://threadreaderapp.com/thread/1646898356419981315.html)). Since 31 Mar 2025 a Short counts a view the moment it starts or replays, so a loop adds a view (TubeBuddy/Sam Proof coverage, [TubeBuddy](https://www.tubebuddy.com/blog/youtube-shorts-view-count-update-what-creators-need-to-know-about-the-new-metrics/)); retention and average view duration still use "engaged views" and monetisation still uses engaged views. SUPPORTED.
4. **Length 21-45 s for stories.** PROVEN for Clank; Galloway found longer Shorts with high average view duration did better (AVD over 50 s averaged 4.1M views; SUPPORTED); YouTube's lead says "no ideal length, storytelling over duration".
5. **Explore, then exploit.** New Shorts go to a small test audience first and are widened only if viewers stay, replay or share (Creator Insider coverage: [vidIQ](https://vidiq.com/blog/post/youtube-shorts-algorithm/) (blocked from here, quoted via search snippet), [Search Engine Journal](https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/)). Consequence: the first 1-3 seconds and the idea decide everything; a flop is cheap, a hit compounds. SUPPORTED.
6. **Consistency, not volume.** Clank 5.9/wk with 421K median; Ahmed's 11.9/wk with 87K median. YouTube: "no magical threshold of posts" ([SEJ](https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/)). PROVEN that more posting did not buy a higher median here.
7. **Original value per Short, varied structure.** YouTube renamed "repetitious" to "inauthentic content" on 15 Jul 2025; mass-produced template videos risk demonetisation; AI narration alone is allowed ([TechCrunch Jul 2026](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/), [YouTube Help](https://support.google.com/youtube/answer/1311392), both in Sources.md). PROVEN (official).
8. **Series.** YouTube announced "Shorts series" (seasons, episodes, a Watch Series button in the feed) on 23 Sep 2026, rolling out to YouTube Partner Program channels ([TechCrunch](https://techcrunch.com/2026/09/23/youtubes-new-short-series-feature-brings-episodic-viewing-to-shorts/)). We are probably not in YPP yet; repeatable formats still help (HYPOTHESIS).
9. **Things that do NOT matter much (and what we already do right):** hashtags are not required (YouTube lead, SEJ link above; our data: no effect), descriptions (no effect), custom thumbnails (the Shorts feed does not use them; they matter on the channel page and in search, per the same interview), likes/comments (no relationship with reach in Galloway or in our data).

Cross-niche check (SUPPORTED only, vendor lists, I did not pull their numbers): the big faceless Shorts channels (Zack D. Films 27.6M subs, Daily Dose of Internet, Scary Pumpkin, MagnatesMedia; [fliki](https://fliki.ai/blog/best-faceless-youtube-niches)) share three things with Clank: one-idea-per-video, a voice that keeps going without throat-clearing, and a repeatable format. I did not measure them.

---

## 4. Caption evaluation and recommendation

### What I saw (cover frames of the top Shorts, six channels; one frame each, so animation is NOT verified)
| Channel | Case | Weight | Words shown | Height | Colour | Notes |
|---|---|---|---|---|---|---|
| CoachClank | sentence | semibold | 3-4 | ~50% | white, thin shadow | calm, no emphasis |
| Ahmed's | sentence | regular | 3-5 | ~50% | white | same as Clank |
| REBOUND | lowercase | heavy | **1** | ~48% | white + **green on one word**, thick black outline | word-by-word |
| Hoop Facts | CAPS | heavy | 1-3 | ~50% | white + **yellow on key word/number** | |
| Hoops Lore | CAPS | heavy | 2-3 | ~50% | white/orange, brown outline | watermark below |
| Courtside | CAPS | bold | whole title | ~55% | white, thin outline | static title, not captions |

Our MetaSports style (ALL CAPS, Montserrat Black 86, thick stroke, red/green by card, 62% down) matches none of the sentence-case winners; it is closest to Hoop Facts / Hoops Lore (median 42K / 36K).

### Evidence on caption style (honest)
- No competitor has tested styles, and their numbers are confounded by topic. **No evidence anywhere that a caption style causes views here.** The most I can say: the two highest-median NBA channels (Clank, REBOUND) both use sentence-case or lowercase, centred at about half height, with REBOUND adding word-by-word highlight.
- All-caps text reads ~12-20% slower in controlled reading studies ([sitelint summary](https://www.sitelint.com/blog/should-we-avoid-writing-in-all-caps), [ERIC study](https://files.eric.ed.gov/fulltext/EJ1204569.pdf)). PROVEN for reading speed; effect on retention is HYPOTHESIS.
- Vendor guidance (low quality, no methods): bold sans, 64-88 px at 1080 wide, white with 2-4 px black stroke, one highlight colour (yellow), centred 55-78% down, active-word highlight "dominant in 2026" ([blitzcut](https://blitzcutai.com/blog/best-caption-style-youtube-shorts-2026), [emax](https://emax.studio/blog/word-by-word-ai-captions-vs-static-subtitles)). The "12-15% higher completion with captions" figure traces to an OpusClip statistic with no stated method. HYPOTHESIS.

### Recommendation: new style `karaoke` (built, not yet A/B tested)
Keep what the winners share, add the one thing REBOUND/Hoop Facts add, drop what nobody top uses.
- Font: Montserrat Bold (already in `Tools/fonts`), **80 px** on 1080x1920, sentence case.
- Stroke: black **6 px**, soft shadow 2, white fill.
- Words per card: **2-3**, max 22 characters, breaks at phrase boundaries (reuses our existing chunker).
- Highlight: the word being spoken turns **yellow (#FFD60A)**, any number or money figure turns **green**. No red. One accent colour keeps it readable.
- Position: centred at **54% of height** (y=1040 of 1920). Clank/REBOUND sit at about 50%; 54% clears the YouTube bottom UI.
- Animation: no scale-pop (the position and width never move, so the eye is not jerked); only the colour steps from word to word.
- Keep our rule: hand-picked emphasis words are not needed.

**Test render (scratch, not in the repo):** a 6-second clip of the Kawhi Short with the new captions: `/tmp/claude-0/-home-user-metasports-shorts/bc228739-3662-5759-8934-674d6d03bfcf/scratchpad/r5/test/test_karaoke_6s.mp4`, three stills `kk.jpg`, and a side-by-side of the three styles `cmp.jpg` in the same folder. In the stills "Brandon Ingram," shows "Brandon" in yellow, "Gradey Dick," shows "Gradey" yellow, "two unprotected firsts," shows "unprotected" yellow; text stays put as the highlight moves. The white-wall photo background showed that the 6 px stroke keeps white words readable.

Code: `Tools/captions.py` has a new `karaoke` entry in `STYLES` (existing `metasports` and `clank` are untouched); `python Tools/assemble.py --folder ... --caption-style karaoke` uses it. One ASS event is written per word.

**A/B plan:** post two similar-lane Shorts (same length band, same posting slot), one `clank`, one `karaoke`, repeat 3 times; compare "Viewed vs swiped away" at 24 h and average percentage viewed. Do not decide from one pair.

---

## 5. 15 checklist rules we do NOT already follow (ranked)

Ranking = evidence strength x expected impact x how easily `Tools/qa_short.py` can measure it. "QA" says how.

| # | Rule | Evidence | QA measurement |
|---|---|---|---|
| 1 | **Lane gate.** Every Short is one of: rule/ban/"caught", size/skill spectacle, one-second oddity, petty/funny player moment. Contract/trade, generic wholesome or fan-interaction stories are blocked unless a rule or number gap is the hook. | PROVEN: rule/ban titles 2.49x (n=26); Clank bottom 15 are generic wholesome/fan stories | notes.md must have `Lane:` from the allowed list; qa fails if missing or "contract/trade/wholesome" |
| 2 | **One-second concept test.** The title and the first spoken sentence both state the weird thing; a stranger gets it in one second. Write the concept in 8 words or fewer in notes.md (`Concept:`). | PROVEN (pattern): Clank top 25 vs bottom 15 | notes.md `Concept:` present and <=8 words; title 5-7 words (qa reads UPLOAD.md) |
| 3 | **Title opens on an action/claim word, not a player name**: He / Why / How / What / Did / Is / "Missing", etc. Name-first titles only with a test. | PROVEN (pattern): Clank name-first 237K vs 494K (n=20); starter words 1.64x (n=28). HYPOTHESIS that it causes views | qa: first word of chosen title not a capitalised proper noun; warn if so |
| 4 | **Story Shorts are at least 21 s** (quick moments flagged `kind: moment` may be 15-20 s). Today the gate accepts 18 s. | PROVEN for Clank (<=20 s 291K vs 21-45 s 848K-999K); pooled 0.83x | qa: length >= 21 unless notes has `Format: moment` |
| 5 | **Speech pace 240-290 words/min** counted from words.json. | SUPPORTED: Round 3 measured 247-289 wpm on Clank's 8 biggest (n=8) | qa: words / duration x 60 in range, warn otherwise |
| 6 | **Ends on the payoff, no outro.** Last 6 spoken words contain none of: subscribe, follow, like, comment, "thanks for watching", "let me know". | SUPPORTED: Clank ends on payoff and stops (Round 2 frame watches); no Short in top 25 has a CTA in the title | qa: regex on last words |
| 7 | **Loop audio and visual.** Last word ends 0.15-0.4 s before the last frame (no dead tail), the last shot is the first clip (exists), and the final sentence reads naturally into the first. | SUPPORTED: loops raise replays; views count per replay since Mar 2025 (TubeBuddy); retention above 100% case studies are vendor ([vidIQ](https://vidiq.com/blog/post/double-youtube-watch-time-looping-shorts/)) | qa: video duration minus last word end in 0.15-0.40 s |
| 8 | **Caption standard.** Sentence case (no ALL CAPS body), size >= 64 px, centre between 45% and 62% of height, <=3-4 words per card, no card on screen over 1.7 s, first caption starts <= 0.2 s (works on mute). | SUPPORTED: observed on Clank/Ahmed/REBOUND; reading-speed research; mute viewing HYPOTHESIS | qa: parse captions.ass (style size, \pos y, text case, event durations) |
| 9 | **One accent colour.** At most one highlight colour for words (yellow) plus green for numbers; no red/green by card. | HYPOTHESIS: REBOUND and Hoop Facts use one accent; vendor guidance says avoid red/green | qa: count distinct \c colours in captions.ass |
| 10 | **Turn inside the first 40% of the words** ("But", "However", "You see", "Until", "Except", "The catch"). | SUPPORTED: Round 3 measured turns in the first 10-40% (n=8) | qa: regex position over words.json |
| 11 | **Search keyword in the first 15 spoken words and in the title** (the player or rule name people search). | HYPOTHESIS: YouTube indexes speech and on-screen text for Shorts per vendor blogs ([miraflow](https://miraflow.ai/blog/youtube-shorts-seo-2026-how-to-rank-shorts-in-search)); search is a minority source (~9-26% depending on source) | qa: title keyword appears in first 15 words |
| 12 | **Original-value line recorded.** notes.md has `Added value:` (our opinion line, a verified number, or a transformed comparison) and a source URL per number. Rotate structure: no more than 2 Shorts in a row with the same opener type or the same shot-count signature. | PROVEN (official policy: inauthentic content) | qa: notes.md field present; compare opener type of last 3 Shorts folders |
| 13 | **Cut-rate floor.** Add a lower bound to the pace gate: average shot >= 1.3 s, and run the 1.9-vs-2.8 s A/B (see section 6) before treating fast as good. | HYPOTHESIS: Clank's biggest Shorts cut every 2.0-4.7 s; a vendor says under 1.2 s is noise | qa: average shot >= 1.3 s (warn) |
| 14 | **Frame 0 is the cover.** The Shorts feed does not show custom thumbnails, so spend no more than 5 minutes on covers; instead check that frame 0 is a face or moving action, not a card, logo or flat colour. | PROVEN (official interview: no thumbnails in the feed); frame check HYPOTHESIS | qa: frame at 0.0 s not near-uniform (pixel std dev above a threshold) and first shot kind is action/face |
| 15 | **Series tag.** Every Short belongs to a named repeatable format (e.g. "Rule Nobody Explained #n", "Size Gap", "200 IQ") recorded as `Series:` in notes.md; at least 3 of every 5 Shorts in a named format so we can use Shorts series when YPP arrives. | HYPOTHESIS; official feature exists since 23 Sep 2026 (TechCrunch) | qa: notes.md field present |

Not added because already followed: no hashtags, no description, voice at 0.0-0.4 s, no filler first word, 3+ shots in 3 s, action in 3 s, loop clip, -14 LUFS, copy-check.

---

## 6. A/B tests to run (one variable, 3 repeats, read at 24 h)

| Test | A | B | Metric |
|---|---|---|---|
| Captions | `clank` (white sentence case) | `karaoke` (yellow active word) | Viewed vs swiped away; average % viewed |
| Title opener | name first ("LeBron Took ...") | action/claim first ("He Took ...") | views at 48 h; impressions to views |
| Lane | rule/ban/oddity | contract/trade | views at 48 h vs channel median |
| Cut rate | average shot 1.9 s | average shot 2.8 s | average % viewed; swiped away |
| Loop tail | 0.15-0.4 s tail + echo line | current ending | average % viewed (above 100% = loop working), replays |
| Hook headline | `--hook-text` on | off | Viewed vs swiped away |
| Length | 22-28 s | 32-40 s | average % viewed and views |
| Post time | 6-11 AM ET | evening | views at 48 h (low priority; YouTube says it matters little) |

---

## 7. Checklist additions (paste into `.claude/skills/cloud-short/SKILL.md` and `Tools/qa_short.py` when approved)

```markdown
### Round 5 checklist additions (Oct 4, 2026)

TIER A - PROVEN (official source or our own data pulled Oct 4)
- [ ] Lane: rule/ban/"caught", size/skill spectacle, one-second oddity, or petty/funny moment. Block contract/trade/wholesome-fan unless a rule or number gap is the hook. (notes.md "Lane:")
- [ ] Concept in 8 words or fewer, understood in one second. (notes.md "Concept:")
- [ ] Title 5-7 words, opens on an action/claim or Why/How/What/Did/Is, not a player name. No hashtags, no description.
- [ ] Story length >= 21 s (quick moment 15-20 s only if notes say "Format: moment"); never over 60 s.
- [ ] notes.md has "Added value:" (our opinion line or verified number) and a source URL per number; rotate opener type and structure (inauthentic-content policy).
- [ ] Do not spend time on covers for the Shorts feed; frame 0 must be a face or moving action.

TIER B - SUPPORTED (several sources or small own measurements)
- [ ] Speech pace 240-290 words/min.
- [ ] Ends on the payoff; no "subscribe/follow/like/comment" in the last 6 words.
- [ ] Loop: last word ends 0.15-0.4 s before the end; last shot = first clip; last line echoes the first.
- [ ] Turn ("But/However/You see/Until") in the first 40% of words.
- [ ] Captions: sentence case, >= 64 px, centred 45-62% of height, <= 3-4 words per card, none over 1.7 s, first caption <= 0.2 s.

TIER C - HYPOTHESIS (test before treating as rules)
- [ ] One accent colour (yellow active word, green numbers) instead of red/green by card (style `karaoke`).
- [ ] Average shot >= 1.3 s floor; test 1.9 s vs 2.8 s.
- [ ] Title keyword (player/rule) in the first 15 spoken words.
- [ ] Series tag in notes.md ("Series:"); 3 of every 5 Shorts in a named format.

A/B tests: captions clank vs karaoke (Viewed vs swiped, avg % viewed); title name-first vs action-first (48 h views);
lane rule vs contract (48 h views); cut rate 1.9 vs 2.8 s (avg % viewed); loop tail on/off (avg % viewed, replays);
hook headline on/off (Viewed vs swiped); length 22-28 vs 32-40 s (avg % viewed).
```

---

## Sources
- Official: [YouTube Help, Shorts analytics tips](https://support.google.com/youtube/answer/12942217) (Viewed vs swiped, shown in feed); [YouTube Help, monetization/inauthentic content](https://support.google.com/youtube/answer/1311392); [TechCrunch, inauthentic content, Jul 2026](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/); [TechCrunch, Shorts series, 23 Sep 2026](https://techcrunch.com/2026/09/23/youtubes-new-short-series-feature-brings-episodic-viewing-to-shorts/); [MediaPost interview with YouTube Shorts product lead](https://www.mediapost.com/publications/article/388588/youtube-shorts-product-lead-offers-insights-for-creators-and-brands/) and [Search Engine Journal](https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/) (hashtags, frequency, thumbnails, length: quoted as relayed by those outlets, not read on YouTube's own site).
- Studies: Paddy Galloway, 3.3B views, 5,400 Shorts, 33 channels: [thread](https://threadreaderapp.com/thread/1646898356419981315.html); OpusClip 13.5M clips (podcast-clip heavy, weak fit for us): [study](https://www.opus.pro/research/how-to-go-viral-youtube-shorts); letter-case reading speed: [ERIC](https://files.eric.ed.gov/fulltext/EJ1204569.pdf); curiosity-gap theory (Loewenstein 1994): [CMU](https://www.cmu.edu/dietrich/sds/docs/golman/golman_loewenstein_curiosity.pdf) (a moderate gap works best: the viewer should already half-guess the answer).
- Vendor blogs (HYPOTHESIS level): [aibrify retention playbook](https://aibrify.com/blog/youtube-shorts-retention-curve-playbook), [blitzcut captions](https://blitzcutai.com/blog/best-caption-style-youtube-shorts-2026), [emax word-by-word](https://emax.studio/blog/word-by-word-ai-captions-vs-static-subtitles), [vidIQ loops](https://vidiq.com/blog/post/double-youtube-watch-time-looping-shorts/), [miraflow Shorts SEO](https://miraflow.ai/blog/youtube-shorts-seo-2026-how-to-rank-shorts-in-search), [air.io 13 viral Short types](https://air.io/en/youtube-hacks/13-types-of-shorts-that-always-go-viral-with-examples), [fliki faceless niches](https://fliki.ai/blog/best-faceless-youtube-niches). Pinned-comment claim ("up to 30% more replies", [air.io](https://air.io/en/youtube-hacks/what-to-write-in-your-youtube-pinned-comment-to-get-a-reaction-from-your-audience)) is vendor data and comments do not drive reach in our data, so I added no pinned-comment rule.
- Channel data: yt-dlp public `/shorts` tabs and per-video metadata (mweb client, no download) for @CoachClank, @rebound, @AhmedsBasketball, @CourtsideFilms, Hoop Facts (UCFEwO714Se45wz5NMnYw4ag), Hoops Lore (UCwdOA-ZRZ9Ihpo6Wfar5wbQ), pulled Oct 4, 2026. Cover frames: `https://i.ytimg.com/vi/<id>/oardefault.jpg`.

## Uncertain or not done
- Could not watch or hear any Short: music vs none, voice, sound effects and caption animation of competitors are unverified.
- Upload time of day was not available in the metadata, so I did not re-test posting time; repo Round 3 data stands (observational).
- Cross-niche channels were taken from vendor lists, not measured.
- Pooled lifts mix channels with different topics; they show patterns, not causes. n is small for several features (marked).
