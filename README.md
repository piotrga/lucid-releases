# Lucid Language

Record agreed system behaviour, its rationale and unresolved choices in a project's
`.lucid` files. A Claude Code project rule loads the language skill when working
on requirements or implementing a change.

## Use in a project

Download `lucid-language.zip` from the GitHub release. From the project root,
run `unzip -n /path/to/lucid-language.zip` and start a fresh Claude Code
session. Commit the three files under `.claude/` to share them with the team.
For upgrades, compare and replace those three files together.

Try “Two people must never buy the last ticket. Write the rule and tell me
which product decisions remain open.”

## Cut the next release

Review the complete diff before pushing to this public repository, including
identifiers, real examples, URLs, local paths and credentials. For changes
developed elsewhere, copy only reviewed changes to the three module files.
Run `python3 tools/build.py`. For an ordinary update, increment the patch
component in `VERSION`. Commit the version and its changes together on
`main`. GitHub Actions builds that commit, publishes the versioned release
and downloads the ZIP anonymously to check its digest. The successful run
summary contains the release link. Rerun a failed job at the same commit.
