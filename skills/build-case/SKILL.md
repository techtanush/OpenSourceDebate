---
name: build-case
description: "Build a constructive case (Aff or Neg) with contentions, evidence, and analytics, sized to the speech time. Use when the user wants a case, constructive, or disadvantage shell."
---

# build-case

First read `AGENTS.md` and `core/integrity.md` from the repo root. Never fabricate or paraphrase inside a quote, and never treat a snippet as the source text.

## Read these files

- `speeches/case/PROTOCOL.md`
- `core/argument-structure.md`
- `core/integrity.md`
- `core/cutting-rules.md`

## Steps

1. Collect resolution, side, format (`formats/`), wpm, and audience.
2. Follow `speeches/case/PROTOCOL.md`: write the chain map for each contention first, list the card needed for every step (UQ, TREND, LINK, IL, IMPACT, SOLVENCY), research the gaps, then cut. One card plus prose is a failed contention. Cards first: analytics only connect cards. On the Aff, every impact needs a SOLVENCY card and a `Solvency:` analytic showing the resolution itself causes it to fall.
3. Build with `tools/build_docx.py`, check with `python tools/lint_case.py case.md` (use `--neg` for DAs), and time with `tools/speech_timer.py`.
4. Deliver the file plus a one-page summary and the caveats list.

## Card quality

Cards need context around the read text and sparse highlighting (see `core/cutting-rules.md`); run `python tools/lint_cards.py` and `python tools/lint_blocks.py`, and fix every flag. Blocks and frontlines hold the actual cut cards, never analytics that merely mention a card in another file. Read `docs/what-good-looks-like.md`.

## Delivering files

Tell the user the formatting and highlighting only appear when the .docx is opened in an editor that supports Verbatim-style formatting (such as CardMirror or Verbatim in Word).

## Finish with

A short "Before you read these" list: UNVERIFIED quotes, biased or weak sources, missing credentials or dates, and highlighting an opponent could attack.
