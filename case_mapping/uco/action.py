from datetime import datetime
from typing import Any, List, Optional, Sequence, Union

from pytz import timezone

from ..base import Facet, UcoObject, unpack_args_array
from .location import Location


class Action(UcoObject):
    def __init__(
        self,
        *args: Any,
        action_count: Optional[int] = None,
        action_status: Optional[str] = None,
        end_time: Optional[datetime] = None,
        environment: Optional[UcoObject] = None,
        error: Optional[UcoObject] = None,
        instrument: Union[None, UcoObject, Sequence[UcoObject]] = None,
        location: Union[None, Location, Sequence[Location]] = None,
        objects: Union[None, UcoObject, Sequence[UcoObject]] = None,
        participant: Union[None, Sequence[UcoObject]] = None,
        performer: Optional[UcoObject] = None,
        results: Union[None, UcoObject, Sequence[UcoObject]] = None,
        start_time: Optional[datetime] = None,
        subaction: Optional[UcoObject] = None,
        **kwargs: Any,
    ) -> None:
        """
        An action is something that may be done or performed.
        Actions group the properties characterizing core action-elements (who, how, with what, where, etc.).
        The properties consist of identifier references to separate UCO objects detailing the particular property.
        :param start_time: The time, in ISO8601 time format, the action was started (e.g., "2020-09-29T12:13:01Z").
        :param end_time: The time, in ISO8601 time format, the action completed (e.g., "2020-09-29T12:13:43Z").
        :param name: The name of the action (e.g., "Forensic mobile device acquisition").
        :param performer: The primary performer of an action.
        :param instrument: The things used to perform an action.
        :param location: The general location where the action took place (Room, Building or Town)
        :param environment: The type of environment (lab, office)
        :param object: The things that the action is performed on/against.
        :param result: The things resulting from performing an action.
        """
        super().__init__(*args, **kwargs)
        self["@type"] = "uco-action:Action"
        self._nonegative_int_vars(
            **{
                "uco-action:actionCount": action_count,
            }
        )
        if action_status:
            self["uco-action:actionStatus"] = {
                "@type": "uco-vocabulary:ActionStatusTypeVocab",
                "@value": action_status,
            }
        self._datetime_vars(
            **{"uco-action:startTime": start_time, "uco-action:endTime": end_time}
        )
        self._node_reference_vars(
            **{
                "uco-action:environment": environment,
                "uco-action:error": error,
                "uco-action:performer": performer,
                "uco-action:instrument": instrument,
                "uco-action:location": location,
                "uco-action:result": results,
                "uco-action:object": objects,
                "uco-action:participant": participant,
                "uco-action:subaction": subaction,
            }
        )

    @unpack_args_array
    def append_results(self, *args):
        """
        Add result(s) to the list of outputs from an action
        :param args: A CASE object, or objects, often an observable. (e.g., one or many devices from a search operation)
        """
        self._append_refs("uco-action:result", *args)

    @unpack_args_array
    def append_objects(self, *args):
        """
        Add object(s) to the list of outputs from an action
        :param args: A CASE object, or objects, often an observable. (e.g., one or many devices from a search operation)
        """
        self._append_refs("uco-action:object", *args)

    def _addtime(self, _type):
        time = datetime.now(timezone("UTC"))
        self[f"uco-action:{_type}Time"] = {
            "@type": "xsd:dateTime",
            "@value": time.isoformat(),
        }
        return time

    def set_end_time(self):
        """Set the time when this action completed."""
        self._addtime(_type="end")

    def set_start_time(self):
        """Set the time when this action initiated."""
        self._addtime(_type="start")


directory = {"uco-action:Action": Action}
