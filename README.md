# Writing Intelligence Studio

*Think deeper. Write better. Publish with confidence.*

Writing Intelligence Studio turns Claude into a small editorial team: an intake editor, researcher, author, sceptical senior editor, copy editor and fact-checker. It plans, drafts, challenges, edits, verifies and reviews substantial writing (essays, articles, blog posts, reports, white papers, technical guides, newsletters, LinkedIn posts and book chapters) while keeping you in control of every change.

## What it does

- **Purpose before prose.** Infers format, audience, tone, depth, reading level and length from a plain request, and asks only the questions that would change the result.
- **Editorial personas.** Journalist, Philosopher, Technical expert, Researcher, Literary writer, Executive thought leader and Human editor. Combine them; each changes reasoning and evidence standards, not just wording.
- **Evidence you can check.** Cites only real sources, marks unsupported claims `[needs source]`, and never invents references, statistics, quotations or personal anecdotes.
- **Readable, original writing.** Targets a reading level, avoids around 30 formulaic AI-style patterns, and paraphrases sources fully.
- **Deterministic quality check.** A standard-library Python script measures reading ease, grade level, sentence length, passive voice, AI-style phrases, repetitive openings and copied wording against your source files.
- **Ready to publish.** Search title, meta description, keywords, LinkedIn hashtags, suggested posting times by region, and repurposed versions.
- **Optional visual workspace.** A full editor with tracked changes, a source library, readability and originality panels, a private document library and version history, where your Claude app supports interactive artifacts.

## Skills included

| Skill | Use it when |
|---|---|
| `writing-studio` | You ask Claude to write, improve, fact-check or prepare any substantial piece for publication |
| `text-quality-check` | You want readability scores, AI-style phrases found, or copied wording checked against your sources |
| `studio-workspace` | You want the interactive editor and document library |

## Example requests

- "Write a 1,200-word essay for CIOs on why enterprise AI pilots stall. Deep, professional reading level."
- "Challenge my draft and add the missing context."
- "Check this article's readability and find any AI-style phrasing."
- "Turn this report into a LinkedIn post with hashtags and the best time to post for readers in India."
- "Open the writing studio."

## Installation

Install from the Claude directory once listed. To try it locally in Claude Code:

```
claude --plugin-dir ./writing-intelligence-studio
```

## What this plugin runs, sends and fetches

- **Skills** are instructions to Claude. They run no code on their own.
- **`text-quality-check`** includes `scripts/check_text.py`, which Claude runs only when you ask for a quality check. It uses the Python standard library, reads the files you give it, prints a report and sends nothing over the network.
- **`studio-workspace`** includes `assets/studio.html`, a readable single-page app. When published inside a Claude app, it sends your brief, text and sources to Claude through that app's runtime (using your own Claude usage), stores your documents in the app's private per-user storage with a backup in your browser, loads two fonts from Google Fonts, and opens Google or YouTube search links only when you click them. It has no analytics, tracking or other network calls.
- No hooks, no MCP servers, no package installs, no credentials.

## Honest limits

- Research is only as current as the tools available. Without a web search tool, Claude asks you for sources instead of guessing.
- The originality check compares against the sources and earlier drafts you provide, not the whole internet. Run a dedicated plagiarism checker before formal submission.
- The editorial review measures quality, specificity and voice. It is not an AI-detection score and makes no promise about detectors.
- Posting-time advice is general guidance; your own platform analytics are a better guide once you have them.

## Privacy

See [PRIVACY.md](PRIVACY.md). Your documents belong to you and are never shared with other users.

## License

MIT. See [LICENSE](LICENSE).

## Author

Sumit Mattey · [github.com/mattey2026](https://github.com/mattey2026) · sumit@matteys.com
