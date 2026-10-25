# Upload schedule (from Oct 24, 2026): follow it every day

**Every day, both channels:**
| Time (ET) | Channel | What to post |
|---|---|---|
| **11:00 AM** | MetaSports (NBA) | The NBA Hub card marked for today. News Shorts first: they only work the day after the game. |
| **12:00 PM** | MetaSports FC | The FC Hub card marked for today. |
| **6:00 PM** (only when the Hub has a second ready NBA card) | MetaSports (NBA) | An evergreen one (a record, not news), e.g. #60 Caitlin Clark. |

**How to post (2 minutes each):** open the Hub, play the video, tap Download, upload it as a Short in the YouTube app, paste the
title (Copy button), set "Not made for kids", add the pinned comment from the card. Nothing is ever posted for you.

**Strict rules:**
1. One soccer Short a day, never two on the same day (S02 went out the same day as S01 and stalled).
2. A news Short that misses its day is skipped, not posted late (#63, a day late: 58% stayed vs 75-80% same day).
3. At least 4 hours between two posts on the same channel.
4. 24 hours after posting, type the numbers into the card's Results box (views, "Stayed to watch" %).
5. **Every Sunday:** in YouTube Studio, Content tab, Shorts, export the table for both channels and send the two zips to a Claude
   session. "Stayed to watch" is only in Studio; it is the number that decides whether YouTube keeps pushing a Short.

**The next four days:**
| Day | NBA 11:00 AM | Soccer 12:00 PM | NBA 6:00 PM |
|---|---|---|---|
| Sat Oct 24 | **#66 Why SGA Ended His Own NBA Record** (post now; the game was Thursday) | **S06** The player who scored 5 goals in 9 minutes (if not posted yet) | |
| Sun Oct 25 | **#60** Caitlin Clark Did What No NBA Player Has (moved up: the morning run could not record) | **S05** Goalkeepers who hid a cheat sheet on their water bottle (music version) | **#68**, today's NBA news Short (made this afternoon) |
| Mon Oct 26 | the new NBA news Short | **S07** The team with worse odds than the Loch Ness monster (no-music version) | |
| Tue Oct 27 | the new NBA news Short | **S04** Players who got sent off in their very last game (music version) | |
| Wed Oct 28 on | a new NBA Short every morning | a new soccer Short every day (S08 Hand of God shirt next) | |

**TikTok and Instagram (from Oct 25; full research: `Research Notes/TikTok and Instagram Playbook (Oct 25, 2026).md`):**
- **Post the same Short on TikTok and Instagram in the same sitting as YouTube**, from the same Hub card. One sitting a Short keeps
  it simple; after about 3 weeks we move the times to what each app's own analytics show.
- **Which file:**
  - **Soccer:** the **long cut** (over 1 minute, the "TikTok-IG long" tab on the card). TikTok only pays on videos over 1 minute,
    and longer story videos get more views there. YouTube keeps the under-60 s cut.
  - **NBA:** the same file as YouTube. NBA Shorts are 20-45 s, and padding them hurts. We'll test a 62-70 s TikTok cut on
    5-10 stories that naturally run long.
- **Text:** paste the card's TikTok caption or Instagram caption (Copy buttons). The searchable phrase comes first; 3-4 hashtags on
  TikTok, at most 5 on Instagram.
- **Always upload our clean file from the Hub.** Never a video saved from TikTok or YouTube: another app's watermark keeps it off
  TikTok's For You feed and out of Instagram's recommendations.
- **TikTok:** upload from TikTok Studio on the web (tiktok.com/tiktokstudio/upload) so it stays 1080p; no AI label needed for a
  generic narrator voice.
- **Instagram:** turn on the **AI label** before sharing (Meta requires it for AI-made realistic audio; our narration is an AI voice).

**Set up once (on your phone, about 10 minutes per account; names, bios and pictures are in each Hub's brand kit):**
1. **TikTok, two accounts** (MetaSports and MetaSports FC). Sign up with a different email for each. Keep them **Personal**
   accounts: a Business account can never join Creator Rewards (TikTok's pay program: 10,000 followers and 100,000 views in 30
   days, then it pays on videos over 1 minute). Usernames: @metasports / @metasportsfc (fallbacks in the brand kit). Paste the
   bio, add the profile picture. **No phone number or email in the bio** (a Creator Rewards rule).
2. **Instagram, two accounts** (or reuse ones you have). Settings > Account type > **Professional > Creator**, keep it public,
   paste the name, bio and picture.
3. Tell a Claude session the four usernames, so the Hubs and notes can link them.

**What runs by itself (scheduled tasks, every day):**
- **6:41 AM ET, MetaSports NBA daily run:** pulls the NBA channel's analytics and retention curves, logs them, researches last
  night's games, makes the day's NBA Short (QA must pass), puts it on the NBA Hub for 11:00 AM, commits it.
- **9:39 AM ET, MetaSports FC daily run:** the same for the soccer channel; its Short goes in the next free noon slot.
- Each run writes what it pulled, found and changed in `Research Notes/Daily Log.md`. Sundays add a weekly review.
- Both follow `.claude/skills/daily-run/SKILL.md`.

**What only you can do (once):**
1. Add `ELEVENLABS_API_KEY` in the cloud environment's settings (the environment menu in the session's title bar, then Edit), so
   the automatic runs can record voices. Without it they write scripts only.
2. For retention curves: add `YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN` (NBA channel) and `YT_REFRESH_TOKEN_FC`
   (soccer channel) the same way. One read-only sign-in per channel, no PC needed: the 4 steps are at the top of `Tools/yt_analytics.py` ("NO PC"). Publish the Google
   app first (OAuth consent screen, "Publish app"), or the sign-in expires after 7 days.
