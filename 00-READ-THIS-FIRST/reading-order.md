# Reading order

Read in this order. Steps 1-4 apply to every task. Then pick the playbook for your task; it tells you which of the other files to open and in what order.

## Every task

| # | Read | Why |
|---|------|-----|
| 1 | [README.md](README.md) (this folder) | What the repo is and the rules everything follows |
| 2 | `AGENTS.md` | The routing table: which playbook, protocol, and tools go with which request |
| 3 | `core/integrity.md` | Non-negotiable rules: verbatim quotes, saved sources, UNVERIFIED labels, what to do with blocked pages |
| 4 | `core/card-anatomy.md` | What a card is, the heading hierarchy (Pocket/Hat/Block/Tag), the spec syntax, and why blocks hold full cards |

## The core guides (read the ones your task needs)

| Read | Use it for |
|------|-----------|
| `core/research-guide.md` | **How to research:** what to look for at each chain step, query templates, how to choose sources, counter-research, researching answers to specific cards |
| `core/argument-structure.md` | **How to build a chain:** uniqueness, trend, link, internal link, impact, solvency; the chain map; Aff solvency for every impact; cards first, analytics last |
| `core/logic-flow.md` | **How the cards add up:** the tag-story test, numbers that fit, no contradictions, case-level read-through |
| `core/refutation-guide.md` | **How to answer an argument:** the hole checklist, answer types ranked, layering, using their own evidence, using the files you have |
| `core/cutting-rules.md` | How to cut and highlight a card: context, read vs. underline vs. unread |
| `core/cite-format.md` | The two cite styles and every required field |
| `core/source-evaluation.md` and `core/research-protocol.md` | Rating sources and the short research checklist |
| `core/judge-adaptation.md` | Lay vs. technical judges: plain analytics, timing, fewer stronger answers |
| `core/file-organization.md` | Blocks vs. frontlines vs. backlines; where files live; merge, don't duplicate |
| `core/glossary.md` | Terms |

## Then the playbook for your task

| You are doing... | Open |
|------------------|------|
| A new case, DA, or any chained argument | `playbooks/01-case-from-scratch.md`, then `speeches/case/PROTOCOL.md` and `templates/case-skeleton.md` |
| A rebuttal to an opposing case | `playbooks/02-answer-an-opposing-case.md`, then `speeches/rebuttal/PROTOCOL.md` |
| Prepared blocks (answers to their arguments) | `playbooks/03-blocks-library.md`, then `speeches/blocks/PROTOCOL.md` and `templates/block-skeleton.md` |
| Frontlines (defense of our own case) | `playbooks/04-frontlines.md`, then `speeches/frontlines/PROTOCOL.md` |
| Backlines, summary, or final speeches | `playbooks/05-backlines-and-summary.md`, then `speeches/backlines/PROTOCOL.md` or `speeches/summary-final/PROTOCOL.md` |
| Cross-ex questions | `speeches/crossx/PROTOCOL.md` |
| Topic or tournament prep | `speeches/prep/PROTOCOL.md` |
| Anything, when the user already has files | `playbooks/06-use-my-files-as-context.md` first |

Also check `formats/<your format>.yaml` for speech order and time.

## Then study the examples

Go through [examples-in-order.md](examples-in-order.md). Start with the fictional examples, then the good-vs-bad pairs, then the real reference files.

## Before you deliver

Run the checks (see `tools/README.md`):

```bash
python tools/verify_quotes.py file.md --strict
python tools/lint_cites.py file.md
python tools/lint_cards.py file.md                  # add --profile case for constructive cards
python tools/lint_blocks.py file.md [--lay]         # blocks and frontlines
python tools/lint_case.py file.md [--neg]           # cases and DAs
python tools/tag_story.py file.md                   # read as a judge: does it flow?
python tools/speech_timer.py file.docx --wpm 300 --limit <seconds>
```

Finish with a short "Before you read these" list: UNVERIFIED quotes, biased or weak sources, missing credentials or dates, highlighting an opponent could attack, anything you could not find.
