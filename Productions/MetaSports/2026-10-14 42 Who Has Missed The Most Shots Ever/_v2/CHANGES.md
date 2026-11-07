# #42 v2: same edit as v1 plus controlled push-ins (Oct 15, 2026)

Only variable changed from `_v1`: per-shot `zoom` in `shots.json` (a slow push from 100% to 100+z% over the shot). Same voice (Alex), footage, cards, captions, one whoosh, no music.

| Shot | Zoom | Why |
|---|---|---|
| S1 airball, both visits | 0.10 each | LeBron is small in a wide frame: pull the eye toward him; 3.7%/s is under the house limit (4%/s) |
| S2 LeBron hands up (record) | 0.05 | emphasis on the record moment |
| S5 LeBron and Bronny (JAMES JR 9) | 0.06 | lands on Bronny's number as "with his son" is said |
| S6 LeBron question face | 0.05 | the "worse shooter?" beat |
| S8 LeBron smiling | 0.06 | the payoff face |
| Kobe x2, cards | none | the Kobe clips are already a 2.67x blow-up; more zoom only softens them |

Checked on the render: frames at 5.0 s and 13.9 s are visibly tighter than `_v1`'s at the same times. `qa_short.py --full` result is the same as `_v1` (only the mono-downmix "clipping" false alarm). **Not judged by ear or by views; v1 stays the safe version.** If the owner prefers motion, post v2; keep the same title.