# Project directories
CWD := $(abspath $(shell pwd))
SRC := $(CWD)/src
OUT := $(CWD)/out
SRC_DIRS := $(wildcard $(SRC)/*)

# Define one output file name for each directory in src
TARGETS := $(addsuffix .pdf,$(subst src,out,$(SRC_DIRS)))
CUSTOM := $(SRC)/arrow-iii-northampton/custom/all_lists.html

# External directories
PANDOC=/usr/bin/pandoc
PANDOC_OPTIONS=--defaults ./pandoc/defaults.yaml
JINJA=/usr/bin/python3 ./render.py
RM=/bin/rm -f

.PHONY: all list clean
.SILENT: all list clean

all: $(TARGETS) $(CUSTOM)

list:
	@echo $(TARGETS) $(CUSTOM)

.SECONDEXPANSION:
$(OUT)/%.pdf: $(CWD)/css/checklist.css $$(wildcard $(SRC)/%/*.jinja) $(SRC)/%/data.yml | $(OUT)
	@echo $@
	@echo $(filter %.jinja,$^) | xargs -n1 $(JINJA) --data data.yml --template
	@$(PANDOC) $(PANDOC_OPTIONS) $(subst jinja,html,$(filter %.jinja,$^)) -o $@
	@$(RM) $(subst jinja,html,$(filter %.jinja,$^))

$(OUT):
	@mkdir -p $@

$(SRC)/arrow-iii-northampton/custom/all_lists.html: $(SRC)/arrow-iii-northampton/custom/all_lists.jinja $(SRC)/arrow-iii-northampton/custom/single_list.css
	@echo $@
	@/home/atrose/.local/bin/jinja2 --strict $(SRC)/arrow-iii-northampton/custom/all_lists.jinja $(SRC)/arrow-iii-northampton/data.yml -o $@

clean:
	- $(RM) $(TARGETS) $(CUSTOM)
