# v6 (2026-10-03): vine boom removed, music A/B

- The `boom` effect on "92%" is gone (it clashed with the voice). Remaining effects: cha-ching on the salary card, click on the contract card and the ESPN quote, camera shutter on the Jaylen presser.
- `assemble.py` now mixes music: `--music <file>`, `--music-db -21` (level under the voice), `--music-start <s>` (default: the loudest steady stretch). The music ducks a few dB whenever the voice speaks and the whole mix is held at -14 LUFS.
- Versions: `final.mp4` (no music), `final_music_yuke.mp4` (yuke instrumental, from 0:26), `final_music_raws.mp4` (EsDeeKid "4 Raws", from 0:14).
- Risk: both tracks are commercial songs. YouTube can claim them (Content ID): the Short may be muted, restricted or lose monetisation. Test one at a time, and check the Studio "copyright" tab. YouTube's own Audio Library tracks are the safe fallback.
- How to judge the test: post a music version and a no-music version on DIFFERENT Shorts of a similar type at the same time of day, then compare "Viewed vs Swiped Away" and average % viewed at 24-48 h. One test is noise: repeat 3 times before deciding.
