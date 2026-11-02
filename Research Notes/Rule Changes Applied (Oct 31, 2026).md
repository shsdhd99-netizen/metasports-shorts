# Rule changes applied, Oct 31, 2026

Owner, Oct 31 2026 (chat, Account 2 terminal): "i think you should implement all those 5 rules, and aswell as that i will allow you to schedule videos and private videos now."

Source for the five: `Research Notes/Account 2/Rules Audit 2026-10-31.md` (about 40 rules checked against our own analytics). Evidence is thin on purpose: each change is a **test**, and each says how it will be read.

| # | Rule before | Rule now | How we read it |
|---|---|---|---|
| 1 | Never post, schedule or replace a public video; never open YouTube Studio; owner posts | Agents may **upload as private** and **schedule** a Short for a future slot. **Still never:** edit, delete or replace a public video, publish instantly outside a slot, touch comments or settings | Needs a one-time YouTube **upload permission** from the owner (our current Google permission is read-only). Until then everything stays a DRAFT. Only Shorts with QA PASS and Gemini READY (or an explained FIX); slots from `UPLOAD SCHEDULE.md`, max 2 per channel a day, 6+ h apart. The owner can unschedule at any time |
| 2 | NBA 20-30 s | Default 20-24 s, up to 30 s when the story needs it. Write the length in `notes.md` | Length test: 20-22 s vs 27-29 s, 3 pairs. Mixed evidence: length vs views -0.13, vs avg % viewed -0.43 |
| 3 | Soccer: global names only | Preferred, not required | Test S17 Krul vs S21 Higuita. Our three hits were trick/object stories |
| 4 | News: morning after or not at all | 24-36 h window; posting-hour slots are a habit | The old rule rested on one Short (#63, n=1) |
| 5 | Line 1 never a question; replay-the-key-second required; delete `src/` on posting | A question line 1 allowed as a test (about 1 in 4); replay is advice; delete `src/` after the 72 h read | Question vs statement titles lean slightly ahead, n too small |

## Kept unchanged
No keys in files or chat. No cookies or DRM/paywall workarounds. Copyright rules (under 60 s, no ripped protected media). No promo outro, no follow ask, no cards (the data agrees, thinly). Line 1 at 11 words or fewer. Shot 1 held 2.0 s or more. Never invent a stat. Never edit, delete or replace a live public video.

## Files edited (small, marked lines only)
`ACCOUNT 2 - START HERE.md`, `MetaSports - Playbook.md`, `Soccer Channel/Playbook.md`, `.claude/skills/daily-run/SKILL.md`, `.claude/skills/cloud-short/SKILL.md`. The main account reads the last four, so it picks the changes up on its next run.
