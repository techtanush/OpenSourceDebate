# File Organization: Blocks, Frontlines, Backlines

Debate teams keep a small set of files, each with one job. Mixing them makes files long, duplicated, and hard to use in a round. This page defines the three kinds and how to keep them tidy. The vocabulary below is the one used by the team this repo was built with; the glossary (`glossary.md`) lists other common names, and `team.yaml` can rename them.

## The three kinds of file

| File | Job | Organized by | Used when |
|------|-----|--------------|-----------|
| **Blocks** | Attack **their** case: prepared answers to the opposing arguments | The argument you are answering ("AT: Retail collapse") | Your rebuttal |
| **Frontlines** | Defend **our** case against their rebuttal | Our contention, then our argument (with its card), then "AT: <their response>" | After they rebut our case |
| **Backlines** | Extend **our rebuttal** against their frontlines | Usually not pre-prepared; built in the round from what they said | Later rebuttals |

If a person says "frontlines" they mean defense of our own arguments. Never turn a frontline into an attack on their case (that is a block).

## Shape of each

### Blocks

```
Hat   : topic area ("Economy")
Block : "AT: <their argument>"
  Analytic : "<Opponent> Argument: <fair one-sentence statement>"
  1. overview answer (analytic)
  2. tag + cite + card (often answers THEIR specific card)
  3. tag + cite + card
  N. closing link or turn (analytic)
```

Details: `speeches/blocks/PROTOCOL.md`.

### Frontlines

```
Hat   : "<Contention>: our case argument"          (the contention)
  Tag + cite + card : our argument and the card we read       (so the file shows what was read)
  Block : "AT: <their rebuttal to this argument>"
    Analytic : "<Opponent> Argument: <their response stated fairly>"
    answers: tag + card (new evidence allowed) / short "Extend <Card> from our case: key point"
    closing line: why it still stands if dropped
```

Details: `speeches/frontlines/PROTOCOL.md`. Cards already read in the constructive appear as a short extension, not re-pasted.

### Backlines

Built live. If the user asks for prep, prepare **extensions of the best rebuttal answers** (the card plus the one-sentence reason it beats their expected frontline), not a full document. Details: `speeches/backlines/PROTOCOL.md`.

## Where files live

Suggested layout for a team repo or folder (rename freely):

```
Aff/
  Blocks/        Aff Blocks.docx              speech-ready answers to Neg arguments
  Frontlines/    Aff Frontlines - <case>.docx  defense of the Aff case (one file per case version, e.g. Lay, Tech)
  Library/       Aff MB Blocks.docx            the full evidence library of blocks (everything collected)
  Old Files/                                    superseded files (do not delete)
Neg/
  Blocks/ Frontlines/ Library/ Old Files/       same
```

- **Library vs. speech-ready:** the *library* holds every block and every card collected (the full evidence base); the *speech-ready* blocks file is the trimmed version used in rounds. New evidence goes into the library first, then into the speech-ready file under its **existing** heading.
- **One home per argument.** There is one block per opposing argument. If a block exists, **merge** new cards into it. Never create a second block for the same argument.
- **Keep the team's headings.** If the user or partner asked to keep existing headings unchanged, add evidence under those headings only; do not rename or reorder them.
- **The user cuts the final version.** Teams usually trim their own files. Don't heavily trim what you deliver; give strong, complete material with the best cards marked, and let them cut for time.
- **Don't delete.** Move superseded files to an `Old Files/` folder instead.
- **Name files by job**, not by date or round: "Aff Blocks", "Neg Frontlines - Lay Case." Put round-specific copies in a `Speech Docs/` folder.

## Before you create a file: check what exists

```bash
python tools/library.py index <team-folder> -o library-index.md
python tools/library.py search <team-folder> <argument keywords>
```

1. Is there already a block for this argument? Add to it.
2. Is the card already in the library? Reuse it.
3. Which cards were read in the constructive? (Those are extendable in frontlines.)
4. What heading names does the team use? Match them.

## Prefer specific-card answers over takeouts

For blocks, answer the opponent's **specific cards** where you can. Case-wide takeouts ("their entire case fails because...") read as a reach to lay judges. Keep a short, airtight takeout only when it is genuinely strong, and put it after the specific answers.

## `team.yaml` keys that control this

See `team.example.yaml`: `judge`, `blocks_dir`, `frontlines_dir`, `library_dir`, `keep_headings`. Agents read these directly; the Python tools only need `cutter_initials` and `cite_style`.
