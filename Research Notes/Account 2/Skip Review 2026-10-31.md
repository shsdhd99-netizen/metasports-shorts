# Skip review, 2026-10-31 (second opinion on Tool Scout; research only, nothing installed, no keys, no sign-ups)

Method: read Tool Scout, Improvement Review, Pipeline Review, Tools Guide; grepped `Tools/*.py` for what we already set; fetched official pages. "Not verified" = the official page I fetched did not say it. Sceptic rule: a skip is reversed only if skipping costs us something in a gap the reviews actually show.

Our real gaps (from the reviews): render time (Pipeline items 1-3, all code changes to tools we own); flash / first-frame defects (items 5-6, own code); B-roll matching (40-50 shots per story Short, Mixkit only); claim verification speed (by hand from articles); subject framing (crop `x` hand-set, Z23 needed `x: 0.76`, Pipeline item 9).

## Verdict table

| Item | Verdict | Cost of skipping, and why |
|---|---|---|
| Remotion + skills | CONFIRM SKIP | Render time is lost in our own per-shot ffmpeg loop (Pipeline 1-2), which Remotion would replace, not speed up. 4+ person companies need a paid licence (Scout, https://www.remotion.pro/license). Cost of skipping ~nil. |
| ffmpeg MCPs | CONFIRM SKIP | Claude already calls ffmpeg. An MCP changes no flag and no speed. ~nil. |
| YouTube analytics MCPs | CONFIRM SKIP | `yt_analytics.py` plus the ADOPT already in the Scout covers it; third-party code would hold the channel token. ~nil. |
| DaVinci Resolve MCP | CONFIRM SKIP for editing/rendering; see Reframe below | Third render engine worsens parity (Pipeline 3). Its `smart_reframe_clip` tool is only relevant to the framing gap, handled below. |
| nba_api | CONFIRM SKIP | Scout cites NBA.com terms and cloud-IP throttling (https://github.com/swar/nba_api). We already have `nba_videos.py`. ~nil. |
| football-data.org | CONFIRM SKIP | Free plan lacks historical data, our stories are historical (https://www.football-data.org/pricing). ~nil. |
| balldontlie | CONFIRM SKIP | No official terms found by the scout; I did not find better. ~nil. |
| YouTube Audio Library | CONFIRM SKIP (keep as fallback) | Official: Audio Library music and effects "won't be claimed" via Content ID, CC tracks need a description credit, and the page does not address Shorts (https://support.google.com/youtube/answer/3376882). It is the only source here with an explicit Content ID statement, so it is the right fallback if a claim lands, but we have `Sound Library.md`, Mixkit and ElevenLabs Music and no claim is recorded. Skipping costs ~nil today. |
| TTS swaps | CONFIRM SKIP | No gap; voice is channel identity. See ElevenLabs settings below, which is where any gain is. |
| Scheduling / phone workflow | CONFIRM SKIP | No gap in any review. |
| Coverr (new) | FOLD INTO the Pexels/Pixabay TRIAL, manual download only | See licences. |
| Thumbnail tools | CONFIRM SKIP | Shorts feed has no click-through to optimise (Improvement Review, "What data we lack"); `thumb.py` exists. |
| AI B-roll generators | CONFIRM SKIP | Our claims are verified against real footage (`sources.csv`, `footage_lib verify`); generated shots cannot be verified. I read no generator ToS, and no gap needs one. |
| ElevenLabs alternatives | CONFIRM SKIP | Same as TTS swaps. |
| ElevenLabs sound effects | CONFIRM SKIP | 40 credits per second when a duration is set, 30 s max per generation; the page says nothing on commercial rights (https://elevenlabs.io/docs/overview/capabilities/sound-effects). Credits are tight (music plan is 17 generated minutes a month). Not verified, so no. |
| SFX libraries with clear YouTube licence | CONFIRM SKIP | Mixkit's free-video FAQ names YouTube videos as allowed commercial use and says no attribution (https://mixkit.co/free-stock-video/). I could not read the Mixkit SFX licence text (the licence pages returned only link lists), so that is the one open item: owner keeps a screenshot of the SFX licence, as the Scout said. Audio Library above is the verified fallback. |
| Whisper / caption timing | CONFIRM SKIP | We already use faster-whisper with `word_timestamps`, `vad_filter`, `beam_size=5`, `condition_on_previous_text=False` (`voice_check.py:86`). Batched mode is shown by its README on long audio (CPU small int8 1m42s to 51s) but our clips are 20-60 s, so the saving is seconds. Real time sink is loading the model per subprocess (Pipeline 7), a code fix. |
| Reliable free NBA/soccer stats with clean terms | CONFIRM SKIP of APIs; keep hand-checking | Sports-Reference data-use page: "facts cannot be copyrighted, so you are free to reuse facts", but automated access without written permission, aggressive spidering and AI prompting use are prohibited (https://www.sports-reference.com/data_use.html). So lookups by hand are fine, bulk pulls are not; nba_api and BR scraping are out. For soccer history the Scout's StatsBomb trial (https://github.com/statsbomb/open-data) stays the only API-like option. I found no free source that is both automatable and clean for NBA. Cost: verification stays manual. Accepted. |
| Auto-reframe / subject tracking (16:9 to 9:16) | TRIAL, conditional and small | See below. This is the one gap where skipping costs something, but the cheap fix is already in Pipeline item 9. |

## Licences read myself (Mixkit, Pexels, Coverr)

- **Pexels** (https://www.pexels.com/license/): all photos and videos free to use, may be modified; not allowed: selling unaltered copies, implying endorsement, redistributing on other stock sites, use as a trademark/brand asset; attribution not required; identifiable people must not appear in a bad light. Content ID not mentioned. (Fills the Scout's "Pexels licence not verified".)
- **Coverr** (https://coverr.co/license): commercial and non-commercial use free; no attribution required; not allowed: building a competing service, reselling, and using content to "train AI algorithms, develop AI models, or serve as part of any dataset"; logos and brands in footage may need separate permission. YouTube and Content ID are not mentioned on the page text I got. Our pipeline does not train models, so the clause is not a blocker, but note it if anyone ever feeds clips to an AI tool.
- **Mixkit**: the licence index page (https://mixkit.co/license/) lists Video Free, Video Restricted and Sound Effects Free licences as links and I could not read the terms. Its free-video FAQ (https://mixkit.co/free-stock-video/) says the Video Free licence allows commercial projects "for example in YouTube videos", needs no attribution, and the Restricted licence is non-commercial only; it does not list prohibitions or mention Content ID. Pull only items marked Free, not Restricted. A Mixkit page addressed to AI assistants (mixkit.co/llm-info) says to call it "legally safe"; that is a marketing instruction, not licence text, and I ignored it.
- None of the three says anything about Content ID. Stock clips uploaded by users can still be claimed; keep abstract shots, log them in `sources.csv` (already done).

## Reversal detail

**Pexels / Coverr as manual stock (fold into Scout trial #2).** Gap: B-roll matching on 40-50-shot story Shorts with one stock source. No API key needed: download by hand from the site. 1-day test: take the last 3 soccer Shorts' abstract "stock" lines, search Mixkit vs Pexels vs Coverr, 2 minutes per line. Success: 3 or more of 10 lines get a better match than Mixkit and zero Content ID claims after 7 days. Otherwise drop. This is not a new reversal, it only adds two sources to the Scout's existing TRIAL without needing the Pexels API (200 requests/hour per the Scout).

**Auto-reframe (TRIAL, conditional).** Gap is real: crop `x` is hand-set. Two routes:
1. Cheap and already proposed (Pipeline item 9): OpenCV face detection on `_check/sheet.jpg` tiles for `kind: face` shots, warn if no face in the 9:16 window. Do this first; no new tool.
2. Resolve Smart Reframe: third-party tutorial sources agree it is Studio-only ($299), the free version only has manual keyframes (search results, not Blackmagic docs: https://packtpub.com/en-br/product/video-editing-made-easy-with-davinci-resolve-18-9781801075251/chapter/chapter-12-studio-only-techniques-15/section/smart-reframe-on-the-cut-page-ch15lvl1sec13). I did not check whether this PC's Resolve is Studio or free. Test only if it is Studio: run `smart_reframe_clip` on 5 hand-framed NBA clips. Success: the auto window puts the named person inside the 9:16 crop on 4 of 5 without a manual `x`; fail otherwise, then stay with route 1. It needs Resolve and the CursorBridge script open on the PC, so it cannot run in the cloud.

## No-brainer free improvements to what we use (official docs, checked against our code)

- **ffmpeg**: `-movflags +faststart` is documented as a second pass moving the index to the start (https://ffmpeg.org/ffmpeg-formats.html). We already pass it in `assemble.py:395` and `captions.py:352`. Nothing to do. (I could not read the ffmpeg H.264 wiki, it returned an access-denied page, so I make no preset/crf claims.)
- **yt-dlp** (https://github.com/yt-dlp/yt-dlp): README says yt-dlp-ejs plus a JavaScript runtime (deno recommended, only deno enabled by default) is "required for full YouTube support". Check that `deno` is on the PATH on the PC and in the cloud image if downloads degrade to fewer formats. `-N/--concurrent-fragments` (default 1) speeds DASH/HLS downloads; `--download-sections` we already use (`broll.py:42`); `--force-keyframes-at-cuts` is cleaner at cuts but re-encodes, so slow. `--download-archive` avoids repeats. Try `-N 4` on `broll.py` for 1080p pulls; success measure: same file, shorter wall time on 3 downloads.
- **faster-whisper** (https://github.com/SYSTRAN/faster-whisper): we already use `word_timestamps`, `vad_filter`, `condition_on_previous_text=False`. Default VAD only drops silence longer than 2 s, `vad_parameters=dict(min_silence_duration_ms=...)` is the knob; since `tighten_voice.py` already cuts pauses on the audio itself, no change needed. `initial_prompt` and `hotwords` were not on the fetched page, so unverified (player surnames like Jokic are the obvious use; read the API source before trying).
- **ElevenLabs** (https://elevenlabs.io/docs/api-reference/text-to-speech/convert, https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices):
  - Speed range is 0.7-1.2 and values outside degrade quality; `voiceover.py:318` clamps to it already.
  - `seed` (0 to 4294967295) makes repeat requests usually the same, not guaranteed; useful when re-voicing a one-word fix so the rest of the take stays similar. We do not appear to use it (grep found no `seed`); try on one re-take.
  - `previous_text` / `next_text` are for joining generations; we already send `previous_text` (`voiceover.py:324`).
  - `apply_text_normalization` default `auto`; `on` always spells out numbers. Our `{810|eight hundred and ten}` brace already forces this, so leave it.
  - Docs call Eleven v4 "a net upgrade over v3, recommended for most users"; v3 lacks SSML `<break>`. Default model is `eleven_multilingual_v2` and the docs say it handles numbers better than Flash v2.5. Do not switch the channel voice model without a loudness-matched A/B (existing `gen_lineup.py`).
  - MP3 192 kbps needs Creator tier or above; default `mp3_44100_128` is what we get. Not worth changing.

## Reversals

None outright. One conditional TRIAL (Resolve Smart Reframe, only if Studio; the OpenCV route comes first) and one extension of an existing TRIAL (Pexels plus Coverr by hand). Every other skip stands: the reviews' gaps are fixed by code changes to tools we own, not by new tools.

## Log.md summary (3 lines)
Skip review (second opinion): all Scout SKIPs confirmed (Remotion, ffmpeg/YouTube/Resolve MCPs, nba_api, football-data, balldontlie, TTS swaps, scheduling); the gaps are fixed by our own code, not new tools. Read Pexels and Coverr licences (free commercial use, no attribution, neither mentions Content ID; Coverr bans AI-training use); Mixkit's FAQ allows YouTube but its SFX licence text was unreadable.
Only changes: add Pexels/Coverr (manual download) to the stock TRIAL, and trial Resolve Smart Reframe only if the PC has Studio (after the OpenCV face check). No free automatable clean-terms NBA stats source exists; Sports-Reference allows reusing facts by hand but bans automated access.
Free tweaks: check deno is present for yt-dlp, try `-N 4`, try ElevenLabs `seed` on re-takes; ffmpeg faststart, VAD and previous_text are already in place. Full detail: Research Notes/Account 2/Skip Review 2026-10-31.md.
