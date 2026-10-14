#!/usr/bin/env python3
"""Flag incomplete cites in a card spec.

Usage:
    python tools/lint_cites.py spec.md [--strict-case]

Required for every card: name (Author YY), author, quals, date, title,
publication or url, doa, initials. Missing pieces are listed per card.
Exit code 1 if any card has a problem.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_docx import load_spec  # noqa: E402

REQUIRED = ["name", "author", "quals", "date", "title", "url", "doa", "initials"]
NAME_RE = re.compile(r"^[A-Z][\w'’.\- &]*? ?(et al\.? )?['’]?\d{2}([-/]\d{1,2})?$")


def lint(cite, team_defaults=None):
    problems = []
    merged = dict(team_defaults or {})
    merged.update(cite)
    if merged.get("raw"):
        return problems  # raw cites are the author's responsibility
    for key in REQUIRED:
        if not merged.get(key):
            problems.append("missing " + key)
    name = merged.get("name", "")
    if name and not NAME_RE.match(name):
        problems.append("name should look like 'Lastname 26' (got %r)" % name)
    url = merged.get("url", "")
    if url and not url.startswith(("http://", "https://")):
        problems.append("url should start with http(s)://")
    return problems


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("spec")
    ap.add_argument("--team", default="team.yaml")
    args = ap.parse_args(argv)
    spec = load_spec(args.spec, args.team)
    defaults = spec.get("defaults", {}).get("cite", {})
    bad = 0
    for item in spec["items"]:
        if item.get("type") != "card":
            continue
        problems = lint(item.get("cite", {}), defaults)
        if problems:
            bad += 1
            print("%s\n   - %s" % (item["tag"][:70], "\n   - ".join(problems)))
    print("%d card(s) need attention" % bad if bad else "all cites complete")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
