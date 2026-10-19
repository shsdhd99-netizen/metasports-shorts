# UPLOAD: #48 Who Has Missed The Most Threes In NBA History? (THE #42 FORMAT, voice A/B slot 1 = Alex)

**DRAFT, awaiting your approval. Not posted, not scheduled.**
**File:** `DRAFT - awaiting approval - 48 Harden most missed threes (no music).mp4` (same as `final.mp4`, 23.5 s, 1080x1920). Video files are not in git; rebuild with `python Tools/assemble.py --folder "<this folder>" --no-music` after re-cutting from `src/` (every in-point and crop is in `sources.csv`).
**Post time:** 6-11 AM ET. **Re-check the counts on posting day** (the 2026-27 season starts Oct 20-21; Harden and Curry add misses every game). If either number moved, re-voice only that sentence.

**Title (exactly as written):** Who Has Missed The Most Threes In NBA History? 😳
**Hashtags (up to 3):** #nba #jamesharden #shorts
**Tags:** james harden, most missed threes nba, harden missed threes record, steph curry threes, harden 3 point attempts, harden 1028 threes, most three point attempts season, nba records, harden vs curry, lebron three point percentage, nba history, cavaliers harden
**Pinned comment:** Regular season, Basketball-Reference: Harden 9,323 attempts, 5,933 misses. Curry 10,073 attempts, 5,825 misses. Is volume a flex or a flaw?

**Music:** none in this render (log it if you add one on upload: the #42 test needs music yes/no recorded).
**Voice:** Alex (multilingual v2, speed 1.2), the first post of the pre-registered voice A/B. The Designed Narrator take is kept in `_voice_designed/`.

## What's on screen (all clips verified by eye; `sources.csv`)
| Time | Line | Footage |
|---|---|---|
| 0.0 | "James Harden has missed more threes than anyone in NBA history." | Harden step-back three at the Knicks, Jan 23 2019 (Knicks official replay): **the miss** |
| 2.4 | "5,933." | the same play at half speed: Mitchell Robinson flies at the release. **5,933 MISSED THREES** |
| 4.9 | "And he's made more threes than anyone except" | Harden step-back three vs Dallas, Jan 31 2020 |
| 6.5 | "Steph Curry. Second in misses is Curry: 5,825." | Curry #30 handling vs Lakers, Christmas 2024; **CURRY 5,825** |
| 9.3 | | Curry close-up, same game |
| 10.9 | "In one season, Harden took 1,028 threes." | Harden step-back three over Denver, Mar 28 2019 (the 2018-19 season); **1,028 IN ONE SEASON** |
| 12.9 | "The most ever." | Harden #13 jogging back, Mar 30 2019; **1,028 THE MOST EVER** |
| 14.5 | "So is he a bad shooter? No." | Harden turns to camera, Mar 28 2019 |
| 16.1 | "Harden makes thirty-six percent from three." | Harden three from near the logo vs Miami, Feb 28 2019; **HARDEN 36%** |
| 17.8 | "LeBron makes thirty-five." | LeBron #6 rising for a three at Washington, Mar 19 2022; **LEBRON 35%** |
| 19.1 | "Harden just shot more threes than anyone not named Curry:" | Harden step-back move vs Denver, Mar 28 2019 |
| 21.5 | "9,323." | Harden walking back after a three at Golden State, 2019 playoffs (slow motion); **9,323 THREES SHOT** |

**Effects (4):** whoosh into HARDEN 36%, ding on LEBRON 35%, riser into the flip, pop on 9,323. None on the miss.

## QA (`qa_short.py --full`, Oct 19): PASS
Warnings, all known:
- **Every clip is 720p** (official NBA.com team-site uploads; the cloud can't reach YouTube), so it's blown up about 2.7x and softer than a 1080p source. On the PC, swapping in 1080p YouTube copies of the same plays would sharpen it. The plays are listed above.
- Slowed shots: the miss replay at 2.4 s plays at about half speed on purpose, and so does the last shot (1.47x, a slow-motion walk-off). Three more (Curry close-up, "The most ever", the question beat) run 1.1-1.3x slow to fill their line.
- Speech-to-text heard "and" for "In" at 10.9 s: listen to that word.
- Pace 168 wpm by the QA count (digits count as one word); it's the same Alex settings as #42.
- True peak -0.7 dBTP (want -1.0 or lower): YouTube's re-encode normally handles this.

**Rights:** NBA footage; a Content ID claim is possible, as on every Short. Sources: Rockets, Knicks, Warriors and Lakers official team-site uploads on NBA.com.
