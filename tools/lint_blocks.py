#!/usr/bin/env python3
"""Check that each Block (A2 / frontline) is a complete, self-contained block.

Usage:
    python tools/lint_blocks.py spec.md
    python tools/lint_blocks.py file.docx

A block is read from during the round, so it must contain the actual cards. Checks per
Block (Heading 3):

  ERROR   no cut cards at all (analytics that only mention a card elsewhere don't count)
  ERROR   a Tag with no cite/body after it (an answer with no card)
  ERROR   no opening statement of the opposing argument ("Aff Argument: ...", "Neg
          Argument: ...", "Argument: ...") before the answers
  WARN    fewer than two answers (numbered analytics plus tagged cards)
  WARN    no closing analytic after the last card (a link back to the resolution, a turn,
          or the weighing)

See speeches/blocks/PROTOCOL.md for the block anatomy. Exit code 1 on any ERROR.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ARG_STATEMENT = re.compile(r"^\s*(?:\S+\s+){0,2}arguments?\s*:", re.I)


def events_from_spec(path):
    from build_docx import load_spec
    out = []
    for item in load_spec(path)["items"]:
        t = item.get("type")
        if t == "block":
            out.append(("block", item["text"]))
        elif t == "card":
            out.append(("card", item["tag"]))
        elif t == "tag":
            out.append(("tag", item["text"]))
        elif t == "analytic":
            out.append(("analytic", item["text"]))
    return out


def events_from_docx(path):
    import inspect_docx as I
    paras = I.read_paragraphs(path)
    out = []
    i = 0
    while i < len(paras):
        p = paras[i]
        text = I.para_text(p)
        if p["style"] == "Heading3":
            out.append(("block", text))
        elif p["style"] == "Analytic":
            out.append(("analytic", text))
        elif p["style"] == "Heading4":
            j = i + 1
            while j < len(paras) and not paras[j]["runs"]:
                j += 1
            has_card = j < len(paras) and paras[j]["style"] == "Normal"
            out.append(("card" if has_card else "tag", text))
        i += 1
    return out


def lint(events):
    """Return list of (level, block_title, message)."""
    results = []
    blocks = []
    cur = None
    for kind, text in events:
        if kind == "block":
            cur = {"title": text, "items": []}
            blocks.append(cur)
        elif cur is not None:
            cur["items"].append((kind, text))
    for b in blocks:
        items = b["items"]
        title = b["title"]
        cards = [t for k, t in items if k == "card"]
        bare = [t for k, t in items if k == "tag"]
        if not cards:
            results.append(("ERROR", title, "no cut cards in this block"))
        for t in bare:
            results.append(("ERROR", title, "tag with no card: %r" % t[:70]))
        first_idx = next((n for n, (k, _) in enumerate(items) if k in ("card", "tag")), len(items))
        opening = [t for k, t in items[:first_idx] if k == "analytic"]
        if not any(ARG_STATEMENT.match(t) for t in opening):
            results.append(("ERROR", title,
                            "no opening statement of the opposing argument "
                            "(e.g. 'Aff Argument: ...') before the answers"))
        answers = [1 for k, t in items if k in ("card", "tag")] + \
                  [1 for k, t in items if k == "analytic" and re.match(r"^\s*\d+\.", t)]
        if len(answers) < 2:
            results.append(("WARN", title, "fewer than two answers"))
        last_card = max((n for n, (k, _) in enumerate(items) if k == "card"), default=-1)
        if last_card >= 0 and not any(k == "analytic" for k, _ in items[last_card + 1:]):
            results.append(("WARN", title,
                            "no closing analytic after the last card "
                            "(link to the resolution, a turn, or weighing)"))
    return results, len(blocks)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("file", help="spec (.md/.json) or .docx")
    args = ap.parse_args(argv)
    events = events_from_docx(args.file) if args.file.lower().endswith(".docx") \
        else events_from_spec(args.file)
    results, n = lint(events)
    for level, title, msg in results:
        print("%-5s %s\n      %s" % (level, title[:80], msg))
    errors = sum(1 for r in results if r[0] == "ERROR")
    print("%d block(s) checked: %d error(s), %d warning(s)" % (n, errors, len(results) - errors))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
