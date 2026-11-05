#!/usr/bin/env bash
# Poll a YouTube Short's public stats and append them to a markdown log (Nov 5, 2026).
#   bash Tools/watch_short.sh <video_id> "<label>" <log.md> [interval_minutes] [rounds] [other_id_to_compare]
# Uses yt-dlp (public counts, no credits) and, when Tools/.env is loaded, the read-only API for title/privacy. Never edits anything.
id="$1"; label="$2"; log="$3"; every="${4:-30}"; rounds="${5:-12}"; other="${6:-}"
[ -f "$log" ] || printf '# %s\n\n| time ET | status | views | likes | comments | title |\n|---|---|---|---|---|---|\n' "$label" > "$log"
for i in $(seq 1 "$rounds"); do
  now=$(TZ=America/New_York date '+%a %H:%M')
  row=$(timeout 90 yt-dlp --skip-download --no-warnings --print "%(availability)s|%(view_count)s|%(like_count)s|%(comment_count)s|%(title).60s" "https://www.youtube.com/shorts/$id" 2>/dev/null | tail -1)
  [ -z "$row" ] && row="not public yet|||||"
  echo "| $now | $(echo "$row" | tr '|' '|' | sed 's/|/ | /g') |" >> "$log"
  if [ -n "$other" ]; then
    o=$(timeout 90 yt-dlp --skip-download --no-warnings --print "%(view_count)s" "https://www.youtube.com/shorts/$other" 2>/dev/null | tail -1)
    echo "|  | (old copy $other) | ${o:-n/a} | | | |" >> "$log"
  fi
  sleep $((every*60))
done
echo "watch finished $(TZ=America/New_York date '+%a %H:%M')" >> "$log"
