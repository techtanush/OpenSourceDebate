# Contributing

Thanks for helping. A few ground rules keep the repo useful and safe to share.

## What's welcome

- Protocols for more formats or speech types (put format data in `formats/`, protocols in `speeches/`).
- Improvements to the `.docx` output (Verbatim compatibility fixes are especially valuable).
- New checks in `tools/` (standard library only, with tests).
- Clearer protocol docs and better examples.

## What not to add

- **Real teams' evidence or files.** The repo is topic-agnostic. `examples/` is fictional, so write new examples from scratch.
- Copyrighted article text, even as a "source" fixture. Write your own fictional text.
- Dependencies that need `pip install`. Keep the tools standard-library only.
- Anything that calls a paid API. The agent brings its own tools.

## Before opening a pull request

```bash
python -m unittest discover -s tests
python tools/build_docx.py examples/example-cards.md -o /tmp/check.docx
python tools/verify_quotes.py examples/example-cards.md --strict
python tools/lint_cites.py examples/example-cards.md
python tools/lint_cards.py examples/example-cards.md
python tools/lint_blocks.py examples/example-cards.md
python tools/lint_case.py examples/example-case.md
python tools/verify_quotes.py examples/example-case.md --strict
```

All must pass. If you change the docx output, add or update a test in `tests/` and open an example in an editor that supports Verbatim-style formatting to confirm it still renders correctly.

## Style

- Protocols: short, step-by-step, with a quality checklist. Keep one source of truth (skills and AGENTS.md should point to protocol files, not duplicate them).
- Python: readable, no clever one-liners, docstrings for tools.
- Be honest in examples: fictional is labeled fictional.

## License

By contributing you agree your contribution is licensed under the repo's MIT license.
