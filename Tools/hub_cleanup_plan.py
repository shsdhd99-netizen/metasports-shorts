"""Build the Hub cleanup writes (ArtifactData batch) from the backup + the Oct 15 metrics CSV. Prints nothing destructive:
it only writes JSON files that are then applied by hand (batch), after the backup exists.

  py -3 Tools/hub_cleanup_plan.py "<Hub backup>/shorts" "<Posted Shorts - metrics ... .csv>" "<out dir>"

For each Short doc:
 - posted: add ytId (from the metrics CSV by number), results (views, engaged %, avg % viewed, published date), drop versions and covers
 - rejected / blocked WITH a local video: drop versions and covers (the text, title, tags and notes stay)
 - kept as is: ready/editing/footage, and any doc without a local video copy (s30, s37, s44)
The asset ids to delete come from `_asset_map.json` (same filter) and are written to `assets_to_delete.txt`.
"""
import csv
import glob
import json
import os
import sys

backup, metrics, out = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(out, exist_ok=True)
rows = {}
for r in csv.DictReader(open(metrics, encoding="utf-8-sig")):
    if r.get("num"):
        key = r["num"].rstrip("r")
        rows.setdefault(key, []).append(r)
amap = {r["doc"]: r for r in json.load(open(os.path.join(backup, "_asset_map.json")))}
VERSIONS = {"s01-lebron": 9, "s11-jordan": 10, "s12-duren": 7, "s13-kawhi": 11, "s14-four-stars": 7, "s15-adams-gta": 7, "s16-giannis-vice-city": 6, "s17-flopping": 8, "s18-lebron-helicopter": 4, "s19-flagg-height": 7, "s20-bad-boys": 6, "s21-jokic-westbrook": 12, "s22-number-six": 4, "s23-bronny-spot": 5, "s24-bronny-safe": 6, "s25-bronny-better": 6, "s26-screens": 5, "s27-lottery": 5, "s28-hinkle": 4, "s29-underhand": 2, "s30-giannis-steps": 4, "s32-spurs-lead": 4, "s33-run-out-players": 3, "s34-2007-draft": 2, "s35-wemby-rugby": 2, "s36-lebron-boozer": 7, "s37-2k27": 4, "s38-lebron-promise": 5, "s39-oldest-triple-double": 2, "s40-jokic-pass": 5, "s41-sharp": 5, "s42-most-misses": 3, "s44-flagg-bags": 2}  # versions at backup time (from the list call)
keep = {"s44-flagg-bags", "s30-giannis-steps", "s37-2k27"}
writes, delete = [], []
for f in sorted(glob.glob(os.path.join(backup, "s*.json"))):
    j = json.load(open(f, encoding="utf-8-sig"))
    doc = os.path.basename(f)[:-5]
    d = j.get("data", j)
    ver = VERSIONS[doc]
    a = amap[doc]
    data = {}
    if a["stage"] == "posted":
        rs = rows.get(str(d.get("num")), [])
        if rs:
            r = rs[0]
            def num(x):
                try:
                    return float(x)
                except Exception:
                    return None
            views = num(r.get("views_public_oct14")) or num(r.get("an_views"))
            er = num(r.get("engaged_ratio"))
            data["ytId"] = r["id"]
            data["results"] = {"when": (r.get("published") or "")[:10], "views": int(views) if views is not None else None,
                               "viewedPct": round(er * 100) if er is not None else None, "avgPct": num(r.get("avg_pct")),
                               "note": "Oct 14-15 reads; viewedPct = engaged-view ratio from the Studio export"}
            if len(rs) > 1:
                data["ytId2"] = rs[1]["id"]
    if a["stage"] in ("posted", "rejected", "blocked") and a["local"] > 0 and doc not in keep:
        data["versions"] = []
        data["covers"] = []
        delete += a["assets"]
    if data:
        writes.append({"op": "update", "collection": "shorts", "doc_id": doc, "if_version": ver, "data": data})
json.dump(writes[:25], open(os.path.join(out, "batch1.json"), "w"), indent=1)
json.dump(writes[25:], open(os.path.join(out, "batch2.json"), "w"), indent=1)
open(os.path.join(out, "assets_to_delete.txt"), "w").write("\n".join(dict.fromkeys(delete)))
print(len(writes), "doc updates;", len(set(delete)), "assets to delete")
