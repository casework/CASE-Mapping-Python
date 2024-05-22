from typing import Optional

from ..base import FacetEntity, ObjectEntity


class Location(ObjectEntity):
    def __init__(self, facets=None):
        super().__init__()
        self["@type"] = "uco-location:Location"
        self.append_facets(facets)


class FacetLocation(FacetEntity):
    def __init__(
        self,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        altitude: Optional[float] = None,
    ):
        """
        A lat long coordinates facet is a grouping of characteristics unique
        to the expression of a geolocation as the intersection of specific
        latitude, longitude, and altitude values.
        :param latitude: The latitude coordinate of a geolocation.
        :param longitude: The longitude coordinate of a geolocation.
        :param altitude: The altitude coordinate of a geolocation.
        """
        super().__init__()
        self["@type"] = "uco-location:LatLongCoordinatesFacet"
        self._float_vars(
            **{
                "uco-location:latitude": latitude,
                "uco-location:longitude": longitude,
                "uco-location:altitude": altitude,
            }
        )


class FacetSimpleAdress(FacetEntity):
    def __init__(
        self,
        country=None,
        locality=None,
        street=None,
        postal_code=None,
        region=None,
        address_type=None,
    ):
        super().__init__()
        self["@type"] = "uco-location:SimpleAddressFacet"
        self._str_vars(
            **{
                "uco-location:adressType": address_type,
                "uco-location:country": country,
                "uco-location:locality": locality,
                "uco-location:postalCode": postal_code,
                "uco-location:region": region,
                "uco-location:street": street,
            }
        )


directory = {
    "uco-location:Location": Location,
    "uco-location:LatLongCoordinatesFacet": FacetLocation,
    "uco-location:SimpleAddressFacet": FacetSimpleAdress,
}
