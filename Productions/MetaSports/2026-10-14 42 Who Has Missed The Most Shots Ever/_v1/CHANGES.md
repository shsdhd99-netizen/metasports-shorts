# #42 v1, voice A (Alex), Oct 15, 2026: RENDERED

One take, approved script unchanged. Twin `_v1_F/` is pham v2 (not rendered). Owner chose Alex on Oct 15.

## Build
- `final.mp4` 23.5 s, 1080x1920, -14.0 LUFS, true peak -1.9 dBTP, no music. `final_nocap.mp4` is the same without captions.
- 10 sources (`sources.csv`, all verified by eye): X post (LeBron airball, 1080x1920), NBA official YouTube: record night (E5JBSJa4flo), Oct 22 2024 Bronny game (Vf03Sl7vNDA), Kobe video (lk5o2PK76hs, 720p, 2.67x blow-up, nothing sharper exists), plus two own cards (`shots_src/mk.py`, Basketball-Reference).
- Shots (see `shots.json`): airball in two visits (push-in), LeBron record, Kobe x2 (under "14,481 misses"), LeBron+Bronny bench and court, LeBron face, FG% card, LeBron smile, 31,502 card (two steps: LeBron, then Kareem 28,307).
- Sound: one whoosh into the FG% card. No rim sound anywhere (frame 1 is an airball). The boom on 31,502 was tried and dropped.

## Fixes made while building (what the render taught)
- Card numbers first sat in the caption band (about 55-65% of the height) and collided with the captions: all card text now stays above y=1040.
- A Kobe clip ran into an interview cut (Dirk Nowitzki) at its end: cut shorter, split into two Kobe visits.
- A LeBron close-up ran into a different player (OKC #6): the clip is trimmed to the first 1.35 s of its shot.
- A "bench" frame showed a Wolves player instead of LeBron: re-cut.

## QA (`qa_short.py --full`, Python 3.12)
Everything passes except one FIX: "7 clipped runs at full scale". **False alarm:** the check mixes stereo to mono, and L and R are correlated, which adds 3 dB. Measured directly: left and right peaks -1.99 dBFS, 0 samples above 0.999, EBU R128 true peak -1.9 dBTP.
Warnings kept on purpose: Kobe clips are 2.67x blown up and soft (no better source); frame 1 is a wide shot (LeBron small); pace 163 wpm counts digits as one word.
The speech-to-text check was skipped (the Python that has faster-whisper lacks cv2, and the other way round). Captions match the script word for word.

## Not done
Music test, keyframe push-ins other than the two on the airball, owner's ear.