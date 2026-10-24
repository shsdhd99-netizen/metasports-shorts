#!/usr/bin/env bash
# One-time setup for a cloud (Linux) session. Safe to run again.
#   bash Tools/cloud_setup.sh
# Needs network access "Full" on the cloud environment and ELEVENLABS_API_KEY set in the environment's settings.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
pip install -q pillow numpy yt-dlp opencv-python-headless faster-whisper "av>=11,<14" 2>&1 | tail -1 || true   # QA: footage_qc needs cv2; export_check speech-to-text needs faster-whisper (PyAV 14+ breaks it)
command -v certutil >/dev/null || apt-get install -y -q libnss3-tools >/dev/null 2>&1 || true
# Chromium (webshot.mjs) must trust the cloud proxy's certificate, or every page shows "Your connection is not private"
if command -v certutil >/dev/null && [ -f /root/.ccr/agent-proxy-ca.crt ]; then
  mkdir -p "$HOME/.pki/nssdb"
  [ -f "$HOME/.pki/nssdb/cert9.db" ] || certutil -d "sql:$HOME/.pki/nssdb" -N --empty-password
  certutil -d "sql:$HOME/.pki/nssdb" -A -t "C,," -n ccr-agent-proxy -i /root/.ccr/agent-proxy-ca.crt 2>/dev/null || true
fi
[ -f "$HERE/.env" ] || cp "$HERE/.env.cloud" "$HERE/.env" 2>/dev/null || true   # voice id only; the key comes from the environment
echo "ffmpeg: $(ffmpeg -version 2>/dev/null | head -1 | cut -c1-30)  node: $(node -v 2>/dev/null)  key: ${ELEVENLABS_API_KEY:+set}${ELEVENLABS_API_KEY:-MISSING}" | sed 's/key: set.*/key: set/'
for h in www.basketball-reference.com www.espn.com x.com api.elevenlabs.io; do printf "%s %s\n" "$h" "$(curl -s -o /dev/null -m 10 -w '%{http_code}' https://$h/)"; done
