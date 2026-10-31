# Account 2: handoff to the terminal session on the PC (Sat Oct 31, 2026, ~1:45 PM ET)

Written by the Account 2 cloud chat for the copy of it the owner teleported into a terminal on the PC (`Documents\metasports-shorts`). You run **on the owner's PC**, so you have full network and local files. The cloud chat could do neither. Read this, then `ACCOUNT 2 - START HERE.md`, then work down the list. The owner reads on a phone and isn't technical: short, plain replies, and name Shorts by their title.

**This repo is public on GitHub. Never put a key, password or secret in any file that gets committed, including this one.**

## 1. Summary so far
- **Oct 29:** the main account wrote the Account 2 handover (`ACCOUNT 2 - START HERE.md`). This Claude account is **Account 2, the workshop**: deeper research, Shorts built ahead, real-audio versions and tool fixes. It pushes only to `account2` and hands work back through `Research Notes/Account 2/Queue.md`. The main account numbers, schedules and puts Shorts on the Hubs and the to-do list. Nobody but the owner posts.
- **Oct 30, evening:** the main account ran out of usage. The first Account 2 session (cloud) merged `main-329h3w` into `account2` and logged its blockers in `Log.md`: the cloud environment had no Full network and no keys, so nothing was built and nothing was queued.
- **Account 2 To-do page** (setup steps, task list, owner-only jobs): https://claude.ai/artifact/SruAZFaUGvp5DVbm5yed68
- **Keys:** the owner pasted three secrets into the chat. They're in your conversation history (two screenshots and a Discord image link), **not** in this file:
  1. a **new ElevenLabs API key** (`sk_...`, from a "new API key" dialog),
  2. a **Google OAuth client** (client ID `816294028132-....apps.googleusercontent.com` + a `GOCSPX-...` secret, created Oct 24), which `Tools/yt_analytics.py` reads as `YT_CLIENT_ID` / `YT_CLIENT_SECRET`. The cloud chat read this one off a blurry image, so a character may be wrong: test it,
  3. a **Supabase database password** (new Supabase project; MetaSports doesn't use Supabase).

  The owner asked for them in `.env` files "the same way as before" (`Tools/.env`, git-ignored). The cloud chat's request for folder access was blocked, so **this is still to do**. The owner was told once that these were exposed in chat and on Discord and that rotating them is wise. Don't repeat that more than once more.
- **Oct 31, morning:** the main account's usage came back. Its NBA and FC runs merged `account2` and wrote **script-only** Shorts, because the main account's routines have **no ElevenLabs key**:
  - `Productions/MetaSports/2026-10-31 80 The Warriors Flipped The Exact Same Score`
  - `Soccer Channel/Productions/2026-11-01 S19 Man United's Penalty Nightmare Is Now Saving Man City`
  - `Soccer Channel/Productions/2026-11-02 S20 Barcelona Signed Messi On A Paper Napkin`
- **Already scheduled by the main account:** #77 Bronny and S17 Krul (Fri AM), #74 free throws (Fri ~3 PM), S18 Mourinho (Sat). #78 Rodman went up Thu evening (y5dxVvGGaMI) and #79 was skipped. Check `UPLOAD SCHEDULE.md` and `Research Notes/Daily Log.md` for anything newer.

## 2. To-do, in order

### Now (on the PC)
1. **Save the keys.** `git pull`, then open `Tools/.env`. **Merge, don't overwrite:** keep `ELEVENLABS_VOICE_ID` and any existing lines. Set `ELEVENLABS_API_KEY`, `YT_CLIENT_ID`, `YT_CLIENT_SECRET` and `SUPABASE_DB_PASSWORD` from the conversation history.
   - Check: `git check-ignore Tools/.env` prints the path, and `git status` doesn't list it.
   - Test: `python Tools/voiceover.py --check` prints `Characters used: X of Y`. Never print the key itself.
   - Gemini: see whether `GEMINI_API_KEY` is already in `Tools/.env` or `~/.config/watch/.env`. If not, the owner makes a new one at aistudio.google.com/apikey.
2. **Cloud environment for later Account 2 sessions** (optional now that the PC works). On claude.ai/code: environment "MetaSports A2", network **Full**, env vars `ELEVENLABS_API_KEY` and `GEMINI_API_KEY`. The owner pastes the keys there; you don't type them into web pages.
3. **Ask the owner one question:** "The main account's last 3 Shorts are scripts with no voice (#80 Warriors, S19 Man United, S20 Messi napkin). Want me to voice and build them here on the PC?" Those folders belong to the main account (guide §4), so only touch them with a yes. If yes, check credits first (guide §6), build them to `built` per guide §5, don't renumber, and note it in `Log.md`.

### Account 2 task list (guide §7; log each item in `Research Notes/Account 2/Log.md`)
4. **Jokić triple-double record pre-build** (200 vs Westbrook's 209). Re-check his current count first. Status target `voice-ready` with a slot for the record night.
5. **Milestone calendar** → `Research Notes/Account 2/Milestones.md` (next 6 weeks, NBA + soccer). Pre-build the top 2.
6. **Soccer backlog:** Ronaldo Coca-Cola bottles first (script in `Soccer Channel/Productions/2026-10-27 S09 ...`; re-check every claim), then Henry, Ronaldinho, Pelé's laces (the FC run flagged a Pelé caution in the Idea Bank: read it), Lampard, Cantona, Balotelli. Each one only if it passes the footage test.
7. **NBA countdown test:** "3 times [star] did X" with a #3/#2/#1 badge.
8. **Real-audio passes** on built Shorts that have a live call.
9. **Sunday competitor review: tomorrow, Sun Nov 1** → `Competitors 2026-11-01.md`.
10. **Footage source map** → `Footage Sources.md` (the PC may reach sources the cloud couldn't. Note which.)
11. **Score the Rodman test.** It went up **Thu Oct 29 evening**, so its 72 h mark is **Sun Nov 1 evening** (the guide said Tue Nov 3 because it assumed a Saturday post). Compare its views with the channel median of about 4-6K. If it wins, plan 3 more NBA history stories.
12. **Music test tally** (#70, #72 music vs #71, #74 no music). Once #74 is 72 h old (about Mon Nov 2 afternoon if it went up Fri ~3 PM), write the comparison.
13. **Tool fixes:** `deflash.py` (keep audio, stream frames), `footage_qc.py` (follow `--profile story`), `assemble.py` (lock file or per-render temp names). Test each on a real Short.
14. **GTA 6 channel plan** from **Thu Nov 12** (launch Nov 19) → `GTA6 Plan.md`.

### Owner only (remind once at most)
Posting; the Monday Studio export for both channels; the YouTube Analytics sign-in (the new OAuth client may be for this: ask); swapping the old Gemini key.

## 3. Rules that matter most here
- Never post, schedule or open YouTube Studio. Push only to `account2`, never force-push. Don't edit `UPLOAD SCHEDULE.md`, `CLOUD STATE`, the Daily or Outcome logs, the Hubs or the to-do list.
- Before every commit: `git diff --cached | grep -c "AQ\.Ab8"` must print 0. Also grep the staged diff for `sk_`, `GOCSPX` and the database password: all must be 0.
- No cookies with yt-dlp, and no DRM or paywall workarounds. Never invent a stat. Render one at a time, never in parallel.
- End every session with 3-5 plain lines: what you did, what's queued, credits used, and anything only the owner can do.
