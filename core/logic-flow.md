# Logic Flow: Making the Cards Add Up

Good individual cards are not enough. A case, a DA, or a block wins when the cards **read as one story**: each step follows from the one before, the numbers fit each other, nothing contradicts, and the whole thing ends at the ballot. This page is the standard for that, and how to test it.

## The four levels of flow

| Level | Question | How to check |
|-------|----------|--------------|
| **Card to tag** | Does the highlighted text say exactly what the tag claims, no more? | Read the tag, then only the highlighted words. If a gap, change the tag or the card. |
| **Tag to tag** (within a contention) | Does each tag follow from the one before it? | The **tag-story test** below. |
| **Contention to contention** (within the case) | Do the contentions support one thesis and not contradict each other? | The case-level read-through below. |
| **Case to ballot** | Does the end of the case tell the judge why this means they should vote for you? | Conclusion and impact framing; leave head-to-head comparison to the rebuttals. |

## The tag-story test

Run it before delivering any case, DA, or block:

```bash
python tools/tag_story.py case.md        # or a .docx
```

It prints the chain map and every tag in order with its card, the step it fills, and the numbers it carries. Read only that output, top to bottom, as the judge would hear it, and ask at every arrow:

1. **Does this follow from the one before?** Say "which means..." between the tags. If the sentence doesn't work, a step is missing or out of order.
2. **Is every jump covered by a card?** If you would need a paragraph of explanation to get from tag 3 to tag 4, you are missing a card.
3. **Do the tags escalate cleanly?** The usual order is: the problem now, how fast it is growing, the mechanism, the consequences, the final impact, then proof the resolution fixes it. Do not put the impact before the judge knows the problem exists.
4. **Does it end where it should?** On the Aff, the last step of every contention is solvency: the resolution itself causes the impact to fall. If the chain ends on an impact, it is unfinished.

## Numbers must fit

Cards from different sources only combine if their numbers and scopes line up. Check:

- **Scale:** the size of the problem in the uniqueness card should be consistent with the size of the impact. If the UQ is one city and the impact is the whole country, say how the scale-up works and add a card for it.
- **Scope and place:** a study of London street closures is not a prediction for a downtown ban in another city. Say what transfers, and add an independent second card.
- **Time:** make sure the periods are comparable (an annual figure against a monthly one; a forecast to 2030 against a measurement from 2023).
- **Units and definitions:** "injuries" vs. "serious injuries," "deaths" vs. "deaths and serious injuries." The terms in consecutive tags should match, or the shift should be stated.
- **Analytics can't invent numbers.** Any number in an analytic must appear in a card of that contention. `tools/lint_case.py` warns when it doesn't.

## Contradictions to avoid

- **Between contentions:** one contention says transit is strong enough to replace cars, another says transit is failing and needs the plan. Pick one story or reconcile them explicitly.
- **Between answers in a block:** answers can be layered ("no link; even if it links, it is small; and it is a turn"), but they must not undercut each other. If one answer concedes something another denies, say so ("even if you grant X...").
- **Between card and analytic:** an analytic must never claim more than its card supports.
- **Between the cards themselves:** if two of your cards disagree (different numbers for the same thing), pick the better source, note the difference, and drop the weaker card or reconcile it.

## Signposting and transitions

Short signposts help the judge follow the chain: "Scenario 1 is the economy," "That's the link," "And solvency." Make them **tags** (as the real files do), not paragraphs. They cost a second to read and make the story easy to flow.

## Case-level read-through (before delivering a whole case)

1. Read the **introduction, plan, and every contention's chain map** only. Do they tell one story about why the resolution is a good idea?
2. Check the **order of contentions**: strongest and most intuitive first, unless time requires otherwise.
3. Check that **each contention's solvency** points back to the same resolution text in the plan. If the plan has provisions (phase-in, exceptions, funding), each solvency card should be about a plan that has them.
4. Check that the **conclusion** names the contentions in the same terms the tags used.
5. Scan for **repeated evidence**: the same source carrying two different steps is fine if it supports both; the same claim carded twice wastes time.

## Flow in blocks and rebuttals

- **Blocks:** the numbered answers should run from the strongest and cleanest claim to the more specific ones, with the closing analytic tying the answer back to the resolution or turning the argument. Number them continuously so the speaker can say "number three."
- **Rebuttals:** open with an overview that tells the judge how to decide, answer line by line in the opponent's order, then weigh. Each answer should make the judge's decision easier, not just contradict a card. See `speeches/rebuttal/PROTOCOL.md`.

## What the tools check, and what they don't

| Automated (`lint_case.py`, `tag_story.py`) | Judgment (you or the agent, using this page) |
|--------------------------------------------|-----------------------------------------------|
| Chain steps in logical order | Whether each step really follows from the last |
| Chain map names match the cards, in order | Whether the numbers and scopes fit |
| Tag labels match the chain map | Whether contentions contradict each other |
| Numbers in analytics appear in a card | Whether the whole case reads as one story |

A passing lint is necessary, not sufficient. Always run the tag-story test and read it as a judge would.


## Match your own case

Before delivering blocks, frontlines, or backlines, read them against the team's own constructive cases (the ones the team actually reads in round). Check three things:

1. **No card contradicts a constructive.** If the constructive says nearby streets get faster, a block must not use a card saying they get slower. If a card's headline says the opposite of the team's thesis, even when the quoted lines are safe, swap it.
2. **Choose the story that fits both.** When two true stories exist (for example, traffic moves to nearby streets vs. traffic disappears), use the one the constructive uses, and keep the other out of every file the team will read from.
3. **Strengthen, never weaken.** Fix a conflict by finding a better card for the same point, not by dropping the point.
