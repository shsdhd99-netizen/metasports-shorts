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

## QA checklist (before "ready")
- [ ] Frame 1 shows a LeBron **miss** (not a make)
- [ ] Every number heard correctly (`voice_check.py`)
- [ ] No footage shown twice; no scorebug naming the wrong era/team on "October 2024" (Lakers, vs MIN)
- [ ] Cards readable, with a source line
- [ ] `qa_short.py` PASS; watch sheet; Critic v2 PASS; the owner's listen
