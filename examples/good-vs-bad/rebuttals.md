# Rebuttals: Good and Bad

Side-by-side examples. Method: `core/refutation-guide.md`. Judge-type rules: `core/judge-adaptation.md`. The working files are in this folder; run the commands at the end to see the tools pass the good one and fail the bad one. Fictional topic and sources.

## The situation

The Neg read a card about a pedestrian pilot in a city called Ashford (`sources/opponent-ashford-pilot.txt`) with this argument:

> *Downtown stores lost 18 percent of their sales when Ashford closed streets to cars, so a ban will wreck local business.*

You are the Aff in your rebuttal, speaking to lay judges, with about two minutes for this argument.

---

## The bad rebuttal (`rebuttal-bad.md`)

```
AT: Retail collapse
1. Extend Smith 24: it says retail would drop 18 percent. This is a bad argument because the Neg's case is built on a single source and their whole case fails, because as we have explained across the entire round many studies show that car bans are good for downtown retail...
2. Retail is fine.      (Extend Whitfield from our case: it says retail does well.)
3. Their source is biased. (The Ashford Chamber is clearly biased and cannot be trusted. Also the plan helps transit riders. Also cars cause pollution.)
```

What is wrong, point by point:

| Problem | Why it hurts |
|---------|--------------|
| No statement of what they argued | The judge doesn't know what is being answered |
| "Extend Smith 24" | That is not even their card (the card is Reyes 24), so it is a misquote. Never name a card you haven't read. |
| A 70-word run-on analytic | A lay judge loses it; there is no card behind it |
| "Retail is fine" with "Extend Whitfield" | No card in the file, and a one-word tag is not an argument; the evidence was never read |
| "Biased" with no evidence | A source attack with no named flaw is a reach |
| Three unrelated points ("also...") | Not ranked, not connected to their argument |
| Never uses their own card | The strongest answer is sitting in their own evidence |

Tools: `python tools/lint_blocks.py examples/good-vs-bad/rebuttal-bad.md` reports 4 errors (no cards, tags with no cards, no argument statement).

---

## The good rebuttal (`rebuttal-good.md`)

```
AT: Retail collapse
Neg Argument: Downtown stores lost 18 percent of their sales when Ashford closed streets to cars, so a ban will wreck local business.
1. That pilot was four streets with no bus changes, and sales came back by the end of the summer.
2. The pilot covered four blocks, changed no bus service, and sales recovered to within three percent      [card: Reyes 24, their source]
   So the drop they read was four streets with no buses added, and by the end of summer it was nearly gone.
3. A four-year study of twelve cities found sales flat to slightly up in eleven of them                                   [card: Whitfield 25]
   That is far more cities, over four years, than one short pilot.
4. The one city where sales fell had no change in transit service, and the plan requires frequent service                [card: Whitfield 25]
   The only bad result happened without buses, and our plan will not start without them.
5. So their evidence describes what happens when a city closes streets and walks away, which is exactly what our plan does not do.
```

Why it works:

1. **It answers their specific card first.** Answer 1 and 2 quote their own source: four blocks, no bus changes, recovery within three percent. That cannot be disputed; they read it.
2. **It layers without contradicting.** First their own card (no link at scale), then more evidence (twelve cities), then a turn (their failure case is the condition our plan fixes).
3. **Each answer has a card.** The cards are cut with context before and after, and only the key words are read.
4. **Plain sentences after cards** for a lay judge, with no labels.
5. **It closes on the resolution**: what their evidence describes is not what the plan does.
6. **It fits two minutes with room to spare**: the timer reports 293 spoken words, about 1:10 at 250 wpm, so there is space for one more answer.

Tools: all of these pass for the good file:

```bash
python tools/verify_quotes.py examples/good-vs-bad/rebuttal-good.md --strict
python tools/lint_cites.py examples/good-vs-bad/rebuttal-good.md
python tools/lint_blocks.py examples/good-vs-bad/rebuttal-good.md --lay
python tools/lint_cards.py examples/good-vs-bad/rebuttal-good.md
python tools/build_docx.py examples/good-vs-bad/rebuttal-good.md -o rebuttal-good.docx
python tools/speech_timer.py rebuttal-good.docx --wpm 250
```

---

## How the good rebuttal was found (the thinking, step by step)

1. **Their card:** read the Ashford article in full, not just the tag. The paragraph before and after the 18% figure shows the pilot was four blocks, bus service did not change, and sales recovered.
2. **Holes found** (hole checklist, `refutation-guide.md`): scope (four blocks vs. a downtown), their own qualifier (no bus changes), the recovery, a date (one summer), and a conflict with our evidence.
3. **Strongest first:** their own card (can't be disputed) → bigger evidence (twelve cities) → a turn (their failure case is the condition the plan fixes).
4. **Research gaps** (`research-guide.md`, section 6): none of the answers needed a new search, because the best answers were in their card and our existing evidence. If it had needed more, the next search would be "pedestrian zone sales recovery after pilot."
5. **Contradiction check:** answers 2-4 all say "sales are fine at scale and with transit," which is consistent with the plan, so they stack.

---

## Other bad rebuttals to avoid

### The takeout

```
AT: Retail collapse
Their whole case is just fear of change and every study shows they're wrong, so this argument is not worth the judge's time.
```

- No evidence, dismissive, and a lay judge may take it as avoiding the argument.

### The unsupported turn

```
Actually, banning cars helps retail a lot, because more people walking means more customers.
```

- A turn needs a card. As spoken it is a claim with no support.

### The source attack with no flaw

```
The Business Journal is a biased newspaper.
```

- Say what is biased and prove it, or leave it out. Here the stronger move is to use their card against them.

### The contradiction between files

A block says "the ban causes no traffic anywhere" while a different block says "the ban moves cars away from downtown." Reconcile before delivering (`core/logic-flow.md`).

---

## The same argument in a technical round

Tech version (see `analytics.md`): same evidence, numbered layers, shorthand, explicit weighing after the answers: "Even if some stores lose short-term, the pilot recovered within three percent, the plan phases in with delivery windows, and our injury impact is permanent while theirs is temporary: prefer ours on timeframe and reversibility."
