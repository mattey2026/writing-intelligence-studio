---
name: studio-workspace
description: Opens the Writing Intelligence Studio, an interactive writing workspace with a nine-step workflow (brief, outline, draft, challenge, edit, verify, illustrate, review, publish), tracked edits, source management, readability and originality checks, a private document library and version history. Use when someone asks to open the writing studio or workspace, wants a visual editor for long-form writing, or wants to manage drafts, sources and versions in one place.
---

# Studio workspace

The workspace is a single self-contained web page at `assets/studio.html`. It runs inside Claude apps that can publish interactive artifacts, and uses that environment's runtime to ask Claude for writing help, store the user's documents privately and offer downloads.

## Open it
1. Check whether this conversation has a tool that publishes interactive web pages (on claude.ai, the **Artifact** tool).
2. If it does:
   - Copy `assets/studio.html` unchanged to the outputs folder (for example `/mnt/user-data/outputs/writing-studio.html`).
   - Ask the tool which runtime capabilities are available, then publish the file declaring `sample` (asking Claude), `db` and `user` (the private library), and `downloads` (exports). Use the favicon "✍️" and the title "Writing Intelligence Studio".
   - Tell the user the first writing action asks permission to use their Claude usage, and that their library is private to their account.
3. If it doesn't, explain that the visual workspace needs a Claude app with interactive artifacts, and continue with the **writing-studio** skill in chat instead. The page can also be opened in any browser, but without Claude its writing features are switched off and documents are kept only in that browser.

## Do not
- Edit or minify the file before publishing; reviewers and users should see the same readable source.
- Add capabilities beyond the four listed above.

## What the page does with data
- Sends prompts built from the user's own brief, text and sources to Claude through the host app's runtime, using the user's own Claude usage.
- Stores documents, versions, voice profiles and sources in the host app's per-user private storage, with a backup copy in the browser's local storage.
- Loads two fonts from Google Fonts.
- Opens Google and YouTube search links only when the user clicks them.
- Sends nothing to any other server, has no analytics and no tracking.
