# DEMO - editing upgrade (#73 re-cut, Nov 3 2026). Never swap onto the live Short.
Built by `python Tools/edit_upgrade.py --folder <#73 folder> --demo <this folder>` (voice, words, captions reused). qa_short --full PASS; edit_lint clean (was 4 flags).
Changes: B02 (wide hook) zoom 1.5 and split into B02 + B02b (3.63 s -> 1.8 + 1.8 s, second at zoom 1.75); B03 and B04 whole frame so the scorebug is whole.
Tradeoff seen on the contact sheet: whole-frame B03/B04 keep the bug but Bones is small there; a close-up angle would fix both and needs another source.
B01 is a close-up, so it is left alone (zoom 1.5 cropped his face; the tool now only zooms shots whose note says wide).
Source video (src/) and clips are not committed; re-download with x_clip.py (status 2114573587965444188).
