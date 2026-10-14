#!/usr/bin/env python3
"""Inspect a Verbatim-style .docx: outline, cites, and highlight statistics.

Usage:
    python tools/inspect_docx.py file.docx            # outline + stats
    python tools/inspect_docx.py file.docx --cards    # cite lines + highlighted text per card
    python tools/inspect_docx.py file.docx --json     # machine-readable paragraphs
    python tools/inspect_docx.py file.docx --text     # plain text, one paragraph per line

Use it to learn how a team formats its files before cutting new cards.
"""
import argparse
import collections
import json
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
HEADING_NAMES = {"Heading1": "Pocket", "Heading2": "Hat",
                 "Heading3": "Block", "Heading4": "Tag"}


def _val(el, tag):
    child = el.find(W + tag)
    return None if child is None else child.get(W + "val", "on")


def read_paragraphs(path):
    """Return paragraphs as dicts: {style, runs:[{text,rstyle,highlight,sz,u,b}]}."""
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    out = []
    for p in root.iter(W + "p"):
        ppr = p.find(W + "pPr")
        style = _val(ppr, "pStyle") if ppr is not None else None
        runs = []
        for r in p.findall(W + "r"):
            text = "".join(t.text or "" for t in r.findall(W + "t"))
            if not text:
                continue
            rpr = r.find(W + "rPr")
            info = {"text": text, "rstyle": None, "highlight": None,
                    "sz": None, "u": False, "b": False}
            if rpr is not None:
                info["rstyle"] = _val(rpr, "rStyle")
                info["highlight"] = _val(rpr, "highlight")
                info["sz"] = _val(rpr, "sz")
                u = _val(rpr, "u")
                info["u"] = bool(u and u != "none")
                b = _val(rpr, "b")
                info["b"] = bool(b and b not in ("0", "false"))
            runs.append(info)
        out.append({"style": style or "Normal", "runs": runs})
    return out


def para_text(p):
    return "".join(r["text"] for r in p["runs"])


def is_read(run):
    """A run is 'read aloud' when it is highlighted."""
    return bool(run["highlight"])


def is_underlined(run):
    return run["rstyle"] == "StyleUnderline" or run["u"]


def card_groups(paras):
    """Yield (tag, cite_paragraph, body_paragraphs) for each Tag followed by a cite."""
    i = 0
    while i < len(paras):
        if paras[i]["style"] == "Heading4":
            j = i + 1
            while j < len(paras) and not paras[j]["runs"]:
                j += 1
            if j < len(paras) and paras[j]["style"] == "Normal":
                body = []
                k = j + 1
                while k < len(paras) and paras[k]["style"] == "Normal":
                    if paras[k]["runs"]:
                        body.append(paras[k])
                    k += 1
                yield para_text(paras[i]), paras[j], body
                i = k
                continue
        i += 1


def outline(paras):
    lines = []
    for p in paras:
        name = HEADING_NAMES.get(p["style"])
        if name:
            indent = "  " * (int(p["style"][-1]) - 1)
            lines.append("%s[%s] %s" % (indent, name, para_text(p)[:110]))
    return lines


def stats(paras):
    hl = collections.Counter()
    rstyles = collections.Counter()
    sizes = collections.Counter()
    pstyles = collections.Counter(p["style"] for p in paras)
    for p in paras:
        for r in p["runs"]:
            if r["highlight"]:
                hl[r["highlight"]] += 1
            if r["rstyle"]:
                rstyles[r["rstyle"]] += 1
            if r["sz"]:
                sizes[r["sz"]] += 1
    return {"paragraph_styles": dict(pstyles), "run_styles": dict(rstyles),
            "highlight_colors": dict(hl), "font_sizes_half_points": dict(sizes)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("docx")
    ap.add_argument("--cards", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--text", action="store_true",
                    help="plain text, one paragraph per line (e.g. to read an opposing case)")
    args = ap.parse_args(argv)
    paras = read_paragraphs(args.docx)
    if args.text:
        for p in paras:
            line = para_text(p)
            if line.strip():
                print(line)
        return 0
    if args.json:
        json.dump(paras, sys.stdout, indent=1)
        return 0
    if args.cards:
        for tag, cite, body in card_groups(paras):
            print("TAG :", tag)
            print("CITE:", para_text(cite)[:300])
            read = [r["text"] for b in body for r in b["runs"] if is_read(r)]
            print("READ:", " | ".join(read)[:400] or "(none highlighted)")
            print()
        return 0
    print("\n".join(outline(paras)) or "(no headings)")
    print()
    print(json.dumps(stats(paras), indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
