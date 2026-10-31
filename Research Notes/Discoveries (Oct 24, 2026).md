# Discoveries (Oct 24, 2026)

**What this is:** new things we are probably not doing yet, in five areas: voice, YouTube, posting, footage and competitors.

**How it was made:**
- Web research on Oct 24, 2026. Official docs, help pages and changelogs came first.
- Live tests from this cloud session (curl, ffprobe, yt-dlp) for footage sources and competitor title lists.
- A re-read of our Ahmed data (`Research Notes/Ahmed Network Data (Oct 21, 2026)/`).
- I checked existing notes first, so known items are only mentioned when something changed. Known items include the Aug 2026 views change, auto-dubbing and the Content ID 60 s rule.

**Evidence tiers:**
- **[V]** verified in an official source, or tested live by me today.
- **[S]** several credible sources agree.
- **[H]** a single or weak source, a vendor study, or my own rough count.

---

## The 5 most useful actions

1. **Get soccer footage from Bundesliga.com and MLSsoccer.com.** Both serve 1080p MP4 files to a server, with no YouTube involved. Bundesliga also has native vertical 1080x1920 clips. Build a small `Tools/league_videos.py` like `nba_videos.py`. [V, tested today] (details: F1, F2)
2. **Run a blind voice test: Eleven v4 against Multilingual v2, both as Alex.** v4 launched Sep 28, 2026 and costs the same per character. It ranks #2 in the blind Artificial Analysis voice arena (Elo 1332). Multilingual v2 ranks #44 (Elo 1096). v4 has no Speed setting, so apply `atempo=1.2` in ffmpeg to match our pace. [V for price and features; ranking from Artificial Analysis] (V1)
3. **Stop judging Shorts on "yesterday's" analytics.** Since Sep 9, 2026, Google's API docs say Analytics data runs 48-72 hours behind. Use the Data API (`videos.list`) for same-day view counts. Score a Short in the daily run only once it is at least 72 hours old. [V] (Y1)
4. **Pass YouTube's Oct 1, 2026 originality update.** Shorts now rank re-uploads lower. Coverage says a voice-over that only describes the on-screen action does not count as original. Add a QA gate: every line must add a fact, an argument or a twist the footage doesn't show. Keep evidence cards on screen. Never run one source clip uncut for long. [S] (Y2)
5. **Add a news-question lane to MetaSports FC.** In 2026 Ahmed's Goal switched to topical question titles, for example "Why is UEFA investigating FC Barcelona?". These are 61 of its newest 120 Shorts (about late July to Oct 21), but only 11 of the 300 before them. Their median is 231K views against 205K for its other recent Shorts, and the top one has 1.9M. Use the Bundesliga and MLS clips (action 1) for match-week news. [H, our own count] (C1)

---

## 1. ElevenLabs

**V1. Eleven v4 is out and costs the same as Multilingual v2.** [V]
- **What:** `eleven_v4` launched Sep 28, 2026. ElevenLabs now recommends it for "video narration".
  - The API price is $0.08 per 1K characters, the same as Multilingual v2.
  - The Creator plan's API allowance is 275K characters for v4, also the same as Multilingual v2.
  - The Help Center says it works with "Create speech" and "Stream speech" (`/v1/text-to-speech`).
- **Why it matters:** in blind tests, v4 is ranked far above our current model, at no extra cost.
- **Catch 1:** "Style and Speed sliders are not available in Eleven v4" and SSML is not supported. We run Alex at speed 1.2.
- **Catch 2:** the docs don't say whether the `/with-timestamps` endpoint accepts v4. The Oct 12 changelog does say the timestamp variants of TTS and Text to Dialogue exist.
- **Action:**
  - Voice two finished scripts both ways, with v4 slowed or sped by ffmpeg `atempo=1.2`.
  - Run `voice_quality.py` on both, then the owner's ear test.
  - Switch only if v4 wins and keeps the 224-229 wpm pace.
  - Watch the numbers: v4 is more expressive and may drift.
- **Sources:**
  - [Models](https://elevenlabs.io/docs/models)
  - [What is Eleven v4](https://elevenlabs.io/docs/help-center/product/core-capabilities/text-to-speech/what-is-eleven-v4.md)
  - [Eleven v4 capability page](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/eleven-v4.md)
  - [Choosing the right model](https://elevenlabs.io/docs/eleven-api/choosing-the-right-model.md)
  - [API pricing](https://elevenlabs.io/pricing/api)
  - [Changelog](https://elevenlabs.io/docs/changelog)
  - [Artificial Analysis voice arena](https://artificialanalysis.ai/text-to-speech/leaderboard)

**V2. Flash v2.5 is half price and almost as well liked, but it misreads numbers.** [V]
- **What:** Flash v2.5 has a "50% lower price per character" (0.5 credit/char on the API).
  - In the blind arena it scores Elo 1078, against 1096 for Multilingual v2. Their rank bands overlap (48-56 and 40-49).
  - But "numbers aren't normalized by default" on Flash v2.5. Only Enterprise can turn normalization on.
  - "Multilingual v2 does a better job of normalizing numbers."
- **Why it matters:** our format ends on a number. "31.4" or "1,301" read wrong would kill the payoff.
- **Action:**
  - Don't switch to save money; our credits are enough (see V5).
  - If we ever need to halve costs, spell every number out in words before sending, then use Flash.
  - Test v4 (V1) first.
- **Sources:**
  - [Models](https://elevenlabs.io/docs/models)
  - [Pricing FAQ](https://elevenlabs.io/pricing)
  - [Artificial Analysis](https://artificialanalysis.ai/text-to-speech/leaderboard)

**V3. Turbo v2.5 is deprecated.** [V]
- **What:** `eleven_turbo_v2_5` and `eleven_turbo_v2` are deprecated. ElevenLabs says "use the Flash models over Turbo models in all use cases."
- **Why it matters:** if a tool ever falls back to Turbo, it is on borrowed time.
- **Action:** none today. No tool in `Tools/` uses Turbo (checked).
- **Source:** [Models](https://elevenlabs.io/docs/models)

**V4. Nobody documents whether `previous_text`/`next_text` are billed, but every reply shows the real cost.** [V]
- **What:** neither the API reference nor the stitching guide says whether context text is charged.
  - The stitching guide says the response headers carry `character-cost`. Newer docs call it `x-character-count`.
  - Other facts from the docs:
    - If `previous_request_ids` is sent, `previous_text` is ignored.
    - Request IDs must be under 2 hours old.
    - Stitching "is not available for the `eleven_v3` model".
- **Why it matters:** `voiceover.py` can send both context fields. If they are billed, each take costs extra.
- **Action:**
  - Log the `character-cost` header on every TTS call.
  - Run one pair: the same line with and without `previous_text`.
  - Keep context only if it's free or clearly helps the sound.
- **Sources:**
  - [TTS with timestamps reference](https://elevenlabs.io/docs/api-reference/text-to-speech/convert-with-timestamps)
  - [Request stitching guide](https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/request-stitching.md)

**V5. The Creator plan now lists 121K credits a month. Rollover is real; overage is gone.** [V]
- **What:** the pricing page lists Creator at "121k credits per month" (the plan used to be 100K).
  - Unused credits roll over for up to two months, while you stay subscribed. Cancelling or downgrading loses them.
  - Usage-based overage "is not available on new self-serve subscriptions". You prepay instead (Pay As You Go top-ups).
  - Annual billing is "two months free": $18.33 a month instead of $22.
  - The Oct 5 price cut was about 20% on the API, per UsagePricing's before-and-after page captures. [H]
- **Why it matters:**
  - At about 520 characters for an NBA Short and about 1,000 for an FC Short, voiced twice each, we use about 3K credits a day.
  - That is about 79K by Nov 19, so the 97.7K left is enough.
  - The 3K a day is my estimate, not a measured figure.
- **Action:**
  - At the Nov 19 renewal, read `character_limit` from `/v1/user/subscription` (already printed by `voiceover.py`). Confirm we get 121K.
  - Never downgrade mid-cycle; that loses the rollover.
  - Annual billing saves about $44 a year if the owner is staying.
- **Sources:**
  - [Pricing](https://elevenlabs.io/pricing)
  - [Billing](https://elevenlabs.io/docs/overview/administration/billing.md)
  - [Have characters changed](https://elevenlabs.io/docs/help-center/account/general/have-characters-changed.md)
  - [UsagePricing capture](https://www.usagepricing.com/blueprint/activity/elevenlabs-2026-10-05-v4-launch-tts-price-cut)

**V6. Free audio effects on TTS calls (Oct 12, 2026).** [V]
- **What:** TTS calls, including the timestamp variants, now take an `audio_effects` object: filter, reverb, room, noise bed, pan. "Effects do not change the cost of a request."
- **Why it matters:** low. We already do sound in ffmpeg.
- **Action:** ignore. Keep sound processing in our own chain.
- **Source:** [Changelog](https://elevenlabs.io/docs/changelog)

---

## 2. YouTube Shorts in 2026

**Y1. The Analytics API is 48-72 hours behind.** [V]
- **What:** on Sep 9, 2026, Google added a Data Model section to the API docs. It describes "a 48 to 72 hour processing delay", and end dates are cut to the last fully processed day. It recommends the Data API's `videos.list` for real-time video stats.
- **Why it matters:** the 6:41 AM daily run "learns from yesterday's results". For a Short posted yesterday at 11 AM, the API may hold little or nothing yet. Lessons drawn from it are noise.
- **Action:**
  - In `yt_analytics.py daily`, take live views from `videos.list`.
  - Only score engaged ratio and retention for Shorts at least 72 h old.
  - Mark younger rows "too early".
  - The owner's 24 h Studio numbers stay the fast signal.
- **Source:** [YouTube Analytics revision history](https://developers.google.com/youtube/analytics/revision_history)

**Y2. Shorts now rank re-uploads lower (Oct 1, 2026).** [S]
- **What:** a TeamYouTube post, "Prioritizing original content on Shorts", says YouTube will "reduce the reach of content re-uploaded from other creators without adding anything of your own".
  - It says "minor technical edits or template-based changes" don't count.
  - PPC Land reports that, per Search Engine Journal's account of YouTube's Rene Ritchie, "voice-over describing on-screen action" doesn't make another creator's clip original.
  - This hits recommendations only, not monetization.
- **Why it matters:** our format is an AI voice over real league footage. A story with a point of view should pass. A line like "LeBron drives and dunks" over a highlight would not.
- **Action:** add a check to the script critic: "Does every line add a fact, argument or twist the footage doesn't show?" Also:
  - Keep evidence cards and number cards on screen.
  - Cut sources short (we already cut every 1.1-2.1 s).
  - Never reuse another creator's captioned clip as the main picture.
- **Sources:**
  - [TeamYouTube thread](https://support.google.com/youtube/thread/470890423/prioritizing-original-content-on-shorts?hl=en)
  - [Android Authority](https://www.androidauthority.com/youtube-shorts-promoting-original-content-reposts-3718668/)
  - [PPC Land](https://ppc.land/re-uploaded-shorts-lose-reach-as-youtube-favours-original-clips/)

**Y3. "Stayed to watch" is still not in the API. A new reach report might come close.** [V that it exists; untested that it helps]
- **What:** the Analytics API metrics list has no swipe, "shown in feed" or "stayed to watch" metric, as our notes already said.
  - New: on Jan 15, 2026, the Reporting API added reach reports (`channel_reach_basic_a1`, `channel_reach_combined_a1`). They give per-video `video_thumbnail_impressions`, and the combined one adds `traffic_source_type`.
  - The docs don't say whether Shorts-feed showings count as impressions.
- **Why it matters:** if Shorts-feed impressions show up, engaged views ÷ Shorts-feed impressions would be a daily, automatic stand-in for "Stayed to watch".
- **Action:**
  - Create one Reporting API job for `channel_reach_combined_a1` on each channel. Reports start a day or two after the job.
  - Check whether rows with traffic source SHORTS appear for our Shorts.
  - If they do, compare the ratio with Studio's "Stayed to watch" on 10 Shorts before trusting it.
- **Sources:**
  - [Analytics metrics](https://developers.google.com/youtube/analytics/metrics)
  - [Channel reports](https://developers.google.com/youtube/reporting/v1/reports/channel_reports)
  - [Revision history](https://developers.google.com/youtube/analytics/revision_history)

**Y4. Use the free "Related video" link on every Short.** [V for the feature; H for any lift]
- **What:** each Short can carry one clickable link to another video or Short on the same channel. It shows under the channel handle in the Shorts player.
  - You set it in Studio (Content, then the Short, then Related video).
  - It needs advanced feature access, which means phone verification.
- **Why it matters:** we don't use it anywhere (checked all UPLOAD.md files). It's the only clickable path out of a Short.
- **Action:**
  - In each UPLOAD.md, add a line, "Related video: [our best Short on the same player/club]".
  - The owner sets it after posting.
  - Point new Shorts at a proven hit (e.g. #19 for the NBA channel).
- **Source:** [YouTube Help: add a related video to Shorts](https://support.google.com/youtube/answer/14075157?hl=en)

**Y5. A/B testing still excludes Shorts. Testing different cuts is "coming soon".** [V]
- **What:** the help page says "A/B testing is not available for Shorts". Tests pick the winner on watch time, not click-through.
  - On Sep 23, 2026 (Made on YouTube), YouTube announced testing "up to three different cuts for which holds audience attention best". No date, no eligibility, and no word on Shorts.
- **Why it matters:** if it reaches Shorts, it is the cleanest possible hook test.
- **Action:**
  - Keep our own paired tests for now.
  - Check Studio's upload flow once a week for a "test cuts" option.
  - When it appears, test the first 2 seconds only.
- **Sources:**
  - [YouTube Help: A/B test titles & thumbnails](https://support.google.com/youtube/answer/16391400?hl=en)
  - [YouTube Blog, Made on YouTube 2026](https://blog.youtube/news-and-events/innovation-youtube-era-made-on-viewers-creators/)
  - [YouTube Blog, new creator tools](https://blog.youtube/news-and-events/made-on-youtube-new-tools-power-creation-journey/)

**Y6. Posts can now be recommended inside the Shorts feed.** [V for the statement; H for value]
- **What:** "On web and mobile devices, viewers will now be recommended posts from the Shorts feed" (YouTube Blog, Sep 23, 2026).
- **Why it matters:** a poll or image post costs no voice credits and could reach Shorts viewers.
- **Action:**
  - Try one poll post a week on each channel. Use the pinned-comment debate question, e.g. "Was SGA right to sit on 17?".
  - Log the post's impressions.
- **Source:** [YouTube Blog: Shorts series and TV features](https://blog.youtube/news-and-events/made-on-youtube-creators-shorts-series-tv-features/)

**Y7. Shorts series (seasons and episodes) launched Sep 23, 2026, for YPP creators.** [V for the launch; S for YPP-only]
- **What:** you can group Shorts into seasons and episodes, with custom artwork and back-to-back playback. TechCrunch says it's for Partner Program creators.
- **Why it matters:** "Back in [year]" stories and record ladders fit a series. We aren't in YPP yet.
- **Action:**
  - After YPP, make one series per channel, e.g. "Records that sound bad" or "Football's strangest rules".
  - Until then, number repeat formats in pinned comments so they are ready to group.
- **Sources:**
  - [YouTube Blog](https://blog.youtube/news-and-events/made-on-youtube-creators-shorts-series-tv-features/)
  - [TechCrunch](https://techcrunch.com/2026/09/23/youtubes-new-short-series-feature-brings-episodic-viewing-to-shorts/)

**Y8. Auto-dubbing: fast speech and copyright claims are excluded.** [V]
- **What:** auto-dubbing is on by default for eligible creators. A video is excluded if it has "speech that is too fast" or copyright claims.
  - "Publish manually" lets you review dubs before they go live.
  - The help page doesn't say whether Shorts are covered.
  - YouTube's own figure: dubbed versions hold about 75% of the original's average view duration (PPC Land, citing YouTube's May 15, 2026 explainer).
- **Why it matters:** NBA Shorts at 224-229 wpm may be too fast to dub. FC Shorts are slower and have a global audience.
- **Action:**
  - In Studio, check the dub status of 3 FC and 3 NBA Shorts.
  - If NBA Shorts never get dubs, don't count dubbing in NBA plans.
  - Use Studio's audio-track filter to see dubbed views on FC.
- **Sources:**
  - [YouTube Help: automatic dubbing](https://support.google.com/youtube/answer/15569972?hl=en)
  - [PPC Land](https://ppc.land/youtube-auto-dubbing-tops-6m-daily-viewers-expands-to-27-languages)

**Y9. No 2026 change to Shorts length or to the Content ID rule over 60 s.** [V]
- **What:** Shorts can still be up to 3 minutes. A Short over 1 minute with any active Content ID claim is still blocked worldwide, and Shorts of 1 minute or less are unaffected. The only 2025-26 change was for Official Artist Channels (Dec 8, 2025).
- **Why it matters:** the FC cap of 55-59.9 s is still right, and now more so: the new league sources (F1, F2) carry Content ID.
- **Action:** keep the hard 59.9 s cap in QA.
- **Source:** [YouTube Help: three-minute Shorts](https://support.google.com/youtube/answer/15424877?hl=en)

**Y10. The views definition: nothing new since Aug 2026.** [V]
- **What:** as already logged in Monetization Research (Oct 23):
  - Since Aug 27, 2026, `views` counts from the first frame on all formats.
  - `engagedViews` is unchanged: "viewed past the first frame".
  - YPP now says "qualified Shorts views".
- **Action:** none. Our engaged ratio stays valid.
- **Source:** [Analytics revision history](https://developers.google.com/youtube/analytics/revision_history)

**Y11. Hashtags and titles: no official 2026 change found.** [H]
- **What:** I found no YouTube announcement that changes Shorts hashtags or titles in 2026. Blogs disagree with each other.
- **Action:** keep up to 3 hashtags outside the title, as we do. Competitors moved the same way (C3).
- **Source:** blog roundups only, e.g. [hashtagtools](https://hashtagtools.io/blog/youtube-shorts-hashtags-title-vs-description-2026). Treat as weak.

**Y12. New Studio "Insights" and "Research" areas for spotting outlier videos.** [V for the announcement]
- **What:** Made on YouTube 2026 announced "new Insights and Research destinations" to "discover outlier videos". No new Shorts metric was named.
- **Action:**
  - When Research appears in Studio, use it as a topic source for the daily run.
  - The owner should screenshot the NBA and soccer outliers once a week.
- **Source:** [YouTube Blog, new creator tools](https://blog.youtube/news-and-events/made-on-youtube-new-tools-power-creation-journey/)

---

## 3. Posting time and frequency

**P1. The biggest 2026 timing study says Shorts do best Friday evening and worst from noon to 5 PM.** [H: vendor study, scored on engagement not views]
- **What:** Buffer (July 2026, about 1.8M videos):
  - Best Shorts slots: Friday 4 PM, 6 PM and 7 PM, local time.
  - Best days: Friday, then Saturday, then Thursday.
  - "The worst times to post YouTube Shorts tend to fall during the afternoon, between 12 p.m. and 5 p.m."
  - Buffer adds that Shorts resurface for a long time, so publish time is "less make-or-break".
- **Why it matters:** our NBA slot is 11 AM and our FC slot is 12 PM, right at the start of Buffer's weakest window.
- **Action:**
  - Keep NBA news at 11 AM: news decays, and our own data shows day-late news drops to 58% stayed.
  - For FC, which is evergreen, alternate 12 PM and 6 PM ET for two weeks. Keep everything else the same and compare "Stayed to watch" and 48 h views.
  - First check FC's audience geography in Studio. If most viewers are in Europe, noon ET is their evening, which suits it.
- **Source:** [Buffer](https://buffer.com/resources/best-time-to-post-on-youtube/)

**P2. Another dataset also favours late afternoon over the morning rush.** [H]
- **What:** Adobe Express (24,274 Shorts from 280 creators, May 2025):
  - Shorts posted off-peak averaged 8.7M views, against 6.2M for the 8-10 AM peak.
  - The best hour was 4 PM. The best slot was Saturday 4 PM.
- **Why it matters:** two independent vendors point to late afternoon or evening, not morning. That fits the 6 PM evergreen NBA slot we already use.
- **Action:** keep the 6 PM NBA evergreen slot. Prefer Saturday or Friday for the strongest evergreen Short.
- **Source:** [Adobe Express](https://www.adobe.com/express/learn/blog/best-times-to-post-youtube-shorts)

**P3. Frequency: each Short does best at 2-4 a week, but monthly totals keep rising with more posts.** [H]
- **What:** Metricool (July 2026, 799,718 videos):
  - "Each Short performs best per post at 2 to 4 uploads a week".
  - There is "no real ceiling on the monthly total".
  - Metricool says this is correlation, not causation.
  - Our own Ahmed data agrees on the downside: their push to about 3 a day in Jul-Sep 2026 lowered medians, and they pulled back.
- **Why it matters:** 1 a day per channel trades a little per-Short reach for more total views. That suits a channel chasing qualified views. Going to 3 a day looks harmful.
- **Action:**
  - Keep 1 a day per channel.
  - Add the second NBA slot only for a formula-fit Short.
  - Never go to 3.
  - Judge by "Stayed to watch", not by views per Short.
- **Sources:**
  - [Metricool YouTube Trends 2026](https://metricool.com/youtube-trends/)
  - `Research Notes/Story Format Study - Ahmed (Oct 21, 2026).md`

**P4. No official YouTube guidance on frequency.** [H]
- **What:**
  - I found no YouTube statement saying several Shorts a day hurts.
  - The most-quoted study, from VidCon 2022 via Tubefilter, says "at least one video per day" but "dozens per day" lowers efficiency. It is old.
  - The Creator Liaison tested 3 a day in July 2024, but no results were published.
- **Action:** none beyond P3.
- **Sources:**
  - [Tubefilter 2022](https://www.tubefilter.com/?p=167933)
  - [YouTube Blog, Liaison top five, July 2024](https://blog.youtube/creator-and-artist-stories/renes-top-five-july-25-2024/)

---

## 4. Footage that works from a server (no YouTube)

**F1. Bundesliga.com: 1080p MP4s through JW Player, including native vertical clips.** [V, tested today]
- **What:** Bundesliga article pages carry JW Player `mediaid` values in their `ng-state` JSON, plus a playlist `feedid`.
  - `https://cdn.jwplayer.com/v2/media/<mediaid>` returns MP4s at 180p to 1080p. `https://cdn.jwplayer.com/v2/playlists/<feedid>` lists 25 related clips.
  - I downloaded one ("Spieltagshelden: Top 5 Saves"): h264, **1080x1920**, 59.8 s.
  - 5 of the 25 feed clips are native vertical: weekly Top 5 Goals, Saves, Skills and Tackles, plus "All goals and assists of Luis Díaz 2026/27".
  - The rest are 1080p match highlights of about 2 minutes, plus player features such as "Every Kane goal in the Bundesliga" (809 s).
- **Why it matters:** this is the first clean, sharp, current soccer source for MetaSports FC. Vertical clips need no crop.
- **Action:**
  - Build `Tools/league_videos.py bundesliga`. Fetch an article page, read the `mediaid`s, then fetch the media JSON and take the top MP4. Follow the redirect (`curl -L`).
  - Watch every frame before use.
- **Catch:** Bundesliga clips will be Content ID matched. Keep FC under 60 s (Y9) and transform them (Y2).
- **Source:** live test. Endpoints: `cdn.jwplayer.com/v2/media/47asv97u`, `/v2/media/kEL6avZg`, `/v2/playlists/rY02UXGi`.

**F2. MLSsoccer.com: 1080p MP4s through Brightcove.** [V, tested today]
- **What:** `mlssoccer.com/video/` lists about 25 Brightcove video IDs (account 5530036772001).
  - The player's public config (`players.brightcove.net/5530036772001/default_default/config.json`) holds the policy key.
  - `edge.api.brightcove.com/playback/v1/accounts/5530036772001/videos/<id>` returns MP4s at 720p and 1080p.
  - I downloaded the first 3 MB of one: h264 1920x1080 with AAC audio, playable.
- **Why it matters:** US soccer with official angles. Good for MLS and Messi-era stories.
- **Action:** add an `mls` mode to the same tool, working from the video page's IDs.
- **Catch:** I did not test keyword search through the API; this session's safety check blocked that call. Per-video fetches from the public page work.
- **Source:** live test, `mlssoccer.com/video/`.

**F3. Other soccer sites, tested.** [V, tested today]
- **Premier League:** pages are built by script from a Pulselive API. There is no MP4 or player ID in the HTML, so it is not usable without more work. Its "The Archive" video section looks promising for "Back in [year]" stories, but is untested.
- **UEFA.com:** timed out from the cloud (bot protection).
- **LaLiga:** uses Vimeo embeds, and the player config returns 403.
- **Ligue 1, Serie A:** script-rendered, with no video links in the HTML.
- **NWSL `/video`:** 404.
- **Action:** don't spend time on these. Bundesliga and MLS first.

**F4. WNBA: titles and stills yes, video files no.** [V, tested today]
- **What:** `content-api-prod.nba.com/public/1/leagues/wnba/content?types=video` works.
  - It returned 1,284 items for "clark", with titles, durations and `cdn.wnba.com` stills.
  - But `videoAssets` is empty. The source MP4 sits on S3 and returns 403, and playback goes through MediaKind.
  - The team-site route that works for NBA returns "Route not found" for WNBA team IDs.
- **Why it matters:** for WNBA Shorts (e.g. #60 Caitlin Clark), use the feed to find moments and stills, and get motion elsewhere (X posts).
- **Action:** add `--league wnba` to `nba_videos.py`, for search and stills only.
- **Source:** live test.

---

## 5. What the big sports story Shorts channels changed in 2026

**C1. Ahmed's Goal switched to news-question Shorts.** [H, our own count from the Oct 21 data]
- **What:** 61 of its newest 120 Shorts (about late July to Oct 21, 2026) have question titles about current news.
  - Examples: "Why is UEFA investigating FC Barcelona?" (623K), "What exactly happened between Cristiano Ronaldo and Portugal?" (1.9M), "Did Liverpool just get robbed by the refs?" (177K).
  - Only 11 of the 300 before them did.
  - Medians: 231K for the question titles, against 205K for its other recent Shorts.
- **Why it matters:** the soccer leader now mixes timely explainers with the evergreen list stories, and the timely ones hold up. MetaSports NBA already shows news works for us.
- **Action:** give MetaSports FC one news-question Short a week. Rules:
  - Pick the day after a big controversy.
  - The title is the question, read aloud as line 1.
  - The answer comes last.
  - Use footage from F1 and F2.
- **Caveats:** my question-title classifier is rough. Views on the newest Shorts are still growing.
- **Source:** `Research Notes/Ahmed Network Data (Oct 21, 2026)/AhmedsGoal_shorts.csv` (re-counted today).

**C2. All three Ahmed channels dropped ALL-CAPS titles in about May-July 2026.** [V, from our data]
- **What:** in early 2026 nearly all their titles used CAPS words ("NBA SCORES THAT LOOK FAKE BUT ARE 100% REAL"). In their newest 120 Shorts, only 2-6% do.
  - Goal: 7/120.
  - Basketball: 2/120.
  - Business: 2/120.
- **Why it matters:** the leaders moved to plain sentence case, which our FC titles already use. Within the switch-over months, CAPS titles didn't clearly win.
- **Action:** no CAPS in FC titles. NBA title style stays as tested.
- **Source:** the same CSVs.

**C3. Other channels: hashtags left the titles, and questions came in.** [H, yt-dlp title lists pulled today]
- **Golden Hoops (2.2M subs):**
  - Older titles carried "#Shorts #NBA" (80 of 80 in an older block). The newest 40 carry 0.
  - It still uses emojis and CAPS words.
- **HoopFlix (841K subs):**
  - 27 of its newest 40 titles are questions ("LeBron's Secret Jersey Lost NBA Millions?"). Only 2 of 80 older ones were.
  - Its newest-40 median is 119.5K views.
- **Why it matters:** together with C1, three of the biggest story channels moved to question titles in 2026. Our NBA "Why/Did/Is..." titles already match.
- **Action:** keep hashtags out of titles. Try question titles for FC news (C1).
- **Source:** live `yt-dlp --flat-playlist` listings of @GoldenHoopsProduction and @HoopFlix.

**C4. What I could not measure: 2026 changes in length, captions and music.** [n/a]
- **What:** YouTube now blocks video pages and downloads from this cloud ("Sign in to confirm you're not a bot"). Only flat title lists work. So I could not measure 2026 changes to length, hooks, captions or music.
- **Action:**
  - On the PC, run `yt-dlp` with cookies on 10 Shorts per channel from Jan 2026 and 10 from Oct 2026.
  - Compare duration, cuts in the first 3 s, caption style and music level, with `Tools/watch_short.py`.
- **Context:** Tubefilter's charts show the World Cup 2026 soccer boom on Shorts, e.g. Mischief Time, AI soccer skits, at 405M weekly views. Tubefilter expected it to fade after the tournament. [S]
  - Source: [Tubefilter, week of Jun 28, 2026](https://www.tubefilter.com/2026/06/29/top-50-most-viewed-youtube-channels-week-of-06-28-2026/)

---

## Open questions, for a later run
- Does Eleven v4 work on `/with-timestamps`? It's one test call (V1).
- Are `previous_text`/`next_text` billed? Read the `character-cost` header (V4).
- Do Reporting API reach reports include Shorts-feed impressions (Y3)?
- Is FC's audience mostly US or Europe? That decides the FC slot test (P1).
