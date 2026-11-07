"""Print a words.json as 'word@start' on one line plus the end time (for planning shots).
  py -3 Tools/words_print.py "<folder>/words.json"
"""
import json
import sys

w = json.load(open(sys.argv[1], encoding="utf-8-sig"))
w = w["words"] if isinstance(w, dict) else w
print(" ".join("%s@%.1f" % (x["word"], x["start"]) for x in w))
print("end", w[-1]["end"])
