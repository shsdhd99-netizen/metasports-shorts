# Critic v2 (Oct 13, 2026): the independent pre-publication review

Why v2: the Round 3 critic's 0-100 craft score ran **backwards** against real views (Spearman −0.63, n=14; it ranked #19 last and #29 second). See `Research Notes/Winning Formula v2 (Oct 13, 2026).md` (g). v2 judges the **premise and the first second first**, uses the measured tools for defects, and gives a verdict, not a score. Run it as a separate agent that did not build the Short. It must look at the export (frame sheet + transcript of the final audio), not only the script.

## Inputs the critic must open
- `final.mp4` (and any variant), `_audit/watch/report.md` + `sheet.jpg` (`python3 Tools/watch_short.py final.mp4 --out _audit/watch` with whisper STT)
- `script.txt`, `notes.md` (fact sheet with dated sources), `shots.json`, `UPLOAD.md`
- `python3 Tools/qa_short.py --folder F`, `python3 Tools/voice_check.py --folder F --stt whisper`, `python3 Tools/voice_quality.py --folder F`

## Gate A: premise (any FAIL = REJECT or rewrite)
1. **Second-1 test.** From the first frame + first 8 words alone, can a non-fan state the question? Write the question they'd state. If you can't, FAIL.
2. **Visible object.** Is the thing that "can't be right" on screen in frame 1 (the jersey, the height, the pass, the number)?
3. **One measure.** Do the facts every 2-3 s move the same measure? List any hop.
4. **Not a retell.** No bigger channel has already told this exact story (search; `Tools/copy_check.py`). Our own old winner retold by name also fails.
5. **Answering ending.** Does the last line answer the first line (ideally the subject's voice or one number) and stop? No debate question, CTA, hedge or restatement.
6. **Truth.** Every voiced claim matches a dated source in notes.md; "only/first/never/taller" claims are qualified as the source qualifies them ("listed", "regular-season").

## Gate B: defects (any = NEEDS REVISION)
- qa_short.py FIX lines (replays, frozen holds, loudness, voice cut off, length 21-45 s)
- voice_check REDO issues: wrong or garbled words, especially names and numbers
- the wrong person, team or era on a spoken name; a number spoken but not visible or not proven
- burned-in source captions or tickers fighting our captions; captions over faces or the key action
- a card or screenshot in the first 4 s (warn; an [H] rule)
- dead air over 0.6 s, a shot that holds after its information is spent, a payoff visual that appears before the payoff line

## Gate C: viewer pass (write it as a viewer, timestamps required)
Where would you swipe, and why? Name the second and the line or picture. Is the payoff worth the 20-25 s?

## Verdict
- **PASS:** the export was inspected, Gate A all pass, no Gate B defect.
- **NEEDS REVISION:** list the exact edits (line, shot, timestamp).
- **REJECT:** say whether a new angle, a rebuild or abandonment is right.
Also record, for experiment 3 in Winning Formula v2, a **3-point formula score** (1 point each: second-1 test, one measure, answering ending) and your gut rank among the Shorts reviewed. These are predictions to check at 48 h, not quality grades.
