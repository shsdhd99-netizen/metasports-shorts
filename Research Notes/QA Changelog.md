# QA changelog (one line per day: what changed, why, evidence). Owner rule, Nov 5: QA is improved every single day.

How to add a line: run `python Tools/qa_audit.py`, read `Research Notes/QA Audit.md`, change ONE check, then write it here.

- **2026-11-05** ADDED `Tools/precut_lint.py` (run on `cuts_plan.json` before cutting): source window past the end of the clip, shot 1 under 2.0 s, overlays in the caption band, shots with no `why`, source under 720p (FIX), source under 1080p, reuse, one-source share (warn). **Why:** `qa_audit.py` over 22 saved QA runs shows the 720p blow-up warning fired 337 times in 14 Shorts and "soft footage" 52 times in 9, and #95 needed 5 re-cuts for problems that were visible in the plan. **Next check to try:** an automatic "player identity" check using jersey-number OCR on the first frame of each clip (the wrong-player clip was caught only by eye). Also added `Tools/qa_audit.py` and `Tools/build_gate.py`.

- 2026-11-06: `Tools/qa_portions.py` added: QA by portion (SCRIPT, VOICE, FOOTAGE, EDIT, AUDIO, PACKAGE, LIVE), each PASS/WARN/FAIL. Run before scheduling: `python Tools/qa_portions.py --folder F --video V --channel nba|fc`. First run caught S30 with no cover image (fixed).
- 2026-11-06: `Tools/pin_helper.py` (writes Desktop\PIN THESE TODAY.txt with links + pinned comments) and `Tools/weekly_review.py` (auto Sunday review) added.
