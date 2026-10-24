# Soccer channel: START HERE (updated Oct 22, 2026)

This is the second channel's own space. The NBA channel (MetaSports) keeps its own files in the repo root; nothing here changes them.

> **Owner rules (they apply here too):**
> - Never publish, schedule or replace anything. Every finished video is a DRAFT awaiting the owner's approval. The owner posts.
> - Never open YouTube Studio, never ask for passwords or keys, and never print the ElevenLabs key.
> - Copy what works (the owner, Oct 21): "do not try new things, stick with what works."
> - No promo at the end (the owner, Oct 22: "that will instantly kill retention") and no dead air: every voice goes through `Tools/tighten_voice.py`.

## What this channel is
- **Name:** MetaSports FC.
  - Handle @MetaSportsFC, claimed by the owner Oct 22 (channel id UCIYlW84gYcChQtdys5L9pOg).
  - Brand v2 (Oct 22) matches the MetaSports Clips picture: red, a yellow figure, white MetaSports, "F C".
  - See `Brand/Brand Kit.md`.
- **Format:** Ahmed's Goal story Shorts, copied in shape, never in wording.
  - 60-80 s per Short.
  - The title is read aloud as line 1.
  - "Back in [year], [famous name]..."
  - A turn every 8-12 s.
  - The ending is a hard number or an ironic twist, and nothing comes after it.
  - A new picture every 1.1-2.1 s.
  - Captions: TikTok Sans, white, dead centre.
  - A quiet music bed under the voice.
  - Evidence: `Research Notes/Story Format Study - Ahmed (Oct 21, 2026).md` and `Research Notes/Ahmed's Network and a Second Channel (Oct 21, 2026).md` (repo root).
- **How to make one:** the skill `.claude/skills/story-short/SKILL.md` (`/story-short`). It is self-contained, so another Claude account can follow it from a zip: `Soccer Channel/story-short-skill.zip`.

| You want... | Open |
|---|---|
| **The phone Hub** (drafts to post, results, channel numbers, to-do, brand kit, ideas) | https://claude.ai/artifact/2UVAcbNpKq6j4YXBEF8ge3 (new account, Oct 24; database: `shorts`, `channel/stats`, `todo`, `brand/kit`, `ideas`; page source `Hub/metasportsfc_hub.html`). The old Hub LFsQtwomdpLAshoz4Xw62H is on the old account. |
| Profile picture, banner, watermark, texts to paste | `Brand/Brand Kit.md` (+ the files in `Brand/`, made by `Brand/make_brand.py`) |
| The rules for this channel, step by step | `Playbook.md` |
| Name, handle, bio, upload settings | `Channel Setup.md` |
| What to make next (ideas with series titles) | `Idea Bank.md` |
| Results after posting | `Outcome Log.md` |
| What we learned | `Lessons Learned.md` |
| Finished drafts | `Productions/<date> S<NN> <title>/` (each has `UPLOAD.md` and `notes.md`) |

## State, Oct 22 2026
| # | Short | Status | Files |
|---|---|---|---|
| S01 | Goalkeepers who hid a cheat sheet in their sock (Lehmann, 2006) | **DRAFT, awaiting approval.** 59.5 s (promo cut, pauses tightened Oct 22). QA PASS (full). | `Productions/2026-10-21 S01 Goalkeepers Who Hid A Cheat Sheet/` |
| S02 | Players who got in trouble the day before a derby (Balotelli, 2011) | **DRAFT, awaiting approval.** 63 s (pauses tightened Oct 22). QA PASS (full). | `Productions/2026-10-21 S02 Trouble The Night Before The Derby/` |
| S03 | Goalkeepers who danced on the line to win a final (Dudek, Istanbul 2005; Grobbelaar 1984) | **DRAFT, awaiting approval.** 70.7 s. QA PASS (full). | `Productions/2026-10-22 S03 Goalkeepers Who Danced To Win A Final/` |

- **Post order:** 1 a day at noon ET: S01 Wed Oct 22, S02 Thu, S03 Fri, S04 Sat (to make). See `Content Plan (Oct 22-25).md` in the repo root. No Short teases another any more.
- **Each Short has two versions:** with a quiet music bed (what Ahmed does) and without (the NBA channel's default since Oct 14). The owner picks one.

## Open decisions for the owner
1. Approve or change S01, S02 and S03 (music or no music).
2. Paste the new short YouTube description (in `Brand/Brand Kit.md` and the Hub).
3. TikTok and Instagram: Ahmed posts the same file on all three. Say if you want that; you post it.

## Running costs to watch
- **ElevenLabs (Creator plan, 100K credits a month):**
  - a 65 s story is about 1,500-1,700 characters a take, and the voice check re-records once in about half the cases;
  - so about 3K credits a Short;
  - 2 a day is about 180K a month, more than Creator gives. At 1 a day it fits.
  - The 75 s music bed was generated once and is reused.
