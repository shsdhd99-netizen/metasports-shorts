# Competitor script breakdown: what the highest-scoring scripts do (Oct 15, 2026)

**Question:** what do CoachClank's and Ahmed's best scripts do that their average and worst ones don't? How does that compare with our winners (Curry Kobes, Giannis, #22, #19) and our flops?

**Rule followed:** we learn structure, not wording. No line, story or signature phrase from these scripts goes into ours (see section 7).

## 1. Sources and limits (read first)
| What | Source | Status |
|---|---|---|
| **Views, length, upload date** | yt-dlp public metadata pulled **Oct 4, 2026**: CoachClank 148 Shorts, Ahmed's 100, plus HoopFacts and HoopsLore (`scratchpad r5/*_full.json`, summarised below) | [V] public counts, 11 days old |
| **Transcripts** | **YouTube's own captions** (mostly auto-generated), returned by the Parallel Search `web_fetch` of `youtube.com/shorts/<id>` on Oct 15. Saved verbatim in `transcripts/` | [V] real captions, **not reconstructed**. Auto-captions can mishear a word. Three of Ahmed's came back partial; the gaps are marked "..." and **not filled in** |
| **Our own transcripts** | Curry Kobes and Giannis: YouTube auto-captions saved Oct 13. Our other Shorts: our `script.txt` files | [V] |
| **Visuals** | **Not watched for these Shorts.** YouTube still blocks downloads from this server, and we couldn't find their TikTok URLs. Visual notes below come from what the narration points at ("this guy", "you see") and from the 2 CoachClank TikToks watched on Oct 5 (Round 9: real game footage, no text cards in about 52 shots) | [H] for visuals |
| **Not available** | Captions for 5 CoachClank Shorts, including their #1 "6'8 vs 7'9" (30.9M, 15 s), which may have no narration at all; 1 of Ahmed's | Said plainly; not guessed |

**What these numbers can't tell us:**
- **Footage quality and the moment itself** drive much of a Short's reach. The scripts are only part of it.
- **Views reflect the platform's distribution**, not only the script.
- **Creator intent:** we don't know why a creator wrote anything a given way. We only describe what the script does.

## 2. Scoring method: relative to each creator's own baseline
- **Score = a Short's views ÷ the median views of the 20 uploads nearest to it in date, from the same creator** ("local median").
  - This controls for channel growth and video age: a March upload is compared with March neighbours, not with a September one.
  - The plain channel-median ratio is shown too.
- **Bands:**
  - top = the highest local scores
  - median band = ×0.85-1.15
  - bottom = the lowest 4
- **Baselines (Oct 4 pull):**

| Creator | Shorts | Median views | Uploads covered | Typical length |
|---|---|---|---|---|
| CoachClank | 148 | 449,058 | Mar 8 to Aug 27, 2026 | 12-35 s |
| Ahmed's Basketball | 100 | 85,791 | Aug 5 to Oct 2, 2026 | 65-80 s |
| HoopFacts | 100 | 42,162 | Apr 22 to Oct 1 | 15-62 s (not transcribed) |
| HoopsLore | 66 | 36,342 | Jan 21 to Sep 29 | interview clips, not narration (not used) |
| **MetaSports (us), new era** | 22 | about 3K | Sep 16 to Oct 14 | 21-33 s |

## 3. The scored sets (transcripts in `transcripts/`)
**CoachClank, top (9 with captions):**

| Short | Views | × local | × channel | Length | Line 1 |
|---|---|---|---|---|---|
| He Didn't Have To Do That | 21.5M | 55.7 | 48.0 | 22 s | "When a player is falling out of bounds, they usually throw it off an opponent to keep possession." |
| He Was Playing By Himself | 21.2M | 57.4 | 47.2 | 22 s | "This has to be the funniest way to end a game." |
| Is LeBron Selfish? | 5.7M | 32.9 | 12.6 | 35 s | "This is why people think LeBron is selfish." |
| He Accidentally Made a Full Court Shot | 10.7M | 29.1 | 23.9 | n/a | "This is what happens when you don't pay attention to the time." |
| How Do You Guard This | 7.7M | 30.8 | 17.2 | 18 s | "This shows how hard it is to block a basketball player." |
| This Is Actually Harder Than Making It | 9.1M | 27.4 | 20.2 | 12 s | "Is this more impressive than making a shot?" |
| **Why No One Shoots Underhand** | 10.9M | 25.6 | 24.3 | 25 s | "They were making fun of this player for shooting his free throws underhanded." |
| The Battle for the World's Highest Basketball Shot | 14.5M | 18.0 | 32.4 | 28 s | "At the time, this was the highest basketball shot ever." |
| The Unwritten Triple Double Rule | 6.5M | 16.7 | 14.4 | 25 s | "When a player is close to a triple double, their teammates usually try to help them get that last stat they need." |

**CoachClank, median band (5) and bottom (4):**

| Short | Views | × local | Line 1 | Ending |
|---|---|---|---|---|
| Brothers Playing 1v1 in the NBA | 419K | 1.09 | "This has to be the most wholesome moment in basketball." | the event |
| Who's Fault Was This? | 271K | 1.02 | "Who do you blame for this play?" | the consequence |
| Luka vs Reaves Trickshot Competition | 262K | 0.97 | "Luka and Austin Reaves had a half-court shooting contest during the game." | Luka's own words |
| Crazy Basketball Rule No One Knows About | 484K | 0.96 | "Do you know about this crazy rule that lets players hit the ball off the rim?" | a hypothetical ("imagine if…") |
| 200 IQ Inbounds Play | 373K | 0.95 | "When a team is in bounding the ball, the opponent usually puts the tallest guy to defend it…" | the event |
| Perfect Defense Didn't Matter | 91K | 0.05 | "This video shows you how good NBA offenses are." | a play-by-play with 7 names in 18 s |
| Caitlin Clark vs Men | 70K | 0.03 | "Have you ever wondered what would happen if a WNBA player played against a man?" | the event |
| Wemby Gets Revenge? | 37K | 0.01 | "Fans are wondering what Wemby whispered to his teammates…" | **a question** ("do you think Wemby actually told him to do this?") |
| She Tried Picking Up Shaq | 8K | 0.01 | "This UFC legend is about to try and lift Shaq…" (then 4 numbers: 300 lb, 7'1", 125 lb, 5'4") | the payoff is withheld ("this was the moment she surprised Shaq") |

> The bottom 4 could also be suppressed, claimed or age-limited uploads; public data can't show that. They are weak evidence.

**Ahmed's Basketball, top (5), median (1), bottom (2):**

| Short | Views | × local | Length | What the 65-70 s actually is |
|---|---|---|---|---|
| Teams that spent everything to keep their star but lost him anyway | 783K | 10.7 | 66 s | **One story** (Cavs, LeBron, Shaq, Jamison, 2010), not a list |
| Players who weren't that good in real life but unstoppable in the video game | 456K | 6.2 | 70 s | One story: Shannon Brown in 2K10 |
| Players who became insanely good after joining a new team | 460K | 5.4 | 68 s | One story: Dale Ellis (partial captions) |
| Basketball shoes that almost destroyed Nike | 390K | 5.4 | 65 s | One story: Curry and Under Armour (partial) |
| Players who were absolute cheat codes in NBA 2K | 557K | 5.4 | 66 s | One story: Josh Smith in 2K13 (partial) |
| Stars who gave up millions so teammates could get paid | 80K | 1.11 | 67 s | Durant's pay cut, with "Bird rights" and 9 numbers |
| Team owners who got fined | 21K | 0.17 | 68 s | Joe Lacob's tampering fine: a rules technicality about an owner |
| Saddest moments in NBA history | 11K | 0.14 | 68 s | Reggie Lewis, 1993 |

## 4. Per-example breakdowns (the strongest 6, plus the two most useful contrasts)
Format: premise, line 1, information order, open loop, escalation, payoff, wording, visuals [H], rhythm, length.

### 4.1 CoachClank, "He Didn't Have To Do That" (21.5M, ×55.7)
- **Premise:** a habit every fan has seen (throwing the ball off an opponent), then the one time it made no sense.
- **Line 1:** states the norm ("When a player is falling out of bounds, they usually…"). It's a statement, not a question.
- **Order:**
  1. the norm
  2. a famous example (LeBron, "full power")
  3. why it's funny
  4. "**But I think what's even funnier is when** Desmond Bane did it"
  5. the detail that makes it absurd (OG was already out of bounds; Bane wasn't falling)
  6. the consequence
- **Open loop:** "what's even funnier is when…" (at 11 s, the midpoint).
- **Escalation:** from normal to absurd, in one step.
- **Payoff:** a consequence the viewer sees: "he receives a technical foul for it." Then it stops.
- **Wording:** "You see," and "However," as connectors; the narrator gives an opinion ("I think").
- **Visuals [H]:** each sentence points at a clip: LeBron's throw, then Bane's throw, then the call.
- **Rhythm:** about 276 wpm from caption timing; 97 words; 0 numbers.
- **Length:** 22 s.

### 4.2 CoachClank, "He Was Playing By Himself" (21.2M, ×57.4)
- **Premise:** a garbage-time moment nobody else was watching.
- **Line 1:** a superlative claim about the clip on screen: "This has to be the funniest way to end a game."
- **Order:**
  1. the claim
  2. "You see," the situation (Moody, the clock, the game already lost)
  3. the absurd detail (Westbrook and Gordon dapping up while he shoots)
  4. escalation (he rebounds his own miss "like he's playing by himself"; "Why not?", another three)
  5. the payoff
- **Payoff:** a star's reaction: "Jokic is the only one left still paying attention to the game, clapping for Moody."
- **Rhythm:** 106 words, 0 numbers except "nine" (the lead).
- **Length:** 22 s.

### 4.3 CoachClank, "Is LeBron Selfish?" (5.7M, ×32.9)
- **Premise:** an accusation about the biggest name, with two pieces of evidence.
- **Line 1:** "This is why people think LeBron is selfish." It names the star and the charge in one sentence.
- **Order:**
  1. claim
  2. evidence 1 (the 2020 Finals; Rondo slams the ball)
  3. **a narrator aside**: "I get he's preserving his field goal percentage, but he can at least pass it."
  4. "**However, it didn't stop there**"
  5. evidence 2 (the next season)
  6. the payoff
- **Payoff:** a teammate's reaction: he "isn't celebrating… because he knew what LeBron was doing."
- **Rhythm:** 152 words, 1 number.
- **Length:** 35 s, the longest of the top 9. Length didn't stop it.

### 4.4 CoachClank, "Why No One Shoots Underhand" (10.9M, ×25.6) vs our #29 on the same topic (1.4K, 56% stayed)
| | CoachClank | Our #29 |
|---|---|---|
| **Line 1** | "They were making fun of this player for shooting his free throws underhanded." (a scene with conflict; no name needed) | "Knicks center Mitchell Robinson made twenty-nine percent of his playoff free throws." (a player casual fans don't know, plus a stat) |
| **The question** | asked out loud at 6 s: "why does no one use it in today's NBA?" | never asked; the viewer has to infer it |
| **Names** | 2 (Rick Barry, Shaq) | 4 (Robinson, Barry, Wilt, Shaq) |
| **Numbers** | 1 (91%) | 8 (29%, 90%, fourth, 100, 28 of 32, 53%, fifteen…) |
| **Payoff** | Shaq's reason, in plain words: "he'd rather miss every free throw than look stupid on the court" | Shaq's quote, but after 8 numbers and 3 detours |
| **Length** | 25 s, about 100 words | 22.8 s, 95 words |

**What it shows:** same topic, same Shaq payoff. CoachClank's version:
- opens on a scene, not a stat
- says the question out loud
- has two names and one number
- ends on the human reason

This is one pair, not proof, but it lines up with our Studio data: number-led and niche-player openings had the lowest stay rates.

### 4.5 CoachClank, "The Battle for the World's Highest Basketball Shot" (14.5M, ×18.0)
- **Premise:** a rivalry over a record.
- **Line 1:** an absolute claim about the clip: "At the time, this was the highest basketball shot ever."
- **Escalation:** **the numbers are the ladder**: 533 ft, then 660 ft ("everyone thought would be the final record"), then 856 ft. Each number is a new rung, one per beat.
- **Payoff:** the final record, after "it actually took them 3 days."
- **Lesson:** numbers work when each one tops the last. They don't work stacked inside one sentence.

### 4.6 Ahmed's, "Teams that spent everything to keep their star but lost him anyway" (783K, ×10.7)
- **Premise:** a famous gamble that failed (Cleveland, LeBron, 2010).
- **Line 1:** the title, read aloud, as a promise. Then straight into one story.
- **Open loops,** one about every 10-15 s:
  - "There was just one problem…" (11 s)
  - "But the version of Shaq they got wasn't the one…" (21 s)
  - "But everything they built for this exact moment was about to fall apart…" (42 s)
  - "**And here's the part that changed the NBA forever**…" (60 s)
- **Payoff:** "LeBron left for Miami, and the franchise that gave up everything to keep him fell apart for years." It answers the title.
- **Rhythm:** 285 words in 66 s (about 258 wpm), 7 numbers spread over 66 s (about one every 9 s).

### 4.7 Ahmed's top 5 vs Ahmed's bottom 2
- **Top 5:** every one is a single story about a famous name or brand (LeBron, Kobe's Lakers, Curry and Nike, NBA 2K) with an irony payoff:
  - "finished dead last in that dunk contest… an unstoppable cheat code"
  - "took a chance on a guard nobody else believed in"
- **Bottom 2:**
  - an owner's tampering fine: a rules technicality, the same lane our audit found flops for us
  - a 1993 tragedy about a player most of today's audience doesn't know
- **The median one** carried a jargon term ("Bird rights") and 9 contract numbers.

### 4.8 Our winners, read the same way
| | Curry Kobes (30.8K) | Giannis game ball (28.3K) | #22 Number six (31.8K, 82% stayed) |
|---|---|---|---|
| **Line 1** | "Stephen Curry just pulled one of the wildest sneaker moves the NBA has ever seen." (star + superlative) | "Giannis just saved a rookie's first NBA memory." (star + a kind act) | "Only two NBA players are still allowed to wear number six." (absolute claim) |
| **Turn** | "But the craziest part…" | "Nobody knew why… but Giannis noticed." | "But players already wearing it kept it." |
| **Payoff** | "Curry still drops 30 like nothing happened." (then a CTA, which should go) | "The look on Adu's face said everything… a moment this rookie will never forget." (a reaction) | "…it's the twenty-four-year-old whose dad picked it without thinking." (the human detail) |

**Same skeleton as CoachClank's top:**
1. a claim about a famous subject
2. the concrete detail
3. a turn
4. a payoff that is a person's reaction, words, or the human reason (3 of the 4; Curry's ends on an event, then a CTA)

## 5. Patterns across the sets (counts; n is small)
| Pattern | CoachClank top 9 | CoachClank median 5 | CoachClank bottom 4 | Our winners | Tier |
|---|---|---|---|---|---|
| **Line 1 is a statement (not a question)** | 8 of 9 | 3 of 5 | 3 of 4 | 4 of 4 | [S] |
| **Line 1 makes a claim about the clip or subject** ("This has to be the funniest…", "This is why people think LeBron is selfish", "At the time, this was the highest…"; ours: "Only two NBA players…") | 6 of 9 | 1 of 5 | 2 of 4 | 4 of 4 | [S] |
| **The last beat is a person's reaction or own words** (Jokic clapping, a teammate not celebrating, the coach yelling, Shaq's reason, LeBron's joke; ours: the rookie's face, the dad's pick, Flagg's "I'm 6-10") | 5 of 9 (plus 1 ending on a consequence: the technical foul) | 1 of 5 | 0 of 4 | 3 of 4 | [S] |
| **Ends on a question or a hypothetical** | 0 of 9 | 1 of 5 | 1 of 4 | 0 of 4 | [S] |
| **At most 2 numbers, or numbers used as a ladder** | 9 of 9 | 5 of 5 | 3 of 4 (the miss: 4 numbers in one breath) | 3 of 4 (#22 had 6 and still won) | [S] |
| **A turn word ("But" / "However") after the setup** | 7 of 9 | 5 of 5 | 2 of 4 | 3 of 4 (#19 turns with "Not so fast") | [S]; common at every level, so it's table stakes, not the edge |
| **A narrator opinion aside** ("I get he's preserving…", "So, to me…", "I think") | 4 of 9 | 0 of 5 | 0 of 4 | 1 of 4 | [H] promising |
| **A famous name in the first 3 s or in the payoff** | 6 of 9 | 4 of 5 | 4 of 4 | 4 of 4 | not a separator on its own |

**What separates top from median for CoachClank** [S, n=9 vs 5]:
- **Line 1 claims something about the clip** (6 of 9 vs 1 of 5).
- **The last beat is a person's reaction or words** (5 of 9 vs 1 of 5).
- **The middle escalates** (normal, then absurd, then the punchline).
- Famous names and a turn word appear at every level, so they're necessary, not sufficient.

**What separates top from bottom** [S, n=9 vs 4]:
- The bottom 4 had: a question opener, a question ending, a play-by-play of 7 names, a number stack, or a withheld payoff.
- This matches our own flops (audit §12-13): number-led, niche, technical.

**Pace:**
- CoachClank's top scripts run about 234-279 wpm (caption timing); ours run 220-236.
- Their top and bottom overlap in pace, so pace doesn't separate them. **We keep our pace** (it's tied to our voice).

**Length:**
- CoachClank's top: 12-35 s.
- Ahmed's: 65-70 s, but one story told slowly, not a list.
- Length is format-specific; it doesn't separate their top from their median.

## 6. What we take from this (principles only; added to the critic's rewrite checklist and the Playbook)
1. **Make line 1 a claim about the moment on screen** ("This is the funniest…", "Only…", "[Star] just…"), and make frame 1 that exact moment. If the sentence could run over any clip, it's too generic.
2. **Say the viewer's question out loud by about 6-8 s**, after the scene, never as line 1. (CoachClank's underhand Short: "why does no one use it?")
3. **Escalate**, don't list: normal, then strange, then the punchline. Numbers only as a ladder (each one tops the last) or one per Short.
4. **End on a person:** their reaction, their words, or the human reason. Then stop. No question, no "imagine if", no CTA.
5. **One opinion aside is allowed** ("I get it, but…") [H]. It gives the narrator a point of view; test it before it becomes a rule.
6. **Two names is plenty for 25 s.** Every extra name is a person the viewer has to place.

## 7. What we don't take
- **No wording:** not "But I think what's even funnier is when…", not "You see,", not "This has to be the funniest…" word for word, not Ahmed's "and here's the part that changed the NBA forever". These are other creators' voices.
- **No story choices copied:** we don't remake their topics. #29's underhand topic is ours and predates this study; if we redo it, it gets our own research, quotes and footage.
- **Not their pace** (CoachClank's narrator is faster) **or Ahmed's 65-70 s format.**
- **No claims about why they made choices.** We describe what the scripts do, not what the creators meant.

## 8. What's still unknown
- **The visuals of these exact Shorts.** Watching the top 5 would test the "line 1 points at the clip" reading [H]. It needs the owner to share links that play, or a vidIQ watch (5 credits left, resets Nov 5).
- **Whether these patterns survive at our size.** CoachClank has 145K subscribers and we have 520. The skeleton matches our own winners, which is the reason to trust it, but the pattern is correlation.
- **The captions are auto-generated.** A misheard word won't change a structure finding, but don't quote these lines as exact.

## 9. Addendum, Oct 17, 2026: two more transcripts, our newest best and worst, concrete rewrites, method update
**New real captions** (verbatim in `transcripts/coachclank_top.txt`, appended):

| Short | Views | × local | Line 1 | Turn | Payoff |
|---|---|---|---|---|---|
| Missing a Free Throw on Purpose? | 10.5M | 13.0 | "Why did this player miss this free throw on purpose?" (question about the clip on screen) | "But then, Boban realized the crowd was cheering for him to miss" (8-9 s) | the human reason: "a man of the people… making everyone's night" |
| Why Kobe Didn't Like His Teammates | 1.0M | 10.0 | "Kobe Bryant was known for not respecting his teammates." (an accusation about a legend) | "Kobe actually revealed the real reason" (5 s) | Kobe's own words, last: "Why should I trust them… when he knows they're not working to get better?" |

**Four more captions were tried and failed** (no transcript returned or the video is unavailable). They are listed in the file, not guessed.

**What the two add:**
- **The Kobe Short is a near-copy of the #42 skeleton**: an accusation about a legend, the question, then his defence in his own words. A 1.0M Short (×10 local) and our record-stay Short share the structure. Two cases, not proof.
- **Boban** is the "visible oddity plus hidden reason" pattern (Curry Kobes, Giannis game ball): the clip shows something strange; the script supplies the why; the ending is a kindness. Zero numbers in 22 s.

### Our newest best vs worst, read the same way
| | #42 Most missed shots (84.3% stayed, 6.3K at 1.5 days) | #46 LeBron fourth team (49.8% stayed at 0.5 day) | #20 Bad Boys (47.8%, 1.6K) |
|---|---|---|---|
| Line 1 | an accusation about a legend ("has missed more shots than anyone") | a list fact ("Only four players ever…") | a naked number ("Ninety-two point nine.") |
| Frame 1 | the claim happening (an airball) | LeBron's face | a scuffle |
| Turn | "So is he a worse shooter? No." | "So why, at forty-one?" | none (a stats chain) |
| Payoff | one number that flips the insult (31,502 attempts) | his quote about a future that can't be answered | "four tenths of a point apart" |

### Concrete rewrites (structure only; nothing copied)
**#20 Bad Boys:** opens on a number with no subject, then 8 numbers.
- **Before:** "Ninety-two point nine. That is what the Bad Boy Pistons allowed per game in the 1989 playoffs."
- **After:** "The Bad Boy Pistons are called the dirtiest defense ever. And last season's Knicks were just as good. Not as dirty: as good. Detroit allowed about ninety-three points a game. The Knicks allowed a hundred and one. So the Pistons were better? No. They just played slower. Count it per hundred trips down the floor, and the best defense of 1989 and the best of 2026 are four tenths of a point apart."
- It now has the accusation hook, the question then "No.", and two numbers before the payoff.

**#13 Kawhi picks:** a list of penalties in line 1 (50.0% stayed).
- **Before:** "The NBA took five first-round picks from the Clippers, fined them $30 million, and suspended their owner for a year…"
- **After:** "The Clippers gave up ten first-round picks for Kawhi Leonard. Toronto just got him for two." Then the turn: "So who got the better deal?"
- One number pair in line 1, and a famous name.

**#46 fourth team** (script not in the cloud copy; built on the PC): open on what can be seen, not on the list.
- **After:** "LeBron James is trying to win a title with a fourth team. Nobody has ever done that as the best player." This needs fact-checking before use (Horry, Salley and Green won with three or more teams as role players).
- Then end on what he *has* done (four titles with three teams), not on a question about the future.

### Script method update (applies from Oct 17; carried into the Playbook)
**Retain (confirmed again):**
- line 1 = one absolute claim about a famous name or the clip on screen
- the viewer's question out loud, then a short answer ("No.")
- the payoff in the subject's own words, or one number that flips the claim
- 0-2 numbers outside a ladder

**Revise:**
- **The accusation-defence skeleton** (#42, Kobe teammates) is now the first template to try for any stat story: *[legend] has [bad-sounding record]. [the number]. [why that's strange]. So is he [bad]? No. [the flip].*
- **Frame 1 must show the claim** (the miss, the bounce, the lookalike's face), not the star's face.

**Retire:**
- **openers that are lists** ("Only four players ever…" on a list rather than an object), penalties or a naked number
- **future-question premises** ("Can he…?") as the whole Short
- **a third Short on the same star in one week**
