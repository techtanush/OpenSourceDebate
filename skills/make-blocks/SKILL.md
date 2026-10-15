---
name: make-blocks
description: "Make a block (A2/AT file): prepared answers to a common opposing argument, ordered strongest first, with cards and analytics. Use when the user wants answers to a specific argument."
---

# make-blocks

First read `AGENTS.md` and `core/integrity.md` from the repo root. Never fabricate or paraphrase inside a quote, and never treat a snippet as the source text.

## Read these files

- `speeches/blocks/PROTOCOL.md`
- `core/research-protocol.md`
- `core/integrity.md`

## Steps

1. State the opposing argument fairly, with the evidence they would read.
2. Write answers: takeouts, turns, mitigation, source indicts. Research and verify cards.
3. Order strongest first; add "if they say X, say Y" follow-ups; time it.
4. Deliver the .docx and the caveats list.

## Card quality

Cards need context around the read text and sparse highlighting (see `core/cutting-rules.md`); run `python tools/lint_cards.py` and `python tools/lint_blocks.py`, and fix every flag. Blocks and frontlines hold the actual cut cards, never analytics that merely mention a card in another file. Read `docs/what-good-looks-like.md`.

## Delivering files

Tell the user the formatting and highlighting only appear when the .docx is opened in an editor that supports Verbatim-style formatting (such as CardMirror or Verbatim in Word).

## Finish with

A short "Before you read these" list: UNVERIFIED quotes, biased or weak sources, missing credentials or dates, and highlighting an opponent could attack.
