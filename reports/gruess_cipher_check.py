#!/usr/bin/env python3
"""Reproduces the steps of the report on Grüß's mental-arithmetic cipher (reports/gruess-cipher.md).

Usage:
    python3 reports/gruess_cipher_check.py                  # the arithmetic and the chance estimate
    python3 reports/gruess_cipher_check.py WORDLIST.txt     # also: ten-letter words with the same repeat pattern

WORDLIST.txt is any plain-text German word list, one word per line (UTF-8).
"""
import random
import sys

CIPHERTEXT = "3150105362170496" + "804276904486349"      # the two published lines, 31 digits
CANDIDATE = "EINHUNDERT"
# Remainders (mod 26) that the candidate word assigns to its eight different letters.
# This table is read off the candidate. It is not derived from an independent rule.
TABLE = {1: "I", 2: "U", 11: "T", 14: "H", 16: "D", 18: "R", 20: "E", 24: "N"}


def pattern(seq):
    """Repeat pattern of a sequence: equal items get equal numbers, in order of first appearance."""
    seen = {}
    return tuple(seen.setdefault(x, len(seen)) for x in seq)


def main():
    assert len(CIPHERTEXT) == 31
    blocks = [int(CIPHERTEXT[1 + 3 * i:4 + 3 * i]) for i in range(10)]
    rem26 = [b % 26 for b in blocks]
    rem13 = [b % 13 for b in blocks]
    print("leading digit :", CIPHERTEXT[0])
    print("blocks        :", blocks)
    print("block div 26  :", [b // 26 for b in blocks])
    print("block mod 26  :", rem26)
    print("block mod 13  :", rem13, "(every one is 1 or a prime)")
    print("repeat pattern:", pattern(rem26))
    print("same pattern as", CANDIDATE, ":", pattern(rem26) == pattern(CANDIDATE))
    print("decoded       :", "".join(TABLE[r] for r in rem26))

    # How often do ten random three-digit numbers show this exact repeat pattern mod 26?
    random.seed(1)
    trials, hits, target = 1_000_000, 0, pattern(CANDIDATE)
    for _ in range(trials):
        if pattern([random.randrange(100, 1000) % 26 for _ in range(10)]) == target:
            hits += 1
    print(f"chance of this repeat pattern for random blocks: about 1 in {trials // max(hits, 1)}")

    if len(sys.argv) > 1:
        fold = str.maketrans({"Ä": "AE", "Ö": "OE", "Ü": "UE", "ß": "SS"})
        words = set()
        with open(sys.argv[1], encoding="utf-8", errors="replace") as handle:
            for line in handle:
                word = line.strip().upper().replace("ẞ", "ß")
                for form in {word, word.translate(fold)}:
                    if len(form) == 10 and form.isalpha() and pattern(form) == pattern(rem26):
                        words.add(form)
        print(len(words), "ten-letter words in the list share the pattern:")
        print(" ".join(sorted(words)))


if __name__ == "__main__":
    main()
