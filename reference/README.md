# Reference material (PRIVATE REPO ONLY)

> **Do not make this repo public with this folder in it.** These are real files from a debate team and from opposing teams. Delete `reference/` (or move it to a private repo) before publishing, and also replace the short quoted snippets in `docs/what-good-looks-like.md`. This folder exists so agents working on the toolkit can study how real, good debate documents are built.

Study these for **structure, formatting, and style**. Do not copy their evidence into other files.

| File | What it is | Use it to learn |
|------|-----------|-----------------|
| `example-blocks/example-blocks-excerpt.docx` | About 6,000 words from a real team blocks file: the first 15 of its 28 blocks, across Energy & Grid, Environment & Health, Community & Governance, and Economy | Block anatomy: opposing-argument line, numbered overview, tagged cards with cites, closing link. Open in CardMirror, Verbatim, or another editor that supports Verbatim-style formatting. |
| `opponent-files/opponent-1AC-example.pdf` | A real opposing 1AC file (policy format), as sent to the opposing team | How a constructive case file is organized: contentions, tags, long cards with context, highlighting, Analytic lines |
| `opponent-files/opponent-1NC-example.pdf` | A real opposing 1NC file with off-case positions | How off-case positions (federalism, DAs) and their cards are laid out; how long cards run in a constructive |

Our own full cases are intentionally **not** included.

## How to use it

1. Run `python tools/inspect_docx.py reference/example-blocks/example-blocks-excerpt.docx --cards` to see cite lines and highlighted text per card.
2. Run `python tools/lint_blocks.py` and `python tools/lint_cards.py` on the excerpt: it should pass `lint_blocks.py` with no errors.
3. For the PDFs, use `pdftotext` (or a PDF reader) to read the text; PDFs keep the visual formatting, so open them to see highlighting and shrinking.
4. Read `docs/what-good-looks-like.md` for the annotated walkthrough.
