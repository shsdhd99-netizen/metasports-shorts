# Max Claude demo 01: How Fingerprints Catch Criminals (prep, Nov 3, 2026)

**Status:** PREP ONLY. Max sent the demo form (photo + about 60 s of voice) on the sales site. What's ready here: a fact-checked script, 12 free stock clips, 3 fingerprint illustration clips we drew ourselves, and the shot plan. **Blocked on three things:** (1) a Netlify token to fetch his photo and voice from the form, (2) the ElevenLabs key to make his instant voice clone, (3) an avatar service for the talking photo (HeyGen photo avatar or similar, in his account or ours).
**Format:** 9:16 1080x1920 (plus 16:9 on request), about 45 s, captioned and clean versions, light music under the voice, his face at the start and end.

## Script changes from the handover draft (fact-check)
- "ridges that split, stop and loop ... minutiae" became "the ridges split and stop": a loop is a pattern, not a minutia (Wikipedia: minutiae are ridge endings, bifurcations and short ridges; loops are one of the three patterns).
- "Then a computer compares it against millions of prints in seconds" became "searches a database of stored prints and suggests possible matches": no source read today for "millions" or "seconds".
- "the computer only suggests a match" became "for crime scene prints, the computer usually just suggests": some systems now auto-confirm high scores ("lights-out"), so "only" was too strong.
- "sweat and oil" became "moisture and oil" (the source's wording is "moisture and grease").

## Claims (every line, with its source)
| Line | Source | Exact wording |
|---|---|---|
| Fingerprints form in the womb, around the fourth month, and stay for life | [Wikipedia, Fingerprint](https://en.wikipedia.org/wiki/Fingerprint) | "formed at around the 15th week of fetal development and remain until after death" (15 weeks is about 3.5 months: "around the fourth month") |
| Not even identical twins share them | Wikipedia, Fingerprint | "Even identical twins (who share their DNA) do not have identical fingerprints." |
| Ridges split and stop; experts call these details minutiae | Wikipedia, Fingerprint | "Features of fingerprint ridges, called minutiae, include: Ridge ending: The abrupt end of a ridge. Bifurcation: A single ridge dividing in two" |
| Touching a glass leaves a copy (moisture and oil) | Wikipedia, Fingerprint | "Moisture and grease on fingers result in latent fingerprints on surfaces such as glass." |
| Investigators brush it with fine powder and the print appears | Wikipedia, Fingerprint | "Nonporous surfaces require the dusting process, where fine powder and a brush are used" |
| A computer searches stored prints and suggests possible matches | [Wikipedia, Automated fingerprint identification](https://en.wikipedia.org/wiki/Automated_fingerprint_identification) | "Latent to tenprint searching will frequently return many (often fifty or more) candidates" |
| For crime scene prints the computer usually just suggests; an examiner makes the call | same | "The confirmation of system-suggested candidates is usually performed by a technician in forensic systems." (and "lights-out" auto-confirm exists, hence "usually") |

Second sources to add before delivery: NIST or FBI pages for the first and last rows.

## Pictures, line by line (all licensed; see sources.csv)
| Line | Picture | File |
|---|---|---|
| Same since before you were born | **Max, talking (avatar), full frame** | from his photo |
| Form in the womb, fourth month | baby's feet / a hand holding a baby's hand | `stock_27331`, `stock_22238` |
| Stay with you for life | ridges appear as if dusted | `gfx_ridges` (ours) |
| Not even identical twins | two sisters who look alike (illustrative: not identified as twins) | `stock_12962` |
| Ridges split and stop; minutiae | close-up, three real splits/endings circled, "minutiae" | `gfx_minutiae` (ours) |
| Touch a glass, moisture and oil | magnifier close-up | `stock_13807` |
| Brush with fine powder, hidden print appears | investigator, UV light, a handprint appears on the wall (light, not powder: keep the line on the dusting graphic if this feels off) | `stock_32791`, `gfx_ridges` |
| Computer searches a database | partial print beside a stored print, scan bar, matching points | `gfx_match` (ours) |
| Usually just suggests; examiner decides | examiner at a magnifier lamp / microscope | `stock_46748`, `stock_4773` |
| Crime scene | evidence markers, investigators | `stock_4736`, `stock_32785`, `stock_32790` |
| Grab a door handle, you signed your name | door handle, then **Max, talking, full frame** for the last line | `stock_33712` + avatar |

Layout: Max full frame for the first and last lines; in between, B-roll full frame with Max in a small circle bottom-left for 2-3 lines (keeps his face on screen without covering the captions at mid-height). Captions centred, key word in colour.

## What makes this the best possible demo (when his files arrive)
- Voice: ElevenLabs Instant Voice Clone from his recording; check it says "minutiae" right (add a pronunciation fix if not); two takes, keep the clearer.
- Face: a talking-photo avatar from his photo, lip-synced to his cloned voice; check the mouth on every line with consonants (p, b, m).
- Edit with our pipeline; full QA; comfort audit; look at the first, middle and last frame.
- Deliver: 9:16 captioned, 9:16 clean, 16:9 if wanted, plus a note saying it's preview quality (the full version uses his 5-minute filmed recording and a professional clone).

## Second sources (checked Nov 4, 2026, WebSearch of nist.gov / ncbi.nlm.nih.gov)
- Row 1 (formed in the womb, stay for life): NIST-hosted [Annotated bibliography on latent print analysis](https://www.nist.gov/document/annotated-bibliography-latent-print-analysispdf): prints are stable from formation in fetal life until death. (Script says only "formed before you were born", which matches.)
- Row 2 (twins): [Fingerprint Recognition with Identical Twin Fingerprints, PMC3338710](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3338710/): twins' prints are not identical, only correlated.
- Last rows (computer suggests, examiner decides): [NIST, Accuracy and reliability of forensic latent fingerprint decisions](https://www.nist.gov/document/113uleryfullibpcpdf) and PMC3299696: AFIS returns candidates, the examiner assesses each (ACE-V). No FBI-specific page found; "usually" wording kept.
