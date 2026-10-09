"""Run with: python3 tests/test_check_text.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "skills", "text-quality-check", "scripts"))
from check_text import analyse  # noqa: E402

DRAFT = """# Title

In today's fast-paced world, we must delve into tokens. Moreover, it's important to note that tokens play a crucial role.

Tokens are units. They cost money. The quick brown fox jumps over the lazy dog near the river bank today.
"""
SOURCE = ("notes.txt", "the quick brown fox jumps over the lazy dog near the river")


def test_patterns_found():
    found = {p["pattern"] for p in analyse(DRAFT)["ai_style_patterns"]}
    for p in ("delve", "in today's ...", "Furthermore / Moreover", "it's important / worth noting", "plays a crucial role"):
        assert p in found, p


def test_copied_wording():
    r = analyse(DRAFT, sources=[SOURCE])
    assert r["copied_passages"] and r["copied_passages"][0]["words"] >= 8


def test_quotes_are_allowed():
    r = analyse('He said "the quick brown fox jumps over the lazy dog near the river" once.', sources=[SOURCE])
    assert not r["copied_passages"]


def test_clean_text():
    r = analyse("Short sentences help readers. Plain words help too. Keep each idea clear and simple for everyone.")
    assert not r["ai_style_patterns"] and r["reading_ease"] > 55


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("passed", name)
