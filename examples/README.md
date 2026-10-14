# Examples

Everything in this folder is **fictional**. The topic ("Resolved: Cities should
ban private cars from downtown cores"), the authors, the institute, and the
article text were all written for this repo so there is nothing to copy-clear.
Do not cite any of it in a real round.

| File | What it shows |
|------|---------------|
| `source-article.txt` | The saved full text a card is cut from (the thing `verify_quotes.py` checks against) |
| `example-cards.md` | A tiny block file in the Markdown spec format: Pocket > Hat > Block > Tag/cite/body |
| `example-cards.docx` | The same file built with `build_docx.py` (regenerate with the command below) |

```bash
python tools/build_docx.py examples/example-cards.md -o examples/example-cards.docx
python tools/verify_quotes.py examples/example-cards.md
python tools/lint_cites.py examples/example-cards.md
python tools/inspect_docx.py examples/example-cards.docx --cards
```
