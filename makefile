VPATH=release/isos:release/docs

all: isos docs

isos: lilith.iso yichin.iso trevor.iso carol.iso
docs: Checklist.pdf Technical.pdf Solutions.pdf Credits.pdf Intro.mp4

%.iso: ./individual_% ./base
	su unprivileged -c "mkdir -p release/isos"
	$(eval ESCAPE_PROFILE := $(shell mktemp -d))
	$(eval ESCAPE_BUILD := $(shell mktemp -d))
	$(eval ESCAPE_OUT := $(shell mktemp -d))
	./assemble_profile.sh $(basename $@) $(ESCAPE_PROFILE)
	mkarchiso -w $(ESCAPE_BUILD) -o $(ESCAPE_OUT) -v $(ESCAPE_PROFILE)
	mv $$(find $(ESCAPE_OUT) -maxdepth 1 -type f | head -n 1) release/isos/$@
	rm -rf $(ESCAPE_PROFILE)
	rm -rf $(ESCAPE_BUILD)
	rm -rf $(ESCAPE_OUT)
	chown `stat -c "%u:%g" release/isos` release/isos/$@

%.pdf: ./docs/%.md
	su unprivileged -c "mkdir -p release/docs"
	su unprivileged -c "pandoc -s -o release/docs/$@ docs/$(basename $@).md"

Intro.mp4: ./docs/Intro.mp4
	su unprivileged -c "mkdir -p release/docs"
	su unprivileged -c "cp docs/Intro.mp4 release/docs/Intro.mp4"

zip-release:
	su unprivileged -c "cd release; rm -f release.zip; tar -cf release.zip *"
