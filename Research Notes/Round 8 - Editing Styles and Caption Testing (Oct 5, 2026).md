# Round 8 - Editing Styles and Caption Testing (Oct 5, 2026)
Scope: what the 30K-1M+ NBA Shorts of the last 60 days (window 2026-08-06 to 2026-10-05) look like, and a low-risk caption A/B plan for us. Tiers: PROVEN (measured by us, reproducible) / SUPPORTED / HYPOTHESIS. Nothing here was uploaded, committed, or built into assemble.py.

## 0. Method and honest limits (read first)
- Public metadata via yt-dlp (`--flat-playlist -J`, then `-j` with `--extractor-args youtube:player_client=mweb --ignore-no-formats-error` for upload date, duration, views). Channels: CoachClank (145K subs), CourtsideFilms (805K), NBA (24.5M), HouseofHighlights (17.7M), BleacherReport (5.06M), AhmedsBasketball (121K). Hoops Lore has no Shorts tab (yt-dlp error), so it is not covered.
- **Video download is blocked** (bot check on every client except storyboards). What worked: the **storyboard image (sb0, 101x180 px tiles, 1 frame per second)** via `-f sb0`. So frames at 0, 1, 2, 4 s (NOT 0.5 s) at thumbnail resolution; caption style, text position, framing, colour are readable, exact fonts and sub-second cuts are not. My automatic "cuts per second" metric saturates at 1/s (1 fps cannot see cuts faster than 1 s) and very short clips (7-15 s) used a different tile layout that my crop mis-split; **cut rate is therefore NOT measured (UNVERIFIED)**. Qualitative frames were reliable for 15 clips: CoachClank 6, Ahmed 3, BR 4 (2 readable), HoH 4 (2 readable), Courtside 3, NBA 3 (not inspected visually).
- n is tiny, views not retention, topic dominates views (Round 5: top 10% differs from median by topic/concept, not by style). Large channels (NBA, HoH, BR) get distribution from subs; their views say little about editing.
- No sound heard: music, SFX, voice speed unverified.
- Scratch data (not in repo): scratchpad `r8/meta.json`, `r8/analysis.json`, `r8/sheet_*.png`.

## 1. Sample used (last 60 days, flat-list views as of Oct 5)
| Channel | Video id | Views | Date | Len s | Title |
|---|---|---|---|---|---|
| CoachClank | iWD-Ni10p1w | 3.10M | 08-20 | 31 | James Harden Makes No Sense |
| CoachClank | 4n1WBUSdc_Y | 1.14M | 08-17 | 15 | Dame Realized How Far It Was |
| CoachClank | 3ZQhLHrsSc0 | 638K | 08-16 | ? | Kyrie vs Wemby |
| CoachClank | 3E_YA1iiPIE | 373K | 08-11 | 19 | 200 IQ Inbounds Play |
| CoachClank | nCaghzKDhag | 148K | 08-27 | ? | Draymond Gets Humbled |
| CoachClank | V5Q01RTKPD4 | 79K | 08-14 | 16 | Was This a Travel? |
| CoachClank | HK9CiYUDlhs / BWlOixJxeBg / a_y5PAVMnNw | 89K / 40K / 35K | 07-23..08 | 17-20 | (weak tail, not framed) |
| CourtsideFilms | euAd0bSG16o | 3.0M | 09-08 | 137 | Top 10 Most Unique Youth Basketball Players |
| CourtsideFilms | GqPz916gSo4 | 366K | 09-17 | 93 | 5'0 as a HS freshman to starting PG at UNC |
| CourtsideFilms | c3DHA1QW-0Y | 98K | 08-08 | 97 | 6'3 375 pounder vs 3rd graders |
| AhmedsBasketball | g2jg4HMfIv8 / RPoc8D0gDhM / OfeoThchhYs | 436K / 329K / 293K | 08-28..09-02 | 66-70 | NBA teams that added too much talent and got worse / players nobody wanted / won a title but forced their way out |
| BleacherReport | xoK5H43GLjs, Wh19WV5lYGc | 789K, 738K | 09-30..10-04 | 21-23 | LaMelo & Ant comedy; Wemby secret talents |
| HouseofHighlights | nERtCRpAyXQ, gwS9hd30nWg | 723K, 362K | 10-02..03 | 21-27 | Jaylen Brown THOUGHT he did something; Rondo hated being called Chris Paul |
| NBA | NtPkddYTLG0, x4qU5vZplfM, A9hgTUJGtc8 | 1.05M, 873K, 725K | 09-28 | 8-30 | camp/media-day clips |
Other facts from the metadata (PROVEN, public numbers): CoachClank's recent Shorts are 15-31 s (not 22-40), and in 60 days only 3 of its Shorts passed 500K; its 15 s Dame clip beat its 31 s clip per second but the 31 s Harden is the biggest. Ahmed's 66-79 s list Shorts reach 180-490K with ~120K subs.

## 2. What the frames show (what they share) and what we do differently
| # | Observation (frames 0/1/2/4 s) | Seen in | Ours today | Evidence tier |
|---|---|---|---|---|
| F1 | **Pure real game footage fills the frame from 0.0 s, no cards, no graphics.** Hook is a mid-action image. | CoachClank 5/5 readable, Ahmed, Courtside | We use ~21% card time (#24: 3 cards) and article screenshots | SUPPORTED (n~12 frames; matches Round 5 and the Wemby 79.5% result, where cards were boxed numbers) |
| F2 | **Captions are small sentence/lowercase white, 3-4 words, centred at ~45-55% height, no colour accent.** CoachClank: thin white text, soft shadow, no box. | CoachClank (all 5 readable), Courtside (white bold caps with black outline, 2-3 words, same height) | Big ALL CAPS red/green | HYPOTHESIS that this matters; PROVEN that it is what they do. 2 of 3 channels with readable captions use a tiny, calm caption |
| F3 | **A persistent top headline for the whole clip** stating the premise (Ahmed: "Teams that added too much TALENT and got WORSE", with 1-2 words in caps; BR: "WHAT'S THE MOST RANDOM THING WEMBY'S GOOD AT?" in a bold white block; HoH: yellow on black box "STOP THE TIMER PRANK" plus second line). | Ahmed 3/3, BR 2/2, HoH 2/2, Courtside (title of the video burned in for the first 3 s, "THIS HS FRESHMAN") | We removed the headline on Oct 4 (user decision, headline over 2 s) | PROVEN that big channels do it; effect on retention UNKNOWN. Not in conflict with the user's rule if it is the premise as small top text rather than a big hook headline |
| F4 | **Speaker name tag when someone talks** (HoH "ANTHONY EDWARDS" over head; BR "Stephon Castle"). | HoH, BR | none (only a tool: visual_fx nametags) | SUPPORTED (4 of 4 interview clips) |
| F5 | **Clips are short (15-31 s) for the CoachClank hits**, longer lists for Ahmed/Courtside, 7-13 s for the big-account clips. No single length wins. | all | 22-28 s favoured | consistent with our notes; HYPOTHESIS for any length rule |
| F6 | **Landscape sources are centre-cropped to fill 9:16 with no blur bars** (CoachClank, Ahmed), or full-height portrait pieces; blurred-bar fits only for squares. | CoachClank, Ahmed | blur-fit for squares | SUPPORTED (frames) |
| F7 | **Colour: untouched broadcast look, no grade or filter.** Saturation measure of frames (HSV S mean 45-190) varied with the footage, no common grade. | all | per-shot grade is a Playbook idea | PROVEN: no shared grade, so grade is the lowest priority |
| F8 | **Zoom/punch-in not visible at 1 fps** (could not tell). | - | - | UNVERIFIED |
| F9 | **Cut rate**: not measurable here. Rely on Round 3 (CoachClank 2.0-4.7 s average). | - | gate 1.9 s avg | UNVERIFIED this round |
What we do NOT differ on: titles with emoji, short real clips, comment-bait. What the 30K-1M clips share that ours do not (ranked below): footage-only picture, calm small caption, persistent premise line, name tags.

What would prove each wrong: F1: a card-heavy competitor Short above 500K (none found in sample). F2: a competitor with large colour ALL CAPS captions and better views than a small-caption rival on the same topic (not found; Courtside uses bold caps white and still hits 3M on topic strength, so style is not decisive there). F3: our A/B shows a top premise line lowers APV or "stayed to watch". F4: name tag Short does not beat a no-tag twin on APV in 3 pairs.

## 3. Ranked action list (evidence x effort)
| Rank | Action | Effort | Tier | Test |
|---|---|---|---|---|
| 1 | **Footage-only picture**: no article cards; replace numbers with a stat card (already in visual_fx) or spoken only; cards <=15% of runtime | low-mid (cards exist) | SUPPORTED | pair: card Short vs footage-only Short, same lane |
| 2 | **Caption A/B** (section 4): house vs `karaoke` first, then sentence-case small | low (styles exist) | HYPOTHESIS | section 4 |
| 3 | **Premise line** as small top text (<=40 chars, sentence case, 1-2 caps words), visible 0-3 s only, not a big hook headline. Needs the user's okay because of the Oct 4 headline decision | low (ffmpeg drawtext on a copy) | HYPOTHESIS | pair with no-line |
| 4 | **Name tag** on every real-voice quote | low (visual_fx nametags) | SUPPORTED (what pros do), gain HYPOTHESIS | on the first quote Short |
| 5 | Centre-crop (no blur) for landscape sources | low | SUPPORTED | none needed, check visually |
| 6 | Punch-in/Ken Burns, per-shot grade | mid | HYPOTHESIS | keep behind A/B; grade last |
| 7 | Cut-rate test 1.4 vs 2.2 s (Round 7 #6) | mid | HYPOTHESIS | after captions |

## 4. Caption A/B plan (uses Shorts we post anyway)
**Arms** (only the captions change; same ASS timing, chunking 2-4 words, max ~22 chars/s, same position 45-62% height, same voice):
- A `metasports`: ALL CAPS, red/green (house).
- B `karaoke`: sentence case, active word highlighted (built, `--caption-style karaoke`).
- C `clank`: sentence-case white, small (built).
- D 2-word emphasis: sentence-case white, only the 1-2 key words (numbers/names) in yellow, rest white (NOT built; specify as a copy of `clank` with per-word colour from the same ASS events).
Order: start with A vs C (biggest contrast, most likely to show an effect), then B vs C, D last.

**Pairing rules** (to cut confounding, the real problem here):
1. Same lane (record/rule/oddity, both), length within +-4 s, both 22-30 s.
2. Same hook type; no same-story-family pair (Round 5 rule: day apart anyway).
3. Same posting slot class: post on different days at the same clock time (user's usual), 24-48 h apart, never side by side the same day (they compete for the same viewers).
4. Alternate which arm goes first across pairs (A first, then C first) to cancel an early-slot bonus.
5. One variable only: do not change title opener, music, hook text between the two. Use the queue: #17 (house vs karaoke) is already planned as pair 1; pair 2 candidates #21 Jokic vs #19 Flagg or #20 Bad Boys; pair 3 #22-style evergreen vs a similar rule oddity from the idea bank (ib06/ib08).

**Metrics** (read at 48 h and 7 d; Studio; 24 h is too noisy because of the test-group stage):
1. Primary: **Viewed vs swiped away** (stayed to watch) at 48 h, because captions mostly act in the first 3 s.
2. Secondary: **Average % viewed** (APV).
3. Context only: views at 48 h and 7 d (distribution lottery; do not decide on it).
Also record the first-3 s retention if vidIQ is available (5 credits per call).

**Sample size / calling it** (honest): with a swipe-away rate near 30% and about 1-5K views per Short, a 5-point difference in stayed-to-watch is about 2-3 standard errors at 2K views each (binomial), so a single pair can show a real-looking gap, but the topic gap between two Shorts was 10-30 points in our own data (Wemby 79.5% vs Duren 63%), so **one pair proves nothing**. Rule: call a caption style better only if it wins on stayed-to-watch AND APV in at least **3 of 3 pairs (or 4 of 5)** with a mean stayed-to-watch gap of >=4 points, and the loser never beats the winner by >4 points in any pair. Anything else: "no detectable effect" and keep the cheaper option. Stop early only if one arm is below 55% stayed in two pairs (a harm).
Honest limit: 3 pairs = 6 Shorts = about 2-3 weeks at our cadence; effect sizes below 4 points cannot be seen with this design.

**Competitor evidence on caption style vs views** (UNPROVEN, confounded): CoachClank (small sentence-case white) 3.1M/1.1M; Courtside (bold white caps, 2-3 words) 3.0M with a 137 s list; Ahmed (premise headline + tiny captions) 290-440K; BR/HoH (bold caps blocks, yellow on black box) 360-790K on 1M+ sub channels. Styles are all over the place across hits, and topic and subscriber base explain more than the caption. No competitor has a same-topic caption comparison. So there is no evidence that sentence case beats ALL CAPS here; that is exactly why we test.

**Results table to paste into Outcome Log**
| Pair | Arm | Short | Caption style | Posted (ET) | Len s | Lane | Viewed (stayed) % 48 h | Avg % viewed | Views 48 h | Views 7 d | Notes (any confound: topic, slot, clip count) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | A | #17 | metasports | | | | | | | | |
| P1 | B | #17 (copy) | karaoke | | | | | | | | |
(Add a Verdict row per pair: winner on stayed %, winner on APV, gap in points, "call" only after 3 pairs.)
Note on #17: the plan has one story as two versions A/B; the platform would show both to the same channel audience, so post one version first and the other after a gap of a week; counts as a weak paired test (the topic is the same, so views drop on the second post, compare stayed % and APV only, not views).

## 5. Cheap tweaks (specified; not built, assemble.py and production folders untouched)
1. **Footage-only cut**: on a copy of #24, replace the three article cards (2.1+2.2+1.7 s) with footage plus a `visual_fx statcard` for the one spoken number; target cards <=15%. Command: see Visuals Playbook section "Exact commands".
2. **Premise line** (test copy): ffmpeg drawtext, sentence case, white with 3 px black outline, 54 px, y = 0.10*H (above the face area), `enable='lt(t,3)'`, <=40 chars, 1-2 words in caps. Example for #21: "Jokic vs Westbrook: who really owns the record?". Needs user approval.
3. **Caption D** (2-word emphasis): copy `clank` entry in Tools/captions.py to a scratch file, colour the numbers/names in `{\c&H00D7FF&}` per ASS word event; do not change the production file.
4. **Name tag** on every real-voice quote via `fx.json nametags` (66% height).
5. **Centre-crop landscape**: broll `--zoom 1.25 --y 0` (already in Lessons) as default for 16:9 sources.

## 6. Could not verify
- Cut rate, zoom, music, SFX, voice speed of competitors (no video, 1 fps thumbnails only; 0.5 s frames impossible).
- Hoops Lore (no Shorts tab).
- Exact caption fonts and sizes (101 px-wide tiles).
- NBA channel frames not inspected; several storyboards of 7-15 s clips used a different tile layout.
- Retention (APV, stayed %) for any competitor; views only.

## 7. Sources
yt-dlp public metadata, Oct 5 2026 (video ids above). Our notes: Round 5 section 4 (captions), Round 6, Round 7 (caption chunking, cut rate), Visuals and Editing Playbook, Outcome Log. Round 5 vendor links are HYPOTHESIS level.
