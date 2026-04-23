"""Path files cross-link into topic files via anchors of the form
`topics/04-prompt-injection.md#start-here`. Every such anchor must
resolve to an H2 that actually exists in the referenced topic file.
"""

from __future__ import annotations

import re

from tests.conftest import parse_markdown

ANCHOR_RE = re.compile(
    r"\(([^)]+?\.md)(?:#([^)]+))?\)",
)


def _github_anchor(h2_text: str) -> str:
    """Reproduce GitHub's auto-generated anchor for an H2 heading."""
    s = h2_text.strip().lower()
    s = re.sub(r"\s*\{#[^}]*\}\s*$", "", s)
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    return s


def test_path_anchors_resolve_to_topic_h2s(path_docs):
    for doc in path_docs:
        for match in ANCHOR_RE.finditer(doc.body):
            rel_path, anchor = match.group(1), match.group(2)
            target = (doc.path.parent / rel_path).resolve()
            if not str(target).endswith(".md"):
                continue
            try:
                target.relative_to((doc.path.parent / "..").resolve() / "topics")
            except ValueError:
                continue
            if not target.exists():
                raise AssertionError(
                    f"{doc.path.name}: link target does not exist: {rel_path} "
                    f"(resolved to {target})"
                )
            if anchor is None:
                continue
            topic = parse_markdown(target)
            valid_anchors = {_github_anchor(h) for h in topic.h2_headings}
            assert anchor.lower() in valid_anchors, (
                f"{doc.path.name}: anchor #{anchor} does not match any H2 in "
                f"{target.name}. Valid anchors: {sorted(valid_anchors)}"
            )
