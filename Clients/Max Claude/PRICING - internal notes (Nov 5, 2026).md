# Max Claude pricing: internal notes (owner only; not on the site)

**Quote sent on the site and in `site/quote.html`:** setup $129 (voice + face + first full video, 2 revision rounds, refund of the setup if unhappy after two rounds); per video $45; Lesson Pack 4 a month $149; Class Pack 8 a month $259; extras: 60-120 s +$20, custom diagram +$15 each, 24 h rush +$25, third revision round $10; deposit $65 (half of setup); founding prices locked 12 months. All of this is a proposal for the owner to change.

## Why these numbers
- **Affordable for a teacher paying out of pocket:** $129 once, then $45 a video or $149 a month (about the price of a streaming-plus-phone bill). The comparison he will make is hiring an editor/actor, or learning 3 tools himself and paying a subscription for each (voice, face, editing) plus hours per video.
- **Worth it for us:** after setup the pipeline takes about 60-90 minutes a video (script and fact check 20-30 min, voice 5 min, avatar clip generation 10-15 min of waiting, captions/B-roll/QA 20-30 min, delivery 5 min). At $45 that is about $30-45 an hour; a 4-pack at $37 a video about $25-37; an 8-pack at $32 about $21-32 (the volume discount is paid for by batching: one research session, one voice session, one render queue). Setup $129 covers about 3 hours (voice clone build and check, face model, template, the first video, 2 revisions) = about $40 an hour.
- **Hard costs per video** (estimates, check the real plan numbers before relying on them): voice about 700-1,000 characters of ElevenLabs credits (under 1% of a 121K-character monthly plan, about $0.10-0.30 at current plan prices); avatar clips on Dreamina Basic ($15 a month, about 1,100 credits left as of Nov 4; a 44 s video used two clips, so roughly 300-500 credits is the likely cost: **measure it on the next build**); LatentSync runs free on the PC GPU (about 8-10 minutes a clip); hosting free. So tool cost is about $3-6 a video, $15-25 a month shared, and the plan can be shared with MetaSports' ElevenLabs.
- **Break-even:** one setup plus one pack covers the tools for 3+ months. The risk is time, not cash.

## Sensitivity (change the quote if the real time per video is above 90 minutes)
| If a video takes | $45 video | 4-pack $149 | 8-pack $259 |
|---|---|---|---|
| 60 min | $45 an hour | $37 | $32 |
| 90 min | $30 | $25 | $21 |
| 120 min | $22 | $19 | $16 |
Raise to $59 / $189 / $329 if it stays above 2 hours. Lower the pack discounts first if you want a higher floor.

## Negotiating room and guardrails
- Offer the founding-client rate for 12 months only if he commits to a pack; otherwise pay-as-you-go.
- Do not discount the setup (it carries the risky work). A pilot at $65 (half of the setup) is already the deposit.
- The refund promise is the main risk reducer for a hesitant client; keep it to the setup only.
- Payment is PayPal (paypal.me/vaughnpayne1) as on the site: remind him that PayPal fees (about 3-4%) come out of each payment.
- The quote makes no claims about results beyond what the draft shows.

## What the owner has to decide
1. Are the prices right (or use the sensitivity table)? 2. Keep the setup-fee refund promise? 3. Founding-rate lock for 12 months? 4. The $65 deposit link in the site goes to paypal.me/vaughnpayne1/65USD.
