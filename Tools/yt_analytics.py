"""Read-only per-video YouTube Analytics for the MetaSports channel (views, average view duration, average % viewed, watch time).

Why (Oct 15, 2026): Metricool's per-video YouTube data stays empty after the reconnect, vidIQ is ruled out by the owner, and the
cloud must never open YouTube Studio. This uses Google's official YouTube Analytics API with READ-ONLY scopes. No pip installs:
standard library only.

ONE-TIME SETUP (on the PC, about 10 minutes; full steps in Tools Guide.md, "YouTube Analytics API"):
  1. console.cloud.google.com -> new project -> enable "YouTube Analytics API" and "YouTube Data API v3".
  2. OAuth consent screen: External, add your own Google account as a test user.
  3. Credentials -> Create OAuth client ID -> "Desktop app" -> Download JSON -> save it as Tools/client_secret.json
     (git-ignored; never commit it, never paste it in chat).
  4. python Tools/yt_analytics.py auth          # opens the browser once; sign in with the channel's account; allow READ-ONLY access
     The token is saved OUTSIDE the repo: %USERPROFILE%/.metasports/yt_token.json (or ~/.metasports/yt_token.json).

EVERY TIME:
  python Tools/yt_analytics.py pull --from 2026-09-16 --to 2026-10-14
      -> "Research Notes/Studio exports/api <from> to <to>.csv": video id, title, published, length (s), views,
         average view duration (s), average % viewed, watch minutes, likes, shares, subscribers gained
  python Tools/yt_analytics.py pull --from 2026-09-16 --engaged     # also asks for engagedViews; skipped if the API refuses it

DAILY (Oct 19, 2026; the owner asked for retention checks every day, automatically):
  python Tools/yt_analytics.py daily            # last 30 days of uploads: per-Short metrics + retention curves for Shorts < 14 days old
      -> "Research Notes/Studio exports/api/daily <date>.csv" and "retention <date>.csv", then prints the report
  python Tools/yt_analytics.py report           # flags from the newest daily files (no API call; the cloud can run this on PC-pushed files)
  Runs by itself: on the PC via Tools/daily_analytics.bat in Windows Task Scheduler (pulls, then pushes the CSVs to git), or in
  the cloud when the environment has the secrets YT_CLIENT_ID, YT_CLIENT_SECRET and YT_REFRESH_TOKEN (copied from the PC's
  token file after `auth`; set them in the cloud environment's settings, never in chat or in git).

What it can't give: Studio's "Stayed to watch (%)" (the swipe-away share) is not in the API. The API's engaged views / views is a
partial stand-in (r = 0.63 with "stayed" over 20 Shorts in the Oct 14 export; every Short under 0.50 had under 60% stayed), so
it catches likely swipes but can't rank the top. Export the Studio "Content" table once a week for the exact number.
Scopes: yt-analytics.readonly + youtube.readonly. It cannot upload, edit, delete or post anything.
"""
import argparse, base64, csv, datetime, hashlib, http.server, json, os, secrets, sys, threading, urllib.parse, urllib.request, webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CLIENT = os.path.join(HERE, "client_secret.json")
TOKEN = os.path.join(os.path.expanduser("~"), ".metasports", "yt_token.json")
SCOPES = "https://www.googleapis.com/auth/yt-analytics.readonly https://www.googleapis.com/auth/youtube.readonly"
AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
METRICS = "views,averageViewDuration,averageViewPercentage,estimatedMinutesWatched,likes,shares,subscribersGained"


def client():
    if os.environ.get("YT_CLIENT_ID") and os.environ.get("YT_CLIENT_SECRET"):
        return os.environ["YT_CLIENT_ID"], os.environ["YT_CLIENT_SECRET"]
    if not os.path.exists(CLIENT):
        sys.exit(f"Missing {CLIENT}. Do setup steps 1-3 (Tools Guide.md, 'YouTube Analytics API').")
    c = json.load(open(CLIENT))
    c = c.get("installed") or c.get("web") or {}
    return c["client_id"], c["client_secret"]


def post(url, data):
    req = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode(), method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def auth():
    """Installed-app OAuth with PKCE on a loopback port (Google's documented desktop flow)."""
    cid, csec = client()
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    state = secrets.token_urlsafe(16)
    got = {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            got.update({k: v[0] for k, v in q.items()})
            self.send_response(200); self.end_headers()
            self.wfile.write(b"MetaSports: access granted (read-only). You can close this tab.")

        def log_message(self, *a):
            pass

    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    redirect = f"http://127.0.0.1:{srv.server_port}"
    url = AUTH_URL + "?" + urllib.parse.urlencode({
        "client_id": cid, "redirect_uri": redirect, "response_type": "code", "scope": SCOPES, "state": state,
        "code_challenge": challenge, "code_challenge_method": "S256", "access_type": "offline", "prompt": "consent"})
    print("Opening the browser to sign in (read-only access). If it doesn't open, paste this link into it:\n" + url)
    webbrowser.open(url)
    t = threading.Thread(target=srv.handle_request); t.start(); t.join(timeout=300); srv.server_close()
    if got.get("state") != state or "code" not in got:
        sys.exit(f"Sign-in did not complete: {got.get('error', 'no code returned')}")
    tok = post(TOKEN_URL, {"code": got["code"], "client_id": cid, "client_secret": csec, "redirect_uri": redirect,
                           "grant_type": "authorization_code", "code_verifier": verifier})
    tok["obtained"] = datetime.datetime.utcnow().isoformat()
    os.makedirs(os.path.dirname(TOKEN), exist_ok=True)
    with open(TOKEN, "w") as f:
        json.dump(tok, f)
    try:
        os.chmod(TOKEN, 0o600)
    except OSError:
        pass
    print(f"Saved the token outside the repo: {TOKEN}")


def access_token():
    refresh = os.environ.get("YT_REFRESH_TOKEN")
    if not refresh:
        if not os.path.exists(TOKEN):
            sys.exit("No token yet: run  python Tools/yt_analytics.py auth  once on the PC (or set YT_REFRESH_TOKEN in the cloud environment).")
        refresh = json.load(open(TOKEN))["refresh_token"]
    cid, csec = client()
    fresh = post(TOKEN_URL, {"client_id": cid, "client_secret": csec, "refresh_token": refresh,
                             "grant_type": "refresh_token"})
    return fresh["access_token"]


def get(url, at):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {at}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def iso_seconds(d):
    """PT1M5S -> 65"""
    import re
    m = re.match(r"P(?:\d+D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", d or "")
    return sum(int(x or 0) * k for x, k in zip(m.groups(), (3600, 60, 1))) if m else ""


def report_url(start, end, metrics):
    return "https://youtubeanalytics.googleapis.com/v2/reports?" + urllib.parse.urlencode({
        "ids": "channel==MINE", "startDate": start, "endDate": end, "metrics": metrics,
        "dimensions": "video", "sort": "-views", "maxResults": 200})


def pull(start, end, engaged, out):
    at = access_token()
    metrics = METRICS + (",engagedViews" if engaged else "")
    try:
        rep = get(report_url(start, end, metrics), at)
    except urllib.error.HTTPError as e:
        if engaged:
            print(f"engagedViews refused ({e.code}); pulling without it")
            metrics = METRICS
            rep = get(report_url(start, end, metrics), at)
        else:
            raise
    cols = [h["name"] for h in rep.get("columnHeaders", [])]
    rows = [dict(zip(cols, r)) for r in rep.get("rows", [])]
    ids = [r["video"] for r in rows]
    meta = {}
    for i in range(0, len(ids), 50):
        d = get("https://www.googleapis.com/youtube/v3/videos?" + urllib.parse.urlencode(
            {"part": "snippet,contentDetails", "id": ",".join(ids[i:i + 50])}), at)
        for v in d.get("items", []):
            meta[v["id"]] = (v["snippet"]["title"], v["snippet"]["publishedAt"], iso_seconds(v["contentDetails"]["duration"]))
    out = out or os.path.join(ROOT, "Research Notes", "Studio exports", f"api {start} to {end}.csv")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    head = ["video_id", "title", "published", "length_s"] + [c for c in cols if c != "video"]
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(head)
        for r in rows:
            t, p, L = meta.get(r["video"], ("", "", ""))
            w.writerow([r["video"], t, p, L] + [r[c] for c in cols if c != "video"])
    print(f"wrote {out}: {len(rows)} videos, metrics {metrics}")

API_DIR = os.path.join(ROOT, "Research Notes", "Studio exports", "api")
DAILY_METRICS = "views,engagedViews,averageViewDuration,averageViewPercentage,subscribersGained,likes,shares"
# Flag thresholds (Oct 19, 2026). Engaged ratio from the Oct 14 Studio export (every Short under 0.50 had under 60% stayed);
# curve thresholds are starting points to recalibrate after 10 Shorts with both a curve and a Studio "stayed" number.
FLAG_ENGAGED = 0.50
FLAG_START = 0.70        # audienceWatchRatio at 10% of the runtime
FLAG_DROP = 0.15         # a fall of this much between two neighbouring 1% points in the first 15% of the runtime


def recent_uploads(at, days=30):
    """[(id, title, published, length_s)] for the channel's uploads in the last `days` days (Data API, read-only)."""
    ch = get("https://www.googleapis.com/youtube/v3/channels?part=contentDetails&mine=true", at)
    uploads = ch["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    items = get("https://www.googleapis.com/youtube/v3/playlistItems?" + urllib.parse.urlencode(
        {"part": "contentDetails", "playlistId": uploads, "maxResults": 50}), at).get("items", [])
    ids = [i["contentDetails"]["videoId"] for i in items]
    out, cut = [], datetime.datetime.utcnow() - datetime.timedelta(days=days)
    for i in range(0, len(ids), 50):
        d = get("https://www.googleapis.com/youtube/v3/videos?" + urllib.parse.urlencode(
            {"part": "snippet,contentDetails", "id": ",".join(ids[i:i + 50])}), at)
        for v in d.get("items", []):
            pub = v["snippet"]["publishedAt"]
            if datetime.datetime.strptime(pub[:19], "%Y-%m-%dT%H:%M:%S") >= cut:
                out.append((v["id"], v["snippet"]["title"], pub, iso_seconds(v["contentDetails"]["duration"])))
    return out


def video_metrics(at, vids, start, end):
    url = "https://youtubeanalytics.googleapis.com/v2/reports?" + urllib.parse.urlencode({
        "ids": "channel==MINE", "startDate": start, "endDate": end, "metrics": DAILY_METRICS, "dimensions": "video",
        "filters": "video==" + ",".join(vids), "maxResults": 200})
    rep = get(url, at)
    cols = [h["name"] for h in rep.get("columnHeaders", [])]
    return {r[0]: dict(zip(cols, r)) for r in rep.get("rows", [])}


def retention_curve(at, vid, start, end):
    """[(elapsedVideoTimeRatio, audienceWatchRatio, relativeRetentionPerformance)] for one video (100 points)."""
    url = "https://youtubeanalytics.googleapis.com/v2/reports?" + urllib.parse.urlencode({
        "ids": "channel==MINE", "startDate": start, "endDate": end, "dimensions": "elapsedVideoTimeRatio",
        "metrics": "audienceWatchRatio,relativeRetentionPerformance", "filters": "video==" + vid})
    return [tuple(r) for r in get(url, at).get("rows", [])]


def curve_flags(curve):
    """Plain-English flags for one retention curve; thresholds above."""
    if not curve:
        return []
    pts = sorted(curve)
    flags = []
    at10 = min(pts, key=lambda p: abs(p[0] - 0.10))[1]
    if at10 < FLAG_START:
        flags.append(f"weak start: {at10:.2f} of viewers still watching at 10% of the runtime (flag under {FLAG_START})")
    early = [p for p in pts if p[0] <= 0.15]
    drops = [(b[0], a[1] - b[1]) for a, b in zip(early, early[1:]) if a[1] - b[1] > FLAG_DROP]
    if drops:
        flags.append("sharp early drop at " + ", ".join(f"{x * 100:.0f}% ({d:.2f})" for x, d in drops) + " of the runtime: check that line")
    end = pts[-1][1]
    if end >= 1.0:
        flags.append(f"rewatch: {end:.2f} at the end (above 1.0 means loops)")
    return flags


def daily(days=30, curve_days=14):
    at = access_token()
    today = datetime.date.today()
    vids = recent_uploads(at, days)
    if not vids:
        sys.exit("no uploads in the window")
    start = min(v[2][:10] for v in vids)
    met = video_metrics(at, [v[0] for v in vids], start, today.isoformat())
    os.makedirs(API_DIR, exist_ok=True)
    dpath = os.path.join(API_DIR, f"daily {today}.csv")
    rpath = os.path.join(API_DIR, f"retention {today}.csv")
    with open(dpath, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["video_id", "title", "published", "length_s", "age_days"] + DAILY_METRICS.split(",") + ["engaged_ratio"])
        for vid, title, pub, L in vids:
            m = met.get(vid, {})
            age = (today - datetime.date.fromisoformat(pub[:10])).days
            v, e = float(m.get("views") or 0), float(m.get("engagedViews") or 0)
            w.writerow([vid, title, pub, L, age] + [m.get(k, "") for k in DAILY_METRICS.split(",")] + [round(e / v, 3) if v else ""])
    with open(rpath, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["video_id", "elapsed_ratio", "audience_watch_ratio", "relative_retention"])
        for vid, title, pub, L in vids:
            if (today - datetime.date.fromisoformat(pub[:10])).days <= curve_days:
                for x, a, r in retention_curve(at, vid, pub[:10], today.isoformat()):
                    w.writerow([vid, x, a, r])
    print(f"wrote {dpath}\nwrote {rpath}")
    report()


def report(path_dir=None):
    """Read the newest daily/retention CSVs and print the flags (no API call)."""
    path_dir = path_dir or API_DIR
    files = sorted(f for f in os.listdir(path_dir) if f.startswith("daily ")) if os.path.isdir(path_dir) else []
    if not files:
        sys.exit(f"no daily files in {path_dir}: run `daily` first (PC or cloud with secrets)")
    day = files[-1][6:16]
    rows = list(csv.DictReader(open(os.path.join(path_dir, files[-1]), encoding="utf-8")))
    curves = {}
    rp = os.path.join(path_dir, f"retention {day}.csv")
    if os.path.exists(rp):
        for r in csv.DictReader(open(rp, encoding="utf-8")):
            curves.setdefault(r["video_id"], []).append((float(r["elapsed_ratio"]), float(r["audience_watch_ratio"]), float(r["relative_retention"] or 0)))
    print(f"YouTube Analytics API, {day} ({len(rows)} uploads in the window). 'Stayed to watch' is Studio-only; engaged ratio is the stand-in.")
    for r in sorted(rows, key=lambda r: -float(r.get("views") or 0)):
        er = r.get("engaged_ratio")
        flags = []
        if er and float(er) < FLAG_ENGAGED:
            flags.append(f"engaged ratio {float(er):.2f} < {FLAG_ENGAGED}: likely under 60% stayed")
        flags += curve_flags(curves.get(r["video_id"], []))
        print(f"  {int(float(r.get('views') or 0)):>7,} views  age {r['age_days']:>2} d  avg {r.get('averageViewPercentage','')}% viewed  "
              f"engaged {er}  subs {r.get('subscribersGained','')}  | {r['title'][:55]}")
        for x in flags:
            print("        FLAG " + x)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("auth")
    d = sub.add_parser("daily")
    d.add_argument("--days", type=int, default=30)
    sub.add_parser("report")
    p = sub.add_parser("pull")
    p.add_argument("--from", dest="start", required=True)
    p.add_argument("--to", dest="end", default=datetime.date.today().isoformat())
    p.add_argument("--engaged", action="store_true")
    p.add_argument("--out")
    a = ap.parse_args()
    if a.cmd == "auth":
        auth()
    elif a.cmd == "daily":
        daily(a.days)
    elif a.cmd == "report":
        report()
    else:
        pull(a.start, a.end, a.engaged, a.out)


if __name__ == "__main__":
    main()
