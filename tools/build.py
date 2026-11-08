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
    "hooks/register.ts",
    "project.md",
    "skills/lucid-language/SKILL.md",
    "skills/lucid-language/assets/CLAUDE.lucid.md",
    "skills/lucid-language/diagnostics.md",
    "skills/lucid-language/examples.md",
    "skills/lucid-language/generalization.md",
    "skills/lucid-language/language.md",
    "skills/lucid-language/lowering.md",
    "skills/lucid-language/modularity.md",
    "skills/lucid-language/projections.md",
    "skills/lucid-language/spec-tests.md",
    "skills/lucid-language/tightening-coherence.md",
    "skills/lucid-language/tightening-noise.md",
    "skills/lucid-language/tightening-structural.md",
    "skills/lucid-language/tightening.md",
    "skills/lucid-language/workflow.md",
    "skills/lucid-language/writing.md",
)
PUBLIC_REFERENCES = (
    "https://alistair.cockburn.us/hexagonal-architecture",
    "https://alistairmavin.com/ears/",
    "https://c4model.com/abstractions",
    "https://cucumber.io/docs/gherkin/reference/",
    "https://www.asd-ste100.org/STE_faq.html",
    "https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions",
    "https://www.domainlanguage.com/ddd/reference/",
    "https://www.eiffel.com/values/design-by-contract/introduction/",
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
    text = data.decode("utf-8")
    # Permit only reviewed, exact documentation links.
    for url in PUBLIC_REFERENCES:
        text = text.replace(f"]({url})", "]()")
    if PRIVATE.search(text):
        raise ValueError(f"Review possible sensitive content in {path.name}")
    return data


def build() -> None:
    plugin = ROOT / "plugin"
    version = json.loads((plugin / ".claude-plugin/plugin.json").read_bytes())["version"]
    if not re.fullmatch(r"(?:0|[1-9][0-9]*)(?:\.(?:0|[1-9][0-9]*)){2}", version):
        raise ValueError("Plugin version must contain a numeric major.minor.patch version")
    shipped = {p.relative_to(plugin).as_posix() for p in plugin.rglob("*") if p.is_file() or p.is_symlink()}
    if shipped != set(FILES):
        raise ValueError("Plugin install and ZIP must contain the same reviewed files")
    sources = {name: validate(plugin / name) for name in FILES}
    for name, data in sources.items():
        if name.endswith(".md"):
            for link in re.findall(r"\]\(([^)]+)\)", data.decode()):
                if link not in PUBLIC_REFERENCES and not ((plugin / name).parent / link).resolve().is_relative_to(plugin):
                    raise ValueError(f"{name} links outside the plugin")
                if link not in PUBLIC_REFERENCES and not ((plugin / name).parent / link).is_file():
                    raise ValueError(f"{name} links to a missing file: {link}")
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
