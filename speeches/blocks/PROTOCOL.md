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

## File shape

```
Block   : "A2: <Argument>"
  Analytic : one-line summary of the answer package
  Tag      : "1. <answer sentence>"
  Card(s)  : evidence (verified)
  Analytic : why it wins / how to weigh it
  Tag      : "2. <answer>"
  ...
  Analytic : "If they say X, say Y."
```

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
- [ ] All cards verified (`verify_quotes.py`), cites complete (`lint_cites.py`).
- [ ] Block fits its time (`speech_timer.py`).
- [ ] Unverified items flagged.
