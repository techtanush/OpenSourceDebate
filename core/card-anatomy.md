# Card Anatomy

A **card** is one piece of evidence. In Verbatim (the Word template most debaters use) a card has four parts, always in this order.

```
[Tag]           the claim the card proves, in the debater's words
[Cite]          who said it, when, and where
[blank line]
[Body]          the author's own words, with the read parts marked
```

## 1. Tag (Heading 4)

- One sentence, 13pt bold, left-aligned.
- States the argument, not the topic ("Frequent buses raise ridership," not "Bus service").
- Must be fully supported by what the highlighted text says. If the body doesn't say it, change the tag.
- Underline key words if you want emphasis for reading.

## 2. Cite line

- The **short cite** (`Lastname YY`, or `Org YY`) is bold 13pt. It is the only part spoken aloud.
- Everything after it is 8pt: full author name, credentials, date, title, publication, URL, DOA, and the cutter's initials.
- Templates and field rules are in `cite-format.md`.

## 3. Body

One paragraph (or a few, if the source has paragraph breaks you keep), made of three kinds of text:

| Kind | Meaning | Formatting |
|------|---------|------------|
| **Read** | Spoken aloud in the round | Underlined + highlighted (cyan) |
| **Underlined** | Supports the argument but is not read (or is read only if time allows) | Underlined, 11pt, no highlight |
| **Unread** | Surrounding context kept so the card isn't "clipped" | 8pt, no underline, no highlight |

Rules for choosing what to mark are in `cutting-rules.md`.

## Document hierarchy (navigation pane)

| Level | Verbatim name | Used for | Look |
|-------|---------------|----------|------|
| Heading 1 | **Pocket** | The whole file ("Aff Frontlines") | 26pt bold, boxed, centered, page break |
| Heading 2 | **Hat** | A topic or contention ("Econ") | 22pt bold, double underline, centered, page break |
| Heading 3 | **Block** | An argument or answer ("A2: Investors") | 16pt bold, underlined, centered, page break |
| Heading 4 | **Tag** | One card's claim | 13pt bold |

Other styles: **Analytic** (dark blue) for your own explanation between cards, and **Undertag** (italic green) for rare notes under a tag.

## Spec format used by this repo

`tools/build_docx.py` turns a Markdown spec into a Verbatim-styled `.docx`. See `tools/README.md` for the full syntax and `examples/example-cards.md` for a working file.

```markdown
#### Tag sentence
cite: Lastname 25
author: First Last
quals: Title, Organization
date: 3-3-2025
title: Article title
publication: Outlet
url: https://...
doa: 10-14-2026
initials: AB
style: frontline        # or: case
source: sources/lastname-25.txt
---
Context __supports the argument__ and ==the words you read aloud== more context.
```

- `==text==` = read (highlight + underline)
- `__text__` = underlined, not read
- plain text = unread (8pt)
- `> text` on its own line = an Analytic paragraph
