#!/usr/bin/env python3
"""Build a Verbatim-style .docx from a card/block spec (JSON or Markdown).

Usage:
    python tools/build_docx.py spec.json -o out.docx
    python tools/build_docx.py spec.md   -o out.docx [--team team.yaml]

No third-party packages are needed. See tools/README.md for the spec formats.
"""
import argparse
import json
import os
import re
import sys
import zipfile
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
STYLES_PATH = os.path.join(HERE, "styles", "verbatim_styles.xml")

NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'

HEADING_STYLE = {
    "pocket": "Heading1",
    "hat": "Heading2",
    "block": "Heading3",
    "tag": "Heading4",
}

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
</Types>"""

ROOT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>
</Relationships>"""

SETTINGS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<w:settings %s><w:defaultTabStop w:val="720"/></w:settings>' % NS)

SECT = ('<w:sectPr><w:pgSz w:w="12240" w:h="15840"/>'
        '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
        'w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>')


# --------------------------------------------------------------------------
# Run / paragraph XML helpers
# --------------------------------------------------------------------------

def _t(text):
    return '<w:t xml:space="preserve">%s</w:t>' % escape(text)


def run(text, mode):
    """mode: unread | underline | read | cite | cite_rest | url | plain"""
    if not text:
        return ""
    if mode == "read":
        rpr = ('<w:rStyle w:val="StyleUnderline"/>'
               '<w:highlight w:val="cyan"/>')
    elif mode == "underline":
        rpr = '<w:rStyle w:val="StyleUnderline"/>'
    elif mode == "cite":
        rpr = '<w:rStyle w:val="Style13ptBold"/>'
    elif mode == "cite_rest" or mode == "unread":
        rpr = '<w:sz w:val="16"/><w:szCs w:val="16"/>'
    elif mode == "url":
        rpr = ('<w:rStyle w:val="StyleUnderline"/>'
               '<w:sz w:val="16"/><w:szCs w:val="16"/>')
    elif mode == "plain":
        rpr = ""
    elif mode == "draft_read":
        # draft mode: proposed read text is bold + underlined, no highlight, for the debater to cut
        rpr = '<w:rStyle w:val="StyleUnderline"/><w:b/><w:bCs/>'
    elif mode == "draft_unread":
        rpr = ""
    else:
        raise ValueError("unknown run mode: %s" % mode)
    rpr_xml = "<w:rPr>%s</w:rPr>" % rpr if rpr else ""
    return "<w:r>%s%s</w:r>" % (rpr_xml, _t(text))


def para(runs_xml="", style=None):
    ppr = '<w:pPr><w:pStyle w:val="%s"/></w:pPr>' % style if style else ""
    return "<w:p>%s%s</w:p>" % (ppr, runs_xml)


# --------------------------------------------------------------------------
# Body markup:  ==read aloud==   __underlined, not read__   plain = unread
# --------------------------------------------------------------------------

_MARKUP = re.compile(r"(==.+?==|__.+?__)", re.S)


def parse_markup(text):
    """Return a list of (text, mode) runs from the card body markup."""
    runs = []
    for piece in _MARKUP.split(text):
        if not piece:
            continue
        if piece.startswith("==") and piece.endswith("==") and len(piece) > 4:
            runs.append((piece[2:-2], "read"))
        elif piece.startswith("__") and piece.endswith("__") and len(piece) > 4:
            runs.append((piece[2:-2], "underline"))
        else:
            runs.append((piece, "unread"))
    return runs


def body_runs(card):
    """Return runs for a card dict. Accepts 'body' markup string or run list."""
    body = card.get("body", "")
    if isinstance(body, str):
        return parse_markup(body)
    return [(r["text"], r.get("mode", "unread")) for r in body]


# --------------------------------------------------------------------------
# Cite rendering
# --------------------------------------------------------------------------

def _join(parts, sep=", "):
    return sep.join(p for p in parts if p)


def cite_runs(cite):
    """Return [(text, mode)] for the cite line.

    Two house styles (see core/cite-format.md):
      frontline: **Name**, [Author, quals, date, "Title," Publication. DOA: x URL] //initials
      case:      **Name** (Author, quals, Publication, date, "Title", URL) initials - DOA: x
    A 'raw' key (string) is used verbatim after the bold name.
    """
    name = cite.get("name", "")
    out = [(name, "cite")]
    if cite.get("raw"):
        out.append((" " + cite["raw"], "cite_rest"))
        return out

    style = cite.get("style", "case")
    author = cite.get("author", "")
    quals = cite.get("quals", "")
    date = cite.get("date", "")
    title = cite.get("title", "")
    pub = cite.get("publication", "")
    url = cite.get("url", "")
    doa = cite.get("doa", "")
    initials = cite.get("initials", "")

    if style == "frontline":
        head = _join([author, quals, date])
        t = '"%s,"' % title if title else ""
        mid = _join([head, t], ", ")
        if pub:
            mid += (" " if t else ", ") + pub + "."
        if doa:
            mid += " DOA: %s" % doa
        out.append((", [" + mid.strip() + " ", "cite_rest"))
        if url:
            out.append((url, "url"))
        out.append(("]" + (" //%s" % initials if initials else ""), "cite_rest"))
    else:
        t = '"%s"' % title if title else ""
        mid = _join([author, quals, pub, date, t])
        out.append((" (" + mid + (", " if url else ""), "cite_rest"))
        if url:
            out.append((url, "url"))
        tail = ")"
        if initials:
            tail += " " + initials
        if doa:
            tail += " - DOA: %s" % doa
        out.append((tail, "cite_rest"))
    return out


# --------------------------------------------------------------------------
# Spec -> document.xml
# --------------------------------------------------------------------------

def render_item(item, defaults):
    kind = item.get("type")
    if kind in HEADING_STYLE:
        return para(run(item["text"], "plain"), HEADING_STYLE[kind])
    if kind == "analytic":
        return para(run(item["text"], "plain"), "Analytic")
    if kind == "undertag":
        return para(run(item["text"], "plain"), "Undertag")
    if kind == "text":
        return para(run(item["text"], "plain"))
    if kind == "card":
        cite = dict(defaults.get("cite", {}))
        cite.update(item.get("cite", {}))
        parts = [para(run(item["tag"], "plain"), "Heading4")]
        parts.append(para("".join(run(t, m) for t, m in cite_runs(cite))))
        parts.append(para())  # blank line between cite and body (house style)
        body_paras = item.get("body_paragraphs")
        if body_paras is None:
            body_paras = [body_runs(item)]
        draft = defaults.get("_draft", False)
        for runs in body_paras:
            if draft:
                runs = [(t, {"read": "draft_read", "unread": "draft_unread"}.get(m, m))
                        for t, m in runs]
            parts.append(para("".join(run(t, m) for t, m in runs)))
        return "".join(parts)
    raise ValueError("unknown item type: %r" % kind)


def build_document_xml(spec):
    defaults = spec.get("defaults", {})
    body = "".join(render_item(i, defaults) for i in spec["items"])
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<w:document %s><w:body>%s%s</w:body></w:document>' % (NS, body, SECT))


def write_docx(spec, out_path, draft=False):
    """Write the .docx. draft=True makes a cutting copy: proposed read text is bold and
    underlined (no highlight) and surrounding context stays at normal size, so the
    debater can cut it in an editor. The default (final) uses highlight + 8pt unread."""
    spec = dict(spec)
    spec["defaults"] = dict(spec.get("defaults", {}), _draft=draft)
    with open(STYLES_PATH, "r", encoding="utf-8") as f:
        styles = f.read()
    doc = build_document_xml(spec)
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", ROOT_RELS)
        z.writestr("word/document.xml", doc)
        z.writestr("word/styles.xml", styles)
        z.writestr("word/settings.xml", SETTINGS)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)


# --------------------------------------------------------------------------
# Markdown spec parser
# --------------------------------------------------------------------------

CITE_KEYS = {"cite": "name", "author": "author", "quals": "quals", "date": "date",
             "title": "title", "publication": "publication", "url": "url",
             "doa": "doa", "initials": "initials", "style": "style", "raw": "raw",
             "source": "source"}


def parse_markdown(text):
    """Parse the Markdown card format described in tools/README.md."""
    items = []
    lines = text.splitlines()
    i = 0
    heading = re.compile(r"^(#{1,4})\s+(.*)$")
    names = {1: "pocket", 2: "hat", 3: "block", 4: "tag"}
    while i < len(lines):
        line = lines[i]
        m = heading.match(line)
        if m:
            level, title = len(m.group(1)), m.group(2).strip()
            # a #### followed by "cite:" is a card
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if level == 4 and j < len(lines) and lines[j].lower().startswith("cite:"):
                cite = {}
                k = j
                while k < len(lines) and lines[k].strip() != "---":
                    key, _, val = lines[k].partition(":")
                    key = key.strip().lower()
                    if key in CITE_KEYS:
                        cite[CITE_KEYS[key]] = val.strip()
                    k += 1
                k += 1  # skip ---
                body, paras = [], []
                while k < len(lines) and not lines[k].startswith(("#", ">")):
                    if lines[k].strip():
                        body.append(lines[k].strip())
                    elif body:
                        paras.append(" ".join(body))
                        body = []
                    k += 1
                if body:
                    paras.append(" ".join(body))
                items.append({"type": "card", "tag": title, "cite": cite,
                              "body_paragraphs": [parse_markup(p) for p in paras]})
                i = k
                continue
            items.append({"type": names[level], "text": title})
        elif line.startswith(">"):
            items.append({"type": "analytic", "text": line.lstrip("> ").strip()})
        elif line.strip():
            items.append({"type": "text", "text": line.strip()})
        i += 1
    return {"items": items}


def load_flat_yaml(path):
    """Tiny flat 'key: value' reader for team.yaml (no nesting)."""
    data = {}
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.split("#", 1)[0].rstrip()
            if ":" in line and not line.startswith(" "):
                k, _, v = line.partition(":")
                data[k.strip()] = v.strip().strip("'\"")
    return data


def load_spec(path, team_path=None):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    spec = json.loads(raw) if path.lower().endswith(".json") else parse_markdown(raw)
    if team_path and os.path.exists(team_path):
        team = load_flat_yaml(team_path)
        d = spec.setdefault("defaults", {}).setdefault("cite", {})
        if team.get("cutter_initials"):
            d.setdefault("initials", team["cutter_initials"])
        if team.get("cite_style"):
            d.setdefault("style", team["cite_style"])
    return spec


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("spec", help="spec file (.json or .md)")
    p.add_argument("-o", "--out", required=True, help="output .docx path")
    p.add_argument("--team", default="team.yaml", help="optional team config")
    p.add_argument("--draft", action="store_true",
                   help="cutting copy: proposed read text bold+underlined, context at normal size")
    args = p.parse_args(argv)
    spec = load_spec(args.spec, args.team)
    write_docx(spec, args.out, draft=args.draft)
    print("wrote %s (%d items)" % (args.out, len(spec["items"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
