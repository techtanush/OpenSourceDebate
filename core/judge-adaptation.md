# Judge Adaptation: Lay vs. Technical

The same argument needs different delivery for a parent or community judge than for a flow judge. The evidence and the honesty rules do not change. What changes is **how much jargon, how many layers, and how much plain explanation** each card gets.

Set the judge type in `team.yaml` (`judge: lay`, `tech`, or `mixed`). If it is not set, ask the user, because it changes the output.

## Lay judges (parents, community members, new judges)

What they respond to: a clear story, simple reasons, specific evidence they can picture. What loses them: jargon, speed, stacked "even if" layers, abstract takeouts.

**Rules for lay files:**

1. **A short plain-English analytic right after every card**, saying what the card means in everyday words. One or two sentences. Example:
   - Card: a study that found travel times on bordering streets fell nine percent.
   - Analytic: *"So the cars did not just move next door. The streets around the area actually got faster."*
2. **No labels that sound like notes to the reader.** Do not write "LAY VERSION:", "In simple terms:", "Plain English:", arrows (`A -> B -> C`), or bracketed meta-text. The file should read like a normal team file. The explanation is just a plain sentence.
3. **No unexplained jargon.** Say "paid for it" not "internalize the cost"; "the cars move to nearby streets" not "displacement"; spell out acronyms once.
4. **Answer the specific claim, not the whole case.** "That study is about one pilot street" lands better than "their entire case fails because of X." A broad takeout can sound like a reach; use it only if it is airtight and short. In the file, name the block for the claim and keep card names out of the titles and analytics.
5. **Fewer, stronger answers.** Two or three clean answers beat six. Lead with the one a parent would nod at.
6. **Keep numbers few and round.** One or two numbers per answer, said slowly. "About a third fewer injuries" over "35.8 percent."
7. **Tell a story with a person in it** when you can: who is affected and how.
8. **Close each argument with why it matters** in one plain sentence.

**Timing for lay rebuttals** (set in `team.yaml`; these are defaults a team used): about **2:00 per contention** in the first rebuttal and about **1:00 per contention** in the second. Responding to one of three arguments should not eat a minute of a short speech.

Check: `python tools/lint_blocks.py file --lay` warns when a card has no plain analytic after it or an analytic reads like an AI label.

## Technical judges (flow judges, circuit-style)

What they respond to: precise structure, labeled arguments, line-by-line coverage, efficient evidence, explicit weighing.

**Rules for tech files:**

1. Numbered answers and clear signposts; shorthand like "extend," "turn," "outweighs" is fine.
2. Analytics can be short and technical: link/impact language is expected.
3. More answers per argument (layered "even if"), each with its card.
4. Explicit weighing in the rebuttals: probability, magnitude, timeframe, reversibility (`speeches/rebuttal/PROTOCOL.md`).
5. Cards can be denser; read only the key words and rely on the tags.

## Mixed judges

Open each argument in plain language (one sentence), then give the layered technical answers. Keep the plain sentence after the key cards.

## What does not change

- Quotes are verbatim and sourced (`integrity.md`).
- Tags state the claim the card supports.
- Analytics never invent numbers or stand in for cards.
- The honest "Before you read these" caveats list is still delivered.

See `examples/good-vs-bad/analytics.md` for side-by-side lay and tech versions of the same block.
