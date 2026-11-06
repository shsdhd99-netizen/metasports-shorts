#!/usr/bin/env bash
# Write "HANDOFF - latest.md" so the next Claude session (either account, PC or cloud) knows where things stand.
# Usage: bash Tools/handoff.sh [account-label] ["note for the next session"]
# Prints no secrets: it reads git history, the Daily Log's STATUS lines and key PRESENCE only.
cd "$(dirname "$0")/.." || exit 1
ACCT="${1:-unknown}"; NOTE="${2:-}"
OUT="HANDOFF - latest.md"
case "$ACCT" in *"account 3"*) OUT="HANDOFF - prep (account 3).md";; esac   # the prep/review account never overwrites the builder's handoff
has() { [ -n "${!1}" ] || grep -qs "^$1=." Tools/.env && echo "set" || echo "MISSING"; }
{
  echo "# Handoff (auto), $(date '+%a %b %d %Y, %H:%M %Z'), written by account: $ACCT"
  echo
  echo "Read this first, then \`Research Notes/Daily Log.md\` (newest entries) before building anything, so two sessions never build the same Short."
  echo
  [ -n "$NOTE" ] && { echo "## Note from the last session"; echo "$NOTE"; echo; }
  [ "$OUT" = "HANDOFF - latest.md" ] && [ -f "HANDOFF - prep (account 3).md" ] && { echo "Prepped scripts and draft reviews from Account 3: \`HANDOFF - prep (account 3).md\` (build PREP-ready folders first; apply each REVIEW.md before a Short is scheduled)."; echo; }
  echo "## Keys on this machine (presence only)"
  for k in ELEVENLABS_API_KEY GEMINI_API_KEY YT_CLIENT_ID YT_REFRESH_TOKEN YT_REFRESH_TOKEN_FC YT_UPLOAD_TOKEN YT_UPLOAD_TOKEN_FC NETLIFY_AUTH_TOKEN HEYGEN_API_KEY; do
    echo "- $k: $(has $k)"
  done
  echo
  echo "## Newest STATUS lines (Daily Log)"
  grep -h "STATUS" "Research Notes/Daily Log.md" 2>/dev/null | head -5 | sed 's/^/- /'
  echo
  echo "## Last 15 commits (any account)"
  git log -15 --format='- %ad %s' --date=format:'%b %d %H:%M'
  echo
  echo "## Uncommitted here"
  git status --short | head -15 | sed 's/^/    /'
} > "$OUT"
git add -f "$OUT" && git commit -q -m "Handoff (auto) from $ACCT" && git pull -q --no-rebase --no-edit origin main-329h3w && git push -q origin main-329h3w && echo "Handoff written and pushed: $OUT"
