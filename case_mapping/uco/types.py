from typing import Any, Dict, List

from ..base import UcoInherentCharacterizationThing


class DictionaryEntry(UcoInherentCharacterizationThing):
    """
    A dictionary entry is a single (term/key, value) pair.
    """

    def __init__(self, *args: Any, key: str, value: str, **kwargs: Any) -> None:
        super().__init__(self, *args, **kwargs)
        self["@type"] = "uco-types:DictionaryEntry"
        self._str_vars(**{"uco-types:key": key, "uco-types:value": value})


class Dictionary(UcoInherentCharacterizationThing):
    """
    A dictionary is list of (term/key, value) pairs with each term/key existing no more than once.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(self, *args, **kwargs)
        self["@type"] = "uco-types:Dictionary"
        self["uco-types:entry"] = []

    def _dict_var(self, arg: Dict[str, str]) -> None:
        for k, v in arg.items():
            entry = DictionaryEntry(key=k, value=v)
            self["uco-types:entry"].append(entry)


class ControlledDictionaryEntry(DictionaryEntry):
    """
    A controlled dictionary entry is a single (term/key, value) pair where the term/key is constrained to an
    explicitly defined set of values.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(self, *args, **kwargs)
        self["@type"] = "uco-types:ControlledDictionaryEntry"


directory = {
    "uco-types:ControlledDictionaryEntry": ControlledDictionaryEntry,
    "uco-types:Dictionary": Dictionary,
    "uco-types:DictionaryEntry": DictionaryEntry,
}
