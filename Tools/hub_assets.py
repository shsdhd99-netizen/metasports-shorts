"""Which Hub assets belong to which Short, and is a full-quality local copy on the PC?

  py -3 Tools/hub_assets.py "<Hub backup folder>/shorts" "<Productions/MetaSports>"

Prints, per Short doc: stage, number of version/cover assets, and whether a local video exists (READY TO POST*.mp4 or
final*.mp4 in the Short's production folder, found by the number in the folder name). Used before deleting the Hub copies of
posted or rejected Shorts: the Hub copies are compressed previews, the PC copies are the originals.
"""
import glob
import json
import os
import re
import sys

backup, prod = sys.argv[1], sys.argv[2]


def stage(d):
    s = str(d.get("status", "")).lower()
    for k, v in (("posted", "posted"), ("ready", "ready"), ("draft", "ready"), ("edit", "editing"), ("reject", "rejected"),
                 ("abandon", "rejected"), ("hold", "blocked"), ("block", "blocked")):
        if s.startswith(k):
            return v
    return "footage"


def local_video(num):
    out = []
    for d in glob.glob(os.path.join(prod, "*")):
        if re.search(r"[ ]%02d[ ]" % int(num), os.path.basename(d)):
            out += [p for p in glob.glob(os.path.join(d, "**", "*.mp4"), recursive=True)
                    if re.search(r"READY TO POST|final", os.path.basename(p), re.I) and "nocap" not in p.lower()]
    return out


rows = []
for f in sorted(glob.glob(os.path.join(backup, "*.json"))):
    j = json.load(open(f, encoding="utf-8-sig"))
    d = j.get("data", j)
    ids = [v.get("assetId") for v in d.get("versions", []) if v.get("assetId")] + [c.get("assetId") for c in d.get("covers", []) if c.get("assetId")]
    n = d.get("num")
    lv = local_video(n) if n else []
    rows.append((os.path.basename(f)[:-5], stage(d), len(ids), len(lv), ids))
    print("%-26s %-9s assets=%-2d local_videos=%d" % rows[-1][:4])
json.dump([{"doc": r[0], "stage": r[1], "assets": r[4], "local": r[3]} for r in rows], open(os.path.join(backup, "_asset_map.json"), "w"), indent=1)
