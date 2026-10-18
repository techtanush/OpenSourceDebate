# Agent Instructions: Open Source Debate Toolkit

You are helping a debater research, cut cards, and write files. This repo gives you the protocols, formats, and small tools. You supply the reasoning, search, and browsing. No API keys are needed.

## Always do this first

0. If this is your first time in the repo, read `00-READ-THIS-FIRST/README.md` and follow `00-READ-THIS-FIRST/reading-order.md`.

1. Read `core/integrity.md`. **Never fabricate or paraphrase inside a quote. Never present a snippet or summary as the source text.**
2. If `team.yaml` exists, read it (cutter initials, cite style, format, wpm). If not, ask the user or use `team.example.yaml` defaults and say so.
3. Read the format file named in `team.yaml` (`formats/<format>.yaml`) to learn speech names, times, and rules.
4. Then follow the routing table.

## Routing table

| The user wants to... | Read these | Use these tools |
|----------------------|-----------|-----------------|
| Cut one or more cards | `core/cutting-rules.md`, `core/card-anatomy.md`, `core/cite-format.md`, `docs/what-good-looks-like.md` | `build_docx.py`, `verify_quotes.py`, `lint_cites.py`, `lint_cards.py` |
| Research evidence on a claim | `core/research-guide.md`, `core/research-protocol.md`, `core/source-evaluation.md` | `verify_quotes.py` |
| Write a constructive case, DA, or any chained argument | `playbooks/01-case-from-scratch.md`, `core/argument-structure.md`, `examples/good-vs-bad/link-chains.md`, `speeches/case/PROTOCOL.md`, `templates/case-skeleton.md` | `build_docx.py`, `lint_case.py`, `speech_timer.py` |
| Write a rebuttal against a case | `playbooks/02-answer-an-opposing-case.md`, `speeches/rebuttal/PROTOCOL.md`, `core/refutation-guide.md` | `inspect_docx.py --text`, `library.py`, `speech_timer.py` |
| Build frontlines (defend our own arguments) | `playbooks/04-frontlines.md`, `speeches/frontlines/PROTOCOL.md` | `inspect_docx.py --cards`, `build_docx.py`, `lint_blocks.py` |
| Build blocks / A2 files (answer their arguments) | `playbooks/03-blocks-library.md`, `speeches/blocks/PROTOCOL.md`, `core/file-organization.md` | `library.py`, `build_docx.py`, `lint_blocks.py [--lay]` |
| Extend our rebuttal against their frontlines (backlines) | `speeches/backlines/PROTOCOL.md`, `playbooks/05-backlines-and-summary.md` | none |
| Prepare cross-ex questions | `speeches/crossx/PROTOCOL.md` | none |
| Write a summary / final speech | `speeches/summary-final/PROTOCOL.md` | `speech_timer.py` |
| Prepare a new topic or tournament | `speeches/prep/PROTOCOL.md` | none |
| Learn the user's existing files and style, and reuse what they have | `playbooks/06-use-my-files-as-context.md`, `skills/import-team-files/SKILL.md` | `library.py`, `inspect_docx.py` |
| Check a finished file | `skills/verify-card/SKILL.md` | `verify_quotes.py`, `lint_cites.py` |

Claude Code users also get the same workflows as skills in `skills/`. Each skill is a thin wrapper that points back to these files, so the instructions stay in one place.

## Tools (Python 3, standard library only)

```bash
python tools/build_docx.py spec.md -o out.docx      # Markdown/JSON spec -> Verbatim-styled .docx
python tools/inspect_docx.py file.docx [--cards]    # outline, cites, highlight stats
python tools/verify_quotes.py spec.md [--strict]    # body text must be verbatim from the saved source
python tools/lint_cites.py spec.md                  # missing/malformed cite fields
python tools/lint_cards.py spec.md                  # cards cut too thin? (also works on .docx; --profile case)
python tools/lint_blocks.py spec.md                 # blocks complete? argument stated, real cards, closing analytic
python tools/lint_case.py spec.md                   # contentions are real link chains (chain map, card per step, step order, numbers traceable)
python tools/tag_story.py spec.md                   # print the tags as a story to test the logic flow
python tools/library.py index|search|outline <folder>  # map and search the user's existing .docx files (read-only)
python tools/speech_timer.py file --wpm 250         # reading time (docx counts highlighted text only)
python -m unittest discover -s tests                # run the tests
```

See `tools/README.md` for the spec syntax and `examples/` for a complete fictional example.

## Viewing the output

The formatting and highlighting in generated `.docx` files only appear when the file is opened in an editor that supports Verbatim-style formatting, such as CardMirror, Verbatim (in Word), or a similar tool. Tell the user this when you deliver a file, and never judge formatting from a TextEdit, Quick Look, or Pages preview. To check formatting yourself, use `python tools/inspect_docx.py file.docx` (it reads the real styles).

## Working rules

- **Save sources.** Put the full text of every article in `sources/<shortcite>.txt` and set `source:` on the card. `sources/` is gitignored.
- **Verify before delivering.** Run `verify_quotes.py`, `lint_cites.py`, `lint_cards.py`, and (for blocks/frontlines) `lint_blocks.py`, and (for cases and DAs) `lint_case.py`. Report failures plainly and fix them.
- **Cut real cards, and put them in the file.** Each card has context around the read text, and only a sparse part is read. Blocks and frontlines hold the actual cards, never analytics that merely mention a card in another file. Follow the block anatomy in `speeches/blocks/PROTOCOL.md` and see `docs/what-good-looks-like.md`.
- **Cards first, and Aff solvency for every impact.** Evidence does the arguing; analytics only connect cards and, on the Aff, show how the *resolution* causes the impact to fall (a `Solvency:` analytic per contention). Never spend paragraphs on analytics where a card belongs.
- **Know the judge.** Lay judges need a plain sentence after each card and fewer, stronger answers; tech judges get layers and weighing (`core/judge-adaptation.md`, `judge:` in `team.yaml`).
- **Check the user's files before researching.** Search and reuse their library, merge into existing blocks, match their headings and style (`core/file-organization.md`).
- **Answer their specific cards.** Read the text around their highlighting and use their own evidence (`core/refutation-guide.md`).
- **Do research properly.** Work slot by slot from the chain map; follow `core/research-guide.md` for what to look for at each step and how to search.
- **Make the logic flow.** The cards must read as one story: each tag follows from the last, numbers and scope fit, nothing contradicts. Run `tag_story.py`, read it as a judge, and follow `core/logic-flow.md`.
- **Build chains, not claims.** Every contention needs a card for each step (UQ, LINK, IL, IMPACT, SOLVENCY) and a chain map. One card plus explanatory paragraphs is a failed contention. See `core/argument-structure.md`.
- **Offer a cutting copy.** If the user will finish the highlighting themselves, also build with `--draft` (proposed read text in bold, context at normal size).
- **Report caveats.** End every evidence task with a short "Before you read these" list: UNVERIFIED quotes, biased or weak sources, missing credentials, attackable highlighting.
- **Respect the user's files.** Read their existing files only to learn style or to reuse their own cards. Do not publish or copy them elsewhere.
- **Ask before outward actions** (publishing, emailing, pushing). Reading and writing local files is fine.
- **Don't invent debate rules.** If the format file doesn't say, ask the user.
- **Don't solve CAPTCHAs or bypass paywalls.** See `core/integrity.md` for what to do when a page is blocked.

## Style of output

- Be concise and organized: tag, cite, body.
- Use `==read==`, `__underline__`, and plain text for unread in specs (`core/card-anatomy.md`).
- Give times as `m:ss` and say the wpm used.
