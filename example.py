from datetime import datetime, timedelta, timezone

import cdo_local_uuid

from case_mapping import base, case, drafting, uco

# This is part of enabling non-random UUIDs for the demonstration
# output. The other part is handled at call time, and can be seen in
# the documentation for cdo_local_uuid._demo_uuid().
cdo_local_uuid.configure()

_current_timestamp_count = 0


def _next_timestamp() -> datetime:
    """
    This example previously used datetime.now(timezone.utc) to generate
    timestamps. This function instead creates a fixed-value timestamp
    sequence, to reduce diff noise from timestamps when re-running the
    example script.
    """
    global _current_timestamp_count
    base_timestamp = datetime(2023, 1, 1, 1, 1, 1, 1, timezone.utc)
    base_delta = timedelta(minutes=1, seconds=1, microseconds=1)
    _current_timestamp_count += 1
    return base_timestamp + _current_timestamp_count * base_delta


# Generate a case bundle and list to hold investigation items
bundle = uco.core.Bundle(description="An Example Case File")
investigation_items: list[base.FacetEntity] = []

############################################
# A DeviceFacet and a OperatingSystemFacet #
############################################
device_camera = uco.observable.ObservableObject()
manufacturer_nikon = uco.identity.Organization(name="Nikon")
bundle.append_to_uco_object(manufacturer_nikon)
device1 = uco.observable.FacetDevice(manufacturer=manufacturer_nikon, model="D750")
os_date = datetime.strptime("2023-02-19T09:22:09", "%Y-%m-%dT%H:%M:%S")
manufacturer_apple = uco.identity.Organization(name="Apple")
os_env_vars = {
    "path": "/opt/local/bin:/opt/local/sbin:/usr/bin:",
    "temp": "/tmp:/usr/temp",
    "systemroot": "/root",
}

os_facet = uco.observable.FacetOperatingSystem(
    os_manufacturer=manufacturer_apple,
    os_advertisingID="DX4CDXKN",
    os_bitness="64-bit",
    os_install_date=os_date,
    os_isLimitAdTrackingEnabled=True,
    os_version="17.4.1",
    os_environment_variables=os_env_vars,
)

device_camera.append_facets(device1, os_facet)
bundle.append_to_uco_object(device_camera)

##################################
# A file to be added to the case #
##################################
sd_card = uco.observable.ObservableObject()
investigation_items.append(sd_card)

f_date_created = datetime.strptime("2024-04-18T12:06:33", "%Y-%m-%dT%H:%M:%S")
f_date_modified = datetime.strptime("2024-04-21T12:06:33", "%Y-%m-%dT%H:%M:%S")
f_date_metadata = datetime.strptime("2024-04-21T10:16:43", "%Y-%m-%dT%H:%M:%S")

file1 = uco.observable.FacetFile(
    file_allocation_status="Contiguous Allocation",
    file_extension="jpg",
    file_name="IMG_0123.jpg",
    file_path="/sdcard/ImG_0123.jpg",
    file_is_directory=False,
    file_metadata_changed_time=f_date_metadata,
    file_modified_time=f_date_modified,
    file_created_time=f_date_created,
    file_size_bytes=35002,
    file_mime_type="image/jpeg",
)

file_content1 = uco.observable.FacetContentData(
    byte_order="Big-endian",
    magic_number="/9j/ww==",
    mime_type="image/jpeg",
    size_bytes=35000,
    data_payload="<base 64 encoded data of the file>",
    hash_method="SHA256",
    hash_value="11122273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b",
)
file_raster1 = uco.observable.FacetRasterPicture(
    picture_type="jpg", picture_height=12345, picture_width=12346, bits_per_pixel=2
)

exif = {"Make": "Canon", "Model": "Powershot"}
file_exif1 = uco.observable.FacetEXIF(**exif)
sd_card.append_facets(file1, file_content1, file_raster1, file_exif1)
bundle.append_to_uco_object(sd_card)

#######################################
# An investigative action on a device #
#######################################
inv_act = case.investigation.InvestigativeAction(
    name="annotated",
    start_time=_next_timestamp(),
    end_time=_next_timestamp(),
)
investigation_items.append(inv_act)  # NOTE: Appending whole object not just id
bundle.append_to_uco_object(manufacturer_apple)
device2 = uco.observable.FacetDevice(
    device_type="iPhone", manufacturer=manufacturer_apple, model="6XS", serial="77"
)
# inv_act.append_facets(action_ref, device2)
inv_act.append_facets(device2)
bundle.append_to_uco_object(inv_act)

#############################################################
# Another investigative action on a device, multiple facets #
#############################################################
inv_act9 = case.investigation.InvestigativeAction(
    name="annotated",
    start_time=_next_timestamp(),
    end_time=_next_timestamp(),
)
dummy_observable = uco.observable.ObservableObject(
    state="this is a dummy observable created as an example"
)
manufacturer_oneplus = uco.identity.Organization(name="oneplus")
bundle.append_to_uco_object(manufacturer_oneplus)
device9 = uco.observable.FacetDevice(
    device_type="Android", manufacturer=manufacturer_oneplus, model="8", serial="123123"
)
inv_act9.append_facets(device9)
bundle.append_to_uco_object(inv_act9)

##############################
# Adding a CASE Relationship #
##############################
cyber_rel1 = uco.observable.ObservableRelationship(
    source=device_camera,
    target=sd_card,
    kind_of_relationship="Contained_Within",
    directional=True,
)
path_rel1 = uco.observable.FacetPathRelation(path="/sdcard/IMG_0123.jpg")
cyber_rel1.append_facets(path_rel1)
bundle.append_to_uco_object(cyber_rel1)

##############################
# Adding an Email Account    #
##############################
email_address_object_1 = uco.observable.ObservableObject()
email_address_1 = uco.observable.FacetEmailAddress(
    email_address_value="info@example.com", display_name="Example User"
)
email_address_object_1.append_facets(email_address_1)

email_account_object_1 = uco.observable.ObservableObject()
account_1 = uco.observable.FacetEmailAccount(email_address=email_address_object_1)
email_account_object_1.append_facets(account_1)
bundle.append_to_uco_object(email_account_object_1, email_address_object_1)

email_address_object_2 = uco.observable.ObservableObject()
email_address_2 = uco.observable.FacetEmailAddress(
    email_address_value="admin@example.com", display_name="Example Admin"
)
email_address_object_2.append_facets(email_address_2)

email_account_object_2 = uco.observable.ObservableObject()
account_2 = uco.observable.FacetEmailAccount(email_address=email_address_object_2)
email_account_object_2.append_facets(account_2)
bundle.append_to_uco_object(email_account_object_2, email_address_object_2)

##############################
#  Adding an Email Message   #
##############################
cyber_item3 = uco.observable.ObservableObject()
email_msg = uco.observable.FacetEmailMessage(
    msg_to=[email_address_object_1, email_address_object_2],
    msg_from=email_address_object_1,
    subject="Thoughts on Our Next Book Club Pick?",
    body="Hello fellow bookworms! It's that time again.",
    sent_time=_next_timestamp(),
    received_time=_next_timestamp(),
    message_id="<1234567890@example.com>",
)
cyber_item3.append_facets(email_msg)
bundle.append_to_uco_object(cyber_item3)


###################################################
#  Adding an FacetUrlHistory and aUrlHistoryEntry #
###################################################
url_object = uco.observable.ObservableObject()
url_facet = uco.observable.FacetUrl(url_address="www.docker.com/howto")
url_object.append_facets(url_facet)
bundle.append_to_uco_object(url_object)

browser_object = uco.observable.ObservableObject()
browser_facet = uco.observable.FacetApplication(app_name="Safari")
browser_object.append_facets(browser_facet)
bundle.append_to_uco_object(browser_object)

url_date_expiration = datetime.strptime("2024-12-27T14:55:01", "%Y-%m-%dT%H:%M:%S")
url_date_first = datetime.strptime("2024-01-02T15:55:01", "%Y-%m-%dT%H:%M:%S")
url_date_last = datetime.strptime("2024-02-10T10:55:01", "%Y-%m-%dT%H:%M:%S")

history_entries = []
history_entry_1 = {
    "uco-observable:browserUserProfile": "Jill",
    "uco-observable:expirationTime": url_date_expiration,
    "uco-observable:firstVisit": url_date_first,
    "uco-observable:hostname": "case_test",
    "uco-observable:keywordSearchTerm": "docker",
    "uco-observable:lastVisit": url_date_last,
    "uco-observable:manuallyEnteredCount": 10,
    "uco-observable:pageTitle": "Docker tutorial",
    "uco-observable:referrerUrl": url_object,
    "uco-observable:url": url_object,
    "uco-observable:visitCount": 18,
}
history_entry_2 = {
    "uco-observable:browserUserProfile": "Tamasin",
    "uco-observable:expirationTime": url_date_expiration,
    "uco-observable:firstVisit": url_date_first,
    "uco-observable:hostname": "case_test",
    "uco-observable:keywordSearchTerm": "git actions",
    "uco-observable:lastVisit": url_date_last,
    "uco-observable:manuallyEnteredCount": 21,
    "uco-observable:pageTitle": "GitHub actions tutorial",
    "uco-observable:referrerUrl": url_object,
    "uco-observable:url": url_object,
    "uco-observable:visitCount": 38,
}

url_history_entry_object = uco.observable.ObservableObject()

history_entries.append(history_entry_1)
history_entries.append(history_entry_2)
url_history_facet = uco.observable.FacetUrlHistory(
    browser=browser_object, history_entries=history_entries
)

url_history_entry_object.append_facets(url_history_facet)
bundle.append_to_uco_object(url_history_entry_object)

############################
# Adding an SMS Account    #
############################
phone_account_object = uco.observable.ObservableObject()
phone_account1 = uco.observable.FacetPhoneAccount(phone_number="123456")
phone_account_object.append_facets(phone_account1)
bundle.append_to_uco_object(phone_account_object)

phone_account_object2 = uco.observable.ObservableObject()
phone_account2 = uco.observable.FacetPhoneAccount(phone_number="987654")
phone_account_object2.append_facets(phone_account2)
bundle.append_to_uco_object(phone_account_object2)

############################
# Adding an SMS Message    #
############################
cyber_item4 = uco.observable.ObservableObject()
application_cyber_item = uco.observable.ObservableObject()
sms_application = uco.observable.FacetApplication(app_name="WhatsApp")
application_cyber_item.append_facets(sms_application)
sms_msg = uco.observable.FacetMessage(
    msg_to=[phone_account_object, phone_account_object2],
    msg_from=phone_account_object,
    message_text="Are you free this weekend?",
    sent_time=_next_timestamp(),
    application=application_cyber_item,
)
cyber_item4.append_facets(sms_msg)
bundle.append_to_uco_object(cyber_item4, application_cyber_item)

############################
#  Adding an Identity block#
############################
identity = uco.identity.Identity()
identity_name = uco.identity.FacetSimpleName(given_name="Davey", family_name="Jones")
# (Example birthday: Roughly 30 years ago.)
identity_birth = uco.identity.FacetBirthInformation(
    birthdate=_next_timestamp() - timedelta(days=10950),
)
identity.append_facets(identity_birth, identity_name)
bundle.append_to_uco_object(identity)

############################
#  Adding a location block #
############################
location1 = uco.location.Location()
lat_long = uco.location.FacetLocation(latitude=61.185055, longitude=9.468836)
location1.append_facets(lat_long)
bundle.append_to_uco_object(location1)

##################################
# An investigation to be added to the case
##################################
investigation = case.investigation.CaseInvestigation(
    focus="Transfer of Illicit Materials",
    name="Crime A",
    description="Inquiry into the transfer of illicit materials and "
    "the devices used to do so",
    core_objects=investigation_items,
)
bundle.append_to_uco_object(investigation)

###########################################
# A message thread to be added to the case #
###########################################

# Application Object
app_object = uco.observable.ObservableObject()
app_facet = uco.observable.FacetApplication(app_name="Discord")
app_object.append_facets(app_facet)
bundle.append_to_uco_object(app_object)

# Account 1
id_account_object_1 = uco.observable.ObservableObject()
id_account_facet_1 = uco.observable.FacetAccount(identifier="11111007")
app_account_facet_1 = uco.observable.FacetApplicationAccount(application=app_object)
id_account_object_1.append_facets(id_account_facet_1, app_account_facet_1)
bundle.append_to_uco_object(id_account_object_1)

# Account 2
id_account_object_2 = uco.observable.ObservableObject()
id_account_facet_2 = uco.observable.FacetAccount(identifier="22222007")
app_account_facet_2 = uco.observable.FacetApplicationAccount(application=app_object)
id_account_object_2.append_facets(id_account_facet_2, app_account_facet_2)
bundle.append_to_uco_object(id_account_object_2)


# 1st message
message_object_1 = uco.observable.Message(
    has_changed=True,
)
sent_datetime = datetime.strptime("2024-01-02T16:55:01", "%Y-%m-%dT%H:%M:%S")
facet_message_1 = uco.observable.FacetMessage(
    msg_to=id_account_object_1,
    msg_from=id_account_object_2,
    message_text="Send me the instructions!",
    sent_time=sent_datetime,
)

message_object_1.append_facets(facet_message_1)
bundle.append_to_uco_object(message_object_1)

# 2nd message
message_object_2 = uco.observable.Message(
    has_changed=True,
)

sent_datetime = datetime.strptime("2024-01-02T17:28:42", "%Y-%m-%dT%H:%M:%S")
facet_message_2 = uco.observable.FacetMessage(
    msg_to=id_account_object_2,
    msg_from=id_account_object_1,
    message_text="Sure, in a couple of hours you'lll receive them",
    sent_time=sent_datetime,
)

message_object_2.append_facets(facet_message_2)
bundle.append_to_uco_object(message_object_2)

# Create MessageThread
message_thread_object = uco.observable.MessageThread(name="Jenny D.")
message_thread_facet = uco.observable.FacetMessagethread(
    visibility=True,
    participants=[id_account_object_1, id_account_object_2],
    messages=[message_object_1, message_object_2],
)

message_thread_object.append_facets(message_thread_facet)
bundle.append_to_uco_object(message_thread_object)

##################################
# Adding a Social Media Activity #
##################################
social_activity_object = uco.observable.ObservableObject()

social_media_app = uco.observable.ObservableObject()
social_media_app_facet = uco.observable.FacetApplication(app_name="Facebook")
social_media_app.append_facets(social_media_app_facet)
bundle.append_to_uco_object(social_media_app)

social_media_url = uco.observable.ObservableObject()
social_media_url_facet = uco.observable.FacetUrl(
    url_address="https://www.facebook.com/search/top?q=rome is more"
)
social_media_url.append_facets(social_media_url_facet)
bundle.append_to_uco_object(social_media_url)

post_datetime = datetime.strptime("2024-04-02T17:28:42", "%Y-%m-%dT%H:%M:%S")

social_activity_facet = drafting.entities.FacetSocialMediaActivity(
    body="Good people exist. We need people like Adrian.",
    page_title="Positive thoughts",
    author_identifier="100016939415901",
    author_name="Rome is more",
    activity_type="Post",
    reactions_count=128,
    shares_count=258,
    comments_count=3180,
    account_identifier="100016939417885",
    created_time=post_datetime,
    application=social_media_app,
    url=social_media_url,
)

social_activity_object.append_facets(social_activity_facet)
bundle.append_to_uco_object(social_activity_object)

##################
# Adding a Call  #
##################
identity_organisation_1 = uco.identity.Organization()
simple_name_facet_1 = uco.identity.FacetSimpleName(given_name="Orange")
identity_organisation_1.append_facets(simple_name_facet_1)

bundle.append_to_uco_object(identity_organisation_1)

account_object_1 = uco.observable.ObservableObject()
account_facet_1 = uco.observable.FacetAccount(
    identifier="Jesse iPhone 8", issuer_id=identity_organisation_1
)
phone_account_facet_1 = uco.observable.FacetPhoneAccount(phone_number="+19821764400")
account_object_1.append_facets(account_facet_1, phone_account_facet_1)

bundle.append_to_uco_object(account_object_1)

identity_organisation_2 = uco.identity.Organization()
simple_name_facet_2 = uco.identity.FacetSimpleName(given_name="Telenor")
identity_organisation_2.append_facets(simple_name_facet_2)
bundle.append_to_uco_object(identity_organisation_2)

account_object_2 = uco.observable.ObservableObject()
account_facet_2 = uco.observable.FacetAccount(
    identifier="Walter iPhone 6", issuer_id=identity_organisation_2
)
phone_account_facet_2 = uco.observable.FacetPhoneAccount(phone_number="+19732941683")
account_object_2.append_facets(account_facet_2, phone_account_facet_2)
bundle.append_to_uco_object(account_object_2)

identity_organisation_3 = uco.identity.Organization()
simple_name_facet_3 = uco.identity.FacetSimpleName(given_name="Vodafone")
identity_organisation_3.append_facets(simple_name_facet_3)
bundle.append_to_uco_object(identity_organisation_3)

account_object_3 = uco.observable.ObservableObject()
account_facet_3 = uco.observable.FacetAccount(
    identifier="Magdalena Android 16", issuer_id=identity_organisation_3
)

phone_account_facet_3 = uco.observable.FacetPhoneAccount(phone_number="+393283633741")
account_object_3.append_facets(account_facet_3, phone_account_facet_3)
bundle.append_to_uco_object(account_object_3)

account_object_4 = uco.observable.ObservableObject()
account_facet_4 = uco.observable.FacetAccount(
    identifier="Polly iPhone 12", issuer_id=identity_organisation_3
)
phone_account_facet_4 = uco.observable.FacetPhoneAccount(phone_number="+393389408011")
account_object_4.append_facets(account_facet_4, phone_account_facet_4)
bundle.append_to_uco_object(account_object_4)

app_call_object = uco.observable.ObservableObject()
app_call_facet = uco.observable.FacetApplication(app_name="Native")
app_call_object.append_facets(app_call_facet)
bundle.append_to_uco_object(app_call_object)

call_start_time = datetime.strptime("2024-04-19T21:38:19", "%Y-%m-%dT%H:%M:%S")
call_end_time = datetime.strptime("2024-04-19T21:40:37", "%Y-%m-%dT%H:%M:%S")
call_object = uco.observable.ObservableObject()

call_facet = uco.observable.FacetCall(
    application=app_call_object,
    call_type="incoming",
    call_duration=138,
    start_time=call_start_time,
    end_time=call_end_time,
    call_from=account_object_1,
    call_to=account_object_2,
    call_participant=[account_object_3, account_object_4],
)
call_object.append_facets(call_facet)
bundle.append_to_uco_object(call_object)

###############################
# Adding a Provenance Record  #
###############################
provenance_rec_object = case.investigation.ProvenanceRecord(
    exhibit_number="CASE_X_camera_nikon_D750_and_sd_001",
    uco_core_objects=[device_camera, sd_card],
)
bundle.append_to_uco_object(provenance_rec_object)


###############################
# Recording an extracted file #
###############################

# TODO - Record provenance of extracted file.

# Record extracted file.
extracted_file_file_facet1 = uco.observable.FacetFile(
    file_extension="jpg",
    file_name="IMG_0123.jpg",
    file_path="file/Image/IMG_0123.jpg",
    file_is_directory=False,
)
extracted_file_1 = uco.observable.File(facets=[extracted_file_file_facet1])
bundle.append_to_uco_object(extracted_file_1)

extraction_root_directory_file_facet1 = uco.observable.FacetFile(file_is_directory=True)
extraction_root_directory1 = uco.observable.File(
    description="Root directory of file extractions for this case.",
    facets=[extraction_root_directory_file_facet1],
)
bundle.append_to_uco_object(extraction_root_directory1)

path_relation_facet1 = uco.observable.FacetPathRelation(path="files/Image/")
path_relation = uco.observable.ObservableRelationship(
    directional=True,
    kind_of_relationship="Contained_Within",
    source=extracted_file_1,
    target=extraction_root_directory1,
    facets=[path_relation_facet1],
)
bundle.append_to_uco_object(path_relation)

##########################################################
# A complete Investigative Action (Forensic Acquisition) #
##########################################################

# Device + Mobile phone
device_object = uco.observable.ObservableObject()
device_phone_facet = uco.observable.FacetDevice(
    device_type="Mobile phone",
    model="iPhone XR",
    manufacturer=manufacturer_apple,
    serial="DX4CDFDBOJE",
)
activation_time = datetime.strptime("2024-02-26T10:18:39", "%Y-%m-%dT%H:%M:%S")
device_mobile_facet = uco.observable.FacetMobileDevice(
    IMEI="359405082912450",
    bluetooth_device_name="Beats solo",
    keypad_unlock_code="124589",
    storage_capacity_in_bytes=64000,
    phone_activation_time=activation_time,
)
sim_card_facet = uco.observable.FacetSimCard(
    ICCID="8901260243790437158",
    IMSI="310260249043715",
    PIN="041981",
    PUK="12345678",
    SIM_form="Micro SIM",
    SIM_type="SIM",
    carrier=identity_organisation_3,
    storage_capacity_in_bytes=65536,
)

device_object.append_facets(device_phone_facet, device_mobile_facet, sim_card_facet)
bundle.append_to_uco_object(device_object)

file_extracted = uco.observable.ObservableObject()
file_zip_facet = uco.observable.FacetFile(
    file_allocation_status="Contiguous Allocation",
    file_extension="zip",
    file_name="Apple_iPhone XR (A1901).zip",
    file_path="Apple_iPhone XR (A1901).zip",
    file_is_directory=False,
    file_size_bytes=16965760332,
    file_mime_type="application/zip",
)

file_hash_facet = uco.observable.FacetContentData(
    hash_method="SHA256",
    hash_value="11122273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b",
)
file_extracted.append_facets(file_zip_facet, file_hash_facet)
bundle.append_to_uco_object(file_extracted)

provenance_mobile_device = case.investigation.ProvenanceRecord(
    exhibit_number="CASE_X iPhoneXR s/n DX4CDFDBOJE",
    uco_core_objects=device_object,
)
bundle.append_to_uco_object(provenance_mobile_device)

provenance_zip_file = case.investigation.ProvenanceRecord(
    exhibit_number="CASE_X iPhoneXR s/n DX4CDFDBOJE extracted ZIP file",
    uco_core_objects=file_extracted,
)
bundle.append_to_uco_object(provenance_zip_file)

performer_object = uco.identity.Organization(name="Reality Net Srl")
bundle.append_to_uco_object(performer_object)

# role_object = uco.role.Role(
#     name="Digital Forensic Expert"
#     )
# bundle.append_to_uco_object(role_object)

# relation_object = uco.observable.ObservableRelationship(
#     source=performer_object,
#     target=role_object,
#     kind_of_relationship="Has_Role",
#     directional=True,
# )
# bundle.append_to_uco_object(relation_object)

tool_creator_object = uco.identity.Organization(name="Cellebrite")
bundle.append_to_uco_object(tool_creator_object)

tool_acquisition = uco.tool.Tool(
    tool_name="UFED PA",
    tool_version="7.57.1.9",
    tool_type="Acquisition",
    tool_creator=tool_creator_object,
)
bundle.append_to_uco_object(tool_acquisition)

action_start_time = datetime.strptime("2024-02-29T12:28:49", "%Y-%m-%dT%H:%M:%S")
action_end_time = datetime.strptime("2024-02-29T12:43:44", "%Y-%m-%dT%H:%M:%S")
action_location_object = uco.location.Location()
action_location_facet = uco.location.FacetSimpleAdress(
    country="Italy",
    locality="Genoa",
    street="via dei Ciclamini, 7",
    postal_code="44100",
)
action_location_object.append_facets(action_location_facet)
bundle.append_to_uco_object(action_location_object)

action_acquisition = case.investigation.InvestigativeAction(
    name="Forensic mobile device acquisition",
    description="Acquisition iPhone XR",
    start_time=action_start_time,
    end_time=action_end_time,
    performer=performer_object,
    location=action_location_object,
    instrument=tool_acquisition,
    objects=provenance_mobile_device,
    results=provenance_zip_file,
)
bundle.append_to_uco_object(action_acquisition)

##################
# Print the case #
##################

print(bundle)
