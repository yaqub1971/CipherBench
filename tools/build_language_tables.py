#!/usr/bin/env python3
"""Build the letter-trigram tables used to tell real language from scrambled letters.

For each language the table is made from public-domain books on Project Gutenberg and
calibrated on one book that is kept out of the table. Run from the repository root:

    python tools/build_language_tables.py [--cache DIR]

Books are downloaded to the cache directory as pg<ID>.txt if they are not there yet.
"""
from __future__ import annotations

import argparse
import collections
import gzip
import json
import math
import os
import random
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cypherbench.language import normalise  # noqa: E402

BOOKS = {
    # language: (books used for the table, book held out for calibration)
    "en": ([1342, 98, 766, 1400, 1260, 599, 1023], 145),
    "de": ([34811, 65661, 40739, 7205, 47406, 24746, 22367], 5323),
    "fr": ([13951, 14155, 17489, 17519, 17989, 2650], 32854),
    "la": ([33849, 28233, 227, 27672, 231, 23306, 226], 218),
}
NAMES = {"en": "English", "de": "German", "fr": "French", "la": "Latin"}
URL = "https://www.gutenberg.org/cache/epub/{id}/pg{id}.txt"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def load(book_id: int, cache: str) -> str:
    path = os.path.join(cache, f"pg{book_id}.txt")
    if not os.path.exists(path):
        os.makedirs(cache, exist_ok=True)
        urllib.request.urlretrieve(URL.format(id=book_id), path)
    text = open(path, encoding="utf-8", errors="replace").read()
    start, end = text.find("*** START OF"), text.find("*** END OF")
    if start != -1:
        text = text[text.find("\n", start) + 1:]
    if end != -1:
        text = text[:text.find("*** END OF")]
    return text


def build(lang: str, cache: str) -> dict:
    books, held_out = BOOKS[lang]
    corpus = "".join(normalise(load(b, cache), lang) for b in books)
    counts = collections.Counter(corpus[i:i + 3] for i in range(len(corpus) - 2))
    total = sum(counts.values())
    table = [round(math.log10((counts.get(a + b + c, 0) + 0.5) / (total + 0.5 * 26 ** 3)), 3)
             for a in ALPHABET for b in ALPHABET for c in ALPHABET]
    logp = {a + b + c: table[(i * 26 + j) * 26 + k]
            for i, a in enumerate(ALPHABET) for j, b in enumerate(ALPHABET) for k, c in enumerate(ALPHABET)}

    def score(s: str) -> float:
        return sum(logp[s[i:i + 3]] for i in range(len(s) - 2)) / (len(s) - 2)

    held = normalise(load(held_out, cache), lang)
    rng = random.Random(2026)
    calibration = {}
    for n in (60, 100, 200, 450, 1000):
        real, scrambled = [], []
        for _ in range(400):
            i = rng.randrange(len(held) - n)
            window = held[i:i + n]
            real.append(score(window))
            letters = list(window)
            rng.shuffle(letters)
            scrambled.append(score("".join(letters)))
        mean = lambda xs: sum(xs) / len(xs)
        calibration[str(n)] = {"real_mean": round(mean(real), 3), "real_min": round(min(real), 3),
                               "scrambled_mean": round(mean(scrambled), 3), "scrambled_max": round(max(scrambled), 3)}
    real_mean = calibration["450"]["real_mean"]
    scrambled_mean = calibration["450"]["scrambled_mean"]
    return {"language": NAMES[lang], "code": lang, "letters_in_table": len(corpus),
            "books": books, "held_out_book": held_out, "source": "Project Gutenberg",
            "threshold": round((real_mean + scrambled_mean) / 2, 3), "calibration": calibration, "log10_prob": table}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache", default=".gutenberg-cache")
    args = ap.parse_args()
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "cypherbench", "data")
    os.makedirs(out_dir, exist_ok=True)
    for lang in BOOKS:
        data = build(lang, args.cache)
        path = os.path.join(out_dir, f"trigrams_{lang}.json.gz")
        with gzip.GzipFile(path, "wb", mtime=0) as f:
            f.write(json.dumps(data, separators=(",", ":")).encode("utf-8"))
        cal = data["calibration"]
        print(f"{data['language']}: {data['letters_in_table']:,} letters; threshold {data['threshold']}; "
              + "; ".join(f"n={n}: real {c['real_mean']} (min {c['real_min']}), scrambled {c['scrambled_mean']} (max {c['scrambled_max']})"
                          for n, c in cal.items()))


if __name__ == "__main__":
    main()
