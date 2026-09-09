---
name: optin-page
description: "Build high-converting opt-in (lead magnet / squeeze) landing pages with AI-generated hero images, proven direct-response copy, animation, and mobile-first design. Also writes the thank-you page and the delivery email. Reads the shared Marketing Suite profile so you never re-explain your business. Trigger with /optin-page, or when the user asks for an opt-in page, squeeze page, lead magnet page, or a landing page for a free guide."
user-invocable: true
argument-hint: "[topic or offer description]"
---

# Opt-In Page Builder

Build opt-in pages that look like a top agency built them, convert like a direct-response pro wrote them, and load fast on every device.

An opt-in page has one job: trade something specific for an email address. Everything on the page either raises the value of the thing or lowers the cost of the ask. Anything else is a leak.

## Optional design helpers

This skill writes and builds the page on its own. If the user wants it to look genuinely designed rather than merely functional, check whether either of these is available in the session and offer it once:

- **impeccable**, a design skill set built to fight generic AI output. Install: `npx impeccable install` then `/impeccable init`. Needs Node 22.12+.
- **frontend-design**, Anthropic's design skill. Install: `/plugin install frontend-design@claude-plugins-official`

Neither ships with this suite, they are other people's work. Offer them once, never block on them, and never install anything without asking first. If the user declines or they aren't present, build with the design rules in this file, which stand on their own.

For hero images, use whatever image tool the user already has connected (an image connector, an API key, or a local model). If none is available, describe the image and let them generate it elsewhere.

---

## Step 0 — First-Time Setup

This skill reads the same profile as the rest of the Marketing Suite, so the business is described once:

- `~/.claude/ad-profiles/config.json` (holds `activeProfile` and `outputDir`)
- `~/.claude/ad-profiles/[brand-slug].md` (one file per brand or client)

**If a profile is active:** load it and say one line: "Using the [brand] profile. What are we building?" Brand, offer, audience, their problem in their own words, proof, story, and voice all come from there. Skip to Step 0b.

**If no profile exists:** run `/marketing-suite` to set one up, or run the same 13-question interview here (name, brand, offer, price and how they buy, audience, their problem in their words, what they tried, mechanism, proof, story, voice, do-not-say, output folder). One question at a time. `skip` and `done` work. Save in the shared markdown layout so every skill in the suite reads it.

### Step 0b — Page preferences (asked once, then stored)

Shared with `/ghl-page`. If the profile has no `## Page preferences` section, ask one at a time:

1. "Default design vibe? Give me hex colors, or describe it (dark premium, clean modern, bright and energetic). Say `skip` to choose each time."
2. "Where do these pages go? **A)** Vercel (Next.js, `/api/submit` route, full deploy), **B)** Standalone HTML (single file, no backend), **C)** GoHighLevel (use `/ghl-page` for the snippet), or **D)** ask me each time."
3. "Do you have a logo or brand font you want used? Paste a URL or a font name, or say skip."

Append to the profile:

```markdown
## Page preferences
- design vibe:
- platform: vercel / html / ghl / ask
- brand fonts:
- logo url:
- last updated: YYYY-MM-DD
```

Then proceed to Step 1.

---

## Step 1 — Gather Intelligence

The profile already covers the brand, audience, their problem in their own words, proof, story, and voice. **Do not ask for those again.** Ask only:

1. **What's the lead magnet?** What are they giving away (free guide, checklist, video training, tool, template, challenge, webinar), and the one specific result someone gets from using it.
2. **What do you sell after this?** The paid thing this lead is meant to buy later. The opt-in page and the thank-you page both point at it, quietly. Default: the main offer in the profile.
3. **Where's the traffic from?** Cold ad, social bio, email, podcast. Cold traffic needs more proof and a tighter promise.
4. **Any specific images needed?** (product mockup, person, abstract, etc.)

If the user already said all of this in their first message, ask nothing and start.

**Update the profile as you go.** If they paste a new testimonial, number, or piece of customer language, append it to the right section of the profile so it's there next time.

---

## Step 2 — Write the Copy

Before writing, read `[outputDir]/learnings.md` if it exists. It holds what has already won for this brand across every skill in the suite: headlines, angles, openers. Lead with the winning pattern, then test new material against it.

Match the voice line from the profile, and respect its "do not say" list on every line.

### Headline Rules

The headline is the single most important element. It must combine **benefit + curiosity**.

Apply these filters in order:

1. **Dan Kennedy Classified Ad Test:** If this headline appeared in the newspaper classifieds with only a phone number, would people call? If not, rewrite.
2. **Benefit + Curiosity Formula:** The headline promises a specific outcome AND creates an open loop the reader needs to close.
3. **Specificity:** Use exact numbers, timeframes, or quantities. "7 AI Tools" beats "Some AI Tools." "In 14 Days" beats "Quickly."
4. **Pattern Interrupt:** Break what they expect to see. Contrarian angles stop the scroll.

### Headline Formula Templates (pick the best fit):

- **How To + Without:** "How to [OUTCOME] Without [THING THEY FEAR]"
- **Number + Outcome:** "[NUMBER] [SECRETS/TOOLS/STEPS] That [SPECIFIC OUTCOME]"
- **Question + Implied Secret:** "Why Do Some [TARGETS] [WIN] While Others [LOSE]?"
- **Contrarian + Proof:** "[THING EVERYONE BELIEVES]? Wrong. Here's What Actually [WORKS]"
- **From/To + Mechanism:** "From [PAINFUL STATE] to [DREAM STATE] Using [NAMED MECHANISM]"
- **Warning + Benefit:** "Stop [COMMON MISTAKE] (Do THIS Instead to [OUTCOME])"
- **Curiosity + Timeframe:** "The [ADJECTIVE] [THING] That [OUTCOME] in [TIMEFRAME]"

### Full Copy Deliverable:

Write and present to the user:

```
BADGE: [Category label, e.g. "FREE AI GUIDE"]

HEADLINE:
[Line 1]
[Line 2]
[Line 3, accent color]

SUBHEADLINE:
[1-2 sentences. What they get + why it matters.]

BULLET POINTS:
✓ [Specific benefit 1]
✓ [Specific benefit 2]
✓ [Specific benefit 3]
✓ [Specific benefit 4]
✓ [Specific benefit 5]

CTA BUTTON: [Action verb + what they get, e.g. "Send Me The Guide"]

TRUST LINE: [e.g. "No spam. Unsubscribe anytime." or "Join 4,200+ subscribers"]

SOCIAL PROOF: [If available: testimonial, subscriber count, media logos]
```

Generate 3 headline options. Recommend the strongest one and explain why in one line.

**Wait for user to approve copy before building.**

---

## Step 3 — Generate Hero Image

Use `arcads_generate_image_gpt` (GPT Image 2 via Arcads) to create visuals.

### Image Strategy by Offer Type:

- **Free Guide / PDF:** Generate a stylized 3D book cover or document mockup floating in space with ambient lighting
- **Video Training:** Generate a laptop/screen showing the training with dramatic lighting
- **Tool / Template:** Generate an abstract tech visualization or dashboard mockup
- **Challenge / Webinar:** Generate a dynamic scene that represents the transformation
- **General Lead Magnet:** Generate a hero background with depth, texture, and brand-aligned colors

### Prompt Engineering for GPT Image 2:

Always include in the prompt:
- The brand's color palette or vibe
- "Professional, high-end, editorial quality"
- "Clean background that works as a web hero section"
- Specific style direction (3D render, flat illustration, photorealistic, etc.)
- "No text in the image" (text goes in the HTML)

Generate 1-2 images. Show them to the user. Proceed when approved.

Save generated images. For Vercel deploys, save to the project's `/public/` directory. For standalone HTML, embed as base64 data URI or use the Arcads CDN URL.

---

## Step 4 — Build the Page

### Design Direction (apply /frontend-design principles)

Before coding, commit to a BOLD aesthetic:

1. **Pick a distinctive Google Fonts pairing** that matches the brand energy. Skip Inter, Roboto, Arial, system fonts, and purple-on-white gradients: they read as a default AI template, which is exactly the look these pages must not have. Starting points (illustrative, not a menu to cycle through):
   - Premium/luxury: Playfair Display + Source Sans 3
   - Bold/modern: Syne + Outfit
   - Clean/editorial: Newsreader + Instrument Sans
   - Tech/startup: Space Grotesk + IBM Plex Sans
   - Warm/approachable: Bricolage Grotesque + Crimson Pro

2. **Color system:** Define as CSS variables. One dominant background + one sharp accent color. Dark backgrounds with a single bright accent outperform safe neutrals for opt-in pages.

3. **Every build looks different from the last one** in layout, palette, type, and motion. If you build these for several brands or clients, repeated pages make all of them look templated.

### Page Structure

```
[ABOVE THE FOLD — must contain headline + form]
├── Navigation bar (minimal — logo/brand + optional link)
├── Hero section (two-column on desktop is the common default, not a requirement; vary it)
│   ├── Badge pill
│   ├── Headline (large, bold, accent on key words)
│   ├── Subheadline
│   ├── Bullet points with icons
│   ├── Hero image or mockup
│   └── Opt-in form card
│       ├── Form heading
│       ├── First Name input
│       ├── Email input
│       ├── CTA button (full width, bold color)
│       └── Trust line
[BELOW THE FOLD — builds desire and trust]
├── Social proof section (testimonials, logos, numbers)
├── "What You'll Get" section (expanded benefits with icons)
├── "Who This Is For" section
├── FAQ accordion (3-5 questions)
└── Footer CTA (repeat form or scroll-to-top button)
```

### Animation Requirements

Animations are CSS-only, with one exception: a small `IntersectionObserver` for below-fold scroll reveals. Reason: no library weight, and `transform`/`opacity` animations stay GPU-cheap on phones.

Every page needs motion that does four jobs: a staggered entrance on the hero elements, something that draws the eye to the form card, a CTA that feels alive (hover plus a gentle idle pulse), and reveals on below-fold sections. A subtle background treatment (gradient shift, particles, noise) is usually worth it. Choose timings and intensity by feel for this brand; reusing the same delays and effects on every build is how pages start looking alike.

Enhancements to pull from so each build feels distinct:
- Glassmorphism on the form card (backdrop-filter: blur)
- Animated border gradient on the form card
- Floating/rotating hero image with perspective transforms
- Parallax scroll effect on background elements
- Animated counter for social proof numbers
- Typewriter effect on a key phrase
- Micro-interactions on bullet points (icon animation on hover)

### Responsive Design — Mobile First

Design for 375px width FIRST, then scale up:
- `max-width: 1200px` content container, centered
- Hero switches from 2-column to stacked at `768px`
- Form card goes full-width on mobile with proper touch targets (min 44px tap areas)
- Font sizes use `clamp()` for fluid scaling, tuned to the chosen typeface (a headline that fits at 375px, reads large on desktop)
- Images use `max-width: 100%` and `loading="lazy"`
- No horizontal scroll ever

### Performance

- Google Fonts: preconnect + display=swap
- Images: WebP when possible, lazy loaded, properly sized
- CSS animations use `transform` and `opacity` only (GPU-accelerated)
- Total page weight target: under 500KB (excluding images)
- Inline critical CSS in `<style>` tag

---

## Step 5 — Platform-Specific Build

### If Vercel (Next.js):

Project structure:
```
{slug}-optin/
├── app/
│   ├── layout.tsx
│   ├── globals.css
│   ├── page.tsx          # Opt-in page
│   ├── thank-you/
│   │   └── page.tsx      # Thank you page
│   └── api/
│       └── submit/
│           └── route.ts  # Form handler
├── public/
│   └── hero.webp         # Generated image
├── package.json
├── tsconfig.json
├── next.config.ts
└── .gitignore
```

The API route uses `/contacts/upsert`, not `/contacts/`. Reason: `/contacts/` returns a 500 when the email already exists in GHL; upsert updates the contact instead.
```typescript
const ghlRes = await fetch("https://services.leadconnectorhq.com/contacts/upsert", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.GHL_API_KEY}`,
    "Content-Type": "application/json",
    Version: "2021-07-28",
  },
  body: JSON.stringify({
    firstName,
    email,
    locationId: process.env.GHL_LOCATION_ID,
    source: "<OFFER NAME> Opt-In",
    tags: ["<offer-tag>", "lead-magnet"],
  }),
});
```

Thank you page: checkmark animation, "Check Your Email" message, Instagram CTA.

### If Standalone HTML:

Single self-contained HTML file. All CSS inline. Images as base64 or CDN URLs. Form submits to a webhook URL the user provides (or a `mailto:` fallback).

---

## Step 6 — Apply /impeccable Polish

After the page is built, run a mental pass through the impeccable "Persuade" mode checklist:

1. **Visual hierarchy:** Does the eye flow naturally from badge → headline → subheadline → bullets → CTA?
2. **Typography:** Are font sizes, weights, and line-heights creating clear hierarchy?
3. **Spacing:** Is there generous whitespace? Are related elements grouped and separated from unrelated ones?
4. **Color:** Is the accent used decisively (not scattered)? Does the CTA button have the highest contrast on the page?
5. **Motion:** Do animations feel purposeful and polished, not janky or overwhelming?
6. **Mobile:** Does it look great at 375px? Are tap targets large enough? Does text read easily?
7. **Performance:** Are animations GPU-accelerated? Are images optimized? Is load time fast?
8. **Conversion:** Is the form above the fold? Is the CTA clear and low-friction? Is there trust/proof?

Fix any issues before showing the preview.

---

## Step 7 — Preview and Deploy

Start the dev server (or open the HTML file), open it in the browser, and give the user the URL. Say what happens after approval: deploy to the chosen platform, set up the GHL email template, hand over the live URL.

**Wait for approval before deploying.**

### Deploy (Vercel):
1. `git init && git add -A && git commit -m "Opt-in page: [offer name]"`
2. `npx vercel --yes` then `npx vercel --prod --yes`
3. Add env vars (GHL_API_KEY, GHL_LOCATION_ID)
4. Redeploy: `npx vercel --prod --yes`

### After Deploy:
- Test the form with a test email
- Verify GHL contact creation and tags
- Clean up test contacts
- Deliver final summary with all URLs, tags, and manual GHL workflow steps

---

## Step 8 — Final Delivery

```
Everything is live!

LANDING PAGE: [URL]
THANK YOU PAGE: [URL]/thank-you
CONTACT TAG: [tag] + lead-magnet
EMAIL TEMPLATE: [name] (in GHL)

MANUAL STEP (2 min):
Create a GHL workflow:
1. Trigger: "Contact Tag Added" → [tag]
2. Action: "Send Email" → [template name]
3. Subject: "Your free [thing] is ready, {{contact.first_name}}"
4. Turn ON
```

---

## Non-negotiables

- Copy is approved before anything is built, and images are generated before the page, because the layout depends on them.
- Nothing deploys until the user has seen the preview and said go.
- The form sits above the fold on desktop and mobile, the CTA is the highest-contrast element on the page, and the headline passes the Classified Ad Test. These are what make the page convert.
