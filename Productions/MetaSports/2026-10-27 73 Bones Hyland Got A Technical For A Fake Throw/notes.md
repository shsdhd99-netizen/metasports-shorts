# #73 Bones Hyland got a technical for a fake throw (moment), built Nov 1, 2026

**Status:** rendered, full QA PASS, DRAFT awaiting approval, not posted. The package is in UPLOAD.md (post the music version).
_History: the script was recovered on Oct 27 from the NBA daily run. It wasn't voiced then (no ElevenLabs key in that session, and the Oct 26 scout footage was gone). The pick was scout #1 (`Research Notes/Daily Research/2026-10-26 overnight scout.md`)._

- **Lane:** a moment you can watch (a rule oddity on camera), built to the Oct 26 rules plus rule 11, real audio on a viral moment.
- **Concept (8 words):** a fake throw at the ref earns a technical.
- **Added value (what the clip alone can't show):**
  - who it is;
  - the score and clock (Wolves up 25, under two minutes left);
  - the ref's warning came before the second fake;
  - the two were chatting again while Toronto shot the free throw.
- **Script change at build:** line 1 lost "just". The game was Oct 25 and this posts a week or more later, and Lessons Learned says to write time-free wording. Line 1 is 9 words.
- **Music test:** #74 (posting Sunday) is the no-music side, so #73 is the **music** side.

## Claims and sources
| Line | Source | Exact words / data |
|---|---|---|
| Bones Hyland got a technical for a fake throw | Yahoo Sports / The Big Lead, "Bones Hyland shocked by technical foul after playfully menacing referee" https://sports.yahoo.com/articles/bones-hyland-shocked-technical-foul-132004283.html (read Nov 1) | "Hyland grabbed the ball and cocked his arm back like he was going to throw it at the official ... Fraher blew his whistle and called a technical foul." |
| The Wolves led Toronto by 25 with under two minutes left | The scorebug in the clip; Yahoo | TOR 89 / MIN 114, 4th, 1:47 to 1:38 (114-89 = 25); "With under two minutes remaining in the fourth quarter". Final 117-94 (Yahoo; Heavy https://heavy.com/sports/nba/minnesota-timberwolves/timberwolves-bones-hyland-punished-ref-making-joke/) |
| Bones got called for a foul, grabbed the ball and cocked it back like he'd fire it at the ref | Yahoo | "Hyland jogged back on defense and was called for a foul on a half-hearted shot contest. That's when Hyland grabbed the ball and cocked his arm back like he was going to throw it at the official." |
| The ref said something. So Bones did it again, grinning. | Yahoo | "referee Pat Fraher said something and Hyland, with a huge smile, cocked his arm back again." |
| Whistle. Technical. | Yahoo | "This time, Fraher blew his whistle and called a technical foul." The broadcast lower third reads "BONES HYLAND TECHNICAL FOUL". |
| His eyes went huge. | Yahoo | "His eyes are huge. His smile even bigger." (the replay shows it) |
| While Toronto shot the free throw, he and the ref were already chatting, all smiles | Yahoo | "Fraher was only briefly annoyed ... the pair immediately went back to having a good-natured conversation while the Raptors shot the technical free throw." The clip shows Fraher smiling, then laughing behind his hand. |
| LIVE: "You can't be mad at Bones." | The broadcast call in the clip, at 30.6-31.9 s of the post | Local speech-to-text (faster-whisper small.en, 4 runs, with and without cleanup) heard the same words every time, followed by "There's just no way." Earlier in the clip the same commentator says "Pat Fraher's laughing about it", but the runs disagreed on its last word ("it"/"us"), so that line isn't used. |

The referee is Pat Fraher (Yahoo; the scout file also cites the ESPN box score https://www.espn.com/nba/boxscore/_/gameId/401909864). The narration only says "the ref".

## Footage
- **The only source:** https://x.com/MrBuckBuckNBA/status/2114573587965444188. MrBuckBuck, Oct 26 2026 04:23 UTC: "Bones Hyland receives a tech for jokingly pretending to throw the ball at ref. His facial expression after it was hilarious". It's 54.7 s at 1280x720, the game broadcast unedited (live and replay; the replay wipe shows a DAZN logo). Saved as `src/2114573587965444188.mp4`.
  - This is a highlights account, not the league, so the licence risk is like any broadcast clip, and higher with the live audio.
  - Yahoo and Heavy embed this same post.
- **Searched with no clip of the moment found:**
  - Timberwolves and Raptors team sites on NBA.com (`Tools/nba_videos.py`: the Wolves site for game 0022600115 has 14 per-play clips, none of the technical; the Raptors site has only game highlights and pressers; also searched Bones' player id and "technical").
  - X / web searches for NBA, Timberwolves, Raptors, ClutchPoints and Bleacher Report posts.
  - Only fan reposts turned up (e.g. @maplewedgie, 9 s), plus a Fox "Wake Up Barstool" segment.
- **Shots** (all from the post above; every row is logged and verified in `sources.csv`; second = second of the post):

| Clip | Post seconds | Shows | Line |
|---|---|---|---|
| B01 | 43.85-46.1 (replay) | Bones cocks the ball back over his head, eyes wide, then grins | line 1 (frame 1) |
| B02 | 0.0-3.3 (live) | wide, scorebug TOR 89 / MIN 114, 1:47; words over the play "WOLVES UP 25" | up 25 |
| B03 | 8.6-10.7 | the foul at the rim; the clock stops at 1:38; #8 ends up with the ball | called for a foul |
| B04 | 16.6-18.6 | live tight: HYLAND 8 cocks the ball by his head, turns grinning | cocked it back |
| B05 | 25.45-26.4 | Fraher talking to him at the sideline | the ref said something |
| B06 | 45.1-45.9 at 0.5x, `"replay": true` | the key second again, slowed: arm cocked, grinning, the ref with his whistle in | did it again, grinning |
| B07 | 46.1-47.1 | the ref, whistle in mouth, then pointing; words "TECHNICAL" | Whistle. Technical. |
| B08 | 47.5-48.9 | Bones' wide eyes, ball in hand | eyes went huge |
| B09 | 34.1-35.2 (live wide) | a Raptor shoots the technical free throw | Toronto shot the free throw |
| B10 | 28.2-30.5 | Fraher smiling face to face with him, then laughing behind his hand | already chatting, all smiles |
| B11 | 50.0-51.8 (replay), sound from 30.48 | Bones grinning, hand on chest; LIVE call "You can't be mad at Bones." | the ending (live) |

## Build
- **Voice:** Alex, 1 take (passed the gate: HNR 7.6, jitter 2.79, shimmer 10.63), then `tighten_voice` (0.25/0.12). The narration runs 18.0 s.
- **Real audio:** `nat_sound.py --burst 18.10-19.58 --tail 0.15 --bed-db -20 --clip-db B06=-32`. The bed is lower than the usual -15 because the clip's commentary is unrelated chatter. B06 is held at -32 so a murmur of the commentator doesn't play under the replay.
- **Music:** `music.json` uses eleven_stats_01 at bed -20 LU, with a drop at 18.08 for 1.8 s under the live call.
- **Effects:** a whoosh into the slowed replay and a whistle on "Whistle."
- **Files:**
  - `final.mp4` (no music, real audio) is `final_vo.mp4` plus nat_sound.
  - `final_music.mp4` (music, real audio) is `final_music_vo.mp4` plus nat_sound.
  - `final_narrated.mp4` (music, no broadcast audio) is the spare. Its inputs are kept as `_*_narration.*`.
- **QA:** `qa_short.py --full` PASSES on all three.
  - Warnings left: the hook word, music not yet approved by ear, one 0.28 s caption ("he and the"), and speech-to-text heard "fired" for "fire it".
  - True peak -3.5 / -3.9 dBTP; -14.1 / -14.0 LUFS.
