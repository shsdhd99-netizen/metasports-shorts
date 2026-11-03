#!/usr/bin/env bash
# Re-render both preview versions. If the Hedra clips are in work/ they replace the photo placeholders:
#   work/open_talk.mp4, work/close_talk.mp4            (16:9)
#   work/open_talk_9x16.mp4, work/close_talk_9x16.mp4  (9:16; if missing, the 16:9 clips are centre-cropped)
set -euo pipefail
cd "$(dirname "$0")"
for c in open_talk close_talk open_talk_9x16 close_talk_9x16; do
  [ -f "$c.mp4" ] && echo "using $c.mp4" || echo "missing $c.mp4 (photo placeholder or 16:9 crop is used)"
done
python3 render.py both
