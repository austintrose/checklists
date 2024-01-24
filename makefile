# External directories
PANDOC=/usr/bin/pandoc
PANDOC_OPTIONS=--defaults ./pandoc/defaults.yaml
JINJA2=/home/atrose/.local/bin/jinja2 --strict --format=yaml
RM=/bin/rm -f

.PHONY: all list clean
.SILENT: all list clean

all: RENDER.html

RENDER.html: checklist.css checklist.jinja.html data.yml
	@$(JINJA2) checklist.jinja.html data.yml --outfile=RENDER.html
# @$(PANDOC) $(PANDOC_OPTIONS) checklist.html --output=$@

clean:
	- $(RM) RENDER.html
