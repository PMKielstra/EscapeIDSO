VPATH=release/isos:release/docs

all: isos docs

isos: lilith.iso yichen.iso trevor.iso carol.iso
docs: Checklist.pdf Technical.pdf Solutions.pdf

%.iso: ./% ./escape_base
	mkdir -p release/isos
	$(eval ESCAPE_BUILD := $(shell mktemp -d))
	$(eval ESCAPE_OUT := $(shell mktemp -d))
	rm -rf ./escape_base/airootfs
	cp -R ./$(basename $@) ./escape_base/airootfs
	mkarchiso -w $(ESCAPE_BUILD) -o $(ESCAPE_OUT) -v escape_base
	mv $$(find $(ESCAPE_OUT) -maxdepth 1 -type f | head -n 1) ./release/isos/$@
	rm -rf $(ESCAPE_BUILD)
	rm -rf $(ESCAPE_OUT)
	rm -rf ./escape_base/airootfs

%.pdf: ./docs/%.md
	mkdir -p release/docs
	pandoc -s -o ./release/docs/$@ ./docs/$(basename $@).md