---
name: channel-check
description: >
  Free MetaSports health check: runs Tools\channel_check.py (public numbers via yt-dlp), then explains
  in plain English what worked, what flopped and the one thing to do next. Use when the user types
  /channel-check or asks how the channel is doing.
---

# /channel-check

ROOT = `C:\Users\Admin\Documents\YouTube-Playbooks`.

1. **Run** `python channel_check.py` from `ROOT\Tools`, with PYTHONIOENCODING=utf-8. Add a handle argument to check another channel.
2. **Read** `ROOT\Tools\data\channel_log.csv` to see the trend across runs.
3. **Reply in at most 6 short lines:**
   - the trend
   - the best Short, and why it likely worked (topic, opener, ending; compare with the playbook)
   - any FLOP, and what to check
   - ONE action for next week
4. **Any WINNER?** Offer to write the follow-up with /nba-short.
