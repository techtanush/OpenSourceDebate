---
name: build-frontlines
description: "Build frontlines: prepared defense of the user's OWN arguments against the opponent's likely responses. Use when the user says frontlines. Not for answering the opponent's case (that is blocks)."
---

# build-frontlines

First read `AGENTS.md` and `core/integrity.md` from the repo root. Never fabricate or paraphrase inside a quote, and never treat a snippet as the source text.

## Read these files

- `speeches/frontlines/PROTOCOL.md`
- `core/integrity.md`
- `core/cutting-rules.md`

## Playbook

The detailed procedure and examples: `playbooks/04-frontlines.md; core/file-organization.md`

## Steps

1. Read the constructive first and note which cards were already read.
2. List the likely responses to each contention, then write the answer to each.
3. Never re-paste constructive cards; write `Extend [Card] from our constructive: ...`.
4. New evidence is allowed: research and verify it. Build the file and report caveats.

## Card quality

Cards need context around the read text and sparse highlighting (see `core/cutting-rules.md`); run `python tools/lint_cards.py` and `python tools/lint_blocks.py`, and fix every flag. Blocks and frontlines hold the actual cut cards, never analytics that merely mention a card in another file. Read `docs/what-good-looks-like.md`.

## Delivering files

Tell the user the formatting and highlighting only appear when the .docx is opened in an editor that supports Verbatim-style formatting (such as CardMirror or Verbatim in Word).

## Finish with

A short "Before you read these" list: UNVERIFIED quotes, biased or weak sources, missing credentials or dates, and highlighting an opponent could attack.
