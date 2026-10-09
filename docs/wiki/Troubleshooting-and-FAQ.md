# Troubleshooting and FAQ

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| "Claude isn't connected in this view" | The page was opened outside a Claude app | Open the workspace inside Claude |
| "Claude access was declined for this page" | Permission was refused | Reload the page and allow it |
| "Too many requests at once" | Rate limit reached | Wait a moment and try again |
| "Saved in this browser" instead of "Saved" | Online save failed | Keep working; it syncs on your next visit. Export from Publish if you're switching devices |
| A panel shows "This panel couldn't load" | An unexpected error | Select **Try again**; the error is recorded privately for diagnosis |
| A draft stops partway | Stopped or hit a limit | The partial text is kept; continue with an edit such as "Finish the remaining sections" |
| `[S3?]` appears in Read mode | The citation points at a source that's no longer attached | Re-attach the source or remove the marker |
| Download doesn't start | Downloads aren't available in this view | Use the copy dialog that appears |
| Tracked changes look like one big replacement | A full rewrite of a very long document | Expected; review the new text as a whole |
| `claude plugin validate` fails | Manifest or file structure problem | Read the message; fix the named file and field |

## FAQ

**Will this make my writing undetectable by AI detectors?**
No, and it doesn't try. It makes writing more original, specific and readable, and it says so honestly.

**Does the originality check guarantee no plagiarism?**
No. It compares your text with your sources and earlier drafts. For formal submissions, run a dedicated checker such as Turnitin, Copyleaks or Grammarly.

**Can it research the web?**
In chat, yes, when Claude has a web search tool. The visual workspace can't browse; ask Claude in chat to research and save the sources to your library.

**Where is my data stored?**
In your Claude account's private storage for the workspace, with a backup in your browser. See [Security and Privacy](Security-and-Privacy).

**Does it use my Claude usage?**
Yes. Writing features in the workspace use your own Claude usage, and the page shows an estimate per document.

**Can I use it in languages other than English?**
Claude can write in many languages, but the readability formulas and AI-pattern list are tuned for English.

**Can my team share a library?**
Not yet. See the [Roadmap](Roadmap).
