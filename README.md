# Lucid Language for Claude Code

Capture agreed behaviour in a project's `.lucid` specifications. New sessions
read the project's rules and open decisions before changing behaviour.

## Install from GitHub

From the project directory, run:

```sh
claude plugin install lucid-language --marketplace piotrga/lucid-releases --scope project
```

Start Claude Code there, or run `/reload-plugins` in an open session.
In Claude Code itself, use `/plugin install lucid-language --marketplace piotrga/lucid-releases`
and choose project scope. The single shell command requires Claude Code 2.1.292+.

Try “Two people must never buy the last ticket. Write the agreed rule and tell
me which product decisions remain open.”

If you previously unpacked v0.1.0, remove its three installed files after
checking for local edits: `.claude/rules/lucid-language.md` and the two Markdown
files under `.claude/skills/lucid-language/`. Keep your project specifications.

## Release

Review the public diff for personal details, private URLs, paths and credentials.
Set the next version in `plugin/.claude-plugin/plugin.json`. Run
`python3 tools/build.py` and commit the manifest and plugin changes together
on `main`. GitHub Actions checks installation from the published repository,
publishes the versioned plugin ZIP and verifies its anonymous download.
