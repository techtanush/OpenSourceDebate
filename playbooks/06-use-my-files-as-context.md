# Playbook 06: Use the User's Files as Context

**Goal:** before researching or writing, learn what the user already has: their case, their blocks, their evidence, their style. Then reuse, merge, and match instead of duplicating.

**Read first:** `core/file-organization.md`. Tools: `tools/library.py`, `tools/inspect_docx.py`.

## Steps

1. **Find the files.** Ask where the team's folder is (or read `team.yaml`: `blocks_dir`, `frontlines_dir`, `library_dir`).
2. **Index the library (read-only).**

```bash
python tools/library.py index <team-folder> -o library-index.md
python tools/library.py outline <file.docx>               # one file's headings with card counts
```

   Read the index: which arguments already have blocks, which cards exist, what the headings are called.
3. **Search before researching.**

```bash
python tools/library.py search <team-folder> <keyword> [<keyword> ...]          # tags and cites
python tools/library.py search <team-folder> <keyword> --text                   # also body text
```

   If a card fits the slot, reuse it. If a block exists for the argument, add to that block.
4. **Learn the style.**

```bash
python tools/inspect_docx.py <file>.docx            # heading levels used, run styles, highlight colors
python tools/inspect_docx.py <file>.docx --cards    # cite template, initials, DOA convention
```

   Match: cite style (`[ ]` or `( )`), field order, initials tail, how analytics are used, what the headings are.
5. **Learn the case.** Read the case file's outline and cards to know the contentions and what has been read (needed for extensions and for not contradicting it).
6. **Write `team.yaml`** from what you found (`cutter_initials`, `cite_style`, `judge`, folders) and tell the user what you inferred.
7. **Merge, don't duplicate.** New evidence goes into the existing block under the existing heading. Keep the team's headings if they asked; do not rename or reorder.
8. **Never publish or copy their files elsewhere.** Use them only for this project.

## Done when

- [ ] You know what exists for the task and have reused what fits.
- [ ] New cards are in existing blocks, not duplicates.
- [ ] New files match the user's style.

## Common mistakes

- Re-cutting an article the library already has.
- Creating a second block for an argument that has one.
- Changing the team's headings.
- Guessing which cards were read in the constructive.
