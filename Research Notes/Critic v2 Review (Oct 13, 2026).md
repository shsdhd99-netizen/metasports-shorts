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
