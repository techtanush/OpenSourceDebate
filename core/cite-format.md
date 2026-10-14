# Cite Format

A good cite lets a judge or opponent find the source, judge the author, and see when it was written. Every cite needs the fields below. Order and punctuation follow one of two common house styles; pick one in `team.yaml` and use it everywhere.

## Required fields

| Field | Notes |
|-------|-------|
| **Short cite** | `Lastname YY` (year in two digits). Use `Org YY` if there is no author (`DOE 25`). Add `et al.` for three or more authors (`Gour et al. 26`). Use a month-day form (`Subin 9-14`) only for very recent articles, so two cards from the same author and year can be told apart. |
| **Full author** | The person's full name. If there is no individual author, the organization. |
| **Qualifications** | Why this person is credible on *this* claim: position, employer, degrees, years of experience. This is where debaters spend the most words. Use the author's real credentials only. Never invent or inflate them. |
| **Date** | Publication date, `M-D-YYYY` (or `M/D/YY`). Use the most recent update date only if the source shows one, and say "updated." |
| **Title** | Exact article or report title, in quotes. |
| **Publication** | Outlet, journal, or organization. |
| **URL** | Full link. |
| **DOA** | Date you accessed it (or read the full text). |
| **Cutter initials** | Who cut the card, so questions go to the right person. |

If a field truly isn't available (no date, no author), write `n.d.` or `no author` explicitly. Do not leave it blank, and do not guess.

## Style A: "frontline" (bracketed)

```
**Reyes 25**, [Marcus Reyes, Senior Fellow @ Example Transit Institute, 5-4-2025, "Article title," Example Transit Institute. DOA: 9-1-2026 https://...] //AB
```

The initials tail is often `//AB` and may add `//recut` when someone re-cut another person's card.

## Style B: "case" (parenthesized)

```
**Whitfield 25** (Dana Whitfield, 13 years covering urban transport, Example Urban Review, 1/2/25, "Article title", https://...) AB - DOA: 9/11/26
```

Both styles are produced by `tools/build_docx.py` via `style: frontline` or `style: case`. For anything unusual, use `raw:` and write the text after the bold short cite yourself.

## Choosing the credential line

Good qualifications answer "why should we believe this person about this?"

- Strong: "Senior Fellow at a named research institute, PhD in economics, 15 years studying labor markets."
- Weak: "Writer." "Blogger." If that's all you can find, say so in your notes. Prefer a better source.

For an organization: say what it is ("nonprofit watchdog," "industry trade group," "federal agency") so the judge can weigh bias.

## Checking a cite

Run `python tools/lint_cites.py spec.md`. It flags missing fields and malformed short cites. It cannot tell you whether the credentials are true, so confirm those from the source page.
