#!/usr/bin/env python3
"""Check that each contention (or DA) in a case is a real link chain of cards.

Usage:
    python tools/lint_case.py case.md            # Pro case (solvency required)
    python tools/lint_case.py case.docx --con    # Con case / turns (solvency not required)

A "contention" is a Hat (Heading 2) or Block (Heading 3) whose title starts with
"Contention", "C1"/"C2"..., "Advantage", "Adv", "DA", or "Disad". Checks per contention:

  ERROR   fewer than MIN_CARDS cards
  ERROR   no chain map: an Analytic starting with "Chain:" before the first card, naming
          each step, e.g.  Chain: UQ (Reyes 25) -> LINK (Whitfield 24) -> IMPACT (WHO 24)
  ERROR   chain map is missing UQ, LINK, or IMPACT (and SOLVENCY for a Pro case)
  ERROR   fewer cards than steps named in the chain map (a step with no card)
  ERROR   (Pro) no "Solvency:" analytic: a short statement of how the resolution itself
          causes the impact to be reduced, tied to the SOLVENCY card
  ERROR   analytics outweigh evidence: analytic words are more than MAX_ANALYTIC_SHARE of
          (analytic words + words actually read from cards)
  WARN    analytics are a large share of the contention (over WARN_ANALYTIC_SHARE)
  WARN    a long analytic (over MAX_ANALYTIC_WORDS words): evidence should carry that work

Logic-flow checks (see core/logic-flow.md):
  ERROR   chain steps out of logical order (UQ, TREND, LINK, IL, IMPACT must not go backwards)
  WARN    the card named in the chain map for a step is not the card at that position
  WARN    a card tag starts with a step label (e.g. "LINK:") that disagrees with the chain map
  WARN    a number (2+ digits, %, or $) appears in an analytic but in no card tag or body of
          that contention: analytics must not introduce numbers the cards don't support

Step names: UQ, TREND, LINK, IL, IMPACT, SOLVENCY. See core/argument-structure.md.
Exit code 1 on any ERROR.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MIN_CARDS = 4
MAX_ANALYTIC_WORDS = 60
WARN_ANALYTIC_SHARE = 0.30
MAX_ANALYTIC_SHARE = 0.50
STEP_RE = re.compile(r"\b(UQ|TREND|LINK|IL|IMPACT|SOLVENCY)\b")
STEP_NAME_RE = re.compile(r"\b(UQ|TREND|LINK|IL|IMPACT|SOLVENCY)\s*\(([^)]*)\)")
TAG_LABEL_RE = re.compile(r"^\s*(UQ|TREND|LINK|IL|IMPACT|SOLVENCY)\s*:", re.I)
NUMBER_RE = re.compile(r"\$?\d[\d,]*(?:\.\d+)?%?")
ORDER = ["UQ", "TREND", "LINK", "IL", "IMPACT"]


def _numbers(text):
    out = set()
    for tok in NUMBER_RE.findall(text):
        clean = tok.replace(",", "").lstrip("$").rstrip("%").rstrip(".")
        if not clean:
            continue
        if len(clean.replace(".", "")) >= 2 or "%" in tok or tok.startswith("$"):
            out.add(clean)
    return out
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
            from verify_quotes import body_runs_any
            read = sum(len(txt.split()) for txt, m in body_runs_any(item) if m == "read")
            body_text = " ".join(txt for txt, _ in body_runs_any(item))
            out.append(("card", 0, item["tag"], read, item.get("cite", {}).get("name", ""), body_text))
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
                read, k, body_text = 0, j + 1, []
                while k < len(paras) and paras[k]["style"] == "Normal":
                    read += sum(len(r["text"].split()) for r in paras[k]["runs"] if r["highlight"])
                    body_text.append(I.para_text(paras[k]))
                    k += 1
                cite_runs = paras[j]["runs"]
                name = cite_runs[0]["text"].strip().rstrip(",") if cite_runs else ""
                out.append(("card", 0, text, read, name, " ".join(body_text)))
    return out


def sections(events):
    """Split events into contention sections: dicts with title, level, items."""
    secs = []
    cur = None
    for ev in events:
        kind, level, text = ev[0], ev[1], ev[2]
        if kind == "heading":
            if cur is not None and level <= cur["level"]:
                cur = None
            if CONTENTION_RE.match(text):
                cur = {"title": text, "level": level, "items": []}
                secs.append(cur)
        elif cur is not None:
            cur["items"].append((kind, text, ev[3] if len(ev) > 3 else 0,
                                 ev[4] if len(ev) > 4 else "", ev[5] if len(ev) > 5 else ""))
    return secs


def lint(events, aff=True):
    results = []
    secs = sections(events)
    for s in secs:
        title, items = s["title"], s["items"]
        cards = [it[1] for it in items if it[0] == "card"]
        if len(cards) < MIN_CARDS:
            results.append(("ERROR", title,
                            "only %d card(s); a contention needs a chain of at least %d" %
                            (len(cards), MIN_CARDS)))
        first_card = next((n for n, it in enumerate(items) if it[0] == "card"), len(items))
        chain = next((it[1] for it in items[:first_card]
                      if it[0] == "analytic" and re.match(r"^\s*chain\s*:", it[1], re.I)), None)
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
        analytics = [it[1] for it in items
                     if it[0] == "analytic" and not re.match(r"^\s*chain\s*:", it[1], re.I)]
        if aff and not any(re.match(r"^\s*solvency\s*:", t, re.I) for t in analytics):
            results.append(("ERROR", title,
                            "no 'Solvency:' analytic: state in a sentence or two how the "
                            "resolution itself causes this impact to be reduced"))
        for t in analytics:
            n = len(t.split())
            if n > MAX_ANALYTIC_WORDS:
                results.append(("WARN", title,
                                "long analytic (%d words): evidence should carry this: %r" %
                                (n, t[:60])))
        a_words = sum(len(t.split()) for t in analytics)
        read_words = sum(it[2] for it in items if it[0] == "card")
        total = a_words + read_words
        if total:
            share = a_words / total
            if share > MAX_ANALYTIC_SHARE:
                results.append(("ERROR", title,
                                "analytics are %d%% of what is spoken (%d analytic words vs %d "
                                "read from cards): replace analytics with cards" %
                                (round(share * 100), a_words, read_words)))
            elif share > WARN_ANALYTIC_SHARE:
                results.append(("WARN", title,
                                "analytics are %d%% of what is spoken (%d vs %d read from "
                                "cards): lean harder on cards" %
                                (round(share * 100), a_words, read_words)))
        # ---- logic-flow checks
        card_items = [it for it in items if it[0] == "card"]
        if chain is not None:
            steps_in_order = STEP_RE.findall(chain)
            ranks = [ORDER.index(x) for x in steps_in_order if x in ORDER]
            if ranks != sorted(ranks):
                results.append(("ERROR", title,
                                "chain steps are out of logical order (%s): the chain must run "
                                "UQ, TREND, LINK, IL, IMPACT" % " -> ".join(steps_in_order)))
            named = STEP_NAME_RE.findall(chain)
            for n, (step, nm) in enumerate(named):
                nm = nm.strip()
                if nm and n < len(card_items):
                    actual = card_items[n][3]
                    if actual and nm.lower() not in actual.lower() and actual.lower() not in nm.lower():
                        results.append(("WARN", title,
                                        "chain map says %s (%s) but card %d is %r: reorder the cards "
                                        "or fix the map" % (step, nm, n + 1, actual)))
            for n, it in enumerate(card_items):
                m = TAG_LABEL_RE.match(it[1])
                if m and chain is not None:
                    seq = STEP_RE.findall(chain)
                    if n < len(seq) and m.group(1).upper() != seq[n]:
                        results.append(("WARN", title,
                                        "card %d tag is labeled %s but the chain map has %s there" %
                                        (n + 1, m.group(1).upper(), seq[n])))
        evidence_numbers = set()
        for it in card_items:
            evidence_numbers |= _numbers(it[1]) | _numbers(it[4])
        for t in analytics:
            missing = sorted(_numbers(t) - evidence_numbers)
            if missing:
                results.append(("WARN", title,
                                "analytic uses number(s) %s that appear in no card of this "
                                "contention: %r" % (", ".join(missing), t[:60])))
    return results, len(secs)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("file", help="spec (.md/.json) or .docx")
    ap.add_argument("--con","--neg", action="store_true",
                    help="Con case / turns: do not require a SOLVENCY step")
    args = ap.parse_args(argv)
    events = events_from_docx(args.file) if args.file.lower().endswith(".docx") \
        else events_from_spec(args.file)
    results, n = lint(events, aff=not args.con)
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
