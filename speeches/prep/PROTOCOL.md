# Prep Protocol

Used for: getting ready for a new topic or tournament: understanding the resolution, brainstorming arguments, and building the files you'll need.

Read first: `core/research-protocol.md`, `core/source-evaluation.md`.

## 1. Understand the topic

1. Write the resolution and define every key term. Use authoritative definitions and note where meaning is contested.
2. Identify **who** is affected, **what** changes, **how** it would work, and **what already exists** (status quo).
3. Collect 5-10 foundational sources (agency reports, major studies, recent news). Save full text to `sources/`.
4. Write a one-page **topic primer**: facts, key numbers, major actors, and the main disagreements.

## 2. Brainstorm arguments

For each side, list arguments in four buckets:

| Bucket | Question |
|--------|----------|
| Benefits / harms | What good or bad things follow? |
| Mechanisms | How does it work in practice? What can fail? |
| Counterfactuals | What happens without the resolution? |
| Values / framing | Which values should the judge weigh? |

Rank by: strength of evidence, likelihood, size, and how hard it is to answer.

## 3. Build files, in this order

1. **Case(s)** for each side (`speeches/case/`).
2. **Frontlines** for your own case's top responses (`speeches/frontlines/`).
3. **Blocks** for the most common opposing arguments (`speeches/blocks/`).
4. **Cross-ex banks** for those arguments (`speeches/crossx/`).
5. **Extensions and weighing** pieces (`speeches/summary-final/`).

Start with the arguments you will read most often. Breadth of mediocre files is worse than depth on the main ones.

## 4. Track evidence

Keep a simple index (spreadsheet or Markdown table): short cite, claim it supports, status (VERIFIED/UNVERIFIED), file, and date accessed. Re-check dates before tournaments, because facts change.

## 5. Practice

- Time each speech with `tools/speech_timer.py`.
- Run a practice round against a friend or the agent playing the other side.
- After each round, record what was dropped, what was surprising, and what you lacked, then add it to the file list.

## Pre-tournament checklist

- [ ] Cases and top blocks built, verified, and timed.
- [ ] Newest evidence added (check dates).
- [ ] Unverified cards resolved or flagged.
- [ ] Cites complete (`lint_cites.py`).
- [ ] Files saved in the format your platform needs (.docx for Verbatim).
- [ ] Backups of all files.
