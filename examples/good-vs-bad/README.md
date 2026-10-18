# Good vs. Bad: Worked Examples

Annotated pairs showing what the repo's rules look like in practice. Everything is fictional. Read the guide, look at the pair, then run the tools to watch them pass or fail.

| Topic | Guide (read this) | Working files (run the tools on these) |
|-------|-------------------|----------------------------------------|
| **Link chains** | [link-chains.md](link-chains.md): nine bad chains, how to fix each, a good Aff chain, a good Neg DA chain, a good turn chain | Good: `../example-case.md`. Bad: `case-bad.md` (fails `lint_case.py`) |
| **Cards** (cutting, highlighting, cites) | [cards.md](cards.md): lone sentence, cut-out qualifier, tag overclaim, fragmented highlighting, snippet, weak cite | `../example-cards.md` |
| **Rebuttals and blocks** | [rebuttals.md](rebuttals.md): a bad rebuttal vs. a good one, and how the good one was found | Good: `rebuttal-good.md` (passes every check). Bad: `rebuttal-bad.md` (fails `lint_blocks.py`). Opponent's source: `sources/opponent-ashford-pilot.txt` |
| **Analytics** (lay vs. tech) | [analytics.md](analytics.md): bad essays, AI labels, invented numbers; good plain sentences, solvency sentence, closing link | `rebuttal-good.md` (lay version) |

## Run them

```bash
# the good ones pass
python tools/lint_blocks.py examples/good-vs-bad/rebuttal-good.md --lay
python tools/verify_quotes.py examples/good-vs-bad/rebuttal-good.md --strict
python tools/lint_case.py examples/example-case.md

# the bad ones fail, on purpose
python tools/lint_blocks.py examples/good-vs-bad/rebuttal-bad.md     # no cards, tags with no cards, no argument statement
python tools/lint_case.py examples/good-vs-bad/case-bad.md           # one card, no chain map, analytics outweigh cards
```
