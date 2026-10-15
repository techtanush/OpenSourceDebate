# A real 1AC, mapped to the chain standard

> Private-repo material: this walkthrough quotes the tags (not the card text) of a real opposing 1AC in `reference/opponent-files/opponent-1AC-example.docx`. Remove it with `reference/` before making the repo public.

This is how a strong real constructive is built. Read it next to `core/argument-structure.md`. The two contentions below each carry 7-8 cards. The speaker reads the tags and only the highlighted words of each card, with almost no analytic prose.

## Numbers from the real file

| | C1 (Grid) | C2 (Renewables) |
|---|-----------|-----------------|
| Cards | 8 (plus 2 short transition tags: "Scenario 1 is Econ", "Scenario 2 is Meltdowns") | 7 |
| Typical card body | 270-720 words | 360-1,930 words |
| Words actually read per card | about 32-51 | about 27-80 |
| Share of each card read | about 5-15% | about 3-20% |
| Analytic paragraphs between cards | none | none |

So a constructive card is long (lots of unread context for anyone who checks it), only the key words are read, and the argument is carried entirely by **tags and cards**.

## C1: Grid, mapped to the chain

| Step | Tag (as written in the file) | Card |
|------|------------------------------|------|
| **UQ** | Data centers are increasing strain on the grid | Dominici 25 |
| **TREND** | Its getting worse | Riley 26 |
| **IMPACT scale** | Blackouts will be 100x more likely in the next 4 years | DOE 25 |
| *(transition)* | Scenario 1 is Econ | none: a signpost tag |
| **IL** | Blackouts devastate the economy: supply disruption reduces consumption, increases prices, and disrupts transportation | Wing et al. 25 |
| **Terminal impact** | Decline causes nuclear war | Tonnesson 15 |
| *(transition)* | Scenario 2 is Meltdowns | none: a signpost tag |
| **IL / impact** | Grid failure causes existential nuclear accidents | Leyse 25 |
| **Terminal impact** | Extinction | Slocum 15 |
| **SOLVENCY** | Aff solves. Moratoriums allow policymakers to update infrastructure and regulations | Bommarito 26 |

What to notice:

- **Every arrow has a card.** The problem now, how fast it is growing, the scale number (100x), each consequence, the terminal impact, and solvency each have their own card.
- **Two scenarios share one root problem** (grid strain), so one solvency card, tied to the resolution ("Moratoriums allow policymakers to update..."), covers both. If the scenarios had come from different problems, each would need its own.
- **Signpost tags** ("Scenario 1 is Econ") cost a second to read and make the chain easy to follow and flow. They are tags, not analytics.
- **The scale arrives early.** The 100x figure is the third card, so the judge knows how big the problem is before hearing the consequences.

## C2: Renewables, mapped to the chain

| Step | Tag | Card |
|------|-----|------|
| **UQ** | Data center expansion is reversing the renewable transition: coal plant extensions prove | Yanez-Barnuevo 26 |
| **TREND** | They're canceling renewables contracts in favor of gas: speed and cost is all they care about | Varanasi 26 |
| **LINK / SOLVENCY** | The aff forces data centers to transition to renewable energy | Kyc 26 |
| **IL** | That's key to public decarbonization | Flanagan 23 |
| **IL** | Fossil fuels in power generation are the #1 driver of climate change | Johns Hopkins 25 |
| **IMPACT** | Warming causes extinction: impact magnifier and laundry list | Kemp 22 |
| **IMPACT** | AND, it triggers knock-on effects: Extinction | Wright 22 |

The solvency card ("The aff forces data centers to transition...") sits **in the middle of the chain** because it is also the link: it is the card that says the resolution produces the change. Where solvency appears can vary; that it exists, and that it is about the resolution, is what matters.

## What this repo asks for beyond the real file

The real 1AC has no analytic prose, which is the target spirit: cards first. This repo adds two small conventions on top, to make chains easier to check:

1. **A chain map** under each contention (`Chain: UQ (...) -> ... -> SOLVENCY (...)`), so a reader or `lint_case.py` can see every step and its card at a glance.
2. **A `Solvency:` analytic** (one or two sentences) per Aff contention, so the argument that the *resolution itself* causes the impact to fall is stated in words as well as carded.

## Where weaknesses show up in this real file (so you can avoid them)

These are limits a Neg could attack, noted so your own chains are tighter:

- Some impact cards (the meltdown and extinction chain) are about events that could follow *any* long blackout, not specifically about the resolution's grid problem. The more steps between the resolution and the impact, the more the Neg can contest the link.
- The solvency for C1 is a survey of moratorium design ("moratoria serve as a regulatory catch-up mechanism"), not evidence that blackouts actually fall. A stronger solvency card would show reduced outages or demand where a pause was used.
- One card is a 2015 piece about solar storms, which is dated and about a different cause of outage.

Fix the equivalent weaknesses in your own cases: short chains, a solvency card that shows the outcome, and a link that is specifically about the resolution.
