# What a good block file looks like

> Note for the maintainer: the walkthrough below quotes short snippets from the real files in `reference/`. Before making this repo public, replace them with fictional snippets (like `examples/`) or delete this note's source material along with `reference/`.

Read this before building a block or frontline file. It is based on real working files in `reference/` and on a test where an agent following an earlier version of the toolkit produced files that were not good enough.

## The problem this fixes

A test run produced two files that followed the old instructions and still came out wrong:

| What the agent did | Why it fell short |
|--------------------|-------------------|
| An "A2 block" made only of analytics ("Extend Smith 25: ...") with no cards in it | A block is read from during the round. If the cards are not in the file, the speaker has nothing to read. The "extend" rule belongs to cards already read in a speech, not to blocks. |
| Frontlines with one card per response and no statement of what the opponent argued | No context for the reader: what is the opposing argument, what is the overview answer, and how do the cards connect back to the resolution? |
| Several cards cut as a single sentence (entirely highlighted, no text around it) | The judge cannot see what the author said before and after. |
| Block-level structure missing: no "Aff Argument:" line, no numbered answers, no closing link or turn | The speaker cannot find or reorder answers in the round. |

`python tools/lint_blocks.py` and `python tools/lint_cards.py` now catch these. On the agent's files they reported 6 and 7 block errors and 2 thin cards; on the real example blocks they report no errors.

## The shape of a good block

From `reference/example-blocks/example-blocks-excerpt.docx` (about 6,000 words from a real team blocks file; open it in an editor that supports Verbatim-style formatting):

```
AT: Data Centers Raise Household Electricity Bills                  <- Block (Heading 3)
Aff Argument: Data centers drive up utility costs, so families pay more.   <- states their argument
1. Empirically, more demand has LOWERED prices. More electricity on the same wires
   spreads fixed costs over more customers.                         <- overview answer (Analytic)
2. Berkeley Lab: load growth helped DEPRESS electricity prices...   <- Tag (specific argument sentence)
   Howland 25 [Ethan Howland, Senior Reporter, Utility Dive, ... EXCERPT https://... ] DOA: ...
   Generally, load growth helped depress electricity prices ...      <- card: cite, then body
3. Data centers aren't to blame — one study links them to LOWER rates...   <- Tag
   Huddleston 26 [...]                                              <- cite
   <context>... it's far from clear that data centers are to blame ...     <- card
4. Hyperscalers have committed to pay their own way ...              <- Tag + card
5. States are locking it in — large-load tariffs ...                 <- Tag + card
6. A moratorium doesn't lower any bill. Existing data centers and the grid upgrades
   already built stay on the rate base...                           <- closing analytic: link/turn
```

What to copy:

1. **The opposing argument is stated first**, in one sentence, so everyone knows what is being answered.
2. **A numbered overview answer** comes before the evidence.
3. **Every tagged answer has a card directly under it**, and the tags are full argument sentences with their specifics (numbers, names), not labels.
4. **Cites are complete** and mark excerpts (`EXCERPT` before the URL is a common convention).
5. **Cards are as long as they need to be**, often just a few sentences, with a small amount of unread text on the sides and only the key words read. Cases use longer cards (see `core/cutting-rules.md`).
6. **The block ends with an analytic** that ties the answer back to the resolution or turns the argument.
7. **Numbering runs through the whole block**, mixing analytics and tagged cards, so the speaker can say "number four."

## Checks before delivering

```bash
python tools/verify_quotes.py file.md --strict   # card text is verbatim from the saved source
python tools/lint_cites.py file.md               # cites complete
python tools/lint_cards.py file.md               # no card is a lone highlighted sentence
python tools/lint_blocks.py file.md              # blocks have real cards and the right shape
```

## Reference material

See `reference/README.md`. It holds an excerpt of real blocks and two real opposing files for studying structure and style. Study the structure; do not copy their evidence into another project.
