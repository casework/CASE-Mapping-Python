from datetime import datetime
from typing import Any, Dict, List, Optional, Union

from cdo_local_uuid import local_uuid

from ..base import Facet, UcoInherentCharacterizationThing, UcoObject
from .action import Action
from .core import Relationship
from .identity import Identity
from .location import Location
from .types import Dictionary


class ObservableDomainName(UcoObject):
    def __init__(self, has_changed=None, state=None, facets=None):
        """
        Used to represent domain name objects
        :param has_changed:
        :param state:
        :param facets: This will contain specific properties for this object
        """
        super().__init__()
        self["@type"] = "uco-observable:DomainName"
        self._str_vars(**{"uco-observable:state": state})
        self._bool_vars(**{"uco-observable:hasChanged": has_changed})
        self.append_facets(facets)


class DomainNameFacet(Facet):
    def __init__(self, domain, isTLD=False):
        """
        Used to represent data for domainname objects
        :param domain: The domain (like google.com)
        :param isTLD: Usually false unless a TLD is required (like when the domain is .com)
        """
        super().__init__()
        self["@type"] = "uco-observable:DomainNameFacet"
        self._str_vars(**{"uco-observable:value": domain})
        self._bool_vars(**{"uco-observable:isTLD": isTLD})


class ObservableHostName(UcoObject):
    def __init__(self, hostname, has_changed=None, state=None):
        """
        Used to represent host names of devices on a network
        :param has_changed:
        :param state:
        :param hostname: The value for this object - a hostname (like ucd.ie)
        """
        super().__init__()
        self["@type"] = "uco-observable:HostName"
        self._str_vars(
            **{"uco-observable:state": state, "uco-observable:value": hostname}
        )
        self._bool_vars(**{"uco-observable:hasChanged": has_changed})


class ObservableIPv4Address(UcoObject):
    def __init__(self, has_changed=None, state=None, facets=None):
        """
        Used to represent an IPv4 address object
        :param has_changed:
        :param state:
        """
        super().__init__()
        self["@type"] = "uco-observable:IPv4Address"
        self._str_vars(**{"uco-observable:state": state})
        self._bool_vars(**{"uco-observable:hasChanged": has_changed})
        self.append_facets(facets)


class IPv4AddressFacet(Facet):
    def __init__(self, ip=None):
        """
        Used to represent IPv4 Addresses
        :param ip: An IPv4 address (like 193.1.137.12)
        """
        super().__init__()
        self["@type"] = "uco-observable:IPv4AddressFacet"
        self._str_vars(**{"uco-observable:addressValue": ip})


class ObservableAutonomousSystem(UcoObject):
    def __init__(self, has_changed=None, state=None, facets=None):
        """
        An autonomous system is a collection of connected Internet Protocol (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative entity or domain that presents a common, clearly defined routing policy to the Internet.

        An Autonomous System object is a grouping of characteristics unique to a distinct article or unit within the digital domain.
        :param has_changed:
        :param state:
        :param facets: This will contain specific properties for this object
        """
        super().__init__()
        self["@type"] = "uco-observable:AutonomousSystem"
        self._str_vars(**{"uco-observable:state": state})
        self._bool_vars(**{"uco-observable:hasChanged": has_changed})
        self.append_facets(facets)


class AutonomousSystemFacet(Facet):
    def __init__(self, as_number, as_handle=None):
        """
        An autonomous system facet is a grouping of characteristics unique to a collection of connected Internet Protocol (IP) routing prefixes under the control of one or more network operators on behalf of a single administrative entity or domain that presents a common, clearly defined routing policy to the Internet.
        :param as_number: An Autonomous System Number (int)
        :param as_handle: An Autonomous System Handle (string)
        """
        super().__init__()
        self["@type"] = "uco-observable:AutonomousSystemFacet"
        self._int_vars(**{"uco-observable:number": as_number})
        self._str_vars(**{"uco-observable:asHandle": as_handle})


class X509Certificate(UcoObject):
    def __init__(
        self,
        has_changed=False,
        state=None,
        description=None,
        facets=None,
        certificate_id=None,
        certificate_name=None,
        created_time=None,
    ):
        """
        Object for certificate
        @param has_changed:
        @param state:
        @param description:
        @param facets:
        @param certificate_id:
        @param certificate_name:
        @param created_time:
        """
        super().__init__()
        self["@type"] = "uco-observable:X509Certificate"
        self._bool_vars(**{"uco-observable:hasChanged": has_changed})
        self._str_vars(
            **{
                "uco-observable:state": state,
                "uco-core:id": certificate_id,
                "uco-core:description": description,
                "uco-core:name": certificate_name,
            }
        )
        self._datetime_vars(**{"uco-core:modifiedTime": created_time})
        self.append_facets(facets)


class X509CertificateFacet(Facet):
    def __init__(
        self,
        is_self_signed=False,
        issuer=None,
        serial_number=None,
        signature=None,
        subject=None,
        subject_pk_algo=None,
        subject_pk_exponent=None,
        subject_pk_modulus=None,
        valid_not_before=None,
        validity_not_after=None,
        version=None,
    ):
        """
        Used to represent aspects of X509 Certificate Properties
        :param is_self_signed: Is the certificate self-signed
        :param issuer: the name of the certificate authority who issued the certificate
        :param issuer_hash: (NI) A hash calculated on the certificate issuer name. (type:Hash)
        :param serial_number: The serial number of the certificate
        :param signature: The signature of the
        :param signature_algo: Algorithm used for the signature of the certificate
        :param subject: Subject of the certificate
        :param subject_hash: (NI) A hash calculated on the certificate subject name. (type:Hash)
        :param subject_pk_algo: The public key algorithm used in the generation of the certificate
        :param subject_pk_exponent: The public key exponent used in the generation of the certificate
        :param subject_pk_modulus: The public key modulus used in the generation of the certificate
        :param thumbprint_hash: (NI) A hash calculated on the entire certificate including signature. (type:Hash)
        :param valid_not_before: A date at which a certificate becomes valid
        :param validity_not_after: A date at which a certificate becomes expired
        :param version: the version of the certificate
        :param x509_extensions: (NI) Extensions of the X509 protocol that may have been included in the cert. (Facet)
        """
        super().__init__()
        self["@type"] = "uco-observable:X509CertificateFacet"
        self._int_vars(
            **{
                "uco-observable:isSelfSigned": is_self_signed,
                "uco-observable:subjectPublicKeyExponent": subject_pk_exponent,
            }
        )
        self._str_vars(
            **{
                "uco-observable:issuer": issuer,
                "uco-observable:serialNumber": serial_number,
                "uco-observable:signature": signature,
                "uco-observable:signatureAlgorithm": signature,
                "uco-observable-subject": subject,
                "uco-observable:subjectPublicKeyAlgorithm": subject_pk_algo,
                "uco-observable:subjectPublicKeyModulus": subject_pk_modulus,
                "uco-observable:version": version,
            }
        )
        self._datetime_vars(
            **{
                "uco-observable:validityNotBefore": valid_not_before,
                "uco-observable:validityNotAfter": validity_not_after,
            }
        )


class AccountFacet(Facet):
    def __init__(self, identifier=None, is_active=True, issuer_id=None):
        """
        Used to represent user accounts
        :param is_active: Active unless specified otherwise (False)
        :param identifier: The idenitifier of the account (like a Skype username)
        :param issuer_id: The id of issuing body for application
                          (e.g., kb:organization-skypeapp-cc44c2ae-bdd3-4df8-9ca3-1f58d682d62b)
        """
        super().__init__()
        self["@type"] = "uco-observable:AccountFacet"
        self._bool_vars(**{"uco-observable:isActive": is_active})
        self._str_vars(
            **{
                "uco-observable:accountIdentifier": identifier,
            }
        )
        self._node_reference_vars(
            **{
                "uco-observable:accountIssuer": issuer_id,
            }
        )


class AccountAuthenticationFacet(Facet):
    def __init__(
        self,
        password: Optional[str] = None,
        password_last_changed: Optional[datetime] = None,
        password_type: Optional[str] = None,
    ):
        """
        An account authentication facet is a grouping of characteristics unique
        to the mechanism of accessing an account.
        :param password: Specifies an authentication password.
        :param password_last_changed: The date and time that the password was last changed.
        :param password_type: The type of password, for instance plain-text or encrypted.
        """
        super().__init__()
        self["@type"] = "uco-observable:AccountAuthenticationFacet"
        self._str_vars(
            **{
                "uco-observable:password": password,
                "uco-observable:passwordType": password_type,
            }
        )
        self._datetime_vars(
            **{
                "uco-observable:passwordLastChanged": password_last_changed,
            }
        )


class MobileAccountFacet(Facet):
    def __init__(
        self,
        IMSI: Optional[str] = None,
        MSISDN: Optional[str] = None,
        MSISDN_type: Optional[str] = None,
    ):
        """
        A mobile account facet is a grouping of characteristics unique to an arrangement
        with an entity to enable and control the provision of some capability or service
        on a portable computing device.
        :param IMSI: An International Mobile Subscriber Identity (IMSI) is a unique identification
        associated with all GSM and UMTS network mobile phone users.
        :param MSISDN: Mobile Station International Subscriber Directory Number (MSISDN) is a number
        used to identify a mobile phone number internationally.
        :param MSISDN_type: The network mobile phone (GMS or UMTS)
        """
        super().__init__()
        self["@type"] = "uco-observable:MobileAccountFacet"
        self._str_vars(
            **{
                "uco-observable:IMSI": IMSI,
                "uco-observable:MSISDN": MSISDN,
                "uco-observable:MSISDNType": MSISDN_type,
            }
        )


class ContentDataFacet(Facet):
    def __init__(
        self,
        byte_order=None,
        magic_number=None,
        mime_type=None,
        size_bytes=None,
        data_payload=None,
        entropy=None,
        is_encrypted=None,
        hash_method=None,
        hash_value=None,
    ):
        """
        The characteristics of a block of digital data.
        :param byte_order: Byte order of data. Example - "BigEndian"
        :param magic_number: The magic phone_number of a file
        :param mime_type: The mime type of a file. Example - "image/jpeg"
        :param size_bytes: A phone_number representing the size of the content
        :param data_payload: A base64 representation of the data
        :param entropy: The entropy value for the data
        :param is_encrypted: A boolean True/False, if encrypted or not.
        :param hash_method: The algorithm used to calculate the hash value
        :param hash_value: The cryptographic hash of this content
        """
        super().__init__()
        self["@type"] = "uco-observable:ContentDataFacet"
        self._str_vars(
            **{
                "uco-observable:magicNumber": magic_number,
                "uco-observable:mimeType": mime_type,
                "uco-observable:dataPayload": data_payload,
                "uco-observable:entropy": entropy,
            }
        )
        self._int_vars(**{"uco-observable:sizeInBytes": size_bytes})
        self._bool_vars(**{"uco-observable:isEncrypted": is_encrypted})

        if byte_order:
            self["uco-observable:byteOrder"] = {
                "@type": "uco-vocabulary:EndiannessTypeVocab",
                "@value": byte_order,
            }

        if hash_method is not None or hash_value is not None or hash_value != "-":
            data = {
                "@id": self.prefix_label + ":" + str(local_uuid()),
                "@type": "uco-types:Hash",
            }
            if hash_method is not None:
                data["uco-types:hashMethod"] = {
                    "@type": "uco-vocabulary:HashNameVocab",
                    "@value": hash_method,
                }
            if hash_value is not None:
                data["uco-types:hashValue"] = {
                    "@type": "xsd:hexBinary",
                    "@value": hash_value,
                }
            self["uco-observable:hash"] = [data]


class ObservableApplicationVersion(UcoInherentCharacterizationThing):
    def __init__(
        self, install_date=None, uninstall_date=None, version: Optional[str] = None
    ):
        """
        Used to represent a grouping of characteristics unique to a particular
        software program version.
        :param install_date: The date the application was installed.
        :param uninstall_date: The date the application was uninstalled
        :param version: The application version installed/uninstalled.
        """
        super().__init__()
        self["@type"] = "uco-observable:ApplicationVersion"
        self._str_vars(**{"uco-observable:version": version})
        self._datetime_vars(
            **{
                "uco-observable:installDate": install_date,
                "uco-observable:uninstallDate": uninstall_date,
            }
        )


class DataRangeFacet(Facet):
    def __init__(self, range_offset=None, range_size=None):
        """
        A data range facet is a grouping of characteristics unique to a particular contiguous scope
        within a block of digital data
        :param range_offset: location in data at which the contiguous data starts
        :param range_size: the length of the data starting at the offset point
        """
        super().__init__()
        self["@type"] = "uco-observable:DataRangeFacet"
        self._int_vars(
            **{
                "uco-observable:rangeOffset": range_offset,
                "uco-observable:rangeSize": range_size,
            }
        )


class DeviceFacet(Facet):
    def __init__(self, device_type=None, manufacturer=None, model=None, serial=None):
        """
        Characteristics of a piece of electronic equipment.
        :param device_type: The type of device (e.g., "camera")
        :param manufacturer: The producer of the device (e.g., "Canon")
        :param model: The model of the device (e.g., "Powershot SX540")
        :param serial: The serial phone_number of the device (e.g., "1296-3219-8792-CL918")
        """
        super().__init__()
        self["@type"] = "uco-observable:DeviceFacet"
        self._node_reference_vars(**{"uco-observable:manufacturer": manufacturer})
        self._str_vars(
            **{
                "uco-observable:deviceType": device_type,
                "uco-observable:model": model,
                "uco-observable:serialNumber": serial,
            }
        )


class WifiAddressFacet(Facet):
    def __init__(self, wifi_mac_address=None):
        """
        :param wifi_mac_address: The wifi mac address of a device (EG: 11:54:00:bc:c8:ba)
        """
        super().__init__()
        self["@type"] = "uco-observable:WifiAddressFacet"
        self._str_vars(**{"uco-observable:addressValue": wifi_mac_address})


class BluetoothAddressFacet(Facet):
    def __init__(self, name=None, address=None):
        """
        :param name:
        :param address: The Bluetooth address value (e.g. "D4:A3:3D:B5:F4:6C")
        """
        super().__init__()
        self["@type"] = "uco-observable:BluetoothAddressFacet"
        self._str_vars(
            **{"uco-core:name": name, "uco-observable:addressValue": address}
        )


class Observable(UcoObject):
    def __init__(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)


class ObservableObject(Observable):
    def __init__(self, *args: Any, has_changed=None, state=None, **kwargs: Any) -> None:
        """
        An observable object is a grouping of characteristics unique to a distinct article or unit within the digital domain.
        :param has_changed:
        :param state:
        """
        super().__init__(*args, **kwargs)
        self["@type"] = "uco-observable:ObservableObject"
        self._str_vars(**{"uco-observable:state": state})
        self._bool_vars(**{"uco-observable:hasChanged": has_changed})


class ObservableAction(Action):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        An observable action is a grouping of characteristics unique to something that may be done or performed within the digital domain.
        """
        super().__init__(*args, **kwargs)
        self["@type"] = "uco-observable:ObservableAction"


class ApplicationFacet(Facet):
    def __init__(
        self,
        application_identifier: Optional[str] = None,
        installed_version_history: Union[
            None, ObservableApplicationVersion, List[ObservableApplicationVersion]
        ] = None,
        number_of_launches: Optional[int] = None,
        operating_system: Union[ObservableObject, None] = None,
        version: Optional[str] = None,
    ):
        """
        A simple application
        :param application_identifier: Application identifier (Whatsapp, Shazam etc)
        :param installed_version_history: The history of installed application version(s).
        :param number_of_launches: How many times the application was launched.
        :param operating_system: A reference to an OperatingSystem object.
        :param version: The version of the application.
        """
        super().__init__()
        self["@type"] = "uco-observable:ApplicationFacet"
        self._str_vars(
            **{
                "uco-observable:applicationIdentifier": application_identifier,
                "uco-observable:version": version,
            }
        )
        self._int_vars(
            **{
                "uco-observable:numberOfLaunches": number_of_launches,
            }
        )
        if installed_version_history is not None:
            # Inline each ApplicationVersion node.
            self._append_stuff(
                "uco-observable:installedVersionHistory",
                *installed_version_history,
                objects=True,
            )
        self._node_reference_vars(
            **{
                "uco-observable:operatingSystem": operating_system,
            }
        )


class UrlHistoryFacet(Facet):
    def __init__(self, browser=None, history_entries=None):
        """
        :param browser_info: An observable object containing a URLHistoryFacet
        :param history_entries: A list of dictionaries, each dict has the
        following keys:
            "uco-observable:browserUserProfile": str,
            "uco-observable:expirationTime" : datetime,
            "uco-observable:firstVisit": datetime,
            "uco-observable:hostname": str,
            "uco-observable:keywordSearchTerm": str,
            "uco-observable:lastVisit" : datetime,
            "uco-observable:manuallyEnteredCount": non negative int
            "uco-observable:pageTitle": str,
            "uco-observable:ble:referrerUrl": url_object,
            "uco-observable:url": url_object,
            "uco-observable:visitCount": int,
        """
        super().__init__()
        self["@type"] = "uco-observable:URLHistoryFacet"
        self._node_reference_vars(
            **{
                "uco-observable:browserInformation": browser,
            }
        )

        keys_str = (
            "uco-observable:browserUserProfile",
            "uco-observable:hostname",
            "uco-observable:pageTitle",
            "uco-observable:keywordSearchTerm",
            "uco-observable:urlHistoryEntry",
        )
        keys_datetime = (
            "uco-observable:firstVisit",
            "uco-observable:lastVisit",
            "uco-observable:expirationTime",
        )
        keys_int = "uco-observable:visitCount"
        keys_ref = ("uco-observable:ble:referrerUrl", "uco-observable:url")

        self["uco-observable:urlHistoryEntry"] = []
        for entry in history_entries:
            history_entry = {}
            history_entry["@id"] = self.prefix_label + ":" + local_uuid()
            history_entry["@type"] = "uco-observable:URLHistoryEntry"
            for key, var in entry.items():
                if key in keys_str:
                    if isinstance(var, str):
                        history_entry[key] = var
                    else:
                        self.__handle_var_type_errors(key, var, "str")
                elif key in keys_datetime:
                    if isinstance(var, datetime):
                        tz_info = var.strftime("%z")
                        iso_format = (
                            var.isoformat() if tz_info else var.isoformat() + "+00:00"
                        )
                        history_entry[key] = {
                            "@type": "xsd:dateTime",
                            "@value": iso_format,
                        }
                    else:
                        self.__handle_var_type_errors(key, var, "datetime")
                elif key in keys_int:
                    if isinstance(var, int):
                        history_entry[key] = {
                            "@type": "xsd:integer",
                            "@value": str(var),
                        }
                    else:
                        self.__handle_var_type_errors(key, var, "int")
                elif key in keys_ref:
                    if isinstance(var, list) or isinstance(var, tuple):
                        is_object_entity = [isinstance(item, UcoObject) for item in var]
                        if all(is_object_entity):
                            history_entry[key] = [
                                {"@id": item.get_id()} for item in var
                            ]
                        else:
                            self.__handle_list_type_errors(
                                key, var, "UcoObject (no @id key)"
                            )
                    elif isinstance(var, UcoObject):
                        history_entry[key] = {"@id": var.get_id()}
                    else:
                        self.__handle_var_type_errors(
                            key, var, "UcoObject (no @id key)"
                        )
                elif key == "uco-observable:manuallyEnteredCount":
                    history_entry[key] = {
                        "@type": "xsd:nonNegativeInteger",
                        "@value": "%d" % var,
                    }

            self["uco-observable:urlHistoryEntry"].append(history_entry)


class UrlFacet(Facet):
    def __init__(
        self,
        url_address=None,
        url_port=None,
        url_host=None,
        url_fragment=None,
        url_password=None,
        url_path=None,
        url_query=None,
        url_scheme=None,
        url_username=None,
    ):
        """
        :param url_address: an address of a url (i.e. google.ie)
        :param url_port: a tcp or udp port of a url for example 3000
        :param url_host: the Ip address of a host that was requested (e.g.192.168.1.1 could be your home router)
        :param url_fragment: A fragment of a url pointing to a specific resource (i.e  subdomain=api)
        :param url_password: A password that may be used in authentication scheme for accessing restricted resources
        :param url_path: the location that may have resources available e.g. /chatapp
        :param url_query: a query that may be used with a resource such as an api e.g. ?health
        :param url_scheme:  Identifies the type of URL. (e.g. ssh://)
        :param url_username: A username that may be required for authentication for a specific resource. (login)
        """
        super().__init__()
        self["@type"] = "uco-observable:URLFacet"
        self._str_vars(
            **{
                "uco-observable:fullValue": url_address,
                "uco-observable:host": url_host,
                "uco-observable:fragment": url_fragment,
                "uco-observable:password": url_password,
                "uco-observable:path": url_path,
                "uco-observable:query": url_query,
                "uco-observable:scheme": url_scheme,
                "uco-observable:userName": url_username,
            }
        )
        self._int_vars(**{"uco-observable:port": url_port})


class BrowserBookmarkFacet(Facet):
    def __init__(
        self,
        accessedTime=None,
        application_id=None,
        bookmarkPath=None,
        modifiedTime=None,
        createdTime=None,
        urlTargeted_id=None,
        visitCount=None,
    ):
        """
        This CASEObject represents a grouping of characteristics unique to a saved shortcut that directs a
        WWW (World Wide Web) browser software program to a particular WWW accessible resource.
        :param accessedTime: The date and time at which the Object was accessed (dateTime).
        :param application_id: The application associated with this object (ObservableObject).
        :param bookmarkPath: The folder containing the bookmark (string).
        :param modifiedTime: The date and time at which the Object was last modified (dateTime).
        :param createdTime: The date and time at which the observable object being characterized was created (dateTime).
        :param urlTargeted_id: The target of the bookmark. (anyURI).
        :param visitCount: Specifies the number of times a URL has been visited by a particular web browser (integer).
        """
        super().__init__()
        self["@type"] = "uco-observable:BrowserBookmarkFacet"
        self._str_vars(**{"observable:bookmarkPath": bookmarkPath})
        self._int_vars(**{"uco-observable:visitCount": visitCount})
        self._node_reference_vars(
            **{
                "uco-observable:application": application_id,
                "uco-observable:urlTargeted": urlTargeted_id,
            }
        )
        self._datetime_vars(
            **{
                "uco-observable:observableCreatedTime": accessedTime,
                "uco-observable:modifiedTime": modifiedTime,
                "uco-observable:accessedTime": accessedTime,
            }
        )


class RasterPictureFacet(Facet):
    def __init__(
        self,
        camera_id=None,
        bits_per_pixel=None,
        picture_height=None,
        picture_width=None,
        image_compression_method=None,
        picture_type=None,
    ):
        """
        This CASEObject represents the contents of a file or device
        :param camera_id: An observable cyberitem
        :param bits_per_pixel: The phone_number (integer) of bits per pixel
        :param picture_height: The height of a picture (integer)
        :param picture_width: The width of a picture (integer)
        :param image_compression_method: The compression method used
        :param picture_type: The type of picture ("jpg", "png" etc.)
        """
        super().__init__()
        self["@type"] = "uco-observable:RasterPictureFacet"
        self._str_vars(
            **{
                "uco-observable:imageCompressionMethod": image_compression_method,
                "uco-observable:pictureType": picture_type,
            }
        )
        self._int_vars(
            **{
                "uco-observable:pictureHeight": picture_height,
                "uco-observable:pictureWidth": picture_width,
                "uco-observable:bitsPerPixel": bits_per_pixel,
            }
        )
        self._node_reference_vars(**{"uco-observable:camera": camera_id})


class CallFacet(Facet):
    def __init__(
        self,
        application=None,
        call_type=None,
        call_duration=None,
        start_time=None,
        end_time=None,
        call_participant: Union[None, ObservableObject, List[ObservableObject]] = None,
        call_from: Union[None, ObservableObject] = None,
        call_to: Union[None, ObservableObject, List[ObservableObject]] = None,
    ):
        """
        This CASEObject represents a call facet, a grouping of characteristics unique to a
        connection as part of a realtime cyber communication between one or more parties.
        :param call_type: incoming outgoing etc
        :param start_time: the time at which the device registered the call as starting
        :param end_time: the time at which the device registered the call as ending
        :param application: ObservableObject with call-application (e.g. WhatsApp) facet-info
        :param call_from: ObservableObject with person/caller facet-info
        :param call_to: ObservableObject with person/caller facet-info
        :param call_duration: how long the call was registedred on the device as lasting in minutes (E.G. 60)
        :param call_participant: ObservableObject(s) with the account(s) that joined the call
        :param allocation_status: The allocation status of the record of the call i.e intact for records that are
        present on the device
        """
        super().__init__()
        self["@type"] = "uco-observable:CallFacet"
        self._str_vars(
            **{
                "uco-observable:callType": call_type,
            }
        )
        self._datetime_vars(
            **{
                "uco-observable:startTime": start_time,
                "uco-observable:endTime": end_time,
            }
        )
        self._int_vars(**{"uco-observable:duration": call_duration})
        self._node_reference_vars(
            **{
                "uco-observable:application": application,
                "uco-observable:from": call_from,
                "uco-observable:to": call_to,
                "uco-observable:participant": call_participant,
            }
        )


class PhoneAccountFacet(Facet):
    def __init__(self, phone_number=None):
        """
        :param phone_number: The number for this account (e.g., "+16503889249")
        """
        super().__init__()
        self["@type"] = "uco-observable:PhoneAccountFacet"
        self._str_vars(
            **{
                "uco-observable:phoneNumber": phone_number,
            }
        )


class EmailAccountFacet(Facet):
    def __init__(self, email_address):
        """
        :param email_address: An ObservableObject (with EmailAdressFacet)
        """
        super().__init__()
        self["@type"] = "uco-observable:EmailAccountFacet"
        self._node_reference_vars(**{"uco-observable:emailAddress": email_address})


class EmailAddressFacet(Facet):
    def __init__(self, email_address_value=None, display_name=None):
        """
        Used to represent the value of an email address.
        :param email_address_value: a single email address (e.g., "bob@example.com")
        """
        super().__init__()
        self["@type"] = "uco-observable:EmailAddressFacet"
        self._str_vars(
            **{
                "uco-observable:addressValue": email_address_value,
                "uco-observable:displayName": display_name,
            }
        )


class EmailMessageFacet(Facet):
    def __init__(
        self,
        msg_to=None,
        msg_from=None,
        cc=None,
        bcc=None,
        subject=None,
        body=None,
        received_time=None,
        sent_time=None,
        modified_time=None,
        other_headers=None,
        application=None,
        body_raw=None,
        header_raw=None,
        in_reply_to=None,
        sender=None,
        x_originating_ip=None,
        is_read=None,
        content_disposition=None,
        content_type=None,
        message_id=None,
        priority=None,
        x_mailer=None,
        is_mime_encoded=None,
        allocation_status=None,
        is_multipart=None,
    ):
        """
        An instance of an email message, corresponding to the internet message format described in RFC 5322 and related.
        :param msg_to: A list of ObservableObjects (with EmailAccountFacet)
        :param msg_from: An ObservableObject (with EmailAccountFacet)
        :param cc: A list of ObservableObjects (with EmailAccountFacet) in carbon copy
        :param bcc: A list of ObservableObjects (with EmailAccountFacet) in blind carbon copy
        :param subject: The subject of the email.
        :param body: The content of the email.
        :param received_time: The time received, in ISO8601 time format (e.g., "2020-09-29T12:13:01Z")
        :param sent_time: The time sent, in ISO8601 time format (e.g., "2020-09-29T12:13:01Z")
        :param modified_time: The time modified, in ISO8601 time format (e.g., "2020-09-29T12:13:01Z")
        :param other_headers: A dictionary of other headers
        :param application: The application associated with this object.
        :param body_raw:
        :param header_raw:
        :param in_reply_to: One of more unique identifiers for identifying the email(s) this email is a reply to.
        :param sender: ???
        :param x_originating_ip:
        :param is_read: A boolean True/False
        :param content_disposition:
        :param content_type:
        :param message_id: A unique identifier for the message.
        :param priority: The priority of the email.
        :param x_mailer:
        :param is_mime_encoded: A boolean True/False
        :param is_multipart: A boolean True/False
        :param allocation_status:
        """
        super().__init__()
        self["@type"] = "uco-observable:EmailMessageFacet"
        self._str_vars(
            **{
                "uco-observable:subject": subject,
                "uco-observable:body": body,
                "uco-observable:otherHeaders": other_headers,
                "uco-observable:bodyRaw": body_raw,
                "uco-observable:headerRaw": header_raw,
                "uco-observable:contentDisposition": content_disposition,
                "uco-observable:contentType": content_type,
                "uco-observable:messageID": message_id,
                "uco-observable:priority": priority,
                "uco-observable:xMailer": x_mailer,
                "uco-observable:allocationStatus": allocation_status,
            }
        )
        self._datetime_vars(
            **{
                "uco-observable:receivedTime": received_time,
                "uco-observable:sentTime": sent_time,
                "uco-core:objectModifiedTime": modified_time,
            }
        )
        self._bool_vars(
            **{
                "uco-observable:isRead": is_read,
                "uco-observable:isMimeEncoded": is_mime_encoded,
                "uco-observable:isMultipart": is_multipart,
            }
        )
        self._node_reference_vars(
            **{
                "uco-observable:from": msg_from,
                "uco-observable:to": msg_to,
                "uco-observable:cc": cc,
                "uco-observable:bcc": bcc,
                "uco-observable:inReplyTo": in_reply_to,
                "uco-observable:sender": sender,
                "uco-observable:xOriginatingIP": x_originating_ip,
                "uco-observable:application": application,
            }
        )


class EXIFFacet(Facet):
    def __init__(self, **kwargs):
        """
        Specifies exchangeable image file format (Exif) metadata tags for image and sound files recorded by digital cameras.
        :param kwargs: The user provided key/value pairs of exif items (e.g., Make="Canon", etc.).
        """
        super().__init__()
        self["@type"] = "uco-observable:EXIFFacet"

        self["uco-observable:exifData"] = {
            "@id": self.prefix_label + ":" + str(local_uuid()),
            "@type": "uco-types:ControlledDictionary",
            "uco-types:entry": [],
        }
        for k, v in kwargs.items():
            if v not in ["", " "]:
                item = {
                    "@id": self.prefix_label + ":" + str(local_uuid()),
                    "@type": "uco-types:ControlledDictionaryEntry",
                    "uco-types:key": k,
                    "uco-types:value": v,
                }
                self["uco-observable:exifData"]["uco-types:entry"].append(item)


class ExtInodeFacet(Facet):
    def __init__(
        self,
        deletion_time=None,
        inode_change_time=None,
        file_type=None,
        flags=None,
        hard_link_count=None,
        inode_id=None,
        permissions=None,
        sgid=None,
        suid=None,
    ):
        """
        An instance of an email message, corresponding to the internet message format described in RFC 5322 and related.
        :param deletion_time: Specifies the time at which the file represented by an Inode was 'deleted'.
        :param inode_change_time: The date and time at which the file Inode metadata was last modified.
        :param file_type: Specifies the EXT file type (FIFO, Directory, Regular file, Symbolic link, etc) for the Inode.
        :param flags: Specifies user flags to further protect (limit its use and modification) the file represented by an Inode.
        :param hard_link_count: Specifies a count of how many hard links point to an Inode.
        :param inode_id: Specifies a single Inode identifier.
        :param permissions: Specifies the read/write/execute permissions for the file represented by an EXT Inode.
        :param sgid: Specifies the group ID for the file represented by an Inode.
        :param suid: Specifies the user ID that 'owns' the file represented by an Inode.
        """
        super().__init__()
        self["@type"] = "uco-observable:ExtInodeFacet"
        self._int_vars(
            **{
                "uco-observable:extFileType": file_type,
                "uco-observable:extFlags": flags,
                "uco-observable:extHardLinkCount": hard_link_count,
                "uco-observable:extPermissions": permissions,
                "uco-observable:extSGID": sgid,
                "uco-observable:extSUID": suid,
                "uco-observable:extInodeID": inode_id,
            }
        )
        self._datetime_vars(
            **{
                "uco-observable:extDeletionTime": deletion_time,
                "uco-observable:extInodeChangeTime": inode_change_time,
            }
        )


class CalendarEntryFacet(Facet):
    def __init__(
        self,
        application: Union[None, UcoObject] = None,
        attendant: Union[None, Identity, List[Identity]] = None,
        duration: Optional[int] = None,
        end_time=None,
        event_status: Optional[str] = None,
        event_type: Optional[str] = None,
        is_private: Optional[bool] = None,
        location: Union[None, UcoObject] = None,
        modified_time=None,
        observable_created_time=None,
        owner: Union[None, UcoObject] = None,
        recurrence: Optional[str] = None,
        remind_time=None,
        start_time=None,
        subject: Optional[str] = None,
    ):
        super().__init__()
        self["@type"] = "uco-observable:CalendarEntryFacet"
        self._str_vars(
            **{
                "uco-observable:eventStatus": event_status,
                "uco-observable:eventType": event_type,
                "uco-observable:subject": subject,
                "uco-observable:recurrence": recurrence,
            }
        )
        self._datetime_vars(
            **{
                "uco-observable:startTime": start_time,
                "uco-observable:endTime": end_time,
                "uco-observable:remindTime": remind_time,
                "uco-observable:observableCreatedTime": observable_created_time,
                "uco-observable:modifiedTime": modified_time,
            }
        )
        self._int_vars(**{"uco-observable:duration": duration})
        self._bool_vars(**{"uco-observable:isPrivate": is_private})
        self._node_reference_vars(
            **{
                "uco-observable:application": application,
                "uco-observable:attendant": attendant,
                "uco-observable:location": location,
                "uco-observable:owner": owner,
            }
        )


class BrowserCookieFacet(Facet):
    def __init__(
        self,
        name=None,
        path=None,
        created_time=None,
        last_access_time=None,
        expiration_time=None,
        secure=None,
    ):
        super().__init__()
        self["@type"] = "uco-observable:BrowserCookieFacet"
        self._str_vars(
            **{"uco-observable:cookieName": name, "uco-observable:cookiePath": path}
        )
        self._datetime_vars(
            **{
                "uco-observable:observableCreatedTime": created_time,
                "uco-observable:lastAccessTime": last_access_time,
                "uco-observable:expirationTime": expiration_time,
            }
        )
        self._bool_vars(**{"uco-observable:isSecure": secure})


class File(ObservableObject):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self["@type"] = "uco-observable:File"


class FileFacet(Facet):
    def __init__(
        self,
        file_accessed_time=None,
        file_allocation_status: Optional[str] = None,
        file_extension: Optional[str] = None,
        file_name: Optional[str] = None,
        file_path: Optional[str] = None,
        file_is_directory: Optional[bool] = None,
        file_metadata_changed_time: Optional[datetime] = None,
        file_modified_time: Optional[datetime] = None,
        file_created_time: Optional[datetime] = None,
        file_size_bytes: Union[int, None] = None,
        file_mime_type: Optional[str] = None,
    ):
        """
        The basic properties associated with the storage of a file on a file system.
        :param file_name: Specifies the name associated with a file in a file system (e.g., "IMG_0123.jpg").
        :param file_allocation_status: the allocation status of a file.
        :param file_path: Specifies the file path for the location of a file within a filesystem. (e.g., "/sdcard/IMG_0123.jpg")
        :param file_extension: The file name extension. Not present if the file has no dot in its account_name. (e.g., "jpg").
        :param file_is_directory: Specifies whether a file entry represents a directory.
        :param size_bytes: The size of the data in bytes (e.g., integer like 35125)
        :param file_accessed_time: The datetime the file was last accessed
        :param file_created_time: The datetime the file was created
        :param file_modified_time: The datetime the file was last modified
        :param file_metadata_changed_time: The last change to metadata of a file but not necessarily the file contents
        :param file_mime_type: A generic (string) tag/label of e file, or example 'text/html' or 'audio/mp3.
        """
        super().__init__()
        self["@type"] = "uco-observable:FileFacet"
        self._str_vars(
            **{
                "uco-observable:fileName": file_name,
                "uco-observable:filePath": file_path,
                "uco-observable:extension": file_extension,
                "uco-observable:allocationStatus": file_allocation_status,
                "uco-observable:mimeType": file_mime_type,
            }
        )
        self._datetime_vars(
            **{
                "uco-observable:accessedTime": file_accessed_time,
                "uco-observable:observableCreatedTime": file_created_time,
                "uco-observable:modifiedTime": file_modified_time,
                "uco-observable:metadataChangeTime": file_metadata_changed_time,
            }
        )
        self._int_vars(**{"uco-observable:sizeInBytes": file_size_bytes})
        self._bool_vars(**{"uco-observable:isDirectory": file_is_directory})


class MessageFacet(Facet):
    def __init__(
        self,
        msg_to=None,
        msg_from=None,
        message_text=None,
        sent_time=None,
        application=None,
        message_type=None,
        message_id=None,
        session_id=None,
    ):
        """
        Characteristics of an electronic message.
        :param msg_to: A list of ObservableObjects
        :param msg_from: An ObservableObject
        :param message_text: The content of the email.
        :param sent_time: The time sent, in ISO8601 time format (e.g., "2020-09-29T12:13:01Z")
        :param application: The application associated with this object.
        :param message_type:
        :param message_id: A unique identifier for the message.
        :param session_id: The priority of the email.
        """
        super().__init__()
        self["@type"] = "uco-observable:MessageFacet"
        self._str_vars(
            **{
                "uco-observable:messageText": message_text,
                "uco-observable:messageType": message_type,
                "uco-observable:messageID": message_id,
                "uco-observable:sessionID": session_id,
            }
        )
        self._datetime_vars(**{"uco-observable:sentTime": sent_time})
        self._node_reference_vars(
            **{
                "uco-observable:from": msg_from,
                "uco-observable:to": msg_to,
                "uco-observable:application": application,
            }
        )


class MobileDeviceFacet(Facet):
    def __init__(
        self,
        ESN: Optional[str] = None,
        IMEI: Optional[str] = None,
        bluetooth_device_name: Optional[str] = None,
        keypad_unlock_code: Optional[str] = None,
        storage_capacity_in_bytes: Optional[int] = None,
        phone_activation_time: Optional[datetime] = None,
    ):
        """
        The basic properties associated with a phone and phone account of a device or user.
        :param IMSI International mobile subscriber identity
        :param ICCID Integrated Circuit Card Identification Number
        :param IMEI international mobile equipment identity
        :param storage_capacity storage capacity of device in bytes
        :param MSISDN mobile station international subscriber directory number
        """
        super().__init__()
        self["@type"] = "uco-observable:MobileDeviceFacet"
        self._str_vars(
            **{
                "uco-observable:IMEI": IMEI,
                "uco-observable:keypadUnlockCode": keypad_unlock_code,
                "uco-observable:bluetoothDeviceName": bluetooth_device_name,
            }
        )
        self._int_vars(
            **{
                "uco-observable:storageCapacityInBytes": storage_capacity_in_bytes,
            }
        )
        self._datetime_vars(
            **{
                "observable:phoneActivationTime": phone_activation_time,
            }
        )


class SimCardFacet(Facet):
    def __init__(
        self,
        ICCID: Optional[str] = None,
        IMSI: Optional[str] = None,
        PIN: Optional[str] = None,
        PUK: Optional[str] = None,
        SIM_form: Optional[str] = None,
        SIM_type: Optional[str] = None,
        carrier: Union[None, Identity] = None,
        storage_capacity_in_bytes: Optional[int] = None,
    ):
        """
        A SIM card facet is a grouping of characteristics unique to
        a subscriber identification module card.
        :param ICCID Integrated Circuit Card Identification Number.
        :param IMSI International mobile subscriber identity.
        :param PIN Personal Identification Number (PIN).
        :patam PUK Personal Unlocking Key (PUK) to unlock the SIM card.
        :param SIM_form The form of SIM card such as SIM, Micro SIM, Nano SIM.
        :param SIM_type The type of SIM card such as SIM, USIM, UICC.
        :param carrier Telecommunications service provider that sold the SIM card.
        :param storage_capacity_in_bytes The number of bytes that can be stored on a SIM card.
        """
        super().__init__()
        self["@type"] = "uco-observable:SIMCardFacet"
        self._str_vars(
            **{
                "uco-observable:ICCID": ICCID,
                "uco-observable:IMSI": IMSI,
                "uco-observable:PIN": PIN,
                "uco-observable:PUK": PUK,
                "uco-observable:SIMForm": SIM_form,
                "uco-observable:SIMType": SIM_type,
            }
        )
        self._int_vars(
            **{
                "uco-observable:storageCapacityInBytes": storage_capacity_in_bytes,
            }
        )
        self._node_reference_vars(
            **{
                "uco-observable:carrier": carrier,
            }
        )


class OperatingSystemFacet(Facet):
    def __init__(
        self,
        *args: Any,
        os_advertisingID: Optional[str] = None,
        os_bitness: Optional[str] = None,
        os_install_date: Optional[datetime] = None,
        os_isLimitAdTrackingEnabled: Optional[bool] = None,
        os_manufacturer: Union[None, Identity] = None,
        os_version: Optional[str] = None,
        os_environment_variables: Union[None, Dict, Dictionary] = None,
        **kwargs: Any,
    ):
        super().__init__()

        self["@type"] = "uco-observable:OperatingSystemFacet"

        # Handle case where environment variables dictionary is provided as a plain Python dict.
        if os_environment_variables is not None:
            if isinstance(os_environment_variables, Dictionary):
                self._node_reference_vars(
                    **{
                        "uco-observable:environmentVariables": os_environment_variables,
                    }
                )
            else:
                _os_environment_variables = Dictionary()
                _os_environment_variables._dict_var(os_environment_variables)
                self["uco-observable:environmentVariables"] = _os_environment_variables

        self._str_vars(
            **{
                "uco-observable:advertisingID": os_advertisingID,
                "uco-observable:bitness": os_bitness,
                "uco-observable:version": os_version,
            }
        )
        self._datetime_vars(**{"uco-observable:installDate": os_install_date})

        self._bool_vars(
            **{"uco-observable:isLimitAdTrackingEnabled": os_isLimitAdTrackingEnabled}
        )
        self._node_reference_vars(
            **{
                "uco-observable:manufacturer": os_manufacturer,
            }
        )


class PathRelationFacet(Facet):
    def __init__(self, path: str) -> None:
        """
        This CASE object specifies the location of one object within another containing object.
        :param path: The full path to the object (e.g, "/sdcard/IMG_0123.jpg")
        """
        super().__init__()
        self["@type"] = "uco-observable:PathRelationFacet"
        self._str_vars(**{"uco-observable:path": path})


class EventRecordFacet(Facet):
    def __init__(
        self,
        account: Union[None, UcoObject] = None,
        application: Union[None, UcoObject] = None,
        cyber_action: Union[None, UcoObject] = None,
        end_time: Optional[datetime] = None,
        event_record_device: Union[None, UcoObject] = None,
        event_record_id: Optional[str] = None,
        event_record_raw: Optional[str] = None,
        event_record_service_name: Optional[str] = None,
        event_record_text: Optional[str] = None,
        event_type: Optional[str] = None,
        observable_created_time: Optional[datetime] = None,
        start_time: Optional[datetime] = None,
    ):
        """
         An event facet is a grouping of characteristics unique to something that happens in a digital context
         (e.g., operating system events).
        :param account: Specifies the account referenced in an event log entry or
                        used to run the scheduled task.
        :param application: The application associated with this object.
        :param cyber_action: The action taken in response to the event.
        :param end_time: The date and time at which the observable object being characterized ended.
        :param event_record_device: The device where the event has been registered.
        :param event_record_id: The identifier of the event.
        :param event_record_raw: The complete raw content of the event record.
        :param event_record_service_name: The service that generated the event record.
        :param event_record_text: The textual representation of the event.
        :param event_type: The type of the event, for example 'information', 'warning' or 'error'.
        :param observable_created_time: The date and time at which the observable object being characterized was created.
        :param start_time: The date and time at which the observable object being characterized started.
        """
        super().__init__()
        self["@type"] = "uco-observable:EventRecordFacet"
        self._str_vars(
            **{
                "uco-observable:eventRecordID": event_record_id,
                "uco-observable:eventRecordRaw": event_record_raw,
                "uco-observable:eventRecordServiceName": event_record_service_name,
                "uco-observable:eventRecordText": event_record_text,
                "uco-observable:eventType": event_type,
            }
        )
        self._node_reference_vars(
            **{
                "uco-observable:account": account,
                "uco-observable:application": application,
                "uco-observable:cyberAction": cyber_action,
                "uco-observable:eventRecordDevice": event_record_device,
            }
        )
        self._datetime_vars(
            **{
                "uco-observable:observableCreatedTime": observable_created_time,
                "uco-observable:startTime": start_time,
                "uco-observable:endTime": end_time,
            }
        )


class ObservableRelationship(Observable, Relationship):
    def __init__(
        self,
        *args: Any,
        source: UcoObject,
        target: UcoObject,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        kind_of_relationship: str,
        directional: bool = False,
        **kwargs: Any,
    ) -> None:
        """
        This object represents an assertion that one or more observable objects are related to another object in some way.  Other parameters are as in uco.core.Relationship.
        :param source: An observable object (specialized over Relationship)
        :param target: An observable object (specialized over Relationship)
        """
        if not isinstance(source, Observable):
            raise TypeError(
                "The source of an ObservableRelationship must be an Observable."
            )
        if not isinstance(target, Observable):
            raise TypeError(
                "The target of an ObservableRelationship must be an Observable."
            )
        super().__init__(
            *args,
            source=source,
            target=target,
            start_time=start_time,
            end_time=end_time,
            kind_of_relationship=kind_of_relationship,
            directional=directional,
            **kwargs,
        )
        self["@type"] = "uco-observable:ObservableRelationship"


class ApplicationAccountFacet(Facet):
    def __init__(self, application=None):
        """
        An application account facet is a grouping of characteristics unique to an account within a particular software
        program designed for end users.
        :param application: An Observable Object (containing an Application Facet)
        """
        super().__init__()
        self["@type"] = "uco-observable:ApplicationAccountFacet"
        self._node_reference_vars(**{"uco-observable:application": application})


class DigitalAccountFacet(Facet):
    def __init__(
        self,
        display_name=None,
        login=None,
        first_login_time=None,
        disabled=None,
        last_login_time=None,
    ):
        """
        A digital account facet is a grouping of characteristics unique to an arrangement with an entity to enable and
        control the provision of some capability or service within the digital domain.
        """
        super().__init__()
        self["@type"] = "uco-observable:DigitalAccountFacet"
        self._str_vars(
            **{
                "uco-observable:displayName": display_name,
                "uco-observable:accountLogin": login,
            }
        )
        self._datetime_vars(
            **{
                "uco-observable:firstLoginTime": first_login_time,
                "uco-observable:lastLoginTime": last_login_time,
            }
        )
        self._bool_vars(**{"uco-observable:isDisabled": disabled})


class CellSiteFacet(Facet):
    def __init__(
        self,
        cell_site_country_code: Optional[str] = None,
        cell_site_identifier: Optional[str] = None,
        cell_site_location_area_code: Optional[str] = None,
        cell_site_network_code: Optional[str] = None,
        cell_site_type: Optional[str] = None,
    ):
        """
        A cell site facet contains the metadata surrounding the cell site.
        :param cell_site_country_code: he country code represents the country of the
        cell site. For GSM, this is the Mobile Country Code (MCC).
        :param cell_site_identifier: Specifies the unique number used to identify each
        Cell Site within a location area code.
        :param cell_site_location_area_code: The location area code is a unique number
        of current location area of the cell site.
        :param cell_site_network_code: This code identifies the mobile operator of
        the cell site.
        :param cell_site_type: Specifies the technology used by the Cell Site
        (e.g., GSM, CDMA, or LTE).
        """
        super().__init__()
        self["@type"] = "uco-observable:CellSiteFacet"
        self._str_vars(
            **{
                "uco-observable:cellSiteCountryCode": cell_site_country_code,
                "uco-observable:cellSiteIdentifier": cell_site_identifier,
                "uco-observable:cellSiteLocationAreaCode": cell_site_location_area_code,
                "uco-observable:cellSiteNetworkCode": cell_site_network_code,
                "uco-observable:cellSiteType": cell_site_type,
            }
        )


class WirelessNetworkConnectionFacet(Facet):
    def __init__(
        self,
        wn_base_station: Optional[str] = None,
        wn_password: Optional[str] = None,
        wn_ssid: Optional[str] = None,
        wn_wireless_network_security_mode: Optional[str] = None,
    ):
        """
        A wireless network connection facet is a grouping of characteristics unique to a connection (completed or
        attempted) across an IEEE 802.11 standards-conformant digital network (a group of two or more computer systems
        linked together).
        """
        super().__init__()
        self["@type"] = "uco-observable:WirelessNetworkConnectionFacet"
        self._str_vars(
            **{
                "uco-observable:baseStation": wn_base_station,
                "uco-observable:password": wn_password,
                "uco-observable:ssid": wn_ssid,
                "observable:wirelessNetworkSecurityMode": wn_wireless_network_security_mode,
            }
        )


class SMSMessageFacet(Facet):
    def __init__(
        self,
        msg_to=None,
        msg_from=None,
        message_text=None,
        sent_time=None,
        application=None,
        message_type=None,
        message_id=None,
        session_id=None,
    ):
        """
        Characteristics of an electronic message.
        :param msg_to: A list of ObservableObjects
        :param msg_from: An ObservableObject
        :param message_text: The content of the email.
        :param sent_time: The time sent, in ISO8601 time format (e.g., "2020-09-29T12:13:01Z")
        :param application: The application associated with this object.
        :param message_type:
        :param message_id: A unique identifier for the message.
        :param session_id: The priority of the email.
        """
        super().__init__()
        self["@type"] = "uco-observable:SMSMessageFacet"
        self._str_vars(
            **{
                "uco-observable:messageText": message_text,
                "uco-observable:messageType": message_type,
                "uco-observable:messageID": message_id,
                "uco-observable:sessionID": session_id,
            }
        )
        self._datetime_vars(**{"uco-observable:sentTime": sent_time})
        self._node_reference_vars(
            **{
                "uco-observable:from": msg_from,
                "uco-observable:to": msg_to,
                "uco-observable:application": application,
            }
        )


class MessagethreadFacet(Facet):
    def __init__(
        self,
        visibility: Optional[bool] = None,
        participants=None,
        messages=None,
    ):
        """
        A message thread facet is a grouping of characteristics unique to a running
        commentary of electronic messages pertaining to one topic or question.
        :param visibility: A boolean value to indicate if the thread is private (False) or
        public (True).
        :param participants: Array of Account ObservableObject,
        :param messages: Array of Message ObservableObjects.
        """
        super().__init__()
        self["@type"] = "uco-observable:MessageThreadFacet"
        self._bool_vars(**{"uco-observable:visibility": visibility})
        self._node_reference_vars(**{"uco-observable:participant": participants})

        self["uco-observable:messageThread"] = {
            "@id": self.prefix_label + ":" + local_uuid(),
            "@type": "uco-types:Thread",
        }
        self["uco-observable:messageThread"]["co:size"] = {
            "@type": "xsd:nonNegativeInteger",
            "@value": str(len(messages)),
        }
        list_id_messages = list()
        for m in messages:
            list_id_messages.append({"@id": m.get_id()})
        self["uco-observable:messageThread"]["co:element"] = list_id_messages

    def append_messages(self, messages):
        raise NotImplementedError(
            "TODO - Need to implement checker for thread having only one terminus."
        )

    def append_participants(self, *args):
        self._append_refs("uco-observable:participant", *args)


class MessageThread(UcoObject):
    def __init__(self, name=None, facets=None):
        super().__init__()
        self["@type"] = "uco-observable:MessageThread"
        self._str_vars(**{"uco-core:name": name})
        self.append_facets(facets)


class Message(UcoObject):
    def __init__(self, has_changed=None, state=None, indexed_items=None):
        """
        A message is a discrete unit of electronic communication intended by the source for consumption by some
        recipient or group of recipients. [based on https://en.wikipedia.org/wiki/Message]
        """
        super().__init__()
        self["@type"] = "uco-observable:Message"
        self._str_vars(**{"uco-observable:state": state})
        self._bool_vars(**{"uco-observable:hasChanged": has_changed})
        self.append_indexed_items(indexed_items)


class DiskPartitionFacet(Facet):
    def __init__(
        self,
        serial_number=None,
        partition_type=None,
        total_space=None,
        space_left=None,
        space_used=None,
        offset=None,
    ):
        """
        Used to represent Disk Partition
        :param serial_number: disk partition identifier
        :param partition_type: FAT32, NTFS etc.
        :param total_space: free space
        :param space_left: total - used space
        :param space_used: used space
        :param space_used: the offset to the beginning of the disk
        """
        super().__init__()
        self["@type"] = "uco-observable:DiskPartitionFacet"
        self._str_vars(
            **{
                "uco-observable:serialNumber": serial_number,
                "uco-observable:diskPartitionType": partition_type,
            }
        )
        self._int_vars(
            **{
                "uco-observable:totalSpace": total_space,
                "uco-observable:spaceLeft": space_left,
                "uco-observable:spaceUsed": space_used,
                "uco-observable:partitionOffset": offset,
            }
        )


class DiskFacet(Facet):
    def __init__(self, disk_type=None, size=None, partition=None):
        """
        Used to represent Fixed Disk
        :param disk_type: Fixed default value
        :param size: disk size
        :param partition: array of @id references to the partitions contained
        """
        super().__init__()
        self["@type"] = "uco-observable:DiskFacet"
        self._str_vars(**{"uco-observable:diskType": disk_type})
        self._int_vars(**{"uco-observable:diskSize": size})
        self._node_reference_vars(**{"uco-observable:partition": partition})


directory = {
    "uco-observable:DomainName": ObservableDomainName,
    "uco-observable:DomainNameFacet": DomainNameFacet,
    "uco-observable:HostName": ObservableHostName,
    "uco-observable:IPv4Address": ObservableIPv4Address,
    "uco-observable:IPv4AddressFacet": IPv4AddressFacet,
    "uco-observable:AutonomousSystem": ObservableAutonomousSystem,
    "uco-observable:AutonomousSystemFacet": AutonomousSystemFacet,
    "uco-observable:AccountFacet": AccountFacet,
    "uco-observable:AccountAuthenticationFacet": AccountAuthenticationFacet,
    "uco-observable:ContentDataFacet": ContentDataFacet,
    "uco-observable:ApplicationFacet": ApplicationFacet,
    "uco-observable:ApplicationVersion": ObservableApplicationVersion,
    "uco-observable:DataRangeFacet": DataRangeFacet,
    "uco-observable:DeviceFacet": DeviceFacet,
    "uco-observable:WifiAddressFacet": WifiAddressFacet,
    "uco-observable:BluetoothAddressFacet": BluetoothAddressFacet,
    "uco-observable:ObservableObject": ObservableObject,
    "uco-observable:URLHistoryFacet": UrlHistoryFacet,
    "uco-observable:URLFacet": UrlFacet,
    "uco-observable:RasterPictureFacet": RasterPictureFacet,
    "uco-observable:CallFacet": CallFacet,
    "uco-observable:PhoneAccountFacet": PhoneAccountFacet,
    "uco-observable:EmailAccountFacet": EmailAccountFacet,
    "uco-observable:EmailAddressFacet": EmailAddressFacet,
    "uco-observable:EmailMessageFacet": EmailMessageFacet,
    "uco-observable:EXIFFacet": EXIFFacet,
    "uco-observable:ExtInodeFacet": ExtInodeFacet,
    "uco-observable:CalendarEntryFacet": CalendarEntryFacet,
    "uco-observable:BrowserCookieFacet": BrowserCookieFacet,
    "uco-observable:FileFacet": FileFacet,
    "uco-observable:MessageFacet": MessageFacet,
    "uco-observable:SMSMessageFacet": SMSMessageFacet,
    "uco-observable:MobileDeviceFacet": MobileDeviceFacet,
    "uco-observable:SIMCardFacet": SimCardFacet,
    "uco-observable:OperatingSystemFacet": OperatingSystemFacet,
    "uco-observable:PathRelationFacet": PathRelationFacet,
    "uco-observable:EventRecordFacet": EventRecordFacet,
    "uco-observable:ObservableRelationship": ObservableRelationship,
    "uco-observable:ApplicationAccountFacet": ApplicationAccountFacet,
    "uco-observable:DigitalAccountFacet": DigitalAccountFacet,
    "uco-observable:WirelessNetworkConnectionFacet": WirelessNetworkConnectionFacet,
    "uco-observable:MessageThreadFacet": MessagethreadFacet,
    "uco-observable:Message": Message,
    "uco-observable:MessageThread": MessageThread,
    "uco-observable:DiskPartitionFacet": DiskPartitionFacet,
    "uco-observable:DiskFacet": DiskFacet,
    "uco-observable:X509Certificate": X509Certificate,
    "uco-observable:X509CertificateFacet": X509CertificateFacet,
}
