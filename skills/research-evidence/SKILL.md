---
name: research-evidence
description: "Research evidence for a debate claim: search, fetch full text, evaluate sources, and cut verified cards. Use when the user wants evidence, cards, or research on an argument."
---

# research-evidence

First read `AGENTS.md` and `core/integrity.md` from the repo root. Never fabricate or paraphrase inside a quote, and never treat a snippet as the source text.

## Read these files

- `core/research-protocol.md`
- `core/source-evaluation.md`
- `core/integrity.md`

## Steps

1. Restate the claim as a tag-shaped sentence and what a strong source would be.
2. Search from several angles (include the counter-claim). Prefer recent, credible, primary sources.
3. Fetch full text and save it; if blocked, follow the fallback in `core/integrity.md`.
4. Rate each source (`core/source-evaluation.md`) and pick the best passage.
5. Cut and verify cards (see the cut-card skill). Report UNVERIFIED items and weak sources.

## Card quality

Cards need context around the read text and sparse highlighting (see `core/cutting-rules.md`); run `python tools/lint_cards.py` and `python tools/lint_blocks.py`, and fix every flag. Blocks and frontlines hold the actual cut cards, never analytics that merely mention a card in another file. Read `docs/what-good-looks-like.md`.

## Finish with

A short "Before you read these" list: UNVERIFIED quotes, biased or weak sources, missing credentials or dates, and highlighting an opponent could attack.
