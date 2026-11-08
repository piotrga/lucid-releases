"""Validate and package the installable plugin."""

from hashlib import sha256
import json
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    ".claude-plugin/plugin.json",
    "hooks/hooks.json",
    "project.md",
    "skills/lucid-language/SKILL.md",
    "skills/lucid-language/language.md",
)
PRIVATE = re.compile(
    r"(?i)(?:[\w.+-]+@[\w.-]+\.[a-z]{2,}|https?://|/Users/|/home/|"
    r"github_pat_|gh[pousr]_[\w]{20,}|sk-[\w-]{20,}|AKIA[A-Z0-9]{16}|"
    r"-----BEGIN [\w ]*PRIVATE KEY-----)"
)


def validate(path: Path) -> bytes:
    if path.resolve() != path:
        raise ValueError(f"Linked source path: {path.name}")
    data = path.read_bytes()
    if PRIVATE.search(data.decode("utf-8")):
        raise ValueError(f"Review possible sensitive content in {path.name}")
    return data


def build() -> None:
    plugin = ROOT / "plugin"
    version = json.loads((plugin / ".claude-plugin/plugin.json").read_bytes())["version"]
    if not re.fullmatch(r"(?:0|[1-9][0-9]*)(?:\.(?:0|[1-9][0-9]*)){2}", version):
        raise ValueError("Plugin version must contain a numeric major.minor.patch version")
    sources = {name: validate(plugin / name) for name in FILES}
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    output = dist / "lucid-language.zip"
    with ZipFile(output, "w") as archive:
        for name, data in sources.items():
            entry = ZipInfo(name)
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, data, compress_type=ZIP_DEFLATED)
    digest = sha256(output.read_bytes()).hexdigest()
    (dist / "SHA256SUMS").write_text(f"{digest}  {output.name}\n")


if __name__ == "__main__":
    build()
