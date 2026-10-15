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

## What a good contention looks like (cases and DAs)

A second test run built a 1AC with three contentions. It had about **one or two cards per contention** and 21 analytic paragraphs, several over 100 words. Each contention argued a direction ("fewer injuries," "cleaner air," "commerce can adapt") from a single study, and explained its limits at length. What was missing:

| Missing | Why it matters |
|---------|---------------|
| **Uniqueness**: no card showing how big the problem is now | The judge has no baseline; "fewer injuries" from what? |
| **A link chain**: no card for each causal step | A mechanism written as prose is an assertion the opponent can simply deny |
| **Impact with a number and a timeframe** | "Fewer injuries" is a direction, not a weighable impact |
| **Solvency**: no card showing the plan works as implemented | The case argues benefits but not that this plan delivers them |
| **Cards instead of essays**: long analytics doing the evidence's job | Analytics connect cards; they are not evidence |

For comparison, the real constructives in `reference/` carry roughly six to eight cards per contention: the problem now, how fast it is growing, the key scale number, the mechanism, the consequence, the terminal impact, and solvency. `python tools/lint_case.py` on the agent's case reported 6 errors and 2 warnings; `python tools/lint_case.py examples/example-case.md` reports none.

The target shape (see `examples/example-case.md`, a fictional contention):

```
Contention 1: Downtown car traffic is injuring and killing people
Chain: UQ (...) -> TREND (...) -> LINK (...) -> IL (...) -> IMPACT (...) -> SOLVENCY (...)
UQ        card: the downtown is <2% of the land but a third of walking injuries (412 injured, 9 killed)
TREND     card: car entries +17%, injuries +22% since 2019, forecast to keep rising
LINK      card: restrictions cut injuries 36% across eleven cities, none shifted next door
IL        card: each serious injury costs ~$187,000, ~41% paid by public programs
IMPACT    card: 7,310 urban pedestrian/cyclist deaths, a four-decade high; >$140B a year
          framing: who it falls on, timeframe, irreversibility (one or two sentences)
SOLVENCY  card: a city that did it with a phase-in cut core injuries 40%
```

Every arrow is a card. Read `core/argument-structure.md` for the standard and for how impact framing (in the constructive) differs from head-to-head weighing (in the rebuttals).

## Checks before delivering

```bash
python tools/verify_quotes.py file.md --strict   # card text is verbatim from the saved source
python tools/lint_cites.py file.md               # cites complete
python tools/lint_cards.py file.md               # no card is a lone highlighted sentence
python tools/lint_blocks.py file.md              # blocks have real cards and the right shape
python tools/lint_case.py file.md                # contentions are chains: chain map, a card for every step
```

## Reference material

See `reference/README.md`. It holds an excerpt of real blocks and two real opposing files for studying structure and style. Study the structure; do not copy their evidence into another project.
