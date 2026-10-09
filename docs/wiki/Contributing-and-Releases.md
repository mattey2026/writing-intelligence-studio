# Contributing and Releases

## Contributing
1. Open an issue describing the problem or idea.
2. Fork the repository and create a branch.
3. Keep changes small and readable; don't minify or bundle code.
4. Run the checks:
   ```bash
   python3 tests/test_check_text.py
   claude plugin validate .
   ```
5. Describe in your pull request what changed and anything the plugin now runs, sends or fetches.

### House rules
- Every file under 256 KiB (images under 5 MiB); text, SVG, PNG, JPEG, GIF, WebP and fonts only.
- No package installs, hooks or credentials without a documented reason.
- Update `README.md` and `PRIVACY.md` whenever data handling changes.
- Keep the honesty rules: no invented facts, no detector-evasion features.

## Release process
1. Update `version` in `.claude-plugin/plugin.json` (semantic versioning: major.minor.patch).
2. Add an entry to `CHANGELOG.md`.
3. Update the version badge in `README.md`.
4. Validate: `claude plugin validate .`
5. Commit and push:
   ```bash
   git add .
   git commit -m "vX.Y.Z: summary"
   git push
   ```
6. The Claude directory picks up the new commit, scans it, and serves it once published from the developer portal at claude.ai/directory/manage.

## Version history
See [CHANGELOG.md](https://github.com/mattey2026/writing-intelligence-studio/blob/main/CHANGELOG.md).
