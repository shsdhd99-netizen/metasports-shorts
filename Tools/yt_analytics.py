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

What it can't give: Studio's "Stayed to watch (%)" (the swipe-away share). Keep exporting the Studio "Content" table for that.
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
    if not os.path.exists(TOKEN):
        sys.exit("No token yet: run  python Tools/yt_analytics.py auth  once on the PC.")
    tok = json.load(open(TOKEN))
    cid, csec = client()
    fresh = post(TOKEN_URL, {"client_id": cid, "client_secret": csec, "refresh_token": tok["refresh_token"],
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


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("auth")
    p = sub.add_parser("pull")
    p.add_argument("--from", dest="start", required=True)
    p.add_argument("--to", dest="end", default=datetime.date.today().isoformat())
    p.add_argument("--engaged", action="store_true")
    p.add_argument("--out")
    a = ap.parse_args()
    auth() if a.cmd == "auth" else pull(a.start, a.end, a.engaged, a.out)


if __name__ == "__main__":
    main()
