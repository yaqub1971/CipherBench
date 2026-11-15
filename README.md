# CipherBench

Can an AI system solve a cipher that nobody has solved?

CipherBench is a benchmark of six open cipher challenges. Each one is unsolved, and each one was selected because a correct answer can be verified.

All six were unsolved on November 2026.

## Testing an AI system

Give the AI system [`INSTRUCTIONS.md`](INSTRUCTIONS.md). It contains the task, the six challenges with their ciphertexts, and what the report must contain. The AI system may use any method to arrive at an answer.

## The six challenges

The challenges are listed from the hardest to the easiest.

| # | Challenge | Year | Size | Language | How a correct answer is checked |
|---|---|---|---|---|---|
| 1 | Kryptos K4 | 1990 | 97 letters | English | The owner of the answer runs an online verifier |
| 2 | Double Column Transposition Reloaded, parts 1–3 | 2013 | 613, 637 and 1,006 letters | English, German | The keys are re-run on the ciphertext |
| 3 | Enigma message from U-534 | 1945 | 72 letters | German | The settings are re-run on an Enigma simulator |
| 4 | French Resistance message | 1944 | 465 letters | French | The keys are re-run on the ciphertext |
| 5 | Enigma message RXPSB | 1941 | 107 letters | German | The settings are re-run on an Enigma simulator |
| 6 | Grüß's mental-arithmetic cipher | 2026 | 31 digits | German | The author published a hash of the answer in advance |

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

### 3. Enigma message from U-534, 1945

The Enigma was the cipher machine of the German armed forces in the Second World War. Several thousand of its radio messages survive. Most of those that have been attacked are now broken, but a few have resisted every attempt.

This is one of them. It is a German Navy message, taken down on board the submarine U-534 on 1 May 1945, four days before she was sunk. The boat's own radio operator tried to decipher it and failed. It was enciphered on the Navy Enigma M4 with four wheels and has 72 letters. [Michael Hörenberg](https://enigma.hoerenberg.com/index.php?cat=Unbroken) publishes it under the number P1030680.

- **Full solution:** the Enigma settings and the complete German plaintext. The settings are the wheel order including the fourth wheel, the reflector, the ring settings, the plugboard connections and the start position.
- **Check:** the settings are entered into an Enigma simulator and must produce the submitted plaintext exactly. The answer counts once the plaintext is confirmed to be a German message.
- **Note:** a solution must work on the standard M4. A machine with invented wiring could be made to produce any text.

### 4. French Resistance message, 1944

A handwritten sheet of 93 five-letter groups, found with a clandestine radio set of the type used by Britain's Special Operations Executive. Didier Clarençon showed it at the HistoCrypt conference in 2026, and Klaus Schmeh [published it](https://klausschmeh.net/an-encrypted-message-from-the-french-resistance-can-you-decipher-it/).

- **What is known:** the first and last groups are identical. The mix of letters matches French, which means the letters were rearranged, not replaced. A double column transposition is the usual guess for this kind of radio traffic.
- **Transcription:** made for this benchmark from the photograph of the sheet. The notes are in the [challenge file](challenges/french-resistance-1944/challenge.json).
- **Full solution:** the keys and the complete plaintext of the message.
- **Check:** the keys are applied to the ciphertext and must produce the submitted plaintext exactly. The answer counts once the plaintext is confirmed to be the French message.

### 5. Enigma message RXPSB, 1941

A second unbroken Enigma message, this one from the German Army. It was sent on 28 June 1941, in the first week of the invasion of the Soviet Union, and enciphered on the Army Enigma with three wheels. It has 107 letters, 2 of them unread. [Frode Weierud's CryptoCellar](https://cryptocellar.org/bgac/g-army-messages.html) publishes it with a copy of the original message form.

- **Full solution:** the Enigma settings and the complete German plaintext. The settings are the wheel order, the ring settings, the plugboard connections and the start position.
- **Check:** the settings are entered into an Enigma simulator and must produce the submitted plaintext exactly. The answer counts once the plaintext is confirmed to be a German message.
- **Note:** a solution must work on the standard Army Enigma. A machine with invented wiring could be made to produce any text.

### 6. Grüß's mental-arithmetic cipher

The mental calculator Wenzel Grüß designed a cipher that can be worked entirely in the head, both ways. He used it to turn one German word of exactly ten letters into 31 digits, [published in October 2026](https://klausschmeh.net/can-you-solve-this-puzzle-from-a-world-class-mental-calculator-and-win-100-euros/):

```
3150105362170496
804276904486349
```

Before publishing, he fixed the answer by releasing a SHA-256 hash of his solution statement. He offers 100 euros for the first solution.

- **Full solution:** the word and the method that turns the 31 digits into it.
- **Check:** the author confirms a correct answer against the hash he published in advance.
- **Note:** a word that is guessed, or matched against the hash without the method, does not count.

## Why these six

Each challenge was selected because a correct answer can be verified and checked:

- **Someone holds the answer.** For Kryptos K4 and the Grüß cipher, a hash of the answer was stored in advance. A submitted answer either matches or it does not.
- **The method is fixed.** For the transposition challenges, the French message and the two Enigma messages, a claimed key is simply run again. It either produces a readable message or it does not.

## How answers are graded

The AI system is asked to write a report explaining how it solved each puzzle. What the report must contain is set out in [`INSTRUCTIONS.md`](INSTRUCTIONS.md). A proposed solution is then confirmed in two ways:

1. **On the challenge's website.** Two of the six challenges have a website that checks solutions. For these, the proposed solution is checked there:
   - **Kryptos K4:** the owner's [online verifier](https://paradigm.xyz/kryptos/k4).
   - **Double Column Transposition Reloaded, parts 1–3:** the solution check on [MysteryTwister](https://mysterytwister.org/challenges/level-3/).

   The Grüß cipher, the French Resistance message and the two Enigma messages have no such website.
2. **By a human.** A human reads the report and confirms that the proposed solution is correct.

## Scoring

Each challenge is worth one sixth of the score, about 16.7%. A challenge counts only when it is solved in full and the solution has been confirmed.

| Challenges solved | Score |
|---|---|
| 0 | 0% |
| 1 | 16.7% |
| 2 | 33.3% |
| 3 | 50% |
| 4 | 66.7% |
| 5 | 83.3% |
| 6 | 100% |

Partial solutions are not accepted. One of the three transposition ciphertexts, or most of a message, scores nothing.

## Sources and credit

The challenges belong to their creators. They are reproduced here, with their sources, so that answers can be checked.

- **Kryptos:** Jim Sanborn. Ciphertext and verifier from [Paradigm](https://paradigm.xyz/kryptos/k4).
- **Double Column Transposition Reloaded:** Arno Wacker, Bernhard Esslinger and Klaus Schmeh, on [MysteryTwister](https://mysterytwister.org/challenges/level-3/).
- **Enigma message from U-534:** [Michael Hörenberg](https://enigma.hoerenberg.com/index.php?cat=Unbroken).
- **French Resistance message:** sheet shown by Didier Clarençon, published by [Klaus Schmeh](https://klausschmeh.net/an-encrypted-message-from-the-french-resistance-can-you-decipher-it/).
- **Enigma message RXPSB:** [Frode Weierud's CryptoCellar](https://cryptocellar.org/bgac/g-army-messages.html), a project of Geoff Sullivan, Olaf Ostwald and Frode Weierud.
- **Grüß's cipher:** Wenzel Grüß, published by [Klaus Schmeh](https://klausschmeh.net/can-you-solve-this-puzzle-from-a-world-class-mental-calculator-and-win-100-euros/).
- **Background:** Klaus Schmeh's [list of the top 50 unsolved encrypted messages](https://scienceblogs.de/klausis-krypto-kolumne/the-top-50-unsolved-encrypted-messages/) and his [current site](https://klausschmeh.net/).
