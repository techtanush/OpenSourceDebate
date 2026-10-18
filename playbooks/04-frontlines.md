# Playbook 04: Build Frontlines for Your Own Case

**Goal:** prepared defense of each contention against the responses the opponent is likely to make, with new evidence where needed, in the order the file will be used.

**Read first:** `core/file-organization.md`, `speeches/frontlines/PROTOCOL.md`, `core/argument-structure.md`.

## Inputs

- **Our case file** (the contentions, chain maps, and cards actually read). This is the context: read it first.
- The likely opposing responses (opposing files you have, circuit arguments, your own weakness list).
- Judge type and times (`team.yaml`).

## Steps

1. **Load our case.**

```bash
python tools/inspect_docx.py our-case.docx            # outline and style stats
python tools/inspect_docx.py our-case.docx --cards    # every card: cite, highlighted text
python tools/tag_story.py our-case.docx               # the chain as a story
```

   Record, per contention: the chain, the cards that were read, and the claims the judge has already heard.
2. **List the likely responses** for each contention, each as a fair one-sentence statement, strongest first. Include responses to each **step** of the chain (UQ, link, IL, impact, solvency).
3. **For each response, write the defense:**
   1. Decide the answer type (`core/refutation-guide.md`): our own evidence says otherwise, no link, non-unique, turn, mitigation, or weighing.
   2. **Extension vs. new card:** a card the user already read becomes a short `Extend <Card> from our case: <key point and numbers>` analytic, not a re-pasted card. Everything else is a **full new card**.
   3. Research new cards (`research-guide.md`); new evidence is allowed in frontlines.
   4. Add the plain analytic after cards for lay judges.
4. **Structure the file** (`file-organization.md`):

```
Hat   : <Contention>
  Tag + cite + card : our argument and the card we read
  Block : AT: <their response>
    <Opponent> Argument: <their response, stated fairly>
    1. overview answer
    2..N tagged answers, each with its card (or an Extend analytic for read cards)
    closing line: why it still stands if dropped
```

5. **Prepare for turns.** For each contention ask whether the opponent can turn it; write the answer in advance.
6. **Check flow** with our case (`logic-flow.md`): the frontline must not contradict anything we said in the constructive.
7. **Build and check:** `build_docx.py`, `verify_quotes.py --strict`, `lint_cites.py`, `lint_cards.py`, `lint_blocks.py [--lay]`, `speech_timer.py`.
8. **Report** unanswerable responses honestly, plus weak or unverified items.

## Done when

- [ ] Each contention has at least its top three likely responses answered, including responses to the weakest chain step.
- [ ] Constructive cards appear only as short extensions; every new answer is a full card.
- [ ] Each block opens with the opponent's response stated fairly and has a one-line "if dropped" claim.
- [ ] Nothing contradicts our case.

## Common mistakes

- Writing attacks on their case (that is a block).
- Re-pasting cards the judge already heard.
- Defending only the impact while the link is the weak step.
- Guessing what was read: if the case file isn't available, ask, or cut a fresh card.
