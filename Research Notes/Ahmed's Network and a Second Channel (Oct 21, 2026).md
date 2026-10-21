# Ahmed's network: deep dive, and how we'd copy the system (Oct 21, 2026)

**Owner's asks:**
- "do you think you could replicate your entire skillset in order to automate another channel? separate info bases, but different niches. research 'ahmeds basketball' and all his channels"
- Then: "there are bigger channels than that! he has a business channel, etc. look harder and do an actual deep dive."

**How the data was gathered.** Public data only (no login, no cookies), read Oct 21, 2026, 16:00-17:30 UTC.
- **Channel listings:** every Short on all three YouTube channels, with view counts (3,154 Shorts). Kept in `Research Notes/Ahmed Network Data (Oct 21, 2026)/` as CSV, together with the analysis script and its output.
- **Upload dates:** read for 226 Shorts spread evenly across each channel's history. Dates for the others are interpolated, so monthly figures are approximate.
- **Transcripts:** 7 YouTube transcripts (YouTube captions via Parallel web_fetch), plus 1 more from the earlier study.
- **Watched:** 2 Shorts frame by frame through their TikTok copies (`Tools/watch_short.py`).
- **Other sources:** About panels, RSS upload feeds (exact upload times), TikTok profiles and cover frames.

## 1. The network
**I searched for more channels, and these three are all I found:**
- About 200 handle and name variants, e.g. @AhmedsX for 100+ niches.
- 400 YouTube channel-search results for "Ahmed's".
- 38 TikTok handles.
- Web searches.
- Featured-channel tabs: none set.

There may be channels under other names. If you know one, send it and I'll add it.

| | **Ahmed's Goal** (soccer) | **Ahmed's Basketball** | **Ahmeds Business** | Network |
|---|---|---|---|---|
| YouTube subs | 424K | 121K | 86.6K | **632K** |
| YouTube views | 752.9M | 377.5M | 187.4M | **1.32B** |
| Videos | 1,373 | 1,175 | 615 | **3,163** |
| Channel created | 2013; Shorts from Mar 2024 | Dec 10, 2024 | Jan 3, 2026 | |
| Median views per Short (all-time) | **276,000** | 159,000 | 49,000 | |
| Shorts at 1M+ | 187 (13.7%) | 68 (5.8%) | 36 (5.9%) | 291 |
| Shorts at 100K+ | 82% | 67% | 32% | |
| Biggest Short | 10M "Players who used to be stars but fell off" | 7.1M "Draft picks that were supposed to be bad but were incredible" | **17M** "Moments where businesses accidentally created their biggest competitors" | |
| TikTok followers / likes | 391K / 64.6M | 105K / 21.8M | 24K / 3.2M | **520K / 89.6M** |
| Instagram | @ahmedsgoal, about 131K (search result, not verified) | | | |

For comparison, our channel: about 550 subs and a 3,600 median over the last 7 Shorts.

**Why I say it's one operator (strong circumstantial evidence; no page states it):**
1. **Matching TikTok bios:** "Daily Football Content! Follow So You Don't Miss It" / "Daily Basketball Content - Follow To Stay Updated" / "Business content posted daily! Follow so you don't miss it".
2. **Same title machine:** 121 concepts are word-for-word identical between Basketball and Goal once the sport words are removed. Business reuses sports templates: "Craziest ways that players got cut" became "Craziest ways that CEOs got fired" (2.6M).
3. **Same batch-scheduling habit:** Basketball and Business both upload in bursts a few minutes apart in the same UTC windows (Basketball 02:08-02:11, 16:08-16:13, 21:07-21:22; Business 01:41-01:43, 15:39, 20:39-20:50), and both were active and quiet on the same days in October.
4. **Same packaging:** identical script structure, caption look and runtime band; no description; no tags.

**Ahmed's NFL (@ahmedsnfl, 1K subs) is probably not his:** different bio ("I rank and edit viral videos"), different format (Top-10 ranking edits with hashtags in the title), a fixed 12:00 UTC daily slot.

## 2. How it grew
- **Goal:**
  - Ran small from Mar 2024: 5-12 Shorts a month, medians 10-20K.
  - Two explainers went viral in Oct 2024: 9.4M "What happened to North Korea after the World Cup?" and 5.4M "He made over $1 MILLION by losing".
  - In **Dec 2024** it jumped to about 50 Shorts a month in the "Players who…" story format.
  - From Feb 2025 its monthly medians sat at **300-500K**.
- **Basketball** launched in the same month (Dec 2024) with the same format. It ran 50-60 a month from Jan 2025, with monthly medians of 150-290K.
  - It dipped to 53-104K in Aug-Nov 2025, then recovered to 250-286K in Feb-Apr 2026.
- **Business** launched Jan 2026. Its first month's median was 326K, with hits of 17M, 8.3M and 7.9M. Then volume rose and the median fell to 31-48K.
- **Summer 2026 push:**
  - Volume went to 84-103 Shorts a month per channel (about 3 a day) in Jul-Sep 2026.
  - Medians fell at the same time: Basketball about 75K in Jul-Aug, Business 31-43K, Goal 190-270K.
  - Then they cut back hard: Basketball posted 29 in September and 10 so far in October.
- The data can't separate "more posts" from "the audience tiring", but more volume did not buy more views.

## 3. The format, piece by piece
**Script** (the same on all 3 channels; checked on 9 transcripts):
1. **Line 1 is the title, read word for word** at 0.0 s ("Companies that spent millions to ruin their own product.").
2. **The title sounds like a list, but the Short tells ONE story** (sometimes 2-3 escalating ones): Jaguar, Tropicana, Deco, Lance Allred, Beckham → Henry → Zlatan.
3. **A turn about every 8-12 s:**
   - "But…"
   - "There was just one problem"
   - "But all those angry comments turned out to be the least of Jaguar's problems"
   - "Here's the wild part"
   - "But that free kick was only the setup for what came three years later"
4. **It ends on a hard number or irony, with no question and no call to action:** "a 97.5% collapse", "that one design swap cost them $30 million", "27-0", "the first legally deaf player in NBA history".
5. **Length and pace:**
   - 58-167 s (median runtime: Basketball 70 s, Goal 76 s, Business 71 s).
   - 231-263 words a minute (measured on 2 Shorts).
   - Some first-person asides ("the first ever match I witnessed in person"), so a person writes them.
   - I can't judge the voice itself.

**Pictures** (2 Shorts watched frame by frame):
- **Pace:** a new picture every 1.6-2.1 s (51 shots in 80 s; 45 in 93 s).
- **A literal picture for nearly every phrase:**
  - real game footage and photos for the facts;
  - stock or meme footage for abstract lines (a rotary phone for "the phone rang", a laughing face for "nobody had heard of them", a FIFA game settings screen for "easiest setting").
- **Framing:** horizontal clips sit over a blurred copy of themselves. Some clips play on a TV inside a branded room (an "@AHMEDSGOAL" backdrop).
- **Captions:** small white sentence-case words near mid-height, the same on all 3 channels.
- **Ending:** the last frame is a graphic (two club crests and "27 0").
- **Sloppy bits:** some borrowed clips still carry their original creator's captions.

**Packaging:**
- No description, no tags, no hashtags. Titles run 6-11 words.
- Title style changed over time: ALL CAPS until spring 2026, then sentence case with 1-2 CAPS words, now plain sentence case.
  - Older ALL-CAPS titles have higher medians, but they're also older, so that isn't proof the caps helped.
- **Series:**
  - A title that works gets reused with a new story each time; numbered "Episode 2…12" on 126 Basketball and 141 Goal titles.
  - Business ran 7 Shorts titled "Business ideas that failed but then succeeded when someone else tried them later".
  - Their cover frames confirm different stories under one title (Vans / UGG, and Agüero / Wan-Bissaka / Mendy).
- **Cross-posting:** the same videos go on TikTok (1,453 / 1,175 / 610 posts) and Instagram. YouTube auto-dubbing is on (seen on a Business Short).
- **Why 60+ s (my guess, not confirmed):** as of 2024-25, TikTok's Creator Rewards only paid on videos over a minute. All of their Shorts run longer than that.

## 4. What wins, by theme (title keywords; one Short can have several themes)
| Theme | Goal median | Basketball median | Business median |
|---|---|---|---|
| Refused / defiant ("players who refused to play…") | **826K** (n=17) | 103K | 51K |
| Records, oddities, "looks fake but is 100% real" | 332K | 150K | 62K |
| Comeback / revenge / glow-up | 311K | 146K | **91K** |
| Underdog / rejected / discovered by accident | 293K | 175K | 88K |
| Relationships (fathers and sons, enemies turned teammates, childhood hero) | 241K | 131K | 57K |
| Downfall / destroyed / fell off | 237K | **189K** | 53K |
| Money / contracts | 268K | 93K (lowest) | 52.5K |

Money and contract stories are the weakest sports theme here too, which matches our own data.

**Do ideas carry over between channels?**
- Ideas move both ways. Of the loosely matched Basketball/Goal pairs, Basketball posted first 315 times and Goal 194 times.
- A hit doesn't reliably transfer. When a concept beat 2x the median on Basketball, its Goal twin also did 33% of the time, against a 26% base rate.
- So the system runs on volume plus a large idea list, not on guaranteed repeats.

## 5. What it earns (rough)
- **YouTube:** Shorts ad pay is cited at about $0.03-0.10 per 1,000 views; AIR Media-Tech lists about $0.33 for US viewers. Over 1.29B Shorts views, that is roughly **$40K-$130K lifetime** from YouTube ads.
- **Other income:** TikTok rewards and anything they don't show publicly come on top.
- **Caveat:** these are blog and vendor figures, not their numbers.

## 6. Can we copy it? Yes. Here's the blueprint
Our pipeline already does the hard parts:
- research with sources;
- voice (ElevenLabs take + check);
- assembly with captions;
- the QA gate;
- copy-check;
- the Hub;
- daily stats.

To run an Ahmed-style network we'd add:
1. **An idea engine:**
   - A bank of title templates per niche, where every winner becomes a series (a new story under the same title).
   - Templates ported between niches: they did this, but only expect about a 1.3x lift.
2. **A 60-75 s story script template, in our own words:**
   - the title as line 1;
   - one story;
   - a turn every ~10 s;
   - escalation;
   - end on a hard number;
   - about 230-260 words a minute;
   - no call to action.
   We also keep our fact-check rule: every number gets a source.
3. **A literal-picture editor:**
   - one picture every 1.5-2 s;
   - real photos and footage for the facts, stock footage for abstract lines;
   - the blurred-background frame we already have;
   - an end card with the number.
   New piece: a stock-footage search (free licensed libraries) next to our X/ESPN/archive sources.
4. **Cadence:** about 2 a day per channel was their steady state. At about 3 a day their medians dropped.
5. **Cross-posting** the same file to TikTok and Instagram (you post).
6. **Separate knowledge bases:** each channel gets its own repo, notes, Hub and stats routine. Optionally, one small shared idea bank, which is the core of how this network works.

**Niche order I'd recommend:**
1. **Soccer.** The biggest audience for this exact format: 276K median, 13.7% of Shorts at 1M+.
2. **Business.** Proven 17M and 8.3M hits, mostly stock and news photos (fewer copyright claims than match footage), and business audiences usually earn more per view. But its median is lower (49K).
3. **Keep MetaSports (NBA).** Test this 60-75 s story format against THE #42 FORMAT on our own channel first. It's the cheapest way to learn whether the format travels.

**What you'd need to provide:**
- The new YouTube, TikTok and Instagram accounts and their names.
- A new GitHub repo added to the cloud environment.
- A bigger ElevenLabs plan. A 60-75 s script is about 1,500-1,800 characters, so 2 a day is about 100K+ a month per channel; Starter is 90K for everything.
- Your OK on each video. I still never post.

## 7. Limits of this study
- Upload dates for most Shorts are interpolated from 226 sampled dates.
- Views are lifetime totals, so newer Shorts are undercounted.
- Theme labels come from title keywords.
- Ownership is inferred, not stated by the channels.
- Only 2 Shorts were watched frame by frame; the rest is transcripts and cover frames.
- I can't hear audio, so the voice is not assessed.
