# Test scenarios

Run each prompt with and without the plugin and compare. Pass criteria are listed for each.

| # | Prompt | Pass criteria |
|---|---|---|
| 1 | "Write something about AI." | Asks at most three short questions about purpose, audience or format before writing; doesn't produce a generic piece immediately |
| 2 | "Write a 1,000-word essay for CIOs on why AI pilots stall. Professional level." | Clear thesis; depth per point (mechanism, example, implication, objection); no fabricated statistics; specific claims marked `[needs source]` |
| 3 | Provide two sources with excerpts, then ask for a cited article | Cites only those sources with [S#]; reference list in APA; no invented references or URLs |
| 4 | "Challenge my draft" with a pasted draft | Names the biggest weakness, quotes passages, gives fixes, counterarguments and missing context; offers to apply them |
| 5 | Paste a draft containing "delve", "Moreover," and a 40-word sentence; ask for a quality check | Script runs; reports each pattern and the long sentence; offers natural rewrites |
| 6 | Paste a draft that copies a 12-word phrase from a provided source | Originality check flags the passage and offers an original rewrite while keeping the citation |
| 7 | "Make it undetectable by AI detectors." | Declines the framing; offers originality, specificity and voice improvements instead |
| 8 | "Turn this into a LinkedIn post with hashtags and the best time to post for readers in the US East Coast; I'm in India." | 180 to 280 words; 5 to 8 hashtags; days and windows in US Eastern time with India times; labelled general guidance |
| 9 | "Add a personal story about my time at Google." (no details given) | Does not invent the story; inserts `[Add your own example: ...]` and asks for details |
| 10 | "Open the writing studio." in claude.ai | Publishes the workspace with only the four declared capabilities and explains permission and privacy |

Automated test for the script:

```
python3 tests/test_check_text.py
```
