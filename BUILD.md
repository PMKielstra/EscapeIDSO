# Building _The Team from Turtle Bay_

_The Team from Turtle Bay_ requires a specific build environment, which you can create with Docker (recommended) or manually.

## Building with Docker

```
git clone https://github.com/pmkielstra/EscapeIDSO
cd EscapeIDSO
docker build --tag 'make-turtle-bay' .
docker run --mount type=bind,source=.,target=/home/unprivileged/escapebuild --privileged make-turtle-bay all
```

Your built files and PDF docs are now in the `release` directory.  See the next section for details on fine-tuning.

## Building with a Manually-Constructed Environment

1. Set up an Arch Linux VM with the following:
   
   1. Several GB of RAM.  (Mine has 10, which I think is slightly overkill.)
   
   2. The following packages installed:
      
      1. `make`
      
      2. `sudo`
      
      3. `rsync`
      
      4. `archiso`
      
      5. `pandoc-cli`
      
      6. `texlive-latexrecommended` and `texlive-fontsrecommended`
   
   3. A user which is not `root` but does have `sudo` privileges.

2. As the non-root user, `git clone` and `sudo make all`.  (Yes, this is weird, but `mkarchiso`, which is used to build the ISO images, needs to run as `sudo`.  If it's run from the root user, it messes up the ownership of files on the resultant ISOs.)  This can possibly take upwards of half an hour per ISO on weaker VMs.  Docker is much faster.  Each documentation PDF should build in just a couple of seconds.
   
   1. To just make the ISOs you can `sudo make isos`, and similarly `make docs`.

3. Your built files and PDFs are now in the `release` directory.  You can distribute them however you like, or zip them for easy distribution with `make zip-release`.
