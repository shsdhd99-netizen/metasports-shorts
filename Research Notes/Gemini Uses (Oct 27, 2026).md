# What the Gemini key is good for (Oct 27, 2026)

**The owner, Oct 27:** "start the study and anything else useful the gemini key is useful for, put it in your notes since i have no billing".

## Status
- **The key works.** It's on Google's free tier, so it never charges anything: when a limit is hit, Google just refuses until it resets.
- **Where it lives:** only on this session's cloud machine (`Tools/.env`, which git ignores; it is never committed). It disappears when the machine resets, and the scheduled daily runs can't see it.
- **To make it permanent:** add it in the environment settings as `GEMINI_API_KEY`. It was pasted in chat, so the safest version is a new key (delete the old one at aistudio.google.com/apikey).
- **Free-tier limits:**
  - 8 hours of YouTube video a day;
  - per-minute and per-day request caps for each model (see aistudio.google.com/rate-limit);
  - public videos only.
- **Privacy:** on the free tier, Google may use what we send to improve its products. That's fine for public Shorts and for drafts that will be public soon.
- **Models on a free key, Oct 27:**
  - **Busy (503 "high demand"):** 3.8 and 3.7 flash. 3.6 and 3.5 flash worked for a few calls, then went busy too.
  - **Worked all day:** flash-lite (3.5 and 3.1).
  - **Refused (429):** pro models; they're not on the free tier.
  - **Closed to new keys:** 2.5.
  - `Tools/yt_watch.py` now tries them in that order and skips a busy one for 10 minutes.

## What I tested, and how far to trust it [S]
| Use | Test | Result | Trust |
|---|---|---|---|
| Word-for-word narration of a Short | Our "Most Missed Threes" and Wemby Shorts | Matched our scripts | **High** |
| Shots in the first 3 s and 5 s | The same two Shorts, against our edit files | Exact on both (3.6 flash and flash-lite) | **Medium**: only 2 checks |
| Total shot count | The same two | Off by up to 3 | **Low** |
| Music bed: yes or no | The same two (both posted without a bed) | Said "music" on both. Arena sound in the clips probably counts as music. | **Don't use** |
| Find a quote and its timestamp in raw footage | Haliburton's 2-minute postgame interview | Found "ABA jerseys… Dr. J" at 58-62 s, the same as I found by hand. Quoted the words exactly. | **High** |
| Pre-post check of a draft | Haliburton, Nuggets kid, Hand of God | All READY, no problems listed | **Lenient**: it adds to QA, never replaces it |

## Uses, most valuable first
1. **Top-vs-bottom channel studies** (`Tools/watch_study.py`).
   - Gemini watches a channel's best and worst recent Shorts, and I read one CSV.
   - This is our cheapest evidence for or against our rules: hold the opening, no cards, replays, countdowns, a short first line.
   - First run, Oct 27: Swishyyy, Hoopiverse and Ahmed's Goal, 60 Shorts in about an hour, all free.
   - Result: hits and misses opened the same way; the subject was the difference.
   - Write-up: `Research Notes/Watch Study/Findings (Oct 27, 2026).md`.
2. **Competitor outliers in the daily research.** The 5:43 AM task already watches the top 2 outliers when the key is set, and says what the hook and payoff were.
3. **Pre-post check of every draft** (`--precheck`).
   - Listens for voice glitches, captions that don't match, loud music, frozen frames and a wrong player.
   - Added to the daily-run skill (step D) for when the key is set.
4. **Find moments and quotes in long footage** (press conferences, full broadcasts from archive.org).
   - Upload the local mp4 and ask "when does X happen?". That's far cheaper than me looking at frame sheets.
   - Long files cost many Gemini tokens: about 100 per second at the default quality. A 2-hour broadcast is about 720K, so cut it to the half you need or use `--fps 0.5`.
5. **Check quotes by ear.** Before, quotes came from speech-to-text and nobody checked them by ear. Now Gemini can confirm the exact words and who says them.
6. **Check the right player is on screen** while his name is spoken (jersey number, face, team).
7. **Our own Shorts against Studio's "stayed to watch"** (once exports or the Analytics sign-in come in).
   - Our edit files already give the cuts and cards.
   - Gemini adds the things only a viewer can judge: is the first second clear, does the end land?

**Not good for:** music yes/no, exact shot counts, judging whether a Short is good (it's lenient), and private or unlisted videos.

## Commands
```
python Tools/yt_watch.py <link or id>                         # full report (JSON) for one Short
python Tools/yt_watch.py <id> --ask "When does the bench react?"
python Tools/yt_watch.py "<DRAFT>.mp4" --precheck --out-dir "Research Notes/Watch Reports/drafts"
python Tools/watch_study.py --channels @swishyhoopz @HoopiverseYT --name "NBA narrated top vs bottom"
```
Reports go to `Research Notes/Watch Reports/` and studies to `Research Notes/Watch Study/`. Each report is cached, so a run cut short by the daily limit continues the next day without paying twice.

## Cost
- **Gemini:** $0. Its limits are the only cap.
- **Claude usage:** small. I read one CSV or summary per study instead of looking at frames.
