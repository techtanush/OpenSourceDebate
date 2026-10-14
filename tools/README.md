# Tools

Standard-library Python 3 only. No `pip install`. Run from the repo root.

## build_docx.py

```bash
python tools/build_docx.py spec.md -o out.docx
python tools/build_docx.py spec.json -o out.docx --team team.yaml
```

Builds a .docx that uses the Verbatim style names (Pocket, Hat, Block, Tag, Cite, Underline, Analytic), so it works with the Verbatim navigation pane and macros.

### Markdown spec

```markdown
# Pocket title            -> Heading 1 (Pocket)
## Hat title              -> Heading 2 (Hat)
### Block title           -> Heading 3 (Block)
#### Tag                  -> Heading 4 (Tag); a card if followed by "cite:"
> analytic text           -> Analytic paragraph (dark blue)
plain line                -> normal paragraph

#### Tag sentence
cite: Lastname 25         # short cite (bold 13pt)
author: First Last
quals: Title, Organization
date: 3-3-2025
title: Article title
publication: Outlet
url: https://...
doa: 10-14-2026
initials: AB
style: frontline          # or: case
source: sources/lastname-25.txt   # used by verify_quotes.py
---
Context __underlined, not read__ and ==read aloud (highlight + underline)== more context.
```

- `==text==` read aloud: underline + cyan highlight
- `__text__` underlined only
- plain text: unread, 8pt
- Blank lines in the body make separate paragraphs.
- Use `raw:` instead of the cite fields to supply the text after the bold short cite yourself.

### JSON spec

```json
{
  "defaults": {"cite": {"initials": "AB", "style": "frontline"}},
  "items": [
    {"type": "pocket", "text": "Aff Frontlines"},
    {"type": "hat", "text": "Economy"},
    {"type": "block", "text": "A2: Recession"},
    {"type": "card", "tag": "Tag sentence",
     "cite": {"name": "Doe 25", "author": "Jane Doe", "quals": "Professor", "date": "1-1-2025",
              "title": "Title", "publication": "Outlet", "url": "https://...", "doa": "10-1-2026"},
     "body": "Context __underlined__ and ==read==."},
    {"type": "analytic", "text": "Extend Doe 25 from our case: ..."}
  ]
}
```

Item types: `pocket`, `hat`, `block`, `tag`, `card`, `analytic`, `undertag`, `text`.

Optional `team.yaml` supplies `cutter_initials` and `cite_style` defaults.

## inspect_docx.py

```bash
python tools/inspect_docx.py file.docx            # outline + style/highlight statistics
python tools/inspect_docx.py file.docx --cards    # cite line and highlighted text per card
python tools/inspect_docx.py file.docx --json     # raw paragraphs and runs
```

Use it to learn how an existing file is formatted before matching it.

## verify_quotes.py

```bash
python tools/verify_quotes.py spec.md            # uses each card's source: path
python tools/verify_quotes.py spec.md --source article.txt
python tools/verify_quotes.py spec.md --strict   # also fail (exit 2) on cards with no source
```

Checks that the full card body is a verbatim excerpt of the source, in order. Omissions are marked with `...` and edits with `[brackets]`. Exit 1 on a mismatch.

## lint_cites.py

```bash
python tools/lint_cites.py spec.md
```

Flags missing name, author, quals, date, title, URL, DOA, or initials, and short cites that don't look like `Lastname 25`.

## speech_timer.py

```bash
python tools/speech_timer.py speech.txt --wpm 250
python tools/speech_timer.py cards.docx --wpm 250 --limit 180
```

For .docx files, counts highlighted text plus headings and analytics (what is spoken). Prints the estimated time; exits 1 over `--limit` (seconds).

## Tests

```bash
python -m unittest discover -s tests -v
```
