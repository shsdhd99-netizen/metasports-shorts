# Round 6: What makes a Short go viral, beyond competitor channels (Oct 4, 2026)

*Cloud session. Scope: everything that could move views, not just the NBA channels covered in Round 5. Evidence labels:*
- **PROVEN** = an official YouTube page/statement I read, or numbers I computed today from public channel data. For channel data, "proven" means the pattern is really there; it is observational, not causal.
- **SUPPORTED** = several independent credible sources, a peer-reviewed study, or our own small measurements pointing the same way.
- **HYPOTHESIS** = vendor blog claim, one source, or my own inference. Needs an A/B test before it becomes a rule.

*How the research was done:* WebSearch/WebFetch on YouTube Help pages and press coverage of Creator Insider interviews; yt-dlp public metadata for 10 channels (about 900 Shorts); cover frames of ~30 top Shorts viewed by eye. vidIQ had 4 credits (a call costs 5), so it was not used. YouTube blocks downloads here, so I could not watch or hear any Short. `support.google.com` pages are fetched through a summariser, so quotes below are as returned by that tool. The vidIQ blog returned 403/429, so I only have its search-snippet text, and I treat that as vendor-level.

**Plain summary.** Almost every popular "viral formula" is vendor opinion. What is firmly known: (1) YouTube measures whether people stay or swipe, and a new Short is shown to a small test group first; (2) the idea and title concept explain far more of the gap between a channel's hits and its median than length, captions, hashtags or posting time do; (3) original value per Short is an official monetisation rule; (4) several of our gate numbers (shot length, 18-35 s window, "never 3 a day") have no support or are contradicted by the channels we copy.

---

## 1. Ranking signals and how YouTube distributes Shorts

| Claim | Evidence | Label |
|---|---|---|
| Studio now reports **"Shown in feed"** and **"Viewed (vs. swiped away)"** for Shorts. | YouTube Help, [Content tab analytics tips, Shorts](https://support.google.com/youtube/answer/12942217); also the YouTube Community post ["New Shorts metric: Viewed vs Swiped Away"](https://support.google.com/youtube/community-video/273390203/new-youtube-shorts-metric-viewed-vs-swiped-away?hl=en) | PROVEN (the metrics exist and are defined) |
| **Which band is "good" (70-90% viewed; under 60% rarely does well)** is not an official YouTube number. It comes from Paddy Galloway's study: 5,400 Shorts, 33 channels, 3.3B views, April 2023. | [Galloway thread](https://threadreaderapp.com/thread/1646898356419981315.html). Same thread: likes, shares, comments showed "no strong relationships with performance"; AVD over 50 s averaged 4.1M views; Shorts convert about 16.9 subs per 10,000 views overall. | SUPPORTED (one good third-party study, pre-dates the 2025 view change) |
| **Explore, then exploit.** A new Short is shown to a small seed audience; if they stay/replay/engage the audience widens, otherwise it stops. | Described by many outlets quoting Creator Insider/YouTube Shorts product lead Todd Sherman, e.g. [Search Engine Journal](https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/), [quso.ai](https://quso.ai/blog/youtube-shorts-algorithm), [clipiq](https://www.clipiq.pro/blog/youtube-shorts-algorithm-2026). I could not open the Creator Insider video itself. | SUPPORTED (consistent across outlets; seed-size numbers like "a few hundred to a few thousand" are vendor guesses = HYPOTHESIS) |
| **Views since 31 Mar 2025 count when a Short starts or replays**, with no minimum watch time; "engaged views" (stayed past the first seconds, not counting loops) still drive average view duration, average % viewed and monetisation. | [YouTube Help, Shorts analytics](https://support.google.com/youtube/answer/12942217) (engaged views defined as "not including any loops"); coverage: [TubeBuddy](https://www.tubebuddy.com/blog/youtube-shorts-view-count-update-what-creators-need-to-know-about-the-new-metrics/), [vidIQ](https://vidiq.com/blog/post/youtube-view-count-update/), [Sam Proof](https://samproof.tv/2025/03/28/youtube-is-changing-how-shorts-views-are-counted-heres-what-creators-need-to-know/) | PROVEN for the definition; SUPPORTED for "loops add public views" |
| YouTube says the ranking looks at **watch time, rewatches, likes, shares and comments** ("deliberate watching"); "the audience is the algorithm". | Quoted via [Social Media Today](https://www.socialmediatoday.com/news/youtube-advice-for-shorts-creators-hashtags-algorithm/691835/) and [MediaPost](https://www.mediapost.com/publications/article/388588/youtube-shorts-product-lead-offers-insights-for-creators-and-brands/) (relayed, not from YouTube's own site; both pieces are older and one still says the Shorts maximum is 60 s, which is out of date, see section 9) | SUPPORTED |
| **Hashtags are not required**; useful when tied to a real-world event or topic. | Same two interviews. | SUPPORTED |
| **Posting frequency:** no algorithmic penalty for posting more, but "if you generated a bunch of relatively lower quality videos ... better in making a better video and fewer of them". Re-uploading the same Short risks being seen as spam. | [Social Media Today](https://www.socialmediatoday.com/news/youtube-advice-for-shorts-creators-hashtags-algorithm/691835/) | SUPPORTED |
| **Post time:** "should not worry about when they post as much as what they post", except breaking news. | [MediaPost](https://www.mediapost.com/publications/article/388588/youtube-shorts-product-lead-offers-insights-for-creators-and-brands/) | SUPPORTED. Contradicts treating our 6-11 AM ET rule as important |
| **Thumbnails/covers:** the Shorts feed is full-screen autoplay, so the first second does the thumbnail's job; the cover only shows on channel pages, the Shorts tab and some search shelves. You can choose a frame (and upload a custom image from desktop Studio). | [Social Media Today](https://www.socialmediatoday.com/news/youtube-advice-for-shorts-creators-hashtags-algorithm/691835/); product details [vidIQ](https://vidiq.com/blog/post/youtube-shorts-custom-thumbnails/), [TubeBuddy](https://www.tubebuddy.com/blog/youtube-shorts-custom-thumbnail-studio) | SUPPORTED |
| **Series:** YouTube announced Shorts series (seasons, episodes, a Watch Series button in the feed) on 23 Sep 2026 for Partner Program channels. | [TechCrunch](https://techcrunch.com/2026/09/23/youtubes-new-short-series-feature-brings-episodic-viewing-to-shorts/), [MediaPost](https://www.mediapost.com/publications/article/418231/youtube-rolls-out-feature-to-encourage-episodic-co.html) | PROVEN that it exists; whether it raises views = HYPOTHESIS |
| **Subscriber conversion:** about 16.9 subs per 10,000 Shorts views (Galloway); CoachClank measured 0.13 per 1,000 in Round 2; ours 0.21 per 1,000. | Galloway thread above; Round 2 | SUPPORTED. Shorts are a reach tool, not a subscriber tool |
| **Pinned comment effect:** one vendor says well-made pins lift replies up to 30% ([air.io](https://air.io/en/youtube-hacks/what-to-write-in-your-youtube-pinned-comment-to-get-a-reaction-from-your-audience)); academic work shows creator interaction raises engagement on long videos ([Online Information Review](https://www.emerald.com/insight/content/doi/10.1108/OIR-04-2022-0217/full/html)). No source shows pinned comments raise Shorts reach. | Our data: CoachClank's top 10% get **fewer** comments per 1,000 views than the rest (0.06 vs 0.16), and likes per 1,000 views are the same (13.1 vs 12.9). Galloway also found no link. | Comments boost reach: contradicted. Pinned comment as engagement habit: HYPOTHESIS, harmless |
| **Tags and descriptions:** I found no official source saying they matter for Shorts. Our data: empty description = 1.00x vs 1.00x relative views (n=344 vs 225). | computed from the 6-channel set | PROVEN no measurable effect in these channels. YouTube still indexes titles and spoken/on-screen text per vendors (HYPOTHESIS) |

---

## 2. Hook science (first 1-3 seconds)

What is solid:
- YouTube measures it directly (Viewed vs swiped away). Vendor summaries say 30-60% of the drop happens in the first 3 seconds ([aibrify](https://aibrify.com/blog/youtube-shorts-retention-curve-playbook), [virvid](https://virvid.ai/blog/first-3-seconds-hook-faceless-shorts-2026)); those percentages are SUPPORTED at best (many blogs repeat each other, no raw data).
- **Curiosity gap is real psychology:** Loewenstein's information-gap theory; curiosity peaks when the viewer half-knows the answer and the gap is moderate ([CMU paper](https://www.cmu.edu/dietrich/sds/docs/golman/golman_loewenstein_curiosity.pdf), [Journal of Cognition](https://journalofcognition.org/articles/10.5334/joc.501)). Four triggers: a question left open, a sequence started, an expectation broken, someone knows something you don't. SUPPORTED as theory. That it raises retention in Shorts is HYPOTHESIS. Research on clickbait headlines found null effects on later retention/trust ([Munger et al.](https://csdp.princeton.edu/sites/g/files/toruqf2376/files/media/munger_clickbait_10182018.pdf)): a curiosity gap gets the click, the payoff earns the stay.
- **What the data shows about "hook words" (computed today, 570 NBA Shorts):** titles opening with Why/How/What/Did/Is/Does/Can get 1.64x their channel's median (n=28); He/She/They-opening 1.23x (n=21); containing a digit 1.04x (n=124, no effect); question mark 0.95x (n=83, no effect). PROVEN (pattern), small n for the first two.
- **Cross-niche, Zack D. Films (28.7M subs, 100 Shorts, median 5.8M):** opens "He Drifted At Sea For 133 Days", "How A Mongolian Baby Cradle Worked", "How Ink Tags Stop Clothing Thieves", "Japanese Eels Can Escape A Fish's Stomach". Pattern: one concrete, odd, visual fact; "How/He" openers; 100% of titles carry an emoji (😨 😮 🤔 😏). Its top 10% is only 2.4x its median, a factory with low variance. **Daily Dose Of Internet** (20.7M subs, median 464K) wins with 12-17 s clips and titles like "Exactly the Right Amount", "Did Not See That Coming": the title is a reaction, the video is the surprise.
- **Pattern interrupts, faces, motion, text in the first seconds:** claims like "motion plus text overlay within 3 seconds averages 38% higher retention" appear on vendor sites with no method ([air.io](https://air.io/en/youtube-hacks/advanced-retention-editing-cutting-patterns-that-keep-viewers-past-minute-8)). HYPOTHESIS.
- **Numbers as hooks:** SUPPORTED as a belief among vendors; our channel data says a digit in the title has no effect. Treat "number first" as a test, not a rule.

---

## 3. Retention structure

| Topic | What the evidence shows | Label |
|---|---|---|
| **Length vs views, NBA channels** | CoachClank: <=20 s median 291K (n=82), 21-30 s 848K (n=52), 31-45 s 999K (n=9), 46-61 s 5.9M (n=2). Pooled over 6 channels: <=20 s 0.83x, 21-34 s 1.06x. | PROVEN (pattern; small n at the long end) |
| **Length vs views, cross-niche** | Zack D. Films: no length effect (0-20 s 5.3M, 21-30 s 6.3M, 31-45 s 5.3M, 46-61 s 5.5M). Daily Dose: the shortest wins, 0-20 s 509K (n=67) vs 21-30 s 324K (n=13). Hoop Facts: no effect. | PROVEN: length alone does not decide; it depends on the idea |
| Length guidance | Galloway: most Shorts are 20-40 s and longer ones did better on average. Vendor: 20-35 s for informational, 12-18 s for punchlines ([toptal](https://www.toptal.com/creator/post/youtube-shorts-length)); "65% retention needed under 30 s, 50% for 30-60 s" is a vendor figure ([retensis](https://retensis.com/blog/audience-retention-benchmarks-2026)). YouTube lead: "no ideal length, storytelling over duration". | SUPPORTED: a story takes as long as it takes; do not pad or cut to hit a number |
| **Re-hook mid-video / payoff timing** | CoachClank's biggest 2026 Shorts put the turn in the first 10-40% (Round 3, n=8). Vendor: "hump" curves peak in the middle where reveals sit ([aibrify](https://aibrify.com/blog/youtube-shorts-retention-curve-playbook)). | SUPPORTED (small own sample) |
| **Loop endings** | A loop adds a counted view since 31 Mar 2025 and can push retention above 100%; one vendor case study reports 85% vs 115% retention and 4x impressions ([vidIQ](https://vidiq.com/blog/post/double-youtube-watch-time-looping-shorts/), [virvid](https://virvid.ai/blog/looping-structure-shorts-retention-2026)); creator Jake Fellman reports a 1M to 20M jump after switching to loops. These are anecdotes, not controlled tests. | SUPPORTED mechanism (official counting rule), HYPOTHESIS size |
| **Ending on a CTA** | No evidence for or against. Clank ends on the payoff. | HYPOTHESIS |

---

## 4. Visuals

| Topic | Evidence | Label |
|---|---|---|
| **Cut rate** | CoachClank's 8 biggest 2026 Shorts: a new shot every 2.0-4.7 s (Round 3, measured). Vendors say 1.5-3 s ([aibrify](https://aibrify.com/blog/youtube-shorts-retention-curve-playbook), [opus](https://www.opus.pro/research/how-to-go-viral-youtube-shorts)). No controlled test found. | Our gate (average shot <= 1.9 s, no shot over 3 s) is **unsupported and partly contradicted** by the channel we copy |
| **Zooms, color, overlays, memes** | No independent data. | HYPOTHESIS |
| **B-roll vs talking head** | OpusClip's 13.5M-clip study is podcast/interview clip heavy (B-roll only 6% of clips) and does not fit AI story Shorts. Our own evidence is one user complaint (#15 v1 swiped, n=1). Clank and Ahmed's use footage/images that match each sentence (cover frames). | HYPOTHESIS that talking-head share causes swipes; SUPPORTED that winners illustrate the spoken line |
| **Captions: used?** | 80% of 13.5M clips use captions (OpusClip, [study](https://www.opus.pro/research/how-to-go-viral-youtube-shorts)). Colour/size claims are vendor. "Retention lift from captions 25-40%" ([aibrify](https://aibrify.com/blog/youtube-shorts-retention-curve-playbook)) and "12-15% completion" (OpusClip, no method) are unverified. About 21% of Shorts viewers keep sound off per one vendor roundup ([zebracat](https://www.zebracat.ai/post/youtube-shorts-statistics)), HYPOTHESIS. | Captions: SUPPORTED as universal practice; their causal effect HYPOTHESIS |
| **Captions: style** | See Round 5: top NBA channels use sentence-case/lowercase, centred ~50% height, with REBOUND adding one accent colour on the spoken word. ALL CAPS reads 12-20% slower in controlled reading studies ([sitelint summary](https://www.sitelint.com/blog/should-we-avoid-writing-in-all-caps), [ERIC](https://files.eric.ed.gov/fulltext/EJ1204569.pdf)). | Reading speed: PROVEN (lab); effect on views: HYPOTHESIS |

---

## 5. Audio

| Topic | Evidence | Label |
|---|---|---|
| **Loudness** | YouTube applies "stable volume" by default on playback ([YouTube Help](https://support.google.com/youtube/answer/14106294)). The "-14 LUFS target" figure is vendor-repeated ([audioedit](https://audioedit.io/blog/best-audio-settings-for-youtube-shorts), [lufsoptimizer](https://lufsoptimizer.com/how-loud-should-youtube-shorts-be)). I did not find YouTube's own page stating -14. | SUPPORTED as safe practice; our -14 gate is harmless |
| **Voice vs music balance** | Vendors: voice 10-15 dB above music, music ducked under speech. | HYPOTHESIS, harmless |
| **Music vs none** | No study found comparing Shorts with and without music. Official note: music from YouTube's licensed library cuts the Creator Pool share for that Short (one track: 50% of the pool revenue goes to music licensing) ([YouTube Help, Shorts monetization](https://support.google.com/youtube/answer/12504220)). | Music helps views: unsupported. Music costs money: PROVEN |
| **Trending audio** | Claims are all vendor ([capcut](https://www.capcut.com/resource/trending-sounds-on-youtube-shorts)); no data. | HYPOTHESIS; poor fit for a narrated story |
| **Voice pace** | CoachClank 247-289 wpm in the 8 biggest (Round 3). No cross-niche measure. | SUPPORTED (n=8) |
| **SFX** | No evidence. | HYPOTHESIS; we already limit to 2-5 |

---

## 6. Topic selection and timing

| Topic | Evidence | Label |
|---|---|---|
| **Rule / ban / "caught" / referee** | Pooled 6 NBA channels: 2.49x relative views (n=26); REBOUND's 13 rule/ban Shorts at 7.7M median vs 775K (Round 4); Clank rule/ref 617K vs 448K. Generic vendor lists agree (rule-created-by-one-player, arguable stats; [air.io](https://air.io/en/youtube-hacks/13-types-of-shorts-that-always-go-viral-with-examples)). | PROVEN (pattern), SUPPORTED |
| **One-second oddity / size gap / spectacle** | Clank top 25 (6'8 vs 7'9, a 13-ft hoop, "playing by himself"); cross-niche: Zack D. Films (odd facts), Daily Dose (strange moments). | PROVEN (pattern) |
| **Generic wholesome/fan/news** | Clank bottom 15 (8K-42K): "Baby Takes Her First Steps at a Game", "Crowd Cheers for Fan", "Nicest NBA Player Ever". | PROVEN (pattern) |
| **Contract/trade** | Ahmed's contract/trade Shorts 105K vs 93K overall (Round 4) | SUPPORTED |
| **Speed after an event** | A study of YouTube news videos found a half-life of 2-15 hours, average 7.3 h ([Sargsyan et al., arXiv 2507.21187](https://arxiv.org/pdf/2507.21187); the abstract numbers as reported by search snippet, the PDF summary did not return them). Vendor: sports clips lose "emotional charge" within a day ([opus](https://www.opus.pro/research/best-time-sports-youtube)). Product lead: timing matters for breaking news. | SUPPORTED for news-type Shorts; evergreen stories are not time-bound |
| **Search vs browse** | Vendors report >60% of organic views are from the Shorts feed and search about 9-26% depending on source ([metricool](https://metricool.com/youtube-shorts-algorithm/), [fluxnote](https://fluxnote.io/guides/youtube-traffic-source-breakdown-2026)); no official number found. | HYPOTHESIS; the feed matters most |
| **Fresh vs retold** | Round 2: three retold stories got 44K-73K vs 2.7M-23M for the original. n=3. | SUPPORTED (small) |
| **Posting hours** | Our Round 3 Clank medians favour 6-11 AM ET; YouTube says posting time matters little; vidIQ's 40M-video study summary is not independently checked. | HYPOTHESIS |

---

## 7. Cross-niche viral Short channels (measured today, public yt-dlp data)

| Channel | Subs | Median / top 10% | Cadence | Length | Title pattern | What it shares with CoachClank |
|---|---|---|---|---|---|---|
| Zack D. Films | 28.7M | 5.8M / 13.9M | **35 a week** | 33 s median, no effect | He/How + weird concrete fact + emoji on every title | one idea in 1 second, short plain title, relentless output |
| Daily Dose Of Internet | 20.7M | 464K / 2.6M | 4.7 a week | 16 s | reaction-style 3-5 words, emoji ~70% | one surprise, shortest clip wins |
| Bleacher Report | 5.1M | 95K (n=100) | not measured | n/a | news headlines | a big official brand gets a lower median than a niche story channel (not analysed further) |
| MagnatesMedia (business/history stories) | 1.9M | 66K / 2.0M (n=29, old: 2021-2025) | slow | ~42 s | "story" titles | its two best (4.1M, 2.0M) are a MrBeast explainer and a "Funny Pricing Tactic": again an oddity, not a biography |

What they share (PROVEN pattern, 4 channels plus the NBA set): a **single concrete, odd idea per Short**, titles of 4-7 plain words that name the odd thing, nothing in the title that needs context, and a repeatable format. Hits differ from the median by 2x-60x within a channel. The two most successful channels in the sample post at very different rates (Zack 35/wk, Clank 5.9/wk), so volume is not the common factor; consistency is.

---

## 8. Policy and monetisation risks

| Risk | What the source says | Label |
|---|---|---|
| **Inauthentic / mass-produced content** | Policy renamed from "repetitious content" to "inauthentic content" on 15 Jul 2025; mass-produced or template videos are ineligible; AI voice with real added value stays eligible ([YouTube Help](https://support.google.com/youtube/answer/1311392), [TechCrunch Jul 2026](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/), [lenspov summary](https://lenspov.com/articles/youtube-ai-content-demonetization-2026)) | PROVEN |
| **Reused content in Shorts** | Shorts monetisation page: non-original Shorts such as unedited clips of others' movies/TV are ineligible; views of reused content without original additions do not count ([YouTube Help, Shorts monetization policies](https://support.google.com/youtube/answer/12504220)) | PROVEN. Our narration, research and opinion line are the "original addition"; a clip with captions only would not be |
| **Copyright claims on Shorts over 1 minute** | The help pages I fetched on 4 Oct still say a Short over 1 minute with an active Content ID claim is blocked globally ([13053317](https://support.google.com/youtube/answer/13053317), [15424877](https://support.google.com/youtube/answer/15424877)). A separate article states that from 24 Sep 2026 such Shorts are no longer auto-blocked and can stay up while the claim is active ([argil](https://www.argil.ai/blog/how-long-can-youtube-shorts-be)); it cites the same YouTube page, which did not show it to my fetcher. **Conflict, unresolved.** | Keeping under 60 s remains the safe choice. UNCERTAIN |
| **Shorts length limit** | Shorts can now be up to 3 minutes ([YouTube Help](https://support.google.com/youtube/answer/15424877)); older interviews quoted "60 s". | PROVEN (current page). Our "never over 60 s" is a risk choice, not a platform limit |
| **Shorts payouts from 1 Feb 2027** | Monthly Creator Pool payout needs 10M qualified Shorts views in the trailing 90 days; entry bar rises from 10M to 20M qualified Shorts views or 4,000 to 8,000 watch hours; channel counts as active with 5 Shorts per 90 days ([Search Engine Journal](https://www.searchenginejournal.com/youtube-updates-partner-program-terms-shorts-payout-rules/585331/), [vidIQ](https://vidiq.com/blog/post/youtube-partner-program-changes-2027/)); creators keep 45% of their allocated revenue and music reduces the pool share ([YouTube Help](https://support.google.com/youtube/answer/12504220)) | PROVEN (official page + press) |
| **Re-uploading / duplicates** | YouTube lead: risk of being seen as spam ([Social Media Today](https://www.socialmediatoday.com/news/youtube-advice-for-shorts-creators-hashtags-algorithm/691835/)) | SUPPORTED |
| **AI visuals of real players** | Round 2 notes: likeness-detection rollout; removal risk | PROVEN (Sources.md official links) |

---

## 9. Our current checklist rules: supported, unsupported or contradicted

| Rule (from `qa_short.py`, cloud-short skill, Lessons Learned) | Verdict | Why |
|---|---|---|
| Voice at 0.0-0.4 s, no filler first word | SUPPORTED (logic) | The metric YouTube judges first is stay vs swipe; no data on "filler" itself (HYPOTHESIS) |
| >=3 shots and real action in first 3 s | UNSUPPORTED | Vendor-only; Clank's cut rate (2.0-4.7 s average) does not obviously fit |
| No shot over 3 s (quote 4 s); average shot <= 1.9 s | UNSUPPORTED, partly CONTRADICTED | Clank's biggest Shorts average 2.0-4.7 s |
| No clip over 35%; >=6 clips | UNSUPPORTED (but low cost; also helps "original value") | no data |
| Talking head <= 45%, b-roll >= 35%, cards <= 25% | UNSUPPORTED by data | one user complaint (n=1); winners show footage that matches the line |
| Length 18-35 s | **CONTRADICTED at both ends** | Clank 21-30 s 848K, 31-45 s 999K, <=20 s 291K; Zack D. no length effect; Daily Dose short wins |
| Last shot = first clip (loop) | SUPPORTED mechanism | replay counts as a view since Mar 2025; effect size unproven |
| Loudness -14 LUFS | SUPPORTED | safe practice; vendor-sourced |
| Never over 60 s | KEEP (unresolved conflict above) | not a platform limit, a claim-risk choice |
| Post 6-11 AM ET | UNSUPPORTED | YouTube says it matters little; observational Clank data only |
| 1 a day base, never 3 | UNSUPPORTED, partly CONTRADICTED | n=3 days; Zack D. posts ~5 a day at 5.8M median; YouTube: quality over volume |
| Titles 4-7 words, 1 emoji at the end | SUPPORTED (5-7 words 1.21x, n=262); emoji weak (1.10x) | |
| Title starts with "a question, number or name" | **CONTRADICTED** | Clank name-first 237K vs 494K (n=20); question mark 0.95x pooled; digit 1.04x; the working openers are action/claim and Why/How/What/Did/Is |
| Avoid 🤔 | UNSUPPORTED | n=5; Zack D.'s 16M Short uses 🤔 |
| No hashtags, no description | SUPPORTED (no measured effect; YouTube: hashtags optional) | |
| Tags 440-490 characters | UNSUPPORTED | no source shows tags move Shorts |
| ALL CAPS red/green captions (house style) | UNSUPPORTED | caps read slower; top NBA channels use sentence case; Round 5 |
| Hook headline `--hook-text`, auto-zoom, boom/sfx on hook | UNSUPPORTED (already flagged "test it") | |
| Argument-ending pinned comment | UNSUPPORTED for reach (SUPPORTED as harmless engagement habit) | comments do not drive reach |
| Three covers per Short | LOW VALUE | Shorts feed does not show covers; channel-page tile only |
| Lane: rule/ban/oddity, contracts are weak | PROVEN / SUPPORTED | |
| Never retell a bigger channel's story | SUPPORTED (n=3) | |
| Original value per Short, vary structure | PROVEN (official) | |
| Voice ~250-290 wpm | SUPPORTED (n=8) | |
| Real quotes in short bursts, evidence cards <= 2 s | UNSUPPORTED (design choice, no data) | |
| Post 2nd Short only with two strong stories | UNSUPPORTED | |

---

## 10. Additions in evidence tiers (supersedes the Round 5 block where they differ)

```markdown
### Round 6 checklist additions (Oct 4, 2026)

TIER A - PROVEN (official source, or measured in 570-900 public Shorts today)
- [ ] Concept: one odd, concrete idea you get in one second. Lane = rule/ban/"caught"/referee, size or skill spectacle, one-second oddity, petty/funny player. Not generic wholesome, fan-interaction or contract news. (notes.md "Lane:" and "Concept:" in 8 words)
- [ ] Title 5-7 plain words that name the odd thing; opens on an action/claim ("He ...", "Why/How/What/Did/Is ...", "Missing a ...") rather than a player name.
- [ ] Original value per Short recorded in notes.md ("Added value:"): our narration, research, opinion line or verified number; a source URL for every number. Rotate structure; no template clones back to back.
- [ ] Do not post unedited third-party clips; keep Shorts under 60 s while the Content ID claim rule is unclear.
- [ ] Keep: no hashtags, no description. Do not spend time on covers beyond a decent frame 0 / chosen frame.
- [ ] Judge every Short by Studio's "Viewed vs swiped away" and average % viewed at 24 h (official metrics), never by comments or likes.

TIER B - SUPPORTED (several sources or our own small measurements)
- [ ] Length follows the story: 21-45 s for stories; do not cap at 35 s or pad to reach it. Quick moments (<= 20 s) only for a single-beat surprise.
- [ ] Voice 240-290 words/min; turn in the first 40% of the words; end on the payoff with no outro or CTA.
- [ ] Loop-friendly ending: last line echoes the first, short tail after the last word, last shot = first clip.
- [ ] Captions on from the first word, sentence case, large, centred near half height (Round 5 `karaoke` or `clank`).
- [ ] News-type stories go out within hours of the event; evergreen oddities can wait.
- [ ] Add a 3-5 Short format name ("Series:") so the repeatable format is ready for Shorts series.

TIER C - HYPOTHESIS (test, do not enforce)
- [ ] Average shot length 1.9 s vs 2.8 s; cut rate floor >= 1.3 s.
- [ ] Hook headline, auto zoom, one SFX on the hook.
- [ ] Music under the voice, on or off (cost: reduces Creator Pool share).
- [ ] 6-11 AM ET posting window.
- [ ] Title keyword in the first 15 spoken words (search).
- [ ] Emoji at the end of the title (💀 😳 😭 vs none).
- [ ] Pinned two-sided question.

DROP or DEMOTE: "title starts with a question/number/name" (contradicted); "average shot <= 1.9 s" and "no shot over 3 s" as hard gates (demote to warnings); "length 18-35 s" (replace with 21 s minimum, no maximum below 60); "never 3 a day" (no data); tags as an SEO tool (no data); 3 covers per Short (low value); avoid-🤔 (n=5).
```

---

## 11. A/B tests (one variable, 3 repeats, same lane and length band, read at 24 h)

| # | A | B | Primary metric | Secondary |
|---|---|---|---|---|
| 1 | Title opens on name ("LeBron Took ...") | Opens on action/claim ("He Took ...", "Why ...") | views at 48 h vs channel median | impressions, viewed vs swiped |
| 2 | Cut rate: average shot ~1.9 s | ~2.8 s | average % viewed | viewed vs swiped |
| 3 | Captions `clank` | `karaoke` (yellow active word) | viewed vs swiped away | average % viewed |
| 4 | Rule/ban/oddity lane | contract/trade lane | views at 48 h | subs per 1,000 views |
| 5 | Ending with a 0.15-0.4 s tail and echo line | current ending | average % viewed (above 100% means loops are working) | replays share |
| 6 | Length 22-28 s | 32-42 s (same story told tighter vs fuller) | average % viewed | views at 48 h |
| 7 | Hook headline on | off | viewed vs swiped away | first-3-s retention |
| 8 | Music under voice | none | average % viewed | Creator Pool revenue per 1,000 views |
| 9 | Post 6-11 AM ET | 7-10 PM ET | views at 48 h | none (low priority) |
| 10 | Emoji 💀/😳 at end | none | views at 48 h | none |

With about 6 Shorts a week and large natural spread (a channel's own top tenth is 5x-60x its median), one pair proves nothing; use medians over at least 3 pairs, and expect only large effects to be visible.

---

## 12. Where the evidence is thin

- Nothing here shows what causes a hit. The strongest pattern (rule/oddity concepts, action-first titles) is observational and mostly measured on a few channels.
- No independent study of cut rate, zooms, captions, music or SFX on Shorts retention. Every figure on those is vendor content. Our own gate numbers for them were set without evidence.
- I could not read Creator Insider videos themselves, only outlets quoting them, and could not read the vidIQ algorithm blog.
- Copyright: the 24 Sep 2026 change to claims on 1-3 minute Shorts is reported by one article but not visible on the YouTube pages I fetched.
- Cross-niche sample is 4 channels measured plus vendor lists; Magnates data is old (2021-2025, n=29).
- Hoop Facts, Hoops Lore, Ahmed's, Courtside, REBOUND detail is in Round 5.

## Sources (all accessed Oct 4, 2026)
Official: [YouTube Help 12942217](https://support.google.com/youtube/answer/12942217), [12504220](https://support.google.com/youtube/answer/12504220), [13053317](https://support.google.com/youtube/answer/13053317), [15424877](https://support.google.com/youtube/answer/15424877), [1311392](https://support.google.com/youtube/answer/1311392), [14106294](https://support.google.com/youtube/answer/14106294), [Community post on Viewed vs Swiped](https://support.google.com/youtube/community-video/273390203/new-youtube-shorts-metric-viewed-vs-swiped-away?hl=en). Press on official interviews/announcements: [Social Media Today](https://www.socialmediatoday.com/news/youtube-advice-for-shorts-creators-hashtags-algorithm/691835/), [MediaPost](https://www.mediapost.com/publications/article/388588/youtube-shorts-product-lead-offers-insights-for-creators-and-brands/), [Search Engine Journal](https://www.searchenginejournal.com/youtube-explains-how-shorts-algorithm-works/494953/), [TechCrunch Shorts series](https://techcrunch.com/2026/09/23/youtubes-new-short-series-feature-brings-episodic-viewing-to-shorts/), [TechCrunch inauthentic content](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/), [SEJ on 2027 payout rules](https://www.searchenginejournal.com/youtube-updates-partner-program-terms-shorts-payout-rules/585331/). Studies: [Galloway 3.3B views](https://threadreaderapp.com/thread/1646898356419981315.html), [OpusClip 13.5M clips](https://www.opus.pro/research/how-to-go-viral-youtube-shorts), [Sargsyan et al. half-life](https://arxiv.org/pdf/2507.21187), [Loewenstein/Golman](https://www.cmu.edu/dietrich/sds/docs/golman/golman_loewenstein_curiosity.pdf), [Munger clickbait](https://csdp.princeton.edu/sites/g/files/toruqf2376/files/media/munger_clickbait_10182018.pdf), [ERIC letter-case reading speed](https://files.eric.ed.gov/fulltext/EJ1204569.pdf). Vendor: aibrify, vidIQ, blitzcut, virvid, air.io, metricool, fluxnote, audioedit, argil (links in the sections above). Channel data: yt-dlp public `/shorts` tabs and per-video metadata (mweb client, no download) for CoachClank, REBOUND, Ahmed's Basketball, Courtside Films, Hoop Facts, Hoops Lore, Zack D. Films (UCvz84_Q0BbvZThy75mbd-Dg), Daily Dose Of Internet (UCdC0An4ZPNr_YiFiYoVbwaw), MagnatesMedia (UCE4Gn00XZbpWvGUfIslT-tA), Bleacher Report (UC9-OpMMVoNP5o10_Iyq7Ndw), pulled Oct 4, 2026.
