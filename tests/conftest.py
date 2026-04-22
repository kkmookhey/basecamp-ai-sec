"""Shared fixtures and helpers for Basecamp structural tests."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
TOPICS_DIR = REPO_ROOT / "topics"
PATHS_DIR = REPO_ROOT / "paths"
README = REPO_ROOT / "README.md"


@dataclass
class MarkdownDoc:
    """Parsed representation of a markdown file with YAML frontmatter."""

    path: Path
    frontmatter: dict
    body: str

    @property
    def h2_headings(self) -> list[str]:
        """Return every H2 heading text (without the ## prefix), in order."""
        return [
            m.group(1).strip()
            for m in re.finditer(r"^##\s+(.+?)\s*$", self.body, flags=re.MULTILINE)
            if not m.group(1).startswith("#")
        ]

    def section_body(self, h2_title: str) -> str | None:
        """Return the body text under the given H2, up to the next H2 or EOF."""
        pattern = re.compile(
            rf"^##\s+{re.escape(h2_title)}\s*\n(.*?)(?=^##\s|\Z)",
            re.MULTILINE | re.DOTALL,
        )
        m = pattern.search(self.body)
        return m.group(1) if m else None

    def links_under(self, h2_title: str) -> list[tuple[str, str]]:
        """Return (text, url) for each markdown link in the named section."""
        section = self.section_body(h2_title)
        if section is None:
            return []
        return re.findall(r"\[([^\]]+)\]\(([^)]+)\)", section)


def parse_markdown(path: Path) -> MarkdownDoc:
    """Parse a markdown file with YAML frontmatter."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)", text, flags=re.DOTALL)
    if not m:
        return MarkdownDoc(path=path, frontmatter={}, body=text)
    fm = yaml.safe_load(m.group(1)) or {}
    return MarkdownDoc(path=path, frontmatter=fm, body=m.group(2))


@pytest.fixture
def topic_docs() -> list[MarkdownDoc]:
    """Every markdown file under topics/, excluding .gitkeep."""
    return sorted(
        (parse_markdown(p) for p in TOPICS_DIR.glob("*.md")),
        key=lambda d: d.path.name,
    )


@pytest.fixture
def path_docs() -> list[MarkdownDoc]:
    """Every markdown file under paths/."""
    return sorted(
        (parse_markdown(p) for p in PATHS_DIR.glob("*.md")),
        key=lambda d: d.path.name,
    )


@pytest.fixture
def readme_text() -> str:
    return README.read_text(encoding="utf-8")
