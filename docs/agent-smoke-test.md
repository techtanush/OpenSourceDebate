# Agent smoke test

Run this by hand in a clean Claude Code or Codex session (no memory of this repo) to confirm the protocols work.

1. Start the agent in the repo root. Do not paste any instructions beyond the prompt below.
2. Prompt: *"Cut a card from `examples/source-article.txt` for the tag 'Retail sales held steady in most cities after a ban.' Use the repo's protocols."*
3. Expected behavior:
   - reads `AGENTS.md`, then `core/integrity.md` and `core/cutting-rules.md`;
   - writes a spec with `source: examples/source-article.txt` and a full cite;
   - runs `build_docx.py`, `verify_quotes.py --strict`, and `lint_cites.py`;
   - finishes with a "Before you read these" list.
4. Negative test: ask it to cut a card from a snippet it cannot verify. It should label the card UNVERIFIED instead of presenting it as a clean card.
5. Record the result (pass/fail, agent, date) in an issue or PR.

## Checking the .docx in CardMirror

Open the generated file in CardMirror (see `docs/CARDMIRROR.md`) or in Word with Verbatim and check: the Navigation pane shows Pocket > Hat > Block > Tag; the short cite is 13pt bold and the rest of the cite is 8pt; read text is underlined with cyan highlight; unread text is 8pt. macOS Quick Look, TextEdit, and Pages ignore Word styles, so they will not show this correctly.
