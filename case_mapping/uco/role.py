from ..base import Facet


class Role(Facet):
    def __init__(
        self,
        description=None,
        _id=None,
        modified_time=None,
        name=None,
        created_time=None,
        spec_version=None,
        tag=None,
        _type=None,
        created_by=None,
        objet_marking=None,
    ):
        """
        A role is a usual or customary function based on contextual perspective.
        :param description: A description of a particular concept characterization.
        :param _id: A globally unique identifier for a characterization of a concept.
        :param modified_time: Specifies the time that this particular version of the object was modified.
        :param name: The name of a particular concept characterization.
        :param created_time: The time at which a characterization of a concept is created.
        :param spec_version: The version of UCO used to characterize a concept.
        :param tag: A generic tag/label.
        :param _type: The explicitly-defined type of characterization of a concept.
        :param created_by: The identity that created a characterization of a concept.
        :param objet_marking: Marking definitions to be applied to a particular concept characterization in its entirety
        """
        super().__init__()
        self["@type"] = "uco-role:Role"
        self._str_vars(
            **{
                "uco-core:description": description,
                "uco-core:name": name,
                "uco-core:specVersion": spec_version,
                "uco-core:tag": tag,
                "uco-core:type": _type,
            }
        )
        self._datetime_vars(
            **{
                "uco-core:modifiedTime": modified_time,
                "uco-core:objectCreatedTime": created_time,
            }
        )
        self._node_reference_vars(
            **{
                "uco-core:id": _id,
                "uco-core:createdBy": created_by,
                "uco-core:objectMarking": objet_marking,
            }
        )


directory = {"uco-role:Role": Role}
