# Fresh-session test prompt 2: answer an opposing case from the user's files

A harder test than `fresh-session-test-prompt.md`: the agent must read an opposing case, use the user's existing files as context, answer specific cards with their own evidence, and write blocks and a rebuttal that pass the repo's checks. It needs the private `reference/` folder (this is a private-repo test); on a public checkout, substitute any opposing case file.

Paste into a brand-new session started in an empty folder:

```
Clone https://github.com/techtanush/OpenSourceDebate.git into this folder and work ONLY from that repo's instructions. Start with 00-READ-THIS-FIRST/README.md, then AGENTS.md, then follow the routing table. Do not edit anything under tools/, core/, speeches/, playbooks/, or skills/. Put all of your work in my-prep/.

Scenario: I am on the Neg for the resolution "The United States federal government should enact a moratorium on hyperscale data center construction." The judges are lay (parents). I am speaking the first rebuttal and have 2:00 per contention. The opposing Aff case is reference/opponent-files/opponent-1AC-example.docx. My own existing files are in reference/example-blocks/ (a sample of my block library).

Do all of the following, using the repo's playbooks:

A. Setup. Create team.yaml (initials TC, cite style frontline, format policy, wpm 250, judge lay). Tell me the time budget for this rebuttal in words.

B. Context. Index and search my existing blocks (tools/library.py) and tell me which of my existing blocks already answer parts of their case, and which of their arguments I have no block for.

C. Map their case. Extract the text, list every contention with its chain (UQ / trend / link / IL / impact / solvency), every card and what it says in full, and the weakest step in each chain. Show the tag-story output for their case.

D. Find the holes. For at least five of their cards, run the hole checklist (core/refutation-guide.md) and report the specific hole you found, quoting their card's own text (verbatim) where you use it. Find at least one cross-position contradiction between their contentions, if one exists.

E. Research. For the gaps my existing blocks do not cover, research real evidence slot by slot (core/research-guide.md), save full text under sources/, keep a research log, and tell me about any slot where no evidence exists. Do not invent evidence.

F. Blocks. Build a blocks file with one block per argument you answer, in the repo's block anatomy: opposing argument stated fairly, numbered overview, tagged answers each with its own fully cut card (answer their SPECIFIC cards first), a plain analytic after each card (no labels or arrows), and a closing link or turn. Merge into my existing block headings instead of duplicating any block I already have.

G. Rebuttal. Write the first rebuttal: overview (use any contradiction you found), line by line in their order, answers ranked and consistent, closing weighing. Check it fits 2:00 per contention with the timer.

H. Cross-ex. Six questions about their strongest contention using the cross-ex protocol.

I. Checks. Build the .docx files, run every checker the repo provides (verify_quotes --strict, lint_cites, lint_cards, lint_blocks --lay, tag_story) and the unit tests, fix real problems, show me the output.

J. Final report. The "Before you read these" list; which repo instructions were unclear; and how I should open the .docx to see its formatting.
```

## Grading sheet

| Step | Pass looks like | Red flag |
|------|----------------|----------|
| Start | Reads READ-FIRST, AGENTS.md, integrity, then the right playbook (02) | Starts without reading the repo |
| Context (B) | Uses `library.py index/search`; names existing blocks that overlap | Re-researches what the library has |
| Map (C) | Every contention broken into chain steps with cards and weakest step | A summary of the tags only |
| Holes (D) | Specific holes tied to specific cards, quoting their text exactly | Generic "their evidence is weak" |
| Research (E) | Slot-by-slot, saved sources, honest about gaps | Invents sources; cuts from snippets |
| Blocks (F) | Anatomy followed; each answer has its own card; specific cards answered; merged into existing headings; lay analytics plain | Cardless answers; "Extend X" for unread cards; duplicate blocks; AI-style labels |
| Rebuttal (G) | Overview, line-by-line, ranked consistent answers, weighing; fits time | Unranked pile of answers; contradicts itself or earlier blocks |
| Cross-ex (H) | Closed, one idea, tied to their cards | Leading or vague |
| Checks (I) | Runs everything, shows output, fixes real failures | Claims checks passed without running them |
| Report (J) | Plain list of weaknesses and doc/tool problems | "Everything looks great" |
