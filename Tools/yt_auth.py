"""One-time sign-in so auto-scheduling can work (Nov 1, 2026). Run it ON THE PC; it opens your browser, you click Allow, done.

  python Tools/yt_auth.py --channel nba     # sign in as the MetaSports channel
  python Tools/yt_auth.py --channel fc      # sign in as the MetaSports FC channel

It asks Google for ONE permission only: upload videos (youtube.upload). That scope cannot read, edit or delete anything.
It saves the resulting refresh token to Tools/.env (git-ignored) as YT_UPLOAD_TOKEN (nba) or YT_UPLOAD_TOKEN_FC (fc). The
token is never printed. Needs YT_CLIENT_ID and YT_CLIENT_SECRET already in Tools/.env (they are).
If Google says "redirect_uri_mismatch", the Google app's client is a Web client: create an OAuth client of type "Desktop app" in
the same Google Cloud project, put its ID and secret in Tools/.env, and run this again. If the token stops working after 7 days,
the app is still in "Testing": publish it on the OAuth consent screen.
Standard library only.
"""
import argparse, http.server, json, os, secrets, sys, threading, urllib.parse, urllib.request, webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
ENVFILE = os.path.join(HERE, ".env")
NAME = {"nba": "YT_UPLOAD_TOKEN", "fc": "YT_UPLOAD_TOKEN_FC"}
SCOPE = "https://www.googleapis.com/auth/youtube.upload"


def env():
    out = {}
    if os.path.exists(ENVFILE):
        for line in open(ENVFILE, encoding="utf-8-sig"):
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.rstrip("\r\n").split("=", 1)
                out[k.strip()] = v.strip()
    return out


def save(key, value):
    lines = open(ENVFILE, encoding="utf-8-sig").read().splitlines() if os.path.exists(ENVFILE) else []
    lines = [l for l in lines if not l.startswith(key + "=")] + [f"{key}={value}"]
    open(ENVFILE, "w", encoding="utf-8").write("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", choices=["nba", "fc"], required=True)
    a = ap.parse_args()
    e = env()
    cid, csec = e.get("YT_CLIENT_ID"), e.get("YT_CLIENT_SECRET")
    if not (cid and csec):
        sys.exit("YT_CLIENT_ID / YT_CLIENT_SECRET are missing from Tools/.env.")
    state, box = secrets.token_urlsafe(16), {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            if q.get("state", [""])[0] == state and "code" in q:
                box["code"] = q["code"][0]
                msg = "Signed in. You can close this tab and go back to the terminal."
            else:
                box["error"] = q.get("error", ["unknown"])[0]
                msg = "Sign-in failed: " + box["error"]
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(msg.encode())

        def log_message(self, *x):
            pass

    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    redirect = f"http://127.0.0.1:{srv.server_port}"
    url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode({
        "client_id": cid, "redirect_uri": redirect, "response_type": "code", "scope": SCOPE,
        "access_type": "offline", "prompt": "consent", "state": state})
    print(f"Opening your browser. Sign in as the {'MetaSports' if a.channel == 'nba' else 'MetaSports FC'} channel and click Allow.")
    webbrowser.open(url)
    threading.Thread(target=srv.handle_request, daemon=True).start()
    for _ in range(600):
        if box:
            break
        threading.Event().wait(0.5)
    if "code" not in box:
        sys.exit("No sign-in received (" + box.get("error", "timed out") + ").")
    data = urllib.parse.urlencode({"code": box["code"], "client_id": cid, "client_secret": csec,
                                   "redirect_uri": redirect, "grant_type": "authorization_code"}).encode()
    try:
        tok = json.load(urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", data=data), timeout=30))
    except Exception as ex:
        sys.exit(f"Google refused the code: {ex}")
    if "refresh_token" not in tok:
        sys.exit("Google gave no refresh token. Remove this app at myaccount.google.com/permissions and run again.")
    save(NAME[a.channel], tok["refresh_token"])
    print(f"Saved {NAME[a.channel]} to Tools/.env (not printed). Auto-scheduling is ready for the {a.channel} channel; it stays OFF until you say which mode.")


if __name__ == "__main__":
    main()
