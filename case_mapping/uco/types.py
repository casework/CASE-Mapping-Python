from ..base import UcoInherentCharacterizationThing


class ControlledDictionaryEntry(UcoInherentCharacterizationThing):
    def __init__(self, key=None, value=None):
        """
        A controlled dictionary entry is a single (term/key, value) pair where the term/key is constrained to an
        explicitly defined set of values.
        """
        super().__init__()
        self["@type"] = "uco-types:ControlledDictionaryEntry"
        self._str_vars = {"uco-types:key": key, "uco-types:value": value}


directory = {"uco-types:ControlledDictionaryEntry": ControlledDictionaryEntry}
