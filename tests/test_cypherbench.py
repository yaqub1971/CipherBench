"""Tests for the checker. Run from the repository root:  python -m unittest discover -s tests"""
from __future__ import annotations

import json
import os
import random
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)

import samples  # noqa: E402
from cypherbench import bookindex, checks, transposition  # noqa: E402

REAL_CHALLENGES = checks.CHALLENGE_DIR


def letters(text: str) -> str:
    return checks.letters_only(text)


def random_key(n: int, rng: random.Random) -> list[int]:
    key = list(range(1, n + 1))
    rng.shuffle(key)
    return key


class Transposition(unittest.TestCase):
    def test_textbook_example(self):
        self.assertEqual(transposition.encrypt("WEAREDISCOVEREDFLEEATONCE", "ZEBRAS"), "EVLNACDTESEAROFODEECWIREE")
        self.assertEqual(transposition.decrypt("EVLNACDTESEAROFODEECWIREE", "ZEBRAS"), "WEAREDISCOVEREDFLEEATONCE")
        self.assertEqual(transposition.column_order("ZEBRAS"), transposition.column_order([6, 3, 2, 4, 1, 5]))

    def test_round_trip(self):
        rng = random.Random(1)
        text = letters(samples.ENGLISH)
        for _ in range(20):
            keys = [random_key(rng.randint(2, 40), rng) for _ in range(rng.randint(1, 3))]
            self.assertEqual(transposition.decrypt_many(transposition.encrypt_many(text, keys), keys), text)

    def test_rejects_bad_numeric_key(self):
        with self.assertRaises(ValueError):
            transposition.column_order([1, 1, 3])


class SolvedChallengeOf2007(unittest.TestCase):
    """The first challenge of this kind, set in 2007 and solved in 2013, with its published keys."""

    KEYS = ["TOSTAYYOUFROMELECTION", "PREPONDERANCEOFEVIDENCE"]

    def setUp(self):
        with open(os.path.join(HERE, "data", "dct_2007.txt"), encoding="utf-8") as f:
            self.ciphertext = letters(f.read())
        self.plaintext = transposition.decrypt_many(self.ciphertext, self.KEYS)

    def test_published_keys_give_english(self):
        self.assertEqual(len(self.ciphertext), 599)
        self.assertTrue(self.plaintext.startswith("THEGIRLHADARRIVEDATLUPTONHOUSEAHALFHOURAHEADOFMISSWESTMACOTT"))

    def test_checker_accepts_the_published_keys(self):
        ok, why = checks.check_columnar(self.ciphertext, {"keys": self.KEYS, "plaintext": self.plaintext})
        self.assertTrue(ok, why)

    def test_checker_rejects_a_plaintext_the_keys_do_not_produce(self):
        fake = self.plaintext[:-5] + "ZZZZZ"
        ok, why = checks.check_columnar(self.ciphertext, {"keys": self.KEYS, "plaintext": fake})
        self.assertFalse(ok)
        self.assertIn("do not turn the ciphertext", why)

class BookIndex(unittest.TestCase):
    def test_rules(self):
        text = "alpha beta gamma\n===\ndelta epsilon zeta\n===\neta theta iota"
        self.assertEqual(bookindex.apply([2, 3, 1], text, "word-initial-by-section"), "BZE")
        self.assertEqual(bookindex.apply([1, 5, 9], text, "word-initial"), "AEI")
        self.assertEqual(bookindex.apply([1, 2, 3], text, "letter-by-section"), "AEA")
        self.assertEqual(bookindex.apply([9, 1, 1], text, "word-initial-by-section"), "?DE")


class WithSyntheticChallenges(unittest.TestCase):
    """End-to-end checks on stand-in ciphertexts made here with known keys."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.root = os.path.join(self.tmp, "challenges")
        shutil.copytree(REAL_CHALLENGES, self.root)
        checks.CHALLENGE_DIR = self.root
        rng = random.Random(11)
        # transposition-reloaded: three stand-in parts
        self.dct = {}
        texts = {"part1": samples.ENGLISH, "part2": samples.ENGLISH_2, "part3": samples.GERMAN}
        sizes = {"part1": (21, 26), "part2": (23, 25), "part3": (29, 33)}
        for name, text in texts.items():
            plain = letters(text)
            keys = [random_key(n, rng) for n in sizes[name]]
            with open(os.path.join(self.root, "transposition-reloaded", f"{name}.txt"), "w") as f:
                f.write(transposition.encrypt_many(plain, keys) + "\n")
            self.dct[name] = {"keys": keys, "plaintext": plain}
        # french message: indicator, prefix, 90 groups of text, indicator
        plain = letters(samples.FRENCH)[:450]
        self.assertEqual(len(plain), 450)
        keys = [random_key(19, rng), random_key(28, rng)]
        body = transposition.encrypt_many(plain, keys)
        groups = ["JFGEU", "QTIIO"] + [body[i:i + 5] for i in range(0, 450, 5)] + ["JFGEU"]
        with open(os.path.join(self.root, "french-resistance-1944", "ciphertext.txt"), "w") as f:
            f.write(" ".join(groups) + "\n")
        self.french = {"groups": [3, 92], "keys": keys, "plaintext": plain}
        # urquhart: a made-up source text whose word initials spell a 64-letter line
        self.line = letters("Keep faith with the old house and its lawful heir until the storm has blown out")[:64]
        self.assertEqual(len(self.line), 64)
        numbers = [int(x) for x in checks.read_ciphertext("urquhart-distich").split()]
        filler = ["and", "of", "to", "in", "is", "by", "on", "we", "us", "so", "no", "my"]
        pages = []
        for n, letter in zip(numbers, self.line):
            words = [filler[rng.randrange(len(filler))] for _ in range(n - 1)] + [letter.lower() + "x"] + filler[:4]
            pages.append(" ".join(words))
        with open(os.path.join(self.tmp, "source.txt"), "w") as f:
            f.write("\n===\n".join(pages))
        self.urquhart = {"source": {"title": "stand-in text", "where": "made for the test"}, "text_file": "source.txt",
                         "rule": "word-initial-by-section", "plaintext": self.line}

    def tearDown(self):
        checks.CHALLENGE_DIR = REAL_CHALLENGES
        shutil.rmtree(self.tmp)

    def k4_answer(self):
        p = ["X"] * 97
        for a, text in ((22, "EAST"), (26, "NORTHEAST"), (64, "BERLIN"), (70, "CLOCK")):
            p[a - 1:a - 1 + len(text)] = text
        return {"plaintext": "".join(p), "method": "stand-in"}

    def test_transposition_needs_all_three_parts(self):
        full = checks.check_transposition_reloaded(self.dct)
        self.assertEqual(full.status, checks.AWAITING, full.parts)
        two = dict(self.dct)
        del two["part3"]
        self.assertEqual(checks.check_transposition_reloaded(two).status, checks.NOT_SOLVED)
        wrong = dict(self.dct)
        wrong["part2"] = {"keys": self.dct["part1"]["keys"], "plaintext": self.dct["part2"]["plaintext"]}
        self.assertEqual(checks.check_transposition_reloaded(wrong).status, checks.NOT_SOLVED)

    def test_french_message(self):
        self.assertEqual(checks.check_french_resistance_1944(self.french).status, checks.AWAITING)
        part = dict(self.french, groups=[10, 60])
        self.assertEqual(checks.check_french_resistance_1944(part).status, checks.NOT_SOLVED)
        bad_reading = dict(self.french, readings={"5": "AAAAA"})
        self.assertEqual(checks.check_french_resistance_1944(bad_reading).status, checks.NOT_SOLVED)

    def test_kryptos_screening(self):
        self.assertEqual(checks.check_kryptos_k4({"plaintext": "TOO SHORT"}).status, checks.NOT_SOLVED)
        self.assertEqual(checks.check_kryptos_k4({"plaintext": "A" * 97}).status, checks.NOT_SOLVED)
        self.assertEqual(checks.check_kryptos_k4(self.k4_answer()).status, checks.AWAITING)

    def test_gruess_screening(self):
        method = "x" * 100
        self.assertEqual(checks.check_gruess_cipher({"word": "kurz", "method": method}).status, checks.NOT_SOLVED)
        self.assertEqual(checks.check_gruess_cipher({"word": "Prüfungen"[:9] + "x", "method": ""}).status, checks.NOT_SOLVED)
        self.assertEqual(checks.check_gruess_cipher({"word": "Abenteurer", "method": method}).status, checks.AWAITING)

    def test_urquhart(self):
        ok = checks.check_urquhart_distich(self.urquhart, self.tmp)
        self.assertEqual(ok.status, checks.AWAITING, ok.detail)
        table_only = {"source": self.urquhart["source"], "plaintext": self.line}
        self.assertEqual(checks.check_urquhart_distich(table_only, self.tmp).status, checks.NOT_SOLVED)
        other = dict(self.urquhart, plaintext=self.line[:-1] + "Q")
        self.assertEqual(checks.check_urquhart_distich(other, self.tmp).status, checks.NOT_SOLVED)

    def test_scoring_in_steps_of_twenty(self):
        def run(answers, confirmed=()):
            results = checks.check_all({"answers": answers}, self.tmp, frozenset(confirmed))
            return checks.score(results)

        answers = {"transposition-reloaded": self.dct, "french-resistance-1944": self.french, "kryptos-k4": self.k4_answer(),
                   "gruess-cipher": {"word": "Abenteurer", "method": "x" * 100}, "urquhart-distich": self.urquhart}
        self.assertEqual(run({}), (0, 0))
        self.assertEqual(run(answers), (0, 0), "an answer does not count until it is confirmed")
        self.assertEqual(run(answers, ["transposition-reloaded"]), (1, 20))
        self.assertEqual(run(answers, ["transposition-reloaded", "french-resistance-1944"]), (2, 40))
        self.assertEqual(run(answers, ["transposition-reloaded", "french-resistance-1944", "kryptos-k4"]), (3, 60))
        self.assertEqual(run(answers, checks.ORDER[:4]), (4, 80))
        self.assertEqual(run(answers, checks.ORDER), (5, 100))
        # a confirmation cannot rescue an answer that fails its own check
        answers["kryptos-k4"] = {"plaintext": "A" * 97}
        two_parts = dict(self.dct)
        del two_parts["part3"]
        answers["transposition-reloaded"] = two_parts
        self.assertEqual(run(answers, checks.ORDER), (3, 60))


class ChallengeFiles(unittest.TestCase):
    def test_the_five_ciphertexts(self):
        self.assertEqual(len(letters(checks.read_ciphertext("kryptos-k4"))), 97)
        for name, n in (("part1", 613), ("part2", 637), ("part3", 1006)):
            self.assertEqual(len(letters(checks.read_ciphertext("transposition-reloaded", f"{name}.txt"))), n)
        self.assertEqual([len(l) for l in checks.read_ciphertext("gruess-cipher").split()], [16, 15])
        groups = checks.read_ciphertext("french-resistance-1944").split()
        self.assertEqual(len(groups), 93)
        self.assertTrue(all(len(g) == 5 and g.isalpha() and g.isupper() for g in groups))
        self.assertEqual(groups[0], groups[-1])
        numbers = [int(x) for x in checks.read_ciphertext("urquhart-distich").split()]
        self.assertEqual((len(numbers), len(set(numbers)), numbers[55]), (64, 32, 38))

    def test_metadata(self):
        for i, cid in enumerate(checks.ORDER, 1):
            ch = checks.load_challenge(cid)
            self.assertEqual((ch["id"], ch["order"], ch["status"]), (cid, i, "unsolved"))
            for name in ch["ciphertext"]:
                self.assertTrue(os.path.exists(os.path.join(checks.CHALLENGE_DIR, cid, name)))

    def test_no_answer_scores_zero_on_the_real_challenges(self):
        with open(os.path.join(os.path.dirname(HERE), "submissions", "TEMPLATE.json"), encoding="utf-8") as f:
            template = json.load(f)
        results = checks.check_all(template, os.path.join(os.path.dirname(HERE), "submissions"))
        self.assertEqual(checks.score(results), (0, 0))


if __name__ == "__main__":
    unittest.main()
