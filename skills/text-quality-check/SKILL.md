---
name: text-quality-check
description: Measures a draft's readability and style with a deterministic script, with no model judgement involved. Reports reading ease and grade level against a target, average sentence length, long sentences, passive voice, AI-style phrases, repetitive sentence openings, dash density and over-long paragraphs, and checks for wording copied from source files. Use when someone asks how readable a draft is, wants AI-style phrasing found, wants to check for copied wording before submitting, or when the writing-studio review step runs.
---

# Text quality check

Run `scripts/check_text.py` on the draft. It uses only the Python standard library and reads local files; it sends nothing anywhere.

## Steps
1. Save the draft as a Markdown or text file, for example `draft.md`. Save each source's notes or excerpts, and any earlier piece the draft built on, as separate text files.
2. Run:
   ```
   python3 scripts/check_text.py draft.md --level General --sources source1.txt source2.txt
   ```
   `--level` is Plain, General (default), Professional or Specialist. Add `--json` for machine-readable output.
3. Read the report and present it plainly: what is on target, what isn't, and the specific sentences or phrases to fix.
4. Offer fixes: rewrite flagged AI-style phrases naturally (not by swapping synonyms), split sentences over 30 words, vary repeated openings, and rewrite any copied passage in original words while keeping its citation.
5. After the author accepts edits, run the check again to confirm the improvement.

## What the numbers mean
- **Reading ease (Flesch):** higher is easier. Targets: Plain 65+, General 55+, Professional 45+, Specialist 30+.
- **Grade level (Flesch-Kincaid):** approximate school grade needed to read comfortably.
- **Copied wording:** any run of 8 or more identical words (outside quotation marks) shared with a source file.

## Limits to state honestly
- The originality check compares only against the files provided. It does not search the internet. For formal submissions, recommend a dedicated plagiarism checker such as Turnitin, Copyleaks or Grammarly.
- Syllable counts and passive-voice detection are heuristics; treat scores as guidance.
- The AI-style phrase list flags formulaic writing. It says nothing about who wrote the text and is not an AI-detector score.
