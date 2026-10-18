# Playbook 01: Build a Case from Scratch

**Goal:** a constructive where every contention is a chain of cards with solvency, short analytics, and a clear story, in a Verbatim `.docx`.

**Read first:** `core/argument-structure.md`, `core/logic-flow.md`, `core/research-guide.md`, `speeches/case/PROTOCOL.md`.

## Inputs

- The resolution (exact wording) and side.
- Format and time (`formats/`), wpm, judge type (`team.yaml`).
- Existing files (check first; `playbooks/06-use-my-files-as-context.md`).

## Steps

1. **Understand the topic.** Define key terms, who is affected, what changes, and what already exists. Write a half-page primer (`speeches/prep/PROTOCOL.md`).
2. **Choose two or three contentions.** For each, write the one-sentence claim. Prefer contentions with a clear harm, a clear mechanism, and evidence you can find. Pick the strongest first.
3. **Draft the chain map for each contention.**
   `Chain: UQ (?) -> TREND (?) -> LINK (?) -> IL (?) -> IMPACT (?) -> SOLVENCY (?)`
   Put a question mark where you have no card yet. Add one card per step; for the Aff, add solvency for each impact.
4. **Turn the question marks into research questions** (`research-guide.md`, section 2) and run searches slot by slot: problem now, trend, mechanism, consequences, scale, solvency. Save full text; log queries and rejects.
5. **Pick the best card for each slot** and a runner-up. Note each card's weakness.
6. **Cut each card** with context and sparse read text (`core/cutting-rules.md`). Use constructive-length cards (one or more paragraphs).
7. **Write the tags** as full sentences with the specifics, labeled by step (`UQ:`, `LINK:`, ...) so the chain is visible.
8. **Write the few analytics:** the chain map, an optional one-sentence impact framing, and the `Solvency:` sentence for each Aff contention. Nothing else unless a card is missing, in which case find the card.
9. **Order the contentions and write the intro, plan (if any), and conclusion.**
10. **Test the flow:** `python tools/tag_story.py case.md`. Read only that output as a judge, saying "which means..." between tags. Fix gaps, numbers that don't fit, and contradictions (`core/logic-flow.md`).
11. **Build and check:**

```bash
python tools/build_docx.py case.md -o case.docx
python tools/build_docx.py case.md -o case-DRAFT.docx --draft      # optional cutting copy
python tools/verify_quotes.py case.md --strict
python tools/lint_cites.py case.md
python tools/lint_cards.py case.md --profile case
python tools/lint_case.py case.md                                   # add --neg for a Neg case
python tools/speech_timer.py case.docx --wpm <rate> --limit <seconds>
```

12. **Deliver** `case.md`, `case.docx`, and the "Before you read these" list (UNVERIFIED items, weak sources, gaps).

## Done when

- [ ] Every contention has a chain map and a card for every step, at least four cards, and (Aff) a `Solvency:` analytic.
- [ ] The link, the impact, and solvency are cards, not prose; the impact has a number and a timeframe.
- [ ] Analytics are a small share of what is spoken.
- [ ] `tag_story.py` reads as one story; numbers and scope fit; no contradictions.
- [ ] All linters pass and the case fits the time limit.
- [ ] Caveats are reported honestly.

## Common mistakes

- Starting with the topic instead of the chain slots.
- One card per contention plus long analytics (see `examples/good-vs-bad/link-chains.md`).
- A solvency card about the problem instead of the resolution.
- Contentions that contradict each other.
- Skipping the flow test.

**Reference:** `examples/example-case.md` (fictional contention), `docs/real-1ac-chain-walkthrough.md` (real 1AC mapped to the chain; private reference).
