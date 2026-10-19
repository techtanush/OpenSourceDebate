# What a good block file looks like

Read this before building a block or frontline file. It is based on how strong team files are built and on a test where an agent following an earlier version of the toolkit produced files that were not good enough.

## The problem this fixes

A test run produced two files that followed the old instructions and still came out wrong:

| What the agent did | Why it fell short |
|--------------------|-------------------|
| An "A2 block" made only of analytics ("Extend Smith 25: ...") with no cards in it | A block is read from during the round. If the cards are not in the file, the speaker has nothing to read. The "extend" rule belongs to cards already read in a speech, not to blocks. |
| Frontlines with one card per response and no statement of what the opponent argued | No context for the reader: what is the opposing argument, what is the overview answer, and how do the cards connect back to the resolution? |
| Several cards cut as a single sentence (entirely highlighted, no text around it) | The judge cannot see what the author said before and after. |
| Block-level structure missing: no "Aff Argument:" line, no numbered answers, no closing link or turn | The speaker cannot find or reorder answers in the round. |

`python tools/lint_blocks.py` and `python tools/lint_cards.py` now catch these. On the agent's files they reported 6 and 7 block errors and 2 thin cards; on the fictional example blocks they report no errors.

## The shape of a good block

This is the shape (fictional topic):

```
AT: Downtown Car Ban Hurts Retail                                  <- Block (Heading 3)
Neg Argument: A ban drives shoppers away, so downtown stores lose sales.   <- states their argument
1. Sales held steady in most cities after a ban.                    <- overview answer (Analytic)
2. <Tag: a full argument sentence with its specifics>               <- Tag
   Author 25 [credentials, date, title, publication. URL] DOA: ...  <- cite
   <context> ==key words read== <context>                           <- card
3. <next tagged answer with its own card>
4. <closing analytic that links back to the resolution or turns it>
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

A second test run built a constructive with three contentions. It had about **one or two cards per contention** and 21 analytic paragraphs, several over 100 words. Each contention argued a direction ("fewer injuries," "cleaner air," "commerce can adapt") from a single study, and explained its limits at length. What was missing:

| Missing | Why it matters |
|---------|---------------|
| **Uniqueness**: no card showing how big the problem is now | The judge has no baseline; "fewer injuries" from what? |
| **A link chain**: no card for each causal step | A mechanism written as prose is an assertion the opponent can simply deny |
| **Impact with a number and a timeframe** | "Fewer injuries" is a direction, not a weighable impact |
| **Solvency**: no card showing the plan works as implemented | The case argues benefits but not that this plan delivers them |
| **Cards instead of essays**: long analytics doing the evidence's job | Analytics connect cards; they are not evidence. Cards first. |
| **Aff solvency**: nothing showing the *resolution itself* would cause the impact to fall | An Aff that proves a big problem but not that its resolution fixes it has not made the case |

A strong contention carries roughly six to eight cards: the problem now, how fast it is growing, the key scale number, the mechanism, the consequence, the terminal impact, and solvency, with only the key words of each card read. The target shape (see `examples/example-case.md`, a fictional contention):

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

Every arrow is a card. On the Aff the contention ends with a `Solvency:` analytic showing the resolution itself causes the impact to fall. Read `core/argument-structure.md` for the standard and for how impact framing (in the constructive) differs from head-to-head weighing (in the rebuttals).

## Does it flow? (the cards must add up)

Good cards are necessary, not sufficient. Before delivering, run `python tools/tag_story.py file` and read only the output as a judge would, saying "which means..." between tags. The standard is in `core/logic-flow.md`: each tag follows from the last, the numbers and scope fit across cards, nothing contradicts, and the contention ends in solvency for the resolution.

## Checks before delivering

```bash
python tools/verify_quotes.py file.md --strict   # card text is verbatim from the saved source
python tools/lint_cites.py file.md               # cites complete
python tools/lint_cards.py file.md               # no card is a lone highlighted sentence
python tools/lint_blocks.py file.md              # blocks have real cards and the right shape
python tools/lint_case.py file.md                # contentions are chains: chain map, a card for every step
```
