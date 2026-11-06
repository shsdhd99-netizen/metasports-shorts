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


PLAYGROUND = "https://developers.google.com/oauthplayground"  # the only redirect registered for our Google client (loopback gives redirect_uri_mismatch, Nov 6)


def main():
    """Two steps, like yt_auth.py:
      1. python Tools/yt_manage_auth.py nba            -> opens Google's sign-in. Choose the channel owner's account, Allow (Advanced > Go to ... if warned).
         You land on the OAuth Playground page: click NOTHING there; copy the full address from the address bar (it contains code=...).
      2. python Tools/yt_manage_auth.py nba --code "<that address>"   -> saves YT_MANAGE_TOKEN (nba) or YT_MANAGE_TOKEN_FC (fc)."""
    ch = (sys.argv[1] if len(sys.argv) > 1 else "").lower()
    if ch not in ("nba", "fc"):
        sys.exit(__doc__)
    e = env(); cid, sec = e["YT_CLIENT_ID"], e["YT_CLIENT_SECRET"]
    code = ""
    if "--code" in sys.argv:
        code = sys.argv[sys.argv.index("--code") + 1].strip()
    if not code:
        url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode({
            "client_id": cid, "redirect_uri": PLAYGROUND, "response_type": "code", "scope": SCOPE,
            "access_type": "offline", "prompt": "consent", "state": "metasports"})
        print(f"Sign in as the owner of the {ch.upper()} channel and press Allow. On the page you land on, click nothing: copy its address.")
        if "--print-url" in sys.argv:
            print(url[:120] + "..."); return
        webbrowser.open(url)
        return
    if "code=" in code:
        code = urllib.parse.parse_qs(urllib.parse.urlparse(code).query).get("code", [""])[0]
    code = urllib.parse.unquote(code)
    data = urllib.parse.urlencode({"client_id": cid, "client_secret": sec, "code": code,
                                   "redirect_uri": PLAYGROUND, "grant_type": "authorization_code"}).encode()
    try:
        tok = json.load(urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", data=data), timeout=60))
    except urllib.error.HTTPError as ex:
        sys.exit("Google refused the code (it works once and expires in minutes; run step 1 again): " + ex.read().decode()[:200])
    if not tok.get("refresh_token"):
        sys.exit("Google returned no refresh token. Remove the app at myaccount.google.com/permissions and run step 1 again.")
    req = urllib.request.Request("https://www.googleapis.com/youtube/v3/channels?part=snippet&mine=true", headers={"Authorization": "Bearer " + tok["access_token"]})
    title = json.load(urllib.request.urlopen(req, timeout=60))["items"][0]["snippet"]["title"]
    save("YT_MANAGE_TOKEN" if ch == "nba" else "YT_MANAGE_TOKEN_FC", tok["refresh_token"])
    print(f"Saved. Channel found: {title!r}. Edit with: python Tools/yt_edit.py {ch} show <video_id>")


if __name__ == "__main__":
    main()
