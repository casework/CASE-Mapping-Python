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

.PHONY: \
  check-mypy \
  check-supply-chain \
  check-supply-chain-pre-commit

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
  drafting.ttl \
  $(example_source_files)
	export CDO_DEMO_NONRANDOM_UUID_BASE="$(top_srcdir)" \
	  && source venv/bin/activate \
	    && poetry run python example.py \
	      > _$@
	source venv/bin/activate \
	  && case_validate \
	    --ontology-graph drafting.ttl \
	    _$@
	mv _$@ $@

case.ttl: \
  case.jsonld
	source venv/bin/activate \
	  && rdfpipe \
	    --output-format turtle \
	    $< \
	    > _$@
	source venv/bin/activate \
	  && case_validate \
	    _$@
	@# In instances where graph nodes omit use of a prefix, a 'default' prefix-base is used that incorporates the local directory as a file URL.  This is likely to be an undesired behavior, so for the generated example JSON-LD in the top source directory, check that "file:///" doesn't start any of the graph individuals' IRIs.
	test \
	  0 \
	  -eq \
	  $$(grep 'file:' _$@ | wc -l) \
	  || ( echo "ERROR:Makefile:Some graph IRIs do not supply a resolving prefix.  Look for the string 'file:///' in the file _$@ to see these instances." >&2 ; exit 1)
	mv _$@ $@

check: \
  all \
  check-mypy \
  case.ttl
	source venv/bin/activate \
	  && poetry run pytest --doctest-modules

check-mypy: \
  .venv.done.log
	source venv/bin/activate \
	  && mypy \
	    case_mapping \
	    example.py \
	    tests

check-supply-chain: \
  check-supply-chain-pre-commit \
  check-mypy

# Update pre-commit configuration and use the updated config file to
# review code.  Only have Make exit if 'pre-commit run' modifies files.
check-supply-chain-pre-commit: \
  .venv-pre-commit/var/.pre-commit-built.log
	source .venv-pre-commit/bin/activate \
	  && pre-commit autoupdate
	git diff \
	  --exit-code \
	  .pre-commit-config.yaml \
	  || ( \
	      source .venv-pre-commit/bin/activate \
	        && pre-commit run \
	          --all-files \
	          --config .pre-commit-config.yaml \
	    ) \
	    || git diff \
	      --stat \
	      --exit-code \
	      || ( \
	          echo \
	            "WARNING:Makefile:pre-commit configuration can be updated.  It appears the updated would change file formatting." \
	            >&2 \
	            ; exit 1 \
                )
	@git diff \
	  --exit-code \
	  .pre-commit-config.yaml \
	  || echo \
	    "INFO:Makefile:pre-commit configuration can be updated.  It appears the update would not change file formatting." \
	    >&2
