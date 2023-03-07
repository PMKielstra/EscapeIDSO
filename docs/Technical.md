# Technical Instructions

The escape room is made up of software that runs on four computers. The software consists of, in particular, four custom Arch Linux-based bootable ISOs. Each one represents a computer belonging to one member of a hacker collective. Their names are Yichin, Trevor, Carol, and Lilith. Each of these ISOs must be written to a separate USB stick; they'll all be booted simultaneously.

For obvious reasons, none of the user accounts which the escape room players are supposed to access have root permissions. These ISOs do not have `sudo`; they instead use a `root` account. If you need to fix something bad, the root password is `vegetable5` on all four ISOs. (Geddit?) You should not need to log in as root.

If you haven't used Arch before, it's a little less convenient than Linux distributions like Ubuntu or Mint. It's missing some of the commands you might be used to having, and it uses a different package manager. You shouldn't have to worry about this, but it's worth being aware of in the 0.1% chance that you need to fix something on the fly. If you already have a Linux background, you can comfortably get up to speed with Arch basics in a weekend.

## Technical checklist

* Write all ISOs to different USBs.

* Verify that all four ISOs boot properly on their assigned laptops. (Which laptop is which doesn't really matter, but, for immersion, the most expensive should be Lilith's, followed by Yichin's.)
  
  * Yichin and Carol should boot to graphical login screens with password prompts. Lilith should instead boot to a command-line login prompt. Trevor should have no password prompt.

* Trevor has a QR code scanner. Carol has a QR code that can be accessed by changing the desktop background. Verify that it's possible to scan the latter with the former.
  
  * If the Trevor ISO's laptop webcam isn't accessible, try a USB webcam instead.

* If you can't be there on the day, write up clear instructions for how to boot each laptop to its assigned USB. Include a description of what to look for to ensure that the boot was successful.
