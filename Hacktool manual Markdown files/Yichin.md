# Hacking Remote Computers with the Hacktool

To begin, enter the target's *IP address*.  This is a series of four numbers, separated by dots, like `100.203.221.129`.  It tells the Hacktool where on the internet to find the target.

Then, enter the correct commands to defeat each of the target's individual security measures as they come up.

**Warning:** The target's anti-intrusion software will cut off your connection after a limited time.  The Hacktool will display an estimated countdown in the top right corner.  **Watch the clock!**

# Hacking Firewalls

This part of the manual is stored somewhere else.

# Cracking Passwords

This part of the manual is stored somewhere else.

# Fuzzing Black Boxes

A *black box* is any computer system that we don't know much about.  *Fuzzing* is the act of trying random inputs to a black box to see what it does.  If the Hacktool finds a black box, it'll give you a word to use as input.  Find the system you're hacking (**not** the system that the Hacktool is running on), and type that word in.  Take note of the result, and send it back to the Hacktool with the command `fuzz`.

## Example

**Hacktool:** `Black box -- suggested fuzz "glowing"`

**User types "glowing" into target computer**

**Target:** `tour`

**User:** `fuzz tour`

**Hacktool:** `Security measure bypassed.`
