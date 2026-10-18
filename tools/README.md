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

Add `--draft` to build a **cutting copy**: proposed read text is bold and underlined (no highlight) and the surrounding context stays at normal size, so you can finish cutting in your editor. The default is the final format (cyan highlight, 8pt unread).

Optional `team.yaml` supplies `cutter_initials` and `cite_style` defaults.

## inspect_docx.py

```bash
python tools/inspect_docx.py file.docx            # outline + style/highlight statistics
python tools/inspect_docx.py file.docx --cards    # cite line and highlighted text per card
python tools/inspect_docx.py file.docx --json     # raw paragraphs and runs
python tools/inspect_docx.py file.docx --text     # plain text, one paragraph per line (read an opposing case)
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

## lint_blocks.py

```bash
python tools/lint_blocks.py spec.md      # or: python tools/lint_blocks.py file.docx
```

Checks every Block (Heading 3): it must contain actual cut cards, every Tag must have a card under it, and it must open with a statement of the opposing argument ("Aff Argument: ...") before the answers. Warns on fewer than two answers or no closing analytic. With `--lay` (lay or parent judges) it also warns when a card has no plain analytic right after it, or an analytic reads like an AI label ("Lay version", "Simply put") or uses arrows. Exit 1 on any error. Block anatomy: `speeches/blocks/PROTOCOL.md`.

## lint_case.py

```bash
python tools/lint_case.py case.md          # Aff case (solvency required)
python tools/lint_case.py case.docx --neg  # Neg case / DAs
```

Checks every contention (a Hat or Block titled "Contention...", "C1...", "Advantage...", "DA..."): at least four cards, a chain map (`Chain: UQ (Card) -> LINK (Card) -> IMPACT (Card) ...`) before the first card, UQ / LINK / IMPACT (and SOLVENCY for Aff) present in the map, and at least as many cards as steps. Also requires an Aff `Solvency:` analytic, fails when analytics outweigh cards, and checks flow: steps in logical order, chain-map card names match the cards in order, and numbers in analytics appear in a card (warning). Warns on long analytics (over 60 words). Exit 1 on any error. Standard: `core/argument-structure.md`.

## library.py

```bash
python tools/library.py index <folder> -o library-index.md   # map every card in the user's .docx files
python tools/library.py search <folder> <term> [<term> ...] [--text] [--limit 20]
python tools/library.py outline <file.docx>                  # one file's headings with card counts
```

Read-only. Use it before researching: reuse existing cards, merge new evidence into existing blocks, learn the team's headings, and see what was already read. See `playbooks/06-use-my-files-as-context.md`.

## tag_story.py

```bash
python tools/tag_story.py case.md      # or a .docx
```

Prints the chain map and every tag in order with its cite, the chain step it fills, and the numbers it carries, so you can read the logic flow as a judge would. It makes the flow visible; it does not judge it. See `core/logic-flow.md`.

## lint_cards.py

```bash
python tools/lint_cards.py spec.md      # or: python tools/lint_cards.py file.docx
```

Flags cards that are cut too thin. The default `block` profile catches only the extremes (a lone sentence, a card that is entirely highlighted, or no unread context on either side); `--profile case` is stricter for long constructive cards. Calibrated on real team files. A warning, not a quality score. Exit 1 if any card is flagged.

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
