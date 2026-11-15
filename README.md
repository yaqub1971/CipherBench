# CypherBench

Can an AI system solve a cipher that nobody has solved?

CypherBench is a benchmark of five open cipher challenges. Each one is unsolved, and each one was selected because a correct answer can be verified and checked.

All five were unsolved on 15 November 2026.

## The five challenges

| # | Challenge | Year | Size | Language | How a correct answer is checked |
|---|---|---|---|---|---|
| 1 | Kryptos K4 | 1990 | 97 letters | English | The owner of the answer runs an online verifier |
| 2 | Double Column Transposition Reloaded, parts 1–3 | 2013 | 613, 637 and 1,006 letters | English, German | The keys are re-run on the ciphertext |
| 3 | Grüß's mental-arithmetic cipher | 2026 | 31 digits | German | The author published a hash of the answer in advance |
| 4 | French Resistance message | 1944 | 465 letters | French | The keys are re-run on the ciphertext |
| 5 | Urquhart's Cyphral Distich | 1653 | 64 numbers | English or Latin | The rule is re-run against a named printed text |

The ciphertexts and their details are in [`challenges/`](challenges).

### 1. Kryptos K4

Kryptos is a sculpture by Jim Sanborn at CIA headquarters. It carries four enciphered passages. Three were solved by 1999. The fourth, known as K4, has 97 letters and has not been solved.

The artist has published four pieces of the plaintext as hints:

| Letters | Plaintext |
|---|---|
| 22–25 | EAST |
| 26–34 | NORTHEAST |
| 64–69 | BERLIN |
| 70–74 | CLOCK |

- **Full solution:** the complete 97-letter plaintext.
- **Check:** the current owner of the artist's solution runs an [online verifier](https://paradigm.xyz/kryptos/k4). It compares a submitted text with a stored hash of the artist's plaintext, so it can say yes or no without revealing the answer.
- **Note:** the plaintext was found among the artist's archived papers in 2025. It has not been published, and how the cipher works is still unknown.

### 2. Double Column Transposition Reloaded, parts 1–3

A column transposition keeps every letter of a message and changes their order: the text is written in rows under a key and read out column by column. A double column transposition does this twice, with two different keys.

The first public challenge of this kind was set in 2007 and solved in 2013. Arno Wacker, Bernhard Esslinger and Klaus Schmeh then published three harder ones on [MysteryTwister](https://mysterytwister.org/challenges/level-3/). Nobody has solved any of them.

| Part | Letters | Plaintext | Keys |
|---|---|---|---|
| 1 | 613 | English | 20–27 columns each, made from English sentences |
| 2 | 637 | Two English texts interleaved word by word | 20–27 columns each, random |
| 3 | 1,006 | German | 27–34 columns each, random |

- **Full solution:** both keys and the complete plaintext of all three parts.
- **Check:** the two keys are applied to the ciphertext and must produce the submitted plaintext exactly. The answer counts once MysteryTwister's solution check accepts it.

### 3. Grüß's mental-arithmetic cipher

The mental calculator Wenzel Grüß designed a cipher that can be worked entirely in the head, both ways. He used it to turn one German word of exactly ten letters into 31 digits, [published in October 2026](https://klausschmeh.net/can-you-solve-this-puzzle-from-a-world-class-mental-calculator-and-win-100-euros/):

```
3150105362170496
804276904486349
```

Before publishing, he fixed the answer by releasing a SHA-256 hash of his solution statement. He offers 100 euros for the first solution.

- **Full solution:** the word and the method that turns the 31 digits into it.
- **Check:** the author confirms a correct answer against the hash he published in advance.
- **Note:** a word that is guessed, or matched against the hash without the method, does not count.

### 4. French Resistance message, 1944

A handwritten sheet of 93 five-letter groups, found with a clandestine radio set of the type used by Britain's Special Operations Executive. Didier Clarençon showed it at the HistoCrypt conference in 2026, and Klaus Schmeh [published it](https://klausschmeh.net/an-encrypted-message-from-the-french-resistance-can-you-decipher-it/).

- **What is known:** the first and last groups are identical. The mix of letters matches French, which means the letters were rearranged, not replaced. A double column transposition is the usual guess for this kind of radio traffic.
- **Transcription:** made for this benchmark from the photograph of the sheet. The notes are in the [challenge file](challenges/french-resistance-1944/challenge.json).
- **Full solution:** the keys and the complete plaintext of the message.
- **Check:** the keys are applied to the ciphertext and must produce the submitted plaintext exactly. The answer counts once the plaintext is confirmed to be the French message.

### 5. Urquhart's Cyphral Distich

Sir Thomas Urquhart, a Scottish writer, printed two poems as rows of numbers.

- **The longer poem has been solved.** It has 285 numbers and appeared in 1652. An AI system solved it in August 2026, as reported by Vals AI, and the solution has been confirmed independently. Each number points to a word on a page of Urquhart's own book, and the first letters of those words spell a prayer for King Charles II.
- **The shorter poem is still open.** It has 64 numbers and appeared in 1653. The rule that opens the longer poem does not open this one. The shorter poem is the challenge here.

Under the numbers Urquhart printed a promise that a skilful reader will find in them "his own heart's wishes, and the Author's minde".

- **Full solution:** a named printed text and a fixed rule that turn all 64 numbers into letters, plus the 64-letter plaintext.
- **Check:** the rule is applied to the named text and must produce the submitted plaintext for every number. The answer counts once the named text is confirmed as a real printing that Urquhart could have used, and the plaintext as a readable line.

## Why these five

Each challenge was selected because a correct answer can be verified and checked:

- **Someone holds the answer.** For Kryptos K4 and the Grüß cipher, a hash of the answer was stored in advance. A submitted answer either matches or it does not.
- **The method is fixed.** For the transposition challenges, the French message and the Urquhart poem, a claimed key is simply run again. It either produces a readable message or it does not.

## Scoring

Each challenge is worth 20%. A challenge counts only when it is solved in full and the solution has passed its check.

| Challenges solved | Score |
|---|---|
| 0 | 0% |
| 1 | 20% |
| 2 | 40% |
| 3 | 60% |
| 4 | 80% |
| 5 | 100% |

Partial solutions are not accepted. One of the three transposition ciphertexts, or most of a message, scores nothing.

An answer counts once it has been confirmed. The checker does the mechanical part and reports the answer as awaiting confirmation until then.

| Challenge | What the checker does | What confirms the answer |
|---|---|---|
| Kryptos K4 | Confirms 97 letters that fit the four published fragments | The owner's verifier accepts the text |
| Double Column Transposition Reloaded | Runs the keys of all three parts and compares the result with the submitted plaintexts | MysteryTwister's solution check accepts them |
| Grüß's cipher | Confirms a ten-letter word with a method, and tries it against the published hash | The author confirms the answer |
| French Resistance message | Runs the keys and compares the result with the submitted plaintext | The plaintext is confirmed to be the French message |
| Urquhart's Cyphral Distich | Applies the rule to the named text and compares the result with the submitted plaintext | The named text and the reading are confirmed |

## Running the checker

It needs Python 3.9 or later and nothing else.

```bash
python -m cypherbench list
```

```bash
python -m cypherbench score submissions/TEMPLATE.json
```

Once an answer has been confirmed, name that challenge with `--confirmed`:

```bash
python -m cypherbench score my-answers.json --confirmed kryptos-k4,gruess-cipher
```

Answers go in one JSON file. [`submissions/TEMPLATE.json`](submissions/TEMPLATE.json) shows the format.

- **Column keys** are given in the order they were used to encipher. A key is either a keyword or a list of numbers giving each column's rank, so `"ZEBRAS"` and `[6, 3, 2, 4, 1, 5]` are the same key.
- **The French message** also needs the run of groups that forms the message, for example `"groups": [3, 92]`.
- **The Urquhart poem** needs the source text as a plain-text file, with its pages or sections separated by lines that start with `===`, and one of the rules listed in [`cypherbench/bookindex.py`](cypherbench/bookindex.py).

The tests include the 2007 transposition challenge with its published keys, as a real case with a known answer:

```bash
python -m unittest discover -s tests
```

## What is in the repository

| Path | Contents |
|---|---|
| `challenges/` | The five ciphertexts, each with a file describing its origin, what is known, and how it is checked |
| `cypherbench/` | The checker and the scorer |
| `submissions/` | The answer template |
| `tests/` | Tests for the checker |

## Sources and credit

The challenges belong to their creators. They are reproduced here, with their sources, so that answers can be checked.

- **Kryptos:** Jim Sanborn. Ciphertext and verifier from [Paradigm](https://paradigm.xyz/kryptos/k4).
- **Double Column Transposition Reloaded:** Arno Wacker, Bernhard Esslinger and Klaus Schmeh, on [MysteryTwister](https://mysterytwister.org/challenges/level-3/).
- **Grüß's cipher:** Wenzel Grüß, published by [Klaus Schmeh](https://klausschmeh.net/can-you-solve-this-puzzle-from-a-world-class-mental-calculator-and-win-100-euros/).
- **French Resistance message:** sheet shown by Didier Clarençon, published by [Klaus Schmeh](https://klausschmeh.net/an-encrypted-message-from-the-french-resistance-can-you-decipher-it/).
- **Urquhart's Cyphral Distich:** text from the [1834 edition of Urquhart's works](https://archive.org/details/worksofsirthomas00mait), page 417. The account of the longer poem follows [Cyphersolver](https://cyphersolver.com/urquhart.html).
- **Background:** Klaus Schmeh's [list of the top 50 unsolved encrypted messages](https://scienceblogs.de/klausis-krypto-kolumne/the-top-50-unsolved-encrypted-messages/) and his [current site](https://klausschmeh.net/).
