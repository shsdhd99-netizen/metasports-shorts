# #42 production package: "Who Has Missed The Most Shots Ever?"

**Status: script-ready + shot plan; footage partly in hand. NOT rendered.**
- **Blocker:** a clip of LeBron **missing** a shot, plus one Kobe clip. YouTube downloads are bot-blocked in the cloud, and X has no search here.
- **Next action:**
  - Get 2-3 LeBron miss clips and 1 Kobe jumper clip, from X post URLs (the owner can paste any) or on the PC.
  - Then: `voice_take.py` → `anchor_shots.py` → `assemble.py` → QA → Critic v2.

## Beats (Hook / Context / Payoff), 70 words, about 17 s at 250 wpm
| Beat | Line | Purpose |
|---|---|---|
| **Hook** (0-2.6 s) | "LeBron James has missed more shots than anyone in NBA history." | The paradox: the GOAT-tier scorer leads in misses |
| Proof | "15,541." | The number on screen (in the captions) |
| Contrast | "And he's the all-time leading scorer." | Escalation: both records at once |
| Context | "The old record was Kobe's: 14,481 misses. LeBron passed it in October 2024, the same night he first played with his son." | One measure (misses), plus the emotional tie-in (#23's top-like-rate topic) |
| Turn | "So is he a worse shooter? No." | The viewer's question, asked and answered |
| Proof | "LeBron makes fifty-one percent. Kobe made forty-five." | |
| **Payoff** | "LeBron just shot more than anyone, ever: 31,502 times." | The answer as one number; stop |

## Shot plan (line → picture that proves it)
| # | Words | Picture | Have it? |
|---|---|---|---|
| 1 | "LeBron James has missed more shots" | **Frame 1:** LeBron's jumper **clanking off the rim** (a miss, close) | ✗ need (X: NBA/Sixers/Lakers posts) |
| 2 | "...than anyone in NBA history. 15,541." | A second miss, a different angle | ✗ need |
| 3 | "And he's the all-time leading scorer." | The 38,388 record moment (Feb 7 2023) or any LeBron make | ✓ LeBron make clips exist in #01/#18/#38/#39 `clips/` (check jersey/era) |
| 4 | "The old record was Kobe's: 14,481 misses." | Kobe fadeaway | ✗ need 1 Kobe clip |
| 5 | "LeBron passed it in October 2024, the same night he first played with his son." | LeBron + Bronny on court together (Oct 22 2024) | ✓ #23/#24 `clips/` (LeBron + "JAMES JR 9") |
| 6 | "So is he a worse shooter? No." | LeBron reaction/face | ✓ #38/#39 clips |
| 7 | "LeBron makes fifty-one percent. Kobe made forty-five." | **One card:** 50.7% vs 44.7% (B-Ref/StatMuse source line) | build with PIL (house card style, as `c_3pa.png` in #41) |
| 8 | "LeBron just shot more than anyone, ever: 31,502 times." | **Card reveal in two steps** (31,502 FGA #1; Kareem 28,307 #2), then back to frame 1 (loop) | build |

Cards: 2, about 4 s of about 17 s; none before 4 s; never two in a row.

## Voice direction
- Clone "pham v2", multilingual_v2, speed 1.15 (Creative System v3 §6).
- Numbers use the {display|spoken} braces so the captions show digits.
- Keep the "No." as its own short beat after the question (about 0.2 s pause).
- Names: "LeBron", "Kobe", "Bronny": no respelling needed.
- Check with `voice_check.py`.

## Captions and sound
- House captions; digits show via the braces.
- One "clank" rim sound on frame 1's miss (the picture makes the sound). One whoosh into the % card.
- No music.

## Upload package (draft)
- **Title:** Who Has Missed The Most Shots In NBA History? 😳
- **Hashtags (≤3):** #nba #lebronjames #shorts
- **Tags (≤12):** lebron james, most missed shots nba, lebron missed shots record, kobe bryant missed shots, lebron passes kobe, nba records, lebron all time leading scorer, lebron field goal attempts, lebron shooting percentage, kobe vs lebron, nba history, sixers lebron
- **Pinned comment:** "Regular season: LeBron 15,541 misses, Kobe 14,481. Does volume make the misses a flex or a flaw?"

## PC footage (Oct 14 night, Grok)

Claude was out of usage, so these were pulled on the PC. They are in `src/` (not in git). Nothing was voiced.

- **LeBron miss, usable:** `src/1863773416718774655.mp4` from https://x.com/LADEig/status/1863773416718774655. 1080x1920, 5.2s. Lakers #23 releases a three against the Timberwolves and the ball misses short of the rim. It is an airball, so it cannot take a rim sound. Frame 1 can use this only if the sound stays silent on the miss.
- **Kobe source, not cut:** `src/kobe-nba-lk5o2PK76hs.mp4` from the official NBA video https://www.youtube.com/watch?v=lk5o2PK76hs ("Kobe's Signature Fadeaway"), 1280x720, 120s. A fadeaway release is not pinned to a timestamp. A full-height crop of 720p is about 2.7x.
- Do not use the Legion Hoops buzzer wide (1044x578) or Dave McMenamin's intentional miss. Notes: `src/FINDINGS.md`.

## QA checklist (before "ready")
- [ ] Frame 1 shows a LeBron **miss** (not a make)
- [ ] Every number heard correctly (`voice_check.py`)
- [ ] No footage shown twice; no scorebug naming the wrong era/team on "October 2024" (Lakers, vs MIN)
- [ ] Cards readable, with a source line
- [ ] `qa_short.py` PASS; watch sheet; Critic v2 PASS; the owner's listen

## Voice (Oct 15, 2026, overnight): two takes exist, none chosen
The "Voice direction" above (clone, speed 1.15) is superseded by `Tools/voice_config.json`. Per the owner's Oct 15 test brief, the approved script was voiced once in Alex (`_v1/`) and once in pham v2 (`_v1_F/`). Numbers and the A/F reading: `VOICE_AB (Oct 15, 2026).md`. Spend 952 characters; 2,596 left.
- **Next action:** the owner picks A or F by ear. Then `anchor_shots.py` on that folder's `words.json`, cut the Kobe clip (see PC footage above), add the ~0.2 s beat before "No." at assembly, trim Alex's tail if A.
- Not rendered, no QA yet. The shot plan above still needs frame 1 = the LeBron miss (the LADEig airball is the only one in hand).
