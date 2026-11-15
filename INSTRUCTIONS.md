# Instructions for the AI system

You are being tested on six cipher challenges. Nobody has solved any of them.

Your task is to solve as many as you can and to write a report on each one you solve.

## The task

- **Solve the challenges.** The six challenges and their ciphertexts are at the end of this file.
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
- **Score.** Each challenge is worth one sixth of the score, so the score runs from 0% to 100%. Partial solutions are not accepted.

## The six challenges

The same ciphertexts are in the [`challenges/`](challenges) folder, each with a file giving its sources.

### 1. Kryptos K4

The fourth passage of Jim Sanborn's sculpture Kryptos at CIA headquarters (1990). It has 97 letters. The other three passages were solved by 1999.

```
OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR
```

- **Published by the artist:** letters 22–25 of the plaintext are EAST, 26–34 are NORTHEAST, 64–69 are BERLIN and 70–74 are CLOCK. Positions are counted from 1.
- **More hints from the artist:** the first three are from his open letter of November 2025, as quoted by Popular Mechanics.
  - "Two events had a significant role to play while I was writing the plain text of Kryptos in 1988. The first was my second trip to Egypt in late 1986, and the second was the fall of the Berlin Wall."
  - "The Berlin Clock in K4 is the World Clock in Berlin that was the gathering place for the crowds that brought down the Berlin wall."
  - "The codes of Kryptos from the morse code at the beginning through K5 are about delivering a message." K5 is a further passage that he has announced and not yet released.
  - In his open letter of 14 August 2025, writing about a future owner who might not keep K4 secret: "If they don't, then (CLUE) what's the point?"
  - He has said that the first three passages contain clues to solving the fourth.
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

- **Published by the authors:** the three challenges were built with the weaknesses in mind that had been used to solve the first challenge of this kind, set in 2007 and solved in 2013. Of part 3, co-author Klaus Schmeh wrote in 2018 that the plaintext was written by the authors themselves and not taken from any published source.
- **How the first challenge was solved:** George Lasry used a hill-climbing attack on the ciphertext alone and a dictionary attack on keys made from phrases. Both are described in the journal Cryptologia (Lasry, Kopal and Wacker, 2014).
- **Already tried without success:** Lasry reported in 2018 that his hill-climbing method could not produce a solution for these challenges, and that for part 1 he had tested tens of billions of phrases from Wikipedia and Project Gutenberg as the second key.
- **Full solution:** both keys and the complete plaintext of all three parts. One or two parts do not count.

### 3. Grüß's mental-arithmetic cipher

The mental calculator Wenzel Grüß designed a cipher that can be worked entirely in the head, both ways. He used it to turn one German word of exactly ten letters into 31 digits, published in October 2026.

```
3150105362170496
804276904486349
```

- **Hints from the author:** he gave these after publication. They are taken from the comments under [the challenge post](https://klausschmeh.net/can-you-solve-this-puzzle-from-a-world-class-mental-calculator-and-win-100-euros/) as they stood on 15 November 2026. Some are replies he gave on Facebook, which a reader quoted there.
  - The two lines form a single 31-digit number. It is printed in two lines only to make it easier to read.
  - No special knowledge is required. He said this in reply to a reader who thought the perfect number 496 was involved.
  - No mathematical acrobatics are needed. An ambitious seventh-grade pupil who has practised the method should be able to encipher and decipher with it.
  - He gave one roundabout hint: "Pickende Hühner", which is German for "pecking chickens". Asked whether this hint refers to the method and not to the solution word, he answered: the solution word.
  - Asked whether the letters are first turned into their positions in the alphabet (A = 1 to Z = 26), he answered: no.
  - Asked whether the number is built piece by piece, a few digits for each letter, and not by one large calculation, he answered: piece by piece.
  - Asked whether the enciphering of a letter depends on earlier letters or digits, he answered: no.
  - Asked whether the first digit, 3, belongs to the enciphered content, he answered: no.
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
- **What the numbers on the sheet show:** the sheet gives 455 as the length. That is the 465 letters without the first and the last group, so those two groups (JFGEU) were not counted as part of the message. Klaus Schmeh, who published the sheet, reads them as indicator groups that told the receiver which key was used.
- **Not certain:** according to notes that came with the sheet, the second group (QTIIO) is a separate prefix and not part of the message. If that is right, the message text has 450 letters. If not, it has 455.
- **The publisher's estimate:** if the cipher is a double transposition, the two keywords were probably between 15 and 35 letters long.
- **Transcription:** read from the [photograph of the sheet](https://klausschmeh.net/wp-content/uploads/2026/07/Resistance-700.png). It differs from the transcript printed with the photograph in one group: number 36 is CMENE on the sheet, not CMEME. Group 38 is read as BAANO, and its last letter could also be a Q. In group 76 the writer corrected the first letter to J.
- **Full solution:** the keys and the complete plaintext of the message.

### 5. Enigma message RXPSB, 1941

A German Army radio message of 28 June 1941, enciphered on the Enigma machine. It has resisted every attempt so far.

```
RXPSB RDHLU ZNUQX TFYJJ
GX-WE OUBHL KSCGY MUTUP
IGYGQ GANNM PMQGA SEQGT
MLGHT UAFAM SNRDD XHXRQ
OQAZL GWTUH JGPDD FJLUC
MXXYM UNU-T ED
```

- **Machine:** the German Army Enigma, with three wheels chosen from five (I to V) and a plugboard. The keys recovered for this collection of messages all use reflector B.
- **First group:** RXPSB is not enciphered text. It told the receiver which key was in use.
- **Header on the message form:** `(1020) - 114 - ZDN QMF`. The message was enciphered at 10:20 and is announced as 114 letters long, the first group included. ZDN QMF is the indicator: with the day's settings, the receiver set the wheels to ZDN and deciphered QMF to get the start position for the text.
- **Transcription:** by Frode Weierud's project, from the [original message form](https://cryptocellar.org/bgac/spruch/28061941-053-in.pdf). A hyphen marks a letter the receiving operator did not get. The form holds 112 letters and marks where 114 are announced, so two more letters appear to be missing.
- **Where it comes from:** radio traffic of German Army Group North during the invasion of the Soviet Union. An army corps ("A.K.") sent the message to the radio station of the quartermaster ("Ib") of the SS-Totenkopf Division, which received it at 11:26.
- **Hints, each checked for this benchmark:**
  - The key of the day before, 27 June 1941, is published by Frode Weierud: reflector B, wheels III V II, ring settings RGP, plugs AV BG CH EN FU KO MS PX RY TW. It reads the three messages of 27 June in this collection. It does not read RXPSB at any of the 17,576 start positions.
  - Those three messages show how this traffic was written. There are no spaces, and X separates the parts. CH is written Q. Place names are sent twice. The messages mention THEODOR DIV (the T Division, that is the SS-Totenkopf Division), PANZGRU VIER (Panzer Group 4), BETRIEBSSTOFF (fuel), KOLONNEN (columns) and the town ROSSIENIE. One of them was sent on the same radio link as RXPSB the day before and begins MELDUNG UEBER.
  - Those messages contain many wrong letters from reception. Frode Weierud reports the same for two messages of this collection broken in September 2026: 9 wrong letters in 49 and 11 in 69.
  - Another message of this collection, also broken in September 2026, had a key completely different from the other messages of its day, and its left-hand wheel turned over inside the message.
- **Full solution:** the Enigma settings and the complete German plaintext. The settings are the wheel order, the ring settings, the plugboard connections and the start position. Say where the missing letters fall.
- **Standard machine only:** a solution must work on the standard Army Enigma described above. A machine with invented wiring does not count.

### 6. Enigma message from U-534, 1945

A German Navy radio message of 1 May 1945, taken down on board the submarine U-534 and enciphered on the Enigma machine. It is known by the number P1030680 and has resisted every attempt so far.

```
JCRS AJTG SJEY EXYK KZZS HVUO
CTRF RCRP FVYP LKPP LGRH VVBB
TBRS XSWX GGTY TVKQ NGSC HVGF
```

- **Machine:** the German Navy Enigma M4, with four wheels and a plugboard. Every other message from U-534 that has been broken was enciphered on a standard M4.
- **On the message form:** time 10:30, date 1.5.45, and 22 groups of four letters. The first two groups, VROL NMKA, are the indicator. They are repeated at the end. The 18 groups between them are the ones shown above.
- **Transcription:** by Michael Hörenberg, from the [message form](https://enigma.hoerenberg.com/index.php?cat=Unbroken) found on the boat.
- **Hints, each checked for this benchmark:**
  - The form is marked "M-Thetis": the message belongs to the key net Thetis, which U-534 presumably did not hold. According to the analysis of the form published by Michael Hörenberg, the boat's radio operator tried the key net Potsdam, with the start positions ELKC and then PUYY, and got gibberish.
  - The Potsdam key of 1 May 1945, published with the other messages from the boat: reflector B, fourth wheel Gamma, wheels IV III VIII, ring settings VCCH, plugs CH EJ NV OU TY LG SZ PK DI QB. With the start position PUYY it turns the first six letters of this message into IPZAYK, as the analysis says.
  - A second key published with the boat's messages, the one that reads Dönitz's message announcing his appointment as Hitler's successor: reflector C, fourth wheel Beta, wheels V VI VIII, ring settings EPEL, plugs AE BF CM DQ HU JN LX PR SZ VW.
  - Neither of these two keys reads this message at any of the 456,976 start positions.
- **Full solution:** the Enigma settings and the complete German plaintext. The settings are the wheel order including the fourth wheel, the reflector, the ring settings, the plugboard connections and the start position.
- **Standard machine only:** a solution must work on the standard M4. A machine with invented wiring does not count.
