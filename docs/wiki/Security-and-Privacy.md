# Security and Privacy

## Summary
- No servers of its own, no analytics, no tracking, no credentials.
- Your workspace library is private to your account.
- Every action that changes your text needs your approval.

## What leaves your device

| Data | Goes to | When |
|---|---|---|
| Your brief, text and sources | Claude, through the host app's runtime | Only when you use a writing feature |
| Documents, versions, voices, sources | The host app's private per-user storage | On save |
| Error details (no document text) | The same private storage | When something fails |
| Font requests | Google Fonts | When the workspace loads |
| Search queries | Google or YouTube | Only when you click a search link |

The quality-check script sends nothing anywhere.

## Access control
- Storage paths are scoped to your user ID; other people who open the workspace page can't read your library, and neither can the page's publisher.
- The workspace declares only four runtime capabilities: `sample`, `db`, `user`, `downloads`.
- Claude usage is the viewer's own and requires the viewer's permission the first time.

## Content safety
- User text, sources and earlier documents are always treated as data, never as instructions.
- Rendered Markdown is escaped before formatting; only `http` and `https` links are allowed.
- Generated SVG is checked to start with `<svg>`, and scripts, event handlers and embedded foreign content are removed before display. SVG is shown through an image element, which can't run code.

## Editorial integrity
- No invented references, statistics, quotations, URLs or personal stories.
- Unsupported claims are flagged; unverified sources are labelled.
- No promises about AI detectors or plagiarism checkers; requests to evade detection are redirected to genuine quality improvements.

## Your control
- **Settings → Export my library** downloads everything as JSON.
- **Settings → Delete everything** removes all documents, versions, voices and sources.
- Deleting a document also deletes its versions.

## Reporting a security issue
Email sumit@matteys.com with details. Please don't open a public issue for security problems.
