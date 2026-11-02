# Tool scout, 2026-10-31 (research only, nothing installed, no keys entered, no sign-ups)

Method: read START HERE, Tools Guide, Improvement Review, Pipeline Review, Footage Sources; checked `Tools/yt_analytics.py` by grep; then fetched official pages. Every claim below has a URL. "Not verified" means the official page I fetched did not say it. Most things are SKIP on purpose: the Pipeline Review shows our real gaps are render speed and QA coverage (tools we own), and the Improvement Review shows the real data gaps are in analytics.

## Ranked shortlist (ADOPT / TRIAL)

| # | Verdict | Candidate | Gap it fixes |
|---|---|---|---|
| 1 | ADOPT | Add `subscribedStatus` and `insightTrafficSourceType` to our own `yt_analytics.py` (official YouTube Analytics API) | Improvement Review "What data we still lack" line 111: viewed vs subscribed and traffic source per Short (the S01 86-vs-7 subs question, section 5) |
| 2 | TRIAL | Pixabay / Pexels video as a second stock source beside Mixkit | Footage Sources table: Mixkit is our only stock source and is "abstract B-roll only" |
| 3 | TRIAL | StatsBomb open data for soccer fact-checking | Improvement Review rule "never invent a stat"; FC claims are checked by hand today |
| 4 | TRIAL (low) | Wikimedia pageviews as a free "what are people reading about right now" signal | Idea/trend sourcing; today it is the 3:43 AM research run |

## 1. YouTube Analytics API: traffic source and subscribed status (ADOPT)
- **What:** The official channel reports support the "Traffic source" report with required dimension `insightTrafficSourceType` and optional `creatorContentType`, `day`, `subscribedStatus`; metrics `engagedViews`, `views`, `estimatedMinutesWatched`. Also a "User activity by subscribed status" report. Source: https://developers.google.com/youtube/analytics/channel_reports
- **Our gap:** `grep` of `Tools/yt_analytics.py` finds no `subscribedStatus`, `insightTrafficSource` or `creatorContentType`; it pulls `video`, daily and `elapsedVideoTimeRatio` only. Review line 111 lists exactly these as missing.
- **Cost / risk:** free, same OAuth we already use, read-only. No ToS issue (our own channel, our own API).
- **Effort:** about 1 hour (new `pull-traffic` subcommand writing a CSV per Short).
- **Not verified:** the valid `creatorContentType` values (the page does not list them; check the Dimensions reference before coding), and the page does not mention "stayed to watch" or swipe-away at all, so that metric stays Studio-export-only. Revision history (https://developers.google.com/youtube/analytics/revision_history) lists only `engagedViews` for Shorts; nothing new on swipe-away.
- **Success measure:** a table of Shorts feed vs browse vs search, split subscribed vs not, for S01, S03, S05; answers or kills the "S01 launch-day subscribers" hypothesis.

## 2. Pixabay / Pexels video (TRIAL)
- **What:** free stock video with search APIs.
  - Pixabay: licence allows free use and modification, no attribution required, but forbids selling unchanged, and forbids misleading use or use with recognisable people in immoral/illegal ways. https://pixabay.com/service/license-summary/ The licence summary does not mention Content ID. API: 100 requests per 60 s, responses must be cached 24 h, automated mass querying prohibited, `medium` size always present, `large` (usually 4K) not guaranteed. https://pixabay.com/api/docs/
  - Pexels: 200 requests/hour and 20,000/month; API asks for "a prominent link to Pexels"; abuse or working around limits ends access. https://www.pexels.com/api/documentation/ The Pexels licence text itself I did not fetch (only secondhand pages), so treat Pexels licence as NOT verified until read at pexels.com/license.
- **Gap:** Footage Sources.md section 1: Mixkit is the only stock row. The Pipeline Review does not cite a stock shortage, so this is a modest gap, not proven.
- **Risk:** Content ID can still hit user-uploaded stock; neither page promises otherwise. Keep it to abstract shots, never people or logos. Log each clip in `sources.csv` as now.
- **Effort:** small `stock.py` backend (needs a free API key entered by the owner, not me).
- **1-day test:** take the last 3 soccer Shorts' "stock" lines; count how many lines found a better match than Mixkit in under 2 minutes. Success: 3+ of 10 abstract lines upgraded, and zero Content ID claims after 7 days on posted drafts. If fewer, SKIP.

## 3. StatsBomb open data (TRIAL, research-only)
- **What:** free event data on GitHub for "certain leagues". Terms: state StatsBomb as the source and use their logo. https://github.com/statsbomb/open-data
- **Gap:** soccer stat claims (shot counts, minutes, penalty-kick details) verified only from articles.
- **Not verified:** which competitions are included (the README points to `data/competitions.json`, not read), and whether recent seasons exist. The logo requirement conflicts with our "no cards" rule, so use it only to check facts, and credit in the description only after reading the user agreement.
- **1-day test:** pick 3 past Shorts with historical match claims (e.g. famous shootouts); see if the data file exists and confirms each number. Success: at least 2 of 3 matches found. Otherwise SKIP.

## 4. Wikimedia pageviews (TRIAL, low)
- **What:** Wikimedia analytics API, content licence CC BY-SA 4.0, example calls need no key. https://doc.wikimedia.org/generated-data-platform/aqs/analytics-api/documentation/getting-started.html
- **Not verified:** the "top articles per day" endpoint, rate limits and User-Agent rule were not on the fetched page (it points to an access-policy page).
- **Test:** pull 7 days of views for 20 player pages and compare spikes with what the daily research flagged. Success: it surfaces 1+ story the research missed. The data is a signal, not a source for claims.

## SKIP list (with why)

| Candidate | Why skip | URL |
|---|---|---|
| Remotion + its Claude skills (incl. captions) | We already render TikTok-style captions with our own `captions.py`; no cited gap. Needs a Node toolchain for a non-technical owner. Free only for individuals/companies up to 3 people; 4+ needs a paid licence ($25/seat/month or $0.01/render with $100/month minimum), so any growth triggers cost. Install commands differ between sources (not confirmed). | https://www.remotion.pro/license , https://remotion.dev/skills |
| ffmpeg MCP servers (e.g. mrdainami/ffmpeg-mcp, PedroMarianoAlmeida/ffmpeg-mcp) | Claude already runs ffmpeg directly; an MCP adds third-party code on the PC to do the same. Repos not audited. | https://github.com/mrdainami/ffmpeg-mcp , https://claudemarketplaces.com/mcp/pedromarianoalmeida/ffmpeg-mcp |
| YouTube analytics / Data API MCP servers (adityaarsharma, youtube-analytics-mcp, youtube-connector-mcp) | `yt_analytics.py` already does this. The first can update titles, descriptions and tags on videos, which clashes with the rule that we never change public videos; low-adoption third-party packages holding the channel OAuth token is a security cost. Not audited. | https://awesome.ecosyste.ms/projects/github.com%2Fadityaarsharma%2Fyoutube-mcp-server , https://www.pkgstats.com/pkg:youtube-analytics-mcp |
| DaVinci Resolve MCP (installed) | Needs Resolve open and the CursorBridge script running. Pipeline Review item 3 says the Drift/editor path already drifts from the ffmpeg engine (no zoom, no `_render.json`); a third engine worsens parity. Resolve-only features (voice isolate, smart reframe, transcribe) exist as tools here, but whether this install is Resolve Studio was not checked, and nothing in the reviews asks for them. Revisit only if the owner wants hand-editing. | tool list in this session |
| `nba_api` | Data is subject to NBA.com Terms of Use; README warns stats.nba.com throttles and "does not respond to many cloud-hosting IP ranges" (AWS, GCP, Azure), and account 2 runs in the cloud. We already have `nba_videos.py` and Basketball-Reference. | https://github.com/swar/nba_api |
| football-data.org free plan | 12 competitions, 10 calls/min, delayed scores; historical access not listed for free; our stories are historical. Commercial-use terms not stated. | https://www.football-data.org/pricing |
| balldontlie | Free-tier limits conflict across third-party pages (5/min vs 60/min), stats endpoints reportedly 401 on free; I found no official terms page. Cannot recommend on this evidence. | https://freeapihub.com/apis/balldontlie-api |
| YouTube Audio Library for SFX/music | Official page: Audio Library tracks "won't be claimed" via Content ID; some tracks need credit in the description. Page does not address Shorts. We already have `Library/Sound Library.md`, Mixkit and ElevenLabs Music; I did not compare contents, so use only as a backup if a Content ID claim ever lands. | https://support.google.com/youtube/answer/3376882 |
| TTS alternatives to ElevenLabs | No gap cited in either review; `voiceover.py` already switches between `eleven_multilingual_v2` and v3/v4 models. Changing voice changes channel identity. Not researched further, on purpose. | n/a |
| Scheduling / phone workflow | Cloud routines (min interval 1 hour), Desktop tasks and `/loop` already cover it; `/loop` expires after 7 days. No gap in the reviews. | https://code.claude.com/docs/en/scheduled-tasks |
| Caption/transcription tools | Whisper-based timing already in `voice_take.py` / `export_check.py`. No gap. | n/a |

## Not covered (said honestly)
Thumbnail/cover tools (our `thumb.py` exists; Shorts covers are minor), A/B tools beyond Studio Test & Compare, AI B-roll generators (copyright and "real footage" rules make most unsuitable), Coverr licence (page not fetched), Mixkit licence text (the licence page I fetched did not contain the terms, so the existing Mixkit use is unconfirmed by me; the owner/main account should keep the licence screenshot on file).

## Log.md summary (3 lines)
Tool scout (research only): ADOPT the YouTube Analytics API traffic-source and subscribedStatus pull in our own yt_analytics.py (fills the "viewed vs subscribed / traffic source" gap, free, official); TRIAL Pixabay/Pexels stock, StatsBomb open data for soccer fact-checks, and Wikimedia pageviews as a trend signal.
SKIP Remotion, ffmpeg and YouTube MCPs, the Resolve MCP, nba_api, football-data.org, balldontlie, TTS swaps: no cited gap, extra third-party risk, or licence/ToS problems.
Full table, URLs and 1-day test plans: Research Notes/Account 2/Tool Scout 2026-10-31.md.
