# #48 "Who Has Missed The Most Threes Ever?" (James Harden): THE #42 FORMAT, first post of the voice A/B

**Status (Oct 19, updated 11:45 UTC): EDITED DRAFT, QA PASS, awaiting the owner's approval. Not posted.**
- File: `DRAFT - awaiting approval - 48 Harden most missed threes (no music).mp4` (23.5 s). Upload package: `UPLOAD.md`. Every clip verified by eye: `sources.csv`, `_audit/final_frames.jpg`.
- Footage: official NBA.com team-site uploads at 1280x720, found through NBA.com's public content index (see `Tools/nba_videos.py`). Frame 1 is the miss: Harden's step-back three at the Knicks (Jan 23 2019), contested by Mitchell Robinson, then the same play at half speed.
- Narrated in both A/B voices, both passing the voice gate:
  - `_voice_alex/` (Alex v2): 23.5 s, HNR 9.0, pitch variety 5.32. **Used in the draft (A/B slot 1 = Alex).**
  - `_voice_designed/` (Designed Narrator v4): 23.6 s, HNR 9.3, pitch variety 5.02, stretched x1.30.

## Script v2 (`script.txt`; v1 is in `script_v1.txt`)
> James Harden has missed more threes than anyone in NBA history. 5,933. And he's made more threes than anyone except Steph Curry. Second in misses is Curry: 5,825. In one season, Harden took 1,028 threes. The most ever. So is he a bad shooter? No. Harden makes thirty-six percent from three. LeBron makes thirty-five. Harden just shot more threes than anyone not named Curry: 9,323.

## Fact check (Basketball-Reference, read Oct 17 and 19, 2026; regular season, before 2026-27)
| Claim | Source | Check |
|---|---|---|
| Harden: most missed threes, 5,933 | 3PA 9,323 − 3PM 3,390 (https://www.basketball-reference.com/leaders/fg3a_career.html , /fg3_career.html) | PASS |
| He has made the most threes except Curry | 3PM: Curry 4,248 (#1), Harden 3,390 (#2) | PASS |
| Curry is second in misses, 5,825 | 10,073 − 4,248 | PASS. Next after him: LeBron 4,929 |
| 1,028 threes in one season, the most ever | https://www.basketball-reference.com/leaders/fg3a_season.html : Harden 2018-19, 1,028, #1 | PASS |
| Harden 36% from three; LeBron 35% | 3,390 / 9,323 = 36.4%; 2,636 / 7,565 = 34.8% | PASS (rounded: 36 and 35) |
| More attempts than anyone but Curry: 9,323 | 3PA #2 | PASS |

**Shelf life:** Curry adds about 1.5 more misses per game than Harden, and the gap is 108. Re-check the counts before posting after about Dec 1 (the season starts Oct 20-21).

## Footage (edit to the #42 spec: frame 1 = the bad thing; 11-13 shots of about 2 s; words over footage; no cards)
**What the cloud found:** NBA.com team-site videos, pulled at **1280x720** by swapping `_320x180` for `_1280x720` in the CDN file name (see `src/`):
- `harden_pacers_0405.mp4`: Cavs vs Pacers, Apr 5 2026, 185 s
  - Harden close-ups at **12.4 s**, **79.3-80.2 s** (a "3-POINTER" graphic) and **151.1-151.7 s** (celebrating with the coach)
  - the rest is wide
- `harden_pistons_g5.mp4`: Cavs at Pistons, May 13 2026, 145 s, all wide
- `curry_downtown.mp4`: Curry deep three, Dec 25 2024, 39 s
- `curry_lookaway.mp4`: Curry look-away three, Oct 14 2023, 12 s

**Why I didn't render:**
- In the wide shots Harden is about 60 px tall after a vertical crop of a 720p source (a 2.67x blow-up), and I can't confirm it's him on most plays.
- No clip of Harden **missing** a three was reachable (YouTube is blocked here, and X has no search here).

**PC list** (YouTube: NBA, Cavaliers, Rockets channels; these searches should each return official uploads):
1. **Frame 1 (must have):** Harden missing a three, a rim-out or airball, close or medium shot (e.g. NBA "James Harden misses" in a game recap or playoff loss).
2. Harden step-back three, 2018-19 Rockets (the 1,028 season): "James Harden step back three Rockets 2019".
3. Curry three plus celebration: `src/curry_*.mp4` already works.
4. LeBron three (Lakers/Sixers): for "LeBron makes thirty-five".
5. Harden close-ups: `src/harden_pacers_0405.mp4` at 79.3 s and 151.1 s.

**Words over footage:**
- "5,933" on the miss
- "1,028 IN ONE SEASON" on the Rockets clip
- "36%" / "35%" on Harden / LeBron
- "9,323" on the last shot

**Effects:** a pop per number, a riser into the flip. No music decision here (the owner's tracks are on the PC; log yes/no).

## Critic (self-review, Script Critic v3 + format gate)
| Premise | Hook | Clarity | Progression | Payoff | Voice | Visual | Originality | Retention | Total | Accuracy | Format |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 4 | 5 | 4 | 5 | 4 | 4 | 3 | 4 | 4 | **37/45 APPROVE** | PASS | FITS |
