from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from pytz import timezone

from ..base import FacetEntity, ObjectEntity


class InvestigativeAction(ObjectEntity):
    def __init__(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        start_time=None,
        end_time=None,
        facets: Union[None, FacetEntity, List[FacetEntity]] = None,
        performer: Union[None, ObjectEntity] = None,
        location: Union[None, ObjectEntity] = None,
        instrument: Union[None, ObjectEntity] = None,
        object: Union[None, ObjectEntity, List[ObjectEntity]] = None,
        result: Union[None, ObjectEntity, List[ObjectEntity]] = None,
    ):
        """
        An investigative action is a CASE object that represents the who, when, what outcome of an action.
        :param name: The name of the action (e.g., "Forensic mobile device acquisition").
        :param start_time: The time, in ISO8601 time format, the action was started (e.g., "2020-09-29T12:13:01Z").
        :param end_time: The time, in ISO8601 time format, the action completed (e.g., "2020-09-29T12:13:43Z").
        :param facets: A list of FacetEntity to be added to this object.
        :param performer: The primary performer of an action.
        :param location: The location where an action occurs.
        :param instrument: The things used to perform an action.
        :param object: The things that the action is performed on/against.
        :param result: The things resulting from performing an action.
        """
        super().__init__()
        self["@type"] = "case-investigation:InvestigativeAction"
        self._str_vars(**{"uco-core:name": name, "uco-core:description": description})
        self._datetime_vars(
            **{"uco-action:startTime": start_time, "uco-action:endTime": end_time}
        )
        self._node_reference_vars(
            **{
                "uco-action:performer": performer,
                "uco-action:location": location,
                "uco-action:instrument": instrument,
                "uco-action:object": object,
                "uco-action:result": result,
            }
        )
        if facets:
            self.append_facets(facets)

    def set_end_time(self):
        """Set the time when this action completed."""
        self._addtime(_type="end")

    def set_start_time(self):
        """Set the time when this action initiated."""
        self._addtime(_type="start")

    def _addtime(self, _type):
        time = datetime.now(timezone("UTC"))
        self[f"uco-action:{_type}Time"] = {
            "@type": "xsd:dateTime",
            "@value": time.isoformat(),
        }
        return time


class CaseInvestigation(ObjectEntity):
    def __init__(self, name=None, focus=None, description=None, core_objects=None):
        """
        An investigative action is a CASE object that represents the who, where, when of investigation
        :param name: The name of an investigation (e.g., Murder of Suspect B,.)
        :param focus: The type of investigation (e.g., Murder, Fraud etc,.)
        :param description: Description of the object  (e.g., Investigation carried out on evidence found in house A)
        :param core_objects: A list of items to be added to this object (e.g., items or objects that are in this
               object e.g., Persons involved in investigation, Investigation into a Murder, object refrences a
               case-object for a phone investigative action
        """
        super().__init__()
        self["@type"] = "case-investigation:Investigation"
        self._str_vars(
            **{
                "uco-core:name": name,
                "case-investigation:focus": focus,
                "uco-core:description": description,
            }
        )
        self.append_core_objects(core_objects)


class ProvenanceRecord(ObjectEntity):
    def __init__(
        self,
        exhibit_number: Optional[str] = None,
        uco_core_objects: Union[None, ObjectEntity, List[ObjectEntity]] = None,
    ):
        super().__init__()
        self["@type"] = "case-investigation:ProvenanceRecord"
        self._str_vars(**{"case-investigation:exhibitNumber": exhibit_number})
        self._node_reference_vars(**{"uco-core:object": uco_core_objects})


directory = {
    "case-investigation:InvestigativeAction": InvestigativeAction,
    "case-investigation:Investigation": CaseInvestigation,
    "case-investigation:ProvenanceRecord": ProvenanceRecord,
}
