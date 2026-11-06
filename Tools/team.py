"""Team board for the Claude accounts working on MetaSports (Nov 6, 2026).

Who is who (labels show in the terminal title, every commit, the board and the handoff):
  A1    = Account 1, BUILDER      (voice, render, QA, schedule; PC)
  A2    = Account 2, BUILDER      (backup builder when A1 is out of usage; PC)
  A3    = Account 3, PREP+REVIEW  (scripts, sources, footage plans, draft reviews, 72-h judgments; PC, own repo copy)
  CLOUD = the claude.ai app session and its scheduled runs (research, stats, re-plans)

Everything lives in git under Team/, one file per writer, so two accounts never edit the same file:
  Team/status/<LABEL>.md          what that account is doing now, next, and what it finished today
  Team/messages/<time>-<FROM>-to-<TO>.md   one file per message (TO = A1, A2, A3, CLOUD, BUILDER = A1+A2, ALL)
  Team/acks/<LABEL>.txt           message ids that account has read
  Team/claims/<slug>.md           "I'm doing this" locks, so two accounts never build or prep the same Short
  TEAM BOARD.md                   generated summary for the owner (status of everyone + open claims + unread counts)

  python Tools/team.py whoami
  python Tools/team.py status "now: prepping S30 Kane" "next: review Klay draft"
  python Tools/team.py say A3 "Klay DRAFT pushed, please review"        (or BUILDER / ALL)
  python Tools/team.py inbox            show unread messages for me;  --ack marks them read
  python Tools/team.py claim "S30 Kane prep"     refuses if someone else holds it
  python Tools/team.py done "S30 Kane prep"      releases the claim and adds it to my "done today"
  python Tools/team.py board            print the board (and rewrite TEAM BOARD.md)
Every write pulls first, commits only Team/ files + TEAM BOARD.md, and pushes (retries a merge 3 times). No keys, ever.
"""
import datetime as dt, glob, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEAM = os.path.join(ROOT, "Team")
BOARD = os.path.join(ROOT, "TEAM BOARD.md")
BRANCH = "main-329h3w"
ROLES = {"A1": "Builder", "A2": "Builder (backup)", "A3": "Prep + Review", "CLOUD": "Research + scheduled runs"}
GROUPS = {"ALL": set(ROLES), "BUILDER": {"A1", "A2"}}


def me():
    lab = os.environ.get("MS_ACCOUNT", "").upper()
    if lab in ROLES:
        return lab
    m = re.search(r"account(\d)$", os.environ.get("CLAUDE_CONFIG_DIR", ""))
    if m and f"A{m.group(1)}" in ROLES:
        return f"A{m.group(1)}"
    return "CLOUD" if os.path.exists("/root/.ccr") else "A1"


def now():
    return dt.datetime.now(dt.timezone.utc)


def stamp(t=None):
    return (t or now()).strftime("%Y%m%d-%H%M%S")


def nice(t=None):
    try:
        from zoneinfo import ZoneInfo
        t = (t or now()).astimezone(ZoneInfo("America/New_York"))
        return t.strftime("%a %b %d, %I:%M %p ET").replace(" 0", " ")
    except Exception:
        return (t or now()).strftime("%a %b %d %H:%M UTC")


def git(*a, check=False):
    r = subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True)
    if check and r.returncode:
        raise SystemExit(f"git {' '.join(a)} failed: {r.stderr.strip()[:300]}")
    return r


def pull():
    r = git("pull", "-q", "--no-rebase", "--no-edit", "origin", BRANCH)
    if r.returncode and "CONFLICT" in (r.stdout + r.stderr):
        fix_conflicts()


def fix_conflicts():
    """Only TEAM BOARD.md can conflict (every other Team file has one writer): regenerate it and finish the merge."""
    bad = [p for p in git("diff", "--name-only", "--diff-filter=U").stdout.split("\n") if p]
    if any(p != "TEAM BOARD.md" for p in bad):
        raise SystemExit(f"merge conflict outside the board, fix by hand: {bad}")
    git("checkout", "--theirs", "TEAM BOARD.md")
    write_board(quiet=True)
    git("add", "TEAM BOARD.md")
    git("commit", "-q", "--no-edit")


def sync(paths, msg):
    write_board(quiet=True)
    git("add", "--", *paths, BOARD)
    if not git("diff", "--cached", "--name-only").stdout.strip():
        return
    git("commit", "-q", "-m", f"[{me()} {ROLES[me()]}] team: {msg}")
    for _ in range(3):
        pull()
        if git("push", "-q", "origin", BRANCH).returncode == 0:
            return
    print("warning: push failed 3 times; the change is committed locally and goes up with the next push")


def path(*p):
    full = os.path.join(TEAM, *p)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    return full


def read_status(lab):
    f = os.path.join(TEAM, "status", f"{lab}.md")
    if not os.path.exists(f):
        return {}
    d = {}
    for line in open(f, encoding="utf-8"):
        m = re.match(r"- \*\*(\w[\w ]*):\*\* (.*)", line.strip())
        if m:
            d[m.group(1).lower()] = m.group(2)
    d["done"] = [l.strip()[2:] for l in open(f, encoding="utf-8") if l.startswith("  - ")]
    return d


def save_status(lab, now_txt=None, next_txt=None, add_done=None):
    d = read_status(lab)
    today = now().strftime("%Y-%m-%d")
    done = d.get("done", []) if d.get("day") == today else []
    if add_done:
        done.append(f"{nice().split(', ')[1]}: {add_done}")
    lines = [f"# {lab} · {ROLES[lab]}", "",
             f"- **Updated:** {nice()}",
             f"- **Day:** {today}",
             f"- **Now:** {now_txt if now_txt is not None else d.get('now', '-')}",
             f"- **Next:** {next_txt if next_txt is not None else d.get('next', '-')}",
             "- **Done today:**"] + [f"  - {x}" for x in done[-15:]]
    open(path("status", f"{lab}.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    return path("status", f"{lab}.md")


def messages():
    out = []
    for f in sorted(glob.glob(os.path.join(TEAM, "messages", "*.md"))):
        m = re.match(r"(\d{8}-\d{6})-(\w+)-to-(\w+)\.md$", os.path.basename(f))
        if m:
            out.append({"id": os.path.basename(f)[:-3], "t": m.group(1), "from": m.group(2), "to": m.group(3),
                        "text": open(f, encoding="utf-8").read().split("\n", 2)[-1].strip(), "file": f})
    return out


def acked(lab):
    f = os.path.join(TEAM, "acks", f"{lab}.txt")
    return set(open(f).read().split()) if os.path.exists(f) else set()


def for_me(msg, lab):
    return msg["from"] != lab and (msg["to"] == lab or lab in GROUPS.get(msg["to"], set()))


def unread(lab):
    a = acked(lab)
    return [m for m in messages() if for_me(m, lab) and m["id"] not in a]


def claims():
    out = []
    for f in sorted(glob.glob(os.path.join(TEAM, "claims", "*.md"))):
        txt = open(f, encoding="utf-8").read().strip().split("\n")
        out.append({"slug": os.path.basename(f)[:-3], "line": txt[-1] if txt else "", "file": f})
    return out


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]


def write_board(quiet=False):
    lines = ["# Team board (auto, do not edit by hand)", "", f"Updated {nice()} by {me()}.", "",
             "| Account | Role | Now | Next | Done today | Unread | Updated |", "|---|---|---|---|---|---|---|"]
    for lab in ROLES:
        d = read_status(lab)
        lines.append(f"| **{lab}** | {ROLES[lab]} | {d.get('now', '-')} | {d.get('next', '-')} | {len(d.get('done', [])) if d.get('day') == now().strftime('%Y-%m-%d') else 0} | "
                     f"{len(unread(lab))} | {d.get('updated', 'never')} |")
    cl = claims()
    lines += ["", "## Claimed (in progress)", ""] + ([f"- {c['line']}" for c in cl] or ["- nothing claimed"])
    recent = messages()[-8:]
    lines += ["", "## Last messages", ""] + ([f"- {m['t'][4:6]}/{m['t'][6:8]} {m['t'][9:11]}:{m['t'][11:13]} UTC, {m['from']} to {m['to']}: {m['text'][:140]}" for m in reversed(recent)] or ["- none"])
    for lab in ROLES:
        d = read_status(lab)
        if d.get("done") and d.get("day") == now().strftime("%Y-%m-%d"):
            lines += ["", f"## {lab} finished today", ""] + [f"- {x}" for x in d["done"]]
    open(BOARD, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    if not quiet:
        print("\n".join(lines))


def main():
    a = sys.argv[1:]
    cmd = a[0] if a else "board"
    lab = me()
    if cmd == "whoami":
        print(f"{lab} · {ROLES[lab]}")
    elif cmd == "status":
        pull()
        f = save_status(lab, a[1] if len(a) > 1 else None, a[2] if len(a) > 2 else None)
        sync([f], f"status: {a[1] if len(a) > 1 else ''}"[:70])
        print(f"{lab} status saved")
    elif cmd == "say":
        if len(a) < 3:
            raise SystemExit('usage: team.py say <A1|A2|A3|CLOUD|BUILDER|ALL> "message"')
        to = a[1].upper()
        if to not in ROLES and to not in GROUPS:
            raise SystemExit(f"unknown recipient {to}")
        pull()
        f = path("messages", f"{stamp()}-{lab}-to-{to}.md")
        open(f, "w", encoding="utf-8").write(f"# {lab} to {to}, {nice()}\n\n{' '.join(a[2:])}\n")
        sync([f], f"message to {to}")
        print(f"sent to {to}")
    elif cmd == "inbox":
        pull()
        u = unread(lab)
        if not u:
            print(f"{lab}: no unread messages")
        for m in u:
            print(f"[{m['id']}] from {m['from']} to {m['to']}: {m['text']}")
        if "--ack" in a and u:
            f = path("acks", f"{lab}.txt")
            with open(f, "a") as fh:
                fh.write("".join(m["id"] + "\n" for m in u))
            sync([f], f"read {len(u)} message(s)")
    elif cmd == "claim":
        task = " ".join(a[1:])
        pull()
        f = path("claims", f"{slug(task)}.md")
        if os.path.exists(f):
            raise SystemExit(f"already claimed: {open(f, encoding='utf-8').read().strip().splitlines()[-1]}")
        open(f, "w", encoding="utf-8").write(f"**{task}**: {lab}, since {nice()}\n")
        d = read_status(lab)
        sf = save_status(lab, f"{task}", d.get("next"))
        sync([f, sf], f"claim: {task}"[:70])
        print(f"claimed: {task}")
    elif cmd == "done":
        task = " ".join(a[1:])
        pull()
        f = os.path.join(TEAM, "claims", f"{slug(task)}.md")
        paths = []
        if os.path.exists(f):
            os.remove(f)
            paths.append(f)
        sf = save_status(lab, "-", None, add_done=task)
        sync(paths + [sf], f"done: {task}"[:70])
        print(f"done: {task}")
    elif cmd == "board":
        pull()
        write_board()
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
