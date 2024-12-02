from datetime import datetime
from typing import Any, Optional, Sequence, Union

from pytz import timezone

from ..base import UcoObject, unpack_args_array


class Compilation(UcoObject):
    def __init__(
        self,
        *args: Any,
        core_objects: Optional[Sequence[UcoObject]] = None,
        **kwargs: Any,
    ) -> None:
        """
        A compilation is a grouping of things.
        """
        super().__init__(*args, **kwargs)
        self["@type"] = "uco-core:Compilation"
        if core_objects is not None and len(core_objects) > 0:
            self.append_core_objects(core_objects)

    @unpack_args_array
    def append_to_uco_object(self, *args) -> None:
        """
        Add a single/tuple of result(s) to the list of outputs from an action
        :param args: A CASE object, or objects, often an observable. (e.g., one of many devices from a search operation)
        """
        self._append_observable_objects("uco-core:object", *args)


class ContextualCompilation(Compilation):
    def __init__(
        self,
        *args: Any,
        core_objects: Sequence[UcoObject],
        **kwargs: Any,
    ) -> None:
        """
        A contextual compilation is a grouping of things sharing some context (e.g., a set of network connections observed on a given day, all accounts associated with a given person).

        Future implementation note: At and before CASE 1.3.0, at least one core:object must be supplied at instantiation time of a contextual compilation.  At and after CASE 1.4.0, these objects will be optional.
        """
        if len(core_objects) == 0:
            raise ValueError(
                "A ContextualCompilation is required to have at least one UcoObject to link at initiation time.  This will become optional in CASE 1.4.0."
            )
        super().__init__(*args, **kwargs)
        self["@type"] = "uco-core:ContextualCompilation"
        self.append_core_objects(core_objects)


class EnclosingCompilation(Compilation):
    def __init__(
        self,
        *args: Any,
        core_objects: Sequence[UcoObject],
        **kwargs: Any,
    ) -> None:
        """
        An enclosing compilation is a container for a grouping of things.
        """
        if len(core_objects) == 0:
            raise ValueError(
                "An EnclosingCompilation is required to have at least one UcoObject to link at initiation time."
            )
        super().__init__(*args, **kwargs)
        self["@type"] = "uco-core:EnclosingCompilation"
        self.append_core_objects(core_objects)


class Bundle(EnclosingCompilation):
    def __init__(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        The main CASE Object for representing a case and its activities and objects.

        Instantiating this class requires a starter sequence (set, list, or tuple) to be passed using the core_objects parameter.  (See EnclosingCompilation.)  To confirm conformant CASE will be generated, at least one UcoObject must be passed in this list.  However, this does not initially need to be the complete sequence of objects that will be in this Bundle.  Other UcoObjects can be added after initialization with bundle.append_to_uco_object.
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
        assert isinstance(self["@context"], dict)
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


directory = {
    "uco-core:Bundle": Bundle,
    "uco-core:Compilation": Compilation,
    "uco-core:ContextualCompilation": ContextualCompilation,
}
