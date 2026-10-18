# Cards: Good and Bad

Examples of cutting and highlighting, all from the fictional article in `examples/source-article.txt`. Rules: `core/cutting-rules.md`, `core/integrity.md`. Markup: `==read==`, `__underline__`, plain = unread context.

---

## 1. The lone sentence (no context)

**Bad**

Tag: *Restricting cars reduces injuries.*
Body: `==Foot traffic rose, and total sales were flat to slightly up in eleven of the twelve cities.==`

- The tag is about injuries; the sentence is about sales.
- There is no text around it, so no one can see what was measured or who said it.

**Good**

Tag: *Sales were flat to slightly up in eleven of twelve cities, and foot traffic rose.*
Body: the paragraph that introduces the quote (the study design and the public dataset), the quote itself with `==Foot traffic rose, and total sales were flat to slightly up in eleven of the twelve cities.==`, and the sentences after it about the nine percent travel-time result.

---

## 2. Cutting out the qualifier (the dangerous one)

The source says: *"A ban without a working alternative just moves the problem," Reyes said.*

**Bad (Neg's cut of the same line)**

Tag: *Experts admit bans just move the problem.*
Body: `==A ban ... just moves the problem==`

- The highlighting removes "without a working alternative," which reverses the author's meaning.
- If an opponent catches this, you lose credibility and the card.

**Good**

Tag: *The study's failure case is a ban with no working alternative.*
Body: `==A ban without a working alternative just moves the problem,== Reyes said. In the one city where sales fell, buses ran only every forty minutes and the ban took effect with no change to service.`

- The qualifier stays. The tag is exactly what the text supports. Also see `integrity.md`: never change what the author means.

---

## 3. Tag claims more than the text

**Bad**

Tag: *Car bans save lives.*
Read text: `==Average travel times on the streets bordering each ban zone fell by nine percent==`

- The text is about travel time on bordering streets. It does not say anything about lives.

**Good**

Tag: *Travel times on streets bordering ban zones fell nine percent.*
Read text: the same sentence.

(If you want a "saves lives" tag, you need an injury or death card, not a travel-time card. See `link-chains.md`.)

---

## 4. Too much highlighting / fragments

**Bad**

`Average ==travel times== on the ==streets bordering== each ban zone ==fell== by ==nine percent==, because ==drivers== switched to ==transit== or took ==different routes==`

- Choppy: it is hard to read aloud and looks like a trick.

**Good**

`==Average travel times on the streets bordering each ban zone fell by nine percent, because drivers switched to transit or took different routes before ever reaching downtown.==`

- One continuous, readable sentence. The rest of the paragraph is unread context.

---

## 5. A card that is a summary or a snippet

**Bad**

Body written from a search result: "The study found car bans reduce traffic." (no source text saved)

- Not the author's words. `verify_quotes.py` has nothing to check it against. Label it UNVERIFIED and tell the user, or find the real text. See `integrity.md`.

**Good**

Full article saved to `sources/whitfield-25.txt`; the card body is a verbatim excerpt; `python tools/verify_quotes.py spec.md --strict` passes.

---

## 6. A weak cite

**Bad**

`Whitfield, a writer, March.`

**Good**

`Whitfield 25 [Dana Whitfield, Staff Writer at The Example Urban Review, reporting on a four-year study by the Example Transit Institute, 3-3-2025, "Downtown Car Bans Cut Congestion Without Hurting Retail, Study Finds," The Example Urban Review. DOA: 10-14-2026 https://example.com/downtown-car-bans-study] //XX`

- Credentials say why to believe the source; the date and DOA let anyone check it.

---

## 7. Context that includes the weakness (and why you want it)

A good card keeps nearby sentences that show limits, because the opponent will find them and your credibility depends on having seen them first. In this article the limit is: *"Critics say twelve cities is a small sample..."* If you cut the card to hide it, a clever opponent reads it back. If you keep it as unread context, you can answer: "The author says the results should not be stretched to very large cities; our resolution is about cities of a few hundred thousand."

---

## Checks

```bash
python tools/verify_quotes.py spec.md --strict   # card text is verbatim from the saved source
python tools/lint_cites.py spec.md               # cites complete
python tools/lint_cards.py spec.md               # no lone-sentence cards
```

The tools catch #1, #5, and #6. Items #2, #3, and #4 need judgment: read the tag, then only the highlighted words, and ask whether the author would agree.
