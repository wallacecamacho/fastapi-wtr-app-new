# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.

GENDOCS       = gendocs
GENDOCSCONFIG = mkgendocs.yml

# Put it first so that "make" without argument is like "make help".
help:
	@$(GENDOCS) -h

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(GENDOCS) --config "$(GENDOCSCONFIG)"
	echo $(call args, ${1})

.PHONY: docs
docs:
	@$(GENDOCS) --config $(config)
	echo "--config $(config)"
