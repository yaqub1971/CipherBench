"""Columnar transposition, single and repeated.

Convention (the classical one): write the text in rows under the key, then read the
columns out in key order. A key is either a keyword (columns are read in alphabetical
order of its letters, ties from left to right) or a list of numbers giving each
column's rank, e.g. the keyword ZEBRAS is the same key as [6, 3, 2, 4, 1, 5].
"""
from __future__ import annotations

from typing import Iterable, Sequence, Union

Key = Union[str, Sequence[int]]


def column_order(key: Key) -> list[int]:
    """Return the column indices in the order in which the columns are read out."""
    if isinstance(key, str):
        letters = [c for c in key.upper() if c.isalpha()]
        if not letters:
            raise ValueError("empty keyword")
        return sorted(range(len(letters)), key=lambda i: (letters[i], i))
    ranks = list(key)
    if sorted(ranks) != list(range(1, len(ranks) + 1)):
        raise ValueError("a numeric key must use each of 1..n exactly once")
    return sorted(range(len(ranks)), key=lambda i: ranks[i])


def key_length(key: Key) -> int:
    return len(column_order(key))


def encrypt(text: str, key: Key) -> str:
    order = column_order(key)
    n = len(order)
    return "".join(text[col::n] for col in order)


def decrypt(text: str, key: Key) -> str:
    order = column_order(key)
    n = len(order)
    rows, extra = divmod(len(text), n)
    columns: dict[int, str] = {}
    pos = 0
    for col in order:
        size = rows + (1 if col < extra else 0)
        columns[col] = text[pos:pos + size]
        pos += size
    out = []
    for r in range(rows + (1 if extra else 0)):
        for col in range(n):
            if r < len(columns[col]):
                out.append(columns[col][r])
    return "".join(out)


def encrypt_many(text: str, keys: Iterable[Key]) -> str:
    for key in keys:
        text = encrypt(text, key)
    return text


def decrypt_many(text: str, keys: Iterable[Key]) -> str:
    """Undo encrypt_many: the keys are given in the order they were used to encrypt."""
    for key in reversed(list(keys)):
        text = decrypt(text, key)
    return text

