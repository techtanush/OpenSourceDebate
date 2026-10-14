# Open Source Debate

A toolkit that teaches an AI coding agent (**Claude Code**, **Codex**, or similar) how to do debate prep properly: research evidence, cut cards, and write cases, rebuttals, frontlines, blocks, and cross-ex, in the standard **Verbatim** Word format.

There is **no AI API and no key** in this repo. Your own agent does the searching and thinking. This repo provides what it needs to do the job right: the protocols, the file format, the integrity rules, and a few small tools that check its work.

> Everything in `examples/` is fictional. No real team's evidence is in this repo.

## What you get

| Folder | What it is |
|--------|-----------|
| `core/` | Rules every task follows: integrity, card anatomy, cite format, cutting and highlighting rules, source evaluation, research protocol, glossary |
| `speeches/` | One protocol per kind of file: `case/`, `rebuttal/`, `frontlines/`, `blocks/`, `crossx/`, `summary-final/`, `prep/` |
| `formats/` | Speech order and times for Policy, LD, and PF, plus a template for your own league |
| `skills/` | Claude Code skills that wrap the protocols (cut-card, research-evidence, build-case, write-rebuttal, build-frontlines, make-blocks, crossx-questions, verify-card, import-team-files) |
| `tools/` | Python (standard library only): build `.docx`, inspect existing files, verify quotes, lint cites, time speeches |
| `templates/` | Blank starter `.docx` files (case, blocks, frontlines) with the Verbatim styles |
| `examples/` | A small fictional example: source article, card spec, generated `.docx` |

## Quick start

```bash
git clone https://github.com/techtanush/OpenSourceDebate.git
cd OpenSourceDebate
cp team.example.yaml team.yaml      # set your initials, cite style, format, wpm
python -m unittest discover -s tests   # sanity check (should say OK)
```

### With Claude Code

Open Claude Code in this folder. It reads `CLAUDE.md` and `AGENTS.md`, and the skills in `skills/` are available. Try:

> Cut a card from this article for the tag "Bordering streets get faster after a ban." Here is the text: ...

or:

> Here is the opposing case (attached). Write a rebuttal to it using the rebuttal protocol.

### With Codex or another agent

Start the agent in this folder and tell it to follow `AGENTS.md`. It has a routing table that sends each request to the right protocol files and tools.

### Using the tools directly

```bash
python tools/build_docx.py examples/example-cards.md -o out.docx
python tools/verify_quotes.py examples/example-cards.md
python tools/lint_cites.py examples/example-cards.md
python tools/inspect_docx.py out.docx --cards
python tools/speech_timer.py out.docx --wpm 250
```

Open `out.docx` in Word to see the Pocket/Hat/Block/Tag hierarchy, cite lines, cyan highlights, and 8pt unread text.

## The workflow in one picture

```
research  ->  save full text  ->  cut card spec  ->  build .docx
                                      |
                       verify_quotes.py + lint_cites.py
                                      |
                  deliver cards + "Before you read these" caveats
```

## Principles

1. **Never fabricate.** Quotes are verbatim. Unverified quotes are labeled.
2. **Evidence is checkable.** Full source text is saved, and a tool checks cards against it.
3. **Honest about weaknesses.** Every deliverable lists source problems and gaps.
4. **Your files are yours.** The toolkit reads your existing files to match your style; it doesn't publish them.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Protocols for more formats, more tools, and fixes to the .docx output are welcome.

## License

MIT. See [LICENSE](LICENSE).
