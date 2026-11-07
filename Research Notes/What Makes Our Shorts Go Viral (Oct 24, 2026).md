# What makes our Shorts go viral: the evidence, and what we change (Oct 24, 2026)

The single playbook that replaces the scattered rules. It combines five studies made on Oct 24:
- `Audit of Our Rules (Oct 24, 2026).md` (our own 38 NBA + 3 soccer Shorts, Studio data)
- `Niche Study - NBA Shorts (Oct 24, 2026).md` (16 channels, 2,772 Shorts, Ahmed's Basketball 1,175)
- `Niche Study - Soccer Story Shorts (Oct 24, 2026).md` (Ahmed's Goal 1,365, 30+ channels, 33 runtimes)
- `Shorts Mechanics and Policy (Oct 24, 2026).md` (official YouTube pages, interviews, studies)
- `Discoveries (Oct 24, 2026).md` (tools, sources, platform changes)

**Tiers:** [V] measured or official · [S] several credible sources · [H] a guess. **n** = Shorts behind the claim.
**The bar for a rule:** 3+ of our own Shorts pointing the same way, or [V] outside evidence. Anything else is a test.

## 1. How a Short wins (the mechanism)
1. **YouTube shows every Short to a small test audience first. The stay-or-swipe decision in the first 1-2 seconds decides whether it goes wider** [V official + ours]. Our data: every 10K+ Short held 74%+ "stayed to watch" (0 of 25 below did; Spearman 0.69 with views, n=38).
2. **74%+ is the gate, not a guarantee** [V]. #40 held 81% and got 1.6K; the same concept swings 5x between airings on Ahmed's Basketball (70% of the spread is inside the same concept, 133 concepts). Luck is large, so we judge rules on batches of Shorts and re-try strong concepts.
3. **Views arrive in about 48 hours** [V]. 68-100% of a Short's views came in its first 2 days. Analytics run 48-72 h behind, so a Short is scored at 72 h+ (live views from the Data API before that).
4. **What reaches the 1M+ tier differs by niche** [V/S]:
   - NBA: one visible, strange moment the viewer can see (CoachClank: median 419K, 34% of Shorts at 1M+; line 1 points at the clip). Our stat paradoxes top out at 20-30K.
   - Soccer: a story where a player or club turns on its own side (Ahmed's Goal: 610K vs 313K median, 1.63x time-adjusted, n=87), or a numbered serial about one global star (FOOTY FACTS "Zlatan Part 1-9": median 1.4M vs 162K for one-offs).

## 2. What we change (evidence clear)
### Both channels
1. **Rotate 3-4 formats; never ride one template** [V]. Every channel that repeated one winner watched it collapse (Korzemba 23M to 8-49K; REBOUND 42M to 184K; ours: #42 86.9%, #48 83.3%, #64 72.6%, #52 59.1% stayed, in posting order). YouTube's July 2026 policy targets interchangeable template videos. **A format gets at most 1 post in 3, and is retired after 3 posts in a row below the channel median.** Rewrite the fixed lines every time.
2. **Frame 1 shows the claim, sharp and lit** [V]: the moment itself, or the star, whichever proves line 1. (#42 opened on the airball, not a face; S01 on the hand going into the sock.) QA already fails a dark frame 1.
3. **Every line adds something the footage doesn't show** [V policy]: a fact, a number, a reason. Narration that only describes the clip is "not original" under the Oct 1, 2026 originality update.
4. **A strong concept that flops gets a new opening, not the bin** [S]: re-cut the first 3 s and frame 1 as a new edit, once. Never delete and re-upload the same file (YouTube can treat that as spam; our identical #25 re-upload got 197 views).
5. **One table decides**: `Research Notes/Shorts Dataset.csv` (`Tools/shorts_dataset.py`). Every post logs lane, star, freshness, frame 1, music, captions and length. A rule changes only with n and medians from it.
6. **Keep the AI voice** [V/S]: the biggest narrated channels use AI voices, YouTube's policy doesn't penalise them, and labelling isn't required for narration. Never clone a real person's voice without consent (the backup "pham" clone stays unused until the owner confirms whose voice it copies).

### NBA (MetaSports)
1. **Lanes, in rotation:**
   - **One clip, one oddity** (new lead lane, 20-35 s): frame 1 is the moment; line 1 points at it ("When X happens, players usually Y. He didn't."). Gate: it must look strange with the sound off.
   - **Household-name star + one-line paradox** (THE #42 FORMAT and its cousins: #22 "Six" 31.8K, the Wemby vote 27K, Flagg's height 21K).
   - **Same-day news with a number gap**, household names only (#58 23K). A day late, drop it (#63 58%).
   - **Evergreen nostalgia/history** about superstars (Rebound Rewind: evergreen 245K vs news 133.5K median).
2. **Rules topics: only visible rule-breaking** [V, n=79 across 13 channels: 1.42x the channel norm]: caught cheating, banned, illegal, a player breaking a rule on camera. **No paperwork rules** (bets, schedules, voting procedure, stat credit: our weakest lane, 2.0K median, n=6), unless a superstar and a hard paradox carry it (#22, the Wemby vote).
3. **Length follows the story; test 35-45 s** [S]: CoachClank's best band is 31-45 s in 2025 and 2026; we have never posted over 33 s, and 20-33 s showed no effect in our data. Five paired tests. Hard cap 58 s (Content ID).

### Soccer (MetaSports FC)
1. **Lanes, in rotation:** the secret object (S01), **"versus their own"** (refused, betrayed, sued, rejected by their own club/country/sponsor), a **numbered serial about one global star** (Messi/Ronaldo/Zlatan "Part 1, 2, 3..."), and a **topical question** answered with a story ("Why did X just...?", 59% of Ahmed's Aug-Oct titles, median 238K vs 245K evergreen, his biggest recent hits).
2. **Titles: shape is neutral** [V]. My Oct 24 "plural beats singular, 318K vs 217K" claim was an era effect (the singular titles are from 2024, when the channel was tiny) and is withdrawn. Post the spoken line 1. **Say the stakes, specifically**; strong verbs lift (1.35x, n=107).
3. **Keep the title as line 1** (still 33 of 33 Ahmed scripts). **"Back in [year]" is optional**: Ahmed now uses it in 1 of 30.
4. **Under 60 s on YouTube while the footage is broadcast archive** [V official]: QA hard gate 59.9 s, warning over 59.5 s. If the owner cross-posts to TikTok/Instagram (TikTok pays only over 1 minute), make a 65-75 s cut there.
5. **Patience:** Ahmed's new style sat at 17K a Short for ~106 Shorts before jumping to 340K. Our soccer rules from S01-S03 stay hypotheses until 20-30 Shorts.

## 3. Tests (not rules yet): run, log in the dataset, decide at the stated n
| Test | Design | Decide at |
|---|---|---|
| NBA length 35-45 s vs 22-28 s | same lane, alternate | 5 pairs |
| Music bed vs none (both channels) | alternate; log which file was posted | 6 each |
| Caption style: house ALL CAPS vs sentence case | alternate | 6 each |
| Eleven v4 vs Multilingual v2 (Alex) | 2 scripts both ways, owner's blind ear test, voice_quality.py | owner |
| FC posting time 12 PM vs 6 PM ET | alternate days | 2 weeks |
| "Related video" link on every Short | owner adds it in the upload | 2 weeks |

## 4. Money reality [V official]
From Feb 1, 2027, Shorts pay nothing below **10M qualified Shorts views per 90 days** (about 111K a day; new applicants need 20M). The NBA channel is at about 17K a day. 20-30K Shorts can't close that gap; only 1M+ hits can. **Track the share of Shorts at 100K+**, and spend new effort on the lanes with 1M+ ceilings (visible oddities in NBA; own-side conflict and star serials in soccer). Before applying, set the off-niche AI/Sora meme Shorts to private (owner).

## 5. What stays the same
News only while fresh. End on the payoff, never a question (the debate goes in the pinned comment). Every fact sourced, exact words in notes.md. No teaser or promo. No dead air. Full QA before any draft.
