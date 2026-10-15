#!/usr/bin/env python3
"""Print the tags of a case or block file as a story, to test the logic flow.

Usage:
    python tools/tag_story.py case.md
    python tools/tag_story.py file.docx

For each section (Hat or Block) it prints the chain map (if any) and then every tag in
order with its cite, the step it fills (from the chain map), and the numbers it carries.
Read the output top to bottom as if you were the judge hearing only the tags:

  * Does each tag follow from the one before? Is any step missing or out of order?
  * Do the numbers build on each other (the scale in the impact should fit the size of
    the problem in the uniqueness card)?
  * Does anything repeat, contradict, or jump?

This tool does not judge; it makes the flow visible. See core/logic-flow.md. The checks
that can be automated (step order, chain map vs. cards, numbers in analytics) are in
tools/lint_case.py.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lint_case import STEP_RE, CONTENTION_RE, _numbers  # noqa: E402

SECTION_RE = re.compile(r"^\s*(a2|at)\b", re.I)


def load_events(path):
    import lint_case
    if path.lower().endswith(".docx"):
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
                    name = paras[j]["runs"][0]["text"].strip().rstrip(",") if paras[j]["runs"] else ""
                    out.append(("card", 0, text, 0, name, ""))
                else:
                    out.append(("tag", 0, text))
        return out
    return lint_case.events_from_spec(path)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("file")
    args = ap.parse_args(argv)
    section = None
    steps = []
    n = 0
    for ev in load_events(args.file):
        kind, level, text = ev[0], ev[1], ev[2]
        if kind == "heading":
            if level >= 2 and (CONTENTION_RE.match(text) or SECTION_RE.match(text) or level == 2
                               or section is None):
                print("\n%s %s" % ("#" * level, text))
                section, steps, n = text, [], 0
            elif level >= 2:
                print("   -- %s" % text)
        elif kind == "analytic" and re.match(r"^\s*chain\s*:", text, re.I):
            steps = STEP_RE.findall(text)
            print("   Chain map: %s" % text.split(":", 1)[1].strip())
        elif kind in ("card", "tag"):
            n += 1
            label = steps[n - 1] if n - 1 < len(steps) else ""
            name = ev[4] if len(ev) > 4 and ev[4] else ("(no card)" if kind == "tag" else "")
            nums = sorted(_numbers(text))
            print("   %2d. %-8s %s" % (n, label, text))
            print("       card: %s%s" % (name or "?", ("   numbers: " + ", ".join(nums)) if nums else ""))
        elif kind == "analytic" and section:
            print("       > %s" % text[:140])
    return 0


if __name__ == "__main__":
    sys.exit(main())
