all: lilith.iso yichen.iso trevor.iso carol.iso

%.iso: ./% ./escape_base
	$(eval ESCAPE_OUT := $(shell mktemp -d))
	rm -rf ./escape_base/airootfs
	cp -R ./$(basename $@) ./escape_base/airootfs
	mkarchiso -w $(shell mktemp -d) -o $(ESCAPE_OUT) -v escape_base
	mv $$(find $(ESCAPE_OUT) -maxdepth 1 -type f | head -n 1) ./$@
	rm -rf ./escape_base/airootfs

%.pdf: ./docs/%.md
	pandoc -s -o $@ ./docs/$(basename $@).md