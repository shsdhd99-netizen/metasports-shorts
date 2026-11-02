# #92 This Rookie Told Luka He Sucks (built Mon Nov 2, 2026, main session)

**Status:** DRAFT, not posted. News from Sunday night: post Mon Nov 2 or skip. Today's two NBA slots were already scheduled by the owner's PC (#73 at 7:15 AM, #83 at 3:30 PM), so this is an optional swap for #83 (evergreen, can move to Fri Nov 6).

- **Lane:** news with a record and a revenge turn (versus a star; the trash talk is in his own voice).
- **Concept (8 words):** trash talk, humbled by 37, then scores 37.
- **Added value:** puts three games side by side (opener quote, Friday's box score, Sunday's record) with the same number, which no recap did.
- **Copy check:** FRESH ("Lendeborg Luka Doncic": top match 3.8K; "Lendeborg 37 points": 82 views).
- 19.1 s, Alex voice plus 1.8 s of Lendeborg's own voice, 12 shots, no cards. Full QA PASS on both versions; comfort audit clean (true peak -3.8 dBTP, loudness spread 2.2 LU).

## Claims (every line, with its source)
| Line | Source | Exact wording / value |
|---|---|---|
| In his first NBA game, Warriors rookie Yaxel Lendeborg went at Luka Doncic | AP via Newsday, Oct 22 2026; ESPN recap of game 401909092 | "The Golden State Warriors rookie began his career Wednesday night by refusing to back down from the reigning NBA scoring champion"; "a prolonged physical and verbal confrontation with Warriors rookie Yaxel Lendeborg, who got a technical foul" |
| "I was telling him, he sucks. He can't score on me." | Anthony Slater on X (x.com/anthonyVslater/status/2113137207389352120), 101 s soundbite, at 58.60-60.38 s | His own voice (Whisper on the cut). Sporting News quotes Slater's post: "I told him he sucks. He can't score on me." |
| Nine days later, they met again | ESPN schedule: Oct 21 opener, Oct 30 at Golden State (game 401909285) | 9 days |
| Lendeborg had 6 points and 5 turnovers | theScore (Oct 31), Basketnews (Oct 31) | "tallying six points and five turnovers"; "six points, five turnovers, and a minus-20" |
| Luka had 37 | Press Democrat / Bay Area News Group (Oct 30); theScore | "Doncic scored 37 while Lendeborg had a quiet six points"; "finished with a game-high 37 points" |
| Then, two days later, without Steph Curry | AP recap of game 401909905 (Sun Nov 1) | "in a game Golden State rested stars Stephen Curry and Draymond Green" |
| Lendeborg went off for the most points by a Warriors rookie since Steph himself. 37. | AP recap, same game; NBA on X (2117106779997753358) | "Rookie Yaxel Lendeborg scored a career-high 37 points"; "his points were the most by a Warriors rookie since Curry went off for 42 on April 14, 2010, at Portland" |
| The exact number Luka scored against him | the Friday line above | Luka's 37 came in a Warriors win (they came back from 25 down), so the Short never says Luka beat him that night |

Not used: Wilt/Rick Barry company (AP: "joined Hall of Famers Wilt Chamberlain and Rick Barry"), "wet the bed" quote (theScore, Basketnews); both true, cut for length.

## Footage
| Clip | What it shows | Source |
|---|---|---|
| L01 | Luka (#77) face to face with Lendeborg (#1, name on his back), Oct 21 | ESPN clip 50244788 "Luka Doncic lets Yaxel Lendeborg hear it after half-court buzzer-beater" (slowed to 0.7) |
| L02 | Luka celebrating that buzzer-beater | same clip |
| L03 | Lendeborg at the podium, Oct 21, lip-synced to his own audio | Anthony Slater on X |
| L04 | Fri Oct 30: Lendeborg (#1) on the floor as Luka attacks | ESPN clip 50332790 |
| L05, L05B | Lendeborg walking off (face), then from behind with LENDEBORG 1, Fri Oct 30 (slowed to 0.5) | ESPN package 50333448 |
| L06 | Luka arm up after a three, Fri Oct 30 | ESPN package 50333448 |
| L07 | Steph Curry resting in a hoodie, cheering from the bench, Sun Nov 1 | NBA on X 2117106779997753358 |
| L08 | Lendeborg's step-back three, Sun Nov 1 | ESPN clip 50355054 |
| L09 | Steph Curry (#30) after a three, Fri Oct 30 | ESPN clip 50333380 |
| L10 | Lendeborg close-up, Sun Nov 1 | NBA on X 2117106779997753358 |
| L11 | Luka close-up, Fri Oct 30 (slowed to 0.62) | ESPN clip 50332790 |

Overlays: "6 POINTS", "5 TURNOVERS" (red), "37 / LENDEBORG, SUNDAY" (green), "37 / LUKA, FRIDAY" (orange).
Fixes during the build: two one-frame flashes removed (L07, L08; originals in `_check/preflash/`); the hook clip slowed so it ends before ESPN's next camera shot; L05 split so "6 POINTS" sits on Lendeborg, not teammate #20; quote captions grouped into four phrases (QA flagged 0.2 s captions); a 0.25 s fade on the last sound.
Build: narration recorded first (`_script_narration.txt`, `_voice_narration.mp3`), then `_build_realaudio.py` opens a 2.02 s gap after "Luka Doncic." and `Tools/nat_sound.py --burst 4.135-5.915 --bed-db -18 --tail 0.06 --burst-lufs -13` plays his voice there.
