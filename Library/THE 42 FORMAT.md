# THE #42 FORMAT: "Bad record, good reason" (Oct 19, 2026). The only format we produce.

**Why this format:** #42 "Who Has Missed The Most Shots In NBA History?" (Ro0oa2VLlqA, posted Oct 16):
- **84.3% stayed to watch**, the channel record (Studio export Oct 17)
- **25,000 views at about 3.5 days** (public count Oct 19)
- 7 subscribers in its first 1.5 days

**The control group:** in the same week, the same voice, the same editor (the PC session) and the **same star** made:
- #46: 49.8% stayed, 2.1K
- #36: 4.3K
- #10: 1.9K

So the star, the voice and the edit tools were not what made #42. **The structure was.** Owner, Oct 19: "focus on what we KNOW works, and stop making new formats."

The two other wins that share the core (a surprising, slightly negative claim about a famous name, resolved in their favour):
- #44 "Flagg still carries the bags" (10K, 69.7% stayed)
- #22 "Only two can wear six" (31.8K, 82.4%)

## 1. The skeleton, with #42's measured timing (`_v3/words.json`)
| Beat | #42 line (spoken) | #42 time | Job | Rule |
|---|---|---|---|---|
| **1. Accusation** | "LeBron James has missed more shots than anyone in NBA history." | 0.0-3.3 s | a bad-sounding superlative about a famous star | **[Famous star] has [bad thing] more than anyone in NBA history.** One sentence. Ends by about 3.5 s. A name every casual fan knows |
| **2. The count** | "15,541." | 3.3-5.3 s | makes it concrete | **The number alone**, as its own sentence. The caption shows digits |
| **3. Paradox** | "And he's the all-time leading scorer." | 5.5-7.2 s | the "wait, what?" moment | **And he's [the opposite, great thing].** Lands by about 7.5 s |
| **4. Old record** | "The old record was Kobe's: 14,481 misses." | 7.3-10.6 s | a second famous name and the stakes | the previous holder, with their number |
| **5. Human tie-in** | "LeBron passed it in October 2024, the same night he first played with his son." | 10.7-14.3 s | warmth, a moment fans remember | **one** human detail tied to the record moment (optional; keep it if true and short) |
| **6. Turn** | "So is he a worse shooter? No." | 14.3-16.0 s | voices the viewer's doubt, then defends the star | **So is he [bad]? No.** with the "No." as its own beat (about 0.4 s) |
| **7. Proof** | "LeBron makes fifty-one percent. Kobe made forty-five." | 16.0-18.5 s | evidence, one number per player | two short sentences, each with words over footage of that player |
| **8. Flip** | "LeBron just shot more than anyone, ever: 31,502 times." | 18.5-23.2 s | the reason: volume, longevity, usage | **[Star] just [did the good thing] more than anyone, ever: [number].** End on the number; nothing after it |

**Counts:**
- about **75 spoken words, about 470 characters, 22-25 s**
- **about 195 spoken wpm** (Alex, multilingual v2, speed 1.2)
- 12 sentences, mean 6 words
- **6 numbers**, each in its own sentence and each shown on screen

## 2. The edit (`_v3/shots.json`, `sources.csv`, `sfx.json`, `music.json`)
| What | #42 | Rule |
|---|---|---|
| Frame 1 | LeBron's three **falls short** (an airball): the accusation happening | **frame 1 shows the bad thing**, not the star's face |
| First 5 s | one play, shown twice: 0-2.7 s, then 2.7-5.2 s with a stronger 10% push-in | **hold the proof**: one readable play for the first 5 s; the second visit changes scale |
| Shots | 12 in 23.6 s, **median 2.0 s**, first cut at 2.7 s | 11-13 shots, about 2 s each. Calmer than our other builds (1.2-1.9 s), and it read better |
| Who's on screen | every shot shows the player the line names, verified by eye and logged | the same, no exceptions |
| Numbers | words over footage (LEBRON 50.7% / KOBE 44.7% / 31,502 / KAREEM 28,307), **zero cards** | numbers sit on footage of the player, above the caption band |
| Push-ins | 5-10% on the airball, the record moment, the son shot and the faces; none on the soft Kobe clips | slow push-ins on clean clips only; never on a blow-up |
| Effects | 4, each on a visible event: a whoosh into the proof numbers, a pop per number, a riser into the flip. None on the airball (silent by design) | 2-4 effects, never the same twice, only where something appears |
| Music | the v3 render had a Yuke instrumental, dipped on "No.". **Which file the owner uploaded is not recorded** | instrumental only, dipped under the turn; log music yes/no in UPLOAD.md for every post |
| Captions | house style (metasports), 28 cards | unchanged |
| Ending | on the flip number over LeBron's record possession; loops to the airball | end on the flip; no CTA, no question |

## 3. What we KNOW vs what we don't
**Known (measured):**
- this skeleton scored the channel's best stayed % and its best post-#19 reach
- the same week's LeBron Shorts **without** it did 2-4x worse

**Not known:**
- whether music helped (not logged)
- whether a different voice would do better (only Alex has been used in this format)
- whether it repeats: **n=1**

The next 3 posts in this format are the test. **Success = 2 of 3 reach 74%+ stayed** (the level where every past Short got 4K+).

## 4. Hard rules for scripts in this format (the critic and lint enforce these)
1. Line 1 matches **"[famous star] has [bad-sounding superlative] … than anyone / most in NBA history"**, true by an official count (Basketball-Reference career or season totals, regular season unless stated).
2. The count follows as its own sentence.
3. A paradox line ("And he's…") by about 7.5 s.
4. A "So is he [bad]? No." turn.
5. The flip is a number that explains the record (volume, longevity, usage). It is **never** a hedge or a question.
6. 65-85 spoken words.
7. **Footage gate:** a clip of the star doing the bad thing (a miss, a turnover, a foul) must exist before voicing.
8. **Star spacing:** a different star from the previous post in this format when possible. The format is the constant, not the name.

## 5. Story bank for this format (each must pass a fact check before scripting)
| # | Accusation | Flip | Status |
|---|---|---|---|
| #48 | James Harden has missed more threes than anyone (5,933) | Only Curry has made more; Curry took 750 more and missed fewer | **script verified Oct 17**; needs footage |
| B1 | LeBron has more turnovers than anyone | he has had the ball more than anyone (assists, minutes) | verify (B-Ref career TOV/AST) |
| B2 | Kareem committed more fouls than anyone | he played more minutes than anyone for 38 years | verify (B-Ref PF, MP) |
| B3 | Harden's 2016-17: the most turnovers in one season | he led the league in assists that year | verify; a second Harden, so space it |
| B4 | Kobe went 6-for-24 in Game 7 of the 2010 Finals | Finals MVP; 15 rebounds | verify; single-game variant |
| B5 | Michael Jordan: "I've missed more than 9,000 shots" | he actually missed 12,345, and that's why he made 12,192 | verify (B-Ref FGA/FG); a quote variant |
