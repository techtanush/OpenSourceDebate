# Blocks (A2 / AT Files) Protocol

A **block** is a prepared set of answers to a common opposing argument. You write it before the round and read from it in rebuttal. Files are organized by the *argument you are answering*.

Read first: `core/integrity.md`, `core/cutting-rules.md`, `core/research-protocol.md`.

## Inputs

- The opposing argument to answer (as the other side would state it, in one paragraph).
- Your side and case, so your answer doesn't contradict it.
- Time and wpm.

## Process

1. **State the argument fairly.** Write it as the opponent would, including the best evidence they'd read. A weak statement of their argument gives you a weak block.
2. **Find answers** in this order:
   - **Takeouts:** no link, non-unique, no impact.
   - **Turns:** the argument helps your side.
   - **Mitigation:** reduces size/probability/timeframe.
   - **Source indicts:** specific, evidenced problems with their likely sources.
3. **Research** each answer (`core/research-protocol.md`). Prefer sources the opponent can't dismiss easily: neutral agencies, peer-reviewed work, their own cited authors.
4. **Cut cards** and add short analytics. Each answer gets: a tag, a card or analytic, one line explaining why it wins.
5. **Order** answers from strongest to weakest so you can read the first N that fit the time.
6. **Write the "if they say..." follow-ups** for the most likely replies.

## Block anatomy (follow this)

This is the structure used in the example blocks in `reference/example-blocks/`. A block is read from during the round, so it is **self-contained**: it states the argument, gives the answers, and **contains the actual cut cards**.

```
Block (Heading 3)   "AT: <opposing argument>"
Analytic            "<Opponent> Argument: <fair one-sentence statement of what they say>"
Analytic            "1. <overview answer: the strongest short claim, often an empirical or no-link point>"
Tag + cite + card   "2. <answer as a full argument sentence with its specifics>"
Tag + cite + card   "3. <next answer>"
  ... (2-5 cards, strongest first)
Analytic            "N. <closing link: why the resolution/plan does or doesn't cause their claim, or a TURN>"
```

Rules:

1. **Open with the opposing argument**, stated the way they would say it ("Aff Argument: ...", "Neg Argument: ...").
2. **Every tagged answer has its own card.** Tag (the answer as a specific argument sentence), then the cite, then the card body with its surrounding context and sparse read text (`core/cutting-rules.md`). A Tag with no card under it is an error.
3. **Analytics sit between and around cards. They never replace them.** Do not write "Extend X" or summarize a card that lives in another file. "Extend" is only for a card the debater already read in an earlier speech.
4. **Number the answers** across tags and analytics (1, 2, 3...), so the speaker can say "number three."
5. **Close with an analytic** that ties the block back to the resolution or turns the argument.
6. **Add a source note** (Analytic) only where the source has a weakness the debater must be ready to answer.
7. Check the **flow**: read the numbered answers in order (`python tools/tag_story.py file`); they should run from the cleanest claim to the specifics, not contradict each other, and close with a link back or a turn (`core/logic-flow.md`).
8. Check with `python tools/lint_blocks.py file` (structure) and `python tools/lint_cards.py file` (cards cut too thin).

A starter file is in `templates/block-skeleton.md`; a worked fictional example is `examples/example-cards.md`.

## Good blocks

- Have 3-6 answers, with at least one strong takeout and one turn if possible.
- Lead with an answer that doesn't depend on any other answer.
- Use the opponent's own evidence where possible.
- Are tight: the whole block can be read in under two minutes, and the first answer alone is usable in 20 seconds.
- Note weaknesses ("this card is from a trade group; pair with X").

## Common mistakes

- Answering a weaker version of the argument.
- Reading a card that doesn't say what the tag says.
- Cards from sources that are easy to dismiss with no backup.
- No weighing: winning the point doesn't matter if it's small.
- Too long to read in the time.

## Quality checks

- [ ] Opposing argument stated fairly at the top.
- [ ] Answers ordered strongest first, each with a reason.
- [ ] All cards verified (`verify_quotes.py`), cites complete (`lint_cites.py`), context present (`lint_cards.py`).
- [ ] Every numbered answer contains its own cut card (no card-less answers, no "Extend" for unread cards).
- [ ] Block fits its time (`speech_timer.py`).
- [ ] Unverified items flagged.
