# Examples, in the order to study them

Work through these in order. Steps 1-4 are the fictional example (safe to share). Steps 5-6 are real files and are in the private-only `reference/` folder.

## 1. The source

`examples/source-article.txt` is a fictional article. This is what a card is cut *from*: the full text, saved to a file. `verify_quotes.py` checks every card against it.

## 2. The card spec (Markdown)

`examples/example-cards.md` is the file an agent writes. Open it and notice:

- Pocket > Hat > Block headings;
- each Block opens with `> Neg Argument: ...` (their argument, stated fairly);
- numbered answers: `> 1.` is an overview analytic, `#### 2.` and `#### 3.` are tags that each have a card under them, `> 4.` closes with a link back to the plan;
- the cite fields (author, quals, date, title, publication, url, doa, initials, source);
- the card body: context around `==the read text==`.

## 3. The built Word files

Run:

```bash
python tools/build_docx.py examples/example-cards.md -o out.docx
python tools/build_docx.py examples/example-cards.md -o out-DRAFT.docx --draft
```

Open them in an editor that supports Verbatim-style formatting (CardMirror, Verbatim in Word, or similar). These are also checked in as `examples/example-cards.docx` and `examples/example-cards-DRAFT.docx`.

- **Final** (`example-cards.docx`): cyan highlight on the read text, 8pt unread context. This is the format you read from.
- **Draft** (`example-cards-DRAFT.docx`): proposed read text in bold, context at normal size. This is the cutting copy: you finish the highlighting.

## 4. Run the checks on the example

```bash
python tools/verify_quotes.py examples/example-cards.md --strict   # text is verbatim from the source
python tools/lint_cites.py examples/example-cards.md               # cites complete
python tools/lint_cards.py examples/example-cards.md               # cards not cut too thin
python tools/lint_blocks.py examples/example-cards.md              # block shape correct
python tools/inspect_docx.py out.docx --cards                      # what the .docx really contains
```

All should pass. Then try breaking it (change one word inside a card body; delete a card under a tag) and watch the right tool fail.

## 4b. The fictional case (a contention as a link chain)

`examples/example-case.md` is one fictional contention built the way the repo requires. Notice:

- the **chain map** under the heading (`Chain: UQ (...) -> TREND (...) -> LINK (...) -> IL (...) -> IMPACT (...) -> SOLVENCY (...)`);
- **a card for every step**, each with a tag that states its job (`UQ:`, `LINK:`, ...);
- **short analytics** only (connecting sentences and one impact-framing line);
- the sources are in `examples/case-sources/` and each card verifies against its source.

```bash
python tools/build_docx.py examples/example-case.md -o case-out.docx
python tools/lint_case.py examples/example-case.md                       # chain map + a card per step
python tools/lint_cards.py examples/example-case.md --profile case       # constructive-length cards
python tools/verify_quotes.py examples/example-case.md --strict
```

Read `core/argument-structure.md` alongside it. Then run `python tools/tag_story.py examples/example-case.md` and read only the tags and numbers as a judge would, with `core/logic-flow.md` open. Built Word versions are checked in as `examples/example-case.docx` and `examples/example-case-DRAFT.docx`.

## 4b-2. Good vs. bad pairs (fictional)

`examples/good-vs-bad/` has annotated pairs with working files. Read [examples/good-vs-bad/README.md](../examples/good-vs-bad/README.md), then in this order:

1. `examples/good-vs-bad/link-chains.md`: nine bad chains (one card and an essay, a missing middle, a scope mismatch, a link written as prose, an impact with no number, solvency for a different problem, padding, a contradiction, hedged into nothing), each with its fix, plus a good Aff chain, a good Neg DA chain, and a good turn chain.
2. `examples/good-vs-bad/cards.md`: bad and good cutting: the lone sentence, the cut-out qualifier, the tag that overclaims, fragmented highlighting, a snippet used as a card, a weak cite.
3. `examples/good-vs-bad/rebuttals.md`: the same argument answered badly and well; how the good answer was found.
4. `examples/good-vs-bad/analytics.md`: bad analytics (essay, AI label, invented number) and good ones; lay vs. tech versions.

Then run the tools to see them pass and fail:

```bash
python tools/lint_blocks.py examples/good-vs-bad/rebuttal-good.md --lay     # passes
python tools/lint_blocks.py examples/good-vs-bad/rebuttal-bad.md            # fails
python tools/lint_case.py examples/example-case.md                          # passes
python tools/lint_case.py examples/good-vs-bad/case-bad.md                  # fails
```

## 4c. A real 1AC mapped to the chain standard (private reference)

`reference/opponent-files/opponent-1AC-example.docx` is a real opposing 1AC. `docs/real-1ac-chain-walkthrough.md` maps each tag and card to UQ, TREND, LINK, IL, IMPACT, and SOLVENCY, with card counts and how much of each card is read. Run `python tools/inspect_docx.py reference/opponent-files/opponent-1AC-example.docx --cards` to see the cites and highlighted text yourself.

## 5. A real blocks file (private reference)

`reference/example-blocks/example-blocks-excerpt.docx`: about 6,000 words from a real team blocks file (15 blocks). Study its shape, then read the annotated walkthrough in `docs/what-good-looks-like.md`.

```bash
python tools/inspect_docx.py reference/example-blocks/example-blocks-excerpt.docx            # outline
python tools/inspect_docx.py reference/example-blocks/example-blocks-excerpt.docx --cards    # cites + highlighted text
python tools/lint_blocks.py reference/example-blocks/example-blocks-excerpt.docx             # should report 0 errors
```

What to notice: every block states the opposing argument, numbers its answers, puts a card under each tag, and ends with an analytic that links back or turns.

## 6. Real opposing files (private reference)

`reference/opponent-files/opponent-1AC-example.pdf` and `opponent-1NC-example.pdf`: real constructive files from other teams. Open the PDFs to see highlighting and shrinking. Study how a contention or off-case position is laid out and how much context their cards carry. Use `pdftotext` if you need the plain text.

## 7. Test it on a fresh agent

- `docs/agent-smoke-test.md`: a short hand test.
- `docs/fresh-session-test-prompt.md`: a hard, multi-part prompt for a brand-new session (build blocks and a case), with a grading sheet.
- `docs/fresh-session-test-prompt-2.md`: a harder one: answer a real opposing case using the user's own files as context, with a grading sheet.

## The mistakes to avoid (from a real test run)

- A block made only of analytics that say "Extend X" (no cards in the file).
- A contention with one or two cards and long explanatory paragraphs instead of a chain of cards: no uniqueness, no proven link, no impact number, no solvency.
- No statement of the opposing argument at the top of a block.
- Cards cut as one highlighted sentence with nothing around it.
- Claiming something was verified without running the tools.

`docs/what-good-looks-like.md` explains each one.
