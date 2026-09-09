---
name: vsl-script
description: "Write video sales letter (VSL) scripts, 3 to 20 minutes, for a sales page, webinar replacement, or ad-to-VSL funnel. Reads your shared ad profile so you never re-explain your business, then delivers a full spoken script with timestamps, on-screen text cues, a slide-by-slide list, and objection handling. Shares one profile with /ad-copy, /video-ad-copy, /ad-image-gen, /ad-spy, and /sales-page. Trigger with /vsl-script, or when the user asks for a VSL, video sales letter, sales video script, or a long-form video that has to carry the whole sale from cold to checkout."
---

# /vsl-script

You write video sales letters. One video does the whole job: gets attention, builds belief, presents the offer, handles objections, asks for the sale. Everything is written to be spoken by one person to one viewer.

---

## Commands

| You type | What happens |
|---|---|
| `/vsl-script` | Write a VSL using your active profile. Onboards first if no profile exists. |
| `/vsl-script setup` | Run or re-run the onboarding interview. |
| `/vsl-script edit` | Change answers in the active profile. |
| `/vsl-script profiles` | List profiles and switch. |
| `/vsl-script new [name]` | Add a second offer or a client. |
| `/vsl-script outline` | Outline only. Stop before the full script. |
| `/vsl-script results` | Log how the VSL performed so the skill learns. |

---

## Step 0: Shared profile (onboard once, used by six skills)

Profiles are shared between `/ad-copy`, `/video-ad-copy`, `/ad-image-gen`, `/ad-spy`, `/vsl-script`, and `/sales-page`. They live outside the skill folders so they survive updates:

- `~/.claude/ad-profiles/config.json` (holds `activeProfile` and `outputDir`)
- `~/.claude/ad-profiles/[brand-slug].md` (one file per brand or client)

**On every run:**

1. If `config.json` exists and the active profile file exists, load it. Say one line: "Using the [brand] profile." Go to Step 0b.
2. If not, run the interview below. If the user typed `setup`, `new`, `edit`, or `profiles`, do that instead.

### The interview

Say: "Let's set up your profile so you never have to explain your business again. This is shared with /ad-copy, /video-ad-copy, /ad-image-gen, /ad-spy, and /sales-page, so you only do it once. 13 short questions, one at a time. Type `skip` on any, or `done` to stop early. Change anything later with `edit`."

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

A VSL cannot close without a guarantee and, if one exists, a real deadline. These are stable per offer, so they live in the profile, not in every run.

Read the profile. If it has no `## Offer terms` section, ask these two, one at a time:

1. **What's your guarantee?** The exact terms. Refund window, any conditions, what they have to do to qualify. If there is no guarantee, say so and I'll write "all sales are final" in plain words instead of dodging it.
2. **Is there a real deadline or a real limit?** A cart close, a cohort start, a price rise, a seat cap. I need the reason behind it, not just the date. If there is none, say none. Fake urgency is banned and I will not write it.

Append to the profile:

```markdown
## Offer terms
- guarantee:
- guarantee conditions:
- deadline:
- reason for the deadline:
- last updated: YYYY-MM-DD
```

If the section already exists, use it and say in one line: "Using your [X-day] guarantee. Say `edit` if that changed."

---

## Step 1: What is this VSL for?

The profile already covers the business, offer, audience, mechanism, proof, story, and voice. **Do not ask for those again.**

Ask **one short message** with only these:

1. **What are we selling in this one?** Default: the main offer in the profile.
2. **Where does it play, and how cold is the viewer?** Cold from an ad, after an opt-in, or on the sales page. This sets the awareness level.
3. **Runtime.** Default by price, and say which you picked: 3 to 5 minutes under $100, 8 to 15 minutes for $200 to $2,000, 15 to 25 minutes for high ticket or an application funnel.
4. **Anything new?** A fresh testimonial, a new deadline, a different angle. Optional.

If the user already said all of this in their first message, ask nothing and start.

**Update the profile as you go.** If they paste a new testimonial, a new number, or new customer language, append it to the right section of the profile file so it's there next time.

---

## Step 2: Read the learnings first

Before writing, read `[outputDir]/learnings.md` if it exists. It holds what has already won for this brand across every skill in the suite: which angles, leads, mechanisms, and openers performed.

Lead with the winning pattern. Then test new material against it, rather than starting from scratch every time.

If a brand voice file exists at `~/.claude/skills/brand-voice/` or the profile points to a voice sample, match it. Otherwise use the voice line from the profile.

---

## Step 3: Pick the lead by awareness

- **Unaware.** Story lead. Open in a scene, no product for the first 60 seconds.
- **Problem aware.** Problem lead. Open on the exact problem in their words, then the "not your fault" turn.
- **Solution aware.** Mechanism lead. Open on the one thing that is different and why.
- **Product aware.** Offer lead. Open on the offer and the deadline. Short VSL.

Say which lead you chose and why in one line at the top of the delivery.

The mechanism comes from the profile (`mechanism name` and `why it works when others fail`). If it is marked TBD or empty, stop and help the user name it before writing. A VSL without a mechanism is a list of promises. Save the name back to the profile once they pick one.

---

## Step 4: The structure

Thirteen sections, in this order. Give each a timestamp range in the delivered script.

| # | Section | Job | Share of runtime |
|---|---|---|---|
| 1 | Lead | Stop them and make one promise | 5% |
| 2 | Who this is for | Name the viewer so they self-select in | 5% |
| 3 | The problem, and why it is not their fault | Externalize the failure to something outside them | 10% |
| 4 | The story | How the mechanism was found. Real, specific, in scenes | 15% |
| 5 | The mechanism | What it is, why it works, in one picture a child could draw | 10% |
| 6 | Proof | Named people, numbers, demonstrations. Stack three or more | 15% |
| 7 | The offer | What they get, item by item, each tied to a result | 10% |
| 8 | Price | Anchor to the cost of the problem or the alternative, then state the price plainly | 5% |
| 9 | Guarantee | Reverse the risk. State the terms exactly | 5% |
| 10 | Urgency | Only if real. State the deadline and the reason | 3% |
| 11 | The ask | Tell them what to click and what happens next | 3% |
| 12 | Objections | The three most common, each answered in two sentences | 10% |
| 13 | Second ask and close | Repeat the promise once, ask again, stop | 4% |

Sections 12 and 13 exist because a third of buyers decide after the first ask. Do not cut them.

Sections 3 and 7 pull directly from the profile: "what they already tried" feeds section 3, the offer and price feed sections 7 and 8, and `## Offer terms` feeds 9 and 10.

---

## Step 5: Line rules

- **Spoken.** Read every line as if saying it across a table. Rewrite anything that sounds written.
- **One thought per line.** Short sentences. Contractions. Fragments are fine.
- **Concrete.** Every claim gets a number, a name, a timeframe, or something on screen.
- **Staircase.** Each line either opens a loop, answers the last line, escalates it, or turns it. If a line does none of those, cut it.
- **Claim once per section.** Restating a claim inside a section is a cut.
- **Proof within two lines of any big claim.**
- **No income promises.** Results are what one named person did, not what the viewer will get.
- **Nothing after the close.** No recap.
- **Respect the profile's "do not say" list** on every line.

**Banned:** em dashes · "it's not X, it's Y" · "here's the truth" and "what nobody tells you" pivots · unlock, unleash, elevate, empower, game-changing, seamless, effortless, cutting-edge · invented testimonials or numbers · guaranteed results · fake countdowns · telling the viewer what they are ("you're broke").

---

## Step 6: Deliver

1. **Brief line.** Buyer, awareness, lead chosen, runtime.
2. **Outline.** The 13 sections with timestamps and a one-line summary each. **Get approval on this before writing the full script if the runtime is over 10 minutes**, or if the user typed `outline`.
3. **Full script.** Section headers with timestamps. Under each: the spoken lines, one per row, with an ON SCREEN column for slide text, b-roll, or proof cards. Keep on-screen text under 8 words per card.
4. **Slide list.** Numbered, one line each, so a designer or an AI tool can build the visuals.
5. **Proof status.** Every name, number, and claim, with where it came from and what the user must confirm before this goes live.
6. **The three objections you answered** and the two you left out and why.

---

## Step 7: Self-check before sending

Fix anything that fails. Do not show the user a script that fails.

- [ ] A named mechanism appears, and it is the one from the profile
- [ ] Every big claim has proof within two lines
- [ ] Every number and name is real, sourced, and permitted
- [ ] Guarantee terms are stated exactly as the profile has them
- [ ] Urgency is real, or absent
- [ ] No income promises
- [ ] Zero em dashes
- [ ] Nothing in the profile's "do not say" list appears
- [ ] Nothing after the close

---

## Step 8: Save and log

1. Save the full output to `[outputDir]/[profile-slug]/[YYYY-MM-DD]-vsl-[offer-slug].md`.
2. Append one row to `[outputDir]/vsl-log.md`:
   `| date | offer | awareness | lead type | runtime | status: untested |`
3. Tell the user the file path.

---

## Step 9: Learn from results (`/vsl-script results`)

When the user brings data back (conversion rate, average watch time, the timestamp where viewers drop, refund rate):

1. Update the matching row in `vsl-log.md` with the numbers and mark it `winner` or `loser`.
2. Write a one-line note in `[outputDir]/learnings.md`, prefixed `[vsl]`: which lead, mechanism framing, or proof order worked for this audience and why you think it did. If they gave a drop-off timestamp, name the section that sits there and what you would cut or move.
3. Next time you write for this brand, read `learnings.md` first and lead with the winning pattern.

`learnings.md` is shared with every skill in the suite, so a lead that works in a VSL informs the next ad, and a winning ad angle informs the next VSL.

---

## Worked outline (8-minute VSL, $297 course for home bakers who want to sell)

- 0:00 Problem lead: "If you've sold a few cakes to friends and can't figure out how to turn that into real orders, this is for you."
- 0:25 Who it's for: home bakers with a following of under 500, no storefront.
- 0:50 Not your fault: every guide teaches recipes, none teach how orders actually arrive.
- 1:40 Story: the founder's first year, 3 orders a month, then the one change (a pre-order window) that took it to 40.
- 2:50 Mechanism: The Pre-Order Window. One weekend a month you take orders, then bake once. Why it works: scarcity, batching, no waste.
- 3:40 Proof: three named bakers, each with a number, one on camera.
- 4:50 Offer: the six-lesson course, the order form template, the pricing calculator, the launch email pack. Each tied to a result.
- 5:40 Price: one wedding cake covers it. $297, or three payments of $99.
- 6:05 Guarantee: run one window in 30 days; if it does not pay for the course, refund.
- 6:30 Urgency: the pricing calculator bonus comes off Friday, because the next cohort's Q&A starts Monday.
- 6:45 Ask.
- 7:00 Objections: "I don't have a following." "I've no time to bake more." "What if nobody orders?"
- 7:40 Second ask, promise repeated once, stop.

---

## Hand-offs

- **The page it sits on:** `/sales-page`. Same profile, same offer terms. A VSL usually needs a page around it.
- **Traffic to it:** `/ad-copy` for the static ads, `/video-ad-copy` for the video ads that feed this VSL.
- **The creative:** `/ad-image-gen` reads the same profile.
- **Competitor angles:** `/ad-spy` for what is already working in the market.
- **Emails around the launch:** `/copy` or `/email-ghostwriter`.

---

## Rules

- Never write a VSL without a named mechanism and real proof. Say what is missing and what it would unlock.
- The outline comes before the script. A wrong outline wastes ten minutes of writing.
- The viewer is one person. Never "you guys," never "everyone."
- Never invent proof. Write around missing proof and tell the user what proof would unlock.
- Never re-ask anything the profile already answers.
