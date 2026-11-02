# Mr. Claude (Max Claude): commission, state on Nov 2, 2026

**Client:** Max Claude, addressed as "Mr. Claude". Commission: high-quality AI videos with HIS OWN cloned voice and HIS OWN
face (AI avatar); we deliver files only, he posts. First example topic: a 45 s forensic science lesson, "How Fingerprints Catch Criminals".

## Sales site (live)
- **https://ondemand-studio.netlify.app** (brand "On Demand"). Source: `Clients/Max Claude/site/index.html` + `thanks.html`.
- Nov 2 update: framed as a helpful tool (not a replacement); demo = our S17 Short (20K views, `site/demo.mp4` built from the S17 real-audio DRAFT at 540p); stat 2.7M+ views over 148 Shorts (both channels, Nov 2); PayPal button in the final block is `hidden` until the owner gives a PayPal.Me link (replace PAYPAL_LINK, remove `hidden` on #paypal and #paypal-note).
- Sales tactics used: outcome headline, phone preview, "old way vs On Demand", our real view numbers as proof, 4-step process,
  guarantees (approve first, likeness stays his, sourced facts), low-friction CTA ("Reserve my setup" = a free draft script first),
  recording guide with a read-aloud script. No prices yet (owner paused pricing until the page is right).
- Netlify site id `795688f4-76fa-4c8f-b0fd-2a405dbb7415`. Visitor login protection turned OFF; form detection ON.
- **Leads:** Netlify → project ondemand-studio → Forms → `video-request` (add an email under Form notifications).
- **Deploy an update:** zip index.html + thanks.html, then
  `curl -X POST -H "Authorization: Bearer $NETLIFY_AUTH_TOKEN" -H "Content-Type: application/zip" --data-binary @site.zip https://api.netlify.com/api/v1/sites/795688f4-76fa-4c8f-b0fd-2a405dbb7415/deploys`
  The token must come from the environment (`NETLIFY_AUTH_TOKEN`), never chat or git. The owner should rotate the token
  that was pasted in chat on Nov 2.

## Pricing proposal (PAUSED; owner decides; PayPal invoices)
Setup $300 (voice clone + avatar + test video) · single video $150 (≤60 s) · Starter 4/mo $450 · Growth 8/mo $800 ·
Pro 16/mo $1,400 · add-ons: rush 48 h +$50, 16:9 copy +$40, extra revision +$25, 60-120 s +$75. 50% deposit on setup.
Basis (Nov 2 research): freelance avatar videos ~$150-400 simple, $300-900+ custom; packages $200-700/mo. His tools in his
name: ElevenLabs Creator (~$22/mo, professional voice clone), an avatar service such as HeyGen (~$29+/mo; check plan limits).

## Next
1. Owner reviews the site; then add pricing + PayPal links.
2. When Max records: build his voice clone and avatar in his accounts, make the fingerprint lesson (see
   `HANDOVER - Account 1 Client AI Videos.md` for the build prompt), deliver files.

## Nov 2 update 2
- Not social-media specific (he doesn't know the use yet): copy says "for whatever you need" (classes, training, talks, sites).
- PayPal button live at the bottom: https://www.paypal.me/vaughnpayne1 (no prices on the page yet).
- **Free self-preview on the site** (section "Try it with my face", form `demo-request`): he takes/uploads one photo (compressed to
  1600 px in the browser) and records ~60 s of voice in the browser (or uploads a voice memo), ticks consent, leaves contact.
  Files land in Netlify → ondemand-studio → Forms → demo-request (tested Nov 2 with a dummy upload, then deleted).
- **How to make his preview when it arrives:** ElevenLabs Instant Voice Clone from the recording (in an account he owns or that
  we delete after); a talking-photo avatar from the photo (HeyGen photo avatar or similar); voice the fingerprint script
  (`HANDOVER - Account 1 Client AI Videos.md`) and edit with our pipeline; 30-45 s, captioned, 16:9 and 9:16. Say it's preview
  quality; the full version uses his 5-minute filmed recording. Delete his files on request (consent text promises it).
