# Refutation Guide: How to Answer an Argument

How to take an opposing argument, find the best ways to refute it, and turn them into answers a judge can follow. Use it for rebuttals, blocks, and frontlines. Read it with `research-guide.md` (finding the evidence) and `judge-adaptation.md` (lay vs. technical judges).

The most common mistake is answering the **topic** instead of the **argument they actually made**. The second is a pile of unranked answers that contradict each other. This guide fixes both.

---

## 1. The procedure

1. **Get their argument exactly.** The card text, the tag, and what they said in the round. Never answer a version you invented.
2. **State it fairly in one sentence** (the "Neg Argument:" / "Aff Argument:" line). If you can't state it fairly, you don't understand it yet.
3. **Break it into its chain.** Every argument has steps (`argument-structure.md`): uniqueness, link, internal links, impact. Write them down. The best answers attack a specific step.
4. **Find the weakest step and the weakest card.** Apply the hole checklist (section 3).
5. **Pick two to four answers**, strongest first, each backed by a card or the opponent's own text.
6. **Layer them** so they don't contradict (section 4).
7. **Close** by tying the answer back to the resolution or turning the argument.
8. **Time it** and trim the weakest answer first.

---

## 2. The answer types, strongest first

| # | Type | What it does | When to lead with it |
|---|------|--------------|----------------------|
| 1 | **Their own card says otherwise** | Quote a qualifier, concession, or scope limit from *their* evidence | Almost always: it can't be disputed |
| 2 | **No link** | The resolution doesn't cause the claimed harm (it doesn't do what their card assumes) | When their card is about a different action |
| 3 | **Non-unique** | The harm happens (or doesn't) either way | When the status quo already has it |
| 4 | **Turn** | Their mechanism, applied to the resolution, helps you | When you have a card that flips it |
| 5 | **Mitigation** | The effect is smaller, slower, or reversible | When you can't fully deny it |
| 6 | **No impact / outweighs** | Even if true, it's small, or ours is bigger | After you've dealt with the link |
| 7 | **Source or methods attack** | Specific, evidenced problem with their card | Only with a concrete flaw |
| 8 | **Cross-position contradiction** | Two of their arguments can't both be true | Whenever you find one; open with it |

**Rule of thumb for lay judges:** answer their specific cards and their specific claim, not abstract takeouts about the whole case. A takeout ("their whole case fails because...") reads as a reach unless it is airtight and short.

---

## 3. The hole checklist (apply to every card they read)

Go card by card. For each, ask:

1. **Scope.** Does the card cover the same place, people, and time as the resolution? (A pilot, a different country, a different measure.)
2. **Date.** Is it current? Is there newer data?
3. **Qualifiers.** Read the sentences before and after the highlighted words. What did the author say that the highlighting dropped? (`may`, `in some cases`, `we cannot conclude`.)
4. **Method.** Correlation or cause? A comparison group? Sample size?
5. **Source.** Who wrote it, who paid for it, what is their stake?
6. **Number.** Does the number in the tag match the number in the body? Is it relative or absolute?
7. **Direction.** Does the evidence actually point where their tag says?
8. **Link to the resolution.** Does the card's action match the resolution's requirement?
9. **Their other cards.** Does it conflict with something else they read?
10. **The author elsewhere.** Did the same author say something that undercuts it?

Write the result as a short list, one line per hole, then pick the best ones.

---

## 4. Layering answers without contradicting yourself

Answers can be stacked ("even if"), but they must be consistent. Use this order:

```
1. The strongest clean claim (usually their own card, or no link)
2. "Even if that were true,"  a second answer on a different step (non-unique or mitigation)
3. "And in fact,"             a turn (their mechanism helps us)
4. Closing link / weighing    tie it back to the resolution
```

**Checks:**

- A **turn** and a **no-link** can coexist only if you say "even if it linked, it would help us."
- Don't say "the problem doesn't exist" and then "the problem is solved by our plan" without bridging ("even if you grant the problem, our plan solves it").
- If two of your answers need opposite facts, drop the weaker one.
- Don't concede a fact in one block that you deny in another file.

---

## 5. Pulling from context: using the files you already have

You are rarely answering from nothing. Use what is in the files:

1. **The opposing case.** Extract the text (`tools/inspect_docx.py file.docx --text`, or `pdftotext` for a PDF). List every argument, card, and source. Their cards are your best source of answers.
2. **Your own case.** Know your contentions, chain maps, and cards (`python tools/inspect_docx.py case.docx --cards`). Your answers must not contradict them, and your turns should link back to them.
3. **Your block library.** `python tools/library.py search <folder> <terms>`: reuse existing cards and add to the existing block instead of making a duplicate.
4. **The round so far.** If you have a flow or earlier speeches, answer what was actually said and extend only the cards that were actually read.

See `playbooks/02-answer-an-opposing-case.md` for the full procedure.

---

## 6. What the answers look like on the page

Each block (see `speeches/blocks/PROTOCOL.md`):

```
AT: <their argument>
<Opponent> Argument: <fair one-sentence statement>
1. <overview answer: strongest, simplest claim>
2. <specific answer, tag states the point>   + card (often a quote from their own card, or a stronger source)
3. <next answer>                              + card
4. <turn or closing link back to the resolution>
```

- **Tags** are full sentences that state the point and its specifics.
- **Cards** carry the argument; analytics connect.
- **For lay judges,** a short plain analytic follows each card (`judge-adaptation.md`).

---

## 7. How to refute specific kinds of arguments

### "Their numbers are huge" (impact inflation)

- Check scope (national number applied to a local policy), time (annual vs. total), and definition.
- Answer with the denominator: "That figure covers X; the resolution affects Y, which is a small share."
- Check whether the number comes from a worst-case scenario.

### "Our solution fails" (solvency attack)

- Find their evidence's scope: a failed pilot that lacked a key feature (no transit, no funding) does not describe your design.
- Answer with a card about the design features that made it work.
- Concede what's true and narrow your claim ("not every city, but cities that phase it in").

### "The resolution causes this disaster" (DA)

- **Link:** does the resolution do what their link card assumes? Quote the resolution's actual requirement.
- **Uniqueness:** is the "disaster" already happening, or already prevented? (non-unique)
- **Impact:** is the number realistic or a worst case?
- **Turn:** does the resolution reduce the disaster?

### "It's already being solved" (non-unique solvency)

- Show the existing measure's limits with a card: it is partial, new, voluntary, or being fought.
- Show the resolution adds something the status quo lacks.

### "A different solution is better" (counterplan / alternative)

- Show it is not competitive (it can be done alongside the resolution), doesn't solve the harm, or has its own cost.

### "Your evidence is biased"

- Concede the stake, then show a second independent source says the same, or that the methodology is checkable.

### Cross-position contradictions

- Compare their contentions and cards: one says X is strong, another says X is failing. State both with cites, ask which is true, and extend whichever helps you.

---

## 8. Using their evidence against them

Their own cards are the strongest source of answers. Look for:

- **Section titles** ("Why the government will not stop the boom") that undercut their link.
- **Qualifiers** that narrow the claim ("may," "in one pilot").
- **Admissions** of a limit ("the study is observational").
- **Concessions** in the paragraphs before and after the highlighted words.
- **Numbers** that, read in full, support you.

Quote them exactly, with the cite, and say where they appear. Verify against the source text before reading (`integrity.md`); never quote a card you could only see in a snippet.

---

## 9. Common mistakes

| Mistake | Fix |
|---------|-----|
| Answering a weaker version of their argument | State it fairly first |
| A pile of unranked answers | Rank, keep two to four |
| Answers that contradict each other | Layer with "even if" |
| A takeout where a specific card answer was available | Answer their card |
| A source attack with no evidence | Name the flaw and cite it, or drop it |
| No evidence for an answer | Find the card or cut the answer |
| Reading a card you couldn't verify | Mark UNVERIFIED and tell the user |
| Never weighing | Close with why your side matters more (rebuttals) |

See `examples/good-vs-bad/rebuttals.md` for full before-and-after examples.
