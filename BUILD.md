# Building _The Team from Turtle Bay_

Please don't try to build _The Team from Turtle Bay_.  It's an enormous hassle.

## But I want to!

OK, fine.

1. Set up an Arch Linux VM with the following:
   
   1. Several GB of RAM.  (Mine has 10, which I think is slightly overkill.)
   
   2. A user called `unprivileged` which is not `root` but does have `sudo` privileges.
   
   3. A custom package repo in `/home/unprivileged/pkgs` containing the packages `greetd` and `greetd-tuigreet`.
   
   4. The `archiso` and `pandoc-cli` packages installed.

2. `git clone` and `sudo make all`.  (Yes, this is weird, but `mkarchiso`, which is used to build the ISO images, needs to run as root.)  This can possibly take upwards of an hour per ISO, although each documentation PDF should build in just a couple of seconds.
   
   1. To just make the ISOs you can `make isos`, and similarly `make docs`.

3. Your built files and PDFs are now in the `release` directory.  You can distribute them however you like, or zip them for easy distribution with `make zip-release`.
