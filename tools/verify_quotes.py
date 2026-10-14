#!/usr/bin/env python3
"""Check that every card body is a verbatim excerpt of its saved source text.

Usage:
    python tools/verify_quotes.py spec.md --source article.txt
    python tools/verify_quotes.py spec.json            # uses each card's cite.source path

Rules (see core/integrity.md):
  * The full card body (read + underlined + unread text) must appear in the source,
    in order. Whitespace and curly quotes/dashes are normalized; words are not.
  * Omissions may be marked with "..." and edits with [brackets]; each piece between
    them must appear in the source, in order.
  * A card with no source file is reported UNVERIFIED (exit code 2 with --strict).

Exit code: 0 all verified, 1 a mismatch was found, 2 unverified cards under --strict.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_docx import load_spec, body_runs  # noqa: E402

_SPLIT = re.compile(r"\[[^\]]*\]|\.\.\.|…")


def normalize(text):
    text = (text.replace("‘", "'").replace("’", "'")
            .replace("“", '"').replace("”", '"')
            .replace("–", "-").replace("—", "-")
            .replace(" ", " "))
    return re.sub(r"\s+", " ", text).strip()


def find_in_order(pieces, source):
    pos = 0
    for piece in pieces:
        piece = piece.strip()
        if not piece:
            continue
        idx = source.find(piece, pos)
        if idx < 0:
            return piece
        pos = idx + len(piece)
    return None


def verify_card(card, source_text):
    """Return None if verified, else the first piece of text not found."""
    body = normalize("".join(t for t, _ in body_runs_any(card)))
    src = normalize(source_text)
    if body in src:
        return None
    return find_in_order(_SPLIT.split(body), src)


def body_runs_any(card):
    if "body_paragraphs" in card:
        return [r for para in card["body_paragraphs"] for r in para + [(" ", "unread")]]
    return body_runs(card)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("spec")
    ap.add_argument("--source", help="source text file used for every card")
    ap.add_argument("--strict", action="store_true",
                    help="exit 2 if any card has no source to check against")
    args = ap.parse_args(argv)

    spec = load_spec(args.spec)
    base = os.path.dirname(os.path.abspath(args.spec))
    bad = unverified = ok = 0
    for item in spec["items"]:
        if item.get("type") != "card":
            continue
        src_path = args.source or item.get("cite", {}).get("source")
        label = item["tag"][:70]
        if not src_path:
            print("UNVERIFIED  %s  (no source file)" % label)
            unverified += 1
            continue
        if not os.path.isabs(src_path) and not os.path.exists(src_path):
            src_path = os.path.join(base, src_path)
        with open(src_path, "r", encoding="utf-8") as f:
            miss = verify_card(item, f.read())
        if miss is None:
            print("OK          %s" % label)
            ok += 1
        else:
            print("MISMATCH    %s\n            not found in source: %r" % (label, miss[:120]))
            bad += 1
    print("\n%d verified, %d mismatched, %d unverified" % (ok, bad, unverified))
    if bad:
        return 1
    if unverified and args.strict:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
