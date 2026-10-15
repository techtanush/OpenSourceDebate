# READ THIS FIRST

Start here. This page explains what the repo is, what to read and in what order, and how to try it in about ten minutes.

## What this repo is

A toolkit that teaches an AI coding agent (**Claude Code**, **Codex**, or similar) to do debate prep properly: research evidence, cut cards, and write cases, rebuttals, frontlines, blocks, and cross-ex questions, in the standard Verbatim Word format.

- **No AI API and no key.** Your own agent does the searching and thinking.
- The repo supplies what the agent needs to do it *right*: protocols, file formats, integrity rules, templates, worked examples, and small Python tools that check the agent's work.
- It is topic-agnostic. The examples are fictional (the only real material is in `reference/`, see below).

## Who reads what

| You are... | Read |
|------------|------|
| **An AI agent** about to do a task | `AGENTS.md`, then follow [reading-order.md](reading-order.md) |
| **A debater** setting it up | This page, then [reading-order.md](reading-order.md) and the Quick start below |
| **Someone improving the repo** | [reading-order.md](reading-order.md), `CONTRIBUTING.md`, `docs/agent-smoke-test.md`, `docs/fresh-session-test-prompt.md` |

## The six rules everything follows

1. **Never fabricate.** Quotes are verbatim from a saved source. Anything unverified is labeled UNVERIFIED (`core/integrity.md`).
2. **Cut real cards.** Tag, full cite, body with context around the read text, only the key words read (`core/cutting-rules.md`).
3. **Cards first; on the Aff, every impact needs solvency.** Evidence does the arguing; analytics only connect cards and show the *resolution itself* causes the impact to fall (`Solvency:`). **Contentions are chains of cards.** Every step (problem now, link, internal links, impact, solvency) has its own card, and a chain map names them (`core/argument-structure.md`). One card plus explanation is not a contention.
4. **Blocks hold the actual cards.** A block states the opposing argument, numbers the answers, puts a cut card under each, and closes with a link or turn. Analytics never replace cards (`speeches/blocks/PROTOCOL.md`).
5. **Check the work.** Run the tools before delivering (below).
6. **Be honest about weaknesses.** End every deliverable with a "Before you read these" list.

## Quick start (about ten minutes)

```bash
git clone https://github.com/techtanush/OpenSourceDebate.git
cd OpenSourceDebate
cp team.example.yaml team.yaml            # your initials, cite style, format, wpm
python -m unittest discover -s tests      # should end with OK
```

Try the tools on the fictional example (see [examples-in-order.md](examples-in-order.md)):

```bash
python tools/build_docx.py examples/example-cards.md -o out.docx
python tools/verify_quotes.py examples/example-cards.md --strict
python tools/lint_cites.py examples/example-cards.md
python tools/lint_cards.py examples/example-cards.md
python tools/lint_blocks.py examples/example-cards.md
python tools/lint_case.py examples/example-case.md
python tools/inspect_docx.py out.docx --cards
python tools/speech_timer.py out.docx --wpm 300
```

Then open `out.docx` in an editor that supports Verbatim-style formatting (CardMirror, Verbatim in Word, or similar). TextEdit, Quick Look, and Pages will not show the highlighting or styles; that is expected.

Using an agent: open Claude Code (or Codex) **in this folder** and ask for a task, for example *"Cut a card from `examples/source-article.txt` for the tag 'Sales were flat in most cities after a ban.'"*

## Map of the repo

| Path | What it is |
|------|-----------|
| `00-READ-THIS-FIRST/` | This folder: orientation, reading order, examples in order |
| `AGENTS.md`, `CLAUDE.md` | Agent entry points; `AGENTS.md` has the task-to-protocol routing table |
| `core/` | Rules every task follows: integrity, card anatomy, cutting rules, cite format, source evaluation, research protocol, glossary |
| `speeches/` | One protocol per kind of file: `case/`, `rebuttal/`, `frontlines/`, `blocks/`, `crossx/`, `summary-final/`, `prep/` |
| `formats/` | Speech order and times for Policy, LD, PF, plus a template for your league |
| `skills/` | Claude Code skills (thin wrappers that point to the protocols above) |
| `tools/` | Python tools (no installs): `build_docx`, `inspect_docx`, `verify_quotes`, `lint_cites`, `lint_cards`, `lint_blocks`, `lint_case`, `speech_timer`; see `tools/README.md` |
| `templates/` | Blank starter files, including `block-skeleton.md` |
| `examples/` | A fictional worked example: source article, card spec, built `.docx` (final and draft) |
| `docs/` | `what-good-looks-like.md`, `agent-smoke-test.md`, `fresh-session-test-prompt.md` |
| `reference/` | **Private-repo only:** real example blocks and two real opposing files, for studying structure |
| `tests/` | Unit tests for the tools |

## A note on `reference/`

`reference/` holds real files from a debate team and opposing teams. It is there so agents can study how good documents are built. **Do not make the repo public with it in.** Delete it (and replace the quoted snippets in `docs/what-good-looks-like.md`) first. See `reference/README.md`.

## A note on formatting

The highlighting and styles live in Word styles, so they only appear when the `.docx` is opened in an editor that supports them, such as CardMirror or Verbatim in Word, or another editor with Verbatim-style support.

## Next

Go to [reading-order.md](reading-order.md).
