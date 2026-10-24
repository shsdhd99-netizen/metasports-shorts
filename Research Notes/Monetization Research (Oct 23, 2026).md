# Monetization research: what it takes for both channels (Oct 23, 2026)

**Owner's ask (via the coordinator):** the YPP requirements for Shorts-first channels, how Shorts views are counted, the policies most likely to block MetaSports and MetaSports FC, real examples, and the maths for each channel.

**How this was made:**
- Web research on Oct 23, 2026: YouTube Help and the YouTube Blog first, then creator-economy press. Every source is listed at the end.
- Our data: `Tools/data/channel_log.csv`, `Research Notes/Posted Tracker (Oct 21, 2026).csv`, `Soccer Channel/Data/fc_channel_log.csv`, the Ahmed study and its data folder, `Roadmap - Next 90 Days.md`, the Studio export in `Posted Shorts - metrics (Oct 15, 2026, with Studio export).csv`, and the FC drafts' `notes.md` / `sources.csv`.
- A fresh public snapshot of both channels failed (YouTube is blocked from the cloud). So the numbers below are from the logs: **MetaSports on Oct 21, FC on Oct 22.**

**Labels:**
- **[Official]** YouTube Help or the YouTube Blog.
- **[Press]** a news or trade site.
- **[Vendor]** a blog that sells a creator tool.
- **[Repo]** our own data.
- **[Inference]** my reading, not stated by any source.
- **(uncertain)** marks anything a source doesn't settle.

---

## 1. The requirements

### 1a. The thresholds
| Tier | What it unlocks | Requirement today | From Feb 1, 2027 | Source |
|---|---|---|---|---|
| **Expanded YPP** (the lower tier) | Memberships, Super Chat, Super Stickers, Super Thanks, Jewels/gifts, Shopping. **No Shorts ad money.** | 500 subs + 3 valid public uploads in the last 90 days + **3M qualified Shorts views in 90 days** (or 3,000 long-form watch hours in 12 months) | **Unchanged** | [Official] Expanded YPP page; [Official] YouTube Blog, Aug 10, 2026; [Press] The Next Web |
| **Full YPP**: ads + Premium on Shorts | Shorts Creator Pool ad share, Premium share, plus everything above | 1,000 subs + **10M qualified Shorts views in 90 days** (or 4,000 long-form watch hours in 12 months) | **New applicants:** 1,000 subs + **20M** Shorts views in 90 days, or **8,000** watch hours in 365 days | [Official] YPP overview; [Official] YouTube Blog, Aug 10, 2026; [Press] Shacknews, Hypebeast, TNW |
| **Shorts payout floor** (new) | Being *paid* from the Shorts Creator Pool | none | You must hold **10M qualified Shorts views in a rolling 90 days**. Below that, Shorts pay pauses; you stay in YPP and long-form still earns. It resumes when you cross 10M again. | [Official] YouTube Blog, Aug 10, 2026. Hypebeast says this covers existing partners too; TNW calls that unclear **(uncertain for existing partners)** |

**Other conditions** [Official] YPP overview:
- Live in a country where YPP runs (the US, UK, Canada and Australia all qualify).
- No active Community Guidelines strikes.
- 2-Step Verification on, access to advanced features, and one linked AdSense account.
- Upload at least once every 6 months.
- Accept the new terms in Studio by **Jan 31, 2027** to keep monetizing.

Other facts:
- The 2027 update also adds a channel-activity requirement. Details aren't published [Press] AIR timeline **(uncertain)**.
- **Review takes about a month.** The channel is reviewed as a whole, and meeting the numbers doesn't guarantee approval [Official].
- **Long-form watch hours and Shorts views can't be combined.** Shorts-feed watch time doesn't count toward watch hours [Official]; [Press] PPC Land, Oct 2025.
- **(Uncertain)** Whether a channel that *applies* before Feb 1 is judged on the old 10M bar if its review ends after Feb 1. The sources say the new bar is for creators "applying" from Feb 1. Apply before Feb 1 if you're eligible.
- **New incentives for channels below the threshold:** Shopping bonuses, brand-deal incentives and trend boosts were announced, but no details yet [Official] YouTube Blog.

### 1b. Rejections, appeals and reapplying [Official]
- **Reapplying:** 30 days after a first rejection; 90 days after any later one.
- **Appeal window:** 21 days after a rejection. Decisions come within 14 days.
- **Appeal video:** unlisted, under 5 minutes. It shows the channel URL in the first 30 s, explains how the channel follows the policies, and shows how you make the content. Don't delete videos before appealing.
- **Suspension:** if one is scheduled, you can appeal within the 7 days before it, and that pauses it.

---

## 2. How Shorts views are counted

### 2a. Counting
- **Mar 31, 2025:**
  - The public Shorts view counter started counting every start or replay, with no minimum watch time.
  - The old metric lives on as **"engaged views"** (Analytics, Advanced mode).
  - **YPP eligibility and Shorts revenue both use engaged views**, not the public counter [Press] SEJ, quoting YouTube.
- **Aug 24, 2026:** the same first-frame counting spread to long-form and Live. YPP and revenue still run on engaged views [Press] Relevant Audience, reporting a TeamYouTube post of Aug 17, 2026.
- **What "qualified" means:** a qualified Shorts view is an engaged view. Ads, private, unlisted and deleted Shorts, and image posts don't count [Press] PPC Land, citing YouTube's Creator Insider of Aug 14, 2026.
  - Views must come from public Shorts that appear in the Shorts feed [Official].
  - Making an unlisted Short public later doesn't credit its earlier views [Press] PPC Land, Oct 2025.
- **The engaged-view threshold is not published.** The "30 seconds" figure you see online is folklore [Press] Agentio.
- **Claimed Shorts:** no source says whether views on a Short with a copyright claim count toward the 10M/20M **(uncertain)**.

### 2b. What this means for us [Repo]
In MetaSports' Studio export (72 Shorts, Sep 16-Oct 14), **engaged views were 54% of public views**. Per Short it ranged from 42% to 68%.
- **So the public counter overstates YPP progress by about 1.85x.**
- The old Roadmap's "~33K views a day for fan funding" and "~110K a day for YPP" treated public views as qualified. In public views it's really **~62K and ~206K a day**.
- FC's longer Shorts may convert differently. Re-measure from its first Studio export.

### 2c. Revenue and RPM
**How the Shorts Creator Pool works** [Official] Shorts monetization policies:
- Ad revenue from between Shorts is pooled monthly.
- Your share follows your share of engaged views. You keep **45%** of what's allocated to you.
- Music tracks from YouTube's partners reduce the pool's share. Other third-party content (e.g. a non-music Content ID claim) is not credited as a contribution to the Short.

**Views that earn nothing:**
- **Unoriginal Shorts:** unedited clips of others' TV or film, reuploads, and compilations with nothing original added.
- Bot views.
- Views that break the advertiser-friendly guidelines.
- **Shorts over 1 minute with claimed content:** blocked.

**Typical Shorts RPM** (no source gives a sports-only figure):

| Source | Shorts RPM |
|---|---|
| [Press/agency] AIR Media-Tech, 274 channels (Sep 2026) | **$0.07-$0.20 per 1,000 views** in most niches. By country: US $0.33, Australia $0.19, UK $0.17, Canada $0.17, Germany $0.16. About $300 per 1M views for a US-heavy audience; $150-$250 for a mixed one. |
| [Vendor] vidIQ (updated May 2026) | $0.03-$0.10, most channels $0.03-$0.06. Their example: 468.5K views paid $16.61. |
| [Vendor] RenderFoot, football Shorts (Jun 2026) | $0.05-$0.15 |

- **[Inference] What it pays:** at the 10M floor, ~10M views a quarter is roughly **$300-$2,000 a quarter per channel**. A US-heavy audience sits at the top of that range.
- So the goal is to clear the gate, not the ad money itself.

---

## 3. The policies, and what reviewers look for

### 3a. How a channel is reviewed [Official] Channel monetization policies
Reviewers can't watch everything, so they look at:
1. the channel's main theme;
2. its **most-viewed** videos;
3. its **newest** videos;
4. the videos with the largest share of watch time;
5. metadata (titles, thumbnails, descriptions);
6. the **About** section.

For reused content they also look at **how you made the videos**. The policy covers the channel as a whole. It applies even when you have permission, and it is separate from copyright.

### 3b. Reused content (unchanged since before 2025)
- **The test:** viewers can see a "meaningful difference between the original video and your video" [Official].
- **Allowed** [Official]:
  - sports replays where the creator explains the moves;
  - edited footage with a new storyline or commentary;
  - reactions with substantive commentary;
  - film scenes with a new voiceover;
  - clips used in critical reviews;
  - material where the creator explains their contribution.
- **Not allowed** [Official]:
  - clips edited together with little or no narrative;
  - compilations of other sites' short videos;
  - downloads with no real changes;
  - mostly non-verbal reactions;
  - **videos that mainly read others' material, such as news feeds or web text**;
  - content uploaded repeatedly.

### 3c. Inauthentic content (mass-produced or repetitive)
- **Jul 15, 2025:** "repetitious content" was renamed "inauthentic content" [Official].
  - YouTube called it a minor update.
  - The reused-content rules didn't change [Press] SEJ.
- **Jul 16, 2026:** a clarification split the policy into three named categories [Press] Tubefilter, Jul 13; TechCrunch, Jul 20; TechRepublic, Jul 21:
  1. **Generic, repetitive or template-based content.** Examples [Official]:
     - same-situation, same-outcome videos;
     - templated storylines;
     - slideshows and scrolling text;
     - AI built on generic templates without the creator's own perspective.
  2. **Unsatisfying or off-putting content:** disturbing themes with no cohesive narrative, staged animal distress, and fake celebrity deaths.
  3. **AI personas posing as experts** on health, legal, financial or political topics.
- **Allowed:** a consistent intro and outro, and series with a recurring format, *as long as each video has its own storyline* [Official].
- **What YouTube is targeting:** YouTube's Matt Halprin said the target is content farming. These are videos that are "very generic and don't really have a narrative arc" [Press] TechCrunch.
- **Enforcement:**
  - **Jan 2026:** faceless and automated channels reported a wave of demonetizations, with some whole networks hit at once. Some were reinstated on appeal [Press] PiunikaWeb, Jan 12, 2026.
  - YouTube didn't confirm a sweep.
  - One secondary report says enforcement uses upload cadence and format similarity [Press] Let's Data Science **(weak source: its dates don't line up)**.

### 3d. AI voice and disclosure [Official] Altered or synthetic content
- **What needs disclosure:** realistic content that:
  - makes a real person seem to say or do something they didn't;
  - alters a real event or place;
  - shows a realistic scene that never happened;
  - or uses AI music that is the main focus of the video.
- **What doesn't:** AI for scripts, titles, thumbnails, captions or ideas; cloning *your own* voice; unrealistic content.
- **A generic AI narrator** (not imitating anyone) is not named either way. No example requires disclosing it **(uncertain, but not required on the page's wording)**.
- **Disclosing costs nothing.** It "won't limit a video's audience or impact its eligibility to earn money."
- **Not disclosing has a cost:** creators who repeatedly fail to disclose can be labelled by YouTube, have content removed, or be suspended from YPP.
- **AI voice itself is not a policy violation.**
  - The risk is low-effort use: AI narration over someone else's clip is a common "slop" example [Press] Tubefilter.
  - So is text-to-speech reading other people's articles or lists [Vendor] vidIQ.

### 3e. Copyright: league footage, Content ID and YPP
- **You need rights.** To monetize content you didn't make, you need commercial rights or a fair-use case. Commercial use is less likely to be fair use [Official] "What content can I monetize".
  - "Fair use is a defence, not a permission" [Press/blog] Clippie.
- **Claims vs strikes** [Official] Content ID claims; Copyright strikes:
  - A claim lets the owner block, monetize or track the video, and it "usually don't impact your channel or account".
  - A **takedown** is a strike. **3 strikes in 90 days ends the channel, and linked channels can be terminated too.** You also can't create new ones.
  - A strike expires after 90 days if you complete Copyright School.
  - Disputing a claim without a valid basis can turn it into a takedown.
  - The YPP page lists "no active Community Guidelines strikes". It doesn't mention copyright strikes. Treat any strike as a serious risk **(uncertain how a reviewer weighs them)**.
- **The 1-minute rule for Shorts** [Official] Three-minute Shorts; Manage Shorts as a rights holder; Content ID claims:
  - **A Short over 1 minute with an active claim is blocked worldwide, whatever policy the owner chose.** It isn't shown, recommended or monetized until the claim is resolved.
  - Under 1 minute, the owner's chosen policy applies.
  - The page doesn't spell out what happens under 1 minute **(uncertain)**.
- **NBA:**
  - In 2024 the league gave 6 YouTube creators a 25,000-hour archive. It reviews their videos and wants "transformative" work [Press] Digiday, Oct 2024.
  - For 2026-27 it has given highlight access to "hundreds of creators", mainly via TikTok; no terms are public [Press] Net Influencer, Oct 21, 2026.
  - Many channels accept NBA claims and treat those Shorts as reach, not revenue [Press] Sportsepreneur, Aug 2025.
  - **(Uncertain)** Whether we could join the NBA program.
- **FIFA:**
  - The World Cup archive on FIFA's channel is for watching, not clipping.
  - The 2026 YouTube-FIFA deal gives footage rights to media partners and an invited creator group, not to ordinary channels.
  - **Caveat:** these points come from a creator blog, not FIFA [Press/blog] Clippie, Jun 2026.
- **Premier League:** it sued YouTube in 2007 and later dropped the case [Press] SportBusiness. I found no current reporting on how it treats archive clips in Shorts **(uncertain)**.

### 3f. What gets clip-based commentary channels approved or rejected
This is a synthesis of 3a-3e. YouTube publishes no approval rubric.

| Gets approved | Gets rejected |
|---|---|
| The voice explains something (a rule, a record, a story) and the footage illustrates it | Footage carries the video, with a voice laid on top or none at all |
| Each video has its own story, angle and payoff | The same template, the same structure and the same outcome every time |
| Original graphics, circles, stat cards, maps, the creator's own research | Reading a news article or Wikipedia aloud |
| Honest, varied titles; an About section that explains the original work | Near-identical titles; a description that doesn't match the content |
| The most-viewed and newest videos all show the same original process | Off-theme uploads, duplicates and bare clips among the top videos |
| Shorts under 60 s when they use league footage | Long Shorts full of claimable broadcast footage |
| You can show your process in an appeal video | No proof of how the videos are made |

---

## 4. Ranked policy risks and do/don't rules

### 4a. MetaSports (NBA)
| # | Risk | Level | Why it applies to us |
|---|---|---|---|
| 1 | **Old and off-theme uploads under review** (reused content, inauthentic content, undisclosed AI) | **HIGH** | Reviewers start with the most-viewed videos. Ours are the 72 old-era Shorts (Nov 2025-Feb 2026, ~30K each), whose production files aren't in the repo. Some titles read like bare moments ("He Finally Hit the Cleanest Swish Ever", "The World's Hardest Dunk", "Wemby makes everything look small.."). There are also **8 off-niche Sora/AI meme Shorts** (Nov 2025), including **realistic AI Snoop Dogg** videos (a real person, so disclosure applies) and a "Top 4 Funniest Sora AI doorbell videos" compilation |
| 2 | **Copyright** (NBA footage; old music beds) | MEDIUM | Claims are likely, but every Short is 10-33 s, so a claim doesn't block it. A takedown would be a strike. The old-era music beds (trap loops) came from an unknown source: check Studio for claims |
| 3 | **Repetitive patterns** | MEDIUM | Duplicate uploads (#25 twice; "Why Jokic's Best Pass Doesn't Count" twice, #40/#40a). Near-twin titles (#42/#48 "Who Has Missed The Most…"). One fixed title template ("… 😳 #nba") on almost every title |
| 4 | **Reading others' material** | LOW-MED | The news lane (e.g. "The Lakers Just Saved Bronny") becomes a risk if the script only restates a report without the why or an angle |
| 5 | **Channel metadata** | LOW-MED [Inference] | The About text "Subscribe If I Made You Laugh!" doesn't describe the channel. The handle **@MetaSportsClips** says "clips" to a reviewer checking how the content is made |
| 6 | **AI voice disclosure** | LOW | The generic ElevenLabs narrator isn't required to be disclosed. A cloned real voice, or realistic AI visuals of real players, would be |

**Do:**
1. **Before applying, open your 20 most-viewed Shorts.** Make private any that have no voice narration, or that are a clip plus music. Reviewers see these first.
2. **Make the 8 AI/Sora meme Shorts private or delete them**, especially the Snoop Dogg ones. Together they're about 27K views, which costs nothing toward the 3M.
3. **Delete the duplicate uploads** (keep the better copy of #25 and of #40).
4. **Rewrite the channel description** to say what you make, e.g. "Researched NBA rule, record and story explainers, written and narrated by MetaSports." Consider whether the "Clips" handle is worth changing (a judgment call, not a rule).
5. **Keep every Short under 60 s.** The Playbook rule stays.
6. **Every Short explains something:** a sourced fact, then your angle and your payoff. Your own cards, circles and stat graphics show the work.
7. **Check Studio > Content > Copyright every week.** Swap claimed footage rather than disputing it, unless you have a clear fair-use case.
8. **Record a 3-5 minute process video now** (sources → script → voice → edit timeline), ready for an appeal.

**Don't:**
- post raw highlights, music-only clips or "best plays" compilations, even for reach;
- let a news Short just read an article;
- re-upload a Short that flopped;
- dispute a claim without a basis;
- clone a player's or announcer's voice, or post realistic AI images of real players;
- use songs except through the in-app audio picker.

### 4b. MetaSports FC (soccer)
| # | Risk | Level | Why it applies to us |
|---|---|---|---|
| 1 | **Claimed broadcast footage + Shorts over 60 s = blocked Shorts, plus strike exposure** | **HIGH** | Footage comes from FIFA World Cup broadcasts (2006, 2018), UEFA finals (2005 SAT.1, 1984 RAI), BBC Match of the Day, Premier League and Bundesliga highlights, and BBC Euro 2020, all found on archive.org (that doesn't make them licensed). **5 of 7 drafts run over 60 s:** S02 63.0 s, S03 70.7, S05 66.7, S06 62.4, S07 63.1. Only S01 (59.5) and S04 (57.7) are under. One claim on a >60 s Short makes it invisible, so its views never count. If the channels share a Google account, strikes put MetaSports at risk too ("linked channels") |
| 2 | **Template / mass-production pattern** | **HIGH-MED** | The format deliberately copies a template:<br>- the title as line 1, then "Back in [year]";<br>- a turn every 8-12 s;<br>- one reused music bed;<br>- fixed captions;<br>- Ahmed's habit of reusing identical titles as "Episodes".<br><br>It runs 1-2 a day from the same pipeline as a second channel. That's the pattern the Jul 2026 clarification and the Jan 2026 network demonetizations describe |
| 3 | **Reused content** | MEDIUM | Archive TV footage plus stock is fine when the narration tells a new story (allowed: "new storyline or commentary"). The risk is shots that still carry other creators' marks or audio. S06 uses a re-narrated highlight reel ("Narração Retrô"): make sure none of its original commentary is left |
| 4 | **Channel history** | MEDIUM, unknown | The channel was "Reddit Unfiltered" before the rename. Reddit-story read-alouds are a textbook "reading others' material" case. Check for old uploads |
| 5 | **AI voice and music disclosure** | LOW | The generic narrator and a quiet ElevenLabs music bed (not the main focus) aren't required to be disclosed |
| 6 | **Distressing topics** | LOW | Stories about injuries, deaths or violence need a real narrative arc, never a shock montage |

**Do:**
1. **Cut every Short that uses broadcast footage to 59 s or less.** Or replace the broadcast shots with stock, licensed photos and our `story_card.py` cards until it's mostly ours. This matters more than any other rule here.
   - Ahmed's Shorts run 58-167 s. How they avoid blocks is unknown. Their 1.6-2.1 s shots and framing may avoid matches, but that's [Inference], not a plan.
2. **Before applying, check the channel's Videos and Shorts tabs** for anything left from "Reddit Unfiltered". Make it private or delete it.
3. **Each Short is one distinct, researched real story** with sources in `notes.md` (already done). Vary:
   - the opening (not always "Back in [year]");
   - the turn phrases;
   - the ending type;
   - the music bed (rotate 3-4).
4. **Give each Short its own title.** Use repeated "series" titles sparingly, and add a distinct hook to each.
5. **Keep the cadence at 1-2 a day.** Ahmed's medians fell at 3 a day, and volume is a mass-production signal.
6. **Keep the two channels visibly different:** a different voice (already), caption look and openings, so they don't read as one automated network ([Inference] from the Jan 2026 reports).
7. **Fill in `licence_risk` in `sources.csv`** for every broadcast clip. Track claims after each post.
8. **Record a process video** (research → script → voice → edit).

**Don't:**
- upload a Short over 60 s containing broadcast footage you haven't cleared;
- keep any shot with another channel's watermark, captions or commentary;
- copy Ahmed's titles or wording (already a rule);
- generate realistic AI images or video of real players or events;
- make shock compilations.

---

## 5. The maths for each channel

**Formula:** a qualified view ≈ a public view × 0.54 (our Studio ratio, section 2b). A 90-day threshold divided by 90 gives the qualified views needed per day; divide that by 0.54 for public views.

| Threshold | Qualified views a day | Public views a day | Per Short, 1 a day | Per Short, 2 a day |
|---|---|---|---|---|
| 3M (fan funding) | 33.3K | **~62K** | ~62K | ~31K |
| 10M (YPP until Jan 31; the payout floor after) | 111K | **~206K** | ~206K | ~103K |
| 20M (YPP for new applicants from Feb 1) | 222K | **~412K** | ~412K | ~206K |

- **These are averages, not medians.** A few hits do most of the work. For example, 3M qualified at 2 a day could be 170 Shorts at 15K plus 10 at 300K.
- **Windows:** to apply under the 10M rule by Jan 31, the 90 days run **Nov 3, 2026 - Jan 31, 2027**. Views before Nov 3 don't help that application.

### 5a. MetaSports [Repo]
| | Now | Fan funding | YPP by Jan 31 (10M) | YPP from Feb 1 (20M) |
|---|---|---|---|---|
| Subscribers | **569** (Oct 21) | 500: **met** | 1,000 (431 to go) | 1,000 |
| Uploads in 90 days | 36+ | 3: **met** | n/a | n/a |
| Qualified Shorts views in 90 days | **~0.15M (estimate)**: ~230K public from the 36 new-era Shorts, plus a small trickle from old Shorts, × 0.54 | 3M (~5%) | 10M (~1.5%) | 20M (<1%) |
| Public views a day | **~12-13K** (229K over Oct 3-21; median of the last 7 is 4,600) | ~62K: **~5x now** | ~206K: **~16x now** | ~412K: **~33x now** |

- **At today's pace** (~6.5-7K qualified a day), 90 days adds up to ~0.6M qualified. That's about 20% of the fan-funding bar, so **no tier is reachable without a big step up.**
- **Subscribers:**
  - 469 → 569 from Sep 26 to Oct 21 (4 a day); 7 a day over Oct 13-21.
  - At 7 a day, you reach 1,000 around **Dec 22**; at 4 a day, around **Feb 6**.
  - Subs follow views: about 0.44 per 1,000 public views here, so 10M views would bring ~4,400. **Views are the real gate, not subscribers.**
- **What would clear fan funding:** 2 a day at a ~31K average. That's roughly the old-era level (Nov 2025-Feb 2026 median 29.8K).
- **What would clear 10M by Jan 31:** 2 a day at a ~103K average from Nov 3, about **20x the current median**. **[Inference] Unlikely without several 1M+ hits.** Plan for fan funding first and 20M after Feb 1.
- **Check the exact number** in YouTube Studio > Earn, which shows progress on each threshold. It's the only authoritative count of qualified views.

### 5b. MetaSports FC [Repo]
| | Now (Oct 22, 12:45 UTC) | Fan funding | YPP by Jan 31 (10M) | YPP from Feb 1 (20M) |
|---|---|---|---|---|
| Subscribers | **29** | 500 | 1,000 | 1,000 |
| Uploads | 1 posted (S01); 3 more drafts finished | 3 in 90 days: met by ~Oct 24 at 1 a day | n/a | n/a |
| Qualified views | ~2.6K (4,866 public × 0.54) | 3M | 10M | 20M |
| Needed per Short at **1 a day** (the ElevenLabs Creator plan) | S01: 4.9K on day 1 | ~62K | ~206K | ~412K |
| Needed per Short at 2 a day | | ~31K | ~103K | ~206K |

- **Subscribers:** S01 brought ~6 subs per 1,000 views (n=1; MetaSports runs at 0.44). Even at 1 per 1,000, 1,000 subs takes ~1M views, long before 10M. **Views are the gate here too.**
- **Benchmark:**
  - Ahmed's Goal ran 162-270K monthly medians in Jul-Oct 2026, at 2-3 a day.
  - **The 10M-by-Jan-31 path needs Ahmed-level medians from about week 2. [Inference] Unlikely.**
  - Fan funding (31-62K per Short) is a realistic first target if the format holds.
- **Cost:** 2 a day needs ~180K ElevenLabs credits a month, more than the Creator plan's 100K. Doubling the cadence halves the per-Short bar.

---

## 6. Real examples
I found **no credible public report** giving an exact time-to-YPP for a sports facts or story Shorts channel. The vendor blogs (EasyViral, RenderFoot) give only hypotheticals. Here is what there is.

**Ahmed's network (our Oct 21 study; [Repo] + [Inference]):**
- **Caveats:**
  - These are lifetime views, not 90-day views, and public, not engaged.
  - Most upload dates are interpolated.
  - **No channel publicly confirms its YPP status.**

| Channel | How it started | Lifetime views of its first Shorts | Reading [Inference] |
|---|---|---|---|
| **Ahmed's Goal** | Mar-Nov 2024 at 5-23 Shorts a month, with 10-20K medians. Viral explainers in Oct 2024 (9.4M, 5.4M), then ~50 a month from Dec 2024, and 300-500K medians from Feb 2025 | First 40: only 2.8M; first 55: 10M+ | Took **~9-10 months and a format change** to reach a 10M-a-quarter pace |
| **Ahmed's Basketball** | Launched Dec 10, 2024 with the proven format at ~2 a day (30 in Dec, 58 in Jan); the first 117 Shorts had a 198K median | First 34: 10M+; first 61: 20M+ | Likely crossed 10M in 90 days within **~1-2 months** |
| **Ahmeds Business** | Launched Jan 2026 with ~39 Shorts that month, including 17M, 8.3M and 7.9M hits | First 5: 10M+; first 11: 20M+ | Likely cleared even the 2027 bar within **weeks** |

- **The lesson:** the operator's later channels launched hot. His first one needed most of a year.
- Even this network's medians fell at 3 a day (summer 2026), and Basketball dipped to 53-104K in Aug-Nov 2025.

**Kapwing's faceless sports Shorts test** [Press] Kapwing, Jan 2025:
- **The channel:** sports and athlete stories, narrowed to gymnastics, with an ElevenLabs "Adam" voice over B-roll.
- **Output:** 60 videos in 157 days (one every ~2.5 days). 1,000 subs on day 157; ~1.1M total views; ~500K Shorts views in its last 90 days.
- **Not monetized** after 6 months.
- **It was terminated once** for "spam or deceptive practices", and reinstated within an hour on appeal.

**NBA story channel for sale** [Press] Empire Flippers listing:
- Mainly long-form, about one NBA legend: game footage, interviews and the owner's own narration.
- Monetized since Jun 2022, with no strikes reported.
- It shows footage-plus-original-narration channels can get into YPP, but it isn't a Shorts or AI-voice case.

**Locked On** [Press] Sportsepreneur:
- Monetized daily team shows using clips.
- Owned by the media company Tegna, which may hold rights deals.

---

## 7. The biggest risks to approval, ranked
1. **Views, not policy, are the binding gate on both channels.**
   - MetaSports needs ~5x its pace for fan funding, ~16x for 10M by Jan 31, ~33x for 20M after.
   - FC needs 31-62K per Short for fan funding.
   - **Plan:** fan funding first; full YPP on the 20M bar after Feb 1.
2. **FC's long Shorts with broadcast footage.** One claim on a >60 s Short blocks it, so its views never count. Takedowns become strikes that can reach linked channels. **Fix this before posting S02, S03, S05, S06, S07 as they are.**
3. **MetaSports' most-viewed and off-theme history:**
   - the old-era bare-moment Shorts;
   - 8 AI/Sora memes (including a real person);
   - duplicates;
   - a mismatched About text.

   Reviewers look at these first. **Clean them up before applying.**
4. **The template look**, on FC especially: a copied format, a reused music bed, repeated titles, two channels from one pipeline. **Vary it, and keep proof of the human research.**
5. **Overstated progress.** Only ~54% of public views qualify. Track Studio > Earn, not the public counter.
6. **After joining:** from Feb 1, 2027, Shorts pay only flows while the channel holds 10M qualified views per 90 days. Plan income (Shopping, brand deals, long-form) around that.

**Before you apply (either channel):**
- [ ] Studio > Earn shows both thresholds met.
- [ ] 2-Step Verification, AdSense and advanced features are set up.
- [ ] The top 20 most-viewed and the 10 newest Shorts are all narrated, original explainers.
- [ ] No off-theme, AI-meme or duplicate uploads.
- [ ] The About text describes the original work.
- [ ] No active strikes. Claims reviewed.
- [ ] The process video is recorded (unlisted, under 5 minutes, channel URL in the first 30 s).

---

## Sources (all read Oct 23, 2026)
**YouTube (official)**
- YPP overview and eligibility: https://support.google.com/youtube/answer/72851
- Expanded YPP: https://support.google.com/youtube/answer/13429240
- YouTube Blog, "Partner Program updates for 2027" (Aug 10, 2026): https://blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/
- Channel monetization policies (inauthentic, reused, off-putting, AI personas): https://support.google.com/youtube/answer/1311392
- Shorts monetization policies (Creator Pool, ineligible views): https://support.google.com/youtube/answer/12504220
- Disclosing altered or synthetic content: https://support.google.com/youtube/answer/14328491
- Three-minute Shorts (claims block >1 min): https://support.google.com/youtube/answer/15424877
- Manage Shorts as a rights holder: https://support.google.com/youtube/answer/13053317
- Learn about Content ID claims: https://support.google.com/youtube/answer/6013276
- Copyright strikes: https://support.google.com/youtube/answer/2814000
- What content can I monetize: https://support.google.com/youtube/answer/2490020
- Why was I rejected for monetization: https://support.google.com/youtube/answer/9235730
- Appeal a YPP rejection or suspension: https://support.google.com/youtube/answer/9564590

**Press and analysis**
- The Next Web, 2027 YPP changes (Aug 10, 2026): https://thenextweb.com/news/youtube-partner-program-doubles-entry-requirements-2027
- Shacknews, 2027 thresholds: https://www.shacknews.com/article/150324/youtube-partner-program-minimum-qualified-public-watch-hours-shorts-views
- Hypebeast, 2027 thresholds (Aug 12, 2026): https://hypebeast.com/2026/8/youtube-partner-program-doubles-watch-hours-for-2027
- Search Engine Journal, Shorts view counting (Mar 2025): https://www.searchenginejournal.com/youtube-changes-shorts-view-counts-no-change-to-monetization/543005/
- Search Engine Journal, Jul 2025 inauthentic-content clarification: https://www.searchenginejournal.com/youtube-monetization-update-spam-not-reaction-channels/550755/
- PPC Land, qualified Shorts views (Aug 2026): https://ppc.land/shorts-watched-as-ads-do-not-count-toward-youtubes-20-million-view-bar/
- PPC Land, eligibility FAQ (Oct 2025): https://ppc.land/youtube-clarifies-partner-program-eligibility-metrics-for-watch-hours/
- Relevant Audience, first-frame view counting (Aug 18, 2026): https://www.relevantaudience.com/youtube/youtube-first-frame-view-count-24-august-2026/
- Agentio, view vs engaged view: https://www.agentio.com/blog/youtube-view-vs-engaged-view
- Tubefilter, Jul 2026 policy clarification: https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/
- TechCrunch, AI slop clarification (Jul 20, 2026): https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/
- TechRepublic, AI monetization rules (Jul 21, 2026): https://techrepublic.com/article/news-youtube-ai-video-monetization-rules
- PiunikaWeb, Jan 2026 enforcement reports: https://piunikaweb.com/2026/01/12/youtube-inauthentic-content-policy-enforcement-reports/
- Let's Data Science, faceless crackdown (weak source): https://letsdatascience.com/news/youtube-cracks-down-on-faceless-creators-monetization-e3bb5892
- AIR Media-Tech, dated policy timeline: https://air.io/en/monetization/youtube-monetization-policy-changes-2026-a-complete-dated-timeline
- AIR Media-Tech, Shorts RPM from 274 channels (Sep 2026): https://air.io/en/air-data-findings/youtube-shorts-rpm-vs-long-form-how-much-do-shorts-earn-in-2026
- Digiday, NBA creator footage program (Oct 2024): https://digiday.com/marketing/why-the-nba-is-helping-basketball-creators-make-longer-youtube-videos/
- Net Influencer, NBA creator access 2026-27 (Oct 21, 2026): https://www.netinfluencer.com/nba-expands-creator-access-tiktok-tap-to-watch-links-ahead-of-2026-27-season/
- Sportsepreneur, monetizing sports content you don't own (Aug 2025): https://sportsepreneur.com/how-youtubers-are-monetizing-sports-content-without-owning-it/
- SportBusiness, Premier League v YouTube settled: https://media.sportbusiness.com/news/premier-league-settles-youtube-copyright-case/
- Kapwing, faceless channel to 1,000 subs (Jan 2025): https://kapwing.com/resources/we-grew-a-faceless-youtube-channel-to-1000-subscribers
- Empire Flippers, NBA channel listing #94475: https://empireflippers.com/listing/94475/

**Vendor and creator blogs (lower weight)**
- vidIQ, Shorts monetization 2026: https://vidiq.com/blog/post/youtube-shorts-monetization/
- vidIQ, why monetization is rejected: https://vidiq.com/ru/blog/post/types-youtube-channels-dont-get-monetized
- Clippie, World Cup footage on YouTube (Jun 2026): https://clippie.ai/blog/can-you-post-world-cup-highlights-youtube-2026
- RenderFoot, faceless football channels (Jun 2026): https://www.renderfoot.com/blog/faceless-football-youtube
- EasyViral, 10M Shorts views in 90 days: https://easyviral.ai/blog/10-million-shorts-views-90-days-ypp-threshold-2026
