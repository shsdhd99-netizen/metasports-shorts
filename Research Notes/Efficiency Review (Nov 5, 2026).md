# Where time and tokens go in building a Short, and what would save them (Nov 5, 2026) [H: estimates from this session, not metered]

**Observed on #95 (Lendeborg), a typical build:** about 55-70 tool calls over roughly 2 hours and on the order of 90-130K tokens. About a third was images (contact sheets and frame checks), a quarter was reading long docs and logs, and a fifth was rebuild loops (5 re-cuts: a wrong-player clip, a repeated podium shot, a source cut that started on a dissolve, a flash frame, a 0.1 s clip shortfall).

| Waste | Fix (find or build) | Estimated saving per Short |
|---|---|---|
| Finding the right player and moment by looking at contact sheets | local face/jersey verification (InsightFace is already in the LatentSync venv); OCR of the scorebug (EasyOCR or Tesseract) to search a highlight for "4Q 3:16" or a score; a whisper transcript of postgame videos to find the quote (done today with faster-whisper) | 25-35% of tool calls and most image tokens |
| Rebuild loops that QA catches late | run `edit_lint`, a flash detector and a "clip shorter than shot" check on `cuts_plan.json` BEFORE cutting; one command `build_short.py` (fill_len, cut, deflash, assemble, qa, fix list) | 3-4 of the 5 re-cuts, 15-20% |
| Reading long rule files each run | a machine-readable `rules.json` (lanes, limits, thresholds) and a one-page `NOW.md` instead of 50 KB of Playbook | 10-15K tokens per session |
| Finding footage | a cached index of team-site videos by game and player (the NBA.com index API supports it): search by game id, not by title | about 10% |
| Re-checking facts | per-claim source rows created at research time (notes.md template exists), a `facts.csv` that QA reads | 5-10% |
| Sync/QA by eye | the SyncNet wrapper (built for Max), automatic mouth/word checks | large for avatar work |
| Posting and analytics glue | already automated (timers); `state.py` health check added | small |

**Total:** about 40-50% less time and tokens per Short once the pre-cut lint and the identity/OCR finder exist (roughly 2 h and 110K tokens down to 1-1.2 h and 55-65K), more on days with 2 builds. Over a month of 40-60 builds that is 40-80 hours and 2-3M tokens. **The biggest single lever is not building weak Shorts at all (the build gate).**

**Useful to others (after removing keys, personal data and rights-sensitive footage):**
- `max_site_protect.mjs` and `max_site_deploy.py`: a private client preview page on Netlify's free plan (client-side encrypted, forms still work). Freelancers need this.
- The SyncNet QA wrapper for AI avatar videos (SyncNet weights are research-licensed: check before commercial use).
- `edit_lint.py`, `fc_reuse.py`, `fc_study.py`: measurable Short-editing QA and a "does repetition hurt retention" study kit.
- `channel_totals.py`: YouTube Partner Program progress (subs, Shorts views per 90 days, projection) from the read-only Analytics API.
- `idea_gauge.py`, `copy_check.py`, `build_gate.py`: a pre-production decision process (score, originality check, skip rule).
- The case-study format: data pull, benchmark, monetization math, ranked tests.
Not shareable as is: anything with the owner's keys, the Max Claude client materials, league footage downloads.
