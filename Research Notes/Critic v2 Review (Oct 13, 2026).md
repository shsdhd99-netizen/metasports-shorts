# Critic v2 Review (Oct 13, 2026): #40, #41, #32 A/B

Independent critic (built none of these). Rubric: `Tools/critic_v2.md`. **Checked:** every export (`watch_short.py` sheets, 10 fps opening frames, every card), a silence scan, `copy_check.py`, key facts on the web. **I can't hear audio:** the voice is judged from transcripts, `voice_check` and timing only. No export has a gap over 0.35 s or a silence over 0.4 s inside the speech.

| Short | Verdict | 3-pt formula (2nd-1 / measure / answer) | Gut rank |
|---|---|---|---|
| #40 Jokic pass | **NEEDS REVISION** | 3 (1/1/1) | 1 |
| #41 Taller than Wemby | **REJECT as cut → rewrite** opening frame + ending | 2 (1/1/0) | 2 |
| #32 Spurs 29 (A and B) | **REJECT, abandon** | 0 (0/0/0) | 3 |

---

## #40 Why Jokic's Best Pass Doesn't Count (21.6 s)

**Gate A**
1. **Second-1: PASS.** "Nikola Jokic's best pass ever doesn't even count." A non-fan asks: "Why doesn't his best pass count?"
2. **Visible object: PASS (weak).** Frame 1 is Jokic with the ball on the baseline. The release comes at about 1.4 s, and the cut to his face at 1.59 s lands mid-release, so the pass is never seen whole (Gate B).
3. **One measure: PASS.** Official assists: 6,080 → "should be 6,081" → "still 6,080".
4. **Not a retell: PASS (caveat).** `copy_check` FRESH, and no "doesn't count / 6,081" version found. But SB Nation (Oct 5) headlined "...and it's only preseason", and the clip itself is widely seen.
5. **Answering ending: PASS.** "Still reads six thousand and eighty" (17.9 s) answers with one number. The last line ("isn't in there") restates; it's tolerable as the loop.
6. **Truth: FAIL (wording).** The hook voices "best pass ever" as fact. Denver Post (Oct 12): "**Probably** was the best pass I ever passed **in my NBA career**." notes.md itself says to keep "probably". The rest is confirmed:
   - 6,080 regular-season assists in 810 games (StatMuse).
   - Said Sunday night, "a week after" the pass.
   - Preseason opener vs Utah at CU Events Center (Rotowire).
   - Corner to corner (HITC).

**Gate B**
- **Wrong picture under the pass words.** "NO LOOK. BEHIND THE BACK." (2.51-3.81 s, shot 3 `M_pass`, in 0.4) plays over **Cam Johnson catching and shooting**, not Jokic's pass. Johnson's shot then repeats from 3 angles in 3.5 s (2.5-6.06 s).
- **Caption chunk.** "EVER DOESN'T" (1.38-1.88 s) splits the hook phrase.
- **No college shown.** Shot 10 ("college gym in Boulder", 14.05-16.25 s) shows no college marking. BUFFALOES appears earlier, in shot 9.
- **Two cards back to back:** 7.82-11.28 s.
- **Listen check.** The small whisper model heard "6,0801" at about 13.2 s; voice_check heard "6,081". The owner should listen at 12.6-13.7 s.

**Gate C:** at 1.6 s I'm cut away before the ball leaves his hand, then I see one corner three three times. **I'd swipe at about 8-9 s** (the quote card): a restatement, and still no "why". Fans may guess "preseason" by 2 s. The payoff is modest but clean.

**Required edits**
1. **Hook (0-2.06 s):** re-voice with attribution, e.g. "Jokic calls this the best pass of his career. It doesn't even count." (`revoice.py`; the voice is provisional anyway).
2. **Shots 1-5:**
   - Run `R_close` through the release (to about 1.9 s).
   - Move shot 3's in-point earlier so "No look. Behind the back." sits on the release and the ball's flight.
   - Keep one angle of the make (`R_shot`).
3. **Captions:** "BEST PASS EVER" / "DOESN'T EVEN COUNT."
4. **Recommended:** a readable BUFFALOES frame under "college gym"; cut the quote card to about 1.2 s.

---

## #41 Is Anyone Taller Than Wemby (26.4 s)

**Gate A**
1. **Second-1: PASS (marginal).** "This man is listed taller than Victor Wembanyama" → "Who's taller than Wemby?" The paradox ("never played... that counts") lands at 2.2-4.0 s.
2. **Visible object: FAIL.**
   - In frame 1, Sharp is side-on with his face away, reaching **up** to kids on a raised rail. He reads as average height.
   - Wemby (1.17 s) is seated at a podium.
   - At 2.2-4.0 s Sharp is tiny in a wide shot.
   - The height first appears on the card at 4.04 s.
3. **One measure: PASS.** Minutes that count: 0/0/0, total 0. Hops: the height hook and DPOY (15.8-18.4 s).
4. **Not a retell: PASS (risk).** No "three cuts, zero minutes" version found. But the hook fact went viral in August: theScore "An inch taller than Wemby 🤯", NY Post, talkSPORT, Yahoo, TikTok.
5. **Answering ending: FAIL.** "Seven-foot-five. NBA minutes that count: still zero." restates line 2. "And it's not his defense" (14.76 s) opens a "then why?" that is never answered. The ending is a what's-next news status.
6. **Truth: PASS.**
   - Listed heights: Sharp 7-5 (B-Ref, NBA.com); Wemby 7-4 (B-Ref, NBA.com, Fox).
   - DPOY 2025-26 (TSN).
   - Clippers two-way, then waived in September.
   - Raptors Exhibit 10, official Mon Oct 12 (HoopsRumors).
   - Dallas waived him Oct 2024 and Oct 18 2025.
   - Risks: Wemby's listing has flipped before (7-5 on the NBA bio in Oct 2025, per SI), and "Seven-foot-five" is voiced bare at 4.0 and 23.3 s (measured 7'3¾").

**Gate B**
- **Doctored image.** `p_clip.png` (11.61-12.95 s, "the Clippers signed him") is a Bleacher Report edit: a **Texas Legends jersey with a Clippers logo pasted over "LEGENDS"**. PACKAGE.md calls it a Clippers jersey.
- **Caption on a face.** "THAN VICTOR WEMBANYAMA." sits on Wemby's chin and mic (1.2-2.1 s).
- **Cropped scorebugs.** Burned-in Summer League bugs with the left edge cut off at 2.2-4.0, 14.8-15.8 and 20.4-23.3 s.
- **Pace and length.** 224 wpm (house 247-289); "Twenty twenty-five: Dallas again" drags at 163 wpm (9 s); 26.4 s is over the formula's 20-24 s.
- **Two cards back to back:** 16.78-20.35 s.
- **Small mismatches:** "Last season" over a July 2026 photo; "they cut him [Clippers]" over a 2025 Dallas clip.
- **Name check.** Small-model STT heard "Wimbong Yama" at about 1.4 s; the owner should check the name.

**Gate C:** I'm promised "taller than Wemby", then see a tiny figure in a wide shot. At 5.6-11.6 s it's a transaction log. **I'd swipe at about 8 s**, on the first tally card. After 4 s I learn nothing new except DPOY.

**Required edits (rewrite)**
1. **Shot 1:** a frame with a height reference (Sharp beside teammates or a coach), or a "7'5" vs 7'4"" pill on frame 1.
2. **Lines at 14.76 s and 23.3-26.4 s:** give a sourced reason why teams cut him (ideally his own words), or delete "And it's not his defense". End on that answer.
3. **Shot 9:** a real Clippers image, or the ClippersPR transaction post.
4. **Shot 2:** caption below Wemby's chin.
5. **Script:** merge the Dallas beats ("Dallas cut him twice") to reach about 23 s.
6. **Before posting:** re-check his status; post by Oct 18 ("On Monday" goes stale).

---

## Pointer twins
- **#40:** the ring is on the right person and clean (thin, tracks through the zoom at about 0.75 s, clear of captions). But it circles his torso and head, not the ball: the ball is on the ring's edge at 0-0.3 s and outside it from 0.4 s. The ring vanishes at 1.1 s, before the release (1.3-1.5 s). From 0.8 s it is mostly crowd. **Fix:** ring the ball and hands from 0.9 to 1.6 s.
- **#41:** the ring and arrow track Sharp's head (the right person), but it is **red on the red Toyota banner**. In frame 1 and in `cover_B_pointer.png` it reads as circling the Toyota logo, and a head says nothing about height. **Fix:** a white or yellow ring on a frame with a height reference.
- Neither twin is clean enough to count as an experiment-1 pair yet.

---

## #32 Why Did The Spurs Lose A 29-Point Lead (A vs B)

**Gate A: REJECT, abandon**
1. **Second-1: FAIL.** The first 8 words state a lead; "And lost" comes at 2.4-3.0 s over a generic wide shot.
2. **Visible object: FAIL.** Both cuts open with a **0.0-0.2 s flash shot** (another camera, "LISA SALTERS" lower third). The bug reads "SA 81 NY" with the 52 cropped off.
3. **One measure: FAIL.** Six measures (29/27 lead, 14 threes, 3-for-17, the 24-since-1997 mark, 1.2 s, 107-106). This is #29's anti-pattern.
4. **Not a retell: FAIL.** notes.md concedes a 7.1M-view Short on this game, and `copy_check` finds Tylertsports. It is also a June recap.
5. **Answering ending: FAIL.** "The biggest comeback in Finals history" restates; the "why" (3-for-17) is buried at 9-11 s.
6. **Truth: FAIL.** "Led **the NBA Finals** by twenty-nine" is wrong: it was Game 4, and the bug on screen says "NY LEADS 2-1". The 14-threes record is unverified.

**A vs B (first 4 s): B is slightly better; neither should post.**
- **A, 1.52-2.37 s:** a grey AP card, headline cut off at the right edge, unreadable text, an **empty red box** at 1.9 s, and the lower 60% flat grey. This is the worst frame in either cut.
- **B** shows a face at 1.5 s instead. Its costs:
  - Our captions stack under the NBA's burned-in "IT JUST HURTS / WEMBY AFTER GAME 4 LOSS" for 1.2 s (A: 0.65 s).
  - That text gives away "loss" 0.9 s before "And lost".
  - "AND LOST." (2.72-3.02 s) sits over a Spurs possession with the bug reading SA 41-22.
- **Both** keep the 0.2 s flash and the cropped bug.
- **Testing the card idea:** one unposted Short can't test it publicly (re-posts die: #25 got 177 views). Test "no card before 7 s" on a fresh pair.

---

**Sources checked (Oct 13):**
- Jokic: Denver Post (Oct 12); StatMuse (https://www.statmuse.com/nba/ask/how-many-assists-does-nikola-jokic-have-in-his-career); CBS/Rotowire and SB Nation (Oct 5).
- Heights: B-Ref (Sharp; Wembanyama https://www.basketball-reference.com/players/w/wembavi01.html); NBA.com and Fox (Wemby 7'4"); SI (Oct 8 2025).
- Sharp: HoopsRumors and TSN (Oct 12); theScore, NY Post, AOL (Aug 2026).

---

## Re-check of v2 (Oct 13, late; second independent critic)

A second critic; I built neither Short. **Checked:** both exports (watch sheets, 10-30 fps frames), the pointer twin, `_audit` QA and voice_check, silence, `copy_check.py` (both FRESH), and the new facts online. **I can't hear audio**, so I judged the voice from transcripts and voice_check only.

| Short | Verdict | 3-pt formula (2nd-1 / measure / answer) | Gut rank |
|---|---|---|---|
| #40 Jokic pass (21.3 s) | **PASS** | 3 (1/1/1) | 1 |
| #41 Taller than Wemby (23.1 s) | **NEEDS REVISION** (one shot) | 3 (1/1/1), weak on measure | 2 |

### #40
- **Edit 1, hook: fixed** (0-4.7 s). It matches the Denver Post (Oct 12): "Probably was the best pass I ever passed in my NBA career," said Sunday night, a week after the pass.
- **Edit 2, shots: fixed.**
  - The ball leaves his hand at about 1.65 s; the cut is at 1.93 s.
  - "No look. Behind the back." sits on the slowed release (4.8-5.9 s).
  - The make is shown from one angle (6.83-8.23 s).
- **Edit 3, captions: fixed** (0-1.24 s).
- **Edit 4, recommended: done.** BUFFALOES is readable at 13.9 s, the quote card is gone, and there's no card before 8.2 s.
- **Gate A:** all pass.
- **Gate B:** none. QA PASS, no gaps inside the speech, end tail 0.58 s.
- **Gate C:** the swipe risk is the StatMuse card (8.2-10.8 s), where the "why" is still held back. The payoff is modest but clean.
- **Optional:** 2.7-4.7 s is a far wide shot where the pass is tiny.
- **Listen:** 11.6-12.9 s and 18.8-20.6 s. The small recogniser heard "6,0801" and dropped "Not", a 0.17 s word at 19.83 s. voice_check heard both right.

### #41
- **Edit 1, frame 1: partly fixed** (0-1.19 s). He's full length, and a guard walks in beside him by 0.6 s. But his back is to the camera and his head is bowed under the rail, so Gate A2 is a weak pass.
- **Edit 2, the "why": fixed.** It ends on "Sharp, in the G League: zero", and the 0 pops in on the word (21.8 s).
- **Edit 3, doctored image: removed**, but the replacement shot has a problem (see the new defect below).
- **Edit 4, caption: fixed.** It sits below Wemby's chin.
- **Edit 5, length: fixed.** 23.1 s.
- **Edit 6, status: re-checked Oct 14.** He's still on the Raptors Exhibit 10 deal (RealGM, Oct 13). Post by about Oct 18.
- **New facts: confirmed.**
  - Wembanyama: 350 three-point attempts, 2025-26 regular season (B-Ref).
  - Raptors HQ (Jul 4 2026): "zero attempts in the G League"; undrafted "due to his offensive limitations".
  - He led the G League with 3.9 blocks per game (Hoops Rumors, Sep 25).
- **NEW defect (wrong team on a spoken name), 8.41-9.76 s:**
  - "The Clippers signed him this summer" plays over Sharp in **Raptors red** (R_dunk2). Viewers saw "RAPTORS 33" at 2.4-5.5 s.
  - **Fix:** drop R_dunk2 and run H3 from 7.69 to 9.76 s. H3 is team-neutral and 2.2 s long.
  - **Or:** use the ClippersPR post here and swap c_tally3 for footage, so cards stay at 25% or less and never touch.
- **Gate A:** all pass. "One measure" is weak: from 12.5 s it shifts to skills (blocks, then threes). It answers the opening question, so it passes.
- **Gate C:** I'd swipe around 8.5-10.7 s, the run of transactions. "And it's not his defense" (12.5 s) pulls me back, and 350 vs 0 is a clear payoff.
- **Optional:** bring the 350 card in on "three" (19.79 s) to trim the 2.9 s slowed hold on Wemby, and label it "regular season". Expect "Gobert shoots zero threes too" comments.
- **Listen:** "Wembanyama" (1.2-2.3 s; 18.8-19.75 s, stretched to 0.93 s) and "Jamarion" (4.4 s).

### Pointer twin (#40)
It's usable. The ring holds the ball at 0.2-0.5 s and 1.3-1.4 s, and it ends at 1.5 s, about 0.15 s before the release. It's static, so at 1.0-1.1 s it sits on Markkanen's head. Count it as the ring half of experiment 1, and log it as "ring, no pill".

### Housekeeping
Both PACKAGE.md files cite a second check "at the end of this file"; it is this section. Hold #41's "ready" status until the 8.41 s fix.

### Applied after the re-check (Oct 14, main session)
- **#41:** the prescribed fix is done. R_dunk2 is dropped, and H3 (the team-neutral tunnel clip) runs 7.69-9.76 s. Re-rendered 23.0 s. `qa_short.py` PASS: cards 23%, b-roll 41%, no holds. Frames at 7.5-9.9 s were checked: no Raptors red under "The Clippers". The critic did not re-review the fix; it is the exact change this section asked for. Status: **ready** (owner listen + status re-check on posting day).
- **#40:** no change needed (PASS).
- **Optional items not taken:**
  - Bringing the 350 card in at "three" would push cards to about 25%, the QA limit.
  - "2025-26 season" already matches the source, so the card keeps that label.
  - #40's far wide shot at 2.7-4.7 s stays, because it keeps 3 cuts inside 3 s.

---

## Queue review (Oct 14): #39, #30, #21 (third independent critic)

I built none of these. **Checked:** each export (watch sheets, 10 fps frames for 0-4 s, extra frames around suspect shots), QA, voice_check (whisper), a replay scan, `copy_check.py`, and key facts online. **I can't hear audio;** the voice is judged from transcripts only. No speech gap is over 0.3 s; tails are 0.32-0.41 s. Shot numbers count from 1. #39 was posted before this review (hde8nIE1J4Y, about 2,100 views at 10:45 UTC Oct 14), so it is a post-mortem.

| Short | Verdict | 3-pt formula (2nd-1 / measure / answer) | Gut rank |
|---|---|---|---|
| #39 Oldest triple-double (22.7 s) | **Post-mortem (already posted)**; would have been NEEDS REVISION | 3 (1/1/1), 1 and 3 weak | 1 |
| #21 Jokic vs Westbrook (22.2 s) | **REJECT as cut → rewrite** | 1 (0/0/1) | 2 |
| #30 Giannis steps (24.3 s) | **REJECT, abandon this angle** | 2 (1/0/1) | 3 |

**Tool gap:** `qa_short.py` only catches identical *neighbouring* shots, so it missed three exact replays (one in #30, two in #21). It should flag any reuse of a clip with overlapping in-points, except the loop.

### #39 Oldest triple-double: post-mortem (already posted)

**Gate A**
1. **Second-1: PASS (weak).** "Who held the record 22 years, and who broke it?" A fact, not a paradox.
2. **Visible object: PASS (weak).** LeBron in the record game; his age first shows at 8.1 s.
3. **One measure: PASS.** Age at triple-double: 40y127d → 41y44d → 79d → 90d → 41y294d.
4. **Not a retell: PASS.** CROWDED with small news recaps; the "broke his own record" angle is FRESH.
5. **Answering ending: PASS (weak).** It answers line 1, but "any triple-double is the oldest ever" is true by definition.
6. **Truth: PASS.** B-Ref log (Feb 12 DAL, Mar 19 @MIA, Mar 30 WAS); ages re-computed; Sixers at Knicks Oct 20.

**Gate B, as lessons**
- **Wrong game under records 2 and 3.** 9.58-10.95 s "again in March" is the Feb 12 Dallas game. 10.95-12.35 s "record 2" shows a GSW scorebug (it was at Miami). 13.64-14.82 s "record 3" (vs Washington) is Dallas. notes.md flagged it; it shipped. **Lesson:** a stand-in shot must never show a scorebug naming another opponent.
- **2.61-6.43 s:** 3.8 s of a 320x240 Malone press conference with TV text under our caption, at the Duren cliff spot. **Lesson:** one 1 s archive shot, then move on.
- **16.11-18.0 s:** "at the Knicks" over playoff footage in Philadelphia, no LeBron; the Sixers move is never voiced.
- **9.61 s:** "He broke his own record again in March" at 360 wpm, with a -22 dB "He". **Lesson:** a >330 wpm note blocks "ready". (The 4.22 s REDO is a false positive.)

**Gate C:** I'd swipe at about 3 s, on the blurry press conference. The count-up at 8-15 s is clean.

**Process lesson:** run Critic v2 before posting day; #39 went up without it.

### #30 Giannis steps: REJECT, abandon this angle

**Gate A**
1. **Second-1: PASS.** "How are three steps legal?"
2. **Visible object: FAIL.** Frame 1 (0-0.99 s) is Giannis dribbling up court, with no gather. No shot shows his steps closely enough to count.
3. **One measure: FAIL.** 13.46-20.33 s (28%) hops to enforcement: a 2018 refs' post about another player, then the points of emphasis.
4. **Not a retell: FAIL.** TAKEN: Business Insider "NBA Ref Explains Why The James Harden Step Back Isn't Traveling" (1.43M), plus a 2.07M "0 step" explainer.
5. **Answering ending: PASS (weak).** "Gather, one, two" answers, after a "count it" instruction.
6. **Truth: PASS (wording).** "That landing foot is free" is loose. NBA.com (Oct 5) lists flopping first; the voice skips it.

**Gate B**
- **Exact replay:** 1.53-2.07 s replays at 10.80-11.33 s (shots 3 and 9, `b1`).
- **Source text and a spent shot:** 2.6-9.24 s (shots 5-7). 6.6 s of referees in a room, with the source's cut-off text under our captions.
- **Wrong picture:** 9.24-10.78 s (shot 8) "gather, step one, step two" over Giannis standing still. 12.45-13.46 s (shot 10) "a fourth is a travel" over James Harden.
- **Wrong team:** 21.97-24.33 s (shot 16) follows "drives in Miami" with a Bucks jersey, dribbling, not gathering.
- **Payoff early, cards unreadable:** `c1` boxes "traveling is still ok" at 16.0 s, before the 19.32 s line; its headline is cut off. `c2` (19.32 s) is small type, boxing the wrong words.

**Gate C:** I'd swipe at 3-4 s: "Here's why" leads to a conference room.

**Decision:** abandon. The story has 2M-view versions, and the footage can't prove the count. Revisit only with a new angle: one Heat-era Giannis play from opening week, counted on screen.

### #21 Jokic vs Westbrook: REJECT as cut → rewrite

**Gate A**
1. **Second-1: FAIL.** Line 1 asks "who passed Oscar?", answered by 5.4 s. The real question arrives at 6.9 s ("Eleven ties it").
2. **Visible object: FAIL.** Frame 1 is an old Oscar-Westbrook ceremony under a cut-off "HISTORY" graphic. 209, 198, 34 and 23 are never on screen.
3. **One measure: FAIL.** 14.46-19.03 s (21%) hops to a box-score record (56-16-15, "first 55-15-15").
4. **Not a retell: PASS (caveat).** CROWDED (Chaz NBA, Jokic-Westbrook clip, 168K). No "game 27" version found.
5. **Answering ending: PASS.** "Four games to spare" answers the title and stops.
6. **Truth: PASS.** B-Ref (Oct 14): 209 / 198 / 181; game 27 = Dec 25 at Golden State. Westbrook retired Aug 2026 (NBA.com). 34 in 65 (StatMuse). 12 ÷ (34/65) = 22.9.

**Gate B**
- **Two exact replays:** 9.20-10.03 s = 14.43-15.27 s (shots 12 and 17, `b8`). 13.03-14.40 s = 16.70-18.07 s (shots 16 and 19, `b11`).
- **Burned-in number vs voice:** "JOKIĆ 32 PTS" at 9.2-10.0 s and 14.46-14.95 s.
- **Wrong game:** 16.75-19.03 s (shots 19-20) "first 55-15-15 game" over a Phoenix-court game, then a Memphis player.
- **Flash and card:** a Knicks-bench flash at 2.20-2.45 s; shot 21 (19.03 s) is tiny rows over blurred grey.

**Gate C:** I'd swipe at 2-3 s, on trivia over an old ceremony. "Eleven ties it. Twelve breaks it." is the real hook.

**Required edits**
1. **Hook, 0-6.9 s (shots 1-8):** re-voice line 1 as the chase, e.g. "Westbrook retired with 209 triple-doubles. Jokic has 198." Frame 1: Jokic with a "198 / 209" pill, no "HISTORY" graphic.
2. **Cut "the first fifty-five, fifteen, fifteen game in NBA history" (16.75-19.03 s, shots 19-20).** Keep the bridge on the measure: "Last Christmas: a triple-double, 56-16-15", over `b9` only.
3. **Shot 17 (14.46 s):** unused Christmas footage instead of `b8`. **Shot 12 (9.21 s):** crop or swap so "32 PTS" is gone.
4. **Shot 21 (19.03 s):** one readable line above the captions: "Game 27 · Dec 25 · @ Golden State".
5. **Shot 22 (20.92 s):** land "Four games to spare" on Jokic or the card.
6. **Shot 2:** trim before 2.20 s. **Shot 9 (6.91 s):** use a Jokic shot.
7. Keep 21 s or more. Re-run QA and a replay scan.
8. **Post before Oct 22** (Nuggets at OKC). After that, 198 and the game count move. The queue's "before Christmas" deadline is wrong.

**Sources (Oct 14):** B-Ref (career leaders, LeBron log, DEN schedule); NBA.com (Westbrook; points of emphasis); StatMuse; Denver Post; NBC Sports Philadelphia; SI (Giannis on the Heat).

### Re-check of #21 v3 (Oct 14; fourth independent critic)

**Verdict: NEEDS REVISION (re-cut only, no re-voice). Formula 3 (1/1/1); second-1 is weak.** Gut rank: first of the unposted Oct 14 queue.

**Checked:** final.mp4 (16.9 s, same file as "READY TO POST"); the watch sheet and whisper; 10 fps frames over the whole cut; 30 fps frames at every cut; qa_short (PASS). **I can't hear audio.** The facts match B-Ref and the new notes.md rows: 209 in 1,301; 198 in 810; 34 in 65; game 27 = Dec 25 at GSW. At 16.9 s the story is complete (A8).

**Gate A:** all pass. Second-1 (weak): the chase is clear at 3.4 s ("the record: 209"). Object (weak): frame 1 is Jokic; 198 shows only as a caption. One measure throughout. The ending ("Four games to spare.") answers and stops.

**The six edits**
1. Hook: **mostly fixed.** It is re-voiced, frame 1 is Jokic and the HISTORY graphic is gone. There is no 198/209 pill (B12 is an owner TEST).
2. 55-15-15 line: **fixed** (cut).
3. Replays and "32 PTS": **fixed.** No scorebug anywhere; only the b1c loop repeats.
4. Card: **fixed.** 13.48-15.52 s, "GAME 27 / FRI, DEC 25 · AT GOLDEN STATE", readable.
5. Payoff: **fixed.** Jokic close-up from 15.52 s.
6. Flashes and shot 9: **partly.** The Knicks flash is gone and 7.04 s is Jokic, but there are two new flashes (below).

**Required fixes**
- **4.70-5.32 s (b13):** "Twelve breaks it" lands on Memphis #24. Jokic is half off the edge, and the caption sits on #24's face. End b13 at 4.70 s and fill the gap with unused **b4** (Jokic close-up, from about 0.2 s).
- **2.87 s:** a one-frame flash of a hoop and a Santa-hat crowd (a3's first frame). Set shot 3's `in` to 0.04.
- **7.03 s:** a one-frame flash of Westbrook in a Rockets #0 jersey (a1's own cut at 1.70 s). Start shot 6 at 7.00 s.
- **1.20-1.45 s:** "HAS 198" sits on Jokic's mouth. Lower shot 1's caption band to about 68%.

**Optional:**
- 1.60-1.99 s: a referee's torso fills the frame.
- 9.6-10.0 s: the shot pans to the floor.
- A source-text sliver on the bottom edge (4.0-5.3 s and 10.0-11.7 s); crop 2%.
- UPLOAD.md: drop the Oscar tag and trim to 12 tags (D8).

**Voice (transcripts only):** The words match the script. Whisper heard "1300 in 1" at 5.9-6.7 s. The pace is 224 wpm, and the first line is 152 wpm. The owner should listen to 0-2 s and 5.3-8.5 s.

**Gate C:** I'd swipe at about 6 s. The wrong player shows on "Twelve breaks it", then the slowest line (142 wpm) runs over a washed-out tribute shot. From 8.5 s, "34 in 65" leading to Christmas holds. A date plus "four to spare" is worth 17 s.

### Applied after the #21 re-check (Oct 14, v3.1)
All four required fixes, re-cut only (same voice). QA PASS, 16.8 s. Each fix was checked on the export at 30 fps (frame strips around every changed cut):
- **"Twelve breaks it" now on Jokic:** b13 ends at 4.67 s; the new shot b4c (Jokic close-up, `in` 0.2) runs to 5.30 s.
- **2.87 s flash:** a3 `in` 0.04. Frames 2.70-3.00 are clean.
- **7.03 s Rockets flash:** b2 starts at 7.00 s. Frames 6.83-7.16 are clean (a1 ends on Westbrook in a Wizards jersey).
- **"HAS 198" on his mouth:** `captions.py` gained a per-shot `cap_y`. Shots 1 and 12 use 1305 px (68%); at 1.30 s the caption sits below the mouth.
- **Optional, done:** b4/b13/b5 cropped 3% at the bottom (source-text sliver); tags cut to 12 and the Oscar tag dropped.
- **Optional, not done:** the referee torso at 1.60-1.99 s and the pan to the floor at 9.6-10.0 s (no better unused Jokic footage of those lengths in the folder).
- **Owner's ear:** "Westbrook needed 1,301 games" reads at 142 wpm, the slowest line (the critic's swipe point was about 6 s). A re-voice of that line is the next fix if it drags on a phone.

**Status:** ready (fixes applied; no fifth critic pass, as with #41's one fix).

### #38 What Did LeBron Promise Sixers Fans (Oct 14, music version; fifth independent critic)

**Verdict: REJECT as cut. Abandon this angle. Don't post it Sat Oct 17; use #36 if you clear its clip.** Formula 2 (1/0/1). Gut rank: last of the ready queue (#40, #41, #21 and #36 are ahead). I'd expect #18's band (2-3K).

I built none of this. **What I checked:**
- `final_music.mp4` (24.0 s; it has the same picture as `final.mp4`)
- the watch sheet, plus whisper (small model) run on the export
- frames: 10 fps for 0-4 s; 30 fps at all 19 cuts; every frame from 11.4 to 13.2 s; full-size frames under every name
- the quote shot frame-matched against `clips/lebron_full.mp4`
- the music isolated by subtracting `final.mp4`, and loudness per phrase
- qa_short (PASS), voice_check (REDO, a false alarm on LeBron's own audio), copy_check
- B-Ref and the Sep 28 coverage

**I can't hear audio.** The voice and music are judged from transcripts, levels and timing.

**Gate A**
1. **Second-1: PASS (weak).** Frame 1 is LeBron in a Sixers #23 jersey, and line 1 is "Philly hasn't reached a conference final since 2001." A viewer would ask: "Can LeBron end that?" The real question (what did he promise?) isn't asked until 17.3 s.
2. **Visible object: PASS.** LeBron in Philly blue is the surprise picture.
3. **One measure: FAIL.**
   - The measure is round two: 2001 → 8 exits → swept → "second round".
   - At 12.21-17.24 s the story hops to Embiid's missed games and then to the 1983 title. That's 5.0 s of 19.9 s of narration (25%; #21 failed at 21%).
   - The title line also makes "round two" sound small just before the payoff.
4. **Not a retell: FAIL (CROWDED, likely TAKEN).**
   - The quote led the Sep 28 stories from AP, CNN, NBA.com, CBS, NBC Sports, PhillyVoice and Yahoo.
   - AP already pairs it with our framing: "failed to advance out of the second round ... since 2001", and a title drought going back "to 1983".
   - B/R's media-day Short has 513K views (from our idea bank; I couldn't watch it).
   - Our own #18 (2.8K) used the same quote and the same footage.
   - By Oct 17 the quote is 19 days old. copy_check says CROWDED for the quote.
   - What we add (8 exits, "LeBron was 16", the 39) is small.
5. **Answering ending: PASS (the strongest part).** LeBron's own words about "the second round" answer line 1, and the video stops 0.38 s after "sure".
6. **Truth: PASS.**
   - B-Ref: 2000-01 "Lost Finals", and no conference final since.
   - B-Ref, 2026 East semis: PHI 0-4 NYK. Game 1 was May 4, 137-98 (39 points).
   - NBA.com/AP (Sep 28): the title drought goes back to 1983; LeBron, 41, signed a two-year deal.
   - The quote's wording matches CBS, NBC Sports and PhillyVoice.
   - Not re-checked: Embiid's 42% (NBA.com, per notes.md).
   - "Promise" is fair: AP calls it "one vow".

**Gate B (defects)**
- **Lip sync drifts in the payoff (20.21-23.97 s).**
  - `Qquote.mp4` is 3.4 s long, so assemble slowed the picture by 1.094x. LeBron's audio still runs at 1.0x.
  - Matched frame by frame against the source: in sync at 20.4 s. After that his lips trail his voice by 0.09 s at 21.2 s, 0.16 s at 22.0 s and 0.26-0.29 s at 23.2-23.8 s ("I know that for sure").
  - That is visible on a close-up face.
- **0.8 s of dead air before the payoff (19.8-20.6 s).**
  - The quote's audio starts at source 19.2 s, but the source is only room tone until 19.55 s. The "I" at 19.24 s in notes.md isn't audible: it's -47 dBFS in the export.
  - The quote's timings in words.json are made up (exactly 0.21 s per word), so qa_short measured only a 0.32 s gap.
  - "I DIDN'T" shows over the silence.
- **The wrong person under "Embiid" (12.21-12.70 s).**
  - Shot `G1b2` opens with a 2-frame flash of the wide shot (12.18-12.25 s).
  - Then a close-up of **Jalen Brunson** (Knicks #11) sits under "EMBIID HAS MISSED".
  - Embiid's back first shows at 12.70 s.
- **A flash at 6.70-6.77 s:** 3 frames of an internal cut inside `K1` (a court shot after the Knicks fan) before `K2`.
- **Two cards back to back inside the first 4 s (1.66-3.74 s):** "2001", then "16".
  - This breaks the "never two in a row" rule and the running "no card before 4 s" test that every build is meant to follow.
  - A third card follows at 4.40 s.
- **A number that never appears (13.06-14.71 s):** "more than half their games the last three years" plays over a wide Knicks possession at MSG (Brunson). Embiid isn't in it, and 42% is never shown.
- **The last words fade (from 21.7 s):** "in the second round" is -18.0 LUFS and "I know that for sure" is -22.1 LUFS. The narration is about -15, so the final sentence is 7 LU quieter.

**Required fixes, only if you post it anyway (a re-cut; no new narration)**
1. **20.21 s, lip sync and dead air:**
   - Take the quote audio from source 19.45 s instead of 19.2 s.
   - Re-cut `Qquote` from `lebron_full.mp4` at 19.42-23.30 s so it plays at 1.0x. The picture's source time must equal the audio's.
   - Swap the quote's made-up word times for whisper's real ones (for example, "didn't" at 19.64 s in the source).
   - The gap after "lose in." should come out at about 0.5 s.
   - Then frame-match the export again: the drift should be under 1 frame.
2. **Cut 12.21-17.27 s** ("Embiid has missed ... nineteen eighty-three.").
   - Both edges are clean sentence ends: "Maxey." ends at 12.18 s and "At media day" starts at 17.27 s.
   - It fixes the extra topics, Brunson under "Embiid", the 2-frame flash, the MSG wide shot, the mascot shot and one card.
   - New length: about 18.7 s.
   - If you keep the Embiid line instead, set `G1b2` `in` to 0.5. Embiid's 21 then shows from the first frame, and the 0.9 s left covers the 0.88 s shot.
3. **6.69 s:** start `K2` at 6.69 s (or end `K1` at 0.92 s into the clip) to remove the 3-frame flash.
4. **0.85-3.74 s, no cards before 4 s:**
   - Let the 2001 Finals footage of Iverson run through "two thousand one", with a small "2001 FINALS" label. `V02_ai` is 1.6 s; add the unused `V01_ai` (an Iverson jumper) if it runs short.
   - Under "LeBron James was sixteen" (2.48-3.74 s), use teenage LeBron footage labelled with its year. Failing that, use the unused media-day `L1` with "16 IN 2001", so the age jump is on his own face.
   - The "8" card at 4.40 s then becomes the first card.
5. **The quote's level:** +4 dB from "in the second round" and +7 dB from "I know that for sure" (or a 3:1 compressor on the quote clip), with true peak at or below -1 dBTP. Then re-run qa_short.

**Optional**
- **Frame 1:** it pushes in 10% over 0.85 s (`zoom` 0.1). The house limit is 6%, and LeBron isn't small, so use 0.05.
- **One press-conference camera angle fills 37% of the video** (0-0.85, 9.50-10.82 and 17.24-23.97 s), with jump cuts in the same framing at 18.50 and 20.21 s.
  - Under "Then LeBron signed at forty-one", use LeBron in uniform from the Oct 3 scrimmage post, if he's in it.
- **Scorebugs as proof (section 10):**
  - `K1`'s bug reads "EAST SEMIS · NY LEADS 3-0" at 5.77-6.69 s, which is under "The last was this May". Put it under "swept" and circle it.
  - `G1d` (7.74 s) crops the Game 1 bug to "57 NYK". Show "EAST SEMIS - GAME 1".
- `L5` (18.50-20.21 s) plays at 0.82x speed. Check that it doesn't look floaty.
- UPLOAD.md has 21 tags; the house target is about 12.
- **An unused fact:** the Knicks went on to win the 2026 title (B-Ref), so Philly was swept by the champions.

**Music** (from music.json and the render log)
- **The move is right.**
  - The bed sits about 21 LU under the voice (speech-band margin 43 dB) and is gone by 20.0 s.
  - The mix is below -40 dBFS from about 19.85 s, and LeBron plays dry.
  - That's the old "Bronny... son." cut, and it suits a real-voice ending.
- **The mood is the open question.**
  - The track was generated as a "nostalgic and hopeful ... sports tribute" piano.
  - Under 4-17 s (the sweep, a 39-point blowout, Embiid, 1983) it may sound like a tribute rather than pressure.
  - For stakes building to a vow, I'd try `eleven_suspense_01` ("Dark build"). It builds under the losses, and stopping it before the vow gives a bigger contrast.
  - Keep the piano only if your ear hears heartbreak, not a tribute. Neither track is approved by ear yet.
- **After the cut and trim:** set `out` at the end of "lose in." with a fade of 0.15 s or less, so the silence before the quote stays at about 0.5 s.

**Voice** (transcripts only)
- The narration runs at 238 wpm, and every name and number is heard right ("Maxie" is just a spelling).
- voice_check's REDO is on LeBron's own audio. Whisper hears it right when the quote is run alone, and as "I don't need my family" in the full pass.
- **Owner:** listen at 20.2-21.0 s.

**Gate C (viewer):** I'd swipe at about 4.5 s.
- After LeBron in frame 1, I get Iverson, then three number cards in under 3 s. The story is a list of Sixers losses, with no reason to stay except "he was 16".
- Anyone who followed media day, or saw our #18, already knows the ending.
- The second risk is at 12-17 s: Brunson under "Embiid", and a mascot under "title".
- The last 3.7 s (LeBron's voice, dry, after the music stops) is the best moment. But it is September's most-quoted line, and it arrives after 0.8 s of silence.

**The only fresh peg left:** on Tue Oct 20, LeBron makes his Sixers debut at MSG against the champion Knicks. They swept Philly in May and raise their banner that night (NBA.com and AP, Aug 11-14).
- Line 1 would be that matchup, and the payoff the same quote.
- It must go up by Oct 19, it clashes with the #10 banner-night idea, and it's a "tonight"-style news frame (the audit's warning).
- I'd skip it unless #10 isn't being built.

**Tool gaps (qa_short PASSed all of this):**
- A `quote` shot fit as "slowed" should FAIL: its audio is real speech, so any factor other than 1.0 breaks lip sync.
- Quote word times should come from speech recognition, not even spacing; otherwise the dead-air check runs on made-up times.
- A wrong face under a spoken name inside a clip isn't caught. sources.csv said `G1b2` shows Brunson and Embiid, but not when.
- **Housekeeping:** my voice_check run wrote `voice_check.json` into the folder. I deleted it, because it wasn't there before.
