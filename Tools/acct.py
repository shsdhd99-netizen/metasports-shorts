r"""One terminal, three Claude accounts (Nov 6, 2026; owner: "run all 3 accounts from 1 terminal and get my money's worth").

  python Tools/acct.py status                      # who is logged in, rough tokens used in the last 5 h / 7 days per account, who is marked limited
  python Tools/acct.py login 2                     # prints the one-time login steps for account 2 (login is always done by you, in the browser)
  python Tools/acct.py run 2 "task text"           # run one headless task as account 2 (claude -p, bypass mode) and print the answer
  python Tools/acct.py run auto "task text"        # first account that is logged in and not limited (order: 1, 2, 3, or --prefer 3)
  python Tools/acct.py fanout "task A" "task B" "task C"   # one task per available account, in parallel, prints each answer
  python Tools/acct.py clear 2                     # remove the "limited" mark early

How it works: every account has its own login folder (CLAUDE_CONFIG_DIR = ~/.claude-account1/2/3, the same folders Tools/claude_acct.sh uses), so a task run
as account N is billed to account N only. A run that answers with a usage-limit message marks that account limited until the reset time in the message (else
+5 h) in ~/.claude-accounts-state.json, and `auto` moves on to the next one; a limited account is never retried before its reset. Nothing here hides which
account is used: every run is logged (account, time, first 80 chars of the task) in Research Notes/Acct Log.csv. Weekly cap guard: set MAX_WEEKLY_TOKENS below to
stop using an account you want to keep a reserve on. Needs no keys. Headless runs cannot answer prompts, so give them tasks that need no questions.
Limit: Anthropic's terms apply to each account separately; this tool only chooses which of YOUR OWN logged-in accounts runs a task.
"""
import argparse, concurrent.futures as cf, csv, datetime as dt, glob, json, os, re, subprocess, sys, time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HOME = os.path.expanduser("~")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(HOME, ".claude-accounts-state.json")
LOG = os.path.join(ROOT, "Research Notes", "Acct Log.csv")
ACCTS = {1: "A1 Builder", 2: "A2 Builder (backup)", 3: "A3 Prep + Review"}
MAX_WEEKLY_TOKENS = {1: None, 2: None, 3: None}  # e.g. {2: 40_000_000} keeps a reserve; None = no cap
LIMIT_RE = re.compile(r"(usage limit|limit reached|rate limit|5-hour limit|weekly limit|out of (extra )?usage|you've hit your)", re.I)
RESET_RE = re.compile(r"resets?\s*(?:at|on)?\s*(\d{1,2})(?::(\d{2}))?\s*(am|pm)", re.I)


def cdir(n):
    return os.path.join(HOME, f".claude-account{n}")


def state():
    return json.load(open(STATE, encoding="utf-8")) if os.path.exists(STATE) else {}


def save(s):
    json.dump(s, open(STATE, "w", encoding="utf-8"), indent=1)


def email(n):
    p = os.path.join(cdir(n), ".claude.json")
    if not os.path.exists(p):
        return None
    m = re.search(r'"emailAddress":\s*"([^"]+)"', open(p, encoding="utf-8", errors="ignore").read())
    return m.group(1) if m else None


def logged_in(n):
    return os.path.exists(os.path.join(cdir(n), ".credentials.json")) and email(n) is not None


def tokens(n, hours):
    cut = time.time() - hours * 3600
    tot = 0
    for f in glob.glob(os.path.join(cdir(n), "projects", "**", "*.jsonl"), recursive=True):
        if os.path.getmtime(f) < cut:
            continue
        for l in open(f, encoding="utf-8", errors="ignore"):
            try:
                u = (json.loads(l).get("message") or {}).get("usage")
            except ValueError:
                continue
            if u:
                tot += (u.get("input_tokens") or 0) + (u.get("output_tokens") or 0) + (u.get("cache_creation_input_tokens") or 0)
    return tot


def limited_until(n):
    t = state().get(str(n), {}).get("limited_until")
    return dt.datetime.fromisoformat(t) if t else None


def available(n):
    if not logged_in(n):
        return False
    u = limited_until(n)
    if u and u > dt.datetime.now():
        return False
    cap = MAX_WEEKLY_TOKENS.get(n)
    return not (cap and tokens(n, 24 * 7) > cap)


def mark_limited(n, text):
    m = RESET_RE.search(text)
    now = dt.datetime.now()
    if m:
        h = int(m.group(1)) % 12 + (12 if m.group(3).lower() == "pm" else 0)
        until = now.replace(hour=h, minute=int(m.group(2) or 0), second=0, microsecond=0)
        if until <= now:
            until += dt.timedelta(days=1)
    else:
        until = now + dt.timedelta(hours=5)
    s = state(); s[str(n)] = {"limited_until": until.isoformat(timespec="minutes"), "note": text.strip()[:120]}; save(s)
    return until


def log(n, task):
    new = not os.path.exists(LOG)
    with open(LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["time", "account", "task"])
        w.writerow([dt.datetime.now().strftime("%Y-%m-%d %H:%M"), n, task[:80].replace("\n", " ")])


def run(n, task, timeout=3000):
    env = dict(os.environ, CLAUDE_CONFIG_DIR=cdir(n), MS_ACCOUNT=f"A{n}")
    env.pop("CLAUDE_CODE_OAUTH_TOKEN", None)
    log(n, task)
    r = subprocess.run(["claude", "-p", "--dangerously-skip-permissions", task], cwd=ROOT, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)
    out = (r.stdout or "") + (r.stderr or "")
    if LIMIT_RE.search(out[:600]) and len(out) < 800:
        return None, out, mark_limited(n, out)
    return out.strip(), "", None


def pick(prefer=None):
    order = [n for n in ([prefer] if prefer else []) + [1, 2, 3]]
    seen = []
    for n in order:
        if n not in seen:
            seen.append(n)
            if available(n):
                return n
    return None


def run_auto(task, prefer=None):
    while True:
        n = pick(prefer)
        if n is None:
            print("No account is available (not logged in, or all limited). `python Tools/acct.py status` shows the reset times.")
            return 1
        print(f"[running on account {n}: {ACCTS[n]}]")
        out, why, until = run(n, task)
        if out is not None:
            print(out); return 0
        print(f"account {n} is limited until {until:%a %H:%M}: {why.strip()[:100]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["status", "login", "run", "fanout", "clear"])
    ap.add_argument("args", nargs="*")
    ap.add_argument("--prefer", type=int)
    a = ap.parse_args()
    if a.cmd == "status":
        print(f"{'acct':5}{'role':24}{'login':34}{'5h tokens':>12}{'7d tokens':>14}  state")
        for n in (1, 2, 3):
            u = limited_until(n)
            st = "not logged in" if not logged_in(n) else (f"LIMITED until {u:%a %H:%M}" if u and u > dt.datetime.now() else "available")
            print(f"{n:<5}{ACCTS[n]:24}{(email(n) or '-'):34}{(tokens(n, 5) if logged_in(n) else 0):>12,}{(tokens(n, 168) if logged_in(n) else 0):>14,}  {st}")
        print("Token counts are this PC's transcripts only (a rough meter, not the plan's real percentage). Ask Claude for /usage inside each account for the real number.")
    elif a.cmd == "login":
        n = int(a.args[0])
        print(f"One-time login for account {n} ({ACCTS[n]}), done by you:\n  1) PowerShell:  $env:CLAUDE_CONFIG_DIR=\"$HOME\\.claude-account{n}\"; claude\n  2) In Claude type /login, pick the claude.ai account for slot {n}, finish in the browser.\n  3) Type /exit. Then `python Tools/acct.py status` shows it as available.")
    elif a.cmd == "run":
        who, task = a.args[0], " ".join(a.args[1:])
        if who == "auto":
            sys.exit(run_auto(task, a.prefer))
        n = int(who)
        out, why, until = run(n, task)
        print(out if out is not None else f"account {n} limited until {until:%a %H:%M}: {why.strip()[:120]}")
    elif a.cmd == "fanout":
        avail = [n for n in (1, 2, 3) if available(n)]
        tasks = a.args[:len(avail)]
        with cf.ThreadPoolExecutor(len(tasks) or 1) as ex:
            futs = {ex.submit(run, n, t): (n, t) for n, t in zip(avail, tasks)}
            for f in cf.as_completed(futs):
                n, t = futs[f]; out, why, until = f.result()
                print(f"=== account {n}: {t[:60]}\n{out if out is not None else 'limited until ' + str(until)}\n")
    elif a.cmd == "clear":
        s = state(); s.pop(a.args[0], None); save(s); print("cleared")


if __name__ == "__main__":
    main()
