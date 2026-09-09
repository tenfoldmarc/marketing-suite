---
name: sales-page
description: "Write long-form sales page copy for a course, membership, service, or product, including the offer stack, price section, guarantee, FAQ, and order button copy. Reads your shared ad profile so you never re-explain your business, then delivers the full page section by section with proof cards and design notes. Shares one profile with /ad-copy, /video-ad-copy, /ad-image-gen, /ad-spy, and /vsl-script. Trigger with /sales-page, or when the user asks for a sales page, sales letter, checkout page copy, or a landing page for a course that has to close the sale in text."
---

# /sales-page

A sales page is a VSL the reader controls. They skim first, then read the parts that concern them. So every section must stand alone, and the page must survive a reader who only reads headlines, bullets, and the price.

---

## Commands

| You type | What happens |
|---|---|
| `/sales-page` | Write a sales page using your active profile. Onboards first if no profile exists. |
| `/sales-page setup` | Run or re-run the onboarding interview. |
| `/sales-page edit` | Change answers in the active profile. |
| `/sales-page profiles` | List profiles and switch. |
| `/sales-page new [name]` | Add a second offer or a client. |
| `/sales-page outline` | Section outline with headlines only. Stop before the full page. |
| `/sales-page results` | Log how the page converted so the skill learns. |

---

## Step 0: Shared profile (onboard once, used by six skills)

Profiles are shared between `/ad-copy`, `/video-ad-copy`, `/ad-image-gen`, `/ad-spy`, `/vsl-script`, and `/sales-page`. They live outside the skill folders so they survive updates:

- `~/.claude/ad-profiles/config.json` (holds `activeProfile` and `outputDir`)
- `~/.claude/ad-profiles/[brand-slug].md` (one file per brand or client)

**On every run:**

1. If `config.json` exists and the active profile file exists, load it. Say one line: "Using the [brand] profile." Go to Step 0b.
2. If not, run the interview below. If the user typed `setup`, `new`, `edit`, or `profiles`, do that instead.

### The interview

Say: "Let's set up your profile so you never have to explain your business again. This is shared with /ad-copy, /video-ad-copy, /ad-image-gen, /ad-spy, and /vsl-script, so you only do it once. 13 short questions, one at a time. Type `skip` on any, or `done` to stop early. Change anything later with `edit`."

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

Create `~/.claude/ad-profiles/` if missing. Write `[brand-slug].md` using the shared profile format (Owner, Offer, Audience, Proof, Story, Do not say, Raw language bank). Then write `config.json`:

```json
{
  "activeProfile": "[brand-slug]",
  "outputDir": "~/Documents/ad-copy/",
  "setupDate": "YYYY-MM-DD"
}
```

Never store API keys or secrets in either file.

If a profile was created by another skill in the suite, it may carry extra sections (video preferences, image preferences, competitors). Leave them alone.

---

## Step 0b: Offer terms (asked once, then stored)

A sales page cannot close without a guarantee and, if one exists, a real deadline. These are stable per offer, so they live in the profile, not in every run. This is the same section `/vsl-script` uses. If it already exists, use it and say in one line: "Using your [X-day] guarantee. Say `edit` if that changed."

If the profile has no `## Offer terms` section, ask these two, one at a time:

1. **What's your guarantee?** The exact terms. Refund window, any conditions, what they have to do to qualify. If there is no guarantee, say so and I'll write "all sales are final" in plain words instead of dodging it.
2. **Is there a real deadline or a real limit?** A cart close, a cohort start, a price rise, a seat cap. I need the reason behind it, not just the date. If there is none, say none. Fake scarcity is banned and I will not write it.

Append to the profile:

```markdown
## Offer terms
- guarantee:
- guarantee conditions:
- deadline:
- reason for the deadline:
- last updated: YYYY-MM-DD
```

---

## Step 1: What is this page for?

The profile already covers the business, offer, audience, mechanism, proof, story, and voice. **Do not ask for those again.**

Ask **one short message** with only these:

1. **What are we selling on this page?** Default: the main offer in the profile.
2. **Where does the traffic come from?** Cold ad, email list, a VSL, an opt-in sequence, organic. Cold traffic needs more proof earlier and a longer opening.
3. **Is there a VSL or video at the top?** If yes, the opening section gets shorter and points at the video.
4. **Anything new?** A fresh testimonial, a price change, a new bonus. Optional.

If the user already said all of this in their first message, ask nothing and start.

Infer the **awareness level** from the traffic source and the profile. Cold ad usually means problem aware. Coming off a VSL or a nurture sequence usually means solution or product aware. Tell them what you picked in one line.

**Update the profile as you go.** If they paste a new testimonial, a new number, or new customer language, append it to the right section of the profile file so it's there next time.

---

## Step 2: Read the learnings first

Before writing, read `[outputDir]/learnings.md` if it exists. It holds what has already won for this brand across every skill in the suite: which angles, leads, mechanisms, headlines, and openers performed.

Lead with the winning pattern. Then test new material against it, rather than starting from scratch every time.

If a brand voice file exists at `~/.claude/skills/brand-voice/` or the profile points to a voice sample, match it. Otherwise use the voice line from the profile.

---

## Step 3: The page, in order

| # | Section | What it does | Notes |
|---|---|---|---|
| 1 | Headline + sub | The promise, specific, with the mechanism named | Under 15 words. Sub-headline says who it is for and how. |
| 2 | Opening | The lead: story, problem, mechanism, or offer, matched to awareness | 100 to 250 words. In scenes, not summary. |
| 3 | Who this is for / not for | Two short lists | Self-selection raises conversion and cuts refunds. |
| 4 | The problem and why it is not their fault | Externalize the failure | Their words, quoted if you have them. Pull from the profile's "problem in their words" and "what they already tried." |
| 5 | The mechanism | What it is, why it works, in one picture | One paragraph plus one diagram description. Use the mechanism name from the profile. |
| 6 | Proof block 1 | Two or three named results with numbers | Photo, name, one line, one number. |
| 7 | What you get | The offer stack, item by item | Each item: name, what it does, the result it produces. No value theater ("worth $4,997"). |
| 8 | How it works | Step 1, 2, 3 after they buy | Removes "what happens next" fear. |
| 9 | Proof block 2 | Screenshots, demonstrations, a longer story | Different kind of proof from block 1. |
| 10 | Price | Anchor to the cost of the problem, then the price plainly, then payment options | Never hide it. Never "investment." |
| 11 | Guarantee | Terms stated exactly, from `## Offer terms` | If none, say sales are final in plain words. |
| 12 | Urgency | Deadline + real reason from `## Offer terms`, or nothing | Fake scarcity is banned. |
| 13 | About | Who made this and why, short | From the profile's Story. Credentials and stake, not a biography. |
| 14 | FAQ | 5 to 8 real objections, each answered in 2 to 3 sentences | The most read section after price. |
| 15 | Final ask | Promise once more, button, one line on what happens after clicking | Stop. No P.S. chain. |

Put a button after sections 1, 7, 10, and 15. Same button text every time.

If the mechanism in the profile is marked TBD or empty, stop and help the user name it before writing. Save the name back to the profile once they pick one.

---

## Step 4: Line rules

- **Spoken.** Read every line aloud. Rewrite anything that sounds written.
- **Skim-proof.** Every section headline is a full sentence a skimmer could act on. "The Pre-Order Window: bake once, sell all month," not "The Method."
- **One thought per line.** Short paragraphs, 1 to 3 lines. White space is a feature.
- **Concrete.** Every claim has a number, a name, a timeframe, or a picture.
- **Proof within two lines of any big claim.**
- **Claim once per section.**
- **Bullets are curiosity gaps** about something specific inside, never feature lists.
- **Button text is a first-person result.** "Get the course" is weak. "Start my first pre-order window" is a button.
- **Respect the profile's "do not say" list** on every line.

**Banned:** em dashes · "it's not X, it's Y" · "here's the truth" pivots · unlock, unleash, elevate, empower, game-changing, seamless, effortless, cutting-edge · "investment" for price · value stacking with made-up dollar figures · fake countdowns · invented testimonials · income promises · "you're broke / tired / failing" address · more than one offer on the page · an embedded checkout above the price section.

---

## Step 5: Deliver

1. **Brief line.** Buyer, awareness, lead, offer, price.
2. **Section outline.** Each of the 15 sections with its headline written out. **Get approval on this first for pages over 1,500 words**, or if the user typed `outline`.
3. **Full page.** Section by section, headlines as full sentences, body copy, bullets, button text, proof cards marked `[PROOF: name, number, source]`.
4. **Button text.** One line, used everywhere.
5. **Three alternate headlines** with a reason to test each.
6. **Proof status.** Every name, number, and claim, with where it came from and what the user must confirm before this goes live.
7. **Design notes.** One line per section: image, screenshot, diagram, or none.

---

## Step 6: Self-check before sending

Fix anything that fails. Do not show the user a page that fails.

- [ ] A named mechanism appears in the headline and section 5, and it is the one from the profile
- [ ] Every big claim has proof within two lines
- [ ] Every number and name is real, sourced, and permitted
- [ ] Price is stated plainly, never as "investment," never hidden
- [ ] Guarantee terms match `## Offer terms` exactly
- [ ] Urgency is real, or absent
- [ ] One offer only
- [ ] Buttons after sections 1, 7, 10, 15, same text every time
- [ ] Every section headline is a full sentence a skimmer could act on
- [ ] Zero em dashes
- [ ] Nothing in the profile's "do not say" list appears

---

## Step 7: Save and log

1. Save the full output to `[outputDir]/[profile-slug]/[YYYY-MM-DD]-sales-page-[offer-slug].md`.
2. Append one row to `[outputDir]/sales-page-log.md`:
   `| date | offer | awareness | lead type | headline | price | status: untested |`
3. Tell the user the file path.

---

## Step 8: Learn from results (`/sales-page results`)

When the user brings data back (conversion rate, add-to-cart rate, scroll depth, refund rate, which headline won a split test):

1. Update the matching row in `sales-page-log.md` with the numbers and mark it `winner` or `loser`.
2. Write a one-line note in `[outputDir]/learnings.md`, prefixed `[sales-page]`: which headline, lead, offer-stack framing, or proof placement worked for this audience and why you think it did. If they gave scroll depth, name the section where readers stop and what you would move above it.
3. Next time you write for this brand, read `learnings.md` first and lead with the winning pattern, then test two new headlines against it.

`learnings.md` is shared with every skill in the suite, so a headline that wins on the page informs the next ad, and a winning ad angle informs the next page.

---

## Hand-offs

- **The video at the top:** `/vsl-script`. Same profile, same offer terms.
- **Traffic to this page:** `/ad-copy` for static ads, `/video-ad-copy` for video ads.
- **The creative:** `/ad-image-gen` reads the same profile.
- **Competitor angles:** `/ad-spy` for what is already working in the market.
- **The opt-in that feeds this:** `/optin-page` builds the page, `/free-guide` builds the lead magnet.
- **Building the actual page:** hand the finished copy to `/impeccable` or `/frontend-design`, or `/ghl-page` for a GoHighLevel snippet.

---

## Rules

- No page without a named mechanism and real proof. Say what is missing and what it would unlock.
- One offer per page. A second offer is a second page.
- The price is a sentence, not a reveal.
- Write for the skimmer first, the reader second.
- Never invent proof, download counts, or results.
- Never re-ask anything the profile already answers.
