import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))

import build_docx  # noqa: E402
import inspect_docx  # noqa: E402
import lint_cites  # noqa: E402
import verify_quotes  # noqa: E402

EXAMPLE_MD = os.path.join(ROOT, "examples", "example-cards.md")
SOURCE = os.path.join(ROOT, "examples", "source-article.txt")


class MarkupTests(unittest.TestCase):
    def test_modes(self):
        runs = build_docx.parse_markup("plain __under__ ==read== tail")
        self.assertEqual([m for _, m in runs],
                         ["unread", "underline", "unread", "read", "unread"])

    def test_cite_styles(self):
        cite = {"name": "Doe 25", "author": "Jane Doe", "quals": "Prof", "date": "1-1-2025",
                "title": "T", "publication": "P", "url": "https://x.org", "doa": "2-2-2026",
                "initials": "AB"}
        front = "".join(t for t, _ in build_docx.cite_runs(dict(cite, style="frontline")))
        case = "".join(t for t, _ in build_docx.cite_runs(dict(cite, style="case")))
        self.assertTrue(front.startswith("Doe 25, [Jane Doe, Prof, 1-1-2025"))
        self.assertTrue(front.endswith("] //AB"))
        self.assertTrue(case.startswith("Doe 25 (Jane Doe, Prof, P, 1-1-2025"))
        self.assertTrue(case.endswith(") AB - DOA: 2-2-2026"))


class DocxRoundTripTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.out = os.path.join(self.tmp, "out.docx")
        spec = build_docx.load_spec(EXAMPLE_MD)
        build_docx.write_docx(spec, self.out)
        self.paras = inspect_docx.read_paragraphs(self.out)

    def test_heading_hierarchy(self):
        styles = [p["style"] for p in self.paras if p["style"].startswith("Heading")]
        self.assertEqual(styles[:3], ["Heading1", "Heading2", "Heading3"])

    def test_only_cyan_highlight(self):
        colors = inspect_docx.stats(self.paras)["highlight_colors"]
        self.assertEqual(set(colors), {"cyan"})

    def test_unread_text_is_8pt(self):
        unread = [r for _, _, body in inspect_docx.card_groups(self.paras)
                  for b in body for r in b["runs"]
                  if not r["highlight"] and not r["rstyle"]]
        self.assertTrue(unread)
        self.assertTrue(all(r["sz"] == "16" for r in unread))

    def test_cite_name_uses_cite_style(self):
        groups = list(inspect_docx.card_groups(self.paras))
        self.assertEqual(len(groups), 4)
        first_run = groups[0][1]["runs"][0]
        self.assertEqual(first_run["rstyle"], "Style13ptBold")

    def test_styles_part_defines_verbatim_names(self):
        import zipfile
        with zipfile.ZipFile(self.out) as z:
            styles = z.read("word/styles.xml").decode()
        for alias in ("Pocket", "Hat", "Block", "Tag", "Cite", "Underline", "Analytic"):
            self.assertIn('w:val="%s"' % alias, styles)


class VerifyTests(unittest.TestCase):
    def setUp(self):
        with open(SOURCE, encoding="utf-8") as f:
            self.source = f.read()

    def test_example_verifies(self):
        spec = build_docx.load_spec(EXAMPLE_MD)
        for item in spec["items"]:
            if item["type"] == "card":
                self.assertIsNone(verify_quotes.verify_card(item, self.source))

    def test_altered_word_fails(self):
        card = {"type": "card", "tag": "t", "cite": {},
                "body": "Foot traffic fell, and total sales were flat to slightly up"}
        self.assertIsNotNone(verify_quotes.verify_card(card, self.source))

    def test_ellipsis_allows_omission(self):
        card = {"type": "card", "tag": "t", "cite": {},
                "body": "Merchants predicted disaster ... Foot traffic rose"}
        self.assertIsNone(verify_quotes.verify_card(card, self.source))

    def test_out_of_order_fails(self):
        card = {"type": "card", "tag": "t", "cite": {},
                "body": "Foot traffic rose ... Merchants predicted disaster"}
        self.assertIsNotNone(verify_quotes.verify_card(card, self.source))

    def test_curly_quotes_normalized(self):
        card = {"type": "card", "tag": "t", "cite": {},
                "body": "“Merchants predicted disaster,” Reyes said."}
        self.assertIsNone(verify_quotes.verify_card(card, self.source))


class LintTests(unittest.TestCase):
    def test_complete_cite_passes(self):
        spec = build_docx.load_spec(EXAMPLE_MD)
        for item in spec["items"]:
            if item["type"] == "card":
                self.assertEqual(lint_cites.lint(item["cite"]), [])

    def test_missing_fields_flagged(self):
        problems = lint_cites.lint({"name": "Smith 24"})
        self.assertIn("missing url", problems)
        self.assertIn("missing doa", problems)

    def test_bad_name_flagged(self):
        problems = lint_cites.lint({"name": "smith"})
        self.assertTrue(any("Lastname" in p for p in problems))


if __name__ == "__main__":
    unittest.main()


class RepoStructureTests(unittest.TestCase):
    def test_skills_have_front_matter(self):
        import glob
        skills = glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md"))
        self.assertGreaterEqual(len(skills), 9)
        for path in skills:
            with open(path, encoding="utf-8") as f:
                text = f.read()
            self.assertTrue(text.startswith("---\nname: "), path)
            head = text.split("---")[1]
            self.assertIn('description: "', head, path)

    def test_protocol_files_exist(self):
        for rel in ("core/integrity.md", "core/cutting-rules.md", "core/cite-format.md",
                    "speeches/case/PROTOCOL.md", "speeches/rebuttal/PROTOCOL.md",
                    "speeches/frontlines/PROTOCOL.md", "speeches/blocks/PROTOCOL.md",
                    "speeches/crossx/PROTOCOL.md", "speeches/summary-final/PROTOCOL.md",
                    "speeches/prep/PROTOCOL.md", "AGENTS.md"):
            self.assertTrue(os.path.exists(os.path.join(ROOT, rel)), rel)

    def test_all_docx_parts_wellformed(self):
        import glob
        import zipfile
        import xml.dom.minidom
        files = glob.glob(os.path.join(ROOT, "templates", "*.docx")) + \
            glob.glob(os.path.join(ROOT, "examples", "*.docx"))
        self.assertTrue(files)
        for path in files:
            with zipfile.ZipFile(path) as z:
                for name in z.namelist():
                    xml.dom.minidom.parseString(z.read(name))

    def test_text_extraction(self):
        import io
        import contextlib
        buf = io.StringIO()
        out = os.path.join(tempfile.mkdtemp(), "t.docx")
        build_docx.write_docx(build_docx.load_spec(EXAMPLE_MD), out)
        with contextlib.redirect_stdout(buf):
            inspect_docx.main([out, "--text"])
        self.assertIn("Foot traffic rose", buf.getvalue())


class DocsTests(unittest.TestCase):
    def test_formatting_disclaimer_present(self):
        for rel in ("README.md", "AGENTS.md"):
            with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
                text = f.read()
            self.assertIn("CardMirror", text, rel)
            self.assertIn("support", text, rel)


class LintCardsAndBlocksTests(unittest.TestCase):
    def test_thin_card_flagged(self):
        import lint_cards
        runs = [("A single sentence that is entirely read aloud by the speaker here.", "read")]
        probs = lint_cards.problems_for(lint_cards.measure(runs), "block")
        self.assertTrue(probs)

    def test_context_card_passes(self):
        import lint_cards
        runs = [("Setup text before the point. " * 4, "unread"),
                ("The key claim read aloud.", "read"),
                ("Qualification and next sentence after. " * 4, "unread")]
        self.assertEqual(lint_cards.problems_for(lint_cards.measure(runs), "block"), [])

    def test_example_blocks_pass(self):
        import lint_blocks
        results, n = lint_blocks.lint(lint_blocks.events_from_spec(EXAMPLE_MD))
        self.assertEqual(n, 2)
        self.assertEqual([r for r in results if r[0] == "ERROR"], [])

    def test_cardless_block_fails(self):
        import lint_blocks
        events = [("block", "A2: X"), ("analytic", "Neg Argument: X is bad."),
                  ("analytic", "1. Extend Smith 25: it says things."), ("tag", "2. Answer")]
        results, _ = lint_blocks.lint(events)
        levels = [(r[0], r[2]) for r in results]
        self.assertTrue(any("no cut cards" in m for _, m in levels))
        self.assertTrue(any("tag with no card" in m for _, m in levels))

    def test_card_named_title_and_card_pointing_analytics_warn(self):
        import lint_blocks
        events = [("block", "AT: Reyes 24 (Pilot Streets Got Slower)"), ("analytic", "Pro Argument: X."),
                  ("analytic", "Their own Reyes card says the pilot was short."),
                  ("card", "1. Answer"), ("analytic", "Plain.")]
        results, _ = lint_blocks.lint(events)
        msgs = " | ".join(r[2] for r in results)
        self.assertIn("title names a card", msgs)
        self.assertIn("points at their card", msgs)

    def test_claim_named_block_has_no_card_warning(self):
        import lint_blocks
        events = [("block", "AT: Car Bans Make Nearby Streets Slower"),
                  ("analytic", "Pro Argument: X."), ("analytic", "1. Gas is chosen for speed."),
                  ("card", "2. Answer"), ("analytic", "Plain.")]
        results, _ = lint_blocks.lint(events)
        msgs = " | ".join(r[2] for r in results)
        self.assertNotIn("title names a card", msgs)
        self.assertNotIn("points at their card", msgs)

    def test_missing_argument_statement_fails(self):
        import lint_blocks
        events = [("block", "A2: X"), ("card", "1. Answer"), ("analytic", "2. Closing.")]
        results, _ = lint_blocks.lint(events)
        self.assertTrue(any("opposing argument" in r[2] for r in results))

    def test_draft_mode_bolds_read_text(self):
        out = os.path.join(tempfile.mkdtemp(), "d.docx")
        build_docx.write_docx(build_docx.load_spec(EXAMPLE_MD), out, draft=True)
        paras = inspect_docx.read_paragraphs(out)
        runs = [r for _, _, body in inspect_docx.card_groups(paras) for b in body for r in b["runs"]]
        self.assertTrue(any(r["b"] for r in runs))
        self.assertFalse(any(r["highlight"] for r in runs))


class ReadFirstFolderTests(unittest.TestCase):
    def test_paths_mentioned_in_read_first_exist(self):
        import glob
        import re
        generated = {"out.docx", "out-DRAFT.docx", "team.yaml", "file.md", "file.docx", "spec.md", "sources/"}
        folder = os.path.join(ROOT, "00-READ-THIS-FIRST")
        files = glob.glob(os.path.join(folder, "*.md"))
        self.assertGreaterEqual(len(files), 3)
        for path in files:
            with open(path, encoding="utf-8") as f:
                text = f.read()
            for ref in re.findall(r"`([A-Za-z0-9_./-]+(?:\.md|\.docx|\.txt|\.py|\.yaml|\.pdf|/))`", text):
                if ref in generated or ref.startswith("<") or "<" in ref:
                    continue
                if ref.startswith(("out", "my-prep")):
                    continue
                if "/" in ref.rstrip("/"):
                    found = os.path.exists(os.path.join(ROOT, ref)) or \
                        os.path.exists(os.path.join(folder, ref)) or \
                        os.path.exists(os.path.join(ROOT, "speeches", ref))
                else:  # bare name: any file or folder with that name somewhere in the repo
                    name = ref.rstrip("/")
                    found = any(name in files or name in dirs
                                for _, dirs, files in os.walk(ROOT)
                                if ".git" not in _)
                self.assertTrue(found, "%s mentions missing path %s" %
                                (os.path.basename(path), ref))


class LintCaseTests(unittest.TestCase):
    CASE_MD = os.path.join(ROOT, "examples", "example-case.md")

    def test_example_case_passes(self):
        import lint_case
        results, n = lint_case.lint(lint_case.events_from_spec(self.CASE_MD))
        self.assertEqual(n, 1)
        self.assertEqual([r for r in results if r[0] == "ERROR"], [])

    def test_example_case_cards_verify(self):
        spec = build_docx.load_spec(self.CASE_MD)
        cards = [i for i in spec["items"] if i["type"] == "card"]
        self.assertEqual(len(cards), 6)
        base = os.path.dirname(self.CASE_MD)
        for card in cards:
            with open(os.path.join(base, card["cite"]["source"]), encoding="utf-8") as f:
                self.assertIsNone(verify_quotes.verify_card(card, f.read()))

    def test_one_card_contention_fails(self):
        import lint_case
        events = [("heading", 2, "Contention one: X"),
                  ("analytic", 0, "Our claim is X."),
                  ("card", 0, "Only card")]
        results, _ = lint_case.lint(events)
        msgs = " ".join(r[2] for r in results)
        self.assertIn("only 1 card", msgs)
        self.assertIn("no chain map", msgs)

    def test_missing_step_flagged(self):
        import lint_case
        events = [("heading", 2, "Contention one: X"),
                  ("analytic", 0, "Chain: UQ (A) -> IMPACT (B)")] + \
                 [("card", 0, "c%d" % i) for i in range(4)]
        results, _ = lint_case.lint(events)
        msgs = " ".join(r[2] for r in results)
        self.assertIn("no LINK step", msgs)
        self.assertIn("no SOLVENCY step", msgs)

    def test_neg_does_not_require_solvency(self):
        import lint_case
        events = [("heading", 2, "DA: X"),
                  ("analytic", 0, "Chain: UQ (A) -> LINK (B) -> IMPACT (C)")] + \
                 [("card", 0, "c%d" % i) for i in range(4)]
        results, _ = lint_case.lint(events, aff=False)
        self.assertEqual([r for r in results if r[0] == "ERROR"], [])

    def test_step_without_card_flagged(self):
        import lint_case
        events = [("heading", 2, "Contention one: X"),
                  ("analytic", 0, "Chain: UQ (A) -> TREND (B) -> LINK (C) -> IL (D) -> IMPACT (E) -> SOLVENCY (F)")] + \
                 [("card", 0, "c%d" % i) for i in range(4)]
        results, _ = lint_case.lint(events)
        self.assertTrue(any("step has no card" in r[2] for r in results))

    def test_long_analytic_warns(self):
        import lint_case
        events = [("heading", 2, "Contention one: X"),
                  ("analytic", 0, "Chain: UQ (A) -> LINK (B) -> IMPACT (C) -> SOLVENCY (D)"),
                  ("analytic", 0, " ".join(["word"] * 120))] + \
                 [("card", 0, "c%d" % i) for i in range(4)]
        results, _ = lint_case.lint(events)
        self.assertTrue(any(r[0] == "WARN" and "long analytic" in r[2] for r in results))


class LintCaseSolvencyTests(unittest.TestCase):
    def _chain(self, extra):
        return [("heading", 2, "Contention one: X"),
                ("analytic", 0, "Chain: UQ (A) -> LINK (B) -> IMPACT (C) -> SOLVENCY (D)")] + extra + \
               [("card", 0, "c%d" % i, 40) for i in range(4)]

    def test_aff_requires_solvency_analytic(self):
        import lint_case
        results, _ = lint_case.lint(self._chain([]))
        self.assertTrue(any("Solvency:" in r[2] for r in results))

    def test_solvency_analytic_satisfies(self):
        import lint_case
        results, _ = lint_case.lint(self._chain([("analytic", 0, "Solvency: the resolution removes the cause.")]))
        self.assertEqual([r for r in results if r[0] == "ERROR"], [])

    def test_analytics_outweighing_cards_fail(self):
        import lint_case
        big = " ".join(["word"] * 55)
        ev = [("analytic", 0, "Solvency: " + big)] + [("analytic", 0, big) for _ in range(6)]
        results, _ = lint_case.lint(self._chain(ev))
        self.assertTrue(any(r[0] == "ERROR" and "analytics are" in r[2] for r in results))

    def test_neg_needs_no_solvency_analytic(self):
        import lint_case
        results, _ = lint_case.lint(self._chain([]), aff=False)
        self.assertFalse(any("Solvency:" in r[2] for r in results))


class FlowChecksTests(unittest.TestCase):
    def _ev(self, chain, cards, analytics=()):
        ev = [("heading", 2, "Contention one: X"), ("analytic", 0, chain)]
        for name, tag, body in cards:
            ev.append(("card", 0, tag, 10, name, body))
        for a in analytics:
            ev.append(("analytic", 0, a))
        return ev

    def test_out_of_order_chain_errors(self):
        import lint_case
        ev = self._ev("Chain: IMPACT (A) -> UQ (B) -> LINK (C) -> SOLVENCY (D)",
                      [("A 25", "t1", ""), ("B 25", "t2", ""), ("C 25", "t3", ""), ("D 25", "t4", "")],
                      ["Solvency: it works."])
        results, _ = lint_case.lint(ev)
        self.assertTrue(any(r[0] == "ERROR" and "out of logical order" in r[2] for r in results))

    def test_chain_map_name_mismatch_warns(self):
        import lint_case
        ev = self._ev("Chain: UQ (Smith 25) -> LINK (Jones 24) -> IMPACT (Lee 23) -> SOLVENCY (Kim 22)",
                      [("Smith 25", "t1", ""), ("Zed 20", "t2", ""), ("Lee 23", "t3", ""), ("Kim 22", "t4", "")],
                      ["Solvency: it works."])
        results, _ = lint_case.lint(ev)
        self.assertTrue(any(r[0] == "WARN" and "chain map says LINK" in r[2] for r in results))

    def test_matching_chain_map_is_clean(self):
        import lint_case
        ev = self._ev("Chain: UQ (Smith 25) -> LINK (Jones 24) -> IMPACT (Lee 23) -> SOLVENCY (Kim 22)",
                      [("Smith 25", "t1", ""), ("Jones 24", "t2", ""), ("Lee 23", "t3", ""), ("Kim 22", "t4", "")],
                      ["Solvency: it works."])
        results, _ = lint_case.lint(ev)
        self.assertEqual(results, [])

    def test_tag_label_mismatch_warns(self):
        import lint_case
        ev = self._ev("Chain: UQ (A) -> LINK (B) -> IMPACT (C) -> SOLVENCY (D)",
                      [("A", "LINK: wrong label", ""), ("B", "LINK: right", ""), ("C", "IMPACT: x", ""), ("D", "SOLVENCY: y", "")],
                      ["Solvency: it works."])
        results, _ = lint_case.lint(ev)
        self.assertTrue(any("is labeled LINK but the chain map has UQ" in r[2] for r in results))

    def test_unsupported_number_in_analytic_warns(self):
        import lint_case
        ev = self._ev("Chain: UQ (A) -> LINK (B) -> IMPACT (C) -> SOLVENCY (D)",
                      [("A", "UQ: 412 people injured", ""), ("B", "t", ""), ("C", "t", ""), ("D", "t", "")],
                      ["Solvency: injuries fall 73 percent."])
        results, _ = lint_case.lint(ev)
        self.assertTrue(any("73" in r[2] and "no card" in r[2] for r in results))

    def test_supported_number_in_analytic_ok(self):
        import lint_case
        ev = self._ev("Chain: UQ (A) -> LINK (B) -> IMPACT (C) -> SOLVENCY (D)",
                      [("A", "UQ: 412 people injured", ""), ("B", "t", ""), ("C", "t", ""), ("D", "t", "")],
                      ["Solvency: all 412 of those injuries are in the core."])
        results, _ = lint_case.lint(ev)
        self.assertFalse(any("no card" in r[2] for r in results))

    def test_tag_story_runs_on_example(self):
        import io
        import contextlib
        import tag_story
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            tag_story.main([os.path.join(ROOT, "examples", "example-case.md")])
        out = buf.getvalue()
        self.assertIn("Chain map:", out)
        self.assertIn("SOLVENCY", out)
        self.assertIn("numbers:", out)


class LibraryAndLayTests(unittest.TestCase):
    def test_library_index_and_search(self):
        import io
        import contextlib
        import library
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            library.main(["index", os.path.join(ROOT, "examples")])
            library.main(["search", os.path.join(ROOT, "examples"), "travel", "--text"])
        out = buf.getvalue()
        self.assertIn("Whitfield 25", out)
        self.assertIn("A2: Retail will collapse", out)
        self.assertIn("tag:", out)

    def test_library_search_no_match(self):
        import io
        import contextlib
        import library
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            library.main(["search", os.path.join(ROOT, "examples"), "zzzznotaterm"])
        self.assertIn("no cards match", buf.getvalue())

    def test_lay_flags_missing_plain_analytic(self):
        import lint_blocks
        events = [("block", "A2: X"), ("analytic", "Neg Argument: X."), ("analytic", "1. Overview."),
                  ("card", "2. Answer"), ("card", "3. Another"), ("analytic", "4. Closing.")]
        results, _ = lint_blocks.lint(events, lay=True)
        self.assertTrue(any("no plain-English analytic" in r[2] for r in results))

    def test_lay_flags_ai_labels_and_arrows(self):
        import lint_blocks
        events = [("block", "A2: X"), ("analytic", "Neg Argument: X."), ("card", "2. Answer"),
                  ("analytic", "Lay version: this means cars are bad."),
                  ("card", "3. Another"), ("analytic", "A -> B -> C"), ("analytic", "4. Closing.")]
        results, _ = lint_blocks.lint(events, lay=True)
        msgs = " ".join(r[2] for r in results)
        self.assertIn("AI label", msgs)

    def test_lay_clean_block_passes(self):
        import lint_blocks
        events = [("block", "A2: X"), ("analytic", "Neg Argument: X."), ("analytic", "1. Overview."),
                  ("card", "2. Answer"), ("analytic", "This means the study found no extra traffic."),
                  ("card", "3. Another"), ("analytic", "So the plan does not make things worse."),
                  ("analytic", "4. Closing.")]
        results, _ = lint_blocks.lint(events, lay=True)
        self.assertEqual([r for r in results if r[0] in ("ERROR", "WARN")], [])


class GoodVsBadAndReferencesTests(unittest.TestCase):
    GVB = os.path.join(ROOT, "examples", "good-vs-bad")

    def test_good_rebuttal_passes_everything(self):
        import lint_blocks
        path = os.path.join(self.GVB, "rebuttal-good.md")
        results, n = lint_blocks.lint(lint_blocks.events_from_spec(path), lay=True)
        self.assertEqual(n, 1)
        self.assertEqual([r for r in results if r[0] in ("ERROR", "WARN")], [])
        spec = build_docx.load_spec(path)
        for item in spec["items"]:
            if item["type"] == "card":
                src = os.path.join(self.GVB, item["cite"]["source"])
                with open(src, encoding="utf-8") as f:
                    self.assertIsNone(verify_quotes.verify_card(item, f.read()))

    def test_bad_rebuttal_fails(self):
        import lint_blocks
        path = os.path.join(self.GVB, "rebuttal-bad.md")
        results, _ = lint_blocks.lint(lint_blocks.events_from_spec(path))
        self.assertTrue(any(r[0] == "ERROR" for r in results))

    def test_bad_case_fails(self):
        import lint_case
        path = os.path.join(self.GVB, "case-bad.md")
        results, _ = lint_case.lint(lint_case.events_from_spec(path))
        msgs = " ".join(r[2] for r in results)
        self.assertIn("only 1 card", msgs)
        self.assertIn("no chain map", msgs)
        self.assertIn("analytics are", msgs)

    def test_new_guides_exist(self):
        for rel in ("core/research-guide.md", "core/refutation-guide.md", "core/judge-adaptation.md",
                    "core/file-organization.md", "core/logic-flow.md", "core/argument-structure.md",
                    "speeches/backlines/PROTOCOL.md", "playbooks/README.md",
                    "playbooks/01-case-from-scratch.md", "playbooks/02-answer-an-opposing-case.md",
                    "playbooks/03-blocks-library.md", "playbooks/04-frontlines.md",
                    "playbooks/05-backlines-and-summary.md", "playbooks/06-use-my-files-as-context.md",
                    "examples/good-vs-bad/link-chains.md", "examples/good-vs-bad/cards.md",
                    "examples/good-vs-bad/rebuttals.md", "examples/good-vs-bad/analytics.md"):
            self.assertTrue(os.path.exists(os.path.join(ROOT, rel)), rel)

    def test_no_broken_repo_paths_in_docs(self):
        import glob
        import re
        skip_dirs = ("/.git/", "/sources/", "/private-fixtures/")
        generated = {"team.yaml", "library-index.md", "research-notes.md", "case.md", "case.docx",
                     "blocks.md", "blocks.docx", "rebuttal.md", "rebuttal.docx", "spec.md", "file.md",
                     "file.docx", "cards.md", "cards.docx", "out.docx", "out-DRAFT.docx",
                     "case-DRAFT.docx", "their-case.docx", "their-case.pdf", "their-case.txt",
                     "our-case.docx", "case-out.docx", "rebuttal-good.docx", "check.docx"}
        pat = re.compile(r"`((?:core|speeches|playbooks|examples|templates|tools|docs|formats|skills|"
                         r"schemas|tests)/[A-Za-z0-9_./-]+\.(?:md|py|docx|yaml|txt|pdf|json))`")
        bad = []
        for path in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
            if any(d in path for d in skip_dirs):
                continue
            with open(path, encoding="utf-8") as f:
                text = f.read()
            for ref in pat.findall(text):
                base = os.path.basename(ref)
                if base in generated or "<" in ref or "*" in ref:
                    continue
                if ref.startswith("sources/") or "/sources/" in ref:
                    continue
                if not os.path.exists(os.path.join(ROOT, ref)):
                    bad.append("%s -> %s" % (os.path.relpath(path, ROOT), ref))
        self.assertEqual(bad, [], "\n".join(bad[:20]))
