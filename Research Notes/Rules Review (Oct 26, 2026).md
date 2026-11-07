# Rules Review (Oct 26, 2026)

**Owner's ask:** "do a review of our playbook/rules. can everything stand? or are you feeding yourself bad info holding you back. everything is up for debate". Focus: YouTube Shorts.

**What this is:** every rule that shapes a Short, from every rulebook, checked against the evidence. Nothing was edited. This file proposes the edits.

## Bottom line
- **Yes, we have been feeding ourselves bad info.** Most of the rules that hurt us came from competitor averages, vendor blogs or one Short. They became FAIL gates before our own data existed.
- **Our own data is now big enough to overrule them.** 40 new-era NBA Shorts have Studio "stayed to watch". They say: the topic and the first second decide. Calm openings and no cards hold better. Pace, length, word count and how many numbers we say show no link.
- **The files have not caught up.** The Oct 26 fixes reached `qa_short.py` and the top box of `cloud-short`. The old rules still sit lower in the same SKILL, in `CLOUD STATE` (read first by every agent), in `nba-short`, `story-short`, the Playbook and the soccer Playbook.
- **THE #42 FORMAT failed its own test.** The rule was "proven if 2 of 3 reach 74%+". Result: 1 of 3. Playbook RULE 1 still says "lead with it".
- **The soccer rules rest on 3 Shorts.** One of the two "flops" (S03) has since reached 14K.

## How to read the tags
- **Tier:** [V] measured · [S] small sample (n<5, or one arm small) · [H] hypothesis or guess.
- **Origin:** OURS (our measured results) · COMP (competitor data) · GEN (generic advice: vendors, lab studies, "best practice") · OWNER (the owner's call).
- **Flags:** **[BAD INFO?]** = built on generic advice or n<5 · **[SLOWS]** = costs time or credits with no evidence.

**File short names** (all paths from the repo root):
| Short | File |
|---|---|
| PB | `MetaSports - Playbook.md` |
| CS | `CLOUD STATE - read this first.md` |
| SH | `00 START HERE.md` |
| cloud | `.claude/skills/cloud-short/SKILL.md` |
| daily | `.claude/skills/daily-run/SKILL.md` |
| story | `.claude/skills/story-short/SKILL.md` (+ `FORMAT.md`, `QA.md`, `SOURCING.md` in that folder) |
| nba | `.claude/skills/nba-short/SKILL.md` |
| titles | `.claude/skills/titles/SKILL.md` |
| QA | `Tools/qa_short.py` |
| TP | `Tools/data/title_patterns.md` |
| F42 | `Library/THE 42 FORMAT.md` |
| ESS | `Library/Editing and Sound Standards.md` |
| SL | `Library/Sound Library.md` |
| BRG | `Library/B-roll Sourcing Guide.md` |
| FCPB / FCSH / FCOL | `Soccer Channel/Playbook.md` / `START HERE.md` / `Outcome Log.md` |
| US | `UPLOAD SCHEDULE.md` |
| WHY | `Research Notes/Why NBA Views Dropped (Oct 26, 2026).md` |
| SW | `Research Notes/Channel Study - Swishyyy (Oct 26, 2026).md` |
| NNBA / NFC | `Research Notes/Niche Study - NBA Shorts (Oct 24, 2026).md` / `... Soccer Story Shorts (Oct 24, 2026).md` |
| AUD24 / RA14 | `Research Notes/Audit of Our Rules (Oct 24, 2026).md` / `Rules Audit (Oct 14, 2026).md` |
| R6 / R7 | `Research Notes/Round 6 - What Makes Shorts Go Viral (Oct 4, 2026).md` / `Round 7 - Viewer Retention Deep Dive (Oct 4, 2026).md` |
| LL / OL | `Research Notes/Lessons Learned (running log).md` / `Outcome Log.md` |
| MP | `Research Notes/Shorts Mechanics and Policy (Oct 24, 2026).md` |
| SER / S23 / WMV | `Research Notes/Studio Export Read (Oct 24, 2026).md` / `Why S02 and S03 Underperformed (Oct 24, 2026).md` / `What Makes Our Shorts Go Viral (Oct 24, 2026).md` |
| DS | `Research Notes/Shorts Dataset.csv` |

---

## 1. The 10 rules that matter most (keep)

**1. "Stayed to watch" is the gate. Aim for 74%+. Judge at 48-72 h.**
- All 6 new-era Shorts at 10K+ held 74%+. 74%+ got a median of 8.6K views; below got 2.9K (WHY §1). Stayed vs views: Spearman 0.70, n=37 (WHY §1); 0.69, n=38 (AUD24 §1). [V] OURS
- Only 13 of 40 new-era NBA Shorts reached 74%; median 69% (WHY §1; re-counted from DS today: 13 of 40, median 69.0%). [V]
- Necessary, not enough: #40 held 81% and got 1.6K (AUD24 §1). [V]
- Fix: PB L79 still says "Target: 70%+".

**2. A household-name star (or an iconic object) plus one idea a casual fan gets in second 1.**
- All 6 of our 20K+ new-era Shorts had it (AUD24 §1). [V n=6] OURS
- Technicalities, niche players and retells were the bottom 6 (PB L67-68). [S n=22] OURS
- Paperwork rules (bets, votes, stat credit) are our weakest lane: 63.7% stayed, 2.0K (AUD24 §1). [V n=6] OURS. Visible rule-breaking is fine: 1.42x the channel norm across 13 channels (NNBA finding 4). [V n=79] COMP

**3. Rotate 3-4 lanes. No format more than 1 post in 3. Rewrite the fixed lines every time.**
- Our #42 format slid in posting order: 86.9%, 83.3%, 72.6%, 59.1% stayed (NNBA finding 2). [V numbers, H cause]
- Its pre-registered test ended 1 of 3 at 74%+ (OL, Oct 26). [V] OURS
- Every outside template decayed: Korzemba 23M to 8-49K, REBOUND 42M to 184K (WMV §2). [V] COMP
- YouTube's Jul 2026 policy targets interchangeable template videos (MP finding 4). [V official]

**4. Line 1 lands by about 3 s: one claim about the name or the moment. Never a bare number.**
- Line 1 done by 3.0 s: 71.1% stayed vs 62.2% (n=23 vs 14, WHY §2). [V] OURS
- "Ninety-two point nine." opened at 48% (PB L84). [S n=1] OURS

**5. Frame 1 proves line 1. Sharp and lit. Face or action both work.**
- Face vs action made no difference: 70.6% vs 68.4% (WHY §2). [V n=37] OURS
- A soft archive frame 1 (#52) kept 59.1%, confounded with a lesser star (SER). [S n=1]
- A dark frame 1 is a QA FAIL since S04 (QA L184-196). [V]

**6. Hold the opening. 2 or fewer shots in the first 3 s. About 10-15 shots in 20-30 s. Let a play run.**
- 15 or fewer shots: 75.0% vs 66.4% stayed (n=13 vs 24, WHY §2). [V] OURS
- 2 or fewer shots in the first 3 s: 75.0% vs 67.5% (n=7 vs 30, WHY §2). [S]: one arm is small, and topic travels with edit choice (WHY §2 caveats).
- Ahmed holds his first picture about 2.5 s (PB L45). [V] COMP

**7. No cards. The proof goes on the footage (words over the play, the scorebug, a circle).**
- Any card: 66.1% / 3.4K vs none 72.6% / 6.1K (n=20 vs 17). A card in the first 4 s: 63.2% / 1.9K vs 72.0% / 5.0K (n=9 vs 28) (WHY §2). [V] OURS
- Owner, Oct 26: "cut cards completely" (CS Oct 26 section). OWNER
- For soccer this is the owner's call, not soccer data: S01 had 6 cards and held 80% (story L111). [S]

**8. End on the payoff. Nothing after it.** No CTA, promo, teaser or question.
- A CTA line dropped end-viewers 12-27% on two curves (RA14 A6). [S] OURS
- Question endings (#12, #18) sat near 2.8K (RA14 A5). [S] OURS
- Ahmed: 32 of 33 October scripts end without a teaser (NFC rules table). [V] COMP. Owner, Oct 22. OWNER

**9. Every line adds something the clip can't show, and every fact has a source with its exact words.**
- Since Oct 1, 2026, YouTube says narration that only describes the screen is not original, and re-upload-style channels lose Shorts reach (MP finding 3). [V official]
- Critics found 4 of 14 hooks false or stale against a primary source (LL, Oct 5). [S] OURS

**10. Exact, verified footage from official sources, under 60 s when it's broadcast footage.**
- The critic found wrong-picture defects in 3 of 3 builds (RA14 D3). [V] OURS. The old hits put the exact moment under 8/11 and 11/13 shots (BRG rule 2). [S]
- No agency photos (#41's Imagn still, LL Oct 14). [V]. No other creators' edits or watermarks (MP safeguard 4). [V policy]
- A Short over 1 minute with an active claim is blocked worldwide on YouTube's US help page; the UK/IN/AU pages say this changed Sep 24, 2026 (MP finding 5). [V official, pages conflict] Keep FC under 59.9 s (QA L81) and NBA under 58 s (NNBA finding 5).

---

## 2. Rules to drop or rewrite now

Ordered by how much they cost us. Each item: the file and line, what it says now, the new wording, and why.

### 1. Playbook RULE 1 still makes #42 the lead format
- **Where:** PB L3-L23. Key lines: L3 "LEAD WITH WHAT WORKS: THE #42 FORMAT"; L19 "The critic must not APPROVE a script that doesn't fit."; L20 "**Retired** ...: news Shorts, rule explainers, lookalike/feel-good stories, "can he…?" questions, height/number oddities."
- **New L3:** `## RULE 1 (Oct 26): rotate 3-4 NBA lanes. No lane more than 1 post in 3. THE #42 FORMAT is one lane, not the lead.`
- **New L19:** `- **Checks:** script_lint.py says whether a script FITS THE #42 FORMAT. A script in another lane doesn't need to fit.`
- **New L20:** `- **Retired:** paperwork rules (bets, schedules, votes, stat credit), future "can he…?" questions, niche players. Lookalikes, height oddities and same-day news are back in rotation.`
- **New L23:** `- **Test result (Oct 26):** 1 of 3 reached 74%+ (#48 83.3%, #64 72.6%, #52 59.1%). Not proven. #52 was read at about 1 day old.`
- **Why:** the test failed (OL Oct 26) [V]. The "retired" lanes did well: #49 lookalike 77.4% stayed, #41 "taller than Wemby" 82.4% (SER) [V]; #19 Flagg height 21K (WHY §1) [V]; #58 news 23K (SER) [V]. Decay risk (NNBA finding 2). OURS.

### 2. "Find 6+ clips before writing, or drop the topic"
- **Where:** cloud L49 "Before writing, find 6+ different real clips ... If a topic has under 6, find a fresher angle ... or drop it." cloud L57 "Order: research -> find 6+ clips -> script around the clips". nba L38 "until six moving clips exist"; nba L43 "six moving clips are named". PB L287 lists "fewer than 6 sources" as a QA FAIL.
- **New cloud L49:** `1. **Footage first.** Before writing, secure frame 1 and one proof clip for each beat: the exact moment, from any number of sources. No frame 1, no script: change the angle or park it. Never cut away to filler to reach a clip count.`
- **New cloud L57:** `Order: research -> frame 1 + a proof clip per beat -> script -> voice -> shots.json -> assemble -> qa_short PASS -> package.`
- **nba L38/L43:** replace "six moving clips" with "frame 1 and a proof clip per beat". **PB L287:** delete the line.
- **Why:** the 6-clip gate "pushed illustrative filler" and cut away from the moment (WHY §3) [S]. No evidence ever backed it (R6 §9: "UNSUPPORTED"). QA already made it a warning for NBA (QA L130-132). Footage-first itself is backed (RA14 D2) [V]. **[BAD INFO?] [SLOWS]**

### 3. CLOUD STATE's "House rules" line, read first by every agent
- **Where:** CS L28: "Real footage first (6+ clips before scripting), hook = real striking image + name/number line at 0.0 s, 3+ cuts in 3 s, 21-45 s, loop to the first shot, end on a comment-bait question, titles 4-7 words opening Why/How/What/Did/Is/He + one emoji, tags 440-490 chars, no description, one cover."
- **New:** `House rules: see "The 10 rules that matter most" in Research Notes/Rules Review (Oct 26, 2026).md. (The Oct 3 summary that stood here was wrong on clip count, cuts in 3 s, the loop and question endings.)`
- **Why:** 4 of its 9 rules are now contradicted: 6+ clips (item 2), 3+ cuts (WHY §2), the loop (item 7 below) and the question ending (rule 8 above). CS L1 calls the file the "single source of truth".

### 4. The daily run is told three different lane rules
- **Where:** daily L57 "first look for last night's **visible moment** ... Use a record/stat story only when no strong moment exists ... (about 1 in 3)". daily L58-L60 "Pick the story that fits THE #42 FORMAT ... or a same-day number-gap story". daily L68 "`/cloud-short` in THE #42 FORMAT: 20-30 s". cloud L34 "About 2 of every 3 NBA Shorts: one moment you can watch ... or a viral creator/streetball clip with an NBA name".
- **New daily L57-L60:** `- **NBA lane:** pick by rotation (the bullet above): a moment you can watch, a star paradox (THE #42 FORMAT is one), same-day news with a number gap, or evergreen superstar history. No lane more than 1 post in 3 until the moment test (section 4 of the Rules Review) says otherwise. A moment needs one fact the clip can't show (MP: audio-only test). Footage from the league, teams and broadcasters only; never another creator's edit (no House of Highlights or fan reels as the base).`
- **New daily L68:** `/cloud-short` in today's lane: length follows the story (cap 58 s), the Alex voice, no music unless the music test is on, words over footage.
- **New cloud L34:** same lane wording as above; drop "or a viral creator/streetball clip".
- **Why:** "2 of 3 moments" rests on one competitor channel, classified by us from titles, with its oldest posts also its weakest (SW §2) [V COMP, age-confounded]. Our own moment data is thin (#49 77.4%, SER) [S]. The Oct 24 policy note says the moments lane is "the most exposed format we have" and lists "House of Highlights-style reels" as a common mistake (MP finding 3; "What sports Shorts channels commonly get wrong" item 2) [V official]. **[BAD INFO?]** for the "2 of 3" number.

### 5. Soccer length: the skill and QA disagree
- **Where:** story L59 "260-290 words. After step 4b that runs about 60-68 s". story L88 "If the length is under 58 s, add a verified beat and re-voice." story L134 "length 58-88 s". story description L4 "Make a 60-80 s story Short". story `QA.md` L6-L8 "FAIL outside 55-120 s; warn outside 58-88 s". FCPB L6 and L20 "60-80 s". FCSH L17 "60-80 s per Short".
- **New story L59:** `- About 230-250 words. After step 4b it must end under 59.5 s (S01: 253 words ran 59.5 s; 194 words ran 46 s).`
- **New story L88:** `- Output: voice.mp3, words.json, captions.srt. If it runs 59.5 s or more after step 4b, cut a sentence; never add one.`
- **New story L134 and QA.md L6-L8:** `Length: FAIL outside 50-59.9 s; warn over 59.5 s.` (This is what QA L81-83 already does.)
- **FCPB L6/L20, FCSH L17, story L4:** "60-80 s" becomes "under 60 s (YouTube cut)".
- **Why:** a script written to the skill fails QA and must be re-cut or re-voiced. QA enforces 50-59.9 s (QA L81) because of the claim rule (MP finding 5) [V official]. **[SLOWS]**

### 6. The first-3-seconds section still teaches the old opening
- **cloud L100** now: "The number, name or stakes is the FIRST word ... ("92% pay cut. LeBron James just took one...")". **New:** `- **Line 1 is one claim about the name or the moment, done by about 3 s.** Never a bare number first. Never open on "So" / "Did you know" / a setup sentence.` Why: PB L84 hook gate; WHY §2 (71.1% vs 62.2%) [V]; QA's naked-number warning (QA L265-266).
- **cloud L101** now: "Punch in: put `"zoom": 0.12` on the first shot". **New:** `A push-in only on a static first shot: 2-5%, at most 4% a second (footage_qc warns above it).` Why: ESS L44 and footage_qc set 2-5% and 4%/s; PB L242 says 6% or less. No evidence for any size (R7 §4 row 2) [H].
- **cloud L107** now: "If two neighbours look alike, add a cut." **New:** `If frame 1 doesn't show the claim, change the shot, not the cut rate.` Why: adding cuts is the habit WHY §2 links to lower stayed % [S/V].

### 7. The forced loop
- **Where:** cloud L54 "Last shot reuses the first clip (loop)." nba L37 "the last shot loops that clip". FCPB L24 (NBA column) "Payoff, then the last frame loops to the first". cloud L63 and L95 "last line echoes the first (loop)".
- **New cloud L54:** `Ends on the PAYOFF image that answers the first line. Loop into frame 1 only when that image is the payoff; never add a shot just to loop.`
- **Why:** loop gains come from vendor anecdotes (R6 §3: "HYPOTHESIS size") [H]. Forcing it made a 0.28 s noise shot in #41 (RA14 B7) [V]. #64 ended better on its payoff image (LL Oct 21) [S]. QA only warns (QA L159-160). **[BAD INFO?]**

### 8. Sound effects: five files, five different numbers
- **Where:** cloud L104 "Four effects when the pictures support them, never more than five". cloud L131 "4 effects ... else 3, never more than 5". LL L7 "four different files". story L127 "3-5 effects". F42 L49 "2-4 effects". ESS L79 "0-3 per Short". PB v3 §5 (L273) "2-5".
- **New (all of them):** `0-4 effects, each on something you can see happen. No file twice, at least 1.5 s apart. Zero is fine.`
- **Why:** no evidence for any count (R6 §5 "SFX: No evidence"; RA14 B11 "no evidence, low cost") [H] GEN. "Aim for four" pushes effects in. The `Tools/sfx` files have an unknown licence (RA14 D13) [V]. **[BAD INFO?]**

### 9. Cards: the tools still make long ones
- **cloud L127** now: `python Tools/card.py ... --len 2.4`. **New:** `--len 1.5` (QA FAILs a card over 1.5 s: QA L140-141).
- **cloud L6** (description) now: "build screenshot evidence cards". **New:** "put the proof on the footage (words over the play, the scorebug, a circle)".
- **LL L22** "Keep cards <= 2 s and <= 25% of runtime" and **PB L220** "Cards: proof only ... none in the first 4 s (TEST)": mark superseded by rule 7.
- **story SOURCING.md L7** "Its graphics ... make strong evidence cards": `Its graphics are proof on the footage: show them as broadcast shots, not as cards.`

### 10. Pace targets that our data doesn't support
- **Where:** cloud L63 "[SUPPORTED] Speech 240-290 wpm". cloud L72 and L78 "230-270 wpm". PB L219 "about 220-230 wpm". PB L150 "Read it aloud at 220 wpm". PB L441 "fast (~250 words/min)".
- **New:** `Pace: whatever the house voice reads at its set speed (#42 ran about 195 wpm). No target. QA warns only outside 200-265.`
- **Why:** pace vs stayed: 0.10, no link (WHY §2) [V n=37]. The 240-290 range came from CoachClank's 8 biggest Shorts (R6 §5) [S] COMP. #42, our best, ran about 195 wpm (F42 L36) [V]. **[BAD INFO?]**

### 11. Titles: an old one-channel rulebook still scores them
- **Where:** TP L34-L39 ("Ask it ... beats a statement", "Don't start with This…", "4-7 words. Never 8+"). titles L16-L21 (the 5-point score). cloud L23 and L136. nba L39-L42. PB L459.
- **New (TP "The 5 title rules" and titles step 3):** `Title = the premise or spoken line 1 in plain words, true to the video, about 4-8 words. Question or statement, emoji or not: no measurable effect. Don't score titles.`
- **Why:** pooled over 13 NBA channels, question titles are 0.88x (n=329) and "This/These/The" openers 1.05x (NNBA Q5) [V] COMP. Swishyyy: question 40K vs statement 41.5K; emoji 45.5K vs 41K (SW §2) [V] COMP. Our old era: no title split moved the median more than 3K (RA14 D5) [V] OURS. TP is CoachClank alone, Sep 2026 (TP L3-6). **[BAD INFO?]**

### 12. Music: the default is "none", but three pages still prescribe a bed
- **PB L221** now: "Sound: a music bed by story type, 20 dB under the voice". **New:** `11. **Sound:** no bed by default (owner, Oct 14) until the music test decides. Log "music yes/no" and the exact file posted, every time.`
- **SL L50** now: "**Default:** route C (our beds) is baked in." **New:** `**Default:** no bed (the house rule at the top). Route C only on purpose or in the music test.`
- **F42 L50** (rule column) now: "instrumental only, dipped under the turn". **New:** `none by default; the music test decides; log music yes/no in UPLOAD.md`.
- **QA L272-273** warns on any baked-in bed, soccer included: skip that warning for the story profile (a bed is the soccer default, story L128).
- **Why:** the owner's Oct 14 call is the default (PB L121). No data either way (WHY §3) [H]. Neither channel logged which version was posted (F42 L50; FCOL "not recorded").

### 13. "Drop a news Short that's a day late"
- **Where:** US L15 "A news Short that misses its day is skipped, not posted late". daily L61 "Only stories from the last 24 h".
- **New:** `Prefer same-day news. A late news Short goes out only with a timeless angle (a record, a "why"). Log its age in hours.`
- **Why:** the rule rests on one Short, #63 (57.6%, 1.4K, SER) [S n=1]. #66 was slotted two days after its Thursday game ("post now", US L24) and had 6.5K by Oct 26 (OL) [S n=1]. Also inconsistent: the NBA Diagnosis says "under 36 h". **[BAD INFO?]**

### 14. Script Critic v3 is a hard gate that was never validated
- **Where:** PB L71 "Script Critic v3 must APPROVE a script before any footage or voice work". SH L14 "every script must pass before footage or voice".
- **New:** `Script Critic v3 is advisory until its prediction check (score vs 72 h views at 10 scored posts) shows Spearman 0.3 or more.`
- **Why:** the "check at 10 posts" (OL Oct 14 late night; Script Critic Log §D) was never run. Its two REJECTs, #40 (28) and #41 (30) (OL Oct 14 late night), later reached 6.7K and 9.7K public (OL Oct 19), above the 3.9K new-era median (WHY §1) [S]. The daily run doesn't call it anyway (daily, no critic step). **[SLOWS]**

### 15. Leftover lines to mark superseded or delete
| File, line | Says now | Do |
|---|---|---|
| QA L8-L14 (docstring) | ">=3 different shots in the first 3 s", "average shot <= 1.9 s", ">=6 distinct source clips", "LENGTH 18-35 s. Last shot repeats the first clip" | Rewrite to the gates the code runs (section 5, QA table) |
| PB L277-L297 | the Oct 14 QA FAIL/warn lists ("fewer than 6 sources", "a shot too long", "3 shots in 3 s") | Replace with "see the header of Tools/qa_short.py" |
| PB L245-L246 | "typically 1-2.5 s"; "'3 shots in 3 s' is a guideline" | "About 2 s; let a play run 3-5 s; 2 or fewer shots in the first 3 s" |
| LL L40 | "The gate ... 3+ shots ... avg <= 1.9 s ... 6+ clips ... loops" | Mark "SUPERSEDED Oct 14 and Oct 26" |
| LL L7, L13, L17 | "four different files", "tags 440-490", "titles 5-7 words with one emoji" | Mark superseded |
| ESS L38 | "Footage shots up to 3.6 s, quotes up to 4.5 s" | "NBA up to 6 s (QA); soccer 3.6 s" |
| ESS L114 | "An F twin is made when credits allow" | Delete: Alex only (owner never picked F; clone consent undocumented, MP safeguard 5) **[SLOWS]** |
| cloud L55 | "render a red-circle twin with `Tools/pointer.py` for the frame-1 test" | Delete: that test is VOID (OL Oct 19) **[SLOWS]** |
| cloud L64 | "[SUPPORTED] Captions: sentence case ..." | Change the tag to [H]: competitors only, never tested here |
| cloud L62 | "[PROVEN] Story length 21+ s (CoachClank ...)" | Delete: our old era's under-18 s Shorts had the best median (RA14 A8) |
| cloud L63, L79; nba L34 | "a turn word ... in the first 40%" | Delete: no support in our data (RA14 D7) |
| cloud L137-L138 | "Covers: `thumb.py --shape short` x3" then "make just one" | "One cover, 5 minutes max" **[SLOWS]** |
| PB L223 | "up to 3 hashtags; about 12 tags" | "Tags: `tags_fit.py` fills to 490 (owner's rule, daily L87-88); hashtags optional" |
| nba L14, L20, L57 | Windows ROOT; "MetaSports - Scripts (Batch 2).md (match this style exactly)"; "post between 6 and 11 AM ET" | Retire the skill or point it to `cloud-short`. SH L44 lists Batch 2 as superseded |
| story L4-L6, FORMAT.md L12, FCPB L6, FCSH L19 | "Back in [year], [famous name]..." as the opener | "Line 2: a named person doing something concrete; 'Back in' is optional" (Ahmed: 1 of 30 October scripts, NFC table) |
| FCPB L7 | "Global names only" | "A famous name by default; a niche story only with an absurd, concrete fact" (NFC table) |
| FCPB L21-L22 | NBA "3 cuts in 3 s"; NBA captions "karaoke/clank" | "1-2 shots in the first 3 s"; "house style (white Montserrat caps)" |
| BRG L95 | "short cuts (≤2-3 s each)" | "Short excerpts, each with our narration over it" (generic fair-use advice; it clashes with "let a play run") |
| SER L13 | "post them with singular titles" | Note: withdrawn (NFC finding 3) |

---

## 3. Contradictions between files

### 3a. Were the old Round 4/5 editing rules removed? No.
They are gone from the QA code (NBA profile) and from the top box of `cloud`. They survive here:

| Old rule | Still in |
|---|---|
| "3+ cuts in the first 3 s" | CS L28; FCPB L21; PB L246 and L294; QA L8 (docstring); cloud L107 ("add a cut") |
| "Average shot 1.4-1.9 s / no shot over 3 s" | QA L10 (docstring); LL L40; PB L245 (1-2.5 s); cloud L94 (1.5-3 s); ESS L38 (3.6 s cap); BRG L95 (≤2-3 s) |
| "Evidence cards for any fact line" | cloud L6 (description); cloud L126-L129 (`card.py --len 2.4`, over the 1.5 s FAIL); LL L22; PB L220; story SOURCING.md L7 |
| ">= 6 source clips" | cloud L49 and L57; nba L38 and L43; PB L287; CS L28; story QA.md L22; QA L130-L132 (still a FAIL for soccer) |

### 3b. Cross-file contradictions
| Topic | One file says | Another says | Which should win |
|---|---|---|---|
| Lead format | PB L3, SH L4, CS L3, daily L59 and L68: lead with #42 | F42 L3, WMV §2, cloud L60: 1 in 3. cloud L34, daily L57: 2 of 3 moments | Rotation, 1 in 3 each (test result, OL Oct 26) |
| Retired lanes | PB L20: lookalikes, height oddities, news retired | SER: #49 77.4%, #41 82.4%; #58 news 23K | Our data |
| Moments + sources | cloud L34, daily L57: viral creator clips; House of Highlights | MP finding 3 and safeguard 4: retire narrated moments; no other creators' edits | MP (official policy) |
| Opening cuts | cloud L102: 1-2 shots | cloud L107: "add a cut"; CS L28: 3+ | cloud L102 (WHY §2) |
| First word | cloud L100: number first | PB L84 and QA L265: never a bare number | PB |
| First-shot push-in | cloud L101: 12% | PB L242: ≤6%; ESS L44: 2-5%, ≤4%/s; F42 L48: 5-10% | ESS (QA tools enforce it) |
| Frame 1 face | F42 L43: not a face; story L117-L118: a face only if the title is about it | cloud L101: "or already a face"; WHY §2: no link | WHY: face or action, as long as it proves line 1 |
| Shot cap | QA: 6 s NBA | ESS L38: 3.6 s; PB L245: 2.5 s; BRG L95: 2-3 s | QA (WHY §2) |
| Clip count | cloud L43: warning only | cloud L49/L57, nba L38/L43: required | cloud L43 |
| SFX count | ESS L79: 0-3 | F42 L49: 2-4; PB L273: 2-5; story L127: 3-5; cloud L104: 4, max 5 | One line: 0-4 (no evidence for any) |
| Pace | PB L219: 220-230 | cloud L63: 240-290; cloud L72/L78: 230-270; PB L441: 250; QA: 200-265 | No target (WHY §2) |
| NBA length | PB L134: 20-30 s | nba L34: 22-26 s; cloud L78: 22-30; cloud L92: 23-40; cloud L62: 21+; PB L438: 22-40 | "Follows the story, cap 58 s" (WHY §2, NNBA finding 5) |
| Soccer length | story L59: 60-68 s; L88: add a beat under 58 s | QA L81: FAIL at 60 s; daily L72: 55-59.5 s | QA |
| Loop | cloud L54, nba L37, FCPB L24: loop to frame 1 | PB L262, QA L159 (warn), LL Oct 21: only when it serves the payoff | PB L262 |
| Ending | CS L28: "end on a comment-bait question" | every other file: never a question | Payoff |
| Music | PB L121, SL L4: no bed | PB L221 (checklist), SL L50, F42 L50: a bed | No bed until tested |
| Music QA | story L128: soccer uses a bed | QA L272: warns "house default is none" on every bed | Skip the warn for soccer |
| Cards | QA L140: FAIL over 1.5 s | cloud L127: 2.4 s; LL L22: ≤2 s | QA (owner) |
| Titles | TP, titles, cloud L23/L136: question, Why opener, no "This" | NNBA Q5: questions 0.88x, "This/The" 1.05x; SW: no effect; RA14 D5: stop scoring | NNBA, SW, RA14 |
| Tags | cloud L137, daily L88, LL L13: 440-490 chars | PB L223, RA14 D8: about 12 | Owner's 490 (automated, free) |
| Hashtags | PB L223: up to 3 | TP L36: none | Optional; no evidence either way |
| Covers | cloud L137: three | cloud L138: one | One |
| Post time | nba L57: 6-11 AM ET | US: 11 AM / 12 PM / 6 PM ET | US (R6 §1: timing matters little) |
| Late news | daily L61: 24 h | NBA Diagnosis §3.2: 36 h | Test (section 4) |
| Critic gate | PB L71: Critic v3 APPROVE first; PB L141: Critic v2 | daily: no critic step; cloud L79: the retired Round 2 scorecard | See section 2, item 14 |
| #42 vs the critic | F42 L32: end on the flip number | `Tools/script_critic.md` Payoff anchor: "Answers the hook with a number" = 3, and APPROVE needs 4+ | Fix the critic anchor if it stays |
| Soccer "copy, change nothing" | story L21, FCSH L8, FCPB L6 | NFC finding 4 (Ahmed's medians fell and he changed format); MP finding 4 (write our own openers) | Copy the mechanics that still hold |
| Soccer titles | SER L13: singular titles | NFC finding 3: shape is neutral | NFC |

---

## 4. Rules to turn into tests

One test at a time stays the rule (PB L161). Log every variable in DS: it has frame 1 filled for 0 of 120 rows, folder for 0 of 120, music for 40 of 120 (counted today). The rule "every rule change must cite this table" (daily L41) can't work until those columns are filled.

| # | Test | Design | Decide at | Why it's a test, not a rule |
|---|---|---|---|---|
| 1 | Moments lane share (NBA) | Moments as 1 post in 3; every moment passes the audio-only test | 6 moment posts vs the channel median stayed % and 7-day views | "2 of 3" is one competitor, title-classified, age-confounded (SW §2) [V COMP]; ours n=1-2 [S] |
| 2 | Music bed vs none (NBA) | Alternate a royalty-free bed at -20 LU and none, both calm cuts | 6 each, stayed % at 72 h | Untested; old hits all had a bed but so did the weak control (WHY §3; Music Guide L10-12) [S]. Needs the owner's yes (WHY §5) |
| 3 | Music bed vs none (soccer) | Log which file was posted; alternate by day | 6 each | Never logged (FCOL) |
| 4 | Length 35-45 s vs 22-28 s (NBA) | Same lane, two turns in the long cut | 5 pairs | No link in 20-33 s (WHY §2) [V]; CoachClank's best band is 31-45 s (NNBA finding 5) [S COMP]; never tried |
| 5 | Script Critic v3 prediction check | Score vs 72 h views, posts since Oct 14 | 10 scored posts; keep as a gate only if Spearman ≥0.3 | Never validated; two REJECTs beat the median (section 2, item 14) |
| 6 | Late news | Log hours since the event on every news Short | 5 posts over 24 h old | #63 vs #66, n=1 each [S] |
| 7 | Soccer hook rules (frame 1 shows the promise; promise back by 20 s; ≤10 names in 15 s) | Keep as warnings; log each on every post | 10 soccer Shorts (AUD24 §6) | n=3 [S]; S03 broke all three and reached 14K (FCOL; S23) |
| 8 | Sound at 0 s | A whoosh/pop on frame 1 vs voice only | 3 pairs | The old hits opened with one (WHY §2); the "no sound in the first second" rule is untested (WHY §3) [H] |
| 9 | Soccer shot rate | 40-50 shots a minute (story L116) vs about 25 | 3 pairs | Ahmed's rate [V COMP], but NBA data says calmer holds better [V]; unknown for soccer [H] |
| 10 | Caption style (NBA) | House ALL CAPS vs sentence case | 6 each, low priority | Style didn't separate winners (RA14 B9) [V]; Swishyyy uses ALL CAPS too (SW §3) [S] |
| 11 | 1 a day vs 2 a day (NBA) | The Oct 14-19 test was set up (OL Oct 14) but never read | Read it, or close it | Pre-registered, never scored |

Parked, owner decides: premise pill on frame 1 (#19 only, RA14 B12) [S n=1]; question vs statement hooks (OL "Q1") [S].

---

## 5. The full table

Columns: rule (where) · verdict · evidence and tier · origin · flags.

### A. Topic lane (NBA)
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| Lead with THE #42 FORMAT (PB L3; SH L4; CS L3; daily L59, L68) | CHANGE: one lane, ≤1 in 3 | Test 1 of 3 (OL Oct 26) [V]; decay (NNBA §2) [V/H]; born from #42 alone (F42 L62 "n=1") | OURS | [BAD INFO?] as a lead rule |
| 2 of 3 NBA Shorts are moments (cloud L34; daily L57) | TEST at 1 in 3 | SW §2 [V COMP, age-confounded]; CoachClank 419K median, 34% at 1M+ (NNBA §3) [V COMP]; ours thin [S]; policy risk (MP §3) [V] | COMP | [BAD INFO?] |
| Household name + one-line paradox (AUD24 §2) | KEEP | 6/6 of 20K+ [V] | OURS | |
| No technicalities or niche players (PB L67) | KEEP | Bottom 6 of 22 [S] | OURS | |
| No paperwork rules; visible rule-breaking OK (cloud L60) | KEEP | 63.7% / 2.0K, n=6 [V]; 1.42x, n=79 [V COMP] | OURS, COMP | |
| Retired: lookalikes, height oddities, rule explainers, news (PB L20) | CHANGE | #49 77.4%, #41 82.4%, #19 21K, #58 23K (SER; WHY) [V] | OURS | contradicts our data |
| No future "can he…?" questions (PB L20; NNBA table) | KEEP | #46 49.8%, #21 64% (NNBA table) [S] | OURS | n<5 |
| Contracts only with a hook (PB L40; cloud L22) | KEEP | Ahmed money 0.88x age-adjusted (NNBA CSV) [V COMP]; Duren 63% (CS L55) [S] | OURS, COMP | |
| Never retell a bigger channel's story; copy-check (cloud L88) | KEEP | #29 1.4K vs CoachClank 10.9M (LL Oct 15) [S n=3] | OURS | cheap |
| Re-run copy-check the morning of posting (PB L438) | KEEP | #65's lane closed in 12 h (LL Oct 21) [V] | OURS | |
| Same-day news only (daily L61; US L15) | TEST | n=1 each way (section 4) | OURS | [BAD INFO?] |
| Retire a lane after 3 posts below median (cloud L60) | KEEP | Template decay (NNBA §2) [V COMP] | COMP | |
| Too many spoken numbers (NBA Diagnosis §3.3) | DROP as a rule | Numbers spoken vs stayed: 0.15, no link (WHY §2) [V] | OURS | |

### B. Topic lane (soccer)
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| Copy Ahmed, change nothing (story L21; FCSH L8; FCPB L6) | CHANGE | Ahmed's medians fell 411K to 178.5K and he changed format (NFC §4) [V COMP]; template policy (MP §4) [V] | OWNER, COMP | |
| Global names only (FCPB L7) | CHANGE | "Too strict" (NFC table) [S COMP] | COMP | |
| "Versus their own" lane (story L39-L43) | KEEP | 1.63x, n=87 (NFC §2) [V COMP] | COMP | |
| Numbered star serial (story L41) | TEST | FOOTY FACTS 1.4M vs 162K (NFC §6) [V COMP, one channel] | COMP | |
| Topical question lane (story L42) | TEST | Ahmed 238K vs 245K (NFC §4) [V COMP] | COMP | |
| Hook word: object or strong verb (story L72-L73) | KEEP, softened | Strong verbs 1.35x, n=107; "trouble" titles 1.0M, n=3 (NFC §3) [V COMP] | COMP | |
| Promise back by 20 s; ≤10 names in 15 s (story L75-L76) | TEST (keep as warns) | n=3 [S]; S03 broke both, now 14K (FCOL) | OURS | [BAD INFO?] |
| Title shape neutral; title = line 1 (story L139) | KEEP | NFC §3 [V COMP] | COMP | |

### C. Title and package
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| 4-7 words, question or Why opener, emoji, no "This" (TP; titles; cloud L23, L136; nba L39; PB L459) | CHANGE | NNBA Q5 [V COMP]; SW §2 [V COMP]; RA14 D5 [V] | COMP (Sep) | [BAD INFO?] |
| Avoid 🤔 (cloud L23) | DROP | n=5 (R6 §9) | COMP | [BAD INFO?] |
| Title = the premise, posted exactly (PB L223) | KEEP | Feed is 94.5% of views (PB L194) [V] | OURS | |
| Tags filled to 490 chars (daily L87-L88) | KEEP (owner), automated | No measured effect (R6 §1) [S]; search 3.9% of views (RA14 D8) [V] | OWNER | free with `tags_fit.py` |
| About 12 tags (PB L223) | DROP | Conflicts with the owner's 490 | — | |
| Up to 3 hashtags (PB L223) / none (TP L36) | Optional | "Not required" (MP) [V]; hashtags ~10% fewer views, correlation (MP) [H] | GEN | |
| No description | KEEP | Empty description 1.00x vs 1.00x (R6 §1) [V COMP] | OWNER | |
| Pinned debate comment | KEEP | Zero cost; comments don't drive reach (R6 §1) [S] | OWNER | |
| Three covers (cloud L137) | CHANGE to one | The feed shows no covers (R6 §1) [S] | GEN | [SLOWS] |

### D. Length and pace
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| NBA 20-30 / 22-26 / 22-30 / 23-40 / 21+ / 22-40 s (six places, section 3b) | CHANGE to one: follows the story, cap 58 s | No link in 20-33 s (WHY §2) [V] | OURS | |
| "[PROVEN] 21+ s" (cloud L62) | DROP | CoachClank only; our under-18 s Shorts had the best old-era median (RA14 A8) [V] | COMP | [BAD INFO?] |
| Soccer 260-290 words, 60-68 s; add a beat under 58 s (story L59, L88) | CHANGE | QA FAILs at 60 s (QA L81) | — | [SLOWS] |
| Soccer under 59.9 s (QA L81; daily L72) | KEEP | US help page (MP §5) [V official] | policy | |
| Pace targets 220-290 wpm (cloud L63, L72, L78; PB L150, L219, L441) | DROP targets | 0.10, no link (WHY §2) [V]; #42 about 195 wpm (F42 L36) | COMP | [BAD INFO?] |
| Word-count windows (nba L34 90-110; cloud L92 95-150; PB L134 85-110) | DROP | Word count -0.08 (WHY §2) [V] | OURS | |

### E. First line
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| One claim, done by about 3 s (PB L80; QA slow-hook warn) | KEEP | 71.1% vs 62.2% (WHY §2) [V] | OURS | |
| Number or name as the first word (cloud L100) | CHANGE | Bare number 48% (PB L84) [S] | GEN (Round 4) | [BAD INFO?] |
| No filler first word (QA FAIL, QA L89-L90) | KEEP | Logic [H]; free | GEN | |
| Hook has a name/number word (QA FAIL, QA L117) | KEEP (weak) | Passes almost every hook (R7 §7.5 row 10) [V code] | GEN | |
| Turn word in the first 40%; re-hook at 45% (cloud L63, L79, L93; nba L34) | DROP | No support in our data (RA14 D7) | COMP n=8 | [BAD INFO?] |
| Say the viewer's question out loud by 6-8 s (PB L109) | KEEP as a check | CoachClank breakdown, small n (PB L108) [S] | COMP | |
| Soccer: title read as line 1 (FORMAT L11) | KEEP | 33 of 33 Ahmed scripts (NFC table) [V COMP]; S01 80% [S] | COMP | |
| Soccer: "Back in [year]" (story L4-6; FORMAT L12; FCPB L6; FCSH L19) | DROP as default | 1 of 30 October scripts (NFC table) [V COMP] | COMP (old) | |

### F. Frame 1
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| Frame 1 proves line 1 (WMV §2; daily L70) | KEEP | #42 airball 86.9% [S]; face vs action no link [V] | OURS | |
| "Not a face" (F42 L43) / "or already a face" (cloud L101) | CHANGE: either, if it proves line 1 | 70.6% vs 68.4%, n=37 (WHY §2) [V] | OURS | |
| Frame 1 lit (QA FAIL) | KEEP | S04 (LL soccer, Oct 24) [V] | OURS | |
| Push-in on frame 1: 12% / ≤6% / 2-5% / 5-10% (cloud L101; PB L242; ESS L44; F42 L48) | CHANGE to 2-5%, ≤4%/s | No evidence for any size (R7 §4 row 2) [H] | GEN | |
| Red ring + twin render (cloud L55) | DROP the twin | Test VOID (OL Oct 19) | OURS | [SLOWS] |

### G. Shots and cutting
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| ≤2 shots in the first 3 s (cloud L40; QA warn) | KEEP as a warn | 75.0% vs 67.5%, n=7 vs 30 (WHY §2) [S] | OURS | |
| About 10-15 shots in 20-30 s (cloud L42) | KEEP | 75.0% vs 66.4%, n=13 vs 24 (WHY §2) [V] | OURS | |
| Average shot 1.8-3.0 s (QA warn) | KEEP as a warn | 75.0% vs 66.4%, n=11 vs 26; views 4.2K vs 3.7K (WHY §2) [V] | OURS | |
| Shot cap: NBA 6 s, soccer 3.6 s (QA L118-L119) | KEEP; fix ESS L38, PB L245, BRG L95 | #42 held one play 5 s (WHY §2) [S] | OURS | |
| ≥6 clips, ≤35% one clip (cloud L49, L57; nba L38; PB L287; QA.md L22) | DROP for NBA docs; warn for soccer | Pushed filler (WHY §3) [S]; unsupported (R6 §9) | GEN | [SLOWS] [BAD INFO?] |
| ≥35% b-roll, ≤45% talking head (cloud L51; QA warn) | KEEP as a warn | One complaint, #15 v1 (R6 §4) [S n=1] | OURS | n=1 |
| Soccer 40-50 shots a minute (story L116) | TEST | Ahmed 1.1-2.1 s (FORMAT L25) [V COMP] | COMP | |
| Same footage twice (QA warn; footage_qc FAIL) | KEEP; mark replays when showing angles | #21, #30 replays (LL Oct 14) [V] | OURS | |
| Hold the payoff shot longest (PB L260) | KEEP | Old hits (BRG rule 4) [S] | OURS | |

### H. Cards and proof
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| No cards; ≤1.5 s; none in the first 4 s (QA L136-L143, L232-L234) | KEEP | WHY §2 [V]; owner | OURS, OWNER | |
| Soccer: no cards (story L111) | KEEP (owner) | S01 had 6 cards and 80% (story L111) [S] | OWNER | not soccer data |
| `card.py --len 2.4` (cloud L127) | CHANGE to 1.5 | QA FAIL over 1.5 s | — | |
| Proof on footage: words over the play, scorebug, circle (cloud L41; BRG rule 3) | KEEP | #42, #48 (WHY §2) [S]; old hits (BRG rule 3) [S] | OURS | |
| Circle the scorebug number (BRG rule 3) | KEEP | Old hits (RA14 B14) [S] | OURS | |

### I. Captions
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| House style: white Montserrat ALL CAPS, 45-62% band (PB L120, L139; ESS §3) | KEEP (owner); low-priority test | Style didn't separate winners (RA14 B9) [V]; Swishyyy ALL CAPS (SW §3) [S]; caps read slower in lab studies (R6 §4) [V lab, H for Shorts] | OWNER | |
| "[SUPPORTED] sentence case" (cloud L64) | CHANGE the tag to [H] | Competitors only | COMP | [BAD INFO?] |
| Captions = script word for word (export_check FAIL) | KEEP | Catches real errors (ESS §6) [V] | OURS | |
| Red/green on ≤35% of cards (ESS L63) | KEEP | House | OWNER | |
| Soccer: TikTok Sans, centred (FORMAT L31-L36) | KEEP | Ahmed [V COMP] | COMP | |

### J. Music
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| NBA: no bed by default (PB L121; Music Guide L3; SL L4) | KEEP + TEST | No data either way (WHY §3) [H] | OWNER | |
| "A music bed by story type" (PB L221); "route C baked in" (SL L50); "instrumental, dipped" (F42 L50) | DROP | Contradict the default | — | |
| Soccer: bed plus a no-music render (story L128-L131; FCPB L11) | KEEP, but log the posted file | "Not recorded" for S01-S03 (FCOL) | COMP | [SLOWS] until logged |
| QA warns on any bed (QA L272-L273) | CHANGE: skip for soccer | Soccer default is a bed | — | |
| No partner or library music baked in | KEEP | Partner music halves the pool share (NNBA Q2) [V official] | policy | |

### K. Sound effects
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| Counts: 0-3 / 2-4 / 2-5 / 3-5 / four (section 3b) | CHANGE to 0-4 | No evidence (R6 §5; RA14 B11) [H] | GEN | [BAD INFO?] |
| Nothing in the first second (cloud L103) | TEST | Old hits had a whoosh/pop at 0 s (WHY §2) [S] | GEN | |
| Only on a visible event; no file twice; ≥1.5 s apart; no vine boom (cloud L103-L105) | KEEP | Habituation (R7 finding 6) [S GEN]; owner | GEN, OWNER | |
| Replace `Tools/sfx` with logged licences (RA14 D13) | KEEP | Unknown source [V] | — | |

### L. Voice
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| Alex, one voice (PB L135; daily L68) | KEEP | Voice ruled out: #42 84.3% and #46 49.8%, same voice (NBA Diagnosis §3.4) [V]; AI voices fine (NNBA §6) [S] | OURS, COMP | |
| F (clone) twins (ESS L114; PB L135) | DROP | Never picked; consent not documented (MP safeguard 5) | — | [SLOWS] |
| No stretch, no denoise, pause cap (PB §6) | KEEP | Voice audition (LL Oct 14 night) [V] | OURS | |
| `tighten_voice.py` (NBA 0.25→0.12 s; soccer 0.09→0.06 s) | KEEP | Owner, Oct 22 | OWNER | |
| `pronunciation.json`; braces for numbers | KEEP | "Wembun Yama" 9/9 (LL Oct 14) [V] | OURS | |
| 2-3 real quote bursts ≤4 s (cloud L52, L73) | KEEP as an option | Voice-change mechanism (R7 finding 6) [S GEN] | GEN | |
| Quote shot plays at 1.0x (QA FAIL) | KEEP | #38 lip drift (LL Oct 14) [V] | OURS | |
| One first-person aside per script (NFC §7) | KEEP | Originality [H] | COMP | |

### M. Ending
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| End on the payoff; no CTA, promo, question | KEEP | Rule 8 above | OURS, COMP, OWNER | |
| Loop: last shot = first clip (cloud L54; nba L37; FCPB L24) | CHANGE | Vendor anecdotes (R6 §3) [H]; #41 noise shot (RA14 B7) [V] | GEN | [BAD INFO?] |
| Last line echoes the first (cloud L63, L95) | DROP as a rule | [H] (R7 §7.3) | GEN | |
| End on a comment-bait question (CS L28) | DROP | Contradicts all files | — | stale |
| 0.15-0.4 s tail; sound dies away (QA FAIL) | KEEP | #66's ringing boom (QA L197-L198) [V] | OURS | |

### N. Posting
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| NBA 11 AM (+6 PM), soccer 12 PM ET (US) | KEEP as a habit | "Timing matters little", except news (R6 §1) [S official quote] | OWNER | |
| Post 6-11 AM ET (nba L57) | DROP | Stale; R6 §9 "UNSUPPORTED" | COMP | |
| Never 3 a day (PB L43) | KEEP | Ahmed's medians fell at 3 a day (PB L42) [V COMP] | COMP | |
| One soccer Short a day (US L14) | KEEP | Credits (FCSH running costs); the S02 cause is n=1 [H] | OWNER | |
| 4 h between posts (US L16) | KEEP (harmless) | [H] | GEN | |
| Never re-upload the same file; make a new cut | KEEP | #25 re-upload 197 views (WMV §2) [V]; YouTube spam warning (MP §2) [V] | OURS, policy | |

### O. QA gates in `Tools/qa_short.py` (as the code runs today)
| Gate | Type | Verdict | Evidence |
|---|---|---|---|
| Voice starts by 0.4 s (L88) | FAIL | KEEP | Logic [H]; free |
| No filler first word (L89-L90) | FAIL | KEEP | [H]; free |
| Action footage in the first 3 s (L96) | FAIL | KEEP | Talking-head open (#15 v1) [S] |
| Hook has a name/number/stakes word (L117) | FAIL | KEEP (weak) | Passes nearly all (R7) |
| Shot too long: NBA 6 s, soccer 3.6 s; quotes 6 / 4.5 s (L118-L120) | FAIL | KEEP | WHY §2 [V]; Ahmed [V COMP] |
| ≤2 shots in 3 s (NBA) / ≤3 (soccer) (L92-L95) | warn | KEEP | WHY §2 [S] |
| Average shot (L122-L125) | warn | KEEP | WHY §2 [V] |
| ≤35% one clip, ≥6 clips (L130-L132) | NBA warn, soccer FAIL | Soccer: make it a warn | No evidence (R6 §9) [BAD INFO?] |
| Talking head ≤45%, b-roll ≥35% (L134-L135) | warn | KEEP | n=1 [S] |
| Any card (L139); two cards in a row (L143) | warn | KEEP | WHY §2 [V] |
| Card over 1.5 s (L141); card in the first 4 s (L232-L234) | FAIL | KEEP | Owner; WHY §2 [V] |
| Same footage twice (L148-L158) | warn | KEEP | [V] |
| Loop to the first clip (L159-L160) | warn | DROP or keep quiet | [H] |
| Dead air over 0.6 s (L161-L162) | FAIL | KEEP | Owner; RA14 [V] |
| Loudness -14 ±1.5 LUFS (L167) | FAIL | KEEP | Vendor figure, harmless (R6 §5) [S] |
| Frozen footage, black frames (L181, L183) | FAIL | KEEP | [V] |
| Frame 1 lit (L196) | FAIL | KEEP | S04 [V] |
| Sound died away at the end (L202) | FAIL | KEEP | #66 [V] |
| Quote shot at 1.0x (L223) | FAIL | KEEP | #38 [V] |
| Voice cut off (L235-L236) | FAIL | KEEP | [V] |
| Pace 200-265 wpm (L249) | warn | KEEP as a warn only | No link (WHY §2) [V] |
| Slow hook (first sentence after 3.5 s) (L258) | warn | KEEP | WHY §2 [V] |
| Naked-number opening (L265) | warn | KEEP | #20 [S] |
| Bed baked in (L272-L273) | warn | CHANGE: skip for soccer | — |
| Music licence; speech band under 12 dB (L278-L305) | FAIL | KEEP | [V] |
| `sources.csv` row and verified (L318-L320) | FAIL | KEEP | #39, #41 (RA14 B16) [V] |
| Length: NBA 12-60 s FAIL, 15-35 warn; soccer 50-59.9 FAIL (L81-L86) | FAIL | KEEP; consider NBA FAIL at 58 s | NNBA §5 cap 58 s |
| Soccer: promise back by 25 s; ≤10 names in 15 s (L97-L115) | warn | TEST | n=3 [S] |
| `--full`: captions = script, 45-62% band, 1080x1920, clipping (export_check) | FAIL | KEEP | ESS §6 [V] |
| `--full`: blow-up over 3x (soccer 6x), one-frame flash, same frames twice (footage_qc) | FAIL | KEEP | ESS §6 [V] |
| Docstring L8-L14 | — | REWRITE | Describes gates the code no longer runs |

### P. Process gates
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| Script Critic v3 APPROVE before footage or voice (PB L71; SH L14) | CHANGE to advisory; TEST | Never validated; #40/#41 REJECTs beat the median (section 2, item 14) [S] | OURS | [SLOWS] |
| Critic v2 on the export (PB L141) | KEEP for hand builds | Real defects in 3 of 3 builds (RA14 D3) [V] | OURS | costs an agent |
| Footage first (PB L146) | KEEP | #40, #41 defects (RA14 D2) [V] | OURS | |
| One A/B at a time; change at n≥3 (PB L161-L162) | KEEP | — | OURS | |
| A rule needs 3+ of our Shorts or strong outside data (AUD24 §3.4) | KEEP | The lesson of this review | OURS | |
| The dataset decides (daily L39-L41) | KEEP, and fill it | frame 1 0/120, folder 0/120 (DS, counted today) [V] | OURS | |
| `content-principles` skill applied to every script | KEEP as optional | Generic, third-party, business examples (Content Principles Evaluation) | GEN | |
| Two-takes voice gate (HNR, jitter, pitch) | KEEP | Voice audition [V] | OURS | |

### Q. Copyright and footage
| Rule (where) | Verdict | Evidence, tier | Origin | Flags |
|---|---|---|---|---|
| Under 60 s with broadcast footage; NBA cap 58 s | KEEP | MP §5 [V official, pages conflict]; NNBA §5 | policy | |
| League, team, broadcaster or archive.org footage only; no other creators' edits or watermarks (MP safeguard 4; BRG rule 7) | KEEP; fix cloud L34 and daily L57 | MP §3 [V official] | policy | |
| No agency photos (BRG rule 7; RA14 B17) | KEEP | #41 (LL Oct 14) [V] | OURS | |
| Every clip in `sources.csv`, verified by eye | KEEP | RA14 B16 [V] | OURS | some cost, protects |
| No AI footage of real players; label realistic AI (BRG rule 8; MP §6) | KEEP | [V official] | policy | |
| AI disclosure "No" for narrated real footage (MP safeguard 6) | KEEP | [V official] | policy | |
| No broadcast audio under narration (ESS §5) | KEEP | Claim risk (BRG §4) [S] | GEN | |
| "Short cuts ≤2-3 s each" (BRG L95) | CHANGE | Generic fair-use advice [H]; clashes with "let a play run" | GEN | [BAD INFO?] |
| Source 1080p+; blow-up over 3x FAILs (BRG rule 7) | KEEP | ESS §6 [S] | OURS | |

---

## What I could not check
- I didn't re-measure the shot and card counts behind WHY §2; the numbers above are as that note reports them. I did re-count the stayed % summary from DS.
- I couldn't see which version (music or not) any Short went up with. Nobody logged it.
- S03's stayed % after its day-2 breakout isn't in any export yet.
