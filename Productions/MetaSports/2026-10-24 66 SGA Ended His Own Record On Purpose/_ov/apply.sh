#!/bin/sh
# Words over footage: run from the Short folder after cut_list.py. Keeps the clean cut as clips/<clip>_raw.mp4.
cd "$(dirname "$0")/.." || exit 1
for spec in _ov/A*.json; do
  c=$(basename "$spec" .json)
  [ -f "clips/${c}_raw.mp4" ] || cp "clips/$c.mp4" "clips/${c}_raw.mp4"
  python ../../../Tools/overlay.py --in "clips/${c}_raw.mp4" --out "clips/$c.mp4" --spec "$spec" || exit 1
done
