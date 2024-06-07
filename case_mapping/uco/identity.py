from typing import Dict, Optional

from ..base import Facet, IdentityAbstraction, UcoObject


class BirthInformationFacet(Facet):
    def __init__(self, birthdate=None):
        """
        :param birthdate: the date of birth of an identity
        """
        super().__init__()
        self["@type"] = "uco-identity:BirthInformationFacet"
        self._datetime_vars(**{"uco-identity:birthdate": birthdate})


class Identity(IdentityAbstraction):
    def __init__(self, name: Optional[str] = None, facets=None):
        super().__init__()
        self["@type"] = "uco-identity:Identity"
        str_vars: Dict[str, str] = dict()
        if name is not None:
            str_vars["uco-core:name"] = name
        self._str_vars(**str_vars)
        self.append_facets(facets)


class Organization(Identity):
    def __init__(self, name: Optional[str] = None, facets=None):
        super().__init__(name, facets)
        self["@type"] = "uco-identity:Organization"


class SimpleNameFacet(Facet):
    def __init__(self, given_name=None, family_name=None):
        """
        :param given_name: Full name of the identity of person
        :param family_name: Family name of identity of person
        """
        super().__init__()
        self["@type"] = "uco-identity:SimpleNameFacet"
        self._str_vars(
            **{
                "uco-identity:givenName": given_name,
                "uco-identity:familyName": family_name,
            }
        )


directory = {
    "uco-identity:BirthInformationFacet": BirthInformationFacet,
    "uco-identity:Identity": Identity,
    "uco-identity:Organization": Organization,
    "uco-identity:SimpleNameFacet": SimpleNameFacet,
}
