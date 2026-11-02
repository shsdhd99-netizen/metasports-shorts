# Handover: Account 1 starts AI videos for a client (Nov 2, 2026)

Paste into a new Claude session on Account 1 (terminal, in this repo, branch `main-329h3w`, after `git pull --no-rebase`).
Fill the CLIENT BRIEF first; nothing below works without it.

## CLIENT BRIEF (owner fills in)
- Client / brand: ______  Niche: ______  Platform(s): YouTube Shorts / TikTok / Reels / other ______
- Format: narrated story Short / explainer / product video / other ______  Length: ______
- Voice: our Alex voice, a new ElevenLabs voice, or the client's own ______ (whose ElevenLabs account pays?)
- Volume and deadline: ___ videos per ___, first delivery by ______
- Footage: client's own files / stock / licensed / AI-generated ______ (who owns the rights?)
- Brand rules: logo, colours, fonts, words to avoid, call to action ______
- Delivery: files only, or posted to the client's channel (whose sign-in?) ______
- Approval: who signs off, and how ______

## Prompt
```
You are starting a new line of work for the owner: AI-made short videos for a client, built with the MetaSports pipeline.
Read first: "HANDOVER - Account 1 Client AI Videos.md" (the brief), "00 START HERE.md", "Tools Guide.md",
.claude/skills/story-short/SKILL.md, .claude/skills/cloud-short/SKILL.md, "Research Notes/Full Review for Retention (Nov 2026).md",
"Research Notes/Editing Study (Nov 1, 2026).md". Those hold everything we learned making 100+ Shorts.

1. Set up a separate workspace: `Clients/<client>/` with its own Brand Kit.md (from the brief), Playbook.md, Idea Bank.md,
   Productions/ and a client-specific skill `.claude/skills/client-<name>/SKILL.md` adapted from story-short. Never mix client
   files, voices, music or tags with MetaSports; never post client work to our channels or ours to theirs.
2. Reuse the tools as they are (voice_take, tighten_voice, captions, cut_list, assemble, qa_short, tags_fit, yt_watch for
   competitor study with GEMINI_API_KEY); add brand options (logo corner, colours, font, end card only if the client wants
   one) as opt-in settings, never changing MetaSports defaults.
3. Research the client's niche the way we did ours: top channels' Shorts (yt_watch.py --channel <handle> --top 10), what
   topics and edits win, measured; write Clients/<client>/Niche Study.md with evidence tiers.
4. Make 2 pilot videos, full QA PASS, frames checked, in the client's brand; an UPLOAD.md each (title, caption, tags,
   pinned comment). Put them in Clients/<client>/Productions/ as "DRAFT - awaiting approval - ...".
5. Write Clients/<client>/Delivery.md: what was made, costs (ElevenLabs credits per video, Claude time), the plan for the
   agreed volume, and what you need from the owner/client.
Commit and push.

Rules: every output is a DRAFT the owner approves; never publish or schedule unless the owner turns that on for this client
with the client's own sign-in; never print, commit or ask for keys (they live in Tools/.env or environment settings); only
footage the client owns or that we can license or legally use; mark AI-made voice/visuals where a platform requires it;
never invent facts; no model names in commits.
```

## What Account 1 should know
- The pipeline makes 20-60 s vertical videos: script -> ElevenLabs voice (auto retakes) -> footage cut list -> captions ->
  render -> QA (`qa_short.py --full`) -> upload package. A finished Short costs about 3K ElevenLabs credits with retakes.
- Proven retention rules (ours, measured): open on the thing itself in frame 1, line 1 under 11 words, few cuts in the first
  5 s, a turn every 8-12 s, end on the payoff with nothing after. Details in the two research notes above.
- Scheduling: `Tools/yt_schedule.py` + `Tools/yt_auth.py` can schedule to a channel the client signs in to, if wanted.
- Keys on the PC: `Tools/.env` (ElevenLabs, Gemini, YouTube). Check whether the client's work should run on a separate
  ElevenLabs account so MetaSports credits aren't used up.
