---
name: thumbnail
description: >
  Make thumbnails with the user's free local maker (Tools\thumb.py): 3 commentary thumbnail versions
  for YouTube Test & Compare, or a 9:16 MetaSports cover. Use when the user types /thumbnail or asks
  for a thumbnail. Arguments: the text idea and, optionally, a background image and a character PNG.
---

# /thumbnail

ROOT = `C:\Users\Admin\Documents\YouTube-Playbooks`. Run from `ROOT\Tools` with `py -3.14` (it has Pillow).

1. **Read** the Thumbnails and Commentary sections of `ROOT\Tools\data\title_patterns.md`.
2. **Gather what you need:**
   - **Background:** a gameplay screenshot or video frame. Use the newest .png/.jpg in the production folder, or ask the user to drop one there.
   - **Text:** 2–3 words that ADD to the title. If none is given, propose 3 and pick the best.
   - **Cutout (optional):** a PNG with a transparent background. Tip: Windows Paint → Remove background → save as PNG.
3. **Run:**
   - Commentary: `py -3.14 thumb.py --bg "<bg>" --text "<TEXT>" --cutout "<png>" --variants 3 --out "<folder>\thumb.png"`. This makes thumb_A/B/C.
   - MetaSports cover: `py -3.14 thumb.py --shape short --bg "<frame>" --text "<TEXT>" --out "<folder>\cover.png"`
   - Use `\n` inside `--text` for a line break (2 lines max).
4. **Look at every image** with the Read tool. If the text is hard to read, covers the character or is cut off, fix it: shorter text, another `--style` (yellow/white/orange), or no cutout. Re-run, at most 2 retries.
5. **Tell the user** the file names, plus: "Upload A, B and C in YouTube Studio → Test & Compare. YouTube picks the winner by watch time."
