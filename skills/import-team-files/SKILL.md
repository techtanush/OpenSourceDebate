---
name: import-team-files
description: "Learn the user's existing debate file conventions (headings, cite style, highlight habits) from their .docx files so new cards match. Use when the user points at existing files."
---

# import-team-files

First read `AGENTS.md` and `core/integrity.md` from the repo root. Never fabricate or paraphrase inside a quote, and never treat a snippet as the source text.

## Read these files

- `core/card-anatomy.md`
- `core/cite-format.md`

## Steps

1. Run `python tools/inspect_docx.py <file>.docx` and `--cards` on a few representative files.
2. Summarize: heading levels used, cite template (bracket style, field order, initials tail), read vs. unread formatting, highlight colors.
3. Write the findings into `team.yaml` (`cite_style`, `cutter_initials`) and note any exceptions.
4. Use the files only for style or the user's own evidence. Never copy them into public places.

## Finish with

A short "Before you read these" list: UNVERIFIED quotes, biased or weak sources, missing credentials or dates, and highlighting an opponent could attack.
