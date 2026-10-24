# Unposted frame check — Oct 10, 2026

Inspection only. No assemble, voice, overwrite, commit, or upload. Frames are in `C:\Users\Admin\AppData\Local\Temp\audit-frames2\`. Durations are from ffprobe. Timestamps below were grabbed with `-ss` after `-i` so the frame matches the clock.

## Part A — Jokic / Westbrook swaps

Voice file: `_v2\words.json`. Current picture map: `_v2\shots.json`.

"two hundred nine" is spoken 1.245–1.797s. That sits inside the `12_wface.mp4` shot that runs 0.65–2.85s (in 0.70). That file is a face crop. OKC is on the chest. The 0 is not in frame for that hold.

"one ninety-eight" is spoken 4.750–5.221s. That sits inside the `07_jback.mp4` shot that runs 3.89–5.96s. The name and 15 are on the jersey, but the clip is a hallway and then a photo curtain.

### Recommended swap — "two hundred nine"

| | |
|---|---|
| Anchor | two hundred nine |
| Clip | `04_wopen` |
| in | 1.80s |
| Readable | Red back. Number 0 is readable from the cut. Full WESTBROOK plus 0 is readable from about 2.0s through 3.15s. Same person the whole way. |
| Clip duration | 3.200s |
| in+2.5 inside? | No. 1.80+2.5 = 4.30, past the end. Longest hold is 1.40s (ends 3.20). |

Do not start earlier than 1.78s. At 1.75s the file is still the Wizards front, number 4, name not readable. That is a different shot.

This is the only compiled clip that keeps Westbrook's name or 0 on one person without a later cut. It does not meet a 2.0s hold. Nothing else in the folder does.

Rejected for this line:

- `12_wface` (3.000s). Current shot. Face crop. 0 never stays in frame.
- `11_wlay` (3.200s). Blue WESTBROOK and 0 are readable about 0.55–1.25s, then at 1.40s it cuts to a different wide play. A 2s hold leaves that person.
- `15_wred` (3.000s). Red OKC 0 is one short look around 0.5–0.9s, then a different white uniform. Not 2s.
- `16_wdunk` (3.000s). Orange 0 on the dunk, then a face interview at 1.43s. Not 2s, and it leaves the jersey.
- `06_wret` (3.200s). Number is 4, not 0. The name is not held for 2s.
- `05_wdrive` (3.200s). The 0 shows up late and blurry, under a second, not a clean read.

### Recommended swap — "one ninety-eight"

| | |
|---|---|
| Anchor | one ninety-eight |
| Clip | `10_jwalk` |
| in | 0.00s |
| Readable | Navy Nuggets jersey. DENVER and 15 are readable from 0.00s through 1.40s. By 1.50s he has turned and 15 is no longer a full read. Same walk, not a cut. Locker room, not the hallway and not the curtain. |
| Clip duration | 3.200s |
| in+2.5 inside? | Yes. 2.50s is inside. At 2.50s the back reads JOKIĆ and 15. Still him. |

The clean front read is about 1.4s, just under a hard 1.5s. The back name and 15 are readable again from about 2.20s to the end (about 1.0s). No game clip in this folder holds 15 or the name for 1.5s without leaving him.

The spoken words land 0.86–1.33s into the current shot. With in 0.00, that is still the front DENVER 15.

Rejected for this line:

- `07_jback` (3.400s). Current shot. JOKIĆ and 15 are readable the whole file, but it is the hallway, then the curtain.
- `02_jside` (3.200s). Game. NUGGETS and 15 are clear at 0.15s and 0.70s, gone by 0.95s. Under 1s.
- `01_jhook` (3.400s). Back JOKIĆ and 15 about 0.40–1.15s, then he turns. Front NUGGETS 15 returns after a cut at 2.03s and does not last 1.5s before the file ends.
- `08_jnug` (2.800s). JOKIĆ and 15 about 0.15–0.65s, then a coach at 0.85s. Different person.
- `09_jast` (3.200s). 15 slides across a face crop, clear at 1.60s, cropped by 1.90s. Cut at 2.13s to another player.
- `03_jpost` (2.600s). Jokic does not hold a readable 15, and the file cuts to other players, including a Rockets 15 and a Nuggets 11.

## Part B — other unposted exports

Lottery v3 in folder 27 was not graded.

### Hart v2 — REJECT

`2026-10-04 28 Hart Added One Extra Line\READY TO POST - Why Hart Added One Extra Line (v2).mp4`

Duration 22.229s.

- 0.2s: Jalen Brunson on the SNL set. The caption says he hosted. The picture is the host, not the extra line.
- 8.0s: Josh Hart's face at a Knicks microphone. The caption is his name.

The unusual fact is the extra sentence, that Brunson has no future in acting. That sentence is only in the captions. The pictures are the SNL stage, a trophy parade, and Hart's face. A clip swap cannot show that sentence. Footage cannot show the fact.

### Bronny v3 — REJECT

`2026-10-04 23 Why Is Bronny Staying Without LeBron\READY TO POST - Why Is Bronny Staying Without LeBron (v3).mp4`

Duration 26.730s. Third Bronny. No polish.

- 0.2s: Lakers number 9 at the rim, another player in white. Caption "SIXTEEN LAKERS." The 16-versus-15 count is not in the picture.
- 8.0s: Bronny at the podium. The nameplate reads Bronny James Jr. The quote is only in the caption.

### Height gap — REJECT

`2026-10-04 26 The One-Second Height Gap\READY TO POST - The One-Second Height Gap.mp4`

Duration 24.533s. Second height short after Flagg. No polish.

- 0.2s: a very tall All-Star player beside a much shorter staff member. A gap is visible. Caption "21 INCHES." Kawamura is not in the frame.
- 8.0s: a close side of the shorter player. Caption "FOOT SEVEN." No comparison in the frame.

The two players are never in one frame, so the 21-inch pair is not visible without the caption.

### Free throw — REJECT

`2026-09-29 02 Is the Free Throw Line Lying\READY TO POST - Is the Free Throw Line Lying (Claude cut).mp4`

Duration 26.645s. No polish.

- 0.2s: overhead of a shooter near the key. The rim is barely at the top edge. No glass. Caption "EVERY NBA."
- 8.0s: the rim and net, with the glass edge circled. The players are under the basket, not a shooter at the line. Caption "OFF THE GLASS."

A later rulebook page and a 15-foot diagram state the measurement as graphics. No frame contains the rim, the glass, the line, and the shooter together.

### Giannis trade — REJECT

`2026-10-01 04 Did the Bucks Win the Giannis Trade\READY TO POST - Did the Bucks Win the Giannis Trade (Claude cut).mp4`

Duration 21.833s. Contract premise. No polish.

- 0.2s: Giannis's face, Bucks 34. Caption "The Bucks traded." The return is not in the picture.
- 8.0s: the draft podium. Caption mentions a pick swap. The 2031 and 2033 delay is not on screen.

### No export

- 05 Are the Sixers a Superteam Now
- 06 Why Is the Corner Three Shorter
- 07 SGA Just Joined a 14-Man Club
- 08 Is Kyrie Still Kyrie
- 09 Did the NBA Do This on Purpose
- 10 53 Years for One Banner
- 30 Why A Heave Miss Is Free
