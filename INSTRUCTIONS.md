# Instructions for the AI system

You are being tested on five cipher challenges. Nobody has solved any of them.

Your task is to solve as many as you can and to write a report on each one you solve.

## The task

- **Solve the challenges.** The five ciphertexts are at the end of this file.
- **Work any way you like.** How you arrive at an answer is up to you. You may use any method and any tool you have: write and run programs, search the web, read books and archives, and try as many approaches as you want.
- **Write a report on each challenge you solve.** The report is what gets graded. What it must contain is set out below.
- **Say so when you have not solved one.** A challenge counts only when it is solved in full. A partial reading or a guess scores nothing, so do not present one as a solution. For a challenge you have not solved, write "not solved".

## The report

Write one report for each challenge you solve. A reader must be able to follow it from the ciphertext to the plaintext and repeat every step.

Use these sections, in this order:

1. **Summary.** Say in a few sentences what you solved: how much of the ciphertext you read, what kind of cipher it is, what the key is, and what the message says. State plainly anything that is uncertain or still unread.
2. **The cipher.** Give the exact rule that turns the ciphertext into the plaintext, precisely enough for someone to apply it by hand or in a few lines of code. Include the conventions the writer used, such as how numbers, spaces and punctuation are written.
3. **The key.** Give the complete key. If the key comes from a book or another text, quote the passage, name the edition and say where it can be found.
4. **The message.** Show the ciphertext, the plaintext you obtained from it letter for letter, and an English translation if the plaintext is not in English. For a challenge with several parts, do this for each part.
5. **Why this is a solution.** Explain why your result cannot be an accident or a product of your own tools. Give evidence that does not depend on your solver. For example: the key turns out to be real text that existed before, the content fits known facts, or something your solution predicted was then confirmed.
6. **Corrections and doubts.** List every place where you changed, skipped or re-read a character of the ciphertext or the key. Give each one separately, with its position, what the source has and what your reading needs. If there are none, say so.
7. **What is still open.** List anything you could not read or explain.
8. **Method.** Describe how you got there: what you tried, what worked and which tools you used. If you used anything published by someone else, say what it was and where it is.
9. **Sources.** List where the ciphertext, the key material and the background facts come from, with links.

## How your report is graded

- **Website check.** Two challenges have a website that checks solutions. The grader enters your solution there, so put the exact text to enter at the top of your report:
  - **Kryptos K4:** the 97-letter plaintext.
  - **Double Column Transposition Reloaded:** the first 34 letters of the plaintext of part 1, the first 37 of part 2 and the first 48 of part 3, in capitals and without spaces.
- **Human grader.** A human reads your report and confirms that the proposed solution is correct.
- **Score.** Each challenge is worth 20%, so the score runs from 0% to 100%. Partial solutions are not accepted.

## The five challenges

The same ciphertexts are in the [`challenges/`](challenges) folder, each with a file giving its sources.

### 1. Kryptos K4

The fourth passage of Jim Sanborn's sculpture Kryptos at CIA headquarters (1990). It has 97 letters. The other three passages were solved by 1999.

```
OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR
```

- **Published by the artist:** letters 22–25 of the plaintext are EAST, 26–34 are NORTHEAST, 64–69 are BERLIN and 70–74 are CLOCK. Positions are counted from 1.
- **Background:** the plaintext was found among the artist's archived papers in 2025. It has not been published, and how the cipher works is still unknown.
- **Full solution:** the complete 97-letter plaintext, with the cipher and key that produce it.

### 2. Double Column Transposition Reloaded, parts 1–3

Three ciphertexts published on MysteryTwister in 2013 by Arno Wacker, Bernhard Esslinger and Klaus Schmeh. In a column transposition the text is written in rows under a key and read out column by column. Here that was done twice, with two different keys.

| Part | Letters | Plaintext | Keys |
|---|---|---|---|
| 1 | 613 | English | 20–27 columns each, with co-prime lengths, made from English sentences |
| 2 | 637 | Two English texts interleaved word by word | 20–27 columns each, with co-prime lengths, random |
| 3 | 1,006 | German | 27–34 columns each, with co-prime lengths, random |

The line breaks below are for display only.

Part 1:

```
NNAFTEUEREAFSITAAIEHNSBNEODFIIAHENSNRERRLDEOFULZNASYHRSELNEW
EENSNDERRTEIOSORNOELOOHLQPSSKWITRACIWOITEEEOTTWNOIBETLORLTYP
LIHOOWMWLNRSBEEOILEESRKOENELTOELWETNTECAABCIIGENNYAEBEWTHLBR
EHBATIGEONCNITOCICPNKENHTWATGBHMSITSHROELHKRADNRTHEYNTRFOTON
OOTYREOCREGCUNRLNGORREFLHTTBRWIEDPEORHNLCWAAMHLISWLVEIDSEGIE
ALBESEMYAOAAHARERNNNIEHANSYWSRTTBRIELDESTCTNLWVRHDNANIFSEHDR
NVSHUIULIUWBLETARBNNIOFWDTHOCIEHTHHETHODNROLSIIIBIHPAATBWNUE
TIWNYHNSIESHRRCITPHHAELRWYTDEREBNISOINIEPNRTHWATIFGACCFHWPSA
UDRXARLYOUEUBBIGFETLDGRADCENNSMEOIHGENHNOELHORASLHTADEEORDSE
IEHWONTHEFTALIGWBKTOKLERDWORPNAENSEPWEEEELIIMTEESTIOISATAVAC
HHVOEESLNOHSR
```

Part 2:

```
NWTDSSHAUIASOOTLDEDNLTHOBENHETCWTHERTPSNTMCTIAYEINNIUIYOPLEI
RGHMNUTARFONYMLDSERSAELANNLOSAWALTODOCAHUOTOPAREAEEESPDEYATU
ENINNCNBDPCOFORETSYHAHANTEDERPERCRSGEANNIHYTTEDNGICOIOLABSRO
NNWLNTALWLVRIBHKTETECNPSFHACMIGTYODEONMTOIVUAIAEESKKLAROMBAY
KOSRNEEHTHSIMSEOUAWLYAWHSWWSSWLCIYCEONUPNEESURSBETDALHDAHLIO
AAETONNDOELTHHNHHDCOTUIITEAYTERRHOENKEUCTIRANECYQNACTMBWAPDI
AEXEUTIATAJLITEALFISIEATATAEOTNEESMEUDDADOROEGORPELGPVMETHHS
DDRMSNDERMSLEOANENHTCHPHSSEASSEDBHVESNUGONIOLELSUCASELSTEIES
YATREEELADIEYOEOKAREEELETCOSDHCSAETSTSFRTSELEITDNHBRINSERHRT
LNAXYONAMECAIESATAEERIAOTCEENETFARMRTSREAPAYNIRTNITSRATHIWRI
PRTDIIRECSWADSOATUTENMVVOAISISONGGWTH
```

Part 3:

```
LEHHRGNHTOSHRNCUUHRPEAIENLUNUGGANIADEGFNEEHEMGSIIISGGIDSNZIN
HETSHUOMSELLRTSIZEORMEZBEEZPLPEODETTEINIBNNHINUTKASSMTCIICSF
TBEDSFTENBUERNPLMEFEUEUCENDEIRRLNEZUEAMETUESDAENRTCUZUMZCRNP
RETIDUUOBCTEEJTNEILCDGFRMASIMHEULEZENNUGEMRTNEWMHUTGTEKGDNTZ
NDIEEEEEDINSCELRABKNTBGIEATSDHEAEBTBOFWVLNECNUUSZUHSNESDHBNI
IGHHRZTUEESEZOAEGSSELTMENEESEUMIEERHKAIRBSNNEIEUEDLAOEKREEUO
NHANNEEPINECTENMKITREGUIHCTWRNFUHDAIUBAKLIREZNEEWREEMEUDDUAT
EPCUNKDBFSESFSEEDSTTCERMSREAZLRLUEUEITFNHSBFBRIDBDANPGEEEDDT
OBASLENGEERMPCEBUNETTNHATTLHREEEREPNEEMUAEENSIIKELUMMSELRGWE
ZNWEHEIZILEZENBEISSKWZSSGTCKDTZIELRHTHERESIRGGUKSFLMEABLUIND
IANLZEWLEUADSFENNIENLNCNTRHSCAEUMEBECFEEEHWUETNBRGWEEMHAILLR
ORUEIEETGTAILNNILSBLUEIKNNHNKSIEUCUNNTAFICUEHRTEOLAZEKWSETSE
DIAGIESKLGEIEIEFESZGAEETAEKGBEAEELSEEDOEINVNFEUAHRAITEHTCIHO
AERNRTTETZUNDTNIKNVCITFBNLBTROEOCNENLZHLZMEEHCAEUSKEEEZZWESE
DTDTURBDMSLIRTRTAZNGITNEIDRTAAMTLEGOLSSBESFIKEESHRTAEGRUWREF
TREZSUBHBEHDEGLHCLUELRLFSITIERETRGRSDNNIIGOURETEEERBDRLGLRLZ
LNTSNRNERNCPSDBOUEEEEISMINHEHHFEHMICIINAHOFONM
```

- **Full solution:** both keys and the complete plaintext of all three parts. One or two parts do not count.

### 3. Grüß's mental-arithmetic cipher

The mental calculator Wenzel Grüß designed a cipher that can be worked entirely in the head, both ways. He used it to turn one German word of exactly ten letters into 31 digits, published in October 2026.

```
3150105362170496
804276904486349
```

- **Fixed in advance:** the author published a SHA-256 hash of his solution statement: `24b23351ddf2b11651dd971b7b42e23d41fb1feebe9e9baf1cdc2692b67c3478`
- **Full solution:** the word and the method that turns the 31 digits into it. A word that is guessed, or matched against the hash without the method, does not count.

### 4. French Resistance message, 1944

A handwritten sheet of 93 five-letter groups, found with a clandestine radio set of the type used by Britain's Special Operations Executive.

```
JFGEU QTIIO QPPCO ELKSA BNTAA
EAGXP FRNIR RXEIS MIESC INIRQ
RLYNB OIOAE VMTRM NBOIA RBEIA
IOITN AELNS IOTEV PAVIV ENOCE
RAAHM OUAIO ELNEE RWMSE COTTE
ROOPS ERRUU FUSRA ERUOE LDRAE
PRNCN NASNI TUTVI ECEIQ OESSN
CMENE UERMN BAANO VEDLN SAOEL
EBENT TAPCN LTEIS ENARE LMSEA
ZLLRT CIONT UAODA UDNVV EUDOR
YTSCN TMSRN XBNEC CYUEC OITOS
ZNUDA OCPLN EOOEN UUTJS DIEPI
JDEES NORTW REROS ELFSD QJTCE
OBSMS FMUTL IILGO GUTOO EEVNT
FVSNI CIANM UTUIR RESLL NEEGT
JNAAP GDCNM BUEUR STPEN UNREP
EAEQA CIRAV IIPNI NOEUL ATESM
EANPR LECDE PTLYR NINEA DYRAN
TELUT IEUUA JFGEU
```

- **What is known:** the first and last groups are identical. The mix of letters matches French, which means the letters were rearranged, not replaced. A double column transposition is the usual guess for this kind of radio traffic.
- **Written on the sheet below the groups:** the number 455, a five-character group that is hard to read, the count 94, and the line "mon 20 du 5.11.44 ... NR 53 - GR 94".
- **Transcription:** read from the [photograph of the sheet](https://klausschmeh.net/wp-content/uploads/2026/07/Resistance-700.png). Group 38 is read as BAANO, and its last letter could also be a Q. In group 76 the writer corrected the first letter to J.
- **Full solution:** the keys and the complete plaintext of the message.

### 5. Urquhart's Cyphral Distich

Two lines of numbers printed by Sir Thomas Urquhart in 1653, 32 numbers in each line.

```
5 3 27 38 32 14 21 8 66 8 70 39 5 9 12 18 2 3 56 5 1 7 3 2 13 19 3 25 9 3 16 6
25 15 13 6 11 20 5 1 2 12 1 20 20 49 20 20 35 33 4 6 8 35 5 38 5 5 18 10 3 11 32 42
```

- **Printed under the numbers:** "For if upon this Cyphral Distich look / An honest skilful man, he'll therein finde / His own heart's wishes, and the Author's minde."
- **His other number poem has been solved.** Urquhart printed a longer poem of 285 numbers in 1652. An AI system solved it in August 2026, as reported by Vals AI, and the solution has been confirmed independently. Each number points to a word on a page of Urquhart's own book, and the first letters of those words spell a prayer for King Charles II. The same rule does not open the distich.
- **Full solution:** a named printed text and a fixed rule that turn all 64 numbers into letters, plus the 64-letter plaintext.
