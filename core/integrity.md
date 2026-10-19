# Evidence Integrity Protocol

Read this before cutting, quoting, or summarizing any evidence. These rules apply to every task in this repo.

## The rules

1. **Never invent evidence.** No made-up quotes, authors, dates, statistics, URLs, or credentials. If you cannot find it, say so.
2. **Words inside a card are verbatim.** A card body is an excerpt of the source with the source's own words, in the source's order. You may:
   - omit text and mark it with `...`;
   - change a word for clarity and mark it with `[brackets]`;
   - normalize whitespace and curly vs. straight quotes.
   You may **not** paraphrase, reorder, or "clean up" the wording.
3. **Cut from full text, not from summaries.** A search snippet, a fetch summary, or a model's paraphrase of a page is not the source. If your only access is a summary, the quote is **UNVERIFIED** (see below).
4. **Save the source text.** Put the full article text in a file (e.g. `sources/author-yy.txt`) and point the card's `source:` at it, so `tools/verify_quotes.py` can check the card.
5. **Record the date accessed (DOA)** for every online source, in the format the team uses.
6. **Do not change what the author means.** Highlighting that flips a claim ("not", "may", "some") is cutting out of context. Keep qualifiers that change the meaning.
7. **Cites come from the page, never from memory.** Take the author, credentials, date, title, publication, and URL from the fetched page (or its metadata). If the page does not show an author or date, say so in the cite or the report; do not guess. A real URL with an invented author is still fabrication.
8. **No notes to yourself inside the file.** Do not leave cutter initials, tool or assistant names, "re-cut" notes, TODOs, or "find a card" reminders in a finished card or block. Put open problems in your report to the user instead.
9. **Disclose weaknesses.** If a card is from a biased source, an old source, a summary, or only partly supports the tag, say so in a short note to the user.

## Statuses

| Status | Meaning | What to do |
|--------|---------|------------|
| VERIFIED | Full source text saved and `verify_quotes.py` passes | Safe to use |
| UNVERIFIED | Quote came from a snippet, summary, or memory | Tell the user plainly; they must check the live page before reading it as a card |
| MISMATCH | Body text is not in the source | Fix the card; never "adjust" the source to match |

## When a page cannot be fetched

Pages sometimes return 403/404, a bot check, or a paywall. In order:

1. Try the browser tool if your agent has one (see `research-protocol.md`).
2. Try a republished copy from a reputable aggregator, and say it is a republication.
3. Use the search snippet only to **locate** the article. Do not cut from it.
4. If the text still can't be read, give the user the link, the tag, and the exact lines the search showed, labeled UNVERIFIED.

Do not complete a bot check or CAPTCHA yourself, and do not bypass a paywall.

## Reporting back

After producing cards, finish with a short "Before you read these" list covering: anything UNVERIFIED, any source with a clear bias or conflict of interest, any card whose date or credentials you could not confirm, and any highlighting the opponent could attack. Be plain about problems. Do not hide them.

## Numbers

Quote numbers exactly as the source prints them. If two sources disagree, give both and say which you used and why. Do not do your own arithmetic and present it as the author's claim; label it as your analysis.
