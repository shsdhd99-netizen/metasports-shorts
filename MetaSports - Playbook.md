# MetaSports — The Playbook (Round 2)

> ## Oct 13, 2026 update (read first; it overrides any older line below that conflicts)
> Evidence: `Research Notes/Winning Formula v2 (Oct 13, 2026).md`, `Handoff Audit (Oct 13, 2026).md`, Outcome Log Oct 13. [V] = verified, [S] = supported (several observations), [H] = hypothesis under test.
> 1. **Screen the premise before any production** [S]. A non-fan must get, in second 1, ONE visible thing that "can't be right" (a jersey number, a height, a shooting form, a vote, a minutes total), stated in the first sentence in plain words. All 3 Oct breakouts (#22 31.8K, #03 27K, #19 20.4K) and 6 of 9 old breakouts fit; news recaps, contracts/picks and "role player as the way in" did not (#12, #13, #29: 1-3K). Two other routes exist (celebrity controversy: "Why Does No One Like Bronny" 79K; family/emotion: #23 6.5K, best like rate), so this is the default, not the only door.
> 2. **The ending answers the opening, then stops** [S]. This replaces "end on something to argue about" (section 3 below): our debate-question/CTA endings (#12, #18) stayed under 3K and Duren had a cliff at 8-10 s; the payoff endings (#03, #22, #19) broke out. Best: the subject's own voice or one number, over the opening image. The debate question goes in the pinned comment.
> 3. **One measure per Short** [S]: each new fact every 2-3 s moves the same measure (heights, owners of a number, minutes). #29 used 6 numbers on 5 measures.
> 4. **Never retell a story a bigger channel already did** (rule 1 below) [V]. #29 broke it (CoachClank's underhand story has 10M views; ours did 1.0K). Retelling our own old winner by name does not carry over.
> 5. **Craft scores do not choose the posting order** [V]. The Round 3 critic score ran backwards against real views (Spearman −0.63, n=14). The critic now judges premise and first second first (`Tools/critic_v2.md`); polish items only catch defects.
> 6. **Technical gates** [V]: no clip replays (`qa_short.py` fails them; `assemble.py` no longer loops), voice audible from 0.0-0.4 s, -14 LUFS, no frozen frame over 0.5 s. Warn: a card/screenshot in the first 4 s [H: the top 4 Oct posts had none before 7 s].
> 7. **Red circle/arrow on the detail in frame 1** [H]: old era 7/27 vs 2/44 reached 40K+ (one coder). Test it in pairs with `Tools/pointer.py`; don't adopt it until 2 of 3 pairs win.
> 8. **Voice** [V]: still one voice as the brand, but the choice is the owner's ear (blind lineup: `Research Notes/Voice Lineup (Oct 13, 2026)/`). Never time-stretch; pause trimming only inside measured silence (`voice_fx.py`, fixed Oct 13).
> 9. **Posting time** is unresolved: this Playbook says 6-11 AM ET, the Oct roadmap tested 12:30 PM / 7:30 PM, and our own data has no post times yet. Don't treat either as proven.

*Built only from the AI NBA story-Shorts niche: CoachClank's full channel (all 432 Shorts; 203 with dates and likes), 7 other channels in the niche, frame-by-frame watches of 12 Shorts, and 180 top comments. Checked Sept 26, 2026.*

---

## First, the honest answer to "is this bs?"

**Round 1's facts were real, but it compared you to the wrong channels** (general NBA-facts channels, not AI NBA story channels), and some of its advice was generic. Four things it told you were wrong for this niche:

| Round 1 said | The niche actually shows |
|---|---|
| Use your own voice | **A fast AI voice is fine.** 0 of 180 top CoachClank comments even mention the voice. |
| Slow down to ~170 words/min | **CoachClank talks at ~260–290 words/min.** Fast is the style. |
| Write keyword descriptions | **CoachClank uses no description and no tags at all.** |
| Your problem is subscriber conversion | **This niche converts low.** CoachClank: 0.13 subs per 1,000 views, yours: 0.21. **Your problem is reach per Short.** |

Everything below is only what the winners actually do.

---

## The benchmark: CoachClank

| | |
|---|---|
| Channel started | **May 31, 2025** (16 months ago) |
| Today | **144K subs · 432 Shorts · ~1.09 billion views** |
| A typical Short | **~500K views** (median) |
| Uploads | ~6 per week, every week |
| Length | median 20s |
| Length vs views | 21–30s → median 765K · 31–45s → median 1.13M · ≤20s → median 321K |
| Titles | 4–7 words, often a question; 1 emoji optional. No hashtags. (Round 3 data: Tools/data/title_patterns.md) |
| Its second-ever upload | "Kobe Bryant's FINAL GAME…" → **5.2M views**. New channels *can* pop fast in this niche. |

Other channels in the same niche, as proof it isn't one lucky guy:

| Channel | Subs | Typical Short | Best Short | Format |
|---|---|---|---|---|
| Ahmed's Basketball | 120K | ~99K | 822K | ~70s list stories ("NBA players who showed up unrecognizable after one summer") |
| Hoop Facts (started Nov 2025) | 51K | ~37K | 2.0M | 20–70s fact stories ("When The Spurs Memed Shaq") |
| Hoops Lore (started Jan 2026) | 16K | ~34K | 9.2M | 60–130s player-told stories |
| Med | 455K | ~772K | 1.5M | 2K "what if" simulations |
| Rebound Rewind | 234K | ~191K | 1.4M | "Every team's ___" lists |

---

## Why you're stuck at ~30K (the real reasons)

### 1. You retold stories that had already gone viral

Same topic, same facts, same length:

| Topic | CoachClank | You |
|---|---|---|
| Why no one shoots underhand | **10,000,000** | 73,000 |
| Dunking without jumping | **2,700,000** | 56,000 |
| The airless basketball | **23,000,000** | 44,000 |

The audience already saw it. Pauly Walnuts makes the same point about his own niche: people just watch the creator who made it first.

**Rule: never retell a story a bigger channel already posted.** Retelling *your own* winners is fine — CoachClank did the underhand story twice (10M, then 2.9M).

### 2. Your first line is a quiz. Theirs is a scene.

> **Round 3 check:** of CoachClank's 8 biggest 2026 Shorts, 6 open on a scene, a claim or a broken rule, 1 on a mystery question ("Why did this player…?") and 1 on "Did you know". A scene is the safe default; a mystery question works too.

| Topic | Your first line | CoachClank's first line |
|---|---|---|
| Underhand free throws | "Ever wonder why underhand free throws disappeared?" | Starts on the scene: fans mocking a player for shooting underhanded, even though he's making them. |
| Dunking without jumping | "Is it possible to dunk without jumping?" | Asks the question, then instantly explains why even the tallest players still have to jump a little. |

Quiz openers ask the viewer to care. Scene openers put them *in* the moment.

### 3. You end on a fact. They end on something to argue about.

- CoachClank's underhand Short ends on Shaq saying he'd rather miss every free throw than look silly shooting underhanded.
- The top comment, with **48,000 likes**, just argues back that missing every free throw looks worse.

That argument in the comments is what spreads the Short.

### 4. You stopped

- **You:** 80 Shorts in 3.5 months, then 7 months dark.
- **CoachClank:** ~6 a week for 16 straight months.

---

## The recipe (what every MetaSports Short looks like now)

**Length:** stories 22–40 seconds (about 90–170 words); quick moments 15–25 seconds. CoachClank's 31–45s Shorts have the best median, and his 8 biggest 2026 Shorts ran 22–34s (Research Notes/Round 3 - Deeper Findings.md). Post between 6 and 11 AM ET.

**Voice:**
- One AI voice, fast (~250 words/min).
- Always the same voice — that's your brand.

**The 3-part script:**
1. **Open with one of these 4** (the four opener types CoachClank uses — templates, fill in your moment):
   - **A scene:** "Fans were laughing at [player] for…"
   - **A rule:** "In the NBA, there's an unwritten rule that…"
   - **A strong opinion:** "[Player] has to be the most ___ player ever."
   - **The stakes:** "It's [player]'s last game, they're down 10 with two minutes left."
2. **The turn:** "But…" / "However…" / "You see…" → the unexpected part. Add one opinion line of your own, e.g. "But honestly, the funniest part is…"
3. **End on a punchline, a consequence, or a quote people will argue with.** Then stop. No "subscribe," no summary.

**Visuals:**
- The actual moment on screen from second one.
- Small, clean captions, 2–3 words at a time.
- Your red circles are fine.

**Title:**
- **4–7 words, often a question** (What / How / Why…?), no hashtags, 1 emoji optional as the viewer's reaction. Round 3 data: 6–7 words and question titles win (Tools/data/title_patterns.md).
- CoachClank's biggest recent titles:
  - "He Didn't Have To Do That 😭" (20M)
  - "This Cost Them The Game 😭" (7M)
  - "James Harden Makes No Sense 😭" (3M)
- No hashtags. Don't bother with the description.

**The kinds of moments that hit** (CoachClank's top 30):

| Kind of moment | Example | Views |
|---|---|---|
| Size mismatches | "6'8 vs 7'9" | 30M |
| | "WNBA Player vs High School Kid" | 32M |
| Wholesome/respect moments | "NBA Player Teaches Manners" | 26M |
| Rule weirdness | "This Cost Them The Game" | 7M |
| | "The Unwritten Triple Double Rule" | 6.4M |
| Funny/petty players | "He Didn't Have To Do That" | 20M |
| | "200 IQ LaMelo" | 11M |
| "What happened to…" | "…the 7'7 Basketball Teen?" | 14M |
| Legendary moments with stakes | Kobe's 60-point finale | 5.2M |

---

## The one habit that matters most: fresh moments, daily

The season tips off **Oct 20**. Every game night creates moments nobody has told yet — that's your edge over retelling.

**The daily loop (~45 min):**
1. **Morning (15 min):** scan last night's highlights, NBA Reddit and NBA X/Twitter. Pick **one** moment that's funny, petty, weird, rule-related or wholesome.
2. **Check it's fresh (2 min):** search YouTube Shorts for it. If a big channel already told it, skip it or find a different angle.
3. **Write (10 min):** `/nba-short [the moment]` — it now follows this recipe.
4. **Build + post (20 min).** Same time every day.

**Target: 6–7 Shorts a week, every week.** Before opening night, use the 10 ready scripts in *MetaSports - Scripts (Batch 2)*. They're storylines CoachClank hasn't touched.

---

## Stop doing these

- Retelling CoachClank's (or anyone's) viral stories
- Quiz-question first lines
- Titles over 5 words, hashtag walls, "Subscribe if you love cake" descriptions
- Fight clips and off-topic AI comedy (your own data: they flopped)
- Going dark. If life gets busy, post fewer, but never zero.

---

## Money & risk (short version)

- **Shorts ad money:** from Feb 1, 2027, Shorts only pay in months when you have **10M+ Shorts views in the last 90 days**. CoachClank clears that easily; you'll need CoachClank-style reach first. Build reach now, money follows.
- **NBA footage:** every channel in this niche uses it, and claims happen. Keep Shorts **under 60 seconds** — claimed Shorts over 1 minute get blocked. Your narration + story is what makes it "yours" under YouTube's rules. Pure clip reposts with music are not.
- **AI:** fake realistic videos of real players are the one AI move to avoid (removal risk + a label required). An AI *voice* is fine.

---

## Your next 14 days

> **Round 3:** the full plan with checkpoints through Dec 27 is in **Roadmap - Next 90 Days**.

| Day | Do |
|---|---|
| 1 | Pick your one AI voice and set it to fast. Change the display name to "MetaSports." |
| 2–10 | Post the 10 Batch-2 scripts, one a day (dates are on each script). |
| 3 onward | Start the daily fresh-moment loop in the background: collect moments now, use them from opening night on. |
| 7 | First check-in. Which openers and titles got the most views in the first 48 hours? Do more of that. |
| 14 | Opening-night week is next: switch to 100% fresh moments from last night's games. |
