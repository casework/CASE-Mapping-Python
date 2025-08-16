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

"""
This module includes tests for JSON-LD RDF-type interpretations of native JSON types.
"""

import json
from typing import Union

from rdflib import XSD, Graph, Literal, Namespace

JSON = Union[dict[str, "JSON"], list["JSON"], str, int, bool, float, None]


def test_json_float() -> None:
    """
    This test demonstrates that JSON-LD has a default interpretation of a JSON float [#jsonld1.1-B.1.3]_, automatically typing as ``xsd:double``.  This happens to differ from CASE's default of ``xsd:decimal``.

    References
    ==========

    .. [#jsonld1.1-B.1.3] https://www.w3.org/TR/json-ld11/#conversion-of-native-data-types
    """

    expected_graph = Graph()
    computed_graph = Graph()

    json_graph: JSON = {
        "@context": {
            "ex": "http://example.org/ontology/",
            "kb": "http://example.org/kb/",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
        },
        "@graph": {
            "@id": "kb:Thing-1",
            "ex:property1": {"@type": "xsd:decimal", "@value": "1.234"},
            "ex:property2": {"@type": "xsd:double", "@value": "2.345"},
            "ex:property3": {"@type": "xsd:float", "@value": "3.456"},
            "ex:property4": 4.567,
        },
    }

    computed_graph.parse(data=json.dumps(json_graph), format="json-ld")

    ns_ex = Namespace("http://example.org/ontology/")
    ns_kb = Namespace("http://example.org/kb/")
    ns_xsd = XSD

    expected_graph.add(
        (
            ns_kb["Thing-1"],
            ns_ex["property1"],
            Literal("1.234", datatype=ns_xsd.decimal),
        )
    )
    expected_graph.add(
        (ns_kb["Thing-1"], ns_ex["property2"], Literal("2.345", datatype=ns_xsd.double))
    )
    expected_graph.add(
        (ns_kb["Thing-1"], ns_ex["property3"], Literal("3.456", datatype=ns_xsd.float))
    )
    expected_graph.add(
        (ns_kb["Thing-1"], ns_ex["property4"], Literal("4.567", datatype=ns_xsd.double))
    )

    expected_triples = [x for x in expected_graph.triples((None, None, None))]
    computed_triples = [x for x in computed_graph.triples((None, None, None))]

    assert expected_triples == computed_triples
