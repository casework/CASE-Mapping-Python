import uuid
from typing import Any, Union

import utils


def check_app_name(app_name, app_names, app_objects, uuid):
    # c_check = utils.CheckDuplicate()
    observable_app = utils.check_value(
        app_name,
        uuid,
        value=app_name,
        list_values=app_names,
        list_objects=app_objects,
        observable_generating_f=generateTraceAppName,
    )
    return observable_app


def check_geo_coordinates(latitude, longitude, geo_coordinates, geo_objects, uuid):
    # c_check = utils.CheckDuplicate()
    observable_app = utils.check_value(
        latitude,
        longitude,
        uuid,
        value=str(latitude) + "#" + str(longitude),
        list_values=geo_coordinates,
        list_objects=geo_objects,
        observable_generating_f=generateTraceLocationCoordinate,
    )
    return observable_app


def generateTraceAppName(app_name, uuid):
    observable = {
        "@type": "uco-observable:ApplicationFacet",
        "@id": uuid,
        "uco-core:name": app_name,
    }
    return observable


def generateTraceLocationCoordinate(
    latitude: Union[float, str], longitude: Union[float, str], uuid: str
) -> dict[str, Any]:
    observable = {
        "@type": "uco-location:LatLongCoordinatesFacet",
        "@id": uuid,
        "uco-location:latitude": {"@type": "xsd:decimal", "@value": str(latitude)},
        "uco-location:longitude": {"@type": "xsd:decimal", "@value": str(longitude)},
    }
    return observable


def test_app_name():
    app_names = list()
    app_objects = list()
    app_1 = "Safari"
    uuid_1 = "kb:" + str(uuid.uuid4())
    check_app_name(app_1, app_names, app_objects, uuid_1)
    assert app_names == [app_1]
    app_2 = "Chrome"
    uuid_2 = "kb:" + str(uuid.uuid4())
    check_app_name(app_2, app_names, app_objects, uuid_2)
    assert app_names == [app_1, app_2]
    uuid_3 = "kb:" + str(uuid.uuid4())
    object_app = check_app_name(app_1, app_names, app_objects, uuid_3)
    assert object_app == {
        "@type": "uco-observable:ApplicationFacet",
        "@id": uuid_1,
        "uco-core:name": app_1,
    }
    assert app_names == [app_1, app_2]
    assert app_objects == [
        {
            "@type": "uco-observable:ApplicationFacet",
            "@id": uuid_1,
            "uco-core:name": app_1,
        },
        {
            "@type": "uco-observable:ApplicationFacet",
            "@id": uuid_2,
            "uco-core:name": app_2,
        },
    ]


def test_geo_coordinates():
    geo_coordinates = list()
    geo_objects = list()
    (lat_1, long_1, uuid_1) = (56.47267913, -71.17069244, "kb:" + str(uuid.uuid4()))
    check_geo_coordinates(lat_1, long_1, geo_coordinates, geo_objects, uuid_1)
    # print(f"\n 1) FT geo_coordinates={geo_coordinates}")
    assert geo_coordinates == [str(lat_1) + "#" + str(long_1)]
    (lat_2, long_2, uuid_2) = (88.26801306, 13.21980922, "kb:" + str(uuid.uuid4()))
    check_geo_coordinates(lat_2, long_2, geo_coordinates, geo_objects, uuid_2)
    # print(f"\n 2) FT geo_coordinates={geo_coordinates}")
    assert geo_coordinates == [
        str(lat_1) + "#" + str(long_1),
        str(lat_2) + "#" + str(long_2),
    ]
    uuid_3 = "kb:" + str(uuid.uuid4())
    uuid_4 = "kb:" + str(uuid.uuid4())
    geo_object = check_geo_coordinates(
        lat_1, long_1, geo_coordinates, geo_objects, uuid_3
    )
    assert geo_object == {
        "@type": "uco-location:LatLongCoordinatesFacet",
        "@id": uuid_1,
        "uco-location:latitude": {"@type": "xsd:decimal", "@value": str(lat_1)},
        "uco-location:longitude": {"@type": "xsd:decimal", "@value": str(long_1)},
    }
    # print(f"\n 3) FT geo_coordinates={geo_coordinates}")
    assert geo_coordinates == [
        str(lat_1) + "#" + str(long_1),
        str(lat_2) + "#" + str(long_2),
    ]
    check_geo_coordinates(lat_2, long_2, geo_coordinates, geo_objects, uuid_4)
    # print(f"\n 4) FT geo_coordinates={geo_coordinates}")
    assert geo_coordinates == [
        str(lat_1) + "#" + str(long_1),
        str(lat_2) + "#" + str(long_2),
    ]
    assert geo_objects == [
        {
            "@type": "uco-location:LatLongCoordinatesFacet",
            "@id": uuid_1,
            "uco-location:latitude": {"@type": "xsd:decimal", "@value": str(lat_1)},
            "uco-location:longitude": {"@type": "xsd:decimal", "@value": str(long_1)},
        },
        {
            "@type": "uco-location:LatLongCoordinatesFacet",
            "@id": uuid_2,
            "uco-location:latitude": {"@type": "xsd:decimal", "@value": str(lat_2)},
            "uco-location:longitude": {"@type": "xsd:decimal", "@value": str(long_2)},
        },
    ]
