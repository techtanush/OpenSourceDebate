# Link Chains: Good and Bad

Examples of weak chains and how to repair them, plus a full good chain. Standard: `core/argument-structure.md`. All topics, sources, and numbers here are fictional. The good chain exists as a working file you can lint: `examples/example-case.md`.

How to read the "bad" versions: each one is a plausible attempt that an agent or a new debater would produce. The diagnosis says what a judge or opponent would do to it.

---

## The good chain (the target)

Contention: *Downtown car traffic is injuring and killing people.*

```
Chain: UQ (Larkspur RSB 25) -> TREND (Larkspur OTP 25) -> LINK (Venkataraman 25) -> IL (Meridian 24) -> IMPACT (NESC 24) -> SOLVENCY (Fairhaven DPW 25)

UQ        Larkspur's downtown is under 2% of the city's land but produces nearly a third of walking and cycling injuries
TREND     Car entries rose 17% and downtown injuries rose 22% since 2019, and the city forecasts more
LINK      Restricting cars in downtown cores cut walking and cycling injuries 36% across eleven cities, with no rise on bordering roads
IL        Each serious injury costs about $187,000, and about 41% of that is paid by public programs
IMPACT    Urban pedestrian and cyclist deaths hit a four-decade high of 7,310, and the cost exceeds $140 billion a year
          Impact: these deaths cannot be made up later, they fall on people with little choice about their exposure, and the toll has risen for a decade.
SOLVENCY  Fairhaven cut core injuries 40% with no rise on bordering streets, because it phased in with transit and permits
          Solvency: our plan requires the same phase-in, permits, and edge transfers, so the resolution removes the cars that cause the Larkspur injuries, and Fairhaven shows the injuries fall when it does.
```

Why it works:

- **Every arrow is a card.** Read the tags alone: the problem now, it is growing, here is what the action does, here is what each injury costs, here is the scale, here is proof it works.
- **The numbers fit.** A local problem (Larkspur) is linked to a multi-city mechanism, then scaled to a national impact with a stated cost, then proven by a city that did it.
- **Analytics are tiny** (one impact sentence, one solvency sentence) and everything else is evidence.
- **Solvency is about the resolution.** The Fairhaven card shows the same design the plan requires (phase-in, permits, edge transfers).

---

## Bad chain 1: one card and an essay

```
Contention 1: Cleaner air
  [1 card: a study of one street's pollution before and after a closure]
  [300 words of analytic explaining why this is a big deal, why it matters for health,
   and why the opponent is wrong to say it only moved pollution elsewhere]
```

**What the opponent does:** "One street. One study. Everything else is the Aff's say-so." They answer the study (scope: one street) and ignore the essay, because an essay is not evidence.

**Diagnosis:** one card plus prose is a *claim*, not a chain (`argument-structure.md`). Analytics were doing the evidence's job; `lint_case.py` reports it as "only 1 card," "no chain map," and "analytics are N% of what is spoken."

**Fixed:**

```
Chain: UQ (...) -> LINK (...) -> IL (...) -> IMPACT (...) -> SOLVENCY (...)
UQ        downtown air pollution levels now, with a number (monitoring report)
LINK      closing streets to cars lowered roadside pollution, with a comparison street (study)
IL        that pollution causes this health effect, per case (health study)
IMPACT    the size of the health harm: cases and cost per year (national figure)
SOLVENCY  a city that closed streets and measured the improvement (evaluation)
Solvency: [one or two sentences tying the resolution to the card]
```

Delete the essay. Where it had a real point (for example, that pollution did not just move), find the card for that point and add it as a second LINK card.

---

## Bad chain 2: the missing middle (a jump)

```
UQ     Traffic congestion is rising downtown.          [card]
IMPACT Congestion causes millions of deaths worldwide. [card]
SOLVENCY The plan reduces congestion.                  [card]
```

**What the opponent does:** "Congestion is delays. Where does it kill anyone?" The judge hears a leap from "traffic is slow" to "millions die."

**Diagnosis:** a step is missing. Congestion and deaths are different things. The tag-story test ("which means...") fails between tags 1 and 2.

**Fixed:** decide what actually connects them. If the real harm is crashes, make that the chain (UQ: crash numbers; LINK: restrictions reduce crashes; IMPACT: deaths). If the real harm is air pollution, make that the chain. Do not borrow a global death figure for a local delay problem.

---

## Bad chain 3: the scope mismatch

```
UQ       One city's downtown has too many injuries.      [card: Larkspur]
IMPACT   Traffic kills 1.2 million people a year.        [card: global figure]
SOLVENCY Our plan will save those lives.                 [card: a pilot in one city]
```

**What the opponent does:** "The plan covers one downtown. The 1.2 million is every road on Earth." The judge sees an inflated impact.

**Diagnosis:** the scale of the impact is not the scale of the resolution. `logic-flow.md`: *numbers must fit.*

**Fixed:** use the impact figure that matches what the resolution affects (downtown injuries and deaths in cities of this size), and say how it scales (cities with similar downtowns, a national share). If you want the large number, add a card about how many cities and downtown cores are in scope and be honest that the plan affects a share of the total.

---

## Bad chain 4: the link as prose

```
UQ      Downtown injuries are high.                      [card]
LINK    (analytic) "Removing cars obviously reduces crashes, because crashes require cars."
IMPACT  Injuries are costly.                             [card]
```

**What the opponent does:** "Obviously? Show me a study. Maybe drivers go faster on the streets next door."

**Diagnosis:** the link is the step they will attack, and it has no card. An analytic asserting the mechanism is not proof.

**Fixed:** find a controlled before-and-after study or a review of cities that did it (`research-guide.md`, LINK section). Keep the one-line analytic only as a connector.

---

## Bad chain 5: the impact with no number

```
IMPACT  "People are hurt downtown and that is bad."      [card that says injuries are painful]
```

**What the opponent does:** "How many people? Compared to what?" Nothing to weigh.

**Diagnosis:** an impact needs a size and a timeframe so it can be compared with the opponent's impact in the rebuttals.

**Fixed:** a card with a number ("7,310 deaths in 2023, a four-decade high; cost over $140 billion a year") plus one sentence of framing: who it falls on and why it can't be undone.

---

## Bad chain 6: solvency for a different problem

```
UQ       Downtown air is polluted.
IMPACT   Pollution shortens lives.
SOLVENCY "Cities that built bike lanes saw more cycling."    [card]
```

**What the opponent does:** "More bike lanes isn't a car ban, and more cycling isn't cleaner air."

**Diagnosis:** the solvency card does not show that *the resolution* reduces *this impact*. It shows a nearby action raising a different measure.

**Fixed:** a card from a place that did what the resolution requires and measured pollution afterward. Add the `Solvency:` analytic: *what the resolution does, how that removes the cause, and what the card shows happened.*

---

## Bad chain 7: padding (three cards saying the same thing)

```
LINK  Study A: restrictions cut injuries
LINK  Study B (same dataset as A): restrictions cut injuries
LINK  News article summarizing study A
```

**Diagnosis:** the contention looks like it has three cards but has one piece of evidence. A judge who knows it cannot count it three times, and the time is wasted.

**Fixed:** keep the best one and spend the time on a different step (or an independent second source for the link: a different city, a different method).

---

## Bad chain 8: the contradiction

```
Contention 1: transit is excellent, so people will switch to it.        [card]
Contention 2: transit is failing and the plan will rescue it.           [card]
```

**What the opponent does:** "Which is it?" They read both of your cards back.

**Fixed:** reconcile in one story: *transit is good enough on the main corridors, and the plan funds the gaps.* State it once, and make sure each card supports the version you commit to (`logic-flow.md`, contradictions).

---

## Bad chain 9: hedged into nothing

```
LINK "A study of a similar thing in another place suggests the effect might apply, though it is not exactly the same."
(then the analytic spends 150 words explaining everything the study does not show)
```

**Diagnosis:** the analytic is arguing against its own card.

**Fixed:** state the limit in one sentence, then add a second, independent card (a different place or method) so the link does not rest on one analogy.

---

## A good Neg chain (DA)

Contention (DA): *The ban strands workers who cannot reach downtown without a car.*

```
Chain: UQ (...) -> LINK (...) -> IL (...) -> IMPACT (...)
UQ      Downtown shift workers already rely on cars at hours when transit does not run (workforce survey, with a number)
LINK    The resolution bans ordinary cars in the core, with no early or late service requirement (the resolution's own text and an analysis of what it requires)
IL      Workers who cannot get to a job lose it; displaced workers lose income (labor study with a number)
IMPACT  Number of workers affected and lost earnings per year (economic estimate)
```

Note the **link card is about what the resolution actually requires**. A DA built on "bans hurt workers" in general, with no card tied to the resolution's text, is the Neg's version of a bad solvency card.

---

## A good turn chain (in a block)

Opponent: "The ban pushes drivers onto surrounding streets, so injuries rise there."

```
1. (overview) The surrounding streets got safer, not more dangerous.
2. Card: multi-city study, injuries on bordering roads did not rise (and fell 2% on average).
3. Card: the same study, injuries inside the zone fell 36%.
4. (closing link) So their harm happens on the streets the ban makes safer: this is a turn.
```

Each tag is a full sentence with its number, each step has a card, and the closing sentence links back to the resolution.

---

## Quick self-check for any chain

1. Read only the tags. Say "which means..." between them. Does it hold?
2. Mark each tag UQ / TREND / LINK / IL / IMPACT / SOLVENCY. Is any missing?
3. Is the link a card? Does the impact have a number? Is solvency about the resolution?
4. Remove one card at a time. Does the chain still stand? If a card isn't needed, it is padding.
5. Run `python tools/lint_case.py` and `python tools/tag_story.py`.
