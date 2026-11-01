# What separates a hit from a miss on the same channel (Gemini watch study, Oct 27, 2026)

**Why:** the owner asked for evidence on our theories without burning credits. Gemini's free tier watched each channel's 10 best and 10 worst recent Shorts (newest 60, skipping the 5 newest). I read the coded results, not the videos.

**Sample:**
- **NBA:** Swishyyy (@swishyhoopz) and Hoopiverse (@HoopiverseYT): 40 Shorts.
- **Soccer:** Ahmed's Goal (@AhmedsGoal): 20 Shorts.
- 6 of the 60 reports came back without the coded fields, so those rows are blank.

**Data:**
- the two `... (2026-10-27).csv` files and their `summary.md` tables in this folder;
- one JSON per Short in `Research Notes/Watch Reports/`.

**Tier:** everything here is [S]. A model coded it (see the trust table in `Research Notes/Gemini Uses (Oct 27, 2026).md`), n is about 10 per group per channel, and it's correlation, not cause.

## 1. The editing basics are the same in hits and misses
| Feature (median or % yes) | NBA top 20 | NBA bottom 20 | Ahmed's top 10 | Ahmed's bottom 10 |
|---|---|---|---|---|
| Shots in the first 3 s | 2 | 2 | 2 | 2 |
| Shots in the first 5 s | 3 | 3 | 3 | 2 |
| Main subject on screen in second 1 | 100% | 100% | 77% | 100% |
| Full-screen cards | 0 | 0 | 4 | 4 |
| Words in the first sentence | 11 | 10.5 | 11 | 9 |
| Length (s) | 24 | 25 | 70 | 74 |

- **What this means:** on these channels, every Short already opens on the subject, holds the opening (2-3 shots in 5 s) and keeps line 1 short. That's the entry ticket. It doesn't decide which Short gets 1M and which gets 30K.
- **For us:** our Oct 26 editing rules are correct, but they're the baseline. More polish on the opening won't turn a 5K Short into a 500K one.

## 2. The subject is what separates them
**NBA, Swishyyy:**
- **Top:** spectacles anyone gets without knowing basketball:
  - "The Craziest Basketball War" 29M;
  - "The World's Biggest Basketball Hoop!" 21M;
  - "The Scariest Basketball Hoop!" 7.4M;
  - "Retired NBA Player vs 30 Hoopers" 1.1M;
  - "He Pretended To Be Klay Thompson" 1.0M.
- **Bottom:** NBA history and trivia explainers ("The Craziest Quarter In NBA History!", "The Injury That Saved The Spurs!", "The Most Impossible NBA Journey"). They are also longer: 39-67 s, against 14-28 s for the hits.

**NBA, Hoopiverse:**
- **Top:** kids, family, size and the biggest legends:
  - Steph Curry and his daughter;
  - Dwyane Wade and his son;
  - "the tallest 9-year-old ever?";
  - Kai vs Wemby height;
  - Kobe;
  - LeBron retiring;
  - "Every Country Has Their Own Version of NBA Players".
- **Bottom:** current players' personality bits that need you to be a fan (Anthony Edwards' offseason, Scottie Barnes "comedy show", LaMelo's "personal announcer", "weird questions").

**Soccer, Ahmed's Goal:**
- **Top:** the biggest names in a current controversy:
  - Ronaldo three times, including "What exactly happened between Cristiano Ronaldo and Portugal" at 1.9M;
  - "What PUNISHMENT is Man City going to face?";
  - "Why is UEFA investigating FC Barcelona?".
- **Bottom:** "Players who..." lists of lesser-known names ("working normal jobs", "sent to prison", "unlucky Ballon d'Or") and mid-table questions (Brighton, De Zerbi, Odegaard).

**The rule this points to (the "stranger test"):** would someone who doesn't follow the sport stop for this? Kids, family, giants, spectacle, the 3-4 biggest names, or a scandal about them all pass. Trivia, history details and role players' personalities don't pass.

## 3. Smaller signals (too thin to act on alone)
- **Loops don't help:** NBA hits loop back to the start less often than misses (38% vs 66%).
- **Countdowns:** 3 of the 37 rated hits use one, against 0 misses. That's too few to judge, so our weekly countdown test continues.
- **Ahmed's Goal cuts faster through the whole Short in its hits:** 38 shots vs 25.5, an average shot of 2.2 s vs 2.8 s. The opening is the same in both. Total shot counts are the least reliable thing Gemini gives us (off by up to 3), and the gap could come from length too.
- **Ahmed's Goal runs 60-140 s.** Our soccer rule stays under 59.5 s, because a copyright claim on a Short over 1 minute can block it. That trade-off hasn't changed.
- **Voice type and words per minute:** Gemini's labels were too unreliable to use.

## 4. What this means for our Shorts
1. **Choose the subject harder than we edit it.** Before scripting, apply the stranger test.
   - Our recent drafts that pass: "This Kid Felt Every Free Throw" (a kid) and "Haliburton Threw An Alley-Oop To Himself" (a spectacle).
   - Borderline: "Bones Hyland Got A Technical For A Fake Throw" (a role player, though a funny visible moment).
   - Soccer, passing: "Ronaldo Moved The Coca-Cola Bottles" (the biggest name plus a controversy).
2. **NBA: keep explainers short, or skip them.** History and stat explainers are Swishyyy's weakest Shorts, and the long ones especially.
3. **Soccer: go for the megastars and current controversies more often.** "Players who..." lists of lesser names are Ahmed's weakest format. Our "Goalkeepers who..." series did OK (30K and 15K), but watch it.
4. **Keep the editing rules as they are,** and don't add new micro-rules. The data says the basics are necessary, not sufficient.

## Caveats
- Older Shorts in the 60-Short window have had more time to collect views. Swishyyy's window spans about 4 months.
- Views measure reach, not "stayed to watch". We can't see other channels' retention.
- These are three channels and about 60 Shorts. Check this against our own 72-hour results before calling it a rule.
