# Marketing Suite

Eight Claude Code skills that run a full direct-response funnel. Describe your business **once**, then every skill knows it.

Competitor research, ad copy, video scripts, ad images, VSLs, sales pages, opt-in pages, and GoHighLevel snippets. All free, all local, nothing uploaded anywhere.

---

## Install

### Option 1: paste one line (simplest)

Open Claude and paste this:

```
Install this skill for me: https://github.com/tenfoldmarc/marketing-suite
```

Claude installs everything and runs the setup right there in the same conversation. You answer a few questions and you're building.

### Option 2: install as a plugin (pick what you want, get updates)

```
/plugin marketplace add tenfoldmarc/marketing-suite
```

Then open the plugin browser with `/plugin` and pick a bundle, or install one directly:

| Bundle | What's in it |
|---|---|
| `marketing-suite` | All eight skills |
| `marketing-suite-ads` | `/ad-spy` `/ad-copy` `/video-ad-copy` `/ad-image-gen` |
| `marketing-suite-pages` | `/optin-page` `/sales-page` `/vsl-script` `/ghl-page` |

```
/plugin install marketing-suite@marketing-suite
```

Installed this way, the skills update when this repo does.

Either way, type `/marketing-suite` to set up.

---

## The eight skills

| Skill | What it does |
|---|---|
| `/ad-spy` | Saves competitor Ad Library links, pulls their active ads, downloads and transcribes the videos, spots the longest-running ones, and turns the winning angles into a brief for the other skills |
| `/ad-copy` | 3 to 5 complete Meta ads, each a different angle. Opener, body, 3 headlines, description, CTA, the line for the image. Checked against character limits and ad policy before you see it |
| `/video-ad-copy` | Video scripts for talking head, UGC, or AI avatar. 5 to 10 hooks, timestamped lines, on-screen text, b-roll cues, 15/30/60 second cuts. Or a shot list with paste-ready prompts |
| `/ad-image-gen` | The actual images. Picks 4 of 11 proven formats, writes the on-image copy, generates in 4:5, then checks every image for spelling, faces, and thumbnail legibility before showing you |
| `/vsl-script` | Video sales letters, 3 to 20 minutes. 13 sections with timestamps, slide list, objections handled |
| `/sales-page` | Long-form sales pages. 15 sections, offer stack, price, guarantee, FAQ, button copy. Written for the skimmer first |
| `/optin-page` | Opt-in and lead magnet pages, plus the thank-you page and the delivery email |
| `/ghl-page` | Production-ready GoHighLevel HTML snippets. Paste into a Custom HTML block and they work first time |

---

## The idea: describe your business once

Most marketing tools make you re-explain your business every single time. These don't.

The first time you open any skill, you answer 13 short questions, one at a time. Your name, what you sell, who buys it, what they've already tried, your proof, your story, how you talk. Skip anything. Type `done` to stop early.

After that, every skill in the suite already knows you.

```
~/.claude/ad-profiles/          who you are (answered once)
├── config.json                 which profile is active, where output goes
├── your-brand.md               the 13 answers
└── a-client.md                 a second business, switch with `profiles`

~/Documents/ad-copy/            what you made (grows)
├── your-brand/                 the finished work
├── swipe-log.md                one row per ad, marked winner or loser
└── learnings.md                what patterns won, and why
```

The profile sits **outside** the skill folders on purpose, so updating or reinstalling a skill never touches your answers.

Running two businesses, or client work? `/marketing-suite new [name]` adds a profile, `profiles` switches between them.

---

## They learn from each other

Tell any skill which ad, page, or video won:

```
/ad-copy results
```

It logs the numbers, then writes a plain-English note to a `learnings.md` that **every skill reads before writing**.

So a headline that wins on your sales page shows up in the next ad. A winning ad angle shows up in the next VSL. The suite gets sharper the more you use it, per brand.

---

## Optional design helpers

The page skills (`/optin-page`, `/sales-page`, `/ghl-page`) build good pages on their own. If you want them to look genuinely designed rather than merely functional, two other people's skills pair well. Neither ships in this repo, and the suite never installs anything without asking.

- **[impeccable](https://impeccable.style/)** by [pbakaus](https://github.com/pbakaus/impeccable). Design skills built to fight generic AI output.
  `npx impeccable install` then `/impeccable init`. Needs Node 22.12+.
- **frontend-design** by Anthropic.
  `/plugin install frontend-design@claude-plugins-official`

The page skills detect what's missing and offer these when you're about to build. Say no and everything still works.

---

## A workflow that works

1. `/ad-spy` to see what competitors have already proven with money
2. `/ad-copy` for 4 ads on the best angle, each with an on-image headline
3. `/ad-image-gen` with that headline, approve the 2 you like
4. `/video-ad-copy` for the same offer, shoot one on your phone
5. `/optin-page` or `/sales-page` for where the traffic lands
6. `/vsl-script` if the page needs a video at the top
7. Launch. A week later, `results` on whichever won

After the first setup, every new campaign is a handful of commands.

---

## What none of them will do

- Invent testimonials, numbers, names, or download counts. Missing proof gets written around, and you get told what proof would unlock.
- Write fake urgency or fake scarcity. Real deadline with a real reason, or nothing.
- Make income promises.
- Stack made-up value figures.
- Ask for an API key in chat. Keys live in `~/.claude/ad-profiles/.env` on your machine, written by you.

---

## Your data

Everything stays on your computer. The profiles are markdown files, the logs are markdown files, and nothing is uploaded anywhere.

Each skill is also published on its own if you only want one:
[ad-copy](https://github.com/tenfoldmarc/ad-copy-skill) ·
[video-ad-copy](https://github.com/tenfoldmarc/video-ad-copy-skill) ·
[ad-image-gen](https://github.com/tenfoldmarc/ad-image-gen-skill) ·
[ad-spy](https://github.com/tenfoldmarc/ad-spy-skill) ·
[vsl-script](https://github.com/tenfoldmarc/vsl-script-skill) ·
[sales-page](https://github.com/tenfoldmarc/sales-page-skill)

---

Built by [Marc Cleroux](https://github.com/tenfoldmarc).
