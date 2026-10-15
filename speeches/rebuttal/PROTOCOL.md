# Rebuttal Protocol

Used for: answering the opponent's case and defending your own after the constructives. Works for first and second rebuttals; adjust the time budget from `formats/`.

Read first: `core/integrity.md`, `core/cutting-rules.md`.

## Inputs to collect

- The opponent's case, as text or a file. If it is a PDF or .docx, extract the text and keep a list of every argument, card, and source.
- Your own case (what you must still defend).
- The time limit and wpm (`formats/`).
- What the opponent actually said in the round, if you have a flow. Never answer an argument they didn't make.

## Step 1: Map their case

List every argument as: `Name: claim -> evidence (author, year, source type) -> impact`. Note:

- Which positions are on-case vs. off-case (disadvantages, counter-plans, frameworks).
- Which cards are central and which are padding.
- Source weaknesses (age, bias, credentials, relevance to the claim).

## Step 2: Find the best answers, in this order

1. **Their own evidence.** Re-read their cards for lines that help you: concessions, qualifiers, scope limits, weak links, internal contradictions between their positions. Quote them back (verbatim, with the cite). This is usually the most effective response.
2. **No link / non-unique / no impact.** Show the resolution doesn't cause their harm, the harm happens anyway, or it doesn't matter.
3. **Turns.** Show their own argument supports your side, with evidence.
4. **Mitigation.** Reduce the size or probability.
5. **Source attack.** Only with a concrete problem (date, conflict of interest, topic mismatch). Don't attack a source without a reason.

## Step 3: Structure

```
Overview        1-3 sentences: how the judge should decide, plus any cross-case contradictions
Line-by-line    one block per opposing argument, in their order
  Label         "Off 1: X", "C1: Y"
  Answers       numbered, strongest first, each 1-3 sentences
  Cards         read only what you need; extend earlier cards as short analytics
Weighing        probability / magnitude / timeframe / reversibility, each with a reason
Voting issues   (if your format's last rebuttal) 2-3 crisp reasons
```

Open with a **cross-case contradiction** if one exists (two of their cards that can't both be true). It can take out several arguments at once.

## Flow check

Before delivering, read your answers in order as the judge would hear them (`core/logic-flow.md`). Each answer should make the decision easier, answers within a block must not contradict one another, and the overview, line-by-line, and weighing should tell one story.

## Step 4: Evidence

- Use evidence you already have; research new cards only where a gap is serious (`core/research-protocol.md`).
- **Do not re-read cards from your constructive.** Write "Extend [Card] from our case: [key point and numbers]."
- Quote the opponent's cards by their cite and a short verbatim excerpt. Check the text against the source you have for them.

## Step 5: Fit the time

Estimate with `tools/speech_timer.py rebuttal.docx --wpm <rate> --limit <seconds>`. If over, cut the weakest answers first, not the weighing.

## Quality checks

- [ ] Every opposing argument is addressed or deliberately conceded.
- [ ] Each answer has a reason and, where possible, evidence.
- [ ] Their own cards are used wherever they help.
- [ ] No fabricated or paraphrased quotes (`integrity.md`).
- [ ] Impacts are weighed, not just listed.
- [ ] Anything unverified is flagged to the user.

## Output

- `rebuttal.md` / `rebuttal.docx`.
- A short "if they respond with X, answer Y" list (feeds `speeches/frontlines/`).
