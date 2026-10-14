# Case (Constructive) Protocol

Used for: the first speech of a side (constructive). Aff builds a case for the resolution; Neg builds a case, disadvantages, or counter-positions against it.

Read first: `core/integrity.md`, `core/card-anatomy.md`, `core/cutting-rules.md`, and the speech time/word budget in `formats/<your-format>.yaml`.

## Inputs to collect

- The resolution (exact wording) and the side.
- The format and time (`formats/`), and the target words-per-minute.
- Any existing files or earlier cases (inspect them with `tools/inspect_docx.py` to match style).
- The audience: technical (flow judges) or lay (parent/community judges). This changes jargon and density, not honesty.

## Structure

A typical constructive, adapt to format:

1. **Introduction**: 1-3 sentences that frame the stakes.
2. **Framework / burden** (if your format uses it): what the judge should weigh.
3. **Contentions** (2-3): each follows the chain below.
4. **Conclusion**: one sentence that ties the contentions to the ballot.

### Contention chain

```
Claim            one-sentence tag of the contention
Uniqueness       what is true now (evidence)
Link             why the plan/resolution (or the Neg position) changes it
Internal link(s) middle steps, only as many as needed
Impact           the final benefit/harm and its size, plus who is affected
Solvency         (Aff) why the resolution actually fixes it
```

Every step needs a card or a clear analytic. A chain that is longer than 4 steps is fragile: shorten it or add evidence.

## Writing the case

1. **List the strongest arguments** for the side. Use the research protocol to find evidence for each.
2. **Order by strength and time.** Lead with the contention you most want the round decided on.
3. **Cut cards** to be read: highlight only what supports the tag, and keep the read text within the word budget (`tools/speech_timer.py`).
4. **Write analytics** (dark blue) between cards: 1-2 sentences connecting card to claim.
5. **Pre-empt the top response** inside the speech if time allows (a short "even if").
6. **Check time.** Run `speech_timer.py case.docx --wpm <rate> --limit <seconds>`.

## Neg cases and off-case positions

- **Disadvantage (DA):** shell with uniqueness, link, impact. State the link in the Aff's own terms ("The resolution requires X; X causes Y").
- **Counter-plan / alternative:** must be competitive (can't be done alongside the resolution) and solve the Aff's harms; include evidence that it avoids the Aff's costs.
- **Case takeouts:** short, evidenced answers to each Aff contention to read alongside off-case positions.
- Note which Neg positions the Aff can turn, and prepare the response.

## Quality checks

- [ ] Each tag is supported by the highlighted words (`verify_quotes.py` and a human read).
- [ ] Cites are complete (`lint_cites.py`).
- [ ] No card is read twice; extensions later should be short analytics (see `speeches/frontlines/PROTOCOL.md`).
- [ ] The speech fits the time limit at your rate.
- [ ] Every impact is weighed against the likely opposing impact.
- [ ] A "before you read these" list is delivered with the case (`integrity.md`).

## Output

- `case.md` (spec) and `case.docx` built with `tools/build_docx.py`.
- A one-page summary: contentions, key cards, expected responses.
