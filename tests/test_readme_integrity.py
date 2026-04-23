"""README masthead one-liner contains '16 topics' and '4 reading paths'.
These numbers must match the filesystem. Direct application of the
'numbers in docs are tests waiting to be written' principle.
"""

import re

from tests.conftest import TOPICS_DIR, PATHS_DIR


def test_readme_topic_count_matches_filesystem(readme_text):
    m = re.search(r"(\d+)\s+topics", readme_text)
    assert m, "README must contain a 'N topics' phrase"
    claimed = int(m.group(1))
    actual = len(list(TOPICS_DIR.glob("*.md")))
    assert claimed == actual, (
        f"README claims {claimed} topics; filesystem has {actual}. "
        "Update the README masthead one-liner to match."
    )


def test_readme_path_count_matches_filesystem(readme_text):
    m = re.search(r"(\d+)\s+reading paths", readme_text)
    assert m, "README must contain a 'N reading paths' phrase"
    claimed = int(m.group(1))
    actual = len(list(PATHS_DIR.glob("*.md")))
    assert claimed == actual, (
        f"README claims {claimed} reading paths; filesystem has {actual}. "
        "Update the README masthead one-liner to match."
    )
