# Round 7: Viewer retention, deep dive (Oct 4, 2026)

*Scope: one question only. Why do people keep watching a Short or swipe, how does YouTube measure it, how do creators get above 100% average percentage viewed (APV), and what exactly should we change in a 22-30 s AI-voiced NBA story Short. The broad "what makes Shorts viral" note is Round 6 (another agent); this one does not repeat topic/title work.*

*Method: official YouTube Help pages first, then peer-reviewed science, then public datasets, then vendor blogs (always labelled). Channel numbers were pulled today with yt-dlp (public view counts and durations only). Nothing was uploaded, no keys were touched, no existing Short folder was edited. All numbers marked "computed" were calculated by me today from the CSVs in this folder or from the yt-dlp pull; the scripts are tiny and the raw pull is described in section 6 so it can be re-run.*

## Evidence labels (used on every recommendation)

- **PROVEN** = an official platform statement of a definition or mechanic, or a number computed from public data (a real pattern in the data, not proof of cause), or a large peer-reviewed dataset measuring exactly this behaviour.
- **SUPPORTED** = peer-reviewed experiment or meta-analysis of the mechanism in a nearby medium (TV, film, radio, surveys, MOOC video), or two or more independent credible sources. Translating it to Shorts is my inference.
- **HYPOTHESIS** = plausible mechanism, vendor claim, or my own rule of thumb. Goes on the A/B list; do not treat as fact.

Honest limit up front: **no public study randomises editing choices on YouTube Shorts and measures retention.** Everything about "this edit raises retention by X%" is either vendor opinion or inference from lab science. I say so wherever it applies. The one thing that would change this note most is our own Studio retention data, which I do not have (see section 7.6).

---

## 0. The twelve findings that matter (read this if nothing else)

1. **YouTube's funnel is: Shown in feed -> Viewed vs swiped away ("stayed to watch") -> engaged view -> average view duration (AVD) and average percentage viewed (APV) -> retention curve.** AVD and APV are calculated only among viewers who stayed past the "initial seconds" (YouTube does not publish the threshold). A Short can therefore have a great APV and still be throttled if the stay rate is poor. [PROVEN, section 1]
2. **Since Mar 31, 2025 a public "view" counts the moment a Short starts or replays, with no minimum watch time; since Aug 24, 2026 the same rule applies to all formats.** The old stricter count survives as "engaged views" (loops excluded) and still drives monetisation. Public view counts are now a reach number, not a retention number, and pre-Mar-2025 benchmarks (Galloway 2023, REBOUND's 2022-23 sample) are not comparable. [PROVEN]
3. **APV above 100% simply means replayed watch time is counted among engaged viewers.** Official pages confirm that rewatching shows as spikes and that segment views can exceed total views; the explicit "APV > 100%" wording is second-hand. [PROVEN mechanism / second-hand wording]
4. **Most short-video sessions end very early.** Measured: >40% of videos on a large commercial short-video service were watched under 25% of their length (22 billion playbacks), and in a 50-person x 100-Shorts crowdsourced test about 70% of viewing sessions ended before 20% of the video. So the stay-or-swipe decision is the whole game for the first seconds. [SUPPORTED, section 3.1]
5. **The strongest scientific explanation of swiping is foraging, not "short attention span":** viewers leave a "patch" when the information rate drops below what the next swipe is likely to give. That predicts the rule "never go more than a few seconds without new information", not "cut as fast as possible". [SUPPORTED mechanism, HYPOTHESIS for the number]
6. **Cuts, sound changes and voice changes trigger an involuntary orienting response that improves encoding of what follows, but too much stimulation overloads (Lang's model; in the 1999 pacing study memory peaked at medium pacing and fell at high pacing, with the biggest penalty for arousing content).** Crucially, **voice changes did not habituate over six repetitions while jingles and production effects did.** Our real-quote bursts are the right kind of re-hook; repeated whooshes are the wrong kind. [SUPPORTED]
7. **"Faster cutting retains more" has no direct evidence.** The best science says tight, coherent editing synchronises viewers (Hasson), and shuffling shot order destroys it; it does not say 1.4 s beats 2.2 s. Our 1.9 s gate and "new image every second until 5 s" are HYPOTHESIS. [honest gap]
8. **The Zeigarnik effect (unfinished tasks are remembered better) failed to replicate (2025 meta-analysis, 37 studies: ratio 0.99). The urge to resume an interrupted task did replicate (~67% resume).** Use "open loop" as "viewers want to finish it", never cite Zeigarnik. Curiosity peaks at intermediate confidence (Kang 2009) and needs a small priming dose (Loewenstein). [SUPPORTED]
9. **Our captions and voice are faster than a person can read.** Our speech is about 21-24 characters per second (measured, 9 Shorts); caption displays median 0.6-1.0 s with peaks of 28-36 cps. Netflix's own limit for adults is 20 cps; average adult silent reading is 238 wpm; listening comprehension in the classic studies starts to fall near 275 wpm. Muted viewers (69% in public places, Verizon/Publicis survey) cannot keep up with a 250-wpm voice. [PROVEN measurement + SUPPORTED]
10. **Length is a weak lever. Topic and audience dominate.** Pooled over 403 Shorts from 5 channels, within-channel duration vs views has rho = +0.12. CoachClank (n=149): 21 s+ Shorts have 3.3x the median views of 20 s or less (978K vs 300K, p=0.002) but the relation is non-monotonic (15 s or less 490K beats 16-20 s 265K), our own channel shows no length effect, and a large published study found topic/channel context explains most of engagement variance (R2 = 0.77). [PROVEN pattern, causality unknown]
11. **Our own 60 NBA-era Shorts are stuck on a plateau: 46 of 60 landed between 20K and 45K views (max 2.6x the median).** Every duration bucket and title style has the same median (29.7-32.8K). CoachClank's max is about 65x its median. That shape looks like a fixed test audience that no Short has escaped, which means the missing ingredient is a retention signal strong enough to trigger expansion, not topic tweaks. [PROVEN pattern, cause HYPOTHESIS]
12. **We have never read our own retention data.** No Viewed %, APV, AVD or curve is in the repo. Every retention rule in the skill (70% at 3 s, 1.9 s shots, loop) is imported from other creators. Exporting Studio's per-Short numbers is the highest-value 30 minutes available. [PROVEN gap]

---

## 1. How YouTube defines and shows Shorts retention

### 1.1 The funnel in YouTube's own words

| Studio item | Official wording or fact | Source | Label |
|---|---|---|---|
| **Shown in feed** | "The number of times that your Shorts showed in the Shorts Feed." | [YouTube Help, Content tab tips - Shorts](https://support.google.com/youtube/answer/12942217?hl=en-GB&co=YOUTUBE._YTVideoType%3Dshorts) | PROVEN |
| **How many chose to view / "Viewed vs swiped away" / "Stayed to watch"** | "This report highlights the percentage of times that viewers viewed your Shorts versus swiped away." Same help text: "How viewers engaged: the percentage of times that viewers stayed to watch past the initial seconds of a Short." | [same page](https://support.google.com/youtube/answer/12942217?hl=en-GB&co=YOUTUBE._YTVideoType%3Dshorts), [Studio app help](https://support.google.com/youtubecreatorstudio/answer/12220281?hl=en-GB&co=GENIE.Platform%3DAndroid) | PROVEN |
| Threshold for "stayed" | "Past the initial seconds." No number published. (Instagram, by contrast, defines skip rate as leaving in the first 3 s.) | [Instagram's definition quoted by Social Media Today, Aug 2025](https://www.socialmediatoday.com/news/instagram-adds-retention-insights-reels/758464/) | PROVEN that it is unpublished |
| **Engaged views** | The pre-Mar-2025 Shorts view logic, kept as a metric: "how many times viewers stayed to watch past the initial seconds", and it "doesn't include loops". Advanced Mode only. YPP earnings use "engaged Shorts views". | [YouTube Help Community announcement, relayed by PPC Land](https://ppc.land/youtube-changes-how-shorts-views-are-counted-from-march-31/), [YouTube Help](https://support.google.com/youtubecreatorstudio/answer/12220281?hl=en-GB&co=GENIE.Platform%3DAndroid) (loops-excluded wording is second-hand: [Creator Essentials glossary](https://www.creatoressentials.com/glossary/shorts-engaged-views/)) | PROVEN (counts), loops wording second-hand |
| **Average view duration (AVD)** | "Average minutes watched among those who stayed to watch. This is calculated from engaged views and their corresponding watch time." | [YouTube Help, Understand your engagement](https://support.google.com/youtube/answer/9313698?hl=en) | PROVEN |
| **Average percentage viewed (APV)** | AVD divided by video length. For Shorts the same engaged-views basis applies (vendor wording: "calculated from engaged views + watch time"). I could not retrieve a Help page that defines APV explicitly (those pages render with JavaScript), so treat the formula as second-hand. | [Shortimize, Jan 2026](https://www.shortimize.com/blog/youtube-shorts-retention-rate) | second-hand |
| **Audience retention curve** | Flat line = watched fully; gradual decline = natural loss; **spikes = rewatched or shared segments**; dips = skipped or stopped. "Absolute views for individual segments may exceed total views because within a single view the same viewer may watch portions multiple times." | [YouTube Help, Measure key moments for audience retention](https://support.google.com/youtube/answer/9314415) | PROVEN |
| "Key moments" highlights | Need a video of at least 60 s and 100+ views, so **our 22-30 s Shorts get no key-moment card**; read the raw curve instead. | [same page](https://support.google.com/youtube/answer/9314415) | PROVEN |
| Compare to similar-length videos | Studio's "typical retention" compares against videos of similar length. Benchmarks must be length-matched. | [YouTube Help](https://support.google.com/youtubecreatorstudio/answer/12220281?hl=en-GB&co=GENIE.Platform%3DAndroid) | PROVEN |

### 1.2 What changed in how views are counted (2025-2026)

| Date | Change | Source | Label |
|---|---|---|---|
| Mar 31, 2025 | Shorts views are counted "from the moment a video starts to play or replay, with no minimum watch time". The old logic is kept and renamed "engaged views". YPP earnings and eligibility unchanged. | [PPC Land summary of the YouTube Help Community post](https://ppc.land/youtube-changes-how-shorts-views-are-counted-from-march-31/), [Digital Music News](https://www.digitalmusicnews.com/2025/03/27/how-does-youtube-shorts-count-views-2025/) | PROVEN (relayed) |
| Aug 24, 2026 | "Views are counted the moment that a video starts to play across all formats, including Shorts, long-form videos (VOD) and live streams." YPP earnings still use "engaged Shorts views" and "engaged watch hours". | [YouTube Studio Help, Understand your YouTube content performance](https://support.google.com/youtubecreatorstudio/answer/12220281?hl=en-GB&co=GENIE.Platform%3DAndroid), [LiveReacting explainer quoting YouTube](https://blog.livereacting.com/youtubes-new-view-count-rule-what-changes-august-24/) | PROVEN |
| Oct 15, 2024 | Shorts may be up to 3 minutes (vertical or square, 3 min or less). | [Descript](https://www.descript.com/blog/article/how-long-can-youtube-shorts-be) (second-hand) | second-hand |

**What it means for us.**
- Public view count includes replays and instant swipes. A Short with 30K views could have 12K engaged views. Use **Engaged views** (Advanced Mode) and **Viewed %** for any retention judgement. [PROVEN]
- Our 2025-26 channel data is all post-Mar-2025, so internal comparisons are consistent. Competitor samples from 2022-23 (REBOUND) were counted under the old rule: use them for topic lanes only. [PROVEN]
- Every vendor blog that gives a "good retention" number from before 2025 is describing a different denominator. [SUPPORTED]

### 1.3 What >100% APV means, precisely

- APV = average watch time among engaged viewers divided by video length. Replayed seconds add to watch time but a loop is **not** an extra engaged view (second-hand), so APV can exceed 100% when engaged viewers watch more than one pass. [second-hand; mechanism PROVEN by the segment-views statement above]
- The curve shows it as values above 100% in the early seconds (every replay re-watches second 0 onwards) or as mid-video spikes (rewatched or shared moments). [PROVEN for spikes; "above 100% at second 1" is vendor wording: [Aibrify](https://aibrify.com/blog/youtube-shorts-retention-curve-playbook)]
- Two causes look identical in the curve: replay because it was great, replay because it was confusing. [Shortimize](https://www.shortimize.com/blog/youtube-shorts-retention-rate) calls them "good spike / bad spike". [SUPPORTED, logical]
- **YouTube has not said that APV above 100% is a ranking trigger.** What YouTube has said publicly: the system looks at whether viewers choose to watch, how long they stay, and satisfaction signals (surveys, likes, "not interested"); there is "not a certain length that benefits creators"; thumbnails and publish time barely matter for Shorts. [TechCrunch, Aug 2023 (YouTube Shorts Q&A)](https://techcrunch.com/2023/08/25/youtube-demystifies-the-shorts-algorithm-views-and-answers-other-creator-questions/) [PROVEN, 2023]. Claims that ">100% is the strongest signal" or "80% APV unlocks reach" trace to vendor blogs ([Humble&Brag](https://humbleandbrag.com/blog/youtube-shorts-benchmarks), [Aibrify](https://aibrify.com/blog/youtube-shorts-retention-curve-playbook)); Aibrify's page even attributes the 80% figure to "TubeBuddy and Creator Insider" without a link. [HYPOTHESIS]
- I could not read Creator Insider transcripts (video, JavaScript pages). Anything attributed to Creator Insider here is second-hand.

---

## 2. Why people stay or swipe: the science, translated

Format: finding -> what it says about our Shorts -> evidence label for the translation.

### 2.1 The stay/swipe decision as foraging

- **Information foraging theory** (Pirolli and Card, PARC) applies the **marginal value theorem**: leave a patch when the rate of gain inside it falls to the average rate you could get elsewhere (including travel cost). [Overview](https://www.uxtigers.com/post/information-foraging), [MVT and human foraging](https://www.nature.com/articles/s41598-017-11763-3). In a feed the "travel cost" is one thumb swipe, so the leaving threshold is extremely low. This is the cleanest explanation of why a Short that is merely fine loses people.
- Translation: the viewer is continuously estimating "new useful information per second" versus "what the next Short might give". Stay requires (a) a visible promise at 0-1 s and (b) a steady stream of small rewards. **Rule: no stretch longer than about 3-4 s without a new fact, new image or new voice.** [SUPPORTED mechanism; the 3-4 s figure is my HYPOTHESIS]

### 2.2 Orienting response, cuts, sound and the limited capacity model

- **Lang's LC4MP:** people have limited processing capacity; novel or signal-bearing stimuli (cuts, sound onsets, voice changes) trigger an **orienting response (OR)**, shown by heart-rate deceleration and skin-conductance rise, which directs resources to encode what follows. [Wikipedia summary with citations](https://en.wikipedia.org/wiki/LC4MP), [Fisher, Keene, Huskey, Weber 2018 review](https://academic.oup.com/anncom/article/42/4/270/7905951). Both related and unrelated cuts caused cardiac orienting.
- **Pacing has an inverted-U for memory.** Lang, Bolls, Potter and Kawahara (1999): for non-arousing content memory rose with pacing, peaking at medium pacing and declining at high pacing; the penalty for fast pacing is largest with arousing content. [J. Broadcasting & Electronic Media 43](https://www.scirp.org/reference/referencespapers?referenceid=1646487) (abstract as relayed). A later study (Fox, Park, Lang 2007) found that being resource-rich can become a "negative resource": [SAGE](https://journals.sagepub.com/doi/10.1177/0093650207300429).
- **Audio:** eight of nine auditory structural features (sound effects, voice changes, silence onset, etc.) elicited orienting in radio listeners and raised recognition of what followed. **Voice changes still elicited orienting after six repetitions in two-minute dialogues; jingles and production effects habituated.** [Potter, Lang, Bolls on audio structural features](https://www.semanticscholar.org/paper/Identifying-Structural-Features-of-Audio-Orienting-Potter-Lang/4caf5aae24fa5a42fea60f99e7337e517c517078), [habituation paper](https://www.researchgate.net/publication/276929868_I've_Heard_That_Before_Habituation_of_the_Orienting_Response_Follows_Repeated_Presentation_of_Auditory_Structural_Features_in_Radio) (habituation result as summarised in search; I did not read the full text). Sound effects raised attention and recall in radio ads ([Rodero 2019, "spark orientation effect"](https://journals.sagepub.com/doi/abs/10.1177/0093650215609085)).
- Translation:
  1. Our **quote bursts (a different real voice cutting in)** are the best-supported re-hook we own. Use 2-3 per Short rather than one long one. [SUPPORTED mechanism, HYPOTHESIS for Shorts retention]
  2. **Repeating the same whoosh/boom will habituate.** Keep SFX rare (2-5) and varied, only where something happens on screen. [SUPPORTED mechanism]
  3. **Do not stack cuts on the lines that carry the number or name** (the thing viewers must encode). Hold the shot 1.5-2.5 s there; cut fast on connective narration. [HYPOTHESIS, derived from the pacing inverted-U]
  4. A deliberate beat of silence before the payoff would count as an orienting event for radio listeners. Untested in Shorts. [HYPOTHESIS]

### 2.3 What the eye does: motion, surprise, gaze cues, faces

- **Carmi and Itti (2006):** in dynamic scenes, low-level **motion and flicker** are causally predictive of where people look; some static cues are only correlates. [Vision Research 46](https://ilab.usc.edu/publications/R.Carmi.html) (abstract). Itti and Baldi (2009): **Bayesian surprise** predicted gaze better than 10 other saliency measures; 72% of gaze shifts landed on locations more surprising than average (84% when all subjects agreed). [PubMed](https://pubmed.ncbi.nlm.nih.gov/18834898/?dopt=Abstract).
- **Smith, Attentional Theory of Cinematic Continuity:** viewers' gaze is guided across cuts by off-screen sound, motion, gaze direction and pointing; **attentional synchrony** (many viewers looking at the same place) rises with contrast, motion and flicker. [Smith 2012](https://ualresearchonline.arts.ac.uk/id/eprint/21187/2/6679.pdf).
- **Hasson et al. 2008 (neurocinematics):** a tightly edited commercial and Hitchcock produced higher inter-subject brain synchrony than an unedited concert clip; shuffling a film's shot order lowered synchrony in higher-order regions. [Projections 2008 PDF](https://www.motionpictures.org/wp-content/uploads/2013/01/Hasson-etal_NeuroCinematics2008.pdf), [overview](https://www.researchgate.net/publication/233713701_Neurocinematics_The_Neuroscience_of_Film).
- **Faces:** the fast-track modulator model says direct gaze is detected quickly via subcortical routes ([Senju and Johnson 2009](https://www.researchgate.net/publication/24011071_The_eye_contact_effect_Mechanisms_and_development)); face "pop-out" in search ([Hershler and Hochstein 2005](https://www.semanticscholar.org/paper/At-first-sight:-A-high-level-pop-out-effect-for-Hershler-Hochstein/34b78445102a969d236497138dca28d32efcf07c)) is contested, and a 2025 paper failed to replicate attentional capture by real and illusory faces ([Psychological Research](https://link.springer.com/article/10.1007/s00426-025-02211-3)).
- Translation:
  - Frame 0 with real motion (or a close face with direct gaze) is consistent with both lines of evidence; **do not claim faces beat action**, A/B it. [SUPPORTED motion; HYPOTHESIS face-vs-action]
  - Make each cut **continuity-driven**: match the direction of motion or gaze across the cut and cut on action. Hasson's shuffled-order result is the best evidence we have that b-roll must *relate* to the line being spoken, not just be "on topic". [SUPPORTED]
  - A **surprising** image (size gap, odd object, unexpected result) is exactly what draws gaze: this is the visual version of the "one-second oddity" lane that wins on CoachClank. [SUPPORTED mechanism]
  - Gaze cues inside footage (a player looking at something) can steer the eye to our headline text. [HYPOTHESIS]

### 2.4 Curiosity, open loops, prediction, variable reward

| Mechanism | Finding | Source | What it means for us | Label |
|---|---|---|---|---|
| **Information-gap curiosity** | Curiosity arises from a perceived gap between what you know and want to know; "a small amount of information serves as a priming dose"; satiation when enough is consumed. | [Loewenstein 1994 overview](https://www.researchgate.net/figure/Figure-1-Lowensteins-1994-theory-of-information-gap_fig1_364061951), [PsychologyFanatic summary](https://psychologyfanatic.com/information-gap-theory/) | The hook must give **one concrete fact** (the number, the odd detail) so the gap exists. A pure teaser ("you won't believe...") has no gap. After the payoff, curiosity is satiated: **stop talking**. | SUPPORTED |
| **Curiosity peaks at intermediate confidence** | fMRI: curiosity and reward-circuit activation rose with an inverted-U of confidence; memory improved for the answers. | [Kang et al. 2009, Psychological Science](https://pubmed.ncbi.nlm.nih.gov/19619181/) | Best hooks make the viewer *guess* ("Do you think he took a pay cut of 5%, 20%, 50%?") and then refuse to confirm. Generating a guess raises curiosity ([Nature npj Science of Learning 2019](https://www.nature.com/articles/s41539-019-0056-y)). | SUPPORTED |
| **Zeigarnik (memory for unfinished tasks)** | Meta-analysis (Ghibellini and Meier 2025): across 37 studies the interrupted/completed recall ratio was 0.99; fewer than a third of 44 replications found the advantage. The **Ovsiankina urge to resume** held (~67% resumed). | [Semantic Scholar record](https://www.semanticscholar.org/paper/Interruption,-recall-and-resumption:-a-of-the-and-Ghibellini-Meier/c98a41f13fd6f3b0b86047ecf92eeb03ac458626), [Mendeley](https://www.mendeley.com/catalogue/3e06bd6a-053c-356f-aed0-524bb30b28cc/) | Delete "Zeigarnik" from our vocabulary. "Open loop" = the viewer wants to *resume* the interrupted question. The loop must be **explicit** (a stated question) or the resume urge never forms. | SUPPORTED |
| **Prediction error / reward** | Dopamine neurons signal reward minus prediction; response grows with surprise; a separate ramp tracks **uncertainty, maximal at p=0.5**. | [Schultz et al. summary](https://www.pnas.org/doi/10.1073/pnas.1014269108), [Fiorillo, Tobler, Schultz 2003](https://www.semanticscholar.org/paper/Discrete-Coding-of-Reward-Probability-and-by-Fiorillo-Tobler/91bf62ef88c5f1308b060ae684923c8bf4db004a) | Frame stories as a **two-outcome question** (right or wrong, legal or illegal) so uncertainty stays near 50% until the reveal; then deliver an unexpected twist. Animal/neuro work, so only a mechanism. | SUPPORTED (neuro) / HYPOTHESIS (video) |
| **Suspense vs curiosity vs surprise** | Structural-affect theory: **suspense** = delay a known-to-be-coming outcome; **curiosity** = give the outcome first, hide the events that led to it; **surprise** = withhold information then reveal an unexpected event. | [Brewer and Lichtenstein 1982](https://journals.scholarsportal.info/details/0304422x/v27i0004/277_scashdacpoas.xml), [review](https://www.sciencedirect.com/science/article/pii/S0304422X22000262) | Our openers ("92% pay cut. LeBron just took one") are the **curiosity** type (outcome first). The mid-video "twist" is the **surprise** type. A "wait for it" countdown is the **suspense** type. Pick one per Short; mixing all three in 25 s dilutes each. | SUPPORTED |
| **Narrative transportation** | Absorption in a story changes beliefs and reduces counter-arguing. | [Green and Brock 2000 record](https://researchconnect.buffalo.edu/en/publications/the-role-of-transportation-in-the-persuasiveness-of-public-narrat/) | Needs concrete imagery and a character, which favours named people and scenes over abstract rules. TikTok-commissioned Neuro Insight research (sponsor-funded) found "crafting a creative story" gave **+16% watch time**, real people +9%, remixing a trend +14% ([TikTok for Business, 2023](https://ads.tiktok.com/business/en-US/blog/resonance-key-factor-ad-effectiveness)). | SUPPORTED (+ sponsored data) |
| **Peak-end rule, duration neglect** | Retrospective ratings of affective film clips used peak and final moments; clip duration barely mattered. | [Fredrickson and Kahneman 1993, summary](https://link.springer.com/content/pdf/10.3758/PBR.15.1.96.pdf) | It governs **how the Short is judged afterwards** (like, share, comment, next-Short willingness; YouTube also asks satisfaction surveys), not minute-by-minute retention. Put the strongest moment in the last third and end on it. | SUPPORTED |
| **Goal gradient and progress cues** | Effort and speed rise as the goal nears; "illusory progress" works. In web surveys, **fast-to-slow progress bars reduced drop-off, slow-to-fast increased it.** | [Kivetz, Urminsky, Zheng 2006](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2733214), [Conrad et al. 2010 / Villar 2013](https://openaccess.city.ac.uk/id/eprint/14427/4/Social%20Science%20Computer%20Review-2013-Villar-744-62.pdf) | Numbered structure ("3 rules", "2 of 3") gives progress cues and a visible finish line. Front-load progress (items 1 and 2 land fast, item 3 is the big one). Survey evidence only. | SUPPORTED (surveys) / HYPOTHESIS (video) |
| **Arousal drives sharing** | In ~7,000 New York Times articles, high-arousal emotions (awe, anger, anxiety) were more viral than low-arousal (sadness); positive content more viral than negative. | [Berger and Milkman 2012, Journal of Marketing Research](https://www.researchgate.net/publication/228137203_What_Makes_Online_Content_Viral) | Governs **sends**, not retention. Prefer awe (size gaps, impossible plays) and outrage (rules, "caught") over sad or wholesome. Matches the rule/oddity lane in Rounds 4-5. | SUPPORTED |

### 2.5 Reading, listening, captions, mute viewing

| Fact | Source | Implication | Label |
|---|---|---|---|
| Average adult silent reading: **238 wpm non-fiction**, 260 fiction (190 studies, 18,573 participants). | [Brysbaert 2019](https://gwern.net/doc/psychology/linguistics/2019-brysbaert.pdf) | Our voice (221-259 wpm, measured) is at or above reading speed. | PROVEN |
| Netflix English subtitle limit: **up to 20 characters/second for adults**, 42 characters per line, 2 lines. | [Netflix Timed Text Style Guide](https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-Timed-Text-Style-Guide) | Our captions run 21-25 cps median with peaks of 28-36 cps (measured, section 6.4). Over the limit by 10-80%. | PROVEN |
| Listening comprehension of time-compressed speech held to roughly **260-275 wpm**, then fell quickly (Foulke and Sticht 1969; Carver 1973), via a review. | [JLTR review](https://www.academypublication.com/issues/past/jltr/vol01/05/23.pdf) | Round 5's "240-290 wpm" upper bound exceeds the classic knee. Use 230-270. Caveat: compressed speech, not natural fast talkers. | SUPPORTED |
| In 6.9 million MOOC video sessions, **shorter videos and instructors who speak fairly fast with high enthusiasm were more engaging**. | [Guo, Kim, Rubin 2014](https://pg.ucsd.edu/publications/edX-MOOC-video-production-and-engagement_LAS-2014.txt) | Fast is good if energetic; fast and flat is not. Supports ~240-260 wpm with pitch variation. | SUPPORTED |
| **Redundancy principle** (Mayer): graphics + narration beat graphics + narration + identical on-screen text for learning; later work questions how general this is. | [overview](https://www.devlinpeck.com/content/mayers-principles-of-multimedia-learning), [2026 critique](https://www.tandfonline.com/doi/full/10.1080/01443410.2026.2678483) | Verbatim word-for-word captions add load for sound-on viewers; short 3-4 word chunks reduce it; fully muted viewers need the text. | SUPPORTED |
| Eye tracking of 211 viewers of a vertical TikTok video: **two-line subtitles drew more total fixation, more revisits and less skipping than one-line**, even controlling for character count. | [Li 2026, Applied Cognitive Psychology](https://onlinelibrary.wiley.com/doi/10.1002/acp.70262?af=R) (via search abstract) | Captions pull the eyes off the picture. One short line keeps the eyes on the action; two lines hold the eyes on text. | SUPPORTED |
| **69% of US consumers (n=5,616) watch video with sound off in public places**; 80% say they are more likely to watch a whole video with captions (survey, self-report). | [Forbes on the Verizon Media/Publicis study](https://www.forbes.com/sites/tjmccue/2019/07/31/verizon-media-says-69-percent-of-consumers-watching-video-with-sound-off/), [RBR](https://rbr.com/video-captions-study/) | Design for sound-off **and** sound-on: the hook must work as a picture plus ~4 words of text. | SUPPORTED (survey, 2019) |

### 2.6 Duration confounds every retention number

- A platform that optimises watch time is biased toward long videos; Kuaishou researchers built **D2Q** to remove duration bias by predicting watch-time quantiles within duration groups. [Zhan et al., KDD 2022](https://arxiv.org/abs/2206.06003). YouTube Studio itself compares to similar-length videos (section 1.1). Conclusion: **APV/AVD are judged relative to length class; compare like with like only.** [PROVEN that Studio does it, SUPPORTED that platforms normalise]
- In 5.3 million YouTube videos, engagement (time and average percentage watched) was predictable with **R2 = 0.77 from video context, topic and channel information alone**. [Wu, Rizoiu, Xie, ICWSM 2018](https://arxiv.org/abs/1709.02541) (long-form, 2016). Translation: how much of a video gets watched is mostly decided by topic and audience match before editing starts. Editing moves the rest. [SUPPORTED]
- In another large dataset, view duration was positively associated with like-per-view and view count ([Park, Naaman, Berger 2016](https://arxiv.org/abs/1603.08308)).

---

## 3. Retention-curve science for short-form

### 3.1 How fast do people leave? (measurements, with their limits)

| Measurement | Number | Who / limits | Label |
|---|---|---|---|
| Large Chinese short-video service, 22B playbacks | **>40% of videos had playback under 25%** | Zhang, Liu, Guo, Lee, IEEE TMC 2023 ([abstract](https://dl.acm.org/doi/10.1109/TMC.2021.3139893); the 40% figure is as cited by the 2026 paper below) | SUPPORTED |
| 229,178 retention curves from YouTube and Bilibili | Short videos show early abandonment, average playback under 50% (as cited) | Chen, Zhu, Jiang, Hu, MMSys 2024 ([vRetention](https://dl.acm.org/doi/abs/10.1145/3625468.3652175)); not Shorts-specific | SUPPORTED |
| 50 crowdsourced viewers x 100 YouTube Shorts (avg 35 s, 4-81 s) in a Shorts-style player | **About 70% of viewing sessions ended before 20% of the video** | [Yen et al., arXiv 2603.22663, Mar 2026](https://arxiv.org/html/2603.22663v1). Participants aged 18-30, no personalised feed, so they swipe more than real users. | SUPPORTED |
| 33 channels, 5,400 Shorts (Apr 2023) | Viewed-vs-swiped under 60% rarely performed; best Shorts 70-90%; higher viewed% did not guarantee success; engagement metrics (likes etc.) not strongly related | [Paddy Galloway thread](https://threadreaderapp.com/thread/1646898356419981315.html). Pre-Mar-2025, observational, YouTube-defined "viewed" threshold unknown. | SUPPORTED |
| Instagram | Skip rate = share of views that left within 3 s; shown with a retention chart since Aug 2025 | [Instagram via Social Media Today](https://www.socialmediatoday.com/news/instagram-adds-retention-insights-reels/758464/) | PROVEN (definition) |
| TikTok | "50% of an ad's impact in the first 2 seconds", "63% of top performers earn attention in 3 s", 70-85% 3-s retention = 2.2x views | Only found via vendor pages, not on a TikTok primary page I could open. | HYPOTHESIS |
| Vendor benchmarks: "50-60% of drop-offs happen in the first 3 s", "cliff = 30-50% lost by s3", "healthy swipe-away 10-30%, red flag over 40%", "APV 70%+ healthy, 80% unlocks reach", "15-30 s Shorts reach 80%+ retention" | [Opus](https://www.opus.pro/blog/ideal-youtube-shorts-length-format-retention), [Aibrify](https://aibrify.com/blog/youtube-shorts-retention-curve-playbook), [Humble&Brag](https://humbleandbrag.com/blog/youtube-shorts-benchmarks) | No dataset, method or sample is given in any of them. The 10-30% / 40% swipe figures are the same numbers as Galloway's 70-90% / 60% viewed bands, so they are **not independent confirmation**. | HYPOTHESIS |

**Use as a yardstick, not a law:** Viewed % 70%+ is the best-supported target (Galloway), under 60% is the best-supported alarm. Everything else is a vendor number.

### 3.2 Typical curve shapes and what each tells you

(Shape names are vendor vocabulary, [Aibrify](https://aibrify.com/blog/youtube-shorts-retention-curve-playbook); the interpretation follows YouTube's own description of dips and spikes.)

| Shape | What it looks like | What it means | Fix | Label |
|---|---|---|---|---|
| **Cliff** | Steep loss in the first 1-3 s, then slow decay | Packaging problem: first frame, first words or promise did not match what viewers expected. Usually shows with a low Viewed %. | Rewrite frame 0 and the first sentence; do not touch the rest. | SUPPORTED |
| **Slope** | Steady decline all the way | Relevance or density problem: the promise was fine but information per second is low | Cut a sentence, tighten, add a new fact every 3-4 s | HYPOTHESIS |
| **Step** | A sharp drop at one second | One specific shot or line lost people (a card, a long quote, a filler sentence, a loud SFX) | Scrub to that second in Studio and replace the shot | PROVEN (YouTube: dips = skipped) |
| **Plateau** | Flat after the initial drop | Those who stayed are satisfied; the Short earns replays | Protect it; shorten the dead tail | SUPPORTED |
| **Mid bump / spike** | A local rise | Rewatched or shared moment, or confusing line | Check which. If it is the payoff, move the payoff earlier or loop to it | PROVEN (YouTube: spikes = rewatch/share) |
| **Early-seconds elevation above plateau (loop)** | Values above 100% at 0-2 s | Replays | Keep the loop, but check it is not confusion | second-hand |
| **End cliff** | Last 1-3 s are lost | Viewers left before the last line (payoff already landed, or a dead tail) | Remove tail silence and the post-payoff sentence | HYPOTHESIS |

### 3.3 The first 1-3 seconds: what the swipe decision is based on

Based on foraging (2.1), OR (2.2), gaze (2.3), curiosity (2.4) and mute viewing (2.5), a viewer decides on three things, probably in this order:
1. **What is this about, and is it for me?** Gets decided by frame 0 plus any text visible before sound registers. (A person, a sport, a number.) [HYPOTHESIS]
2. **Is something happening / odd?** Motion and surprise capture gaze. [SUPPORTED]
3. **Is a question being raised that I can half-answer?** Curiosity at intermediate confidence. [SUPPORTED]

YouTube does not publish when the "stayed" threshold is crossed. Galloway: "make your first second really punchy ... treat your intro like a thumbnail." [SUPPORTED]. YouTube's own Shorts statement that "most thumbnails are never seen" ([TechCrunch](https://techcrunch.com/2023/08/25/youtube-demystifies-the-shorts-algorithm-views-and-answers-other-creator-questions/)) means frame 0 and the text overlay are the thumbnail. [PROVEN]

### 3.4 Mid-video drops and how to patch them

| Patch | Mechanism | Evidence | Label |
|---|---|---|---|
| Re-hook sentence at ~40-50% ("But here is the part nobody mentions") | New gap and OR; resets the foraging rate estimate | No Shorts data. Mechanism from 2.1/2.4. | HYPOTHESIS |
| Voice change (real quote burst of up to 4 s) | Voice changes did not habituate in six repetitions | Potter et al. | SUPPORTED mechanism |
| Escalating stakes (number 1 small, number 2 bigger, number 3 absurd) | Goal gradient plus surprise | Kivetz 2006; Itti and Baldi 2009 | HYPOTHESIS |
| Pattern interrupt (hard cut to a different kind of image, a card with the proof, a sound drop) | Unrelated cuts also elicit OR | Lang | SUPPORTED mechanism |
| Visible progress ("2 of 3", countdown) | Goal gradient, fast-to-slow progress reduces drop-off | Conrad 2010 (surveys) | HYPOTHESIS for video |
| Remove, don't patch: delete the sentence that causes the Step | Foraging (rate of gain) | Curve + common sense | SUPPORTED |

Re-hooks must be **honest**: a re-hook that promises something the Short does not deliver converts retention into dislikes and "not interested", and YouTube says it weights satisfaction ([vendor summary of Todd Beaupre's 2025 comments: Outlierkit](https://outlierkit.com/resources/youtube-viewer-satisfaction-algorithm-2026/); second-hand). [HYPOTHESIS on size of penalty]

### 3.5 Endings and loops

**What a loop does arithmetically** (my model, not YouTube's):
APV = first-pass completion c + (fraction of engaged viewers who replay, r) x (average fraction of the Short they re-watch, f).

| Short | c | to reach 100% APV you need r x f of | Example | Watch seconds per engaged viewer at 100% |
|---|---|---|---|---|
| 12 s one-second oddity | 0.90 | 0.10 | 10% of viewers replay once in full | 12 s |
| 20 s | 0.80 | 0.20 | 20% replay in full, or 40% replay half | 20 s |
| 26 s story | 0.72 | 0.28 | 28% replay in full | 26 s |
| 30 s story | 0.68 | 0.32 | 32% replay in full | 30 s |

(c values are illustrative assumptions in the vendor 65-80% range, not measurements.)

- **Why under about 20 s is the easy route to >100%:** the first pass is almost always completed (higher c), a 12 s clip is cheap to replay, and a loop restarts before the viewer decides to leave. **Cost:** less story, less new information per view; at 100% a 12 s Short yields 12 watch-seconds per engaged viewer, a 26 s story at 80% APV yields 21 s. If YouTube's Shorts ranking leans on watch time or satisfied watch time rather than APV alone (YouTube has not said), the longer, lower-APV Short can still win. Galloway's data show Shorts with AVD over 50 s averaged 4.1M views, although that is confounded because longer Shorts also have higher AVD. [HYPOTHESIS; both sides plausible]
- **CoachClank lens (computed, section 6):** the 16-20 s bucket is the **worst** bucket (median 265K) while 15 s or less (490K) and 21-25 s (1.03M) do better. One reading: very short Shorts win by looping/replays, 21+ s stories win by depth, and the 16-20 s middle gets neither. This is a story that fits the numbers, not a tested cause. [HYPOTHESIS]
- **Seamless loop (last frame to first frame, last word into first word):** vendor sources agree it raises replays but none publishes a controlled test ([VidIQ](https://vidiq.com/blog/post/double-youtube-watch-time-looping-shorts/), [Virvid](https://virvid.ai/blog/looping-structure-shorts-retention-2026), [Aibrify](https://aibrify.com/blog/youtube-shorts-retention-curve-playbook)). Mechanism: if the join is hidden, the viewer's decision point is bypassed (no "ending" event to trigger a swipe). [HYPOTHESIS]
- **Payoff-first-line design:** the first line states the claim, the last line is the explanation that makes the first line mean something new; replays then feel like "I get it now". [HYPOTHESIS]
- **Cliffhanger/question end:** drives comments (the SKILL's "two-sided argument") but also leaves the viewer unresolved at the moment peak-end says they form their judgement; and an unanswered question is an invitation to swipe to find the answer elsewhere. [HYPOTHESIS]
- **Loop-baiting vs satisfying ending, trade-off:** confusing endings produce "bad spikes" (replay out of confusion) and may raise dislikes; satisfying endings raise like/share but give no reason to replay. The only evidence is mechanistic. Hence it is **A/B test #3 in section 7.7**.

---

## 4. Practical editing techniques and what the evidence actually says

| # | Technique | Mechanism | Evidence | Label | Testable rule |
|---|---|---|---|---|---|
| 1 | **Cut rate** | OR from cuts; overload at very high pace | No study ties cut rate to Shorts retention. Lang: memory peaks at medium pacing. Hasson: tight editing synchronises. Vendor claims ("2.5 s clips = +35% completion", "under 1.2 s reads as noise") have no dataset ([Round 5 already flagged this](Round%205%20-%20Competitor%20Formulas%20(Oct%204,%202026).md)). | HYPOTHESIS | Test 1.4 s vs 2.2 s average shot on the same footage. Never hold >3 s; never place 3 cuts under the line carrying the number. |
| 2 | **Zoom / punch-in** | Adds motion/flicker (Carmi and Itti); keeps stills alive | Indirect only | HYPOTHESIS | Subtle push on every still or static shot; A/B 0 vs 0.06 on the same story. |
| 3 | **B-roll relevance** | Coherent order synchronises viewers; shuffled shots lower synchrony | Hasson 2008 | SUPPORTED | Every shot must show what the current sentence says; the person named is the person on screen. |
| 4 | **Hook headline text (0-2 s)** | Curiosity gap in text; works sound-off | Mechanism only; no hook-text experiment found | HYPOTHESIS | Two lines of 14 characters or fewer, containing one concrete fact. A/B. |
| 5 | **Sound design: SFX** | Sound effects raised attention and recall in radio ads; production effects habituate | Rodero 2019; Potter habituation | SUPPORTED (radio) | 2-5 varied SFX, each tied to an on-screen event; never the same SFX twice in a row. |
| 6 | **Sound design: voice-change re-hooks** | Voice changes do not habituate | Potter 2000 (as summarised) | SUPPORTED mechanism | 2-3 real-voice quote bursts of 4 s or less spaced through the Short. |
| 7 | **Music vs none, ducking** | No retention evidence found | none | HYPOTHESIS (ducking is mixing hygiene, not a retention lever) | Test none vs quiet bed; voice always -14 LUFS first. |
| 8 | **Voice pace** | Fast, enthusiastic delivery = engagement; comprehension knee near 275 wpm | Guo 2014; Foulke and Sticht | SUPPORTED | 230-270 wpm with real pitch variation; test 230 vs 270. |
| 9 | **Silence / pause** | Silence onset elicits OR (radio) | Potter, Lang, Bolls | HYPOTHESIS for Shorts | One 0.4-0.8 s beat immediately before the payoff. |
| 10 | **Caption chunking and timing** | Reading load; eyes on text vs picture | Brysbaert 238 wpm; Netflix 20 cps; Li 2026 | SUPPORTED | 2-4 words, 0.7-1.2 s on screen, max 20-22 cps, one line. |
| 11 | **Caption style (karaoke vs sentence-case, ALL CAPS)** | None for retention | none | HYPOTHESIS | A/B at constant timing. |
| 12 | **Progress / countdown device** | Goal gradient; fast-to-slow progress cuts drop-off | Kivetz 2006; Conrad 2010 (surveys) | HYPOTHESIS | Number structure ("3 rules"), show "1/3". |
| 13 | **"Wait for it"** | Suspense, uncertainty ramp at p=0.5 | Brewer and Lichtenstein; Fiorillo 2003 | HYPOTHESIS | Use only if the payoff is visibly worth it and arrives within the Short. |
| 14 | **Numbers/stakes escalation** | Curiosity gap size; goal gradient | Loewenstein; Kivetz | HYPOTHESIS | Order the facts small to enormous; last number is the biggest. |
| 15 | **Re-hook at fixed interval** | Foraging rate; OR | no direct evidence for *fixed* intervals | HYPOTHESIS | One re-hook at 40-50% runtime, not a metronome. |
| 16 | **End on the payoff** | Peak-end; curiosity is satiated by the answer | Fredrickson and Kahneman | SUPPORTED | Last word 0.15-0.4 s before the end; no CTA. |
| 17 | **Visual loop** (final frame matches first) | Hides the decision point | Vendor only | HYPOTHESIS | Pixel match (section 7.5). |
| 18 | **Audio loop** (last word grammatically flows into the first) | Same | Vendor only | HYPOTHESIS | Test one story with a deliberate wrap line. |
| 19 | **Face in frame 0** | Eye-contact effect | Contested replication | HYPOTHESIS | A/B face vs action. |
| 20 | **Motion in frame 0** | Motion/flicker causal for gaze | Carmi and Itti 2006 | SUPPORTED | Frame 0 already moving; never a still, logo or black. |

---

## 5. Case studies with real numbers

What exists publicly, and how much weight it can bear:

| Case | Numbers | Reliability |
|---|---|---|
| **Galloway, 33 channels / 5,400 Shorts (2023)** | Viewed-vs-swiped under 60% rarely did well, 70-90% best; AVD over 50 s averaged 4.1M views; likes/comments not strongly related to performance | Observational, pre-2025 counting. Best public dataset. [thread](https://threadreaderapp.com/thread/1646898356419981315.html) |
| **Short-form viewing lab study (2026)** | ~70% of sessions end before 20% of video | 50 viewers, crowdsourced. [arXiv](https://arxiv.org/html/2603.22663v1) |
| **Commercial short-video service (22B playbacks)** | >40% of videos under 25% playback | Large, not YouTube. [IEEE TMC](https://dl.acm.org/doi/10.1109/TMC.2021.3139893) |
| **TikTok / Neuro Insight (sponsored)** | creative story +16%, remix a trend +14%, real people +9% watch time | Sponsored by TikTok. [TikTok blog](https://ads.tiktok.com/business/en-US/blog/resonance-key-factor-ad-effectiveness) |
| **Instagram** | Defines skip rate as 3-s leavers; retention chart; Mosseri names watch time, sends per reach and likes per reach as top signals (via vendor summaries) | Definition official; ranking claim second-hand. [Social Media Today](https://www.socialmediatoday.com/news/instagram-adds-retention-insights-reels/758464/), [Dataslayer](https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers) |
| **MrBeast production memo (leaked, long-form)** | Retention graph "freak out" on minute 1, minutes 1-3 as next most important, "crazy progression" | Real mechanism (front-load and escalate), long-form. [Alexander Jarvis copy](https://www.alexanderjarvis.com/memo-how-to-succeed-in-mrbeast-production/) |
| **Creators reporting 100%+ APV** | "from 60% to 120% by looping" appears in sales material and blogs | No screenshot, channel or method I could verify. Treat as marketing. |

**What separates 100%+ APV Shorts from the rest, honestly.** I found no verifiable dataset. The consistent claims are: (1) short (usually under about 20 s), (2) the end is built to flow into the start (visual and audio), (3) something worth re-checking (a detail missed on first pass, a satisfying motion), (4) loop hidden by no end card, no CTA, no silence at the tail. All four are logically consistent with the APV arithmetic in 3.5, but **none is demonstrated**. For a 22-30 s story, reaching 100% needs about a quarter of engaged viewers to replay in full, which is a hard ask; a better target is a high first-pass completion (APV 80-95%) plus a 5-10% replay lift. [HYPOTHESIS]

---

## 6. Our own data (computed Oct 4, 2026)

Sources: `MetaSportsClips - all 80 Shorts.csv` (our channel), `Tools/data/channel_log.csv`, and a fresh yt-dlp pull of public metadata (id, duration, views, date) via the mobile web client (the default client is bot-blocked for per-video metadata). Pulled today: CoachClank last 149 Shorts, REBOUND 57, Courtside Films 59, Ahmed's Basketball 78. Hoop Facts returned 0 (handle did not resolve). Our own productions folders (9 finished Shorts) were read for speech and caption statistics only; nothing was edited.

### 6.1 Does duration relate to views?

| Channel | n | Median duration | Median views | Spearman rho (duration, views) | Note |
|---|---|---|---|---|---|
| CoachClank (2026) | 149 | 20 s | 477K | **+0.13** (p=0.10) | Age-adjusted +0.14 |
| REBOUND (2022-23) | 57 | 37 s | 822K | **+0.41** (p<0.001) | Confounded by 3-item list format (~58 s) and old counting; still +0.43 (p=0.004) among non-rule titles |
| Courtside Films | 59 | 77 s | 322K | +0.16 (p=0.23) | 54 of 59 are 41 s+; almost no short ones |
| Ahmed's Basketball | 78 | 69 s | 88K | 0.00 | All 60-79 s; no variation to test |
| **MetaSports (Dec 2025-Feb 2026)** | 60 | 22 s | 30.7K | **-0.17** (p=0.20) | Durations 10-33 s |
| **Pooled, z-scored within channel** | 403 | | | **+0.12** (p=0.018) | Length explains roughly 1-2% of variance |

CoachClank detail (computed, permutation test on medians):
- 20 s or less: n=84, median **300K**. 21 s or more: n=65, median **978K**; ratio 3.3x, p=0.002; bootstrap 95% interval for the ratio 1.2x to 5.8x. Round 5's "21+ s beats 20 s or less" is **reproduced on a fresh pull, but not independent** (the samples overlap) and it is a post-hoc split.
- Buckets: 15 s or less n=30 median 490K; 16-20 s n=54 median 265K (the worst); 21-25 s n=36 median 1.03M; 26-34 s n=24; 35 s+ n=5.
- Share of Shorts at or above 1M views: 27% (15 s or less), 24% (16-20), **53% (21-25)**, 38% (26-34).
- Top 10%: median 22 s; the rest 19 s. Top Shorts: 15 s, 22 s, 22 s, 28 s, 34 s, 20 s, 54 s, 25 s, 16 s, 22 s.

**Verdict:** length is not a reliable lever on its own. There may be a real "21-25 s story sweet spot" and a "dead zone at 16-20 s" for CoachClank; our channel (n=60) shows no length effect at all. [PROVEN pattern; causal claim HYPOTHESIS]

### 6.2 Our views are on a plateau

NBA-era (Dec 2025-Feb 2026) Shorts, n=60: percentiles of views: min 422, p10 17.9K, p25 27.7K, **median 30.7K**, p75 33.9K, p90 45.4K, max 80.7K. **46 of 60 sit between 20K and 45K.** Median by duration bucket: 32.8K (17 s or less), 30.9K (18-20), 30.8K (21-24), 30.3K (25-28), 29.7K (29-33). Medians by title style: starts with Why/How/Is/Does/What/Did 31.3K vs 30.6K otherwise; question mark 31.5K vs 30.6K; emoji 30.2K vs 32.5K.
Channel log (Sep 26, 2026): 469 subscribers, median last 7 = 30,000, before = 30,500, trend FLAT, last upload 215 days earlier (so the 60 NBA-era Shorts are 7-10 months old and the numbers are final).

Reading: the distribution is very tight (max/median 2.6x; CoachClank about 65x). That is the signature of a **fixed-size test audience that no Short has escaped**. If that is right: (a) topic, title and length tweaks are not the current bottleneck, (b) a Short must clear the stay-or-swipe and retention gates to be served beyond the batch, (c) our A/B tests should be read on **Viewed %** and **APV**, not on views. [PROVEN pattern, cause HYPOTHESIS. Check with Studio "Shown in feed": if it is also about the same for every Short, the gate theory is confirmed.]

### 6.3 What we already ship (production stats, 9 finished Shorts)

| Metric | Our range | Reference |
|---|---|---|
| Speech rate | 221-259 wpm (mean about 240, n=9) | Reading 238; listening knee about 275 |
| Characters per second of speech (with spaces) | 20.8-23.7 | Netflix adult subtitle limit 20 |
| Shots per Short | 7 (#02) to 20 | avg shot interval 1.25-1.75 s (3.88 s for #02) |
| Shots in first 3 s | 1 (#02) to 4 | gate wants 3+ |
| Longest pause inside the voice | 0.07-1.04 s (mostly under 0.3) | gate: 0.6 s |
| Captions | median 0.6-1.0 s on screen, 2.4-3.8 words, peaks 28-36 cps | Netflix 20 cps |

### 6.4 Limits of this section

- yt-dlp gives views, not retention. All "what works" statements are about views, which now include replays and instant swipes (Mar 2025 rule).
- Competitor topic mix differs; duration is confounded with format (listicle, size gap, prank).
- Several splits were tested. The 21 s split was suggested by Round 5, the 15/16 s split was found by looking; treat the p-values as descriptive.

---

## 7. What this means for OUR format

### 7.1 Beat sheet for a 22-30 s story (about 100-110 words at 240-260 wpm)

| Time | Job | Words (approx.) | What must be on screen | Sound | Label |
|---|---|---|---|---|---|
| **0.0-1.0 s** | Stop the swipe: state the claim or number. First spoken word is the number/name/stake (voice starts at 0.0-0.2 s). | 3-4 | **Real moving footage of the named moment** or a close face with direct gaze; 2-line headline (14 characters or fewer each) containing one concrete fact; no logo, black, still or card. | Voice only; no boom. | SUPPORTED (motion), HYPOTHESIS (headline, face) |
| **1.0-3.0 s** | Finish the hook sentence; create a gap with a priming dose (the odd fact) and a **two-outcome question** the viewer can half-answer. | 6-8 | A different image at about 1.0-1.5 s that is matched in motion/gaze to the first; at least 3 distinct shots by 3.0 s (existing gate). | Optional single SFX on the first new image. | SUPPORTED mechanism |
| **3.0-8.0 s** | Context in two sentences maximum, but **deliver one small micro-payoff** (a clip or number that proves the claim is real) so staying is rewarded. | 16-20 | Footage of the person/event; evidence card only if visually rich, 2 s or less. | Voice. | HYPOTHESIS |
| **8-18 s (mid)** | Escalate: 2-3 beats, each a new fact and a new image, ordered small to enormous. **Re-hook at about 40-50% of runtime** (a turn: But / Until / Now) by voice and, if you want, a 1-line text. Insert 1-2 real quote bursts (4 s or less, voice change). Numbers sit on shots of 1.5-2.5 s. | 40-45 | No shot over 3 s; no information-free stretch over about 3-4 s. | Quote audio; 1-2 varied SFX tied to events. | SUPPORTED / HYPOTHESIS |
| **18 s to last 5 s** | Land the turn/twist (surprise) and set up the payoff. | 15-20 | Closest, most vivid shot of the story; progress cue if the Short is numbered. | Optional 0.4-0.8 s beat of silence just before the payoff. | HYPOTHESIS |
| **Final 5 s** | **Peak, then stop.** One sentence payoff that makes the first line mean something new (payoff-first-line loop) *or* a two-sided question (comment bait); never a CTA, never a recap. Last word ends 0.15-0.4 s before the end. | 10-14 | Last frame **matches frame 0** (same subject, composition, motion direction); no end card; no fade. | Last word flows into first word if you use the audio loop. | SUPPORTED (end on payoff); HYPOTHESIS (loop design, ending type) |

### 7.2 Editing rules (each with a label)

1. Frame 0 is moving real action or a face; never a still, logo or black. [SUPPORTED]
2. New information at least every 3-4 s; delete rather than patch a sagging sentence. [HYPOTHESIS, foraging]
3. Every shot illustrates the line being spoken; the named person is on screen. [SUPPORTED, Hasson]
4. Cut on motion or gaze; match direction across cuts. [SUPPORTED, Smith]
5. Hold the shot that carries a number or name 1.5-2.5 s; cut fast on connective lines. [HYPOTHESIS, Lang pacing]
6. Use quote bursts as voice-change re-hooks; keep SFX to 2-5, varied, event-tied. [SUPPORTED mechanism]
7. One short caption line, 2-4 words, 0.7-1.2 s, max about 22 characters per second, centred 45-62% height; the voice at 230-270 wpm. [SUPPORTED]
8. Headline text answers "why should I care" with one concrete fact, never a vague teaser. [HYPOTHESIS]
9. Re-hook once at 40-50% and only if a real payoff follows. [HYPOTHESIS]
10. Number structure with front-loaded progress when the topic allows ("3 rules"). [HYPOTHESIS]
11. End on the payoff; no CTA; last word 0.15-0.4 s before end. [SUPPORTED]
12. Do not stack all devices: pick one hook type (curiosity-first) and one mid device per Short. [HYPOTHESIS]

### 7.3 Loop design for our stories (22-30 s)

Priority order, because a 25 s story cannot realistically reach 100% APV and should not be sacrificed for it:
1. **Seamless visual match:** final shot = the same clip/subject as shot 1 *and* a matching composition; keep the last 0.15-0.4 s a held frame of the payoff face/action. [HYPOTHESIS]
2. **Payoff-first-line:** write the Short so line 1 reads as a claim, and the last line recasts it ("...and that is why he took the pay cut"). [HYPOTHESIS]
3. **Audio wrap:** keep the voice's last word's energy up and avoid a trailing breath so the join to word 1 is not a silence. Optional. [HYPOTHESIS]
4. **Do not loop by confusion:** a Short that only replays because the viewer missed the point shows a bad spike and risks dislikes. [HYPOTHESIS]
5. Keep the ending type (payoff vs question) as a **separate A/B variable** from the loop (section 7.7).

### 7.4 What to measure (every Short, 48 h and 7 d)

Studio fields: Shown in feed; Viewed % (stayed to watch); engaged views; views; AVD; APV; retention curve values at 1 s, 3 s, 5 s, 10 s, 50%, 75%, last second and the early-second bump; likes, comments, shares, subscribers per 1,000 views. Plus, for our log: story ID, test variable and arm, length, wpm, shots, cut times, hook words.
Rules for reading:
- Viewed % decides the hook (70%+ target, under 60% = rewrite the first 2 s). [SUPPORTED]
- APV and the curve decide the story. Compare **against our own Shorts of similar length**, not against vendor numbers. [PROVEN, that is what Studio does]
- Watch for the Step: scrub to the second where the curve drops more than 5 points in one second.
- Use Engaged views for performance comparisons across the Mar-2025/Aug-2026 boundaries.

### 7.5 What `Tools/qa_short.py` could check automatically (spec, not built)

Already present: hook word timing, filler first word, 3+ shots and action in first 3 s, shot length, clip repeats, kind mix, loudness, CTA in last 6 words, wpm range, tail 0.15-0.6 s, turn word in first 40%.
Add (all cheap with ffmpeg and words.json):

| # | Check | How | Replaces / adds | Label |
|---|---|---|---|---|
| 1 | **Frame-0 quality**: not near-black/white, not a flat-colour title card, contains motion in the first 1 s | luminance of frame 0, mean absolute difference between frames 0-24 | New | SUPPORTED motion |
| 2 | **Visual change per second** over first 3 s and "dead zones" (no scene-score above 0.3 or pixel difference for more than 3.5 s) | `select='gt(scene,0.3)'` | Adds the foraging rule | HYPOTHESIS (threshold) |
| 3 | **Loop match**: last frame vs first frame (SSIM or histogram distance) and last 0.3 s vs first 0.3 s loudness | `ssim` filter, ebur128 windows | Replaces the "last clip name = first clip name" gate, which cannot tell if it loops | HYPOTHESIS |
| 4 | **Info-dead window**: no new shot, caption chunk or number for over 3.5 s | shots.json + captions | New | HYPOTHESIS |
| 5 | **Windowed speech rate**: wpm per 5 s; flag windows over 280 or under 190; flag any 2 s window with 12+ words | words.json | Replaces a single average wpm | SUPPORTED |
| 6 | **Caption load**: chunk 2-4 words, displayed 0.7-1.2 s, cps at most 22 (warn above 20, fail above 30), one line | captions.srt | New | SUPPORTED |
| 7 | **Number-on-held-shot**: every spoken digit/name token falls inside a shot at least 1.2 s long | words.json + shots.json | New | HYPOTHESIS |
| 8 | **SFX repetition**: same SFX file used more than twice, or two SFX within 1.5 s | sfx.json | New | SUPPORTED (habituation) |
| 9 | **Quote bursts**: 1-3 spliced voice bursts of 4 s or less | shots kind quote | New | SUPPORTED mechanism |
| 10 | **Hook content**: first 6 words must contain a digit, currency, or a capitalised name that is not sentence-initial; tighten the current regex (it matches any "Capitalised Capitalised" pair, so nearly every hook passes) | words.json | Fixes a weak gate | PROVEN (code reading) |
| 11 | **Payoff position**: the sentence tagged `payoff:` in notes.md starts at or after 70% of runtime | notes.md + words.json | New | SUPPORTED (peak-end) |
| 12 | **Ending silence**: silence in the last 1 s except the tail | ebur128/silencedetect | Extends the tail check | HYPOTHESIS |
| 13 | **Length gate unified** (one range in code and SKILL) | constants | Fixes inconsistencies in 7.8 | PROVEN |
| 14 | **Whitelist question-first hooks**: remove "did" and "you" from the filler list or allow "Did/Is/Why + proper noun" | FILLER set | The current gate blocks the question-first A/B arm | PROVEN (code reading) |

### 7.6 Data we need from the user (the cheapest big win)

Export from Studio (Analytics, Content, Shorts, Advanced Mode, last 90 days, by video): Views, Engaged views, Viewed %, AVD, APV, Shown in feed, Likes, Comments, Subscribers; and the retention curves of the five best and five worst Shorts (screenshots are fine). With 80 Shorts this tests in an hour: is Viewed % flat too (gate theory), does APV correlate with views, does duration matter on *our* audience, which Shorts had loops and bumps. It replaces most guesses in this note.

### 7.7 Ranked A/B tests (one variable each, metric named)

Design: **matched pairs** on comparable stories (same lane), randomise which arm goes first, post on the same weekday/time slot, read at 48-72 h. Sampling noise on Viewed % at about 30K views is under 0.5 percentage points, so noise comes from story-to-story variance (assumed SD of paired differences about 7 points until we have our data). With that assumption the smallest detectable difference (80% power, alpha 0.05) is about **6.9 points with 8 pairs, 4.9 with 16, 3.6 with 30**. Do not run two variables at once. Do not post the same story twice (inauthentic-content/duplication risk): vary stories.

| Rank | Test (A vs B) | Primary metric | Secondary | Why this rank (evidence x cost x size) | Evidence label |
|---|---|---|---|---|---|
| 1 | **Frame 0 + first words:** moving action + number-first claim vs face close-up + same claim | Viewed % | retention at 3 s | Cliff is the most fixable shape; hook is the gate; free to test | SUPPORTED mechanism |
| 2 | **Hook sentence form:** number/stakes-first vs question-first (needs qa filler fix, 7.5 #14) | Viewed % | retention at 5 s | Already queued; high impact | HYPOTHESIS |
| 3 | **Ending type:** end on payoff with matching loop vs end on two-sided question (both same loop match) | APV and replay bump | comments/1K views, likes/1K, Viewed % of the *next* Short | The SKILL currently contains both; decides loop strategy | HYPOTHESIS |
| 4 | **Hook headline text:** 2-line headline over 0-2 s vs none | Viewed % | retention at 3 s | Already queued; sound-off benefit | HYPOTHESIS |
| 5 | **Mid re-hook:** turn plus 1-line text at 45% vs plain narration | retention change between 40% and 60% | APV | Patches the Slope/Step | HYPOTHESIS |
| 6 | **Cut rate:** average shot 1.4 s vs 2.2 s on the same footage pool | Retention at 10 s and APV | Viewed % | Removes our unsupported 1.9 s gate if neutral | HYPOTHESIS |
| 7 | **Speech pace:** about 230 vs about 270 wpm, captions same chunking | APV | Viewed % | Speech is above reading speed; tests the 275 knee | SUPPORTED mechanism |
| 8 | **Caption style:** karaoke word highlight vs sentence-case 3-word chunks (one line) | APV | Viewed % | Already queued | HYPOTHESIS |
| 9 | **Length:** 22-24 s vs 28-30 s same lane | APV and AVD (seconds) | views | Pooled length effect is weak; tests whether AVD seconds matter | HYPOTHESIS |
| 10 | **Silence beat before payoff:** 0.6 s vs none | retention at the payoff second | likes/1K | Cheap | HYPOTHESIS |
| 11 | **SFX:** 3 varied SFX vs none | APV | Viewed % | Habituation says less is more | SUPPORTED (radio) |
| 12 | **Music:** quiet bed vs none | APV | Content ID risk | Already queued, low evidence | HYPOTHESIS |

### 7.8 Rules in `.claude/skills/cloud-short/SKILL.md` that are contradicted or unsupported

| # | Rule in SKILL | Problem | Recommendation | Label |
|---|---|---|---|---|
| 1 | "Ends on a question" (Quality formula 6) vs "End on a two-sided argument" (section 2) vs "end on the payoff ... last line echoes the first" (Round 5 block) | Three different ending rules in one file; no evidence for any; peak-end favours the payoff | Pick **payoff + loop match** as default; make question-ending test #3 | PROVEN (inconsistency) |
| 2 | "A sound on the hook word: one `boom` (gain -12) at 0.0" (section 2, first 3 s) | Contradicts Round 4/5 and the Lessons log (boom removed); no evidence; production effects habituate | Delete the line; allow one SFX on the first new image only | PROVEN (inconsistency) |
| 3 | Average shot 1.4-1.9 s (recipe), 1.9 in the Round 5 block, `qa_short` hard-fails above 2.6 s, its docstring says 1.9 | Four thresholds; no evidence that faster is better (Round 5 admitted this); Lang predicts an inverted-U for memory | One number, as a warn, until test #6 reports | PROVEN (inconsistency) / HYPOTHESIS |
| 4 | "A new image about every second until 5 s" | No evidence; at that rate every cut is an OR, which may overload on arousing content | Change to "at least 3 distinct shots by 3 s, then a new shot or fact at least every 3 s" | HYPOTHESIS |
| 5 | Heading "aim 70%+ at 3 s" | Studio's Viewed % is "past the initial seconds" (threshold unpublished), not 3 s retention (that is Instagram's definition); 70-90% comes from one 2023 study | Say "Viewed % 70%+ (Galloway 2023 yardstick)" | PROVEN (definition) |
| 6 | "Last shot reuses the first clip (loop)" as a **hard gate** | The check compares clip names, not pixels; no evidence that loops raise APV for 22-30 s stories | Make it a warn that tests pixel and audio match (7.5 #3) | HYPOTHESIS |
| 7 | Length: SKILL "22-34 s, 95-125 words", `qa_short` fail outside 21-40, docstring 18-35, Round 5 "21+ s" | Four ranges; the 21+ finding is real on CoachClank but confounded; our own data show no length effect | Single range 21-32 s; test #9 | PROVEN (inconsistency) |
| 8 | "No silence over 0.6 s" hard gate | Blocks a deliberate pre-payoff beat that has a mechanism (silence elicits OR) | Warn only; allow one beat of 0.4-0.8 s before the payoff | HYPOTHESIS |
| 9 | "Speech 240-290 wpm [SUPPORTED]" | Upper end exceeds the listening knee (~275 wpm) and reading speed (238); our captions already exceed Netflix's 20 cps | 230-270 wpm; downgrade the label to HYPOTHESIS until test #7 | SUPPORTED against |
| 10 | Captions "none on screen over 1.7 s; 3-4 words" | Fine, but our measured caption speed peaks at 28-36 cps | Add the cps rule (22 max, 30 fail) | PROVEN (measured) |
| 11 | "Turn word in first 40%" and "re-hook around 45%" | Consistent with mechanism, no direct evidence | Keep, label HYPOTHESIS, test #5 | HYPOTHESIS |
| 12 | `qa_short` FILLER includes "did" and "you" | Blocks every question-first hook ("Did Jalen Duren..."), which is the B arm of test #2 | Allow "Did/Is/Why/How + name" | PROVEN (code reading) |
| 13 | Hook-content regex accepts any "Capitalised Capitalised" pair | Nearly every hook passes; gate has no power | Tighten (7.5 #10) | PROVEN (code reading) |
| 14 | "Real quotes in short bursts (4 s or less)" | **Supported**: voice changes did not habituate. Keep and encourage 2-3 per Short | Keep | SUPPORTED |
| 15 | "Frame 1 is already moving or already a face" | Supported for motion; face unproven | Keep; A/B face vs action (test #1) | SUPPORTED / HYPOTHESIS |
| 16 | "Post time 6-11 AM ET" | YouTube says timing matters little for Shorts (except news) | Already labelled HYPOTHESIS in Round 5; keep as habit only | PROVEN (YouTube statement, 2023) |

### 7.9 The five checklist changes I would make now

1. **Hook:** frame 0 is real motion and the first spoken word is a number/name/stake with a two-line headline carrying one concrete fact; nothing else is required in the first 3 s.
2. **Information flow:** no stretch over 3-4 s without a new fact or image; hold number-carrying shots 1.5-2.5 s; use 2-3 real quote bursts as the re-hooks; SFX 2-5, varied.
3. **Voice and captions:** 230-270 wpm with pitch variation; captions one line, 2-4 words, at most about 22 characters per second.
4. **Ending:** end on the payoff with a matching last frame and a 0.15-0.4 s tail; no CTA; treat the question ending as an A/B arm, not a default.
5. **Measurement and gates:** log Viewed %, APV, AVD and curve points for every Short; convert the loop gate to a pixel/audio check and fix the filler and length-range inconsistencies.

---

## 8. Sources (grouped)

**YouTube / Instagram / TikTok official or near-official**
- Content tab analytics tips (Shorts): https://support.google.com/youtube/answer/12942217?hl=en-GB&co=YOUTUBE._YTVideoType%3Dshorts
- Understand your YouTube content performance (Studio app help; contains the Aug 24, 2026 views change and "How viewers engaged"): https://support.google.com/youtubecreatorstudio/answer/12220281?hl=en-GB&co=GENIE.Platform%3DAndroid
- Understand your YouTube engagement (AVD definition): https://support.google.com/youtube/answer/9313698?hl=en
- Measure key moments for audience retention: https://support.google.com/youtube/answer/9314415
- YouTube Help Community thread "A change to how we count views on Shorts" (JavaScript-rendered, not readable here; cited via PPC Land): https://support.google.com/youtube/thread/333869549/a-change-to-how-we-count-views-on-shorts?hl=en
- PPC Land on the Mar 31, 2025 change: https://ppc.land/youtube-changes-how-shorts-views-are-counted-from-march-31/
- LiveReacting on the Aug 24, 2026 change (quotes YouTube): https://blog.livereacting.com/youtubes-new-view-count-rule-what-changes-august-24/
- TechCrunch, YouTube Shorts Q&A (Aug 2023): https://techcrunch.com/2023/08/25/youtube-demystifies-the-shorts-algorithm-views-and-answers-other-creator-questions/
- Instagram skip rate and retention (Social Media Today): https://www.socialmediatoday.com/news/instagram-adds-retention-insights-reels/758464/
- TikTok for Business, Marketing Science / Neuro Insight: https://ads.tiktok.com/business/en-US/blog/resonance-key-factor-ad-effectiveness
- Netflix English Timed Text Style Guide: https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-Timed-Text-Style-Guide

**Peer-reviewed / academic**
- Lang's LC4MP overview: https://en.wikipedia.org/wiki/LC4MP ; Fisher et al. 2018: https://academic.oup.com/anncom/article/42/4/270/7905951
- Lang, Bolls, Potter, Kawahara 1999 (pacing): https://www.scirp.org/reference/referencespapers?referenceid=1646487
- Potter, Lang, Bolls audio structural features: https://www.semanticscholar.org/paper/Identifying-Structural-Features-of-Audio-Orienting-Potter-Lang/4caf5aae24fa5a42fea60f99e7337e517c517078 ; habituation: https://www.researchgate.net/publication/276929868_I've_Heard_That_Before_Habituation_of_the_Orienting_Response_Follows_Repeated_Presentation_of_Auditory_Structural_Features_in_Radio
- Rodero 2019: https://journals.sagepub.com/doi/abs/10.1177/0093650215609085
- Carmi and Itti 2006: https://ilab.usc.edu/publications/R.Carmi.html ; Itti and Baldi 2009: https://pubmed.ncbi.nlm.nih.gov/18834898/?dopt=Abstract
- Smith, Attentional Theory of Cinematic Continuity: https://ualresearchonline.arts.ac.uk/id/eprint/21187/2/6679.pdf
- Hasson et al. 2008: https://www.motionpictures.org/wp-content/uploads/2013/01/Hasson-etal_NeuroCinematics2008.pdf
- Cutting et al. on shot structure and pace: https://journals.sagepub.com/doi/10.1177/0956797610361679 ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5256470/
- Senju and Johnson 2009: https://www.researchgate.net/publication/24011071_The_eye_contact_effect_Mechanisms_and_development ; Hershler and Hochstein 2005: https://www.semanticscholar.org/paper/At-first-sight:-A-high-level-pop-out-effect-for-Hershler-Hochstein/34b78445102a969d236497138dca28d32efcf07c ; failure to replicate: https://link.springer.com/article/10.1007/s00426-025-02211-3
- Loewenstein 1994 (via summaries): https://www.researchgate.net/figure/Figure-1-Lowensteins-1994-theory-of-information-gap_fig1_364061951 ; Kang et al. 2009: https://pubmed.ncbi.nlm.nih.gov/19619181/ ; https://www.nature.com/articles/s41539-019-0056-y
- Ghibellini and Meier 2025 (Zeigarnik meta-analysis): https://www.semanticscholar.org/paper/Interruption,-recall-and-resumption:-a-of-the-and-Ghibellini-Meier/c98a41f13fd6f3b0b86047ecf92eeb03ac458626
- Schultz dopamine prediction error: https://www.pnas.org/doi/10.1073/pnas.1014269108 ; Fiorillo, Tobler, Schultz 2003: https://www.semanticscholar.org/paper/Discrete-Coding-of-Reward-Probability-and-by-Fiorillo-Tobler/91bf62ef88c5f1308b060ae684923c8bf4db004a
- Brewer and Lichtenstein 1982: https://journals.scholarsportal.info/details/0304422x/v27i0004/277_scashdacpoas.xml ; https://www.sciencedirect.com/science/article/pii/S0304422X22000262
- Green and Brock 2000: https://researchconnect.buffalo.edu/en/publications/the-role-of-transportation-in-the-persuasiveness-of-public-narrat/
- Fredrickson and Kahneman 1993 / peak-end: https://link.springer.com/content/pdf/10.3758/PBR.15.1.96.pdf
- Kivetz, Urminsky, Zheng 2006: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2733214 ; Villar et al. 2013 progress indicators: https://openaccess.city.ac.uk/id/eprint/14427/4/Social%20Science%20Computer%20Review-2013-Villar-744-62.pdf
- Berger and Milkman 2012: https://www.researchgate.net/publication/228137203_What_Makes_Online_Content_Viral
- Pirolli and Card / foraging: https://www.uxtigers.com/post/information-foraging ; https://www.nature.com/articles/s41598-017-11763-3
- Brysbaert 2019: https://gwern.net/doc/psychology/linguistics/2019-brysbaert.pdf
- Foulke and Sticht via review: https://www.academypublication.com/issues/past/jltr/vol01/05/23.pdf
- Guo, Kim, Rubin 2014: https://pg.ucsd.edu/publications/edX-MOOC-video-production-and-engagement_LAS-2014.txt
- Mayer redundancy: https://www.devlinpeck.com/content/mayers-principles-of-multimedia-learning ; https://www.tandfonline.com/doi/full/10.1080/01443410.2026.2678483
- Li 2026 vertical-video subtitles: https://onlinelibrary.wiley.com/doi/10.1002/acp.70262?af=R
- Verizon Media / Publicis (sound-off, captions): https://www.forbes.com/sites/tjmccue/2019/07/31/verizon-media-says-69-percent-of-consumers-watching-video-with-sound-off/ ; https://rbr.com/video-captions-study/
- Zhan et al. KDD 2022 (duration bias): https://arxiv.org/abs/2206.06003 ; Wu, Rizoiu, Xie 2018: https://arxiv.org/abs/1709.02541 ; Park, Naaman, Berger 2016: https://arxiv.org/abs/1603.08308
- Short-video viewing studies: https://arxiv.org/html/2603.22663v1 ; https://dl.acm.org/doi/10.1109/TMC.2021.3139893 ; https://dl.acm.org/doi/abs/10.1145/3625468.3652175

**Data and practitioner (second-hand, labelled in text)**
- Galloway 3.3B-views study thread: https://threadreaderapp.com/thread/1646898356419981315.html
- Shortimize: https://www.shortimize.com/blog/youtube-shorts-retention-rate ; Aibrify: https://aibrify.com/blog/youtube-shorts-retention-curve-playbook ; Humble&Brag: https://humbleandbrag.com/blog/youtube-shorts-benchmarks ; Opus: https://www.opus.pro/blog/ideal-youtube-shorts-length-format-retention ; Creator Essentials glossary: https://www.creatoressentials.com/glossary/shorts-engaged-views/ ; VidIQ loops: https://vidiq.com/blog/post/double-youtube-watch-time-looping-shorts/ ; Virvid: https://virvid.ai/blog/looping-structure-shorts-retention-2026 ; Outlierkit: https://outlierkit.com/resources/youtube-viewer-satisfaction-algorithm-2026/ ; Dataslayer: https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers ; Descript on 3-min Shorts: https://www.descript.com/blog/article/how-long-can-youtube-shorts-be
- MrBeast memo copy: https://www.alexanderjarvis.com/memo-how-to-succeed-in-mrbeast-production/

**Our data:** `Research Notes/MetaSportsClips - all 80 Shorts.csv`, `Tools/data/channel_log.csv`, `Productions/MetaSports/*/words.json`, `shots.json`, `captions.srt` (read only), yt-dlp public metadata for @CoachClank, @rebound, @CourtsideFilms, @AhmedsBasketball pulled Oct 4, 2026.
