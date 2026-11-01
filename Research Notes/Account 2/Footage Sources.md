# Footage source map: what the PC can reach (tested Sun Nov 1, 2026, 12:30 ET)

Tests were run from this Windows PC with no cookies. "Plain file" means a direct video file URL we can cut with ffmpeg. Everything stays under the standing rules: no cookies, no DRM or paywall workarounds, drop a source that returns 403.
Versions: yt-dlp 2026.08.19.

| Source | Result on the PC | How to use it | Cloud (per the Account 2 brief) |
|---|---|---|---|
| **YouTube** (yt-dlp) | **Works.** A search (`ytsearch1:`) found a Oct 31 Wemby video; format selection passed; a 3-second section download (`--download-sections "*0-3"`, 720p cap) wrote a file | `yt-dlp -f "bv*[height<=720]+ba/b" --download-sections "*START-END" -o out.%(ext)s URL`. Use official league, team and broadcaster uploads only; never another creator's edit as the base (playbook). Note the clip's rights holder in `sources.csv` | Blocked in the cloud |
| **X posts** via `Tools/x_clip.py` | **Works.** The docstring's example post (NBA account, id 2104605201990877584) downloaded: 720x900, 10.4 s, 815 KB. The syndication endpoint (`cdn.syndication.twimg.com/tweet-result`) answered with a page, not JSON, for a fake id, so check each real post as the brief says | `python Tools/x_clip.py <post url> --out src` | Works, some 403s |
| **ESPN public clip API** | **Works.** NBA scoreboard for Oct 31 (7 events) and summary pages return `videos[]`: 3, 7, 3 clips on three games, each with an `espnmedia-cdn.akamaized.net` mp4; a HEAD gave 200 and a range request gave 206 (seekable). Soccer: Premier League (8 events, 5 clips in the first 3), La Liga (4 events, 11 clips in the first 3). UEFA Champions League on Oct 28 had 0 events (no match day that date) | `site.api.espn.com/apis/site/v2/sports/<sport>/<league>/scoreboard?dates=YYYYMMDD` then `.../summary?event=<id>`; take `videos[].links.source.HD.href`; league codes tested: `basketball/nba`, `soccer/eng.1`, `soccer/esp.1`, `soccer/usa.1` (scoreboard 200), `soccer/uefa.champions` (scoreboard 200) | Works |
| **archive.org** | **Works.** Advanced search API (200) and the item metadata API return files. A "jokic" search gave 178 items, the first a YouTube re-upload (`youtube-4Z8Az9WfwII`, mp4 listed). Seekable by HTTP range, as the brief notes | Search with `advancedsearch.php`, list files with `/metadata/<id>`, then `ffmpeg -ss T -i URL -t D -c copy`. Many items are third-party re-uploads of broadcast video, so check the rights note before using | Works |
| **Wikimedia Commons** | **Works** for the API (search found 7,960 hits for "Nikola Jokic"; imageinfo gave a direct upload URL, which answered 200). These are mostly still photos, not game video | Use the API (`commons.wikimedia.org/w/api.php`, set a descriptive User-Agent; a request without one, or to a guessed thumbnail path, got 400). Good for B-roll stills and portraits under a free licence; record the licence and author in notes.md | Not tested in the brief |
| **NBA.com / cdn.nba.com** | **Blocked.** `www.nba.com` and `cdn.nba.com/static/json/liveData/...` answered 403 to curl; `stats.nba.com` did not answer; `yt-dlp` on an `nba.com/watch/video/...` URL timed out on the video metadata host | Drop NBA.com as a download source. Use ESPN, X (the NBA account's posts) or YouTube instead. Check results and box scores in a browser or Basketball-Reference | n/a |
| **Sky Sports / Arsenal.com** | Pages load (Sky 200, Arsenal 301 redirect), but the brief already found the players do not give a plain file | Do not use as footage sources | Doesn't work |
| **Mixkit stock** | Not re-tested; `Tools/stock.py` | Generic B-roll only | Works |
| **Dailymotion** | Not supported by yt-dlp as a search URL (a search page is unsupported) | Skip | n/a |

## Differences from the cloud (what the PC adds)
- **YouTube is the big one.** The PC reaches YouTube through yt-dlp; the cloud could not. That unlocks official highlight uploads and press-conference clips, with the usual rights caution, and frame-by-frame verification on the PC.
- Other sources behave as in the cloud; **NBA.com is blocked from both** as far as these tests show.
- Tool cautions: `Tools/yt_sheet.py` was the cloud's preview-frames workaround; on the PC use yt-dlp directly.

## Notes for the pipeline
- ESPN `videos[]` entries change with the match day; fetch clips within a day or two of the game (clip links are dated paths).
- Keep every download logged: `x_clip.py` writes `downloads.csv`; add YouTube downloads to the Short's `sources.csv` with the channel and URL.
- A caveat on my tests: I did not run a full download of an ESPN or archive.org file, only HEAD and range requests; and the yt-dlp section download covered 3 seconds of a public test video.
