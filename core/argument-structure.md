# Argument Structure: Building a Link Chain

An argument wins when every step between "what is true now" and "why it matters" is proven. A chain with one card and a lot of explanation is a **claim**, not a proven argument. This page defines the parts and the standard each part must meet. It applies to contentions, advantages, disadvantages, and turns.

## The parts of a chain

| Step | Question it answers | Evidence that proves it |
|------|--------------------|-------------------------|
| **Uniqueness (UQ)** | What is the problem or situation *right now*, and how big is it? | Current statistics, official reports, recent studies, named examples |
| **Trend / urgency** (optional) | Is it getting worse, and how fast? | Forecasts, time series, projections with dates |
| **Link** | Why does the plan (or the resolution) change that situation? | A mechanism card: a study, expert, or example showing the action causes the effect |
| **Internal link (IL)** | What does that change cause next? One card per step. | Studies or experts showing each causal step |
| **Impact** | What is the final harm avoided or benefit gained, and how large? | Numbers: deaths, dollars, people affected, scale and timeframe |
| **Solvency** (Aff) | Does the plan actually fix it, and how do we know it works? | Cases where it was tried, expert endorsement, implementation evidence |

For a disadvantage, the same parts apply from the other side: UQ (things are fine now), link (the Aff causes the trigger), internal links, impact.

## The standard

1. **One card per step. Never one card for the whole argument.** If a step has no card, it is an assertion. Write "UQ," "Link," and so on next to each card in your outline and look for gaps.
2. **A contention needs a chain of cards.** In strong constructive files, a typical contention carries about six to eight cards: the problem now, the trend, the key scale number, the mechanism, the consequence, the terminal impact, and solvency. Two cards per contention is a sketch, not a case.
3. **The link must be proven, not described.** The most common weakness is a link written as analytic prose ("removing cars obviously reduces crashes"). Find the card that shows the mechanism. An analogy study can be used if you say what it does and does not show, but you still need the card.
4. **The impact needs size and a timeframe.** "Fewer injuries" is a direction. "About 1.2 million road deaths a year, and X in this city" is an impact. Scale is what makes a chain weighable.
5. **Every card carries a step label in your outline** (and the chain map, below), so the judge, your partner, and the lint tool can see what each card is for.
6. **Analytics connect cards; they are not evidence.** Keep them to a sentence or two between cards. A long analytic paragraph that stands in for a missing card does not count as support.
7. **Hedged evidence is fine if you say how far it goes.** If a card is a London study and your plan is a different city, state the limit in one sentence and add a second card (from a different place or method) so the chain does not rest on a single analogy.

## Solvency: the Aff must prove the resolution causes the impact

On the Aff, **every impact you claim needs solvency**: evidence that *the resolution itself* will actually reduce that impact. Showing that a problem is large is not enough, and showing that a similar action elsewhere helped is not enough unless you tie it to the resolution.

1. **No impact without solvency.** If a contention ends in an impact (deaths, damage, cost), a SOLVENCY card in that contention must show the resolution fixes *that* problem. If a contention has two scenarios from two different problems, each needs its own solvency.
2. **Solvency is about the resolution, not about the problem.** Cards that only say "the problem is bad" or "this action worked somewhere" are UQ and LINK. The SOLVENCY card shows implementation of what the resolution requires and its effect.
3. **Write the solvency sentence.** Every Aff contention ends with a short analytic that starts `Solvency:` and says how the resolution produces the reduction, tied to the card: *"Solvency: <what the resolution does> removes <the cause>, and <card> shows <the impact> falls when it does."* This sentence is the one place an analytic is required.
4. **Make the card match the plan.** If the resolution requires a phase-in, permits, or funding, the solvency card should come from a case that did the same, or the analytic must say how the evidence transfers and what it does not show.
5. **Neg equivalent:** the Neg must prove the resolution causes the harm it claims. The DA link card has to be about the resolution's actual requirements, not a general similar action.

## Cards first, analytics last

Evidence does the arguing. Analytics only connect and clarify, and on the Aff their main job is the `Solvency:` sentence.

- **Allowed analytics in a contention:** the chain map, one `Solvency:` sentence or two, and an optional one-sentence impact framing (size, who is affected, timeframe).
- **Everything else should be a card.** If you want to explain the mechanism, find the card that explains it. If you want to claim a number, find the card with the number.
- **Budget:** analytics should be a small fraction of what is spoken. `tools/lint_case.py` warns above 30% and fails above 50% of (analytic words + words read from cards). An analytic over about 60 words is a warning.
- **Don't write a paragraph of explanation under each card.** A one-line "source note" to flag a limit is fine; a paragraph is a sign the card is missing.

## The chain map

Open every contention with a one-line analytic that names each step and the card that proves it. This is the checklist for you and for any reader:

```
Chain: UQ (Reyes 25) -> LINK (Whitfield 24) -> IL (Park 23) -> IMPACT (WHO 24) -> SOLVENCY (Larkspur 25)
```

Use these step names: `UQ`, `TREND`, `LINK`, `IL`, `IMPACT`, `SOLVENCY`. `tools/lint_case.py` reads this line and checks it against the cards that follow. For a contention with two scenarios, list each impact and its solvency, e.g. `... -> IMPACT (A) -> IMPACT (B) -> SOLVENCY (C)`.

## Testing a chain

Before delivering a case or a DA, run this test:

1. **Remove each card in turn.** Does the argument still stand? If removing a card does not matter, the card is padding. If removing it breaks the chain, make sure a second card backs it up.
2. **Read only the tags.** Do the tags alone tell the story from the problem now to the final impact? If there is a jump, you are missing a step.
3. **Ask the opponent's best question at every arrow.** "Why does that cause that?" The answer must be a card.
4. **Check the numbers line up.** The UQ scale, the link's effect size, and the impact's size should be consistent with each other. If they are not, say why.

## Impact framing vs. weighing

- In a **constructive** (Pro or Con), frame each impact: state its size, who is affected, and its timeframe, and note whether it is reversible. This is a few sentences of analytic around the impact card.
- **Comparing** your impact to the opponent's (probability, magnitude, timeframe, reversibility, and which one the judge should prefer) is done in the **rebuttals**, when you know what the other side argued. See `speeches/rebuttal/PROTOCOL.md` and `speeches/summary-final/PROTOCOL.md`.
- Do not skip impact framing in a constructive, and do not spend constructive time on a head-to-head comparison against arguments that have not been made yet.

## Common weaknesses (what to fix first)

| Weakness | Fix |
|----------|-----|
| One card per contention | Add a card for each missing step; target at least four to six |
| No uniqueness: the problem is asserted | Add a current statistic or report |
| Link is analytic prose | Find the mechanism card; if none exists, narrow the claim |
| Impact has no number or timeframe | Add a magnitude card |
| Everything rests on one analogy | Add an independent second source |
| Long analytics doing the evidence's job | Replace each with a card, keep one connecting sentence |
| No solvency, or solvency for a different problem | Add a card showing the resolution itself fixes this impact, plus the `Solvency:` sentence |
| Paragraphs of analytics under each card | Delete them, find the missing card, keep one connecting sentence |

Run `python tools/lint_case.py case.md` to check structure.
