from typing import Any, Optional

from ..base import UcoObject
from .identity import Identity


class Tool(UcoObject):
    def __init__(
        self,
        *args: Any,
        description: Optional[str] = None,
        name: Optional[str] = None,
        tool_version: Optional[str] = None,
        tool_type: Optional[str] = None,
        tool_creator: Optional[Identity] = None,
        **kwargs: Any,
    ) -> None:
        """
        The Uco tool is a way to define the specifics of a tool used in an investigation
        :param name: The name of the tool (e.g., "exiftool")
        :param tool_creator: The developer or organisation that produced this tool
        :param tool_type: The type of tool
        :param tool_version: The version of the tool
        """
        super().__init__(*args, description=description, name=name, **kwargs)
        self["@type"] = "uco-tool:Tool"
        self._str_vars(
            **{
                "uco-tool:version": tool_version,
                "uco-tool:toolType": tool_type,
            }
        )
        self._node_reference_vars(**{"uco-tool:creator": tool_creator})


directory = {"uco-tool:Tool": Tool}
