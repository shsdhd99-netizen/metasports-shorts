#!/usr/bin/env bash
# One-command terminal prep (Nov 3, 2026): restore the regenerated index, pull, fix .env permissions, check keys. Prints no secrets.
cd "$(dirname "$0")/.." || exit 1
git restore "Research Notes/Watch Reports/index.csv" 2>/dev/null
git pull --no-rebase --no-edit origin main-329h3w
chmod 600 /c/Users/Admin/.config/watch/.env 2>/dev/null && echo "watch .env: permissions fixed"
python Tools/voiceover.py --check
bash Tools/cloud_setup.sh
git status -sb | head -1
echo "Ready. Now run: bash Tools/claude_acct.sh 1   (or 2)"
