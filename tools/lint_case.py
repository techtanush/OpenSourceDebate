#!/usr/bin/env python3
"""Check that each contention (or DA) in a case is a real link chain of cards.

Usage:
    python tools/lint_case.py case.md            # Aff case (solvency required)
    python tools/lint_case.py case.docx --neg    # Neg case / DAs (solvency not required)

A "contention" is a Hat (Heading 2) or Block (Heading 3) whose title starts with
"Contention", "C1"/"C2"..., "Advantage", "Adv", "DA", or "Disad". Checks per contention:

  ERROR   fewer than MIN_CARDS cards
  ERROR   no chain map: an Analytic starting with "Chain:" before the first card, naming
          each step, e.g.  Chain: UQ (Reyes 25) -> LINK (Whitfield 24) -> IMPACT (WHO 24)
  ERROR   chain map is missing UQ, LINK, or IMPACT (and SOLVENCY for an Aff case)
  ERROR   fewer cards than steps named in the chain map (a step with no card)
  WARN    a long analytic (over MAX_ANALYTIC_WORDS words): evidence should carry that work

Step names: UQ, TREND, LINK, IL, IMPACT, SOLVENCY. See core/argument-structure.md.
Exit code 1 on any ERROR.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MIN_CARDS = 4
MAX_ANALYTIC_WORDS = 90
STEP_RE = re.compile(r"\b(UQ|TREND|LINK|IL|IMPACT|SOLVENCY)\b")
CONTENTION_RE = re.compile(r"^\s*(contention|c\d+\b|advantage|adv\b|da\b|disad)", re.I)


def events_from_spec(path):
    from build_docx import load_spec
    level = {"pocket": 1, "hat": 2, "block": 3}
    out = []
    for item in load_spec(path)["items"]:
        t = item.get("type")
        if t in level:
            out.append(("heading", level[t], item["text"]))
        elif t == "card":
            out.append(("card", 0, item["tag"]))
        elif t == "analytic":
            out.append(("analytic", 0, item["text"]))
    return out


def events_from_docx(path):
    import inspect_docx as I
    paras = I.read_paragraphs(path)
    out = []
    for i, p in enumerate(paras):
        text = I.para_text(p)
        if p["style"] in ("Heading1", "Heading2", "Heading3"):
            out.append(("heading", int(p["style"][-1]), text))
        elif p["style"] == "Analytic":
            out.append(("analytic", 0, text))
        elif p["style"] == "Heading4":
            j = i + 1
            while j < len(paras) and not paras[j]["runs"]:
                j += 1
            if j < len(paras) and paras[j]["style"] == "Normal":
                out.append(("card", 0, text))
    return out


def sections(events):
    """Split events into contention sections: dicts with title, level, items."""
    secs = []
    cur = None
    for kind, level, text in events:
        if kind == "heading":
            if cur is not None and level <= cur["level"]:
                cur = None
            if CONTENTION_RE.match(text):
                cur = {"title": text, "level": level, "items": []}
                secs.append(cur)
        elif cur is not None:
            cur["items"].append((kind, text))
    return secs


def lint(events, aff=True):
    results = []
    secs = sections(events)
    for s in secs:
        title, items = s["title"], s["items"]
        cards = [t for k, t in items if k == "card"]
        if len(cards) < MIN_CARDS:
            results.append(("ERROR", title,
                            "only %d card(s); a contention needs a chain of at least %d" %
                            (len(cards), MIN_CARDS)))
        first_card = next((n for n, (k, _) in enumerate(items) if k == "card"), len(items))
        chain = next((t for k, t in items[:first_card]
                      if k == "analytic" and re.match(r"^\s*chain\s*:", t, re.I)), None)
        if chain is None:
            results.append(("ERROR", title,
                            "no chain map before the first card "
                            "(e.g. 'Chain: UQ (Card) -> LINK (Card) -> IMPACT (Card)')"))
        else:
            steps = STEP_RE.findall(chain)
            required = ["UQ", "LINK", "IMPACT"] + (["SOLVENCY"] if aff else [])
            for r in required:
                if r not in steps:
                    results.append(("ERROR", title, "chain map has no %s step" % r))
            if len(cards) < len(steps):
                results.append(("ERROR", title,
                                "chain map names %d steps but there are only %d cards: "
                                "a step has no card" % (len(steps), len(cards))))
        for k, t in items:
            if k == "analytic" and not re.match(r"^\s*chain\s*:", t, re.I):
                n = len(t.split())
                if n > MAX_ANALYTIC_WORDS:
                    results.append(("WARN", title,
                                    "long analytic (%d words): evidence should carry this: %r" %
                                    (n, t[:60])))
    return results, len(secs)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("file", help="spec (.md/.json) or .docx")
    ap.add_argument("--neg", action="store_true",
                    help="Neg case / DAs: do not require a SOLVENCY step")
    args = ap.parse_args(argv)
    events = events_from_docx(args.file) if args.file.lower().endswith(".docx") \
        else events_from_spec(args.file)
    results, n = lint(events, aff=not args.neg)
    if n == 0:
        print("no contentions found (headings starting with Contention / C1 / Advantage / DA)")
        return 1
    for level, title, msg in results:
        print("%-5s %s\n      %s" % (level, title[:80], msg))
    errors = sum(1 for r in results if r[0] == "ERROR")
    print("%d contention(s) checked: %d error(s), %d warning(s)" %
          (n, errors, len(results) - errors))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
