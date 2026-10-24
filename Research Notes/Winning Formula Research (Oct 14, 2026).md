# Winning Formula Research (Oct 14, 2026, night)

**Purpose:** the evidence behind the one-page **Winning Formula** at the top of `MetaSports - Playbook.md`. This doesn't repeat earlier work; it cites it.

Evidence tiers:
- **[V]** measured on our files or data
- **[S]** small-n support
- **[H]** hypothesis
- **[E]** external

## 1. What was inspected (and what could not be)
| Source | What | How |
|---|---|---|
| **Our best Shorts** | Curry Kobes (daIsE50TcoQ, 30.8K) and Giannis game ball (pr-JQuzAUxY, 28.3K): full transcripts | YouTube auto-captions saved Oct 13 (scratchpad `formula/yt/*.vtt`) |
| **Our old era** | 12 old Shorts, narration exactly as voiced, with views | `Library/Reference Videos - old Shorts transcripts.md` |
| **Our new era** | 22 new Shorts: views, avg % viewed, voiced length, words, wpm, first sentence | `Research Notes/Posted Shorts - metrics (Oct 14, 2026).csv` |
| **CoachClank** | 2 full videos watched: "Alley Oop Three" and "Shaq vs Normal Person" (60 s TikTok versions); 148 YouTube Shorts with views and lengths | Round 9 watch reports; yt-dlp metadata pulled Oct 4 (`r5/CoachClank_full.json`) |
| **Ahmed's Basketball** | 1 full video watched: "1% chance of NBA success", 102 s; 120 Shorts titles with views | Round 9; Round 5 |

**Blocked tonight:**
- CoachClank's actual top YouTube Shorts (30.9M "6'8 vs 7'9", 21.5M "He Didn't Have To Do That") could not be watched.
  - YouTube refuses this server ("Sign in to confirm you're not a bot", retested Oct 14 21:15 UTC).
  - The TikTok profile page shows "Something went wrong" to an automated browser, so its video list can't be read.
  - Web search doesn't index their TikTok posts.
- vidIQ has 5 credits (a watch costs 10).
- **So the CoachClank evidence is:** 148 view counts and lengths, plus 2 longer TikTok story videos, not the viral 15-28 s set. Said plainly so nobody over-reads it.

## 2. Measurements
**A. Length.** [V on their data; S as a rule for us]
- **CoachClank YouTube Shorts:**
  - 20-62 s: 848K median (n=72)
  - under 20 s: 299K median (n=73; 145 Shorts have a length)
- The gap holds in both halves of their upload history:
  - Mar-May: 439K vs 269K
  - May-Aug: 1.03M vs 376K
- Their top 15 run 12-54 s (median 22 s).
- **Our old hits were voiced at 20-32 s.** Curry Kobes is 84 words and Giannis 85 words, about 22-24 s at our pace.
- **Our new Shorts are all 21-29 s.** So length did not separate our new winners from our new losers.

**B. Retention separates our winners from our losers.** [V]
- New-era winners (#22 31K, #03 26K, #19 20K): 103-116% avg viewed.
- Losers (#11, #20, #25, #12, #35, #16): 63-80%.
- Same as the audit's Spearman +0.52.
- But #14 had 115% and only 1.6K, so retention is **necessary, not sufficient** (audit §1).

**C. CoachClank title lanes** (n=148, median 449K): [V on their data; S for us]

| Lane | n | Median vs channel |
|---|---|---|
| "Why…" rule curiosities ("Why No One Shoots Underhand" 10.9M) | 9 | ×2.1 |
| "IQ" plays ("200 IQ Defense" 12M) | 6 | ×2.2 |
| Titles that open on "He/This/They" (a moment) | 30 | ×1.4 |
| A named star | 33 | ×1.2 |
| " vs " matchups | 15 | ×0.6 (yet "6'8 vs 7'9" is their #1) |
| Wholesome fan moments ("Baby Takes Her First Steps", "Crowd Cheers for Fan") | — | their bottom 10 |

**D. Our two best Shorts, line by line** (both are format 2, "moment + hidden detail"): [V]

| Beat | Curry Kobes (30.8K) | Giannis game ball (28.3K) |
|---|---|---|
| Line 1: a statement with "just" plus the star | "Stephen Curry just pulled one of the wildest sneaker moves the NBA has ever seen." | "Giannis just saved a rookie's first NBA memory." |
| The concrete detail | "…wearing Nike Kobes. Not customs, not tributes, actual Kobes." | "…the refs refused to give him the game ball." |
| Proof/reaction | "People courtside were pointing at his feet…" | "He walked right over and grabbed the ball…" |
| The turn | "**But the craziest part,** Under Armour executives were in the arena…" | "He handed it straight to Luka Doncic so he could pass it to the rookie himself." |
| Payoff | "Curry still drops 30 like nothing happened." (then a CTA) | "A small move by Giannis that turned into a moment this rookie will never forget." (feeling line) |

**E. The old scripts vs the new scripts** (audit §11): [V counts; S for the effect]
- The old scripts tell a story: 14.8-word sentences, escalation 5/12, reframe endings, personality asides.
- The new scripts chain facts: 9.4 words a sentence, escalation 2/20, 0 reframes.
- Same voice (0.93-0.95 speaker similarity), so **the voice is not why the old ones won.**

**F. Openings.** [V]
- Old and best Shorts open on a statement: 11/12 old voiced, plus Curry and Giannis.
- CoachClank 1 of 2 watched, Ahmed's 1 of 1.
- CoachClank's question titles: ×0.6.
- Every reference narrator starts speaking at 0.0 s and talks to the last frame.

## 3. The patterns, sorted
**Supported by several independent examples** (ours + references):
1. **Line 1 states the surprising thing about a named subject, within about 3 s, as a statement.**
   - Ours: old 11/12, Curry, Giannis, #22, #03, #19.
   - CoachClank's "This guy just created the alley-oop three"; Ahmed's title-as-hook.
2. **The footage IS the moment being described.**
   - Old hits: 8/11 and 11/13 exact-moment shots.
   - CoachClank: 0 cards in about 52 shots.
   - Critic failures came from stand-ins.
3. **Story voice with one turn:** "But the craziest part…", "Then it gets crazier", "but not this time, because…".
   - Curry, Quentin Post, Korver, the WNBA one, Alley Oop ("This is what happens when…").
4. **Lanes that travel:**
   - rule/record paradoxes ("Why…", #22, #03, Korver, Disaster Draft)
   - a star's visible moment with a hidden detail (Curry, Giannis, Bronny 1v1)
   - basketball IQ / "how is that legal"
5. **Payoff = a reframe or the feeling, then stop.**
   - Giannis "a moment this rookie will never forget", Korver "one of the deadliest shooters", Quentin Post "sometimes in the NBA that's all it takes".
6. **Voice from 0.0 s to the end, no dead air.** All references, and our QA already enforces it.
7. **Retention ≥100% is the bar our winners clear.** Necessary, not sufficient.

**Promising but limited:**
- **20-30 s single-story length.** CoachClank's 20-62 s Shorts get 2.8× the median of their under-20 s ones (n=145), and our old hits were 20-32 s. Our new posts already sit here, so it's a guard rail, not a lever.
- **Fresh "just happened" moments** posted within a day or two: Curry, Giannis, Bronny 1v1 (65K). Counter-examples: LeBron's pay cut (3.9K), 3 Plays Bronny (4.9K).
- **A quiet music bed:** all 5 old Shorts watched; CoachClank's own mix. It did not separate hits from misses (Music Guide §1).
- **Faster narration** (CoachClank 265-309 wpm). Our old hits ran 206-252. Not shown to matter.

**Creator-specific (don't copy):**
- CoachClank's own narrator, their 265-309 wpm, and kids/amateur clips.
- Ahmed's 60-120 s "Players who…" list compilations, with AI-style stills. A different format; Ahmed posts 2× as often for 1/5 of CoachClank's median (Round 5).
- Emoji-heavy titles. Their emoji titles do better, but titles barely move our reach (94.5% of our views come from the feed).

**Personal preference (the owner's, kept as rules):**
- no hook headline text
- white Montserrat captions
- music on by default
- no vine boom

## 4. Rules this challenges
| Rule | Verdict |
|---|---|
| "Pace: the old hits measured 182-212 wpm" (Playbook §5/§6, Voice README) | **Wrong.** The voiced old hits measured 206-252 (median 220). Corrected. |
| "The voice reads numbers flat, which is why the new ones flop" | **Not supported.** The old hits were just as flat. |
| 10 experiments open at once (Playbook §7) | **Too many** for 1-2 posts a day; nothing reaches n=3. Freeze to one test at a time (Winning Formula). |
| Q1 "question hook vs statement hook" | **Demote.** Statements are the supported default (§2F). Q1 stays parked. |
| "Fact chain, one measure, a new fact every 2-3 s" (format 1 context) | **Revise:** keep one measure, but tell it as a story with a turn (pattern 3). |
| Three formats | **Keep**, but name format 2 (moment + hidden detail) as the first choice whenever a fresh moment exists: it's our two best new-era-adjacent hits. |
