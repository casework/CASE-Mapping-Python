#!/usr/bin/env python3

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

import importlib

import case_mapping


def test_version() -> None:
    """
    This test confirms the package version is retrievable and non-null.
    """
    version_by_init = case_mapping.__version__
    assert version_by_init is not None
    assert isinstance(version_by_init, str)
    # Ensure the version matches the expected major.minor.build format
    assert len(version_by_init.split(".")) == 3

    version_by_metadata = importlib.metadata.version("case_mapping")
    assert version_by_metadata is not None

    assert version_by_init == version_by_metadata
