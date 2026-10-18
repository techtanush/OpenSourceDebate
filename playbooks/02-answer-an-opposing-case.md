# Playbook 02: Answer an Opposing Case

**Goal:** a rebuttal and a set of blocks that answer the opponent's **specific** arguments and cards, using their own evidence wherever it helps, in files the debater can read from.

**Read first:** `core/refutation-guide.md`, `core/judge-adaptation.md`, `core/research-guide.md` (section 6), `speeches/rebuttal/PROTOCOL.md`, `speeches/blocks/PROTOCOL.md`.

## Inputs

- The opposing case: a `.docx`, a PDF, or pasted text.
- Our own case file (so we don't contradict ourselves and can link turns to it).
- Judge type, time limit, wpm (`team.yaml`, `formats/`).
- The existing library of blocks (`playbooks/06-use-my-files-as-context.md`).

## Steps

1. **Extract their text.**

```bash
python tools/inspect_docx.py their-case.docx --text > their-case.txt      # .docx
pdftotext -layout their-case.pdf their-case.txt                           # PDF
python tools/inspect_docx.py their-case.docx --cards                      # cite lines + highlighted text
python tools/tag_story.py their-case.docx                                 # their tags as a story
```

2. **Map their case.** For every argument write: name, claim, steps (UQ / link / IL / impact), each card (author, year, source type, what the card actually says in full), and which steps have no card.
3. **Run the hole checklist on every card** (`core/refutation-guide.md`, section 3): scope, date, qualifiers, method, source, number, direction, link to the resolution, their other cards, the author elsewhere. Read the paragraphs **before and after** their highlighting.
4. **Find cross-position contradictions** between their arguments. If you find one, it becomes your opening overview.
5. **Check our own case and library** for cards that already answer them (`tools/library.py search`). Reuse; do not re-cut.
6. **Choose answers per argument:** two to four, strongest first. Prefer, in this order: their own card, no link, non-unique, a turn, mitigation, and only then source or method attacks. Prefer answers to their **specific cards** over case-wide takeouts.
7. **Research the gaps** for each chosen answer (`research-guide.md`): a newer number, a stronger study, a counter-study, an independent source. Save full text.
8. **Cut cards** with context, and quote their own cards from their text exactly (verify against the text you extracted).
9. **Build each block** in the block anatomy: opposing-argument line, numbered overview, tagged cards, closing link or turn. For lay judges add a plain analytic after each card (`--lay`).
10. **Write the rebuttal:** overview (including any cross-case contradiction), line-by-line in their order, then weighing. Use blocks as the source; extend our case cards only as short analytics.
11. **Check flow:** read the answers in order; no contradictions between answers or with our case (`core/logic-flow.md`).
12. **Build, lint, and time:**

```bash
python tools/build_docx.py blocks.md -o blocks.docx
python tools/verify_quotes.py blocks.md --strict
python tools/lint_cites.py blocks.md
python tools/lint_cards.py blocks.md
python tools/lint_blocks.py blocks.md --lay        # drop --lay for a technical judge
python tools/speech_timer.py rebuttal.docx --wpm <rate> --limit <seconds>
```

13. **Cross-ex questions** from the same holes (`speeches/crossx/PROTOCOL.md`).
14. **Deliver** blocks, rebuttal, cross-ex list, and the caveats list.

## Done when

- [ ] Every opposing argument is answered or deliberately conceded; none is answered as a weaker version.
- [ ] Their own cards are used wherever they help, quoted exactly.
- [ ] Each answer has a card; no "Extend X" for unread cards.
- [ ] Answers are ranked and consistent with each other and with our case.
- [ ] The rebuttal ends with weighing (if the format uses it) and fits the time.
- [ ] Quotes verified; unverified items flagged.

## Common mistakes

- Answering the topic instead of the card (`examples/good-vs-bad/rebuttals.md`).
- A takeout where a specific answer existed.
- Quoting a card from memory or a snippet.
- Answers that contradict each other.
- Never reading the text around their highlighting.
