# Critique Round 3B - Shorts 21 19 20 26 27 (Oct 5, 2026)
Critic: strict, hostile-but-fair. Judged against the VIRAL FORMULA in `critic3_common.txt`. No production file was changed.

## 0. Method and honest limits
- Used only the precomputed audit files (watch/report.md, sheet.jpg, voice_check.json, voice_quality, words.json, shots.json, notes.md, UPLOAD.md) plus Audit Summary and Voice Investigation. I looked at every sheet.jpg (#21 also storyboard.jpg). I cannot hear audio. Voice verdicts come from the recogniser diff and acoustic numbers only.
- The watch reports for all five say "speech-to-text unavailable", so the "heard" text comes from voice_check.json (it covers the final audio).
- Premise facts are taken from each notes.md / UPLOAD.md (primary sources named there). I did NOT re-verify them on the web this round. Anything I could not check is labelled UNVERIFIED.
- #21 was re-voiced on Oct 5 (22.2 s, 242 wpm, HNR 8.3). All other narration will be re-recorded, so the voice verdicts list only wrong words, bad joins and level problems.
- Not repeated from Round 2: #21 "end on game 27" (done), #20 "honest reframe" (done), #19 "ends on a question" (now ends on a quote, see below).

## 1. Verdict table
| # | Short | Verdict | Biggest reason |
|---|---|---|---|
| 27 | Back-to-back lotteries | FIX | Best hook/turn of the five (turn at 2.1 s), but the closing Wizards claim is the producer's own reading of the rule, stated as fact; cards are 23% of runtime |
| 21 | Jokic vs Westbrook | FIX | Clean payoff (game 27, four to spare) but ~15 spoken numbers and none shown on screen; avg shot 0.92 s; two repeated clips |
| 20 | Bad Boys defense | FIX | Strongest payoff (104.5 vs 104.9) buried behind a 6 s off-topic rule/quote detour; true turn lands at 14.4 s (56%) |
| 26 | Screens | REWRITE | Duren-cliff structure: the first real reversal (Stewart, "play on") lands at 19.2 s; 14 s of "Foul. Foul. Foul." |
| 19 | Flagg height | REWRITE | Hearsay hook, two script facts with no source on record, quotes played in the reverse of their real order, payoff restates 6-10 |

---
## 2. Short #21 How Close Is Jokic To Westbrook's Record (22.2 s, 88 words, 242 wpm, 24 shots, avg 0.92 s)

### Scorecard
| # | Item | Score | Evidence |
|---|---|---|---|
| 1 | Hook | WEAK | Voice at 0.00 s. First 8 words "Only two players ever passed Oscar Robertson's triple-double record" are a record recap, not a conflict. First frame = Oscar Robertson with mic and Westbrook (head cropped at top) at a ceremony, a "HISTORY" logo on top; 4 cuts in 3 s |
| 2 | Turn | WEAK | "But Jokic had thirty-four..." at 8.30 s (target 6-8; Duren cliff 8-10 s). It is a pace pivot, not a reversal. The 8 s before it carry 7 facts, so no flat stretch |
| 3 | Escalation | PASS | 198 -> 11/12 -> 34 in 65 -> 23 games -> game 27 -> four to spare. Longest zero-new-fact stretch 1.3 s ("That's about one every two games", 11.15-12.39) |
| 4 | Payoff | PASS | Hook/title promise = how close. Last 5 s: "This Christmas is game twenty-seven, in Golden State. Four games to spare." Ends on it, no question. (It is a projection, see C5.) |
| 5 | Loop | WEAK | Visual loop only (Oscar+Westbrook shot returns 20.9-22.2). "Four games to spare." does not flow into "Only two players ever passed" |
| 6 | Proof/footage | WEAK | 209, 198, 11/12, 34, 65, 23, 56-16-15, 55-15-15, 27 never shown as numbers (caption words only; schedule card 19.0-20.9 is tiny). Repeats: b8 (9.2 and 14.5), b11 (13.0 and 16.75-19.0). "Eleven ties it" (6.9-7.6) is a Grizzlies #7. "JOKIC 32 PTS" graphic under "fifty-six" (14.5). Cards 1.9 s = 8.6% (fine). Premise sourced to B-Ref/NBA on Oct 5 |
| 7 | Pace/edit | WEAK | 22.2 s, 242 wpm fine; avg shot 0.92 s (target 1.7-2.6), 4 cuts in 3 s; "HISTORY" logo clutter on the first and last shot |
| 8 | Voice | PASS (VOICE-OK) | New pipeline, HNR 8.3, all 8 mismatches are digits vs words; no real-quote bursts, so no level mismatch |
| 9 | Packaging | PASS | Title "How Close Is Jokic To Westbrook's Record? 🤯" 7 words; tags 444 chars; pinned comment = the debate; record-oddity lane = this audience's winner |

### Criticisms
**C1 CLAIM:** The Short is arithmetic and shows none of it.
EVIDENCE: Spoken numbers at 4.3, 6.3, 7-8, 8.9-10.8, 13.7, 15.4-18.2, 19.8 s. Sheet frames 4-18 s are footage plus caption words only. The one visible figure under "fifty-six" is a broadcast "JOKIC 32 PTS" graphic (14.5-15.0), which contradicts the spoken 56.
WHY IT MATTERS: The viewer must hold 209/198/12/34/65/23/27 with no visual anchor; the 11-14 s math chain is the likeliest swipe spot.
WHAT WOULD PROVE ME WRONG: Retention curve flat through 8-15 s.
PROPOSED FIX: statcard overlays (visual_fx statcard) for "209 vs 198" (5.0-6.9 s), "34 in 65" (9.2-11.1 s), and the real "56 PTS 16 REB 15 AST" graphic clip (NBA post 2004448562327765394) under "fifty-six".
CONFIDENCE: high.
COUNTER-ARGUMENT: CoachClank wins with no cards. But those are stories; this is a calculation.

**C2 CLAIM:** The hook states a record, not a stake, and the "But" arrives at 8.3 s.
EVIDENCE: words.json: "But" 8.30; "Eleven ties it. Twelve breaks it." 6.94-8.28 restates what 5.4-6.9 already said.
WHY: Duren's cliff was where a hook ended and set-up started (8-10 s).
WRONG IF: the 8-10 s retention is level.
FIX: lead with the stake ("Jokic is twelve triple-doubles from the NBA record"), drop "Only two players ever passed Oscar" and "Eleven ties it", move "But" to about 5.8 s (tight script below).
CONFIDENCE: medium.
COUNTER: Oscar + Westbrook is a clean face shot and the Round 2 fix; the first 8 s are fact-dense.

**C3 CLAIM:** Repeated and unidentifiable footage.
EVIDENCE: shots.json: b8 at 9.21 and 14.46, b11 at 13.03 and 16.75 (storyboard shows the same purple-court wide shot, no readable player, 2.3 s at 16.75-19.03 under "the first fifty-five, fifteen, fifteen game"). "Eleven ties it" shows a Grizzlies player with Jokic only at the frame edge.
WHY: "no repeated shot"; the Christmas line is not shown on the Christmas game.
WRONG IF: the in-points differ (shots.json lacks an in-point field; the storyboard looks identical).
FIX: use the NBA Christmas recap (2004447226358313094) for 14.4-19.0, and a Jokic shot at 6.9.
CONFIDENCE: medium-high.

**C4 CLAIM:** The "first 55-15-15 game" digression costs 4.6 s (14.4-19.0, 21% of the runtime) and delays the payoff.
EVIDENCE: words 14.49-19.03. WHY: it is not needed for the pace math; it only sets up "Christmas". WRONG IF: the Christmas curiosity is what keeps viewers.
FIX: keep it short (one clause) and show the 56-16-15 graphic. CONFIDENCE: low-medium. COUNTER: it is the most striking verified fact in the Short.

**C5 CLAIM:** "Four games to spare" overstates a projection.
EVIDENCE: notes.md: assumes he plays every game; he missed 17 last season (not in the script). Counting is ambiguous (Christmas game included or not).
FIX: "If he plays them all" (in tight script). CONFIDENCE: low. COUNTER: pace math is labelled "at that pace".

### Drop-off prediction
- 1.1-2.2 s: first cut, a Westbrook scream, the viewer has not yet heard a stake.
- 11-14.4 s: the math chain (34/65, "one every two games", "at that pace, twelve, twenty-three") with only wide footage.

### Voice
VOICE-OK. Take 3 passed after two REDO takes (rejected for "198" and "65" format and a stray "the next" at 21.1 s). Nothing garbled in the final.

### Verdict: FIX
Exact edits: (1) replace the hook sentence and cut "Only two...Oscar" and "Eleven ties it" (see tight script); (2) statcards at 5.0, 9.2; (3) swap b8/b11 repeats for the Christmas recap clip; (4) swap the Grizzlies shot at 6.9; (5) zoom 1.12 on the Oscar shot to push the "HISTORY" logo off, hold the opener 2.2 s (2 cuts, not 4); (6) enlarge the schedule card to only the Dec 25 row; (7) re-voice (about 560 characters).

### Tightened script (88 words, about 19.6 s at 270 wpm; hook 8 words; "But" at about 5.8 s)
Jokic is twelve triple-doubles from the NBA record. Russell Westbrook, who just retired, finished with two hundred nine. Jokic is at one ninety-eight. But last season he had thirty-four triple-doubles in just sixty-five games, even after missing seventeen. That's one every two games. At that pace, twelve takes about twenty-three games. Last Christmas night he went for fifty-six, sixteen and fifteen, the first fifty-five, fifteen, fifteen game in NBA history. This Christmas is game twenty-seven, in Golden State. If he plays them all, that's four games to spare.

Cut/merge list: cut "Only two players ever passed Oscar Robertson's record"; merge "One just retired" into the Westbrook sentence; cut "Eleven ties it. Twelve breaks it." (the hook already says twelve); fold "in just sixty-five games" + "even after missing seventeen"; add "If he plays them all". 88 words is 7 under the 95 target: add "Oscar Robertson's one eighty-one is third." (B-Ref per notes) after the Jokic 198 line only if a 7 s turn is acceptable.

---
## 3. Short #19 How Tall Is Cooper Flagg Really (21.9 s, 87 words, 247 wpm, 19 shots, avg 1.15 s)
(A premise-line version, final_premise.mp4, exists: small top pill "Flagg: 6-8 to 6-11?" for the whole video. It is a good fix for the flat opening because it puts the number conflict on screen at 0 s, but it cannot repair the spoken hook, the quote order or the payoff. If the hook below is adopted, the pill becomes redundant. Test the pill on the rewritten cut, not this one.)

### Scorecard
| # | Item | Score | Evidence |
|---|---|---|---|
| 1 | Hook | WEAK | Voice 0.00 s. "An Instagram account said Cooper Flagg grew two inches this summer" = hearsay opener with no number conflict; first frame = Flagg at the photo shoot, face visible but static |
| 2 | Turn | WEAK | First hedge at 5.4 s (quote "maybe I'm 6-11. I don't know"), true turn "Not so fast" at 8.6 s |
| 3 | Escalation | WEAK | Numbers oscillate (6-11, 6-10, 6-9, 6-10.5, 6-11?, 6-10), they do not climb. Longest no-new-fact stretch: last 1.8 s (the final quote restates 6-10) |
| 4 | Payoff | FAIL | Hook promise "how tall really". Last 5 s: "So is he six-eleven? Flagg's answer. not very accurate. I'm 6-10." = restates 6-10 already heard at 11.7 and 16.9; the Townsend "6-10 but not 6-11" fact (UPLOAD.md) is unused |
| 5 | Loop | WEAK | Last words (a quote) do not flow into "An Instagram account said"; visual loop to P1 only |
| 6 | Proof/footage | FAIL | (a) "Instagram account...two inches" and "five days later...six-ten and a half, with shoes" have NO source in notes.md/UPLOAD.md (notes still describe the v1 script). (b) Quotes appear in the reverse of their source order. (c) "NBA's website still lists him at six-nine": notes say 2026-27 listing not checked. (d) Same footage repeats (P1, W1, G3; the gym pull-up-bar clip at 2.5, 5.0, 10.0, 19.0 s) |
| 7 | Pace/edit | WEAK | 21.9 s, 247 wpm fine; avg shot 1.15 s, 3 cuts in 3 s; cards 2.1 s (9.6%) fine |
| 8 | Voice | WEAK (VOICE-REDO) | Pieces HNR 7.7 and 6.6 (11.5 s piece is the worst); quote words at 6.85-7.65 s are -14 to -26 dB ("I don't know" nearly inaudible vs narration); "and a half" heard as "5" (check "ten and a half"); script typo "Flagg's answer. not very accurate." |
| 9 | Packaging | PASS | "How Tall Is Cooper Flagg Really 😳" 6 words; tags 477; pinned comment is the debate; Flagg is a top name |

### Criticisms
**C1 CLAIM:** The two quotes are played in the reverse of their real order, so "Flagg's answer" is presented out of context.
EVIDENCE: plan.json: "maybe I'm 6-11. I don't know" is cut from 18.0-20.6 s of the source; "not very accurate. I'm 6-10" from 5.55-7.4 s. Larry Brown (cited in notes): "I'm 6-10 with no shoes ... maybe I'm 6-11". The Short plays 6-11 first and then labels 6-10 "Flagg's answer".
WHY: it invents a Q&A sequence (the 6-10 line answered the reporter's 6-11 question first); a quote-context error is the classic comment-section attack.
WRONG IF: the source video really has the 6-11 line before the 6-10 line (I only have offsets, not audio).
FIX: play them in source order, or only use "not very accurate. I'm 6-10" as the answer.
CONFIDENCE: medium.
COUNTER: both lines are genuine Flagg words from the same press conference.

**C2 CLAIM:** Two script facts have no recorded source.
EVIDENCE: the hook "an Instagram account said...grew two inches" and "Then five days later, he claimed another quarter inch: six-ten and a half, with shoes" appear nowhere in notes.md or UPLOAD.md. Audio notes call the 5 days / 10.5 line the one the recogniser heard as "5".
WHY: Round 2 lesson 1 (4 of 14 hooks were false/stale). WRONG IF: a dated source exists (add it to notes.md). FIX: cut both or source them. CONFIDENCE: high that they are unrecorded; UNVERIFIED whether true.

**C3 CLAIM:** The hook is hearsay and the payoff is a restatement.
EVIDENCE: 0-3 s "An Instagram account said"; 19.8-21.6 s "I'm 6-10" after 6-10 was said at 11.7 and 16.9 s.
WHY: no tension up front, no reveal at the end. WRONG IF: viewers stay for the quotes. FIX: lead with the four heights; end on the sourced confirmation ("six-ten, but not six-eleven"). CONFIDENCE: high.

**C4 CLAIM:** Footage and levels. Six source clips carry 22 s; the quote's tail is far below narration level.
EVIDENCE: voice_check notes (quiet words -14 to -26 dB at 6.85-7.65 s); sheet repeats. FIX: level the quote bursts (visual_fx level) and vary footage (Summer League slam, warm-up and 49-point clips are in the notes). CONFIDENCE: medium.

### Drop-off prediction
- 0-3 s: hearsay opener ("An Instagram account said").
- 12.9-15.0 s: 2.1 s NBA-site stat card plus "still lists him at six-nine", flat.

### Voice: VOICE-REDO
Spots: 5.5 s and 8.1 s real-quote bursts read as "(nothing)" (noisy source, judged audibly risky); 6.85-7.65 s quote tail -14 to -26 dB; 17.2 s "and a half" heard "5"; "Marc" heard "Mark" (fine). Merge: the two narration pieces (#0 5.3 s, #2 11.5 s) are separated only by the quote, regenerate the 11.5 s piece first (HNR 6.6). Quote bursts and narration do NOT sit at one loudness.

### Verdict: REWRITE
Tightened/replacement script (95 words incl. quote text, about 21 s at 270 wpm; hook 8 words; first quote at about 4.5 s; uses only notes.md facts: draft 6-8, NBA site 6-9 last season, trainer quote, Stein physical 6-10, Townsend 6-10 not 6-11, 51 points):
Cooper Flagg is six-eight, six-nine, six-ten, or six-eleven. Depends who you ask, and when. At media day a reporter asked if he's six-eleven. [quote: not very accurate. I'm 6-10.] Then he added this. [quote: maybe I'm 6-11. I don't know.] His own trainer told Marc Stein he can't confirm or deny that Flagg has grown. The Mavericks' physical, reportedly: six-ten, without shoes. The NBA's site last season: six-nine. A Dallas Morning News reporter confirmed six-ten, but not six-eleven. Rookie of the Year, fifty-one points as a teenager, and his height needed a tape measure. Six-ten. Not six-eleven.

Cut: "An Instagram account...two inches" and "five days later...six-ten and a half" (unsourced); "So is he six-eleven? Flagg's answer." (filler); the card line "And the NBA's website? Still lists him" becomes one clause with "last season".

---
## 4. Short #20 Would Bad Boys Defense Be Legal Now (25.8 s, 89 words, 210 wpm, 23 shots, avg 1.12 s)

### Scorecard
| # | Item | Score | Evidence |
|---|---|---|---|
| 1 | Hook | WEAK | Voice 0.00 s; "Ninety-two point nine. That is what the Bad Boy Pistons allowed" is a number that does not fit (strong). But first frame = tiny letterboxed 4:3 archive scuffle on blurred bars (about 60% of the frame is blur), plus a cut at 0.4 and 0.5 s (possible 0.1 s flash, check) |
| 2 | Turn | FAIL | The real reversal "But Detroit played eighty-nine possessions" is at 14.4 s (56%). "Now the NBA just told refs" at 8.2 s opens a new topic that is never paid off. 8.2-14.4 s sits on the Duren cliff |
| 3 | Escalation | WEAK | Facts keep coming, but 8.2-14.4 s (6.2 s) is off the loop; 15.15-21.48 s (6.3 s) shows the same two cards twice |
| 4 | Payoff | PASS | Hook = 92.9 vs today. Last 5 s: "Best defense of 1989, best defense of 2026. Four tenths of a point apart." Ends on it (note "best defense" = playoff DRtg, 1st of 16, say "playoff") |
| 5 | Loop | WEAK | "Four tenths of a point apart" does not flow into "Ninety-two point nine"; last shot O5 = first shot (visual only) |
| 6 | Proof/footage | WEAK | Cards 5.41 s = 21% (cap 20%), C89 and C26 each shown twice; the card numbers ARE boxed and readable (good). The hook's 92.9 and the Knicks' 101 are never on screen. "Knicks allowed a hundred and one" is shown over a Cavaliers guard; rule bullets shown over Blazers/Nuggets, Spurs/Kings generic play; the rule quote has no speaker tag |
| 7 | Pace/edit | WEAK | 25.8 s fine; 210 wpm (target 240-290) with a 148 wpm "dragging" sentence at 17.6 s; 5 cuts in 3 s, avg shot 1.12 s |
| 8 | Voice | WEAK (VOICE-REDO) | See Voice section |
| 9 | Packaging | WEAK | Recommended title "How Good Were The Bad Boys Defense Really 😳" = 8 words (limit 7) and ungrammatical ("Bad Boys'"); folder name still "Would Bad Boys Defense Be Legal Now" and the Short never says "legal"; tags 453; pinned comment is three sentences; cover "104.5 VS 104.9" is strong |

### Criticisms
**C1 CLAIM:** The turn is at 14.4 s and the 6 s before it are an off-topic detour.
EVIDENCE: words.json: "Now the NBA just told refs" 8.2; quote 11.4-14.4; "But Detroit" 14.4. Neither the rule nor the quote is used again; the payoff is pure pace math.
WHY: this is the Duren pattern (set-up exposition at 8-10 s).
WRONG IF: the rule line is what holds the 8-14 s audience.
FIX: cut 8.2-14.4 entirely; the "Wrong." turn lands at about 6.5 s.
CONFIDENCE: high.
COUNTER: it carries the original "would it be legal now" title idea. The upload title already dropped it.

**C2 CLAIM:** The first impression is a small blurred archive window.
EVIDENCE: sheet frames 0-4 s (picture band in the middle, blurred bars top and bottom); Notes: 1991 East finals footage used for 1989 numbers.
FIX: crop-zoom 1.25 to fill (accept some softness) or open on the clear Laimbeer/Isiah faces at 2.0 and 3.0 s. CONFIDENCE: medium.

**C3 CLAIM:** Cards are over the cap and repeated, and the pace is slow.
EVIDENCE: shots.json: C89 at 15.15 and 18.5; C26 at 16.48 and 20.08; 5.41 s of 25.8 s. voice_check: 210 wpm, 148 wpm at 17.6 s.
FIX: one side-by-side card ("104.5 | 104.9") for 2.0 s, keep pace/DRtg boxes as overlays; narration at the native fast read. CONFIDENCE: high.

**C4 CLAIM:** The quote is an orphan and quiet.
EVIDENCE: voice_check: quote heard as nothing at 11.3 s; "marginal." at -23 dB (13.96 s); no name tag. FIX: cut it (C1). CONFIDENCE: medium-high.

**C5 CLAIM:** "Best defense of 1989 / 2026" overclaims.
EVIDENCE: notes.md: DRtg is 1st of the 16 PLAYOFF teams; relative to league average the Knicks (7.1 better) beat Detroit (5.7), unsaid. WHY: a commenter will say "playoffs only / era-adjusted". FIX: say "playoff" (tight script). CONFIDENCE: medium. COUNTER: the claim is accurate for playoffs and the Short compares like for like per 100.

### Drop-off prediction
- 8.1-11.4 s: "Now the NBA just told refs..." flat rule talk right after the "right?" setup.
- 15.2-17.6 s: a white B-Ref table for 2.4 s, then again at 18.5-21.5 s.

### Voice: VOICE-REDO
Recogniser diffs: "ninety 2 point" heard "92" and "a 100 and 1" heard "101" (formatting, fine); "Knicks" heard "nix" x4 (normal pronunciation, not a defect); "quote" 11.3 s heard nothing (noisy real audio, audibly risky); "marginal." -23 dB; 17.6 s sentence 148 wpm. Narration pieces HNR 7.5 and 7.8 with 617-627 clicks/min. Quote and narration do not sit at one level. Merge the two ~11 s pieces once the quote is cut (one continuous read).

### Verdict: FIX
Edits: cut "Now the NBA just told refs...grabbing a cutter...bumping a dribbler" and the quote (8.2-14.4 s); turn word "Wrong." at about 6.5 s; one comparison card; no repeated cards; add "slower than the league's ninety-four" and "exactly the league average" (both from the card data in notes.md); say "playoff"; retitle (7 words, e.g. "How Good Were Bad Boys Defense Really").

### Tightened script (91 words, about 20.2 s at 270 wpm; hook 3 words; turn at about 6.5 s)
Ninety-two point nine. That is what the 1989 Bad Boy Pistons allowed per game in the playoffs. Last season's champion Knicks allowed a hundred and one. Nobody defends like that anymore? Wrong. Detroit played eighty-nine possessions a game, slower than the league's ninety-four. The Knicks played ninety-six, exactly the league average. Per hundred possessions, Detroit allowed one-oh-four-point-five. The Knicks allowed one-oh-four-point-nine. Both won the title. Each was the best defense of the sixteen playoff teams. Best playoff defense of 1989. Best playoff defense of 2026. Four tenths of a point apart.

(91 words is 4 under target; do not pad with the rule line, it re-creates the cliff.)

---
## 5. Short #26 How Is A Screen Suddenly Illegal Now (29.9 s, 103 words, 210 wpm, 13 shots, avg 2.30 s)

### Scorecard
| # | Item | Score | Evidence |
|---|---|---|---|
| 1 | Hook | WEAK | Voice 0.00 s. "A screen is legal. Shoving while you set one is a foul." is common knowledge with no number, name or conflict; first frame = Hornets #25 dribbling under the NBA's cropped "Movement - Screens" banner, no screen or shove in sight; 2.6 s ESPN article card at 2.4-5.0 |
| 2 | Turn | FAIL | First real reversal ("But Isaiah Stewart...play on. Why?") at 19.2 s (64%) |
| 3 | Escalation | FAIL | 5.0-19.2 s (14 s) = four examples of the same fact ("Foul" x4: Plumlee 5.0, Reid 11.7, Williams 17.0, Sharpe 18.0); no new fact type for 14 s |
| 4 | Payoff | PASS | "The line isn't contact. It's whether the defender can still play." = the NBA's own rule in one line, closes "where the line is", ends on it |
| 5 | Loop | PASS | "...can still play." flows back to "A screen is legal."; last shot V1 = first shot |
| 6 | Proof/footage | WEAK | One official source (NBA referee video, banner on every frame) = strong proof; premise audited (rule "not new", the Short does not claim it). But 8 spoken names (Plumlee, Reid, DiVincenzo, Okoro, Williams, Sharpe, Stewart, Black) have no name tag and sit on wide shots where the shove is not visible at phone size; names are from speech-to-text only (UNVERIFIED) |
| 7 | Pace/edit | WEAK | 29.9 s at the top of the range; 210 wpm; avg shot 2.30 s and 2 cuts in 3 s are the best pacing of the five; 11.5 s (38%) is the referee narrator's flat voice |
| 8 | Voice | WEAK (VOICE-REDO) | See Voice |
| 9 | Packaging | WEAK | Hub/folder title "How Is A Screen Suddenly Illegal Now" contradicts the audited premise (UPLOAD.md recommends "What Makes A Screen A Foul Now 😳", 7 words, use it); tags 482; pinned comment asks who should get the foul (muddled; ask "Foul or play on, Plumlee or Stewart?") |

### Criticisms
**C1 CLAIM:** Duren cliff in a new coat: the reversal is at 19.2 s.
EVIDENCE: shots.json/words: Q1 6.64-10.79, Q2 13.61-16.62, "But Isaiah Stewart" 19.21. WHY: the most interesting thing (two near-identical contacts, opposite rulings) is saved for the last third. WRONG IF: the retention curve holds through 10-19 s. FIX: open on the contradiction, put Stewart by 7 s. CONFIDENCE: high. COUNTER: the accurate order teaches the rule first; but formula item 2 is explicit.

**C2 CLAIM:** The hook is a definition.
EVIDENCE: words 0.0-4.8. FIX: "Two screens. Same contact. One is a foul, one is play on." CONFIDENCE: high.

**C3 CLAIM:** The viewer cannot see the shoves or who is who.
EVIDENCE: sheet 5-18 s: wide tactical angles, players about 60 px tall, no arrows/zoom/name tags. WHY: "every spoken name shows the right person" cannot be checked by a viewer. FIX: name-tag each real-audio clip (visual_fx nametags), 1.15x punch-in on the contact moment. CONFIDENCE: medium (I cannot see the full-res frames).

**C4 CLAIM:** Real-audio bursts are clipped, quiet and not a player's voice.
EVIDENCE: voice_check: "Okoro" heard "a" (16.3 s, the end of quote Q2 is cut mid-word), quiet words "arms," -13 dB, "and" -12, "both" -13, "he" -23 (15.4 s), "on." -12; a stray "thanks" at 29.34 s after the last word (check the tail); "The" swallowed at 2.5 s. WHY: 38% of the runtime is a monotone referee-narrator read. FIX: use only the Stewart quote; narrate the rest. CONFIDENCE: medium.

### Drop-off prediction
- 5.0-10.8 s: Plumlee play on a wide angle, shove not legible.
- 13.6-19.0 s: "Foul. Robert Williams. Foul. Sharpe. Foul." fourth repetition of the same fact.

### Voice: VOICE-REDO
Narration pieces: #0 (0-6.5 s) HNR 7.8; #2 (10.8-13.6, "Foul, says the NBA. Next, Naz Reid screens for DiVincenzo") 2.6 s HNR 6.5 = glitch suspect; #4 (16.6-22.5) 7.0; #6 (26.8-29.5) 7.7. Names at risk: "Naz Reid" heard "nas reads", "DiVincenzo" "devin chinzo", "Day'Ron Sharpe" "dearon sharp", "Plumlee" "plumley" (check pronunciations by ear), "Okoro" swallowed. Merge: pieces #2 and #4 (both quick "Foul" bridges) into the single narration read in the rewrite so only one real quote (Stewart) interrupts. Quote vs narration level: not equal.

### Verdict: REWRITE (same footage, new order)
Tightened/replacement script (93 words incl. quote text, about 20.7 s at 270 wpm; hook 2 words; Stewart "Play on" at about 6.5 s). Facts only from notes.md: Plumlee foul, Stewart play on, NBA quote about Black, Reid/Okoro, Williams, Sharpe fouls:
Two screens. Same contact. One is a foul, one is play on. Mason Plumlee sets a screen, then extends his arms and shoves the defender. Foul, says the NBA. Isaiah Stewart makes contact on a screen too. Play on. Why? [quote: This contact by Stewart does not affect Black's ability to play defense.] The NBA's own referee video shows both. Naz Reid screens for DiVincenzo, then extends both arms and pushes Okoro. Foul. Robert Williams. Foul. Day'Ron Sharpe. Foul. Four examples, four fouls. The line isn't contact. It's whether the defender can still play.

Cut: "A screen is legal. Shoving while you set one is a foul." (definition), "The NBA just showed referees exactly where the line is" (the banner already says it), the ESPN card (2.6 s), the Q1 and Q2 real-audio bursts (replaced by narration), "But Isaiah Stewart makes contact...and the NBA says play on" (merged to two short sentences).

---
## 6. Short #27 Why Cant Teams Win Back-To-Back Lotteries (24.8 s, 102 words, 248 wpm, 17 shots, avg 1.46 s)

### Scorecard
| # | Item | Score | Evidence |
|---|---|---|---|
| 1 | Hook | PASS | Voice 0.00 s. "Two years in a row, one team beat the lottery. Now the NBA has banned it." = oddity plus a ban inside 8 words (11 for the pair; shorten to 9 below). First frame = Shaq close-up in Magic pinstripes, clear face; 2 cuts in 3 s |
| 2 | Turn | PASS | "Now the NBA has banned it" at 2.1 s, then new facts at 3.3 (Orlando), 7.9 (Cleveland) |
| 3 | Escalation | WEAK | 0-12 s escalates well (1 ball in 66, then 1.7% second time). 12.0-17.0 s (5 s) is a rule recital over the same rule card (twice) and an irrelevant Stern talking head (14.5-17.0) |
| 4 | Payoff | WEAK | Ends on a consequence ("even if the Wizards' ball comes up first, they cannot pick first") but: it is the producer's own reading of the rule (notes.md: no major outlet naming the Wizards was read); the title's "Why" (to stop tanking, per the NBA release title) is never said |
| 5 | Loop | PASS | Shaq close-up returns at 23.7 s; "cannot pick first" re-reads into "Two years in a row, one team beat the lottery" |
| 6 | Proof/footage | FAIL | Cards 5.7 s = 23% (cap 20%; rule card twice: 2.04 and 12.01); Webber/Stern handshake (W2) used twice in 8 s; the 3.3-5.2 s "Orlando took Shaq" shot appears to show a dark-jersey #34 (Shaq wore #32), check; 2014 Cavs clip "#21 = Wiggins, not proven" (notes). Positives: odds table boxed, NBA primary source dated May 28, 2026, "has banned" not "just" |
| 7 | Pace/edit | PASS | 24.8 s, 248 wpm, 2 cuts in 3 s; avg 1.46 s (a bit under 1.7, acceptable) |
| 8 | Voice | PASS (VOICE-OK) | One continuous 24.7 s piece, HNR 7.7, no joins, no real-quote bursts; check "Dybantsa" (heard "dibant's saw") and the quiet "it." (-17 dB) at 3.19 s |
| 9 | Packaging | PASS | "Why Can't Teams Win Back-To-Back Lotteries? 🎰" 6 words; tags 456; pinned comment has two debate questions; rule/ban-oddity lane |

### Criticisms
**C1 CLAIM:** The closing claim is unverified and stated as fact.
EVIDENCE: notes.md: "Derived from the NBA text...No article by a major outlet naming the Wizards was read"; the rule takes effect with the 2027 draft, and the Wizards' 2026 No. 1 pick happened before it. Whether the 2026 pick counts toward the "two consecutive drafts" test is not confirmed anywhere in the notes.
WHY: the whole payoff and the pinned debate rest on it. If wrong, the Short is publicly corrected in the first hour.
WRONG IF: an NBA FAQ or a major outlet states that 2026 counts (then change nothing).
FIX: verify; until then say "By that wording" (tight script) or end on the top-five clause. CONFIDENCE: medium-high that it is unverified; UNVERIFIED whether true.
COUNTER: the plain reading of the NBA text supports it and the Short is not claiming a quote.

**C2 CLAIM:** The title's "Why" is never answered.
EVIDENCE: no word about tanking in the script; NBA release is titled "...to address tanking". FIX: "So the NBA wrote a rule against tanking." (+8 words). CONFIDENCE: high.

**C3 CLAIM:** 12-17 s is the Short's one soft stretch and cards are over the cap.
EVIDENCE: c27_rule 12.01-14.48 (2.5 s) repeats the 2.04-3.32 card; T1/T2 Stern clips 14.48-16.95 (2.5 s, a decade-old talking head not about the rule); card total 5.7 s of 24.8 s. FIX: show the rule once (1.3 s), overlay it as text on Wizards/Dybantsa footage afterwards; swap Stern for Wizards footage. CONFIDENCE: high.

**C4 CLAIM:** Footage identity risk.
EVIDENCE: notes (#21 clip "not proven by name", W2 Webber unnamed); sheet 3.5-5.0. FIX: check frames 3.3-5.2 s; if the player is not Shaq, replace with the Shaq-with-Magic-cap shot. CONFIDENCE: low.

### Drop-off prediction
- 12.0-14.5 s: a card to read while the voice recites rule text.
- 14.5-17.0 s: Stern talking head over "no team's pick can be first two years in a row".

### Voice: VOICE-OK
Mismatches are numbers/years (1992, 66, 2013, 2014, 27) and names: "A.J. Dybantsa" heard "aj dibant's saw" (the script pronunciation hint {Dybantsa|Dye-BAHNT-sah} may be wrong; check by ear and against how his team says it); "team's" heard "teams" (fine); "it." at 3.19 s -17 dB (the hook's key word is swallowed; keep sentence-end level). No real-quote bursts, so no level mismatch.

### Verdict: FIX
Edits: verify C1 or soften; add the "why" (anti-tanking) clause; one rule card only (1.3 s), drop the second; swap Stern shots for Wizards/Dybantsa; vary the Webber clip; hook shortened to 9 words; keep the ending.

### Tightened script (101 words, about 22.4 s at 270 wpm; hook 9 words; turn at 2 s)
One team beat the NBA lottery two years running. Now the NBA has banned it. Orlando won it for Shaq in nineteen ninety-two, then won again a year later, with one ball in sixty-six. Cleveland did it in twenty-thirteen and twenty-fourteen, the second time at one point seven percent. So the NBA wrote a rule against tanking. Starting with the twenty-twenty-seven draft, no team's pick can be first two years in a row, or top five three years running. The Wizards just took A.J. Dybantsa first. By that wording, next May, even if their ball comes up, they cannot pick first.

---
## 7. Ranking (strongest to weakest, for retention under the formula)
1. #27 Lotteries: hook and turn inside 2 s, escalating odds, one soft stretch; needs the claim verified and fewer cards.
2. #21 Jokic: clean payoff and the winners' lane; needs numbers on screen and de-duplication.
3. #20 Bad Boys: best payoff of all five, hurt by the turn at 14.4 s.
4. #26 Screens: accurate and honestly sourced, but the reversal is at 19.2 s.
5. #19 Flagg: hearsay hook, unsourced script facts, reversed quote order, no reveal.

What the strongest Shorts share: a concrete number or oddity in the first sentence, a new fact every 2-3 s, and a last line that is a number or consequence on the named people's footage.

## 8. Three most common defects across these five
1. Late or missing turn (4 of 5): #20 at 14.4 s, #26 at 19.2 s, #19 at 8.6 s, #21 at 8.3 s. Only #27 turns by 3 s. The cause is rule/definition set-up before the contradiction.
2. Numbers heard but not seen, plus repeated shots and card misuse (5 of 5): #21 no stat cards and b8/b11 repeats; #19 gym clips x4; #20 and #27 over the 20% card cap with the same card shown twice; #26 no name tags.
3. Claims stronger than the sources, or quotes out of context (4 of 5): #19 unsourced Instagram/6-10.5 lines and reversed quote order; #27 derived Wizards ban stated as fact; #20 "best defense" without "playoff" plus an orphan quote; #21 "four games to spare" ignoring the 17 missed games.

## 9. Not verified
Audio by ear; footage identity beyond the sheet resolution; every premise beyond what notes.md/UPLOAD.md cite (no web checks this round); retention predictions are guesses.

## 10. Machine-readable ratings
Voice mapping: PASS = VOICE-OK, WEAK = VOICE-REDO (all narration is being re-recorded). Word counts of the tight scripts: #21 88, #19 95, #20 91, #26 93, #27 101 (quote text counted).

```json
{
 "ratings": {
  "21": {
   "1": "WEAK",
   "2": "WEAK",
   "3": "PASS",
   "4": "PASS",
   "5": "WEAK",
   "6": "WEAK",
   "7": "WEAK",
   "8": "PASS",
   "9": "PASS",
   "verdict": "FIX",
   "tight_script": "Jokic is twelve triple-doubles from the NBA record. Russell Westbrook, who just retired, finished with two hundred nine. Jokic is at one ninety-eight. But last season he had thirty-four triple-doubles in just sixty-five games, even after missing seventeen. That's one every two games. At that pace, twelve takes about twenty-three games. Last Christmas night he went for fifty-six, sixteen and fifteen, the first fifty-five, fifteen, fifteen game in NBA history. This Christmas is game twenty-seven, in Golden State. If he plays them all, that's four games to spare."
  },
  "19": {
   "1": "WEAK",
   "2": "WEAK",
   "3": "WEAK",
   "4": "FAIL",
   "5": "WEAK",
   "6": "FAIL",
   "7": "WEAK",
   "8": "WEAK",
   "9": "PASS",
   "verdict": "REWRITE",
   "tight_script": "Cooper Flagg is six-eight, six-nine, six-ten, or six-eleven. Depends who you ask, and when. At media day a reporter asked if he's six-eleven. [quote: not very accurate. I'm 6-10.] Then he added this. [quote: maybe I'm 6-11. I don't know.] His own trainer told Marc Stein he can't confirm or deny that Flagg has grown. The Mavericks' physical, reportedly: six-ten, without shoes. The NBA's site last season: six-nine. A Dallas Morning News reporter confirmed six-ten, but not six-eleven. Rookie of the Year, fifty-one points as a teenager, and his height needed a tape measure. Six-ten. Not six-eleven."
  },
  "20": {
   "1": "WEAK",
   "2": "FAIL",
   "3": "WEAK",
   "4": "PASS",
   "5": "WEAK",
   "6": "WEAK",
   "7": "WEAK",
   "8": "WEAK",
   "9": "WEAK",
   "verdict": "FIX",
   "tight_script": "Ninety-two point nine. That is what the 1989 Bad Boy Pistons allowed per game in the playoffs. Last season's champion Knicks allowed a hundred and one. Nobody defends like that anymore? Wrong. Detroit played eighty-nine possessions a game, slower than the league's ninety-four. The Knicks played ninety-six, exactly the league average. Per hundred possessions, Detroit allowed one-oh-four-point-five. The Knicks allowed one-oh-four-point-nine. Both won the title. Each was the best defense of the sixteen playoff teams. Best playoff defense of 1989. Best playoff defense of 2026. Four tenths of a point apart."
  },
  "26": {
   "1": "WEAK",
   "2": "FAIL",
   "3": "FAIL",
   "4": "PASS",
   "5": "PASS",
   "6": "WEAK",
   "7": "WEAK",
   "8": "WEAK",
   "9": "WEAK",
   "verdict": "REWRITE",
   "tight_script": "Two screens. Same contact. One is a foul, one is play on. Mason Plumlee sets a screen, then extends his arms and shoves the defender. Foul, says the NBA. Isaiah Stewart makes contact on a screen too. Play on. Why? [quote: This contact by Stewart does not affect Black's ability to play defense.] The NBA's own referee video shows both. Naz Reid screens for DiVincenzo, then extends both arms and pushes Okoro. Foul. Robert Williams. Foul. Day'Ron Sharpe. Foul. Four examples, four fouls. The line isn't contact. It's whether the defender can still play."
  },
  "27": {
   "1": "PASS",
   "2": "PASS",
   "3": "WEAK",
   "4": "WEAK",
   "5": "PASS",
   "6": "FAIL",
   "7": "PASS",
   "8": "PASS",
   "9": "PASS",
   "verdict": "FIX",
   "tight_script": "One team beat the NBA lottery two years running. Now the NBA has banned it. Orlando won it for Shaq in nineteen ninety-two, then won again a year later, with one ball in sixty-six. Cleveland did it in twenty-thirteen and twenty-fourteen, the second time at one point seven percent. So the NBA wrote a rule against tanking. Starting with the twenty-twenty-seven draft, no team's pick can be first two years in a row, or top five three years running. The Wizards just took A.J. Dybantsa first. By that wording, next May, even if their ball comes up, they cannot pick first."
  }
 }
}
```
