# Playbook 03: Build a Blocks Library

**Goal:** prepared, well-organized answers to the arguments you expect, before you know the opponent's case. One block per opposing argument, strongest answers first, ready to merge into a speech-ready file.

**Read first:** `core/file-organization.md`, `speeches/blocks/PROTOCOL.md`, `core/refutation-guide.md`, `core/research-guide.md`.

## Steps

1. **List the arguments to answer.** Sources: the topic's common arguments, the opposing cases you have seen (`reference/`, the user's files), and the weaknesses you found in your own case. Group by topic area (Hats).
2. **Check what exists.** `python tools/library.py index <folder> -o library-index.md` and `python tools/library.py search <folder> <keywords>`. If a block exists for the argument, **add to it**; do not create a duplicate.
3. **For each argument:**
   1. Write the fair one-sentence statement ("Neg Argument: ...").
   2. Write the chain of their argument and mark its weakest steps.
   3. Pick answers: takeouts, turns, mitigation, source indicts, with a **card for each** (`research-guide.md`, section 6). Include at least one answer to the **specific card** they are likely to read (find the likely source first).
   4. Cut the cards with context.
   5. Add the numbered overview answer and the closing link or turn.
   6. For lay judges, add a plain analytic after each card.
4. **Rank the answers** so the first one alone is usable in 20 seconds and the whole block fits in the time you have (`speech_timer.py`).
5. **Add "if they say X, say Y"** for the two most likely replies.
6. **Merge into the right file.** New evidence goes into the library first, then the speech-ready blocks file under its **existing** headings (`file-organization.md`). Keep the team's headings if asked.
7. **Check and build:** `verify_quotes.py --strict`, `lint_cites.py`, `lint_cards.py`, `lint_blocks.py [--lay]`, `build_docx.py`.
8. **Report** gaps (arguments with no good answer), weak sources, and anything unverified.

## Done when

- [ ] One block per argument, no duplicates.
- [ ] Each block follows the anatomy and passes `lint_blocks.py`.
- [ ] Every answer has a card; the best answers address specific cards.
- [ ] The first answer is short and strong; the block fits the time.

## Common mistakes

- Making a second block for an argument that already has one.
- Writing takeouts because specific answers took more research.
- Cards that don't match the tag.
- No closing link back to the resolution.
