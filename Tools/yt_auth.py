"""One-time sign-in so auto-scheduling can work (Nov 1, 2026). Run it ON THE PC; it opens your browser, you click Allow, done.

  python Tools/yt_auth.py --channel nba     # sign in as the MetaSports channel
  python Tools/yt_auth.py --channel fc      # sign in as the MetaSports FC channel

It asks Google for ONE permission only: upload videos (youtube.upload). That scope cannot read, edit or delete anything.
It saves the resulting refresh token to Tools/.env (git-ignored) as YT_UPLOAD_TOKEN (nba) or YT_UPLOAD_TOKEN_FC (fc). The
token is never printed. Needs YT_CLIENT_ID and YT_CLIENT_SECRET already in Tools/.env (they are).
Nov 1: the loopback address is refused by our Google client; the two-step Playground flow below is the working one.
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


PLAYGROUND = "https://developers.google.com/oauthplayground"  # the only redirect registered for our Google client (Nov 1 test)


def auth_url(cid, state="metasports"):
    return "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode({
        "client_id": cid, "redirect_uri": PLAYGROUND, "response_type": "code", "scope": SCOPE,
        "access_type": "offline", "prompt": "consent", "state": state})


def main():
    """Two steps (Nov 1 fix: Google refuses http://127.0.0.1 for this client with redirect_uri_mismatch, only the OAuth Playground
    address is registered):
      1. python Tools/yt_auth.py --channel nba            -> opens the sign-in page. Sign in as the channel, click Allow (if Google
         warns the app is unverified: Advanced > Go to ... (unsafe)). You land on the OAuth Playground page: DO NOT click anything there.
         Copy the full address from the browser's address bar (it contains code=...).
      2. python Tools/yt_auth.py --channel nba --code "<that address or just the code>"   -> saves the token to Tools/.env."""
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", choices=["nba", "fc"], required=True)
    ap.add_argument("--code", help="the address you landed on (or just its code= value)")
    a = ap.parse_args()
    e = env()
    cid, csec = e.get("YT_CLIENT_ID"), e.get("YT_CLIENT_SECRET")
    if not (cid and csec):
        sys.exit("YT_CLIENT_ID / YT_CLIENT_SECRET are missing from Tools/.env.")
    if not a.code:
        url = auth_url(cid)
        print(f"Sign in as the {'MetaSports' if a.channel == 'nba' else 'MetaSports FC'} channel and click Allow. "
              "On the page you land on, click nothing: copy its address from the address bar.")
        webbrowser.open(url)
        print(url)
        return
    code = a.code.strip()
    if "code=" in code:
        code = urllib.parse.parse_qs(urllib.parse.urlparse(code).query).get("code", [""])[0]
    code = urllib.parse.unquote(code)
    data = urllib.parse.urlencode({"code": code, "client_id": cid, "client_secret": csec,
                                   "redirect_uri": PLAYGROUND, "grant_type": "authorization_code"}).encode()
    try:
        tok = json.load(urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", data=data), timeout=30))
    except urllib.error.HTTPError as ex:
        sys.exit("Google refused the code (codes work once and expire in minutes; run step 1 again): " + ex.read().decode()[:200])
    if "refresh_token" not in tok:
        sys.exit("Google gave no refresh token. Remove this app at myaccount.google.com/permissions and run step 1 again.")
    if "youtube.upload" not in tok.get("scope", ""):
        sys.exit("The token does not have the upload permission; run step 1 again and tick the upload box.")
    save(NAME[a.channel], tok["refresh_token"])
    print(f"Saved {NAME[a.channel]} to Tools/.env (not printed). Auto-scheduling is ready for the {a.channel} channel.")


if __name__ == "__main__":
    main()
