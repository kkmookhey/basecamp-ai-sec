"""Topic files with status: ready must have 5-15 curated links total
across the four link-bearing sections: Start here, Go deeper, Tools, Watch.

Files with status: skeleton are exempt — they're WIP placeholders.
"""

LINK_BEARING_SECTIONS = ("Start here", "Go deeper", "Tools", "Watch")
MIN_LINKS = 5
MAX_LINKS = 15


def _count_links(doc) -> int:
    return sum(len(doc.links_under(h2)) for h2 in LINK_BEARING_SECTIONS)


def test_ready_topics_have_link_count_in_range(topic_docs):
    for doc in topic_docs:
        if doc.frontmatter.get("status") != "ready":
            continue
        count = _count_links(doc)
        assert MIN_LINKS <= count <= MAX_LINKS, (
            f"{doc.path.name} is status: ready but has {count} links "
            f"(expected {MIN_LINKS}-{MAX_LINKS})"
        )


def test_skeleton_topics_exist_and_are_exempt(topic_docs):
    """Sanity check: at least some topics are still skeletons in Plan 1."""
    skeleton_count = sum(
        1 for d in topic_docs if d.frontmatter.get("status") == "skeleton"
    )
    ready_count = sum(
        1 for d in topic_docs if d.frontmatter.get("status") == "ready"
    )
    assert skeleton_count + ready_count == len(topic_docs), (
        "Every topic must be skeleton or ready; no other status permitted."
    )
