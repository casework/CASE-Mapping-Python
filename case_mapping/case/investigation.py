from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from pytz import timezone

from ..base import FacetEntity, ObjectEntity
from ..uco.action import Action
from ..uco.location import Location


class InvestigativeAction(Action):
    def __init__(
        self,
        *args: Any,
        description: Optional[str] = None,
        facets: Optional[List[FacetEntity]] = None,
        end_time: Optional[datetime] = None,
        environment: Optional[ObjectEntity] = None,
        instrument: Union[None, ObjectEntity, List[ObjectEntity]] = None,
        location: Union[None, Location, List[Location]] = None,
        name: Optional[str] = None,
        objects: Union[None, ObjectEntity, List[ObjectEntity]] = None,
        performer: Optional[ObjectEntity] = None,
        results: Union[None, ObjectEntity, List[ObjectEntity]] = None,
        start_time: Optional[datetime] = None,
        **kwargs: Any,
    ) -> None:
        """
        An investigative action is a CASE object that represents the who, when, what outcome of an action.
        """
        super().__init__(
            *args,
            description=description,
            facets=facets,
            end_time=end_time,
            environment=environment,
            instrument=instrument,
            location=location,
            name=name,
            objects=objects,
            performer=performer,
            results=results,
            start_time=start_time,
            **kwargs,
        )
        self["@type"] = "case-investigation:InvestigativeAction"


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
