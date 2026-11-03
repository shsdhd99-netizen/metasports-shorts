"""Preflight for unattended runs (Nov 3, 2026). Zero Claude credits, prints no secrets, uploads nothing.

  python Tools/preflight.py            # check everything, write Research Notes/Preflight.md, exit 1 if a BLOCKER is found
  python Tools/preflight.py --quiet    # only the verdict line

BLOCKER = a run would die or skip mid-build (no voice key, voice credit under the next Short, dead upload token, disk under 5 GB,
ffmpeg missing). WARN = fix soon (token about to age out, usage file stale, scheduled task missing). The daily run starts with this
and, on a BLOCKER, writes one `STATUS: skipped, <reason>` line and does only the zero-credit steps.
"""
import argparse, datetime as dt, json, os, shutil, subprocess, sys, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RN = os.path.join(ROOT, "Research Notes")
ET = dt.timezone(dt.timedelta(hours=-5))  # EST (after Nov 1); only used for display
rows = []


def add(level, name, detail):
    rows.append((level, name, detail))


def load_env():
    env, p = {}, os.path.join(HERE, ".env")
    if os.path.exists(p):
        for ln in open(p, encoding="utf-8-sig"):
            if "=" in ln and not ln.lstrip().startswith("#"):
                k, v = ln.rstrip("\r\n").split("=", 1)
                env[k.strip()] = v.strip()
    for k, v in os.environ.items():
        env.setdefault(k, v)
    return env


def run(cmd, timeout=30):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout, cwd=ROOT)
        return r.returncode, (r.stdout + r.stderr).strip()
    except Exception as e:  # missing binary, timeout
        return 127, str(e)


def http_json(url, data=None, headers=None, timeout=20):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method="POST" if data else "GET")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    env = load_env()

    # tools
    for tool, args in (("ffmpeg", ["-version"]), ("yt-dlp", ["--version"]), ("git", ["--version"]), ("node", ["-v"])):
        rc, out = run([tool] + args)
        add("OK" if rc == 0 else ("BLOCKER" if tool in ("ffmpeg", "git") else "WARN"), tool, out.splitlines()[0][:60] if rc == 0 else "not found")

    # disk
    free = shutil.disk_usage(ROOT).free / 1e9
    add("BLOCKER" if free < 5 else "WARN" if free < 30 else "OK", "disk free", f"{free:.0f} GB on {os.path.splitdrive(ROOT)[0] or '/'} (a render needs about 1-3 GB; clips and src pile up)")

    # keys present (names only)
    for k, need in (("ELEVENLABS_API_KEY", True), ("ELEVENLABS_VOICE_ID", False), ("GEMINI_API_KEY", False), ("YT_CLIENT_ID", True),
                    ("YT_CLIENT_SECRET", True), ("YT_REFRESH_TOKEN", False), ("YT_REFRESH_TOKEN_FC", False), ("YT_UPLOAD_TOKEN", True), ("YT_UPLOAD_TOKEN_FC", True)):
        add("OK" if env.get(k) else ("BLOCKER" if need else "WARN"), f"key {k}", "set" if env.get(k) else "MISSING")

    # ElevenLabs credit
    if env.get("ELEVENLABS_API_KEY"):
        try:
            d = http_json("https://api.elevenlabs.io/v1/user/subscription", headers={"xi-api-key": env["ELEVENLABS_API_KEY"]})
            used, lim = d.get("character_count", 0), d.get("character_limit", 0)
            left = lim - used
            reset = dt.datetime.fromtimestamp(d.get("next_character_count_reset_unix", 0), ET).strftime("%b %d") if d.get("next_character_count_reset_unix") else "?"
            add("BLOCKER" if left < 3000 else "WARN" if left < 15000 else "OK", "ElevenLabs credit", f"{left:,} characters left of {lim:,} (resets {reset}); a Short uses 1.2K-4K with retakes")
        except Exception as e:
            add("WARN", "ElevenLabs credit", f"could not read ({str(e)[:60]})")

    # YouTube tokens: ask Google for an access token (reads nothing, uploads nothing)
    for ch, key in (("nba", "YT_UPLOAD_TOKEN"), ("fc", "YT_UPLOAD_TOKEN_FC"), ("nba analytics", "YT_REFRESH_TOKEN"), ("fc analytics", "YT_REFRESH_TOKEN_FC")):
        if not (env.get(key) and env.get("YT_CLIENT_ID") and env.get("YT_CLIENT_SECRET")):
            continue
        try:
            data = urllib.parse.urlencode({"client_id": env["YT_CLIENT_ID"], "client_secret": env["YT_CLIENT_SECRET"],
                                           "refresh_token": env[key], "grant_type": "refresh_token"}).encode()
            http_json("https://oauth2.googleapis.com/token", data=data)
            add("OK", f"token {ch}", "refresh works")
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")[:80]
            add("BLOCKER" if "upload" in key.lower() else "WARN", f"token {ch}", f"REJECTED ({e.code}: {body}); re-run Tools/yt_auth.py --channel {ch.split()[0]}; if it dies every 7 days, publish the Google app")
        except Exception as e:
            add("WARN", f"token {ch}", f"could not test ({str(e)[:60]})")

    # git
    rc, out = run(["git", "status", "-sb"])
    first = out.splitlines()[0] if out else "?"
    add("OK" if rc == 0 and "behind" not in first else "WARN", "git", first[:80])

    # builder and usage files
    bp = os.path.join(RN, "BUILDER.txt")
    add("OK" if os.path.exists(bp) else "WARN", "BUILDER.txt", open(bp).read().strip() if os.path.exists(bp) else "missing (both runs may build)")
    up = os.path.join(RN, "USAGE.txt")
    if os.path.exists(up):
        age = (dt.datetime.now() - dt.datetime.fromtimestamp(os.path.getmtime(up))).total_seconds() / 3600
        txt = open(up, encoding="utf-8").read().strip().splitlines()[0] if os.path.getsize(up) else ""
        add("WARN" if age > 24 else "OK", "USAGE.txt", f"{txt[:60]} (updated {age:.0f} h ago)")
    else:
        add("WARN", "USAGE.txt", "missing: headless runs cannot obey the usage guard (owner: write `weekly 40` and the date)")

    # scheduled tasks (Windows)
    if os.name == "nt":
        rc, out = run(["powershell", "-NoProfile", "-Command", "Get-ScheduledTask | Where-Object {$_.TaskName -like '*MetaSports*'} | ForEach-Object { $_.TaskName }"])
        names = out.splitlines() if rc == 0 else []
        for need in ("MetaSports analytics", "MetaSports schedule ready AM", "MetaSports schedule ready PM", "MetaSports daily nba", "MetaSports daily fc"):
            add("OK" if need in names else "WARN", f"task {need}", "registered" if need in names else "NOT registered (owner: see the handoff)")

    # last analytics pull
    api = os.path.join(RN, "Studio exports", "api")
    if os.path.isdir(api):
        days = sorted(f[6:16] for f in os.listdir(api) if f.startswith("daily "))
        if days:
            age = (dt.date.today() - dt.date.fromisoformat(days[-1])).days
            add("OK" if age <= 2 else "WARN", "analytics pull", f"newest daily file {days[-1]} ({age} d old)")

    blockers = [r for r in rows if r[0] == "BLOCKER"]
    verdict = f"PREFLIGHT {'BLOCKED: ' + '; '.join(b[1] for b in blockers) if blockers else 'OK'} ({sum(1 for r in rows if r[0] == 'WARN')} warnings)"
    lines = [f"# Preflight ({dt.datetime.now():%Y-%m-%d %H:%M})", "", f"**{verdict}**", "", "| Level | Check | Detail |", "|---|---|---|"]
    lines += [f"| {l} | {n} | {d} |" for l, n, d in rows]
    open(os.path.join(RN, "Preflight.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    if a.quiet:
        print(verdict)
    else:
        for l, n, d in rows:
            print(f"{l:8} {n:32} {d}")
        print(verdict)
    sys.exit(1 if blockers else 0)


if __name__ == "__main__":
    main()
