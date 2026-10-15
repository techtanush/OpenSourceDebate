# Cutting Rules

How to turn a source into a card. Follow `integrity.md` first.

## Step by step

1. **Know the claim.** Write the tag first (one sentence). You are looking for the author's words that prove exactly that.
2. **Read the whole source.** Don't cut from the first paragraph that sounds right. Find the author's strongest, clearest passage, and check the rest of the piece doesn't contradict it.
3. **Pick the excerpt.** Start at a natural beginning (a topic sentence or the start of the reasoning) and end where the thought ends. Keep the sentences that make the claim *and* any that supply the reason or evidence.
4. **Mark it up** with three levels (below).
5. **Cite it** (`cite-format.md`).
6. **Verify** with `tools/verify_quotes.py`, and check context with `tools/lint_cards.py`.

## How much of the source to include (context)

A card is **not** just the one sentence you want to read. Include enough of the surrounding text that a judge or opponent can see what the author was talking about. How much depends on where the card is used. These figures come from measuring real team files (143 block/frontline cards, 53 case cards):

| Where the card is used | Typical body | Typical share read | Unread context |
|------------------------|--------------|--------------------|----------------|
| Blocks / frontlines | a few sentences up to a short paragraph (median ~170 words; many are 50-100) | ~10-30% | a sentence or two before and after |
| Case / constructive | 350-700 words (median ~500) | ~5-12% | a paragraph or more, especially after the read text |

Rules:

1. **Start where the point starts** (the setup sentence, the definition, the claim being answered) and **end where the thought ends**, including any qualification the author attaches. Do not drop a qualifier just to shorten a card.
2. **Keep the read text sparse.** Read only what proves the tag. In a block, a card that is entirely highlighted, or that has no unread text on either side, is almost always cut too thin.
3. **Cases need more context than blocks.** A constructive card that is one paragraph or less is probably too thin; take the surrounding paragraphs.
4. **Context comes from the source only**, contiguous and in order (`integrity.md`). Never add your own words inside the card body; put explanation in an Analytic paragraph.
5. `python tools/lint_cards.py file --profile block|case` flags the extremes. It is a warning, not a quality score: a card can pass and still be a poor card. Use your judgment, and explain any deliberate exception (a one-sentence source, a table value) in your notes.

## The three levels

| Level | What goes here |
|-------|----------------|
| **Read** (highlight + underline) | The shortest set of words that, read aloud, makes the claim and is grammatical. |
| **Underline** | Supporting words you may read if there's time, or that a judge could scan on the page. |
| **Unread** (8pt) | Everything else in the excerpt: context that stops the card from being "clipped." |

Highlighting must be a subset of the underlining, which must be a subset of the excerpt.

## Highlighting rules

- **Read aloud, it must sound like a sentence.** Skipping words is fine as long as the result is grammatical and means what the author meant.
- **Don't change the meaning.** Never highlight around a "not," "may," "could," "some," or "if" in a way that makes the claim stronger than the author's.
- **Keep the numbers and names** that carry the argument (`44%`, `by 2030`, the institution).
- **Highlight in contiguous chunks** where you can. Highly chopped, word-by-word highlighting is hard to read and invites a "clipping" challenge.
- **Don't highlight your own words.** Only the author's.

## Editing the text

- `...` marks text you removed *between* highlighted words when the omission is large.
- `[word]` marks a word you changed or added for clarity (`[the Aff]`, `[increases]`). Keep these rare, and never change the meaning.
- Do not fix the author's typos silently. If necessary, leave them.

## Common errors that lose rounds

| Error | Why it's a problem |
|-------|--------------------|
| Tag claims more than the text says | Opponent reads the card and shows the gap |
| Highlight omits a qualifier | "Cutting out of context" |
| Excerpt starts or ends mid-argument | Looks like hiding the author's real conclusion |
| Paraphrase presented as a quote | Fabrication |
| Old or irrelevant source | Easy to answer |
| Cite is missing credentials or date | Judge can't weigh it |

## What a good card looks like

- The tag says exactly what the highlighted words say.
- The read portion is 2-4 clear sentences' worth, not a paragraph of fragments, inside a body with real context before and after it (`lint_cards.py` passes).
- The cite lets anyone check it in 30 seconds.
- `verify_quotes.py` passes and `lint_cites.py` is clean.

## Counting reading time

`python tools/speech_timer.py cards.docx --wpm 250` counts only highlighted text (and headings, analytics), because that is what gets spoken. Use it to check a block fits its time.
