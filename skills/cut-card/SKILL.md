---
name: cut-card
description: "Cut a debate card from a source: tag, cite, body with read/underline/unread marking, in Verbatim format. Use when the user asks to cut, highlight, or format a card or evidence."
---

# cut-card

First read `AGENTS.md` and `core/integrity.md` from the repo root. Never fabricate or paraphrase inside a quote, and never treat a snippet as the source text.

## Read these files

- `core/integrity.md`
- `core/cutting-rules.md`
- `core/card-anatomy.md`
- `core/cite-format.md`

## Steps

1. Get the claim (tag) and the source. Save the full source text to `sources/<shortcite>.txt`.
2. Write the card spec (see `core/card-anatomy.md`) with `source:` set.
3. Build: `python tools/build_docx.py cards.md -o cards.docx`.
4. Verify: `python tools/verify_quotes.py cards.md --strict` and `python tools/lint_cites.py cards.md`.
5. Reply with the cards and a short "Before you read these" list.

## Card quality

Cards need context around the read text and sparse highlighting (see `core/cutting-rules.md`); run `python tools/lint_cards.py` and `python tools/lint_blocks.py`, and fix every flag. Blocks and frontlines hold the actual cut cards, never analytics that merely mention a card in another file. Read `docs/what-good-looks-like.md`.

## Delivering files

Tell the user the formatting and highlighting only appear when the .docx is opened in an editor that supports Verbatim-style formatting (such as CardMirror or Verbatim in Word).

## Finish with

A short "Before you read these" list: UNVERIFIED quotes, biased or weak sources, missing credentials or dates, and highlighting an opponent could attack.
