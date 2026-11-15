"""Checks for answers to the five challenges.

A challenge is either solved or not solved. There is no partial credit. The checks
here confirm what can be confirmed mechanically; an answer counts as solved once it
has also been confirmed from outside, as described in the README.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import unicodedata
from dataclasses import dataclass, field

from . import bookindex, transposition

SOLVED = "solved"
NOT_SOLVED = "not solved"
AWAITING = "awaiting confirmation"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHALLENGE_DIR = os.path.join(ROOT, "challenges")
ORDER = ["kryptos-k4", "transposition-reloaded", "gruess-cipher", "french-resistance-1944", "urquhart-distich"]


@dataclass
class Result:
    challenge: str
    status: str
    detail: str
    parts: dict = field(default_factory=dict)


def load_challenge(cid: str) -> dict:
    with open(os.path.join(CHALLENGE_DIR, cid, "challenge.json"), encoding="utf-8") as f:
        return json.load(f)


def read_ciphertext(cid: str, name: str = "ciphertext.txt") -> str:
    with open(os.path.join(CHALLENGE_DIR, cid, name), encoding="utf-8") as f:
        return f.read()


def letters_only(text: str) -> str:
    """Upper-case A-Z only, accents folded."""
    text = text.replace("ß", "SS").replace("œ", "oe").replace("æ", "ae")
    text = unicodedata.normalize("NFKD", text)
    return re.sub(r"[^A-Z]", "", text.upper())


def check_columnar(ciphertext: str, answer: dict) -> tuple[bool, str]:
    """Run the submitted column keys (given in the order used to encipher) on the ciphertext."""
    keys = answer.get("keys")
    plaintext = letters_only(str(answer.get("plaintext", "")))
    if not isinstance(keys, list) or not 1 <= len(keys) <= 3:
        return False, "give one to three column keys under 'keys', in the order they were used to encipher"
    try:
        keys = [k if isinstance(k, str) else [int(x) for x in k] for k in keys]
        rerun = transposition.decrypt_many(ciphertext, keys)
    except (ValueError, TypeError) as e:
        return False, f"key not usable: {e}"
    if rerun != plaintext:
        return False, "the keys do not turn the ciphertext into the submitted plaintext"
    return True, "the keys turn the ciphertext into the submitted plaintext"


def check_kryptos_k4(answer: dict, base_dir: str = ".") -> Result:
    cid = "kryptos-k4"
    ch = load_challenge(cid)
    plaintext = letters_only(str(answer.get("plaintext", "")))
    if len(plaintext) != 97:
        return Result(cid, NOT_SOLVED, f"the plaintext must have 97 letters, this one has {len(plaintext)}")
    for frag in ch["known_plaintext"]:
        a, b = frag["positions"]
        if plaintext[a - 1:b] != frag["text"]:
            return Result(cid, NOT_SOLVED,
                          f"positions {a}-{b} must read {frag['text']}, as published by the artist")
    return Result(cid, AWAITING, "fits the published fragments; counts once the owner's verifier accepts it "
                                 f"({ch['verification']['where']})")


def check_transposition_reloaded(answer: dict, base_dir: str = ".") -> Result:
    cid = "transposition-reloaded"
    ch = load_challenge(cid)
    parts, all_ok = {}, True
    for name, spec in ch["parts"].items():
        sub = answer.get(name)
        if not isinstance(sub, dict):
            parts[name] = "no answer"
            all_ok = False
            continue
        ciphertext = letters_only(read_ciphertext(cid, f"{name}.txt"))
        ok, why = check_columnar(ciphertext, sub)
        if ok and len(sub.get("keys", [])) != 2:
            ok, why = False, "this challenge uses exactly two keys"
        if ok:
            why += f"; to submit to MysteryTwister: {letters_only(sub['plaintext'])[:spec['solution_prefix']]}"
        parts[name] = why
        all_ok = all_ok and ok
    if all_ok:
        return Result(cid, AWAITING, "the keys of all three parts produce the submitted texts; "
                                     "counts once MysteryTwister's solution check accepts them", parts)
    return Result(cid, NOT_SOLVED, "all three parts are required, each with keys that produce its plaintext", parts)


def check_gruess_cipher(answer: dict, base_dir: str = ".") -> Result:
    cid = "gruess-cipher"
    ch = load_challenge(cid)
    word = unicodedata.normalize("NFC", str(answer.get("word", "")).strip())
    if len(word) != 10 or not all(c.isalpha() for c in word):
        return Result(cid, NOT_SOLVED, "the answer must be one German word of exactly ten letters")
    if len(str(answer.get("method", "")).strip()) < 80:
        return Result(cid, NOT_SOLVED, "describe the method that turns the 31 digits into the word; a guessed word does not count")
    target = ch["commitment"]["hash"]
    for form in {word, word.upper(), word.lower(), word.capitalize()}:
        for tail in ("", "\n"):
            if hashlib.sha256((form + tail).encode("utf-8")).hexdigest() == target:
                return Result(cid, SOLVED, "the word matches the hash the author published in advance")
    return Result(cid, AWAITING, "ten letters with a method; counts once the author confirms it against his published hash")


def check_french_resistance_1944(answer: dict, base_dir: str = ".") -> Result:
    cid = "french-resistance-1944"
    ch = load_challenge(cid)
    groups = read_ciphertext(cid).split()
    for number, reading in (answer.get("readings") or {}).items():
        allowed = ch["transcription"]["alternative_readings"].get(str(number), [])
        if reading not in allowed:
            return Result(cid, NOT_SOLVED, f"group {number} may only be read as one of {allowed or 'the transcribed form'}")
        groups[int(number) - 1] = reading
    try:
        first, last = (int(x) for x in answer.get("groups", ()))
    except (TypeError, ValueError):
        return Result(cid, NOT_SOLVED, "state which groups form the message, e.g. \"groups\": [3, 92]")
    if not (1 <= first <= 3 and 92 <= last <= 93):
        return Result(cid, NOT_SOLVED, "the solution must cover the whole message: from group 1, 2 or 3 to group 92 or 93")
    ok, why = check_columnar("".join(groups[first - 1:last]), answer)
    if not ok:
        return Result(cid, NOT_SOLVED, why)
    return Result(cid, AWAITING, why + "; counts once the text is confirmed to be the French message")


def check_urquhart_distich(answer: dict, base_dir: str = ".") -> Result:
    cid = "urquhart-distich"
    numbers = [int(x) for x in read_ciphertext(cid).split()]
    plaintext = letters_only(str(answer.get("plaintext", "")))
    source = answer.get("source") or {}
    if not (source.get("title") and source.get("where")):
        return Result(cid, NOT_SOLVED, "name the printed text the numbers point into: \"source\": {\"title\": ..., \"where\": ...}")
    if not answer.get("text_file"):
        return Result(cid, NOT_SOLVED, "give the text as \"text_file\" and the rule that reads the numbers against it")
    try:
        with open(os.path.join(base_dir, answer["text_file"]), encoding="utf-8") as f:
            text = f.read()
        derived = bookindex.apply(numbers, text, str(answer.get("rule", "")), int(answer.get("section_offset", 0)))
    except (OSError, ValueError) as e:
        return Result(cid, NOT_SOLVED, f"could not apply the rule: {e}")
    if "?" in derived:
        return Result(cid, NOT_SOLVED, f"the rule gives no letter for {derived.count('?')} of the 64 numbers; all 64 are required")
    if derived != plaintext:
        wrong = sum(a != b for a, b in zip(derived, plaintext)) + abs(len(derived) - len(plaintext))
        return Result(cid, NOT_SOLVED, f"the rule does not produce the submitted plaintext ({wrong} letters differ)")
    return Result(cid, AWAITING, "the rule produces all 64 submitted letters; "
                                 "counts once the named text and the reading are confirmed")


CHECKS = {
    "kryptos-k4": check_kryptos_k4,
    "transposition-reloaded": check_transposition_reloaded,
    "gruess-cipher": check_gruess_cipher,
    "french-resistance-1944": check_french_resistance_1944,
    "urquhart-distich": check_urquhart_distich,
}


def check_all(submission: dict, base_dir: str = ".", confirmed: frozenset = frozenset()) -> list[Result]:
    """Check a whole submission. `confirmed` names the challenges whose answer has been confirmed."""
    answers = submission.get("answers") or {}
    results = []
    for cid in ORDER:
        answer = answers.get(cid)
        if not isinstance(answer, dict):
            results.append(Result(cid, NOT_SOLVED, "no answer submitted"))
            continue
        result = CHECKS[cid](answer, base_dir)
        if result.status == AWAITING and cid in confirmed:
            result = Result(cid, SOLVED, "confirmed: " + result.detail.split(";")[0], result.parts)
        results.append(result)
    return results


def score(results: list[Result]) -> tuple[int, int]:
    """Number of challenges solved, and the score in per cent. Each challenge is worth 20."""
    solved = sum(r.status == SOLVED for r in results)
    return solved, 100 * solved // len(ORDER)
