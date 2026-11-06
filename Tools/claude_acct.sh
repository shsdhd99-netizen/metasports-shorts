#!/usr/bin/env bash
# Start Claude on the PC as Account 1, 2 or 3, each with its own saved login, in bypass mode, already briefed.
# Accounts 1 and 2 are the BUILDER (one at a time). Account 3 is PREP + REVIEW only and works in its own copy of the repo
# (~/Documents/metasports-prep), so it can run at the same time as the builder without touching its files.
# Usage (Git Bash):  bash Tools/claude_acct.sh 1   |   bash Tools/claude_acct.sh 2   |   bash Tools/claude_acct.sh 3 (prep + review)
#                    bash Tools/claude_acct.sh 2 "build today's FC Short"     (optional first task)
# First time per account: Claude asks you to log in once (pick that account); after that it remembers.
# Switching: just quit (Ctrl+C twice) and run the other number. The handoff is written for you both ways.
cd "$(dirname "$0")/.." || exit 1
N="${1:-}"; TASK="${2:-}"
case "$N" in 1|2|3) ;; *) echo "Usage: bash Tools/claude_acct.sh 1|2|3 [\"first task\"]"; exit 1;; esac
if [ "$N" = 3 ]; then                                     # own copy of the repo, so two sessions never share one working folder
  PREP="$HOME/Documents/metasports-prep"
  if [ ! -d "$PREP/.git" ]; then
    echo "First run: making the prep copy at $PREP ..."
    git clone -q --branch main-329h3w "$(git remote get-url origin)" "$PREP" || { echo "Clone failed"; exit 1; }
  fi
  [ -f Tools/.env ] && cp -u Tools/.env "$PREP/Tools/.env"   # same keys (never printed, never committed: Tools/.env is git-ignored)
  cd "$PREP" || exit 1
fi
export CLAUDE_CONFIG_DIR="$HOME/.claude-account$N"      # separate login + settings per account
mkdir -p "$CLAUDE_CONFIG_DIR"
git restore "Research Notes/Watch Reports/index.csv" 2>/dev/null
git pull -q --no-rebase --no-edit origin main-329h3w
python Tools/voiceover.py --check 2>/dev/null | tail -1
bash Tools/handoff.sh "PC account $N (start)" >/dev/null 2>&1
if [ "$N" = 3 ]; then
  PROMPT="You are Account 3 on the owner's PC: PREP + REVIEW only, in the prep copy of the repo. Read \"Research Notes/ACCOUNT 3 - Prep and Review.md\" and follow it exactly (never voice, render, upload or touch slots), then ${TASK:-run the loop in that file until the queue is prepped and every new DRAFT is reviewed}. Commit only your own files and push small and often (git pull --no-rebase first). Before you stop (or if you hit a usage limit), run: bash Tools/handoff.sh \"PC account 3\" \"<one line: what's done, what's next>\""
else
PROMPT="You are Account $N on the owner's PC. Read \"HANDOFF - latest.md\" and the newest Daily Log entries, then ${TASK:-continue the open work}. Commit and push small and often. Before you stop (or if you hit a usage limit), run: bash Tools/handoff.sh \"PC account $N\" \"<one line: what's done, what's next>\""
fi
echo "Starting Claude as Account $N (bypass mode)..."
claude --dangerously-skip-permissions "$PROMPT"
bash Tools/handoff.sh "PC account $N (end)" >/dev/null 2>&1 && echo "Handoff saved for the next session."
