"""Topic files may only use the five approved H2 headings."""

ALLOWED_H2 = {"Start here", "Go deeper", "Tools", "Watch", "Related topics"}
REQUIRED_H2 = {"Start here", "Go deeper", "Related topics"}


def test_topic_h2s_are_in_allowed_set(topic_docs):
    for doc in topic_docs:
        for h2 in doc.h2_headings:
            assert h2 in ALLOWED_H2, (
                f"{doc.path.name}: H2 '{h2}' is not in the approved set "
                f"{sorted(ALLOWED_H2)}. See CONTRIBUTING.md for the lock-in rule."
            )


def test_topic_required_h2s_present(topic_docs):
    for doc in topic_docs:
        h2_set = set(doc.h2_headings)
        missing = REQUIRED_H2 - h2_set
        assert not missing, (
            f"{doc.path.name}: missing required H2(s): {sorted(missing)}"
        )


def test_topic_h2s_unique(topic_docs):
    """A topic file must not repeat the same H2."""
    for doc in topic_docs:
        seen = []
        for h2 in doc.h2_headings:
            assert h2 not in seen, f"{doc.path.name}: duplicate H2 '{h2}'"
            seen.append(h2)
