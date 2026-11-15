"""Book ciphers: numbers that point into a printed text.

A source text is a plain-text file. Sections (pages, chapters, numbered paragraphs)
are separated by a form-feed character or by a line that starts with "===".
"""
from __future__ import annotations

import re
import unicodedata

RULES = {
    "word-initial-by-section": "the k-th number n points to the n-th word of section k; take its first letter",
    "word-initial": "the number n points to the n-th word of the whole text; take its first letter",
    "letter-by-section": "the k-th number n points to the n-th letter of section k",
    "letter": "the number n points to the n-th letter of the whole text",
}


def _fold(s: str) -> str:
    s = s.replace("œ", "oe").replace("æ", "ae").replace("Œ", "OE").replace("Æ", "AE")
    return "".join(c for c in unicodedata.normalize("NFKD", s) if c.isascii())


def sections(text: str) -> list[str]:
    parts, cur = [], []
    for line in text.replace("\f", "\n===\n").split("\n"):
        if line.startswith("==="):
            parts.append("\n".join(cur))
            cur = []
        else:
            cur.append(line)
    parts.append("\n".join(cur))
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z]+", _fold(text))


def letters(text: str) -> str:
    return re.sub(r"[^A-Za-z]", "", _fold(text))


def apply(numbers: list[int], source: str, rule: str, section_offset: int = 0) -> str:
    """Return one upper-case letter per number, or '?' where the rule points outside the text."""
    if rule not in RULES:
        raise ValueError(f"unknown rule {rule!r}; available: {', '.join(RULES)}")
    secs = sections(source)
    out = []
    for k, n in enumerate(numbers):
        if rule.endswith("by-section"):
            idx = k + section_offset
            unit = secs[idx] if 0 <= idx < len(secs) else ""
        else:
            unit = source
        if rule.startswith("word-initial"):
            w = words(unit)
            out.append(w[n - 1][0].upper() if 1 <= n <= len(w) else "?")
        else:
            s = letters(unit)
            out.append(s[n - 1].upper() if 1 <= n <= len(s) else "?")
    return "".join(out)
