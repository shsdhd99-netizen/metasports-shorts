# #79 Two buzzer-beaters from 40 and 50 feet, 20 minutes apart (Oct 29, 2026; daily NBA build)

- **Lane:** moment (a skilful/odd thing you can watch), real-audio arm (both live broadcast calls).
- **Concept (8 words):** Two long buzzer-beaters, then their box scores' punchline.
- **Added value (facts the clips can't show):** the two shots were 20 minutes apart (ESPN play-by-play wallclock); Jović played only 7 minutes all game; Edgecombe went 1 of 6 from three, so his only make was the 50-footer (ESPN box scores).
- **Copy check:** no competitor in the newest 15 (18 watchlist channels) has it; `copy_check.py "two half court buzzer beaters"` matched only an old 1984 Short (a different story).
- **Slot:** Fri Oct 30, second NBA post (about 2 PM ET, 6+ h after #74). It's a Wednesday-night moment, so the script says "on Wednesday", not "last night".

## Claims and sources
| Line | Source | Exact data |
|---|---|---|
| Buzzer-beaters from 40 and 50 feet on Wednesday | ESPN play-by-play, games 401909881 (MIA @ ATL) and 401909884 (PHI @ IND), Oct 28 2026 | "Nikola Jovic makes 40-foot three pointer" (2nd, 0.1); "VJ Edgecombe makes 50-foot three point jumper" (2nd, 0.2) |
| Twenty minutes later | same, play wallclock | Jović 2026-10-29T00:02:58Z; Edgecombe 2026-10-29T00:23:07Z (20 min 9 s) |
| Loose ball, one second left in the half | Hawks/Heat broadcast call on the clip | "Jovic has a loose ball, a second left in the half, he got it, and that one does count." |
| In Indiana | ESPN scoreboard | 76ers 114, Pacers 109 at Indiana |
| Edgecombe grabs a rebound with a second left | the clip (scorebug 1.7 → 1.4 as he gathers) and the ESPN call | "Ubre tries a three, well short, rebound, Edgecombe, gonna get a chance, half-court, that'll count if it goes. Oh, Edgecombe nails it at the buzzer." |
| Jović played seven minutes all game | ESPN box score 401909881 | Nikola Jovic: 7 MIN, 5 PTS, 2-2 FG, 1-1 3PT |
| Edgecombe went one for six from three; his only make came from 50 feet | ESPN box score 401909884 | VJ Edgecombe: 29 MIN, 8 PTS, 3-10 FG, 1-6 3PT |

Note: the NBA's post says Jović's shot was "from half court"; ESPN logs it as a 40-foot shot (half court is 47 feet), so the script says 40 feet. The heave rule (2025-26) counts missed end-of-quarter heaves from 36+ ft as team attempts; made ones count for the player, which is why Edgecombe's 1-for-6 includes this make.

## Footage
- **ESPN clips** (public ESPN video, Oct 29 2026): "Nikola Jovic buries 3-point shot vs. Atlanta Hawks" (21 s; the shot, Heat bench, Jović with teammates) and "VJ Edgecombe buries the half-court buzzer-beater" (32 s; the shot, a replay, a floor angle, a behind-the-shooter close-up with his arms up). Both carry the broadcasts' own calls.
- **NBA on X:** [Jović](https://x.com/NBA/status/2115597137949982921) (8.1 s) and [Edgecombe](https://x.com/NBA/status/2115602130547433870) (11.5 s), the same broadcast pictures; kept as backups.
- Rights: league/broadcaster footage, short shots; the real-audio version plays about 10 s of the two broadcast calls (Content ID risk is higher than footage alone: the narrated version is the fallback).
