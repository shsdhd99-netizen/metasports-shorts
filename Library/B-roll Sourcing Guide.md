# B-roll Sourcing Guide (canonical; Oct 14, 2026; quality standard and QA tools added Oct 15)

This guide answers how we find, check, log and reuse footage for every Short.
- **What footage should do in a Short:** `MetaSports - Playbook.md` → Creative System v3, §5.
- **Why:** `Research Notes/Posted Video Audit (Oct 14, 2026).md`, section 10. Our old hits showed the exact moment under nearly every line and kept the broadcast scorebug as proof.

Evidence tiers: **[V]** verified on our own files or tests, **[S]** small-n support, **[H]** hypothesis, **[E]** external guidance.

## 1. The rules (they apply to every build)
1. **Opening visual first.** Secure the strongest real image of the subject doing the thing *before* the script is final. If you can't get it, change the angle or park the idea (Creative System v3 footage-first gate). [S: 4/4 old hits opened on the subject or the exact moment]
2. **Every line gets footage that proves it.**
   - Exact player, game, event, reaction or moment beats generic basketball.
   - Generic footage is allowed only under a "what if" line, and never with a scorebug or jersey that contradicts the line.
   - [S: the old hits put the exact moment under 8/11 and 11/13 of their shots; #39's stand-ins with another opponent's scorebug were a critic failure]
3. **The broadcast is your proof.**
   - When the clip IS the game being described, keep the scorebug and banners and circle the number when it's named (`broll.py circle`).
   - Crop the scorebug only when the shot is a stand-in. [S: Luka 126-125 / 1.5 s; Kobe 96-86 / "60 POINTS"]
4. **Vary with purpose.**
   - No clip shown twice except a deliberate loop or a marked replay. `qa_short.py` checks this.
   - Hold the payoff shot longest. [S]
5. **Check every frame that ships**, at 30 fps around every cut.
   - One-frame flashes come from a clip's first frame or its own internal cut. [V: #21's two flashes]
6. **Log everything** in `<production>/sources.csv`: link, account, date, in/out seconds, crop, what it shows, the line it sits under, verified yes/no.
   - QA FAILs a build whose log misses a clip or has an unverified clip.
7. **Quality standard (Oct 15):**
   - **The source must be 1080p or better.** A full-height vertical crop of a 1080p landscape broadcast is a 1.78x blow-up, and that's the house baseline.
   - Over 2.0x (a 720p source, or a tight crop) is allowed only when no better copy of that moment exists; say so in PACKAGE.md.
   - Over 3.0x fails QA.
   - **No upscaling pretence:** never run footage through an AI upscaler or sharpener and describe it as HD. A soft archive clip stays labelled as archive.
   - **No other creator's overlays,** watermarks, captions or channel logos in frame.
   - **No scorebug that contradicts the line** (rule 3).
   - `footage_qc.py` measures the blow-up from the logged source size, flags soft shots, and lists the source's own internal cuts.
8. **Never fabricate.**
   - No AI-generated footage of real players and no doctored images (#41 v1's pasted logo was rejected).
   - No game presented as another game.
   - If a moment can't be sourced, use an honest alternative (section 6) or flag the blocker.

## 2. The workflow, step by step (commands run from `Tools/`)
| Step | Do | Command / output |
|---|---|---|
| 1. Beats | Write the visual beats next to the draft script: the opening image, one image per claim, the payoff image | `notes.md` |
| 2. Search | Find posts of the exact moment (section 3 has the search patterns) | WebSearch `site:x.com ...` |
| 3. Download | Pull the posts into the production's `src/` (gitignored) | `python x_clip.py <post urls> --out "<folder>/src"` → `src/<id>.mp4` + `src/downloads.csv` (account, date, post text) |
| 3b. Best copy | When the same moment is posted more than once, keep the **original poster** (league or team over reposts) at the **highest resolution**. Compare candidates before cutting | `ffprobe -v error -select_streams v -show_entries stream=width,height,bit_rate -of csv=p=0 src/*.mp4`; the source size goes into the log automatically at the cut |
| 4. Preview | Contact sheet of each source to pick clean seconds. **For a long source, list its scene changes first:** frames with exact timestamps show where the source cuts, so no shot straddles an internal cut | `python broll.py sheet "<folder>/src/<id>.mp4" --every 1 --out sheet.jpg`; `python vendor/watch/scripts/watch.py "<folder>/src/<id>.mp4" --engine local --max-frames 40` (owner-supplied tool, Oct 15; YouTube URLs on the PC only; never with cookies; see `Tools/vendor/watch/README_METASPORTS.md`) |
| 5. Cut | 1080x1920 clip; keep or crop the scorebug per rule 3 | `python broll.py cut "<folder>/src/<id>.mp4" --at 3.2 --len 2 --x 0.5 --out "<folder>/clips/A1.mp4"` → writes the clip's `sources.csv` row automatically |
| 6. Circle | Red circle on the named detail (score, clock, shoe, hand) | `python broll.py circle clips/A1.mp4 --at 0.62,0.88 --out clips/A1c.mp4` |
| 7. Map | Shots to words (`anchor` in shots.json); fill "line" and "used at" in the log | `python anchor_shots.py ...`; `python footage_lib.py log "<folder>"` |
| 8. Verify | Look at the used part of every clip; record what it shows | `python footage_lib.py sheet "<folder>"` → `_audit/clips/*.jpg`; `python footage_lib.py verify "<folder>" A1.mp4 "Jokic #15 Nuggets, no-look pass vs Utah, Oct 4 2026 preseason"` |
| 9. Older clips | Recover the source post and second of clips cut before logging existed | `python footage_lib.py match "<folder>" --src <dirs of downloaded posts>` (0.80+ = match; 0.70-0.80 = "probable", confirm by eye) |
| 10. QA | `qa_short.py` warns if there is no `sources.csv`, and FAILs on a missing or unverified clip once one exists. `--full` adds the footage check (blow-up, softness, duplicates under other names, one-frame flashes, busy picture, internal cuts) and the export check (captions = script, caption timing and safe width, export speech vs script, timeline, clipping) | `python qa_short.py --folder "<folder>" --full`; footage only: `python footage_qc.py "<folder>" --json` → `_audit/footage_qc.json` |
| 11. Reuse | Index every clip of every production, then search before downloading again | `python footage_lib.py index` → `Library/footage_library.csv`; `python footage_lib.py search jokic pass` |

**What "verified" means:** you looked at the used seconds, **including the footage after any internal cut `footage_qc.py` lists**, and checked each of these against the line it sits under:
- the player (face, number)
- the uniform (team, home/away, era)
- the scorebug (opponent, score, clock, date if shown)
- the arena
- the season

Write what it shows, not what you hoped.

## 3. Where footage comes from (tested from this cloud machine on Oct 14, 2026)
| Source | What you get | Cloud access [V] | Rights and restrictions | Use it for |
|---|---|---|---|---|
| **NBA and team accounts on X** (@NBA, @NBAHistory, team accounts, team PR accounts, @NBAonPrime, ESPN) | game clips, reactions, press-conference bites, media day, graphics | **yes**, `x_clip.py` (yt-dlp). Search with `site:x.com NBA <player> <event>` | Owned by the NBA or the team. X's terms allow viewing and embedding, not re-uploading. Our use is commentary (fair use, see section 4). The same rights holder as the broadcast, so no extra risk | First choice for any moment from the last few years |
| **Reporters and highlight accounts on X** (e.g. Kevin O'Connor, House of Highlights, Bleacher Report) | fast clips of the night's moments | yes | They don't own the broadcast and may add their own edit or watermark. Use only the broadcast part; crop watermarks; prefer the league's own post of the same moment | When the league hasn't posted it yet |
| **TikTok** (official NBA and team accounts) | the same clips, often vertical | yes, through the browser (`watch_short.py <url>` keeps the mp4) | same as X | Vertical-native clips |
| **YouTube** (NBA, teams, press conferences, classic games) | full press conferences, classic games | **no from the cloud** ("sign in to confirm you're not a bot"). The owner's PC works (`broll.py cut <youtube id>`) | Same as above. Full classic games are often re-uploads: check the uploader | Press conferences, archive. Build on the PC or ask the owner for X links |
| **NBA.com** (video, stats) | stats pages, some video | **no** (403 from the cloud) | NBA owned | Stats screenshots from the PC; use B-Ref from the cloud |
| **Basketball-Reference, StatMuse, team sites** | stats, logs, schedules (screenshots for cards) | yes (`webshot.mjs`) | Factual data isn't copyrightable; the page design is. A screenshot quoted for commentary is low risk; name the source | Proof cards (the quote or number circled) |
| **Wikimedia Commons** | photos of players, arenas, historic scenes with stated licences (CC BY, CC BY-SA, public domain) | the API rate-limited us (429) once; retry later | **Attribution required** for CC BY/BY-SA (author, licence, link). Our no-description rule means the owner must allow a one-line credit in the description or pinned comment | Historic players with no usable video (Wilt) |
| **archive.org** | old newsreels, radio, some broadcasts | yes | **Not automatically public domain**: many items are uploads of copyrighted broadcasts. Use only items marked public domain or with a clear licence | Pre-1970 moments (#43 Wilt: the "100-point" item is radio only) |
| **Library of Congress, national archives** | public-domain photos | not tested | Mostly public domain (check each item) | Historic stills |
| **Getty Images, AP, Imagn** | licensed photos and archival video, the cleanest rights | not tested; paid | Paid licence per use | Only if a key moment has no other source and the owner approves the cost |
| **Our own cards** | number and quote cards, schedule cards | yes (`card.py`, `broll.py page`) | Ours | Proof of a number when no broadcast graphic shows it |
| **AI-generated video of real players** | — | — | **Never.** Fabrication and likeness risk | — |

**Search patterns that worked:**
- `site:x.com NBA Jokic behind the back pass Cam Johnson`
- `site:x.com Raptors Jamarion Sharp summer league`
- `site:x.com NBAHistory Kobe 60`
- `site:tiktok.com nba <player> <moment>`

Add the date or the opponent to narrow it. Official accounts first.

## 4. Copyright, licences and platform risk (practical, not legal advice) [E]
- **Publicly viewable is not free to reuse.**
  - NBA game footage, broadcast graphics and press conferences are copyrighted by the league, its broadcast partners or teams.
  - Our use relies on **fair use**: short excerpts inside new commentary that explains a fact.
  - Fair use is a defence judged case by case, not a permission.
- **What lowers the risk** (we already do all of these):
  - short cuts (≤2-3 s each)
  - our own narration and analysis over every clip
  - crops and edits
  - no broadcast audio commentary (clips are cut without audio)
  - no other creator's watermark
  - a sourced fact the footage illustrates
- **What YouTube can still do:**
  - Content ID can match NBA footage automatically. The usual outcome is a claim: the ad money goes to the claimant, or the video is blocked in some countries.
  - A manual takedown can give a copyright strike.
  - The source log is how to dispute a claim honestly.
  - **I can't see the channel's claims** (no Studio access). The owner should say if any Short got a claim, so the log can record which source caused it.
- **Do not:**
  - re-upload whole plays with the broadcast audio
  - use broadcast music
  - bypass access controls (we don't use YouTube workarounds; one was refused on Oct 14)
  - present a stand-in as the event
- **Photos with licences** (Wikimedia CC BY/BY-SA): keep the author, licence and link in `sources.csv`, and add the credit wherever the licence requires.

## 5. How it's organised
| Where | What | In git? |
|---|---|---|
| `Productions/<folder>/src/` | downloaded posts + `downloads.csv` | no (large); the log copies what matters into sources.csv |
| `Productions/<folder>/clips/` | cut clips | no (media stays out of git), except finished Shorts |
| `Productions/<folder>/sources.csv` | **the source log** (one row per clip) | **yes** |
| `Productions/<folder>/_audit/clips/*.jpg` | verification contact sheets | no (jpg) |
| `Library/footage_library.csv` | every clip of every production: what it shows, source, verified | **yes** |

## 6. When the key moment can't be sourced (honest alternatives)
1. **A verified photo** of the moment (official, Wikimedia with its licence) with a slow push-in.
2. **The proof as a card:** the box score, the quote or the schedule, with the source named.
3. **A related verified moment**, labelled by the line as what it is ("Here's Wilt in 1962" not "Here's the 100-point game").
4. **The subject's face** (media day, bench) under the line, with no claim it's the moment.
5. **Park the idea** and name the blocker in the queue (#42: footage of LeBron misses; #43: identifiable Wilt film).

## 7. Status of the logs (Oct 14, 2026)
- **#40, #41 and #21 have `sources.csv` files.**
  - Clips cut before logging existed were matched back to their posts by frame comparison (`footage_lib.py match`).
  - Clips matched at 0.70-0.80 are marked "probable".
  - Clips whose download is gone say so; the post-level sources are in each `notes.md`.
- **Older productions:** no logs yet. Run `footage_lib.py log` + `sheet` + `verify` before reusing any of their clips.
