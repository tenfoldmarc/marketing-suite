# Shot List Format (for Seedance 2.5 and other AI video models)

When the user wants a shot list instead of a talking-head script, deliver the script in this format. It works for Seedance 2.5 on Higgsfield, Kling, Veo, Sora, and Arcads scene tools. Ask which model they're using and adjust the notes at the bottom.

---

## The table

One row per shot. Shots are 2 to 6 seconds each. A 30-second ad is 6 to 10 shots.

| # | Time | Shot | What we see | What we hear (VO / dialogue) | On-screen text | Sound / music |
|---|---|---|---|---|---|---|
| 1 | 0:00 to 0:03 | Close-up, handheld, slight push in | [subject, setting, action, lighting] | "[hook line]" | "[hook, 3 to 7 words]" | [sfx or music cue] |

Column rules:
- **Shot**: framing (extreme close-up / close-up / medium / wide), camera move (static / push in / pull back / handheld / orbit / whip pan), and lens feel (shallow depth of field, phone camera, cinematic).
- **What we see**: subject first, then action, then setting, then light. Concrete nouns. No adjectives the model can't render ("premium," "trustworthy").
- **What we hear**: the exact spoken line for that shot. Voiceover or on-camera dialogue. Under 20 words per shot.
- **On-screen text**: exact text in quotes, or "none." Say where: top third, center, lower third.
- **Sound / music**: music cue, sfx, or "music continues."

---

## The generation prompt (one per shot)

After the table, give a paste-ready prompt for each shot. Structure, in this order:

```
Shot [N] of [total]. [Duration] seconds. 9:16 vertical.
[Framing and camera move]. [Subject description, including consistent traits: age, hair, clothing, so the character matches across shots]. [Action in one sentence]. [Setting]. [Lighting]. [Style: phone-camera UGC / clean studio / cinematic].
On-screen text, exactly: "[text]" in [heavy white sans-serif, upper third]. No other text, no logos, no watermark.
[If dialogue]: The person says, lip-synced: "[line]".
Mood: [one word].
```

Character consistency rule: the subject description is identical in every prompt, word for word. Change only action, framing, and setting.

---

## Model notes

**Seedance 2.5 (Higgsfield)**
- Best at: multi-shot continuity, natural motion, lip-sync on dialogue, 9:16 native.
- Write shots as one prompt each, or chain up to 3 shots in one prompt with "Then cut to:" between them.
- Include the spoken line inside the prompt for lip-sync. Keep it short.
- State aspect ratio and duration at the top of every prompt.
- Avoid: text longer than 7 words on screen (spelling drifts), crowds, hands holding small labeled products.

**Arcads (AI actors)**
- You supply the script, Arcads supplies the actor. Deliver the script as a line-by-line list with [pause] and emphasis marks. No camera directions needed.
- Keep each line under 20 words. Add b-roll cues in brackets for the editor.

**Kling / Veo / Sora**
- Same prompt structure. Veo and Sora handle dialogue; Kling is stronger on motion than speech. If the model doesn't lip-sync well, write the line as voiceover and show the person mid-action instead of talking.

---

## Delivery checklist

- [ ] Hook lands in shot 1 with spoken line + on-screen text + a visual break.
- [ ] Something changes every 3 to 5 seconds (new shot, new text, new angle).
- [ ] Subject description is identical across all prompts.
- [ ] Every on-screen text is 7 words or fewer and in quotes.
- [ ] CTA shot at the end: person to camera or text card, "Tap Learn More" plus the outcome.
- [ ] Total runtime matches the requested cut (15 / 30 / 60).
- [ ] Safe zones respected: no text in top 250px or bottom 340px of a 1080x1920 frame.
