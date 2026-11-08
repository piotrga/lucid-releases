#!/usr/bin/env bash
set -euo pipefail

tag="v$(jq -r .version plugin/.claude-plugin/plugin.json)"
repo=${GITHUB_REPOSITORY:?}
commit=${GITHUB_SHA:?}
assets=(dist/lucid-language.zip dist/SHA256SUMS)
release() { gh release "$@" --repo "$repo"; }

# An existing tag belongs to one commit. Preserve published assets on retry.
tag_sha=$(git ls-remote "https://github.com/${repo}.git" "refs/tags/$tag" | cut -f1)
[[ -z "$tag_sha" || "$tag_sha" == "$commit" ]] || { echo "Version already used" >&2; exit 1; }
if ! release view "$tag" >/dev/null 2>&1; then
  summary="Lucid Language for Claude Code."
  if [[ -f "release-notes/$tag.md" ]]; then summary=$(<"release-notes/$tag.md"); fi
  release create "$tag" --target "$commit" --draft --title "Lucid Language $tag" \
    --notes "$summary

Install from the project directory, then start a fresh Claude Code session.

\`\`\`sh
claude plugin install lucid-language --marketplace $repo --scope project
\`\`\`"
fi
if [[ $(release view "$tag" --json isDraft --jq .isDraft) == true ]]; then
  target=$(release view "$tag" --json targetCommitish --jq .targetCommitish)
  [[ "$target" == "$commit" ]] || { echo "Draft targets another commit" >&2; exit 1; }
  release upload "$tag" "${assets[@]}" --clobber
  release edit "$tag" --draft=false
fi

url=$(release view "$tag" --json url --jq .url)
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
curl --fail --silent --show-error --location --retry 4 --retry-all-errors "$url" -o /dev/null
for file in "${assets[@]}"; do
  name=${file##*/}
  curl --fail --silent --show-error --location --retry 4 --retry-all-errors \
    "https://github.com/$repo/releases/download/$tag/$name" -o "$tmp/$name"
  cmp "$file" "$tmp/$name"
done
(cd "$tmp" && sha256sum --check SHA256SUMS)
echo "[$tag]($url)" >> "${GITHUB_STEP_SUMMARY:?}"
