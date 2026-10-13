# MetaSports — The Playbook (Round 2)

## STRICT SHORT FORMULA (canonical, Oct 13, 2026). It overrides any older line below that conflicts.

**Evidence labels:**
- **A** = proven in this channel's data
- **B** = working hypothesis
- **C** = outside best practice
- **D** = a decision made for testing

**Confidence:** H / M / L.

**Evidence files:**
- `Research Notes/Winning Formula v2 (Oct 13, 2026).md`
- `Research Notes/Handoff Audit (Oct 13, 2026).md`
- the Outcome Log

**Queue:** `Production Queue.md`. **Critic rubric:** `Tools/critic_v2.md`.

**Nothing here guarantees views.** The rules come from 3 recent breakouts, 9 old ones, and about 20 recent non-breakouts.

### 1. Premise (decide this before anything is made)
- **Default story type:** ONE thing a casual fan can see that "can't be right" (a jersey number, a height, a pass, a vote, a minutes total), resolved in 20-26 s.
  - Evidence: all 3 Oct breakouts (#22 31.8K, #03 27K, #19 20.4K) and 6 of 9 old 40K+ Shorts fit. News recaps, contracts/picks and "role player as the way in" did not (#12 2.9K, #13 1.9K, #29 1.0K). **[A/B, M]**
- **Viewer emotion:** "how is that possible?" (surprise), then "huh, that's unfair/funny".
- **Two other routes exist and are allowed:**
  - celebrity controversy ("Why Does No One Like Bronny", 79K)
  - family/emotion (#23, 6.5K, best like rate)
  - **[A, L]**
- **Reject before scripting:**
  - a bigger channel already told the story (CoachClank's underhand: 10M, ours 1.0K) **[A, M]**
  - the facts need more than one measure
  - no footage proves the key line
  - the premise is only true with qualifiers we would hide

### 2. First second (line AND frame)
- **The first sentence states the paradox in plain words,** 10 words or fewer, with a name or number in it. Examples:
  - "Nikola Jokic's best pass ever doesn't even count."
  - "This man is listed taller than Victor Wembanyama."
  - **[B, M]**
- **Frame 1 is the object itself,** big enough to read at phone size (the player or the thing). Never a card, logo, wide crowd or headless crop. **[A for "no card": Oct top-4 posts had none before 7 s; B for the rest]**
- The voice starts by 0.4 s. There are 3+ shots in the first 3 s. No hook headline (owner rule, Oct 4). **[D]**
- **Optional test:** a red circle on the object in frame 1 (`Tools/pointer.py`). Old era: 7/27 Shorts with one reached 40K+, vs 2/44 without (one coder). **[B, L, being tested]**

### 3. Hook / Context / Payoff
- **Hook (0-3 s):** the paradox, over the object.
- **Context (3 s to about 75%):** every sentence adds a new fact **on the same measure** (heights, or assists in the book, or minutes that count), every 2-3 s. One short turn line ("It isn't." / "Still zero.").
  - No background stretch: Duren's cliff came at 8-10 s, exactly where exposition started. **[A, M]**
  - #29 used 6 numbers on 5 measures. **[A, L]**
- **Payoff (last ~25%):** the answer to line 1, as ONE number or the subject's own words, then stop. The last line plays over the opening image so the Short loops. **[A/B, M]**
- **No-filler rule:** a sentence that adds no fact, raises no stakes, answers nothing and sets up nothing gets cut. Script 90-100 words. **[C/D]**
- **Ending rule:** no question, no CTA, no hedge ("a little, maybe": #25, 68.4% viewed). The debate question goes in the pinned comment. **[A, M]**

### 4. Pacing map (from the measured voice, not fixed timestamps)
- **Clone voice, setting C:** 224-271 wpm measured (whisper), so 90-100 words = 21-26 s. Use `--speed 1.1` when auto 1.2 rushes short sentences (#41: 359-386 wpm at 1.2).
- **Slower voices (premade v3, ~176-181 wpm after pause trimming):** 70-80 words for the same length.
- Shot length follows the words: 1-2.5 s. Shot length did NOT separate winners from flops (Flagg 1.15 s average, same as the flops). **[A, M]**
- A shot can be shorter than its clip, never longer (`assemble.py` now slows ≤1.33x or holds; QA fails replays). **[A, H: a defect]**

### 5. Shot-to-line rule
- Every claim with a name or number has a picture that **proves** it: the right person on their name, the number visible (footage or a rich card), the quote on screen with its source. **[C, H]**
- **Cards:** only as proof, 25% of runtime or less, none in the first 4 s, text above the caption band (above ~45% height), readable at phone size. **[A/B, M]**
- **Repeats:** only on purpose (e.g. "watch it again"). No accidental loops. No burned-in source captions or tickers fighting ours (crop them). **[A, H]**

### 6. Captions, motion, sound, voice
- **Captions:** house style (white Montserrat, ALL CAPS, red/green emphasis), word-timed, in the 45-62% band, never over a face or the key action. Caption style did not separate winners (#03 used clank, #19/#22 house). **[A, M]**
- **Camera motion:** a gentle push-in (≤6%) on frame 1 and on stills only. No random zooms, no flash cuts (they washed out faces in the Oct 5 test). **[B, L]**
- **Sound:**
  - 2-3 effects, only where the picture makes the sound (a swish on a make) or on the single reveal line. No music by default. **[D]**
  - Mix: the voice at -14 LUFS integrated, limiter ceiling -2 dBFS, true peak ≤ -1 dBTP (QA warns above). **[C, H]**
- **Voice:**
  - One take of the whole script, never time-stretched beyond 1.08x.
  - Pause trimming only inside measured silence (`voice_fx.py`).
  - Check every take with the speech recogniser (`voice_check.py --stt whisper`): names and numbers must be heard correctly. **[A, H: verified defects Oct 13]**
  - Naturalness is the owner's ear (`Research Notes/Voice Lineup (Oct 13, 2026)/`).

### 7. Title and cover
- **Title:** 4-7 words, opens with Why/How/What/Did/Is, plus one emoji. It must be true to the fact sheet.
  - #17 went up as "Did The NBA Just BAN Flopping?" although flopping has been a technical since 2023-24. Never do that.
  - Title wording split views by less than 3K in the old era, so **the premise matters more than the title words**. **[A, M]**
- **Cover:** frame 1 (the object). The circled frame is used only for the pointer test.

### 8. Pass/fail gate before "ready"
**All must pass.** Run `qa_short.py`, `voice_check.py --stt whisper` and `voice_quality.py`, then Critic v2 as a separate agent, then the owner's listen.
1. The premise is clear to a casual fan in second 1 (write the question they would ask).
2. The first line is ≤10 words, specific, and creates the question.
3. Frame 1 shows the object.
4. Hook / Context / Payoff; one measure; every sentence earns its place.
5. Every claim is sourced with a date in notes.md; qualifiers are kept ("listed", "regular season", "reportedly").
6. Not a duplicate: copy check, the 39+ folders and both idea banks.
7. Every name/number beat has proof on screen; no claimed footage that doesn't exist.
8. Captions are readable and clear of faces, action and card text.
9. Voice: every word is heard correctly; no rushed (>330 wpm) or cut-off lines.
10. Sound effects only where the picture makes the sound.
11. The payoff answers line 1 and adds something; no CTA, question or hedge.
12. Title and cover are accurate.
13. Runtime 21-45 s (target 21-26), 1080x1920, -14 LUFS, no frozen/black frames, no replays.
14. The render was inspected (frame sheet plus transcript of the final audio). A human listen is still required, and the critic report must say what was not verified.
15. The production folder, `Production Queue.md` and UPLOAD.md match the current version.

### 9. Anti-patterns (each has burned us)
- Generic or insider openers ("Knicks center X made 29% of his playoff free throws").
- A dark stat card or article screenshot in the opening.
- Hopping between stats.
- A debate-question or hedged ending.
- Retelling an old winner by name (#29), or a bigger channel's story.
- B-roll that only "resembles" the topic.
- Accidental clip loops (22 of 27 folders had one until Oct 13).
- Time-stretched voice.
- Unfair voice comparisons (unmatched loudness).
- Polishing a weak premise: the old critic's craft score ran backwards against views (rho −0.63).
- Re-posting an identical file (#25: 177 views).

### 10. What would falsify this formula
- The next 6 formula Shorts have a median under 5K at 48 h, OR
- contract/role-player Shorts pass 18K while formula Shorts don't, OR
- every type of Short recovers at once. That would mean the drop came from distribution (the 215-day gap, 2 a day), not the premise.

Then revise sections 1-3.

### 11. Per-batch loop (one pass per batch, about one session)
1. Run `python3 Tools/channel_check.py @MetaSportsClips` and log it in the Outcome Log (date, source). Add vidIQ retention if credits are 10 or more.
2. Compare the last posts with the formula (did the Shorts that fit do better at the same age?).
3. Refresh candidates (Idea Banks, `Tools/fresh_moments.py`, news from the last 7 days). Score them in `Production Queue.md`. Lock the facts with dated sources before scripting.
4. Write 2-3 hooks; pick by clarity, curiosity, specificity, novelty and visual fit. Script 90-100 words; run `script_cadence.py`.
5. Inventory footage and map every line to a shot (EDL in PACKAGE.md). Build frame 1 first.
6. Voice with `voice_take.py` and check names and numbers. Anchor the shots, render with `assemble.py`, then make the pointer twin with `pointer.py`.
7. QA: `qa_short.py`, `voice_check.py`, `voice_quality.py`, `watch_short.py`; open the frame sheet. Then the Critic v2 agent. Fix and re-check.
8. Save notes.md, UPLOAD.md and PACKAGE.md. Update the queue status. Hub upload with `hub_pack.sh`.
9. After the owner posts, log the time. **Read the numbers at 24 h and 48 h** (views plateau after about 2 days), and at 7 days for the record. Compare only posts of similar age. Change a rule only with n≥3 or a large effect.


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

### 3. You end on a fact. They end on something to argue about. *(SUPERSEDED Oct 13: our data says end on the payoff that answers line 1; the argument goes in the pinned comment. See Strict Short Formula §3.)*

- CoachClank's underhand Short ends on Shaq saying he'd rather miss every free throw than look silly shooting underhanded.
- The top comment, with **48,000 likes**, just argues back that missing every free throw looks worse.

That argument in the comments is what spreads the Short.

### 4. You stopped

- **You:** 80 Shorts in 3.5 months, then 7 months dark.
- **CoachClank:** ~6 a week for 16 straight months.

---

## The recipe (what every MetaSports Short looks like now)

**Length:** stories 22–40 seconds (about 90–170 words); quick moments 15–25 seconds. CoachClank's 31–45s Shorts have the best median, and his 8 biggest 2026 Shorts ran 22–34s (Research Notes/Round 3 - Deeper Findings.md). Post between 6 and 11 AM ET. *(Unverified for this channel; see Strict Short Formula §11: log post times.)*

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
3. **End on the payoff that answers the opening (one number or the subject's own words).** Then stop. *(Updated Oct 13.)* No "subscribe," no summary.

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
