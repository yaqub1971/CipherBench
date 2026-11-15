"""Tell real language from scrambled letters with letter-trigram statistics.

A text is scored by the average log-probability of its three-letter sequences in a
given language. Real text and scrambled letters fall far apart on this scale; the
threshold stored with each table lies halfway between the two.
"""
from __future__ import annotations

import functools
import gzip
import json
import os
import re
import unicodedata

LANGUAGES = {"en": "English", "de": "German", "fr": "French", "la": "Latin"}
_DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def normalise(text: str, lang: str = "en") -> str:
    """Lower-case letters a-z only; accents folded the way telegrams and ciphers do."""
    text = text.lower().replace("œ", "oe").replace("æ", "ae")
    if lang == "de":
        text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    text = unicodedata.normalize("NFKD", text)
    text = re.sub(r"[^a-z]", "", text)
    if lang == "la":
        text = text.replace("v", "u").replace("j", "i")
    return text


@functools.lru_cache(maxsize=None)
def table(lang: str) -> dict:
    if lang not in LANGUAGES:
        raise ValueError(f"no language table for {lang!r}; available: {', '.join(LANGUAGES)}")
    with gzip.open(os.path.join(_DATA, f"trigrams_{lang}.json.gz"), "rt", encoding="utf-8") as f:
        return json.load(f)


def score(text: str, lang: str) -> float:
    """Average log10 probability per trigram; higher means more like the language."""
    s = normalise(text, lang)
    if len(s) < 3:
        return float("-inf")
    logp = table(lang)["log10_prob"]
    a = [ord(c) - 97 for c in s]
    return sum(logp[(a[i] * 26 + a[i + 1]) * 26 + a[i + 2]] for i in range(len(a) - 2)) / (len(a) - 2)


def threshold(lang: str) -> float:
    return table(lang)["threshold"]


def reads_as(text: str, lang: str) -> bool:
    return score(text, lang) >= threshold(lang)
