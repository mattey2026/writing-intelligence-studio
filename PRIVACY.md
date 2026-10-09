# Privacy

Writing Intelligence Studio collects no personal data and runs no servers of its own.

## Skills
The skills are instructions that guide Claude. Your conversation is handled by Claude under your existing Anthropic account terms.

## Quality-check script
`skills/text-quality-check/scripts/check_text.py` reads only the files you give it, runs locally, and sends nothing over the network.

## Visual workspace
When you open the workspace inside a Claude app:
- **Writing requests** go to Claude through the app's own runtime and use your Claude usage. The page asks your permission the first time.
- **Your library** (documents, versions, voice profiles, sources) is stored in the app's private per-user storage, which other people who open the page cannot read. A backup copy is kept in your browser's local storage.
- **Fonts** are loaded from Google Fonts (fonts.googleapis.com and fonts.gstatic.com).
- **Search links** to Google and YouTube open only when you click them.
- There are no analytics, cookies set by the plugin, tracking pixels or third-party scripts.

## Your control
From the workspace's Settings you can export your entire library as JSON or delete everything. Deleting a document also deletes its saved versions.

## Contact
Sumit Mattey, sumit@matteys.com
