#!/usr/bin/env python3
"""Check that cards are cut like real debate cards: enough context, sparse highlighting.

Usage:
    python tools/lint_cards.py spec.md                  # block/frontline cards (default profile)
    python tools/lint_cards.py file.docx --profile case # constructive/case cards (longer)

Why: a card that is only the highlighted sentence has no context, so an opponent
(or the judge) can't see what the author said around it. Thresholds were calibrated on
real team files (143 block/frontline cards, 53 case cards):

  profile  typical body (median)  read share (median)  unread context before/after (median)
  block    ~170 words             ~18%                 ~10 / ~17 words
  case     ~500 words             ~8%                  ~24 / ~97 words

Real block cards are often only a few sentences, so the block profile flags only the
extremes (a lone sentence, or a card with no unread context on either side at all). The
case profile is stricter because constructive cards are long. These are warnings, not a
quality score; a card can pass and still be a poor card. See core/cutting-rules.md.

Checks per card:
  * body at least the profile's minimum words
  * read words at most the profile's maximum share of the body
  * at least the profile's minimum unread words before the first read run and after the last
  * the body contains some read text

Exit code 1 if any card has a problem.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

PROFILES = {
    #         min body words, max read share, min unread words before/after
    # block cards in real files are often short (a few sentences), so this profile only
    # catches the extremes: a lone sentence, or a card that is entirely highlighted.
    "block": {"min_body": 30, "max_ratio": 0.85, "min_context": 3},
    "case": {"min_body": 150, "max_ratio": 0.30, "min_context": 15},
}


def _words(text):
    return len(text.split())


def measure(runs):
    """runs: list of (text, mode) with mode read | underline | unread."""
    total = sum(_words(t) for t, _ in runs)
    read_idx = [i for i, (_, m) in enumerate(runs) if m == "read"]
    read = sum(_words(runs[i][0]) for i in read_idx)
    if not read_idx:
        return {"total": total, "read": 0, "ratio": 0.0, "before": total, "after": total}
    before = sum(_words(t) for t, _ in runs[:read_idx[0]])
    after = sum(_words(t) for t, _ in runs[read_idx[-1] + 1:])
    return {"total": total, "read": read, "ratio": read / total if total else 0.0,
            "before": before, "after": after}


def problems_for(m, profile="block"):
    prof = PROFILES[profile]
    MIN_BODY, MAX_READ_RATIO, MIN_CONTEXT = prof["min_body"], prof["max_ratio"], prof["min_context"]
    out = []
    if m["read"] == 0:
        out.append("no read (highlighted) text")
    if m["total"] < MIN_BODY:
        out.append("body is only %d words (want %d+): include the surrounding paragraph(s)" %
                   (m["total"], MIN_BODY))
    if m["ratio"] > MAX_READ_RATIO:
        out.append("%d%% of the body is read (want %d%% or less): add context, trim highlighting" %
                   (round(m["ratio"] * 100), round(MAX_READ_RATIO * 100)))
    if profile == "block":
        if m["read"] and m["before"] < MIN_CONTEXT and m["after"] < MIN_CONTEXT:
            out.append("no unread context before or after the read text: include the sentences around it")
    else:
        if m["read"] and m["before"] < MIN_CONTEXT:
            out.append("only %d unread words before the read text (want %d+)" %
                       (m["before"], MIN_CONTEXT))
        if m["read"] and m["after"] < MIN_CONTEXT:
            out.append("only %d unread words after the read text (want %d+)" %
                       (m["after"], MIN_CONTEXT))
    return out


def cards_from_spec(path):
    from build_docx import load_spec
    from verify_quotes import body_runs_any
    spec = load_spec(path)
    for item in spec["items"]:
        if item.get("type") == "card":
            yield item["tag"], [(t, m) for t, m in body_runs_any(item)]


def cards_from_docx(path):
    import inspect_docx as I
    paras = I.read_paragraphs(path)
    for tag, _cite, body in I.card_groups(paras):
        runs = []
        for b in body:
            for r in b["runs"]:
                mode = "read" if r["highlight"] else ("underline" if I.is_underlined(r) else "unread")
                runs.append((r["text"], mode))
        yield tag, runs


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("file", help="spec (.md/.json) or .docx")
    ap.add_argument("--profile", choices=sorted(PROFILES), default="block",
                    help="block (default): blocks/frontlines; case: constructive cards")
    args = ap.parse_args(argv)
    gen = cards_from_docx if args.file.lower().endswith(".docx") else cards_from_spec
    bad = n = 0
    for tag, runs in gen(args.file):
        n += 1
        m = measure(runs)
        probs = problems_for(m, args.profile)
        if probs:
            bad += 1
            print("%s\n   body %d words, read %d (%d%%), context before/after %d/%d" % (
                tag[:80], m["total"], m["read"], round(m["ratio"] * 100), m["before"], m["after"]))
            for p in probs:
                print("   - " + p)
    print("%d of %d card(s) need more context or less highlighting" % (bad, n) if bad
          else "all %d card(s) look properly cut" % n)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
