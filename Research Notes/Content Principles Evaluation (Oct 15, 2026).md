# content-principles evaluation (Oct 15, 2026)

**Source:** https://github.com/aiwithremy/content-principles (88 stars, last push Oct 13 2026, not archived). **No licence file** (all rights reserved by default): fine for private use in our private repo, do not redistribute.
**Contents:** two text files, `README.md` and `content-principles/SKILL.md` (10.7 KB). No code, no dependencies, no network calls, no scripts, no hidden instructions (read in full).
**Install (done, reversible):** copied `SKILL.md` to `.claude/skills/content-principles/` in this repo, as the README says for Claude Code. Undo: delete that folder. Not installed to `~/.claude/skills`.

## What it says (10 sections)
One viewer, not "the audience"; value vs time cost; each line must sell the next line; curiosity loops (open a new one at 60-70%, never deflate one); specificity (a number/name/date beats a summary); a good idea fits in ten words and a 10-year-old gets every line; value in the first 3 s and delivered by 5-10 s; cut anything that doesn't serve the hook's promise; preempt the viewer's objection; more beats give the edit more places to cut. It tells the model to apply this silently, as priors, never as a checklist.

## Fit for MetaSports
Mostly agrees with what we already do (Winning Formula hook gate, Script Critic v3, specificity rules, "stayed to watch"). Useful additions: the **loop at 60-70%** test, the **"does line N sell line N+1"** read, the **ten-word idea** test, and **"cut the interesting-but-irrelevant line"**. Weak fit: written for business/creator content (its examples are ads accounts and apps), so "name the viewer" and "pre-empt 'this is an ad'" matter little for NBA facts; its "no template" stance conflicts with our numeric scoring, so keep our critic as the score and use this only as a second read.

## Test (honest scope)
Applied by reading it against the #42 script only (it is guidance, not a program; there is nothing to run). Result: line 1 sells line 2 (claim, then the number); the loop at 14.3 s ("So is he a worse shooter?", 61%) is where it says to re-open; the ending closes on a number with no new question, which it would flag as "stops, doesn't open" (our pinned comment carries that loop instead); "And he's the all-time leading scorer" is the one line it would test for fluff but it sets up the paradox. Same verdict as Script Critic (APPROVE, 34-36/45). **Not yet run on the other scripts and not compared on a rewrite**, so no claim that it improves results.

## Decision
Keep installed, optional second read after Script Critic; revisit after 10 posts.