# #36 rookie-LeBron footage check (Oct 15, 2026, overnight)

**Owner's rule (Oct 15):** footage may come from any account. Keep a clip when it is sharp and shows the right player, uniform, game and action. Reject it when it is soft, watermarked or the wrong moment. "That approves #36's rookie-LeBron clip if a frame check shows LeBron in the 2003-04 Cavs uniform and the picture is not soft."

**Result: the NBACobwebs clip is NOT approved. It fails the "not soft" half. A sharper official source passes all of it, and two cut-ready clips are in `_rookie_candidates/`.**

## 1. The NBACobwebs post (`x.com/i/status/2019099383988711856`), the source of v2's `l2bg` and `k2bg_df`
Downloaded again on this PC to `src/2019099383988711856.mp4` (960x720, 10.25 s). Post text: "NBA Cobwebs - February 4, 2004: Cleveland rookie LeBron James with a breakaway dunk...". I looked at native-resolution frames every 0.5 s.

| Check | Result |
|---|---|
| Right player and uniform | Yes from 4.4 s: LeBron in the white Cavs home jersey with the wine "Cavaliers" script, headband, #23 (legible on the rim-cam dunk at 6.5-7.0 s). Opponent is the Lakers (Derek Fisher #2 at 7.8 s). |
| Not soft | **No.** SD interlaced source: combing lines on the dribble frames, the "Cavaliers" script is a smear and "23" is barely readable at 5.0 s, pink colour cast in the middle section, compression blocks. |
| Watermark / bug | **Two network bugs:** "ESPN Classic" top-right (0.5-3.5 s and 7.5-10 s) and "PREMIERE" top-left (about 3.7-7.2 s). |
| Right moment | The first 3.5 s are blurred wide shots where no player can be identified. That is where v2's hook frame (`l2bg`, "frame 1 = rookie LeBron") would sit. |

Correction to `_v2/sources.csv`: it describes `l2bg` as "driving vs Boston, FOX broadcast". For this post that is wrong (the opponent is the Lakers; the bugs are ESPN Classic and PREMIERE). I did not edit the v2 file; the right description is in `_rookie_candidates/sources.csv`.

## 2. The sharper source: the official NBA video "LeBron James BEST NBA Rookie Highlights | 2003-2004 NBA Season"
`https://www.youtube.com/watch?v=EEq1n6yJGfc` (NBA, 3:02, 1280x720, a 4:3 picture pillarboxed). Downloaded to `src/yt_EEq1n6yJGfc.mp4`. It is the same SD-era footage, but cleaner: no combing, no pink cast, and the lettering is readable.

Same-magnification crops of LeBron dribbling in the white jersey: in the NBACobwebs frame the "Cavaliers" script and the "23" are smeared; in the NBA frames at 174.0 s and 178.5 s the "CAVALIERS" script, the "23", the wine and gold trim, and faces in the crowd are all readable.

| Clip (in `_rookie_candidates/`) | Source seconds | Shows | Use in v2 |
|---|---|---|---|
| `rookie_A_fastbreak_173p47-175p47.mp4` (2.00 s) | 173.47-175.47 | LeBron #23 fast break against a Blazers defender, then rising for the dunk | the "teenage LeBron" slot (5.54-7.71 s), slowed about 1.085x to 2.17 s |
| `rookie_B_reaction_177p70-180p55.mp4` (2.87 s) | 177.70-180.55 | LeBron right after the dunk: face, headband, jersey, crowd | the hook slot (0-1.56 s): use clip seconds 0.3-1.9 (source 178.0-179.6). **Not the last 0.6 s:** a Blazers player crosses in front of him |

Both are one continuous broadcast shot each, with no scorebug and no channel bug in the picture. Picture area cut: 924x720 at x=190, native resolution, which removes the pillarbox and the dark edge fade. The two clips do not overlap, so QA's "footage shown twice" check will not fire.

**Game and season:** from on-screen evidence only. The shot just before clip A carries the FOX Sports Net scorebug "POR 74 CLE 84, 4th QTR", and the arena ribbon board in the same continuous shot reads "...Pacers Tuesday Dec. 30 at 7:00". So it is a Cavs-Blazers home game in December 2003, which is LeBron's rookie season in Cleveland. The exact date is not verified.

The video is from the official NBA account, so the account question does not arise.

## A measuring trap (so nobody repeats it)
My first sharpness comparison said the NBA video was 2.6x sharper than the Cobwebs clip. That compared a downscaled 1280-wide frame with an upscaled 960-wide one. Re-measured on equal footing (Laplacian variance, picture area scaled to 1080 wide), the Cobwebs windows scored **higher** (about 510-570) than the NBA windows (about 300-360). That number is wrong as a sharpness measure across different sources: interlace combing, noise and compression blocks add fake edge energy. Side-by-side crops at the same magnification settled it, and they show the opposite. `footage_qc.py`'s sharpness check compares shots against the same Short's median, so keep using it for that, but never to rank two different sources. Look at the pixels.

## What this does NOT do
- It does not re-render #36. The v2 clips, the three proof cards (`c_75`, `c_34`, `c_24`) and the other 13 clips are not on this PC (they live in the cloud container; the card maker `rc.py` is not in the repo). A re-render needs them re-made or fetched from the cloud copy. The voices are unchanged and still exist: `_v2` (Alex) and `_v2_F` (pham v2).
- It does not fix the other soft shots QA found in v2 (`a1_df`, `a1bj`: the 2007 LeBron close-up). That is still open.
- Not evaluated: two more downloads kept in `src/` in case a different angle is needed: the ESPN debut package (`yt_Ob5-nC8okpY.mp4`, 720p60) and an unofficial 1080p upload of the same Feb 4, 2004 Lakers game (`yt_Hs0oqRXA2kQ.mp4`).
- Nothing was posted or scheduled.

## Decision for the owner
Approve `rookie_A` and `rookie_B` as the rookie-LeBron shots for #36, in place of the NBACobwebs clip. If you would still rather use NBACobwebs, it needs the bugs cropped out and it will look soft.
