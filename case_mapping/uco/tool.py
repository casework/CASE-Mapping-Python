from ..base import ObjectEntity


class Tool(ObjectEntity):
    def __init__(
        self, tool_name=None, tool_version=None, tool_type=None, tool_creator=None
    ):
        """
        The Uco tool is a way to define the specifics of a tool used in an investigation
        :param tool_name: The name of the tool (e.g., "exiftool")
        :param tool_creator: An ObservableObject The developer and or organisation that produces this tool {might need to add a dict here}
        :param tool_type: The type of tool
        :param tool_version: The version of the tool
        """
        super().__init__()
        self["@type"] = "uco-tool:Tool"
        self._str_vars(
            **{
                "uco-core:name": tool_name,
                "uco-tool:version": tool_version,
                "uco-tool:toolType": tool_type,
            }
        )
        self._node_reference_vars(**{"uco-tool:creator": tool_creator})


directory = {"uco-tool:Tool": Tool}
