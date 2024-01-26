#!/usr/bin/make -f

# Portions of this file contributed by NIST are governed by the
# following statement:
#
# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to Title 17 Section 105 of the
# United States Code, this software is not subject to copyright
# protection within the United States. NIST assumes no responsibility
# whatsoever for its use by other parties, and makes no guarantees,
# expressed or implied, about its quality, reliability, or any other
# characteristic.
#
# We would appreciate acknowledgement if the software is used.

# Purpose:
#
# This Makefile assists with local development, mimicking the test suite
# run as part of continuous integration.

SHELL := /bin/bash

PYTHON3 ?= python3

top_srcdir := $(shell pwd)

example_source_files := \
  $(wildcard case_mapping/*.py) \
  $(wildcard case_mapping/*/*.py) \
  example.py

all: \
  .venv-pre-commit/var/.pre-commit-built.log \
  case.jsonld

# This virtual environment is meant to be built once and then persist, even through 'make clean'.
# If a recipe is written to remove this flag file, it should first run `pre-commit uninstall`.
.venv-pre-commit/var/.pre-commit-built.log:
	rm -rf .venv-pre-commit
	test -r .pre-commit-config.yaml \
	  || (echo "ERROR:Makefile:pre-commit is expected to install for this repository, but .pre-commit-config.yaml does not seem to exist." >&2 ; exit 1)
	$(PYTHON3) -m venv \
	  .venv-pre-commit
	source .venv-pre-commit/bin/activate \
	  && pip install \
	    --upgrade \
	    pip \
	    setuptools \
	    wheel
	source .venv-pre-commit/bin/activate \
	  && pip install \
	    pre-commit
	source .venv-pre-commit/bin/activate \
	  && pre-commit install
	mkdir -p \
	  .venv-pre-commit/var
	touch $@

.venv.done.log: \
  .github/workflows/ci.yml \
  pyproject.toml
	rm -rf venv
	$(PYTHON3) -m venv \
	  venv
	source venv/bin/activate \
	  && pip install case-utils poetry
	source venv/bin/activate \
	  && poetry install
	touch $@
	
case.jsonld: \
  .venv.done.log \
  $(example_source_files)
	export CDO_DEMO_NONRANDOM_UUID_BASE="$(top_srcdir)" \
	  && source venv/bin/activate \
	    && poetry run python example.py \
	      > _$@
	source venv/bin/activate \
	  && case_validate \
	    _$@
	mv _$@ $@

check: \
  all
	source venv/bin/activate \
	  && poetry run pytest
