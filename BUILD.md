# Building _The Team from Turtle Bay_

_The Team from Turtle Bay_ requires a specific build environment, which you can create with Docker (the recommended way, and the way that the standard builds are produced through GitHub Actions) or manually.

## Building with Docker

```
git clone https://github.com/pmkielstra/EscapeIDSO
cd EscapeIDSO
docker build --tag 'make-turtle-bay' .
docker run --mount type=bind,source=.,target=/home/unprivileged/escapebuild --privileged make-turtle-bay all
```

Internally, the Docker container first switches to a non-root user called `unprivileged` and then runs the build process with `sudo`.  This is because `archiso` has to be run as root, but, if the files that it accesses are _owned_ by root, the resultant files on the generated ISO will be as well.  They will therefore not be accessible by the non-root accounts that the escape room participants will use.

Your built files and PDF docs are now in the `release` directory.  Due to the fact that the build process involves running `sudo` inside a `--privileged` container, they are owned by root.  You can fix this with a `chown`, or use a VM instead, as outlined below, and build in a shared folder.  Since the hypervisor will not be running as root, the files the VM creates won't be owned by root.

The main build time-sinks are (1) downloading all the packages and (2) compressing the image to build the ISO.  The former can be improved with a faster internet connection, and the latter automatically works in parallel and speeds up with more processors.  On a standard GitHub-hosted runner, it takes about 45 minutes to build all four.  (Building the documentation PDFs is very quick.)  Lilith is by far the fastest, so that's the one to use if you just want to test your toolchain.

If you want to build just the ISOs or just the docs, you can replace `all` with `isos` or `docs`.  Once you've built the docs, you can zip them together for easy distribution by replacing `all` with `zip-docs`.

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

2. As the non-root user, `git clone` and `sudo make all`.  Building on a VM is slower than building in Docker, and weaker VMs can take up to half an hour to build a single ISO.  Once again, the documentation PDFs should build quickly.

3. Your built files and PDFs are now in the `release` directory.
