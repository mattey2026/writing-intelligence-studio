# Roadmap

What Writing Intelligence Studio doesn't do yet, and how it could. Effort is a rough guide: **S** (days), **M** (weeks), **L** (months).

## Now: quality and reliability (next release)

| Item | Why | Effort |
|---|---|---|
| Automated before-and-after quality tests using Claude Code's built-in plugin testing | Prove the plugin improves output against plain Claude, and catch regressions | S |
| Duplicate-section detection | Warn when edits create repeated headings | S |
| Accessibility audit (keyboard paths, screen-reader labels, contrast) | Meet WCAG 2.2 AA throughout the workspace | S |
| Error-log viewer in Settings | Let users see and clear their own recorded errors | S |
| Readability support for more languages | Language-specific formulas and pattern lists | M |

## Next: research and publishing

| Item | Why | Effort |
|---|---|---|
| **Live web research inside the workspace** through an MCP research connector | Find and cite current sources without leaving the studio | M |
| **Citation import** from DOI, URL, Zotero and BibTeX | Add sources with complete metadata in one step | M |
| **Word (.docx) and PDF export** | Formal submissions and sharing | M |
| **Google Docs and Notion export** | Move drafts into team tools | M |
| **Raster image generation** through an image connector | Photographic and painted featured images | M |
| **Plagiarism-check integration** (Copyleaks or similar API, user's own key) | Check against the wider web before submission | M |
| **Live keyword volumes** through an SEO data connector | Choose keywords with real search data | M |
| **Direct publishing and scheduling** to LinkedIn, Medium, WordPress and newsletters | Publish at the recommended time without copy and paste | L |

## Later: intelligence and teams

| Item | Why | Effort |
|---|---|---|
| **Semantic search with embeddings** | Faster, more accurate "find what I wrote about..." over large libraries | M |
| **Knowledge graph** linking documents, concepts and sources | See topic coverage and reuse research | L |
| **Performance feedback loop** from post analytics | Learn which topics, formats and times work for you | L |
| **Team workspaces** with roles and shared libraries | Collaborate with editors and colleagues | L |
| **Shared style guides and voice libraries** | Consistent brand voice across a team | M |
| **Comments and approval workflows** | Editorial sign-off before publishing | L |
| **Exact token metering** | Replace estimates with precise counts when the platform exposes them | S, once available |
| **Book mode** | Chapters, cross-chapter consistency checks and a manuscript view for long projects | L |
| **Dictation and audio** | Draft by speaking; turn articles into podcast scripts | M |
| **Enterprise controls**: SSO, audit logs, retention policies, admin export | Adoption inside organizations | L |

## Ideas we're deliberately not pursuing
- **Detector evasion.** Quality and honesty matter more than gaming classifiers.
- **Fully automatic publishing without review.** The author always approves what goes out.

Have a suggestion? Open an issue on the repository.
