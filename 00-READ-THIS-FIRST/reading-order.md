# Reading order

Read in this order. The first four steps apply to every task; step 5 depends on what you are doing.

## Every task

| # | Read | Why |
|---|------|-----|
| 1 | [README.md](README.md) (this folder) | What the repo is and the five rules |
| 2 | `AGENTS.md` | The routing table: which protocol and tools go with which request |
| 3 | `core/integrity.md` | Non-negotiable rules: verbatim quotes, saved sources, UNVERIFIED labels, what to do with blocked pages |
| 4 | `core/card-anatomy.md` | What a card is, the heading hierarchy (Pocket/Hat/Block/Tag), the spec syntax, and why blocks hold full cards |

## For anything that involves cutting cards

| # | Read | Why |
|---|------|-----|
| 5 | `core/cutting-rules.md` | Underline vs highlight vs unread, how much context to include, editing marks |
| 6 | `core/cite-format.md` | The two cite styles and every required field |
| 7 | `docs/what-good-looks-like.md` | An annotated real block, and exactly what went wrong in a test run |
| 8 | `core/source-evaluation.md` and `core/research-protocol.md` | How to find, rate, and save sources |
| 9 | `core/argument-structure.md` | For cases, DAs, and any argument with causal steps: the link-chain standard (uniqueness, link, internal link, impact, solvency), the chain map, and impact framing vs. weighing |
| 10 | `core/logic-flow.md` | How the cards combine into one story: the tag-story test, numbers that fit, no contradictions, case-level read-through |

## Then the protocol for your task

| You are writing... | Read |
|--------------------|------|
| A constructive case, DA, or any chained argument | `core/argument-structure.md`, `speeches/case/PROTOCOL.md`, and `templates/case-skeleton.md` |
| A rebuttal to an opposing case | `speeches/rebuttal/PROTOCOL.md` |
| Frontlines (defending your own arguments) | `speeches/frontlines/PROTOCOL.md` |
| Blocks / A2 files (answering their arguments) | `speeches/blocks/PROTOCOL.md` and `templates/block-skeleton.md` |
| Cross-ex questions | `speeches/crossx/PROTOCOL.md` |
| A summary or final speech | `speeches/summary-final/PROTOCOL.md` |
| Topic or tournament prep | `speeches/prep/PROTOCOL.md` |

Also check `formats/<your format>.yaml` for speech order and time, and `core/glossary.md` for terms.

## Then study the examples

Go through [examples-in-order.md](examples-in-order.md). Read the fictional example first, then the real reference files.

## Before you deliver

Run the checks (see `tools/README.md`):

```bash
python tools/verify_quotes.py file.md --strict
python tools/lint_cites.py file.md
python tools/lint_cards.py file.md
python tools/lint_blocks.py file.md        # blocks and frontlines
python tools/lint_case.py file.md          # cases and DAs (add --neg for Neg)
python tools/speech_timer.py file.docx --wpm 300 --limit <seconds>
```

Finish with a short "Before you read these" list: UNVERIFIED quotes, biased or weak sources, missing credentials or dates, highlighting an opponent could attack, anything you could not find.
