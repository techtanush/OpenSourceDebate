---
name: verify-card
description: "Verify finished cards: check quotes are verbatim from saved sources and cites are complete. Use when the user wants cards checked before a round."
---

# verify-card

First read `AGENTS.md` and `core/integrity.md` from the repo root. Never fabricate or paraphrase inside a quote, and never treat a snippet as the source text.

## Read these files

- `core/integrity.md`
- `core/cite-format.md`

## Steps

1. Run `python tools/verify_quotes.py spec.md --strict` and `python tools/lint_cites.py spec.md`.
2. For a .docx without a spec, run `python tools/inspect_docx.py file.docx --cards` and check each tag against its highlighted text.
3. Report each card as VERIFIED, UNVERIFIED, or MISMATCH, plus tag-vs-text gaps and weak sources.

## Finish with

A short "Before you read these" list: UNVERIFIED quotes, biased or weak sources, missing credentials or dates, and highlighting an opponent could attack.
