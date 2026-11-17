# Challenge 6: Grüß's mental-arithmetic cipher

**Status: not solved.**

This report documents a candidate reading, the plaintext **EINHUNDERT** ("one hundred"), and the evidence for and against it. It is not a confirmed solution. Two things are missing:

- **The rule for the letters.** The candidate needs each letter to have a fixed number between 1 and 26. Those numbers are not the positions in the alphabet, and I did not find the rule behind them.
- **A check.** The author's hash cannot be tested without the exact text he hashed.

Do not enter EINHUNDERT as a solved challenge on the strength of this report. The sections below follow the order asked for in [`INSTRUCTIONS.md`](../INSTRUCTIONS.md).

The script [`gruess_cipher_check.py`](gruess_cipher_check.py) repeats the arithmetic in this report.

## 1. Summary

- **Read:** all 31 digits are accounted for: a leading 3 and ten blocks of three digits.
- **Finding:** when each block is divided by 26, the ten remainders are 20, 1, 24, 14, 2, 24, 16, 20, 18, 11. Blocks 1 and 8 have the same remainder, and so do blocks 3 and 6. No other two agree.
- **Candidate plaintext:** EINHUNDERT has exactly this pattern of repeated letters: E in places 1 and 8, N in places 3 and 6, and eight different letters in all. It is also the prize the author offers, 100 euros.
- **Kind of cipher, if the candidate is right:** a substitution with many numbers for each letter. Each letter has a number from 1 to 26. Any three-digit number that leaves this remainder when divided by 26 stands for the letter.
- **Key, as far as recovered:** I = 1, U = 2, T = 11, H = 14, D = 16, R = 18, E = 20, N = 24.
- **Uncertain:** the key above is read off the candidate word. It is not derived from a rule, so it cannot be used to confirm the word. The numbers of the other 18 letters are unknown.

## 2. The cipher

This is the rule as far as I could reconstruct it. Steps 1 to 3 use only the ciphertext. Step 4 depends on the candidate.

1. Write the two lines as one number of 31 digits: `3150105362170496804276904486349`.
2. Set the first digit, 3, aside. The author has said it is not part of the content. It probably states the length of a block.
3. Cut the other 30 digits into ten blocks of three and divide each block by 26. Keep the remainder.
4. Replace each remainder by its letter, using the table in section 3.

To encipher, the writer would do the reverse: take the number of the letter, add any multiple of 26 that gives a three-digit result, and write the result down. The multiples in this message are 5, 4, 13, 6, 19, 30, 10, 34, 18 and 13. I see no pattern in them.

In code:

```python
n = "3150105362170496804276904486349"
blocks = [int(n[1 + 3 * i:4 + 3 * i]) for i in range(10)]
table = {1: "I", 2: "U", 11: "T", 14: "H", 16: "D", 18: "R", 20: "E", 24: "N"}
print("".join(table[b % 26] for b in blocks))    # EINHUNDERT
```

## 3. The key

| Letter | I | U | T | H | D | R | E | N |
|---|---|---|---|---|---|---|---|---|
| Remainder | 1 | 2 | 11 | 14 | 16 | 18 | 20 | 24 |

- **Not complete.** Only the eight letters of the candidate word are covered.
- **Not explained.** The numbers are not the positions in the alphabet. This agrees with the author, who said the letters are not first turned into A = 1 to Z = 26. I could not find what they are instead. Section 8 lists what I ruled out.
- **No book or text is involved,** as far as I can tell.

## 4. The message

| Place | Block | Block ÷ 26 | Remainder | Letter |
|---|---|---|---|---|
| 1 | 150 | 5 | 20 | E |
| 2 | 105 | 4 | 1 | I |
| 3 | 362 | 13 | 24 | N |
| 4 | 170 | 6 | 14 | H |
| 5 | 496 | 19 | 2 | U |
| 6 | 804 | 30 | 24 | N |
| 7 | 276 | 10 | 16 | D |
| 8 | 904 | 34 | 20 | E |
| 9 | 486 | 18 | 18 | R |
| 10 | 349 | 13 | 11 | T |

- **Ciphertext:** `3 150 105 362 170 496 804 276 904 486 349`
- **Candidate plaintext:** EINHUNDERT
- **Translation:** "one hundred"

## 5. Why this might be the solution, and why it is not proven

**For the candidate**

- **The word was named before I looked.** On 28 October 2026 a reader guessed "einhundert" under the challenge post. It is the amount of the prize. I tested that word.
- **The alphabet size comes out of the numbers.** The two E blocks differ by 904 − 150 = 754 = 26 × 29. The two N blocks differ by 804 − 362 = 442 = 26 × 17. Their greatest common divisor is 26, the number of letters in the alphabet. I did not put 26 in.
- **The pattern is rare.** Ten random three-digit numbers show this exact pattern of equal remainders about once in 2,400 tries. The script estimates this by simulation.
- **Few words fit.** About 60 of 190,000 ten-letter German words in my word lists have this pattern. EINHUNDERT is by far the most common of them. The others are words such as GUTMÜTIGER, EHRBARKEIT and TODESDATUM.
- **It agrees with the author's answers.** The number is built block by block, a block does not depend on earlier ones, the first digit is not content, and the letters are not numbered by their place in the alphabet.
- **The line break fits.** The first line holds the 3 and five blocks. The second line holds the other five blocks.

**Against it**

- **The key is circular.** I chose the eight numbers so that the word comes out. Only two facts are independent of that choice: the two E blocks agree, and the two N blocks agree.
- **No rule for the key.** The author says a keen seventh-grade pupil can encipher and decipher after practice, and that no special knowledge is needed. So the letter numbers should follow from a simple rule. I did not find one.
- **The author did not confirm the guess.** He answered the reader who guessed "einhundert" on 31 October. He wrote that the puzzle is "relatively simple" and that no AI had come close. He said nothing about the word.
- **The hint is not explained.** I have no convincing path from "Pickende Hühner" to this word.
- **The hash cannot be checked.** It covers the author's full solution statement, and its wording is not public.

My own estimate is that the word is more likely right than wrong. That is a judgement, not a result.

## 6. Corrections and doubts

- **Ciphertext:** none. I used the 31 digits exactly as published and changed, skipped or re-read nothing.
- **Key:** all eight entries are inferred from the candidate word. None is confirmed from outside.

## 7. What is still open

- **The letter numbers.** What rule gives I = 1, U = 2, T = 11, H = 14, D = 16, R = 18, E = 20 and N = 24, and what are the numbers of the other letters?
- **The leading 3.** Block length is my reading. The author has only said it is not content.
- **The hint.** How "Pickende Hühner" points to the word.
- **A second regularity.** Divided by 13, every block leaves 1, 2, 3, 5, 7 or 11, that is 1 or a prime. For ten random numbers that happens about once in 2,300 tries. It may be part of the missing rule. The author is a factorisation record holder and says he knows the primes below 1000 "like the alphabet". It may also be chance.

## 8. Method

Everything was done with short Python programs and five public German word lists.

**What led to the candidate**

1. Setting the 3 aside leaves 30 digits for ten letters, so I cut them into blocks of three.
2. I tested the words named in the comments under the post. For EINHUNDERT, the blocks of the repeated letters differ by multiples of 26, as shown in section 5.
3. I then compared the pattern of equal remainders modulo 26 with every ten-letter word in the lists, to see how many other words fit.

**What I ruled out.** None of these produced a German word.

- **Alphabet order on the remainders.** Remainders for every divisor from 2 to 999, read with the alphabet in order, reversed, shifted or stepped, and with 29- and 30-letter alphabets that include the umlauts.
- **Sums of the digits.** Every weighted sum of the three digits of a block, taken modulo 26. That is 17,576 weightings.
- **Other properties of a block.** Quotients, digit sums and products, distances to squares and primes, counts and indexes of prime factors, and remainders for two or three divisors at once.
- **Order-preserving codes.** No word has letters in the alphabetical order that the sizes of the blocks would require.
- **Blocks of other lengths.** Cuts into ten pieces of one to seven digits, where each piece is a multiple, a square, a cube, a prime or a similar function of a letter number.
- **Fractions.** The blocks are not the first decimals of fractions with a common denominator.
- **One large calculation.** Neither the 31-digit number nor the 30-digit remainder is a product of small primes or a perfect power. The 31-digit number is 149 × 2621 × 2391064073 × 3373498928930597.
- **Formulas for every word.** For each ten-letter word, I tested whether the blocks are a low-order formula in the letter number and the place in the word.

**What I tried for the letter numbers of EINHUNDERT.** None fits all eight letters.

- **Formulas in the alphabet position.** Linear rules for every modulus up to 1,500, powers, exponentials, modular inverses, prime sequences, and several million small formulas. Polynomials are impossible in principle: E and R are 13 places apart in the alphabet, so any polynomial gives them the same remainder modulo 13, and their numbers do not have that.
- **Other orders of the alphabet.** Keyboard rows, columns and snake paths, phone keys, Morse code, letter frequency in several languages, vowels first, the alphabet written in grids and read by columns, diagonals or spirals, and counting-out orders.
- **Keyword alphabets.** Alphabets mixed with any of about 960,000 German words as keyword.

**The hash.** I hashed the candidate and every other ten-letter word in about 790 million short statement forms, such as "Das Lösungswort lautet …". None matched. The statement is therefore longer than a sentence around the word.

## 9. Sources

- **Ciphertext, prize and hash:** Klaus Schmeh, [Solve this puzzle from a world-class mental calculator and win 100 Euros](https://klausschmeh.net/can-you-solve-this-puzzle-from-a-world-class-mental-calculator-and-win-100-euros/), 16 October 2026.
- **Author's hints and the reader's guess:** the 14 comments under that post, read on 16 November 2026.
- **Background on the author:** [interview with Wenzel Grüß](https://mentalcalculation.org/wenzel-interview), and a dpa report of November 2012 on [news4teachers](https://www.news4teachers.de/2012/11/mag-keine-wurzeln-essen-ich-ziehe-sie-lieber/), which describes the 36-digit numbers he split into twelve three-digit primes as a child.
- **Word lists:** [davidak/wortliste](https://github.com/davidak/wortliste), [enz/german-wordlist](https://github.com/enz/german-wordlist), [creativecouple/all-the-german-words](https://github.com/creativecouple/all-the-german-words), [cpos/AlleDeutschenWoerter](https://github.com/cpos/AlleDeutschenWoerter) and the German list of [hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords).
