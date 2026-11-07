#!/usr/bin/env bash
# Pack one Short for the Hub (the Hub asset limit is 20 MiB; READY mp4s are ~25 MB).
# Usage: Tools/hub_pack.sh "Productions/MetaSports/<folder>" [more folders...]
# Writes <folder>/_hub/s.mp4 (crf 24, aac 128k) from final.mp4 and <folder>/_hub/cover_A.jpg from cover_A.png.
# Also refreshes the "READY TO POST - *.mp4" copy so it always equals final.mp4.
set -euo pipefail
for f in "$@"; do
  [ -f "$f/final.mp4" ] || { echo "SKIP (no final.mp4): $f"; continue; }
  mkdir -p "$f/_hub"
  ffmpeg -loglevel error -y -i "$f/final.mp4" -c:v libx264 -crf 24 -preset medium -c:a aac -b:a 128k "$f/_hub/s.mp4"
  for c in A B C; do
    [ -f "$f/cover_$c.png" ] && ffmpeg -loglevel error -y -i "$f/cover_$c.png" -q:v 3 "$f/_hub/cover_$c.jpg" || true
  done
  for r in "$f"/READY\ TO\ POST*.mp4; do
    [ -f "$r" ] && cp "$f/final.mp4" "$r"
  done
  printf '%s  hub %s MB\n' "$(basename "$f")" "$(du -m "$f/_hub/s.mp4" | cut -f1)"
done
