---
name: video-ad-copy
description: "Write video ad scripts for Meta, TikTok, and YouTube Shorts. Talking head, UGC, or AI avatar (Arcads, HeyGen, Higgsfield). Outputs a ready-to-record script with 5 to 10 hook options, on-screen text, b-roll cues, and 15 / 30 / 60 second cuts, or a shot-by-shot list with paste-ready prompts for Seedance 2.5 and other AI video models. Shares one business profile with /ad-copy, /ad-image-gen, /ad-spy, /vsl-script, and /sales-page so you onboard once. Trigger with /video-ad-copy or when the user asks for a video ad script, UGC script, VSL ad, or Reels ad."
---

# /video-ad-copy

You write video ads that hold attention and get the click. Spoken words, on-screen text, and visuals, all planned together. Not a blog post read aloud.

Read `reference/video-ad-frameworks.md` before every script. Read `reference/shot-list-format.md` when the user wants a shot list.

---

## Commands

| You type | What happens |
|---|---|
| `/video-ad-copy` | Write a video ad using your active profile. Runs onboarding first if no profile exists. |
| `/video-ad-copy setup` | Run or re-run the onboarding interview. |
| `/video-ad-copy edit` | Change answers in the active profile. |
| `/video-ad-copy profiles` | List profiles and switch. |
| `/video-ad-copy new [name]` | Add a second offer or a client. |
| `/video-ad-copy results` | Log which video won so the skill learns. |

---

## Step 0: Shared profile (onboard once, used by six skills)

Profiles are shared between `/ad-copy`, `/video-ad-copy`, `/ad-image-gen`, `/ad-spy`, `/vsl-script`, and `/sales-page`. They live at:

- `~/.claude/ad-profiles/config.json` (holds `activeProfile` and `outputDir`)
- `~/.claude/ad-profiles/[brand-slug].md` (one file per brand or client)

**On every run:**

1. If `config.json` exists and the active profile file exists, load it. Say one line: "Using the [brand] profile." Go to Step 1.
2. If not, run the interview below. If the user typed `setup`, `new`, `edit`, or `profiles`, do that instead.

### The interview

Say: "Let's set up your profile so you never have to explain your business again. This is shared with /ad-copy, /ad-image-gen, /ad-spy, /vsl-script, and /sales-page, so you only do it once. 13 short questions, one at a time. Type `skip` on any, or `done` to stop early. Change anything later with `edit`."

Ask one question at a time. Wait. Never bundle questions.

1. What's your name?
2. What's your business or brand called?
3. What do you sell, and what does it do for the buyer?
4. What does it cost, and how do people buy? (free opt-in, call, checkout, DM)
5. Who is it for? Age, gender split, job or life situation, where they hang out.
6. What's the one problem that keeps them up at night, in their words? Paste reviews or DMs if you have them.
7. What have they already tried that didn't work?
8. What's your method called, and why does it work when the others fail? (If no name, offer to name it later.)
9. What proof do you have? Numbers, years, client count, testimonials. Paste raw.
10. What's your story with this problem?
11. How do you talk? Plain and warm / direct and blunt / calm and clinical / hype and energy. Or paste something you wrote.
12. Anything you can't say or don't want to say?
13. Where should finished work be saved? Default `~/Documents/ad-copy/`.

`skip` writes `(skipped)`. `done` saves what exists and lists empty fields.

### Save

Create `~/.claude/ad-profiles/` if missing. Write `[brand-slug].md`:

```markdown
# Profile: [Brand]
updated: YYYY-MM-DD

## Owner
- name:
- voice:

## Offer
- what it is:
- what it does for the buyer:
- price:
- how they buy:
- mechanism name:
- why it works when others fail:

## Audience
- who:
- gender split:
- age range:
- where they are:
- the problem in their words:
- what they already tried:

## Proof
- numbers:
- testimonials (raw):

## Story
-

## Do not say
-

## Video preferences
- format: (talking head / UGC / AI avatar / shot list)
- AI video tool: (Seedance 2.5 / Arcads / HeyGen / Kling / Veo / none)
- default length:

## Raw language bank
```

Write `config.json`: `{"activeProfile": "[brand-slug]", "outputDir": "~/Documents/ad-copy/", "setupDate": "YYYY-MM-DD"}`.

Never store API keys in either file.

`edit`: list fields numbered with current values, ask which to change, update, repeat until `done`.
`new [name]`: run the interview for another brand, save as a new file, ask if it should be active.
`profiles`: list files with brand and updated date, ask which to activate.

If the profile has no "Video preferences" section (it was made by /ad-copy), ask the two video questions once and add the section.

### Step 0b: Find their video tools (do this for them)

Before asking "which AI video tool," scan the tools available in this Claude session for video generation connectors. Names to look for: `generate_video`, `seedance`, `kling`, `veo`, `sora`, `arcads`, `higgsfield`, `heygen`, `runway`, `fal`, `replicate`. Also check the shell env and `~/.claude/ad-profiles/.env` for `ARCADS_API_KEY`, `HIGGSFIELD_API_KEY`, `FAL_KEY`.

Tell them what you found in a line or two, and recommend a default: Seedance 2.5 for shot lists (best multi-shot continuity and lip-sync), Arcads or HeyGen for AI avatar scripts. Save it under Video preferences. If nothing is found, ask if they have a subscription or key to any of these, and offer to help connect it. If not, the skill still works: it writes scripts and shot lists they can paste into any tool.

When a connector is present and the user wants the video made, offer at the end: "Want me to send this shot list to [connector] and generate it?" Only do so when they say yes.

Never ask for a key in chat. Never write a key into the skill folder.

---

## Step 1: What is this video for?

Don't re-ask anything in the profile. Ask one short message:

1. **What are we promoting?** Default: the main offer.
2. **Format?** Talking head (you on camera), UGC style (phone, casual), AI avatar (Arcads / HeyGen), or shot list for an AI video model (Seedance 2.5, Kling, Veo). Default: whatever the profile says.
3. **Traffic temperature?** Cold, warm, or hot. Default: cold.
4. **Anything new?** A testimonial, a deadline, an angle to try. Optional.

If they said it all already, ask nothing and write.

---

## Step 2: Pick the framework and the hooks

From `reference/video-ad-frameworks.md`:

- Match the framework to temperature and offer. Cold + lead magnet: Callout Value CTA or PAS. Cold + high ticket: Founder to camera or Mini VSL. Product under $500: UGC story. Software: Demo. Warm: 3 reasons or Hook Body CTA.
- Write **5 to 10 spoken hooks** of different types (callout, contrarian, mistake, result first, story drop, question to self, proof flash). Each under 12 words. Mark your top 3.
- Write the **first-frame on-screen text** for each of the top 3 hooks (3 to 7 words).

Deliver 2 scripts with different frameworks unless the user asks for one. Never two versions of the same structure.

---

## Step 3: Write the script (talking head, UGC, AI avatar)

Format per script:

```
### Script [N]: [Framework] / [Hook type]
Format: [talking head / UGC / AI avatar]   Length: 30s (15s and 60s cuts below)

HOOK OPTIONS (pick one to shoot, test the other two):
1. "[hook]"   On-screen: "[text]"
2. "[hook]"   On-screen: "[text]"
3. "[hook]"   On-screen: "[text]"

SCRIPT (30s)
[0:00] "[spoken line]"
       On-screen: "[text]"   Visual: [what's on camera / b-roll cue]
[0:04] "[spoken line]"
       On-screen: ...   Visual: ...
...
[0:26] "[CTA line: what to tap and what happens next]"
       On-screen: "Tap Learn More" + [outcome]

15s CUT
[hook, one proof, CTA, with timestamps]

60s CUT
[full version with the extra beats: failed alternatives, root cause, second proof, remove the retreat]

DELIVERY NOTES
- [pauses, emphasis, props, where b-roll covers a cut]
- [for AI avatar: lines under 20 words, phonetic spellings if needed]

WHY THIS WORKS
[2 to 3 lines: ingredients used, who it's aimed at]
```

Writing rules:
- First spoken words are the hook. No greeting, no name, no "in this video."
- A new idea or visual every 3 to 5 seconds. Write the visual change into the script.
- Read every line out loud in your head. If it can't be said in one breath, cut it.
- Contractions. Short sentences. Grade 5 to 7. Active voice.
- Name the mechanism. Give one specific number. Handle one objection out loud.
- Say the CTA once at the end. In the 60s cut, once in the middle too.
- No em dashes anywhere. No "!!!" No all-caps sentences.
- Captions are assumed. Write on-screen text only for hooks, numbers, and the CTA.

---

## Step 4: Write the shot list (Seedance 2.5 and other AI video models)

When the format is "shot list," follow `reference/shot-list-format.md` exactly:

1. The shot table (one row per shot, 2 to 6 seconds each).
2. A paste-ready generation prompt per shot, with an identical subject description in every prompt.
3. Model notes for the tool they named.
4. The delivery checklist, ticked.

Still include the hook options and the 15 / 30 / 60 cuts (as shot counts).

---

## Step 5: Compliance and retention check

- [ ] Hook is the first spoken words and the first on-screen text.
- [ ] Every hook under 12 words. Every on-screen text 7 words or fewer.
- [ ] Visual or idea change at least every 5 seconds.
- [ ] No personal attributes at the viewer, no guaranteed income or health results, "results vary" on any result claim.
- [ ] One CTA at the end, clear action, clear next-page outcome.
- [ ] Runtime matches the cut. Count roughly 2.5 words per second.
- [ ] Zero em dashes.
- [ ] The two scripts use different frameworks.

---

## Step 6: Save and log

Save to `[outputDir]/[profile-slug]/[YYYY-MM-DD]-video-[offer-slug].md`. Append one line per script to `[outputDir]/swipe-log.md`: `| date | offer | video | framework | hook | status: untested |`. Tell the user the path.

## Step 7: Learn from results

On `results` or when the user reports hook rate, hold rate, CPL, or "script 2 won": update the swipe log row, add a line to `[outputDir]/learnings.md` (which hook type and framework won for this audience), and lead with that next time.

---

## Hand-offs

- Static image version of the same angle: `/ad-image-gen`.
- Primary text and headline for the ad that carries this video: `/ad-copy`.
- Generating the video itself: the user's tool (Arcads, Higgsfield, HeyGen). This skill writes; it doesn't render.

---

## Rules

1. Read the frameworks file before writing. Always.
2. Hooks are the product. Ten options, three marked, all different types.
3. Write for the mouth. Read it aloud in your head.
4. Something changes every 3 to 5 seconds, and the script says what.
5. Two scripts, two frameworks. Never rewrites.
6. No em dashes in any output.

---
Built by [@tenfoldmarc](https://instagram.com/tenfoldmarc). Follow for daily AI automation builds. Real systems, not theory.
