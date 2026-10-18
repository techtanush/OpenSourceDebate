---
name: use-my-files
description: "Index and search the user's existing debate files before researching or writing, to reuse cards, merge into existing blocks, and match their style. Use at the start of any task when the user has files."
---

# use-my-files

First read `AGENTS.md` and `core/integrity.md` from the repo root.

## Read these files

- `core/file-organization.md`
- `playbooks/06-use-my-files-as-context.md`

## Steps

1. Ask where the team's folder is (or read `team.yaml`).
2. `python tools/library.py index <folder> -o library-index.md`, then read the index.
3. `python tools/library.py search <folder> <keywords> [--text]` for the task's topic; reuse cards that fit.
4. `python tools/inspect_docx.py <file>.docx --cards` on a couple of files to learn their cite style and headings.
5. Merge new evidence into the existing block under its existing heading; do not duplicate or rename headings.
6. Tell the user what you found, reused, and inferred (and write `team.yaml` from it).

## Finish with

What existed, what you reused, what is new, and anything you inferred about their style.
