from datetime import datetime
from typing import Any, List, Optional, Union

from pytz import timezone

from ..base import UcoObject, unpack_args_array


class Bundle(UcoObject):
    def __init__(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        The main CASE Object for representing a case and its activities and objects.
        """
        super().__init__(*args, **kwargs)
        self.build = []  # type: ignore
        self["@context"] = {
            "@vocab": "http://caseontology.org/core#",
            "case-investigation": "https://ontology.caseontology.org/case/investigation/",
            "drafting": "http://example.org/ontology/drafting/",
            "co": "http://purl.org/co/",
            "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "uco-action": "https://ontology.unifiedcyberontology.org/uco/action/",
            "uco-core": "https://ontology.unifiedcyberontology.org/uco/core/",
            "uco-identity": "https://ontology.unifiedcyberontology.org/uco/identity/",
            "uco-location": "https://ontology.unifiedcyberontology.org/uco/location/",
            "uco-role": "https://ontology.unifiedcyberontology.org/uco/role/",
            "uco-observable": "https://ontology.unifiedcyberontology.org/uco/observable/",
            "uco-tool": "https://ontology.unifiedcyberontology.org/uco/tool/",
            "uco-types": "https://ontology.unifiedcyberontology.org/uco/types/",
            "uco-vocabulary": "https://ontology.unifiedcyberontology.org/uco/vocabulary/",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
        }

        # Assign caller-selectible prefix label and IRI, after checking
        # for conflicts with hard-coded prefixes.
        # https://www.w3.org/TR/turtle/#prefixed-name
        if self.prefix_label in self["@context"]:
            raise ValueError(
                "Requested prefix label already in use in hard-coded dictionary: '%s'.  Please revise caller to use another label."
                % self.prefix_label
            )
        self["@context"][self.prefix_label] = self.prefix_iri
        self["@type"] = "uco-core:Bundle"

    @unpack_args_array
    def append_to_case_graph(self, *args):
        self._append_observable_objects("@graph", *args)

    @unpack_args_array
    def append_to_uco_object(self, *args):
        """
        Add a single/tuple of result(s) to the list of outputs from an action
        :param args: A CASE object, or objects, often an observable. (e.g., one of many devices from a search operation)
        """
        self._append_observable_objects("uco-core:object", *args)

    @unpack_args_array
    def append_to_rdfs_comments(self, *args):
        self._append_strings("rdfs:comment", *args)

    @unpack_args_array
    def append_to_uco_core_description(self, *args):
        self._append_strings("uco-core:description", *args)


class Relationship(UcoObject):
    def __init__(
        self,
        *args: Any,
        source: UcoObject,
        target: UcoObject,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        kind_of_relationship: str,
        directional: bool = False,
        **kwargs: Any,
    ) -> None:
        """
        This object represents an assertion that one or more objects are related to another object in some way
        :param source: A UcoObject
        :param target: A UcoObject
        :param start_time: The time, in ISO8601 time format, the action was started (e.g., "2020-09-29T12:13:01Z")
        :param end_time: The time, in ISO8601 time format, the action completed (e.g., "2020-09-29T12:13:43Z")
        :param kind_of_relationship: How these items relate from source to target (e.g., "Contained_Within")
        :param directional: A boolean whether a relationship assertion is limited to the context FROM a source object(s) TO a target object.
        """
        super().__init__(*args, **kwargs)
        self["@type"] = "uco-core:Relationship"
        self._bool_vars(**{"uco-core:isDirectional": directional})
        self._str_vars(**{"uco-core:kindOfRelationship": kind_of_relationship})
        self._datetime_vars(
            **{
                "uco-core:startTime": start_time,
                "uco-core:endTime": end_time,
            }
        )
        self._node_reference_vars(
            **{"uco-core:source": source, "uco-core:target": target}
        )

    def set_start_accessed_time(self) -> None:
        """Set the time when this relationship initiated."""
        self._addtime(_type="start")

    def set_end_accessed_time(self) -> None:
        """Set the time when this relationship completed."""
        self._addtime(_type="end")

    def _addtime(self, _type: str) -> None:
        time = datetime.now(timezone("UTC"))
        self[f"uco-core:{_type}Time"] = {
            "@type": "xsd:dateTime",
            "@value": time.isoformat(),
        }


directory = {"uco-core:Bundle": Bundle}
