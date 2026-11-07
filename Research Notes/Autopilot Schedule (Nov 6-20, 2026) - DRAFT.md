# Autopilot schedule, Fri Nov 6 to Fri Nov 20, 2026: DRAFT for the owner (written Nov 6 by the PC terminal)

> **SUPERSEDED Nov 6 by `Autopilot Schedule v2 (Nov 9-22, 2026).md`** (selective: only ideas rated 10+/12 get a slot). Kept for the tonight table and the Studio-access section.

Merges `Two-Week Plan (Nov 7-20, 2026).md` (cloud), the posting test (`Posting Plan (Nov 5, 2026).md`), the test-and-learn policy and tonight's 7:30 PM slot test. **Nothing here is scheduled except what is marked ON YOUTUBE.** Times ET. Every slot is filled only if the idea passes `build_gate.py` (80%+, FRESH, proven lane or a logged one-variable test); an empty slot is skipped and counted.

## 0. Tonight (done, on YouTube, private until publish)
| Time | Channel | Short | Notes |
|---|---|---|---|
| 12:00 PM | FC | S28 (old copy titled "unknown", now private) | replaced |
| 1:35 PM | FC | S28 replacement, music version, correct title | `tXAQ1r12Fnw` |
| 3:30 PM | NBA | #95 Lendeborg peer pressure | `MM1y6yBSgLE` |
| **7:30 PM** | **NBA** | **#92 "This Rookie Told Luka He Sucks" (real audio, no music; QA PASS after re-fetching clips)** | `5dp81kNOClU`; new-slot test; its Sunday 7:15 AM slot is freed |
| **7:30 PM** | **FC** | **S30 "The Ballon d'Or winner who missed a penalty days later" (51 s, no music, QA PASS)** | `m_HnsJrkvIQ`; new-slot test; its Monday slot is freed. Weak spot: no clean clip of the kick itself (labelled). |
**What the 7:30 PM test measures:** views at 24 h and 72 h and engaged ratio of each, against the same channel's 3:30 PM / 12 PM posts; n=1 each, so it only shows direction. Run the evening slot on 3 more days before concluding anything.

## 1. The two weeks (even dates NBA 2 + FC 1; odd dates from Nov 9 NBA 1 + FC 2; the posting test)
`P` = planned (built, scheduled a day ahead). `M` = last night's best moment (research 3:43 AM, built by the 6:45 AM gap-fill, 3:30 PM). `T` = TEST lane (one variable changed, logged in `Test Log.csv`). `K` = proven goalkeeper lane.
| Date | NBA 7:15 AM | NBA 3:30 PM | FC 12:00 PM | FC 6:00 PM (odd dates) |
|---|---|---|---|---|
| Sat Nov 7 | P Klay blocked Steph (#98, A1 builds today; real audio if the call is good) | M Fri night | K S29 Martinez (ON YOUTUBE) | - |
| Sun Nov 8 | P #79 buzzer-beaters (built; #92 moved to tonight) | M Sat night (Curry v DeRozan watch) | K S09 Ronaldo (ON YOUTUBE) | - |
| Mon Nov 9 (odd) | P #67 Jordan insult (no music, story-format test) | - | K S21 Higuita (Style v3 test) | T family-with-a-twist premise (a star's relative) |
| Tue Nov 10 | P List 1: most missed free throws (copy-check first) | M Mon night | K Bounou/Spain 2022 (2 sources first) | - |
| Wed Nov 11 (odd) | P #65 LeBron answers a Knicks fan | - | T fans-vs-club premise | K Livakovic's saves v Japan (2 sources first) |
| Thu Nov 12 | P List 2: most turnovers | M Wed night (NBA Cup) | K S22 Ceni | - |
| Fri Nov 13 (odd) | P #59 WNBA minimum (check the CBA line first) | - | T banned-skill/rule you can see | T stat-device premise |
| Sat Nov 14 | P milestone catch-up (Curry/DeRozan or LeBron/Kidd) or best leftover | M Fri night | K S36 Martinez changed the rules | - |
| Sun Nov 15 (odd) | P List 3: most fouled out | - | K new keeper 3 (source first) | T rejected-then-revenge World Cup story |
| Mon Nov 16 | P best leftover moment | M Sun night | T manager oddity, new hook (action-first) | - |
| Tue Nov 17 (odd) | P List 4: most technical fouls | - | K new keeper 4 | T club saga, new footage type |
| Wed Nov 18 | P Lendeborg Part 3 (only if he keeps rolling) | M Tue night (NBA Cup) | K S31 Baby Messi bathed (copy-check TAKEN: own call) | - |
| Thu Nov 19 (odd) | P best leftover | - | K S37 Como 9-1 (needs a 2nd source) or new keeper | T family/fan-kid lane, second attempt with a changed variable |
| Fri Nov 20 | P List 5: most games lost | M Thu night | Ballon d'Or follow-up with our own angle (copy-check Ahmed's 3 titles) | - |
Counts if every slot fills: NBA 22 posts (14 at 7:15 AM + 8 at 3:30 PM), FC 20 posts (14 at noon + 6 evening). Credits: about 38-45K of the 67K left (plan resets Nov 19); the posting test is credit-neutral on average because odd dates drop one NBA post.

## 2. Reading the test (set before it runs)
- Per-post 72 h median by posts-that-day, total views per day, cannibalization of the first post, subs per 1K views, engaged ratio.
- First read Nov 17 (about 4-5 days per arm, direction only), decision Dec 3 (12 days per arm).
- Tonight's 7:30 PM test: compare with the same day's earlier post on each channel at 24 h and 72 h.
- If a slot cannot be filled by a gate-passing idea, the Daily Log gets `AUTO: <slot> skipped (reason)`; skipping does not count against the automation target.

## 3. What the autopilot still needs from you
- The cloud routines are blocked on keys; the PC gap-fill (6:45 AM NBA, 7:30 AM FC) builds. Sleeping PC wakes for the 6:25 task.
- `AUTOPILOT_TEST.txt` keeps terminal sessions from building; I built #92's QA and S30 tonight only because you asked for the 7:30 PM test.
- The "unknown" titles: both old copies are now private; delete them in Studio when you are ready.

## 4. Studio access, "indefinitely, on all accounts" (what is possible)
**I cannot be given your passwords, and you should not paste them or tokens in chat.** What works:
1. **Right now (read-only, no Studio needed):** the YouTube Analytics API and Data API read both channels with refresh tokens in `Tools/.env`. That already gives views, retention curves, titles, privacy, schedule times.
2. **The missing numbers ("stayed to watch") are Studio-only.** Two safe routes: (a) a weekly Studio CSV export you drop in `Research Notes/Studio exports/` (30 s), or (b) the Claude in Chrome extension on your own PC browser, signed into the same claude.ai account as this Claude Code (it is currently disconnected with "OAuth token belongs to a different account"). With (b) I would read the Studio pages from your logged-in browser; I would still never enter passwords, and it only works while the browser is open.
3. **Edit/replace/delete from code (so a bad title is fixed in seconds):** re-authorize each channel once with the broader `youtube` scope (today the upload token has `youtube.upload` only, which cannot edit or delete). Steps: Google Cloud console, OAuth consent screen, set **Publishing status to "In production"** (in "Testing" the refresh tokens expire after 7 days, which is why "indefinitely" fails today), then run the auth step once per channel and store the new refresh tokens in `Tools/.env`. Risks to accept knowingly: a token with `youtube` scope can edit and delete anything on that channel, so keep `.env` private and rotate if the PC is ever shared.
4. **Several channels, one login:** if both channels sit under one Google account as brand accounts, one token per channel is still needed (a token is per channel). Adding the Claude account as a channel manager is not possible (Claude has no Google account).
**My recommendation:** do (2a) weekly now, and (3) once this week. That removes the "I can't fix a title" problem and the 7-day token expiry without handing over any password.
