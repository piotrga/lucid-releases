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

## Work on specifications

| Project task | What the plugin helps you do |
| --- | --- |
| Capture a requirement | Turn examples into definitions, conditions, exceptions and rationale. Record open product choices separately. |
| Review a change | Check contradictions, missing outcomes, duplicated rules and unsafe generalisations. Follow the impact across files. |
| Derive an artefact | Generate traceable test expectations, diagrams, architecture or API views and implementation mappings. |
| Explain a discrepancy | Compare the agreed intent, written spec, implementation and observed behaviour. |
| Resume or delegate work | Hooks supply the project contract and list conventional spec files on new requests, after compaction and to ordinary workers. |

Read the [skill guide](plugin/skills/lucid-language/SKILL.md) for the full
reference index. The [evaluation cases](checks/spec-cases.md) describe expected
behaviour. They are examples for evaluating a model on project tasks.

The hooks supply context to Claude. The project retains its own test commands
and implementation workflow. The plugin writes no session intent record and
introduces no approval gate.

## Release

Review the public diff for personal details, private URLs, paths and credentials.
When preparing a release from the full Lucid project, run its spec export check against this checkout. Review the resulting diff and run the check again after applying it.
Set the next version in `plugin/.claude-plugin/plugin.json`. Run
`python3 tools/build.py` and commit the manifest and plugin changes together
on `main`. GitHub Actions checks installation from the published repository,
publishes the versioned plugin ZIP and verifies its anonymous download.
