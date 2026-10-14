#!/usr/bin/env python3
"""Estimate how long a speech takes to read.

Usage:
    python tools/speech_timer.py speech.txt --wpm 250
    python tools/speech_timer.py cards.docx --wpm 250   # counts only highlighted (read) text
    python tools/speech_timer.py speech.md --wpm 200 --limit 90   # limit in seconds

For .docx files only highlighted runs and non-card paragraphs (analytics, plain
text) count, because unread text is not spoken. Exit code 1 if over --limit.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def words(text):
    return len(re.findall(r"\S+", text))


def count_docx(path):
    from inspect_docx import read_paragraphs, para_text, is_read
    total = 0
    for p in read_paragraphs(path):
        if p["style"].startswith("Heading"):
            total += words(para_text(p))            # tags/headings are read
        elif any(r["highlight"] for r in p["runs"]):
            total += sum(words(r["text"]) for r in p["runs"] if is_read(r))
        elif p["style"] in ("Analytic", "Normal") and not any(
                r["sz"] == "16" for r in p["runs"]):
            total += words(para_text(p))             # analytics, plain speech text
    return total


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("file")
    ap.add_argument("--wpm", type=int, default=250)
    ap.add_argument("--limit", type=int, help="time limit in seconds")
    args = ap.parse_args(argv)
    if args.file.lower().endswith(".docx"):
        n = count_docx(args.file)
    else:
        with open(args.file, "r", encoding="utf-8") as f:
            n = words(f.read())
    secs = round(n / args.wpm * 60)
    print("%d words at %d wpm = %d:%02d" % (n, args.wpm, secs // 60, secs % 60))
    if args.limit and secs > args.limit:
        print("OVER limit by %d seconds" % (secs - args.limit))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
