# Research Protocol

How an AI agent (Claude Code, Codex, or similar) should research evidence for a debate. The agent brings its own search and browsing tools. This repo supplies the process.

## The loop

```
1. Define    -> exactly what claim do we need to prove or answer?
2. Search    -> find candidate sources (several angles; prefer recent, credible)
3. Fetch     -> get the FULL TEXT and save it to sources/<shortcite>.txt
4. Select    -> pick the best passage for the claim
5. Cut       -> write the card spec (core/cutting-rules.md)
6. Verify    -> tools/verify_quotes.py + tools/lint_cites.py
7. Report    -> deliver cards + a "before you read these" caveats list
```

Do not skip step 3. A card cut from a search snippet is UNVERIFIED (`integrity.md`).

## 1. Define the need

Write it as a tag-shaped sentence ("City bus ridership rises when service runs more often"). Also note:

- What would count as a strong source (an agency? peer review? a named expert?).
- What the opponent is likely to say back.
- Whether you need a number, a mechanism, an example, or an expert opinion.

## 2. Search well

- Run several differently worded searches, not one.
- Search for the **claim** and for the **counter-claim**, so you know what the other side can cite.
- Prefer primary sources: reports, filings, data, studies. Use news to find them.
- Note the publication date for every result. Reject stale evidence on fast-moving facts.
- Look for the same fact in two independent sources.

## 3. Fetch and save full text

- Fetch the page and save the full article text to `sources/<shortcite>.txt` (strip nav and ads, keep the article exactly as written).
- If your tool only returns a **summary**, ask it for the verbatim passage and still treat the result as UNVERIFIED until you have the page text.
- If the page is blocked (403, bot check, paywall), follow "When a page cannot be fetched" in `integrity.md`. Never solve a CAPTCHA or bypass a paywall.
- Record: author, credentials, date, title, publication, URL, date accessed.

## 4-6. Select, cut, verify

See `cutting-rules.md`. Then:

```bash
python tools/build_docx.py cards.md -o cards.docx
python tools/verify_quotes.py cards.md --strict
python tools/lint_cites.py cards.md
```

## 7. Report

Always end with a short plain-language list:

- **Verified** vs. **UNVERIFIED** cards.
- Source problems: bias, age, republished copies, missing credentials.
- Places where an opponent could attack the highlighting or the tag.
- What you could not find.

## Working with the user's existing files

If the user has a folder of prior files, run `python tools/inspect_docx.py <file>.docx` on a few of them to learn their cite style, heading conventions, and highlight habits, then follow their conventions (`skills/import-team-files/`). Do not copy their evidence into another project or share it publicly.

## Time and effort

Match depth to the request. A single card needs one good source. A full block or case file needs breadth: several sources per argument, counter-evidence, and a note on each source's weaknesses.
