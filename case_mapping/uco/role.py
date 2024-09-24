from typing import Any

from ..base import UcoObject


class Role(UcoObject):
    def __init__(
        self,
        *args: Any,
        **kwargs: Any,
    ):
        """
        A role is a usual or customary function based on contextual perspective.
        """
        super().__init__(*args, **kwargs)
        self["@type"] = "uco-role:Role"


directory = {"uco-role:Role": Role}
