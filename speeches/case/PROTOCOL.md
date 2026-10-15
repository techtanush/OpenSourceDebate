# Case (Constructive) Protocol

Used for: the first speech of a side (constructive). Aff builds a case for the resolution; Neg builds a case, disadvantages, or counter-positions against it.

Read first: `core/integrity.md`, `core/argument-structure.md` (the link-chain standard, which this protocol depends on), `core/card-anatomy.md`, `core/cutting-rules.md`, and the speech time budget in `formats/<your-format>.yaml`.

## Two rules above all

1. **Cards first.** Evidence does the arguing. Analytics only connect cards, and on the Aff their main job is to show the **resolution** would actually produce the impact (the `Solvency:` sentence). Do not write paragraphs of explanation where a card should be.
2. **On the Aff, every impact needs solvency.** If a contention claims a harm or benefit, a SOLVENCY card must show the resolution itself fixes it, and a `Solvency:` analytic must say how. Proving the problem is big is not enough. See `core/argument-structure.md`.

## The main failure to avoid

A case built from **one or two cards per contention** plus long explanatory paragraphs. It reads like an essay with a few citations. A real contention is a **chain of cards**: the problem now, the mechanism that connects the plan to the change, each consequence, the final impact with its size, and proof the plan works. Analytics connect the cards; they never stand in for them. Read `core/argument-structure.md` before you start.

## Inputs to collect

- The resolution (exact wording) and the side.
- The format and time (`formats/`), and the target words-per-minute.
- Any existing files or earlier cases (inspect them with `tools/inspect_docx.py` to match style).
- The audience: technical (flow judges) or lay (parent/community judges). This changes jargon and density, not honesty.

## Structure

A typical constructive, adapted to the format:

1. **Introduction:** 1-3 sentences that frame the stakes.
2. **Plan / resolutional commitments** (Aff, if your format uses a plan): the exact text, with the evidence that its provisions are workable.
3. **Framework / burden** (if your format uses it): what the judge should weigh.
4. **Contentions** (usually 2-3): each is a full chain (below).
5. **Conclusion:** one sentence that ties the contentions to the ballot.

### The contention chain

Each contention follows the parts in `core/argument-structure.md`:

```
Heading         Contention N: <claim in one sentence>
Chain map       Chain: UQ (card) -> LINK (card) -> IL (card) -> IMPACT (card) -> SOLVENCY (card)
Tag + card      UQ:       the problem now, with a number
Tag + card      TREND:    it is getting worse (optional but strong)
Tag + card      LINK:     the mechanism: why the plan changes it
Tag + card      IL:       each consequence, one card per step
Tag + card      IMPACT:   final harm or benefit, with size and timeframe
Tag + card      SOLVENCY: the plan works when implemented
Analytic        Impact: 1 sentence of framing: size, who is affected, timeframe, reversibility
Analytic        Solvency: how the resolution itself causes this impact to fall, tied to the SOLVENCY card
```

### Minimums

- **At least 4 cards per contention**, and one for every step named in the chain map. About 6-8 is typical for a strong contention in the real files in `reference/`.
- **Every step in the chain map has a card.** A step with no card is an assertion; cut the step or find the card.
- **The link is a card.** Do not write it as analytic prose.
- **The impact has a number and a timeframe.**
- **Every Aff contention ends with a `Solvency:` analytic** (1-3 sentences) saying how the resolution causes the impact to fall, supported by the SOLVENCY card. The only other analytics are the chain map and an optional one-line impact framing.
- **Analytics stay a small share of what is spoken** (lint fails above 50% of analytic words plus card-read words, warns above 30%). Do not use a long analytic paragraph where evidence is missing.
- **Hedge honestly, not endlessly.** If a card is an analogy (a different city or a different measure), state the limit in a sentence and add a second, independent card so the chain does not rest on one analogy.

`python tools/lint_case.py case.md` checks these.

## Impact framing vs. weighing

In a constructive, **frame** each impact (size, who is affected, timeframe, reversibility) in a few sentences. Do **not** spend constructive time comparing against arguments the opponent has not made yet; that head-to-head weighing (probability, magnitude, timeframe, reversibility) belongs in the rebuttals and summary speeches (`speeches/rebuttal/PROTOCOL.md`, `speeches/summary-final/PROTOCOL.md`).

## Writing the case

1. **Outline the chains first.** For each contention write the chain map, then list the card you need for each step. Mark the gaps.
2. **Research the gaps** (`core/research-protocol.md`). Look hardest for the link, the impact scale, and solvency; those are the usual holes.
3. **Order contentions by strength** and by the time you have. Lead with the contention you most want the round decided on.
4. **Cut each card** with context and sparse read text (`core/cutting-rules.md`); a constructive card is usually longer than a block card.
5. **Write the connecting analytics** after the cards exist, so each one says what the cards prove, not what you hope they prove.
6. **Check time.** `python tools/speech_timer.py case.docx --wpm <rate> --limit <seconds>`. If over, cut the weakest contention's extra cards, never a required step.

## Neg cases and off-case positions

- **Disadvantage (DA):** use the same chain standard: UQ (things are stable now), link (the Aff causes the trigger), internal links, impact. A DA with one card is a claim.
- **Counter-plan / alternative:** must be competitive and solve the Aff's harms; include evidence that it avoids the Aff's costs.
- **Case takeouts:** short, evidenced answers to each Aff contention to read alongside off-case positions.
- Note which Neg positions the Aff can turn, and prepare the response.

## Quality checks

- [ ] Each contention opens with a chain map and has a card for every step in it (`lint_case.py`).
- [ ] At least four cards per contention; the link, the impact, and the solvency are cards, not analytics.
- [ ] Each Aff contention has a SOLVENCY card and a `Solvency:` analytic showing the resolution itself causes the impact to fall.
- [ ] Analytics are a small share of the speech: cards carry the argument.
- [ ] Each tag is supported by the highlighted words (`verify_quotes.py` and a human read).
- [ ] Cites are complete (`lint_cites.py`) and cards are properly cut (`lint_cards.py --profile case`).
- [ ] No card is read twice; later extensions should be short analytics (see `speeches/frontlines/PROTOCOL.md`).
- [ ] The speech fits the time limit at your rate.
- [ ] Each impact is framed (size, timeframe); comparison against the opponent is left to the rebuttals.
- [ ] A "before you read these" list is delivered with the case (`integrity.md`).

## Output

- `case.md` (spec) and `case.docx` built with `tools/build_docx.py` (add `--draft` for a cutting copy).
- A one-page summary: contentions, the chain map for each, key cards, expected responses.
