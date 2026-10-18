# Analytics: Good and Bad

Analytics are the short sentences you write yourself between cards. Evidence does the arguing; analytics connect and explain. Standard: `core/argument-structure.md` (cards first) and `core/judge-adaptation.md` (lay vs. tech). Fictional topic.

---

## What analytics are for

| Job | Example | Where |
|-----|---------|-------|
| State the opposing argument fairly | `Neg Argument: Downtown stores lose sales when cars are banned.` | Top of a block |
| Overview answer | `1. Their own card says it was four streets with no bus changes.` | Start of the answers |
| Connect or explain a card (lay) | `So the cars did not move next door; the streets around the area got faster.` | Right after a card |
| Solvency sentence (Aff case) | `Solvency: our plan requires the same phase-in and permits, so it removes the cars that cause the injuries, and Fairhaven shows injuries fall when it does.` | End of a contention |
| Closing link or turn | `4. So their harm is what happens when a city closes streets and walks away, which our plan does not do.` | End of a block |

Not for: introducing numbers no card supports, replacing a missing card, or repeating what the tag already says.

---

## Bad analytics

### A. The essay

> The study shows that downtown streets will be much safer, which is very important because safety is one of the most fundamental values that a city must consider, and when we weigh that against the supposed economic losses the other side keeps pointing to, it is clear that the impact of increased safety outweighs any possible negative effect on merchants, especially considering that merchants in other cities have adapted over time.

- 70 words, no number, no card behind the weighing claim ("merchants adapted"), and a head-to-head comparison that belongs in the rebuttal.
- `lint_case.py` warns on analytics over 60 words and fails when analytics outweigh the cards.

### B. The AI label

> LAY VERSION: Cars -> more crashes -> fewer people walking. Simply put: bans good.

- Labels like "LAY VERSION" or "Simply put," and arrows, read like notes to a reader, not like a team's file. `lint_blocks.py --lay` warns on both.

### C. The new number

> Solvency: the plan will cut injuries by 73 percent.

- 73 appears in no card. `lint_case.py` warns: "analytic uses number(s) 73 that appear in no card of this contention."

### D. The restated tag

> This card says injuries fell.

- Adds nothing. If the tag already says it, cut the analytic.

---

## Good analytics

### Lay (plain sentence right after the card)

Card: *Average travel times on the streets bordering each ban zone fell by nine percent.*

> So the cars did not just move next door. The streets around the area actually got faster.

- One plain sentence, no label, no jargon, no arrows. Says what the card means.

### Tech (compressed, structured)

Card: the same.

> No displacement: bordering-street travel times fell nine percent, which turns their spillover link.

- Uses debate shorthand ("turns their link"), one sentence, ties to the opponent's argument.

### Solvency sentence (Aff)

> Solvency: our plan phases in over eighteen months with permits and edge transfers, as Fairhaven did, so the resolution removes the cars behind the injuries, and Fairhaven shows the injuries fall when it does.

- Starts with `Solvency:`, names what the resolution does, how that removes the cause, and what the card shows. Every number is in a card.

### Closing link (block)

> 5. So what their card describes is a city that closes streets and walks away, and our plan requires frequent service before it starts.

- Ties the answer back to the resolution's actual requirements.

---

## The same block, lay vs. tech

**Lay file** (a plain sentence after each card; fewer, stronger answers):

```
AT: Retail collapse
Neg Argument: Downtown stores lose sales when cars are banned.
1. Their own card says it was four streets with no bus changes, and sales came back.
2. [their card: four blocks, no bus changes, recovered within three percent]
   So the drop they read was four streets with no buses added, and by the end of summer it was nearly gone.
3. [twelve-city study: flat or up in eleven]
   That is far more cities, over four years, than one short pilot.
4. So their evidence describes a city that closed streets and walked away, which our plan does not do.
```

**Tech file** (more layers, compact analytics, explicit turn):

```
AT: Retail collapse
Neg Argument: Downtown stores lose sales when cars are banned.
1. Their Ashford card concedes four blocks, no transit change, and recovery to within 3 percent: no link at scale, and the drop is transitional.
2. [their card]
3. [twelve-city study: flat or up in eleven] Empirics outweigh a four-block pilot.
4. [study's failure case: no service change] Turn: the exception proves the plan requires frequent service.
5. Even if some stores lose short-term, the plan's phase-in and delivery windows mitigate; their impact is small and temporary.
```

Same evidence and the same honesty. The difference is length, labels, and how much the judge is walked through.
