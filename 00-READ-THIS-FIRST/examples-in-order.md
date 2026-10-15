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
- `docs/fresh-session-test-prompt.md`: a hard, multi-part prompt for a brand-new session, with a grading sheet.

## The mistakes to avoid (from a real test run)

- A block made only of analytics that say "Extend X" (no cards in the file).
- No statement of the opposing argument at the top of a block.
- Cards cut as one highlighted sentence with nothing around it.
- Claiming something was verified without running the tools.

`docs/what-good-looks-like.md` explains each one.
