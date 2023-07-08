FROM archlinux:latest

RUN pacman --noconfirm -Sy make sudo rsync archiso pandoc-cli texlive-latexrecommended texlive-fontsrecommended

RUN useradd -ms /bin/bash unprivileged
RUN usermod -aG wheel unprivileged

# Enable sudo without password -- you can't run mkarchiso as root without messing up file permissions
RUN echo "unprivileged ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/10-aaa

USER unprivileged
WORKDIR /home/unprivileged

RUN mkdir escapebuild
WORKDIR /home/unprivileged/escapebuild

ENTRYPOINT ["sudo", "make"]

