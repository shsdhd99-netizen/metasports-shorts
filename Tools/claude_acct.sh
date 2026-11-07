#!/usr/bin/env bash
# Start Claude on the PC as one of the three labelled accounts, each with its own saved login, in bypass mode, already briefed.
#   A1 = Account 1, BUILDER            bash Tools/claude_acct.sh 1
#   A2 = Account 2, BUILDER (backup)   bash Tools/claude_acct.sh 2      (when A1 is out of usage; never both at once)
#   A3 = Account 3, PREP + REVIEW      bash Tools/claude_acct.sh 3      (runs AT THE SAME TIME as the builder, in its own repo copy)
#   Optional first task:               bash Tools/claude_acct.sh 2 "build today's FC Short"
# The label shows in the window title, on every commit ("[A3 Prep + Review] ..."), on TEAM BOARD.md and in the handoffs.
# The accounts talk through Tools/team.py (messages, claims, status); unread messages are pasted into the start prompt.
# First time per account: Claude asks you to log in once (pick that account); after that it remembers.
cd "$(dirname "$0")/.." || exit 1
N="${1:-}"; TASK="${2:-}"
case "$N" in 1|2|3) ;; *) echo "Usage: bash Tools/claude_acct.sh 1|2|3 [\"first task\"]"; exit 1;; esac
case "$N" in 1) LABEL="A1"; ROLE="Builder";; 2) LABEL="A2"; ROLE="Builder (backup)";; 3) LABEL="A3"; ROLE="Prep + Review";; esac
if [ "$N" = 3 ]; then                                     # own copy of the repo, so two sessions never share one working folder
  PREP="$HOME/Documents/metasports-prep"
  if [ ! -d "$PREP/.git" ]; then
    echo "First run: making the prep copy at $PREP ..."
    git clone -q --branch main-329h3w "$(git remote get-url origin)" "$PREP" || { echo "Clone failed"; exit 1; }
  fi
  [ -f Tools/.env ] && cp -u Tools/.env "$PREP/Tools/.env"   # same keys (never printed, never committed: Tools/.env is git-ignored)
  cd "$PREP" || exit 1
fi
export MS_ACCOUNT="$LABEL"
export CLAUDE_CONFIG_DIR="$HOME/.claude-account$N"      # separate login + settings per account
mkdir -p "$CLAUDE_CONFIG_DIR"
printf '\033]0;Claude %s - %s\007' "$LABEL" "$ROLE"      # window title, so you can tell the windows apart
# Every commit from this folder gets the label of whoever made it (reads MS_ACCOUNT at commit time, so A1 and A2 can share it).
cat > .git/hooks/prepare-commit-msg <<'HOOK'
#!/usr/bin/env bash
[ -n "$MS_ACCOUNT" ] || exit 0
case "$MS_ACCOUNT" in A1) R="Builder";; A2) R="Builder (backup)";; A3) R="Prep + Review";; *) R="";; esac
head -1 "$1" | grep -q '^\[' || sed -i "1s/^/[$MS_ACCOUNT $R] /" "$1"
HOOK
chmod +x .git/hooks/prepare-commit-msg
git restore "Research Notes/Watch Reports/index.csv" 2>/dev/null
git pull -q --no-rebase --no-edit origin main-329h3w
python Tools/voiceover.py --check 2>/dev/null | tail -1
python Tools/team.py status "starting a session" "reading the inbox and handoff" >/dev/null 2>&1
INBOX="$(python Tools/team.py inbox 2>/dev/null | head -20)"
bash Tools/handoff.sh "PC account $N (start)" >/dev/null 2>&1
TEAMRULES="You are $LABEL ($ROLE). Team protocol (TEAM HANDOFF.md): run 'python Tools/team.py inbox' now and after every finished task (add --ack once you've acted on them); 'python Tools/team.py claim \"<task>\"' before starting any Short or task (if it says already claimed, pick another); 'python Tools/team.py done \"<task>\"' when finished; 'python Tools/team.py status \"now\" \"next\"' when you switch tasks; 'python Tools/team.py say <A1|A2|A3|CLOUD|BUILDER|ALL> \"...\"' to hand something over. Unread for you right now: ${INBOX:-none}."
if [ "$N" = 3 ]; then
  PROMPT="$TEAMRULES You work in the prep copy of the repo. Read \"Research Notes/ACCOUNT 3 - Prep and Review.md\" and follow it exactly (never voice, render, upload or touch slots), then ${TASK:-run the loop in that file until the queue is prepped and every new DRAFT is reviewed}. Commit only your own files (never git add -A) and push small and often (git pull --no-rebase first). Before you stop (or if you hit a usage limit), run: bash Tools/handoff.sh \"PC account 3\" \"<one line: what's done, what's next>\""
else
  PROMPT="$TEAMRULES Read \"HANDOFF - latest.md\", \"HANDOFF - prep (account 3).md\" and the newest Daily Log entries, then ${TASK:-continue the open work: build PREP-ready folders first and apply each REVIEW.md before a Short is scheduled}. Commit and push small and often. Before you stop (or if you hit a usage limit), run: bash Tools/handoff.sh \"PC account $N\" \"<one line: what's done, what's next>\""
fi
echo "Starting Claude as $LABEL - $ROLE (bypass mode)..."
claude --dangerously-skip-permissions "$PROMPT"
python Tools/team.py status "offline (session ended)" "-" >/dev/null 2>&1
bash Tools/handoff.sh "PC account $N (end)" >/dev/null 2>&1 && echo "Handoff saved for the next session."
