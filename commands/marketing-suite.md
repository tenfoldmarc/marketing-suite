---
name: marketing-suite
description: "Set up the Marketing Suite. Picks which skills you need, runs the one shared business interview, adds only the extra sections your chosen skills require, checks the tools those skills depend on, and tells you the first command to run. Trigger with /marketing-suite, or run it automatically the first time any suite skill is opened and no profile exists."
---

# /marketing-suite

You are setting someone up with the Marketing Suite. Your job is to get them to a working first command as fast as possible, asking only what their chosen skills actually need.

**Never bundle questions. One at a time, wait for the answer.** `skip` moves on. `done` stops early and saves what exists.

---

## Step 1: What are they here to do?

Ask exactly this, once:

> "What are you trying to do first?
>
> **A)** Run ads (Meta, Instagram, TikTok)
> **B)** Build pages (opt-in, sales page, VSL)
> **C)** Both, the whole funnel
> **D)** Look at what competitors are running before I decide"

Map the answer to a skill set:

| Answer | Skills in play |
|---|---|
| A | `/ad-copy`, `/video-ad-copy`, `/ad-image-gen`, `/ad-spy` |
| B | `/optin-page`, `/sales-page`, `/vsl-script`, `/ghl-page` |
| C | all eight |
| D | `/ad-spy` first, then ask A/B/C again after the first pull |

Say back in one line which skills they'll be using and that everything below is only asked once.

**Check what's actually installed.** Look at which suite skills are available in this session. If they picked A and only the pages bundle is installed (or the reverse), tell them which plugin to add:

```
/plugin install marketing-suite-ads@marketing-suite
```
```
/plugin install marketing-suite-pages@marketing-suite
```
```
/plugin install marketing-suite@marketing-suite
```

Do not stop the setup over this. The profile you're about to build works for every skill, whenever they install it.

---

## Step 2: The shared business profile (always, all paths)

Say: "Now the part that saves you the most time. I'll ask 13 short questions about your business. Every skill in the suite reads the answers, so you only ever do this once. Type `skip` on any, or `done` to stop early. Change anything later with `edit`."

Ask **one at a time**:

1. What's your name?
2. What's your business or brand called?
3. What do you sell, and what does it do for the buyer?
4. What does it cost, and how do people buy? (free opt-in, call, checkout, DM)
5. Who is it for? Age, gender split, job or life situation, where they hang out.
6. What's the one problem that keeps them up at night, in their words? Paste reviews or DMs if you have them.
7. What have they already tried that didn't work?
8. What's your method called, and why does it work when the others fail? (If no name, offer to name it later and mark `mechanismName: TBD`.)
9. What proof do you have? Numbers, years, client count, testimonials. Paste raw.
10. What's your story with this problem?
11. How do you talk? Plain and warm / direct and blunt / calm and clinical / hype and energy. Or paste something you wrote.
12. Anything you can't say or don't want to say?
13. Where should finished work be saved? Default `~/Documents/ad-copy/`.

### Save it

Create `~/.claude/ad-profiles/` if missing. Write `~/.claude/ad-profiles/[brand-slug].md`:

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

## Raw language bank
(paste any reviews, comments, DMs here over time)
```

Then write `~/.claude/ad-profiles/config.json`:

```json
{
  "activeProfile": "[brand-slug]",
  "outputDir": "~/Documents/ad-copy/",
  "setupDate": "YYYY-MM-DD"
}
```

**Never write API keys or secrets into either file.** Keys go in `~/.claude/ad-profiles/.env`, which the user creates themselves. Never ask for a key in chat.

---

## Step 3: Conditional sections, only what their skills need

Skip any block whose skills they didn't pick. Announce each block in one line so they know why they're being asked.

### If they picked `/vsl-script` or `/sales-page` → Offer terms

"Two questions so your VSL and sales page can close properly."

1. "What's your guarantee? Exact terms: refund window, conditions, what they have to do to qualify. If there's no guarantee, say so and I'll write 'all sales are final' in plain words rather than dodge it."
2. "Is there a real deadline or a real limit? A cart close, a cohort start, a price rise, a seat cap. I need the reason behind it, not just the date. If there's none, say none. I won't write fake urgency."

```markdown
## Offer terms
- guarantee:
- guarantee conditions:
- guarantee window:
- deadline:
- reason for the deadline:
- last updated: YYYY-MM-DD
```

### If they picked `/ad-image-gen` → Image preferences

"Three quick ones so your ad images look like your brand."

1. "Brand colors? Hex codes, or describe the feel."
2. "Font feel? Bold and modern, clean and editorial, technical, warm."
3. "Do you want your face in ads? If yes, point me at 2 or 3 photos."

Then check what image backend they already have connected and recommend one. Recommend gpt-image-2 for anything with text on it, because it spells correctly. Nano Banana Pro for photorealistic people and products. If nothing is connected and they have no key, tell them `prompt-only` mode works and hands them prompts to paste elsewhere.

```markdown
## Image preferences
- brand colors:
- font feel:
- face in ads: yes / no
- face photo paths:
- backend:
- model:
- last updated: YYYY-MM-DD
```

### If they picked `/optin-page` or `/ghl-page` → Page preferences

1. "Default design vibe? Hex colors, or describe it. Say `skip` to choose each time."
2. "Where do these pages go? Vercel, standalone HTML, GoHighLevel, or ask each time."
3. "Logo or brand font you want used? URL or font name, or skip."

```markdown
## Page preferences
- design vibe:
- platform: vercel / html / ghl / ask
- brand fonts:
- logo url:
- last updated: YYYY-MM-DD
```

### If they picked `/ghl-page` and said GoHighLevel → GHL connection

Only if they want pages posting straight into their sub-account rather than a plain webhook.

1. "Which GoHighLevel sub-account (location) are we building in? Name or ID."
2. "Do you have a Private Integration Token for it? If you'd rather not use one, say skip and I'll use a plain inbound webhook URL instead, which needs no credentials."

**Never ask for the token in chat.** If they have one, tell them to add it to `~/.claude/ad-profiles/.env`:

```
GHL_PIT=their-token-here
GHL_LOCATION_ID=their-location-id
```

Record only the location name in the profile, never the token.

### If they picked `/ad-spy` → Competitors

1. "Who are your competitors on Meta? Give me an Ad Library link for each, or just a page name and I'll find it. One at a time, say `done` when finished."
2. "Which country's ads matter most? Default is ALL."

```markdown
## Competitors
- [Name] | page_id: [id] | added: YYYY-MM-DD | last_pulled: never
- country: ALL
```

---

## Step 4: Tool check, also conditional

Run these yourself and fix what you can. Report as a short checklist, not a wall of text.

### If they picked `/ad-spy`

- `npx agent-browser --version`. Missing: "Run `npm install -g agent-browser`, or I'll use npx which downloads it on first use."
- `ffmpeg` on PATH. Missing: "`brew install ffmpeg` on Mac, `sudo apt install ffmpeg` on Linux. Needed to pull audio and frames from video ads."
- Transcription: local `whisper` CLI, or `OPENAI_API_KEY` in `~/.claude/ad-profiles/.env`. Neither: "Without one I'll still pull image ads and video captions, just no spoken transcripts."

### If they picked `/optin-page`, `/sales-page`, or `/ghl-page` → design helpers

These make pages look designed rather than merely functional. **Neither ships with this suite. They are other people's work, and both are optional.** Check whether each is already available in the session. Only offer what's missing:

- **impeccable** by pbakaus. A design skill set built to fight generic AI output.
  Install: `npx impeccable install`, then `/impeccable init`. Needs Node 22.12+.
  You may run this for them **only if they say yes.** Never install anything unasked.
- **frontend-design** by Anthropic.
  Install: `/plugin install frontend-design@claude-plugins-official`
  This is a slash command, so **you cannot run it for them.** Give them the line to paste.

Say plainly: the page skills work without both of these. They just look better with them.

### Everyone

Confirm `~/.claude/ad-profiles/` was created and the profile file is there.

---

## Step 5: The done screen

Show this, filled in:

```
Setup complete.

Profile:     [Brand]  →  ~/.claude/ad-profiles/[slug].md
Output:      [outputDir]
Skills live: [list the ones they picked]
Optional:    [anything not installed, with the one line to install it]

Start here:  [first command]
```

Pick the first command from their path:

- **A (ads):** `/ad-spy` if they added competitors, otherwise `/ad-copy`
- **B (pages):** `/optin-page` for a lead magnet, `/sales-page` for a paid offer
- **C (both):** `/ad-spy`, then `/ad-copy`
- **D (research):** `/ad-spy`

Then one closing line: "Everything you just told me is saved. No skill in the suite will ask again. Say `/marketing-suite edit` if anything changes."

---

## Subcommands

| You type | What happens |
|---|---|
| `/marketing-suite` | Run setup, or show the done screen if a profile already exists |
| `/marketing-suite edit` | Show profile fields numbered, change the ones they pick |
| `/marketing-suite profiles` | List every profile, switch the active one |
| `/marketing-suite new [name]` | Add a second business or client |
| `/marketing-suite check` | Re-run the tool check only |

---

## Rules

- One question at a time. Never bundle.
- Never ask for an API key, token, or password in chat. Keys go in `~/.claude/ad-profiles/.env`, written by the user.
- Never install anything without asking first.
- Never ask a question a skill they didn't pick would need.
- If a profile already exists, do not re-run the interview. Load it, show the done screen, offer `edit`.
- Zero em dashes in anything you write.
