"""Every topic and path file must have valid frontmatter."""

from datetime import date


def test_topic_files_exist(topic_docs):
    assert len(topic_docs) == 16, f"expected 16 topic files, found {len(topic_docs)}"


def test_path_files_exist(path_docs):
    assert len(path_docs) == 4, f"expected 4 path files, found {len(path_docs)}"


def test_topic_frontmatter_schema(topic_docs):
    required = {"title", "summary", "last-reviewed", "status"}
    for doc in topic_docs:
        missing = required - set(doc.frontmatter)
        assert not missing, f"{doc.path.name}: missing frontmatter fields {missing}"


def test_topic_status_is_valid(topic_docs):
    allowed = {"skeleton", "ready"}
    for doc in topic_docs:
        status = doc.frontmatter.get("status")
        assert status in allowed, f"{doc.path.name}: status '{status}' not in {allowed}"


def test_last_reviewed_is_parseable_date(topic_docs):
    for doc in topic_docs:
        value = doc.frontmatter.get("last-reviewed")
        # PyYAML may return a datetime.date directly if the value parses as a date
        if isinstance(value, date):
            continue
        raise AssertionError(
            f"{doc.path.name}: last-reviewed must be YYYY-MM-DD, got {value!r}"
        )


def test_topic_summary_length(topic_docs):
    for doc in topic_docs:
        summary = doc.frontmatter.get("summary", "")
        word_count = len(summary.split())
        assert 3 <= word_count <= 25, (
            f"{doc.path.name}: summary is {word_count} words; "
            "spec says roughly 20 words"
        )
