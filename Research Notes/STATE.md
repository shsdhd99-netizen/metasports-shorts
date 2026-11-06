# STATE (one page for any account/session; update at the end of every run)
<!-- AUTO:START -->
## AUTO (written by `python Tools/state.py`, 2026-11-05 11:17 local; do not edit by hand)
- Builder: cloud
- Preflight: PREFLIGHT OK (2 warnings)**
- Disk free: 17.4 GB
- NBA: 23,851 Shorts views/day (7-day), 488,299 in the last 90 days (4.9% of the 10M line), data to 2026-11-02
- FC: 9,565 Shorts views/day (7-day), 120,771 in the last 90 days (1.2% of the 10M line), data to 2026-11-02
- Next open slot: NBA GAP nba 2026-11-07 15:30 ET (Sat Nov 7, 03:30 PM ET); FC NO GAP fc in the next 54 h
- Last scheduler lines: - 2026-11-04 18:30 ET: scheduled 0; skipped/refused 1. | - 2026-11-05 06:30 ET: scheduled 0; skipped/refused 1. | - 2026-11-05 06:47 ET: scheduled 1: 2026-11-05 95 A Rookie Chased 40 Because His Teammates Said So; skipped/refused 1.
- Last cloud STATUS lines: STATUS: blocked, no build. BUILDER.txt = `cloud`; `cloud_setup.sh`: voice key set, Gemini set; `pref | STATUS: blocked, no build. `cloud_setup.sh`: voice key set, Gemini set; `preflight.py --quiet`: BLOC | STATUS: Automation check written to Research Notes/Automation Check.md: PC timers PASS; cloud 3:17/4
- **Needs attention:** cloud routines: the last STATUS says blocked (keys missing in the cloud environment?)
<!-- AUTO:END -->
- Updated: 2026-11-04 17:30 ET by PC account 1 (full-automation prompt run).
- Builder: `cloud` (see `BUILDER.txt`); routines NBA 3:17 AM ET, FC 4:23 AM ET.
- Weekly usage last seen: unknown in terminal sessions (owner said "low" after the Nov 3 run; reset Wed Nov 4 1 PM ET). Ceiling for runs: 99% (owner, Nov 3).
- PC timers registered (verified Nov 3 22:45): analytics 3:20 AM, schedule ready 6:30 AM / 6:30 PM, terminal resume Wed Nov 4 1:30 PM.
- Last learn run: `python Tools/learn.py all --fetch`; weights in `Learned Weights.md`.
- Next: `HANDOFF - latest.md`, then `HANDOFF - Account 1 START HERE (Nov 4).md` section 3A.
- 2026-11-04: all PC timers fired overnight (wake, analytics 3:20, schedule AM 6:30, gap-fill 6:45/7:30). Topic shapes labelled (Tools/data/topic_shapes.csv); learn.py reports shape + subs/1K. NBA gap Fri Nov 6 3:30 PM -> Thu 6:45 gap-fill (build family/moment). FC scripts S21/S22/S36 written (Nov 11-13 folders, not voiced). Studio pull: not automated (CLAUDE.md: never open Studio; no Chrome tool in terminal).
- Open slots: NBA from Fri Nov 6 7:15 AM (no ready draft); FC Sat Nov 7 double-booked (S09 and S29, owner picks), Sun Nov 8 open.

- 2026-11-03 19:50 ET: S29 (FC, goalkeeper lane) built on the PC, both versions QA PASS, awaiting owner's ear and an A/B arm choice; slot Sat Nov 7 12:00 PM ET. Hub card not made. Voice used so far today about 1.6K characters on S29 (plan check: 49,630 of 121,224 used before).

- 2026-11-03 20:20 ET: Account 1 handoff written (`HANDOFF - Account 1 (Nov 3 night).md`). Preflight OK, 6 warnings (no timers registered, USAGE.txt added, disk 27 GB).

- 2026-11-03 22:00 ET: BUILDER=cloud. Routines trig_01PUCBRzwuJ1j1r3Y53GdfoY (NBA 3:17 AM ET) and trig_011nY5arZZHcgKkWQvcBkNKc (FC 4:23 AM ET) ENABLED, prompts point to `CLOUD DAILY RULES.md`. Cloud env still lacks keys until the owner runs `Tools/copy_cloud_env.ps1` and pastes them.
- 2026-11-03 22:45 ET: tasks verified; Account 1 start-up list is in HANDOFF - Account 1 START HERE (Nov 4).md; backlog in Research Notes/Improvement Backlog.md.
- 2026-11-03 19:45 ET: #94 Rodman No. 69 BUILT on the PC (QA PASS), card on HOLD for the owner's OK; slot Fri Nov 6 7:15 AM ET. Next NBA slot open: Fri Nov 6 3:30 PM ET onward.
- 2026-11-03 20:45 ET: PC gap-fill tasks registered (NBA 6:45 AM, FC 7:30 AM; build only if next_gap.py finds an uncovered slot). Next NBA gap: Fri Nov 6 3:30 PM (in range Thu morning). FC covered through Sun Nov 8.

- 2026-11-04 ~19:00 ET (terminal, owner request): CLAIM: terminal built the Lendeborg Short (#95); BUILDER.txt left as `cloud`. #96 Porzingis and #97 Warriors streak = scripts + sources only (notes.md in their folders), not voiced, not built. FC clip-repetition study done (not supported at n=15) and edit_lint reuse guard shipped. Max Claude synced preview done (Clients/Max Claude/Productions/00 Preview/QA.md). S09/S29 are already uploaded and scheduled by schedule_ready, so NOT re-cut. Backlog items (schedule_ready --require-approved, hub_pack helper, learn.py subs columns): not done.
- 2026-11-05 04:30 ET (cloud FC run): preflight BLOCKED (YT_* secrets missing in the cloud env; voice and Gemini keys now set). No FC gap within 54 h, no build. Public: S25 11K, S26 8.5K, S19 3.7K, S20 1.0K. Learned Weights refreshed.
- 2026-11-05 PC account 1 CLAIM: NBA gap Fri Nov 6 3:30 PM ET filled by finishing existing #95 (Lendeborg peer pressure; already built, QA PASS re-run Nov 5). No new build.
- 2026-11-05 PC account 1: #95 scheduled for Fri Nov 6 3:30 PM ET (gap closed). NBA next open: Sat Nov 7.
- 2026-11-06 04:30 ET (cloud FC run): preflight BLOCKED (YT_* secrets still missing in the cloud env). No FC gap within 54 h, no build. S25 23K at 72 h; goalkeeper trick n=5, 8.0x.
