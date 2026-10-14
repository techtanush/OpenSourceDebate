# Frontlines Protocol

**Frontlines** = prepared defense of **your own** arguments against the responses the opponent is likely to make. (Prepared answers to *their* arguments are "blocks" or "A2s," see `speeches/blocks/`.)

Read first: `core/integrity.md`, `core/cutting-rules.md`.

## Inputs to collect

- Your case file (contentions, tags, cards).
- A list of the likely responses to each contention. Get these from: the opposing case if you've seen it, arguments seen on the circuit, and the weak points you find yourself ("what would I say against this?").
- Time and wpm (`formats/`).

## Process

1. **Read the constructive text first.** Note which cards you already read in your speech. They are "extendable" and must not be re-read in full.
2. **For each contention, list the opposing responses**, from strongest to weakest, each in one line. Use their wording.
3. **For each response, write your answer:**

```
Block (Heading 3):   "C1 - [Response being answered]"
Tag (Heading 4):     the answer in one sentence
Card or Analytic:    new evidence, or a short extension of a constructive card
```

4. **Order the answers** by how directly they deal with the response: usually (a) no-link or non-unique, (b) your best card, (c) a turn if you have one, (d) a weighing line.
5. **Mark extension vs. new evidence.** New evidence is allowed in frontlines, and research it with `core/research-protocol.md`.
6. **Add a "terminal defense" line** at the end of each block (a one-sentence claim that stands if everything else is dropped).

## Rules specific to frontlines

- **Never re-paste a constructive card in full.** Write an Analytic: `Extend [Card] from our constructive: [key point + numbers].` Reading it again wastes speech time and the judge has already heard it.
- **Defend, don't attack.** Attacks on the opposing case belong in blocks and rebuttal files.
- **Prepare for turns.** For each contention, ask: could the opponent turn this? If so, write the answer before the round.
- **Keep answers short.** A frontline answer should be 20-40 seconds to read aloud.
- **Disclose gaps.** If you have no good answer to a response, say so in the notes instead of papering over it.

## File structure

```
Pocket  : "<Side> Frontlines"
Hat     : each contention or argument being defended
Block   : each opposing response
Tag     : your answers (cards, with extension analytics between them)
```

Build with `tools/build_docx.py`. Check read time with `tools/speech_timer.py`.

## Quality checks

- [ ] Every contention has at least its top three likely responses answered.
- [ ] Constructive cards appear only as Extend analytics.
- [ ] New cards verified with `tools/verify_quotes.py` and `lint_cites.py`.
- [ ] Each block has a one-line "if dropped" claim.
- [ ] Unverified quotes or weak sources are flagged.
