# Hints and Walkthrough

This document provides general hints, some specific hints for each puzzle, and full solutions.  They may not be the optimal hints.  Read them ahead of time and make such changes as you feel necessary based on your target audience.

It goes without saying that this is entirely spoiler territory.

## General Hints

* Aside from scanning one QR code, you'll never need to move a laptop -- or, indeed, do anything other than typing on one.

* There are plenty of text files around for a reason.  Typing in notes is encouraged.

* The laptops are missing most of the software you would find on a home computer.  This is by design.  You have everything you need.  Don't worry if you can't find a browser or an office suite.

* You shouldn't be able to break anything by clicking around, as long as you don't do something obviously silly like deleting files without knowing what they do.

* If all else fails and you break things horribly, turn off the relevant computer and boot it from the ISO again.  That will reset it to the state it was in at the beginning of the game.  Immersion goes out the window but at least you have a chance to solve all the puzzles.

## Specific Hints and Solutions

### What do I do first?

* Take stock of the situation.

* Two computers look different to the others.  How?

* One has a weird text-interface prompt.  One doesn't require a password.

* **Solution:** Click through to log into the computer that doesn't need a password.

### How do I log in to Lilith?

* Read the `Chat log 001` text file.

* Apparently Trevor put the password in a "big fat PDF on his desktop."  Can you find a PDF on the desktop?

* There's a PDF, but it's just covered in weird symbols.  Try to select the symbols.  Could they just be text in a different format?  Is there an obvious way to strip formatting from this sort of thing?

* **Solution:** Open the `Password1` PDF on Trevor's desktop and copy/paste the contents into a text file.  (You can get one by opening the `Chat log 001` file.)  That will give you the password to Lilith, which is `mesopotamia`.

### Am I here to kill Lilith?  Should I tell her so?

* **Solution:** Yes.

### How do I find Carol's security answer?

* Trevor made her a puzzle.  Read `Chat log 002` on his machine.

* Lima is the geographic capital of Peru.  But there isn't a LIMA in the puzzle map.  What else could be the capital of Peru?

* There's only one "capital of Peru" in the puzzle map.

* **Solution:** The capital of Peru is the letter P.  There's only one P.  Start on that letter and go up (north).  The only city you find that starts along that path is Lexington.  Tell that to Lilith and she'll tell you that Carol's password is `eos5d`.

### Where's the hidden code on Carol's computer?

* Look at her desktop icons.  Is there anything strange about them?  Anything you haven't seen before?

* She's got an option to change her desktop background.  It might be worth seeing what backgrounds she has available.

* One of them (the one with the red gradient) looks kind of funky.  Where have we seen that sort of pattern before?

* **Solution:** Set Carol's desktop background to the one with the red gradient and the QR code in the bottom right, then scan it with Trevor's laptop.  The word is `hobbledehoy`.

### How do I decode Yichin's password from `Chat log 003`?

* Yichin is flexing on Carol and Trevor by proving that she can write things in their code.  Check the other two chat logs: the encoded word is `noobs`.

* Carol and Trevor's jobs seem to involve a lot of typing, and they communicate via online chat.  It seems reasonable that they'd make up a code involving keyboards.

* Try starting from the top left of the keyboard.  Go right, then go down.

* **Solution:** The numbers represent distance from the letter Q.  The first letter is the horizontal distance; the second is the vertical.  D would be 2/1, because it's two across and then one down (diagonally).  The password is `boulder`.

### How do I find the master key on Yichin's computer?

* Lilith says it's in a maze.  Does the `Maze` folder have any files that look different?

* `0000 READ ME FIRST` tells you to hack `127.0.0.1`.  There's a hacking manual and a shortcut to launch the hacktool on Yichin's desktop.

* Where else have you seen hacktool manual pages before?

* **Solution:** Hack `127.0.0.1`, using the information from Trevor's hacktool manual.  It will tell you that the correct file from the `Maze` folder to look at is `0258`.

### How do I find Yichin's part of the master key?

* As explained in the maze document, hack `192.168.2.32`.  You'll need both Trevor's and Carol's manual pages.
* **Solution:** `942`.

### How do I find Trevor's part of the master key?

* Look at Trevor's desktop.  What haven't we used so far?

* Open the `Number Mangler` folder and `NumberMangler.py`.  Trevor is apparently using this to determine "a secret number, for a thing."

* You don't just need to fix the number mangler; you need to figure out what number broke it in the first place.  (There was only one.)

* **Solution:** Looking through the number mangler code, nothing seems out of place until we reach `x = 12 / x`.  This can go wrong if `x` is zero, because division by zero is impossible.  So, what value input would be mangled to `0` by the time it got to that line?  We can work backwards to get `-10`.  The rest is simple: remove the line `x = 12 / x` (or put a `#` symbol at the start of it), run the code, and enter `-10` when asked for a number to mangle.  The output is exactly `2`.

### I've messed up the number mangler code!  What do I do?

* **Solution:** There's an uneditable (PDF) backup provided in the same folder.  You can copy and paste from it as many times as you want.

### How do I find Carol's part of the master key?

* Take the photo quiz on Carol's desktop.

* For the first two questions, look at the direction of the shadows.

* For the third and fifth questions, look at the prevalence of clotheslines.  For the fourth question, look at the width of the streets.

* **Solution:** The shadows point northeast, so the sun is in the southwest.  That makes it afternoon (first question) and the northern hemisphere (second question).  There are clotheslines everywhere and glass roofs, so yes, sunny days are presumably common here.  The roads are narrow and the buildings are large, so people here probably don't drive much.  Once again, there are loads of clotheslines, so we can't say most people here dry everything electrically.  The correct answers are, in order, `2`, `1`, `1`, `2`, and `2`, and the final number is `25`.

### How do I enter the master key?

* The correct formatting is given in Yichin's note from the maze.

* Put the numbers together in the order Yichin-Trevor-Carol, with single dashes in between.

* **Solution:** Type `942-2-25` into Lilith and press enter.

### Lilith is evil now?

* **Solution:** If she's even Lilith any more.

### How do we stop her?

* Wait long enough and she'll make one fatal mistake.

* She tells you her IP address.  What have you been able to do with IP addresses?

* Go back to Yichin's computer and hack `102.153.223.125`.  You'll need all three of the manual pages.  When it says to fuzz something, just type that word into Lilith as if you were talking to her.  She'll respond with another word, and then you just type `fuzz <that word>` into the hacktool.

* **Solution:** Hacking Lilith reveals that the self-destruct code is `MAIMONIDES`.  Enter that into Lilith's prompt, press enter, and enjoy your victory.
