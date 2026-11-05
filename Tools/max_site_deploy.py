"""Deploy Max Claude's private site (Nov 5, 2026).

  python Tools/max_site_deploy.py draft|prod

Encrypts the private files (index.html, quote.html, media/*) with the password MAX_SITE_PASSWORD from Tools/.env (AES-256-GCM, PBKDF2 250k;
Tools/max_site_protect.mjs, needs Node), zips the result with the plain public files (thanks.html, demo.mp4, poster.jpg) and uploads it to the
Netlify site `ondemand-studio` with NETLIFY_AUTH_TOKEN from Tools/.env. `draft` makes a preview deploy (the live URL is unchanged); `prod` publishes.
Why not Netlify password protection or an edge function: the free plan has no site password and zip uploads do not bundle edge functions.
Draft/preview URLs are public but show only the encrypted shell. Nothing here prints a secret.
"""
import json, os, subprocess, sys, tempfile, urllib.request, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "Clients", "Max Claude", "site")
SITE_ID = "795688f4-76fa-4c8f-b0fd-2a405dbb7415"


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "draft"
    env = {}
    for l in open(os.path.join(ROOT, "Tools", ".env"), encoding="utf-8"):
        if "=" in l and not l.lstrip().startswith("#"):
            k, v = l.strip().split("=", 1); env[k] = v
    pw, tok = env.get("MAX_SITE_PASSWORD"), env.get("NETLIFY_AUTH_TOKEN")
    if not pw or not tok:
        sys.exit("MAX_SITE_PASSWORD and NETLIFY_AUTH_TOKEN must be in Tools/.env")
    stage = tempfile.mkdtemp(prefix="maxsite_")
    subprocess.run(["node", os.path.join(ROOT, "Tools", "max_site_protect.mjs"), SITE, stage, pw], check=True)
    zp = os.path.join(stage + "_zip.zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for d, _, fs in os.walk(stage):
            for f in fs:
                p = os.path.join(d, f); z.write(p, os.path.relpath(p, stage).replace("\\", "/"))
    url = f"https://api.netlify.com/api/v1/sites/{SITE_ID}/deploys" + ("?draft=true" if mode == "draft" else "")
    req = urllib.request.Request(url, data=open(zp, "rb").read(), method="POST", headers={"Authorization": "Bearer " + tok, "Content-Type": "application/zip"})
    d = json.load(urllib.request.urlopen(req, timeout=600))
    print(d.get("id"), d.get("state"), d.get("context"), d.get("deploy_ssl_url"))


if __name__ == "__main__":
    main()
