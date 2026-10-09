# Installation

There are four ways to use Writing Intelligence Studio. Pick the one that matches where you work.

## Requirements

| Use | You need |
|---|---|
| Skills in Claude apps | A Claude account with plugins from the directory available |
| Skills in Claude Code | Claude Code installed |
| Visual workspace | A Claude app that supports interactive artifacts (for example claude.ai on the web or desktop) |
| Quality-check script on your own machine | Python 3.8 or later. No packages to install |
| Submitting or updating the directory listing | A paid Claude plan (Pro, Max, Team or Enterprise) |

## Option 1: Install from the Claude directory (recommended)

Once the listing is approved and published:

1. In Claude, open **Customize** and browse the **directory**.
2. Search for **Writing Intelligence Studio**.
3. Select it and choose **Add** (or **Install**).
4. Start a new chat and ask, for example: *"Write a 900-word essay for CFOs on AI token costs."*

Claude loads the right skill automatically when your request matches.

## Option 2: Try it locally in Claude Code

1. Download or clone the repository:
   ```bash
   git clone https://github.com/mattey2026/writing-intelligence-studio.git
   ```
2. Start Claude Code with the plugin loaded for this session:
   ```bash
   claude --plugin-dir ./writing-intelligence-studio
   ```
3. Ask Claude: *"Which skills do you have from Writing Intelligence Studio?"* It should list the three skills.

To check the plugin's structure before using it:
```bash
claude plugin validate ./writing-intelligence-studio
```
A healthy plugin prints `✔ Validation passed`.

## Option 3: Open the visual workspace

In a Claude app with interactive artifacts, with the plugin installed, ask:

> Open the writing studio.

Claude publishes the workspace as a private page in your account. The first time you use a writing feature, the page asks permission to use your Claude usage. Your documents are stored privately and other people can't see them.

You can also open `skills/studio-workspace/assets/studio.html` directly in a browser. Without Claude, its writing features are switched off and documents are kept only in that browser.

## Option 4: Run the quality check on your own machine

```bash
python3 skills/text-quality-check/scripts/check_text.py draft.md --level General --sources notes.txt
```

| Option | Meaning |
|---|---|
| `draft.md` | Your draft (Markdown or plain text) |
| `--level` | `Plain`, `General` (default), `Professional` or `Specialist` |
| `--sources` | One or more source or earlier-draft files to check for copied wording |
| `--json` | Output machine-readable JSON instead of a report |

Run the automated tests:
```bash
python3 tests/test_check_text.py
```

## Updating

- **Directory install:** updates arrive automatically after each new version is published.
- **Claude Code:** pull the latest code with `git pull`, then restart Claude Code with `--plugin-dir`.
- **Visual workspace:** reload the page; your library is kept.

## Uninstalling

Remove the plugin from **Customize** in Claude. Your workspace library stays in your account until you delete it from the workspace's **Settings → Delete everything**.
