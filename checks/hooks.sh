#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
cp -R plugin "$work/plugin"
mkdir -p "$work/plugin/tests"
cp checks/context.test.ts "$work/plugin/tests/"
"${1:-claude}" plugin test "$work/plugin"
