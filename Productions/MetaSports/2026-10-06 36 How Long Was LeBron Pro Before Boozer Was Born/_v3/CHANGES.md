# #36 v3: rebuilt with sharp footage (Oct 15, 2026, PC)

Same approved script and voice A (Alex, `_v2` take, copied unchanged: no new voice credits). Replaces v2's unofficial fan-account clips. Twin voice F (`_v2_F`) was not rebuilt.

## What changed vs v2
- **Rookie LeBron:** both rookie shots now come from the NBA's own "LeBron James BEST NBA Rookie Highlights | 2003-2004" (`EEq1n6yJGfc`, 1280x720): the reaction at 178.0 s (hook) and the fast break at 173.47 s slowed 1.1x. No channel bug, no combing. Frame-checked.
- **Cameron Boozer:** four shots from the NBA's Summer League post (`2076009196248596739`); Duke dunk and Carlos in the stands from ESPN's post (`1985911140497424619`).
- **LeBron 2007:** the three "2007" shots are from NBAHistory's Eastern Conference Finals G5 reel (`1531650124266496001`, 640x640): **the ECF, not the Finals**. The v2 clips (a Duncan hug with another creator's captions burned in) were dropped. No sharper Finals source was found: the YouTube Finals reuploads are wide shots with a watermark. The line says "NBA Finals"; the owner should decide whether to keep it over ECF footage.
- **Cards:** three new navy cards (`shots_src/mk.py`), numbers kept above the caption band: 75 starts, 34 days, YEAR 24.
- **Sixers media day** shot kept (Sixers post `2104593268793041172`).

## Checks
Footage log `sources.csv` (all 15 clips verified by eye). `qa_short.py --full`: only FIX is the mono-downmix audio false alarm (see `Research Notes/Editing Practice Log (Oct 15, 2026).md`); real true peak -2.0 dBTP, -14 LUFS, 21.5 s. Warnings accepted: 640x640 and 720p sources blown up 2.7-3.0x (no better source); two LeBron 2007 shots are soft and busy; card at 3.5 s; cards 26% of the length.

## Not done
No music (none planned), no effects, not listened to. Needs the owner's OK before posting.