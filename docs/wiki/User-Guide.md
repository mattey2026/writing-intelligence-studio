# User Guide

This guide covers both ways of working: **in chat** with the skills, and in the **visual workspace**.

## Working in chat

Just describe what you want. Claude picks the right skill.

| You say | What happens |
|---|---|
| "Write a LinkedIn post about agentic AI in sales." | Claude infers the brief, may ask one quick question, then drafts |
| "Here's my draft. Challenge it." | Weaknesses, counterarguments and missing context, each with a suggested fix |
| "Make this easier to read." | A clearer version with shorter sentences, active voice and plain words |
| "Check readability and find AI-style phrasing." | Claude runs the quality-check script and explains the results |
| "Add citations for every factual claim." | Claims are linked to sources; anything unsupported is flagged `[needs source]` |
| "Turn this into a newsletter with hashtags and the best time to post for US readers." | A repurposed version, hashtags and posting windows in US and your local time |
| "Learn my voice from these three posts." | A voice profile describing how you write |

## Working in the visual workspace

### Layout

| Area | What it holds |
|---|---|
| **Top bar** | Home, Write, Library, Voice profiles, Research library, Settings; shows where your library is saved |
| **Left panel** | The nine workflow steps and your document's outline (click a heading to jump to it) |
| **Centre** | The writing canvas. **Write** mode edits Markdown; **Read** mode shows the formatted article with citations and references. Undo and Redo, word count, reading time, token estimate and save status sit above it |
| **Right panel** | The tool for the selected step |

On phones and narrow windows, the three areas become tabs at the bottom: **Steps**, **Write** and the current tool.

### Home

Type your idea in plain words, optionally pick a format chip (Blog post, Essay, Article and so on), and select **Start writing**. Press **Ctrl+Enter** to start quickly. Home also shows documents to continue, documents awaiting review, and **Suggest topics I haven't covered**.

### Step 1: Brief

1. Check or edit **Your idea**, then select **Analyze my idea**.
2. Claude fills in the format, purpose, audience, tone, length, perspective, destination, research mode and personas, and explains the approach.
3. Answer any questions that appear (at most three) by tapping an option or choosing **Other...**.
4. Adjust any field:

| Field | Options |
|---|---|
| **Depth** | Standard; Deep (default): mechanism, example, implication and objection for each point; Expert |
| **Reading level** | Plain (grade 7 to 8), General (default, 9 to 10), Professional (11 to 12), Specialist (13+) |
| **Research** | Use only sources I add (cited); Claude's knowledge with flagged claims; Creative, no references |
| **Editorial approach** | Any mix of the seven personas |
| **Voice profile** | One of your saved voices, or none |

**You've written about this before** lists related documents from your library. **Build on it** adds one as material for the new piece.

### Step 2: Outline

Select **Generate outline** for a thesis, a distinctive angle, sections with specific points, claims that need evidence, and keywords. Edit any of it freely; the draft follows your edited plan.

### Step 3: Draft

Select **Write full draft**. The text streams into the canvas, and **Stop** keeps whatever has been written so far. If you already had text, it's saved as a version first. Deep and Expert drafts use Claude's most thorough mode, so they take longer.

### Step 4: Challenge

Select **Challenge this draft** for:
- a verdict on the biggest strength and weakness;
- issues rated high, medium or low, each with **Fix this**;
- counterarguments, with **Work these into the draft**;
- missing context, with **Add this** or **Add all missing context**.

### Step 5: Edit

1. Optionally select text in the canvas to edit only that passage.
2. Type an instruction, or tap a common edit: Go deeper, Make it easier to read, Make the argument stronger, Remove generic AI-style phrasing, Shorten by 30%, Publication-ready polish and more.
3. Review the tracked changes (green added, red removed) and choose **Accept changes** or **Discard**.

Every accepted change saves a version first.

### Step 6: Verify

- Choose a **citation style**: APA, MLA, Chicago, Harvard, IEEE or inline links.
- Attach saved sources or **Add new source**. Paste the passages you rely on into its notes, because Claude can only cite what's there.
- For a video source, **Insert video in text** places it in the article; it shows as a video card in Read mode and plays inside exported HTML.
- **Find real examples and sources** suggests documented cases, publications and videos, each with a link to confirm it.
- **Check every claim** lists each factual claim as supported, contradicted, needs source or opinion.

### Step 7: Illustrate

Choose an aspect ratio and style, select **Suggest 3 concepts**, then **Create this image**. You get an original vector illustration, alt text, a caption and a prompt for photo or painting generators. **Download SVG**, **Redraw** or **Remove** it any time.

### Step 8: Review

- **Readability and style** (instant, no Claude usage): reading ease, grade level, sentence length, long sentences, passive voice, dashes, long paragraphs, AI-style phrases and repetitive openings, with one-click fixes.
- **Originality check**: flags any 8-word run copied from your sources or earlier pieces, with **Rewrite in original words**.
- **Authenticity review**: an editor's 1-to-10 scores on ten dimensions, a summary, generic phrases found, and the highest-value edits with **Apply with review**.

### Step 9: Publish

- Set **Status** (Draft, In review, Final, Published), **Project** and **Tags**; **Summarize and tag** helps library search.
- **Find keywords and LinkedIn tags**: primary keyword, related phrases, reader questions, search title, meta description, missing keywords, 5 to 8 hashtags.
- **Best time to publish**: choose where your readers are; see days and windows per platform in their time and yours.
- **Export**: Markdown, HTML web page, plain text, or copy Markdown.
- **Repurpose**: LinkedIn post, newsletter, executive summary or thread, each as a new document.
- **Version history**: save a named version, compare any version with the current text, or restore it.
- **Claude usage**: estimated tokens for this document.

### Library

Search titles, text and tags instantly, filter by format, status and project, or **Ask your library** in plain language ("everything I've written about AI agents"). Tick two or more documents and select **Combine into a long-form report**. Each document can be duplicated or deleted.

### Voice profiles

Name a profile, paste 120 or more words of your own writing, and select **Analyze my voice**. Save the result, then choose it in any document's brief.

### Research library

Your saved sources, searchable, with where each is used. Tick **I have opened this source and confirmed the details** only after checking it yourself; unverified sources are marked in reference lists.

### Settings

Theme (match device, light, dark), default research mode and citation style, thinking depth (Quick, Balanced, Deep), export your whole library as JSON, and delete everything.

## Tips for the best results

- Give the purpose, not just the topic: *"so that CFOs approve a token budget"*.
- Add sources before drafting if the piece makes factual claims.
- Use **Go deeper** on thin sections rather than regenerating the whole draft.
- Run the Review step after every major edit.
- Replace every `[Add your own example: ...]` with a real story of your own before publishing.
