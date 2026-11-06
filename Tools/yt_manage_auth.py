"""One-time sign-in that lets the tools EDIT your own videos (titles, tags, privacy, publish time), so a wrong title can be fixed in seconds (Nov 6, 2026).

  python Tools/yt_manage_auth.py nba      # sign in with the account that owns the MetaSports (NBA) channel, press Allow
  python Tools/yt_manage_auth.py fc       # sign in with the account that owns MetaSports FC

What it does: opens Google's sign-in page in your browser (the standard desktop flow, PKCE on a local port), asks for the `youtube` scope (manage your
YouTube account: edit and delete your own videos; it cannot read passwords or touch other Google services), and saves ONLY the refresh token to
Tools/.env as YT_MANAGE_TOKEN (nba) or YT_MANAGE_TOKEN_FC (fc). Prints the channel name it found, never a token. Needs YT_CLIENT_ID and YT_CLIENT_SECRET in
Tools/.env (they are already there). The tokens stop working after 7 days while the Google Cloud app is in "Testing": set the OAuth consent screen's
Publishing status to "In production" first (Tools/yt_edit.py explains the click path).
Then edit with Tools/yt_edit.py.
"""
import base64, hashlib, http.server, json, os, secrets, sys, threading, urllib.parse, urllib.request, webbrowser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV = os.path.join(ROOT, "Tools", ".env")
SCOPE = "https://www.googleapis.com/auth/youtube"


def env():
    d = {}
    for l in open(ENV, encoding="utf-8"):
        if "=" in l and not l.lstrip().startswith("#"):
            k, v = l.strip().split("=", 1); d[k] = v
    return d


def save(key, val):
    lines = open(ENV, encoding="utf-8").read().splitlines()
    out, done = [], False
    for l in lines:
        if l.startswith(key + "="):
            out.append(f"{key}={val}"); done = True
        else:
            out.append(l)
    if not done:
        out.append(f"{key}={val}")
    open(ENV, "w", encoding="utf-8").write("\n".join(out) + "\n")


def main():
    ch = (sys.argv[1] if len(sys.argv) > 1 else "").lower()
    if ch not in ("nba", "fc"):
        sys.exit(__doc__)
    e = env(); cid, sec = e["YT_CLIENT_ID"], e["YT_CLIENT_SECRET"]
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    state = secrets.token_urlsafe(16); got = {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            got.update({k: v[0] for k, v in urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query).items()})
            self.send_response(200); self.send_header("Content-Type", "text/plain; charset=utf-8"); self.end_headers()
            self.wfile.write(b"MetaSports: access granted. You can close this tab and go back to the terminal.")
        def log_message(self, *a): pass

    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    redirect = f"http://127.0.0.1:{srv.server_port}"
    url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode({
        "client_id": cid, "redirect_uri": redirect, "response_type": "code", "scope": SCOPE, "state": state,
        "code_challenge": challenge, "code_challenge_method": "S256", "access_type": "offline", "prompt": "consent"})
    print(f"Opening the Google sign-in page for the {ch.upper()} channel. Choose the account that OWNS that channel, then press Allow.")
    if "--print-url" in sys.argv:
        print(url[:120] + "..."); return
    threading.Thread(target=srv.handle_request, daemon=True).start()
    webbrowser.open(url)
    for _ in range(600):  # wait up to 10 minutes
        if got.get("code"):
            break
        import time; time.sleep(1)
    if got.get("state") != state or not got.get("code"):
        sys.exit("No consent received (timed out or the state did not match). Run it again.")
    data = urllib.parse.urlencode({"client_id": cid, "client_secret": sec, "code": got["code"], "code_verifier": verifier,
                                   "redirect_uri": redirect, "grant_type": "authorization_code"}).encode()
    tok = json.load(urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", data=data), timeout=60))
    if not tok.get("refresh_token"):
        sys.exit("Google returned no refresh token. Remove the app at myaccount.google.com/permissions and run this again.")
    req = urllib.request.Request("https://www.googleapis.com/youtube/v3/channels?part=snippet&mine=true", headers={"Authorization": "Bearer " + tok["access_token"]})
    title = json.load(urllib.request.urlopen(req, timeout=60))["items"][0]["snippet"]["title"]
    save("YT_MANAGE_TOKEN" if ch == "nba" else "YT_MANAGE_TOKEN_FC", tok["refresh_token"])
    print(f"Saved. Channel found: {title!r}. Edit with: python Tools/yt_edit.py {ch} show <video_id>")


if __name__ == "__main__":
    main()
