from datetime import datetime, timezone

import cdo_local_uuid

from case_mapping import case, uco

# This is part of enabling non-random UUIDs for the demonstration
# output.  The other part is handled at call time, and can be seen in
# the documentation for cdo_local_uuid._demo_uuid().
cdo_local_uuid.configure()

# Generate a case bundle and list to hold investigation items
bundle = uco.core.Bundle(description="An Example Case File")
investigation_items = []

###################################
# An item to be added to the case #
###################################
cyber_item1 = uco.observable.ObservableObject()
manufacturer_nikon = uco.identity.Organization(name="Nikon")
bundle.append_to_uco_object(manufacturer_nikon)
device1 = uco.observable.FacetDevice(manufacturer=manufacturer_nikon, model="D750")
cyber_item1.append_facets(device1)
bundle.append_to_uco_object(cyber_item1)

##################################
# A file to be added to the case #
##################################
cyber_item2 = uco.observable.ObservableObject()
investigation_items.append(cyber_item2)
file1 = uco.observable.FacetFile(
    file_system_type="EXT4",
    file_name="IMG_0123.jpg",
    file_path="/sdcard/ImG_0123.jpg",
    file_extension="jpg",
    size_bytes=35002,
)
file_content1 = uco.observable.FacetContentData(
    byte_order="Big-endian",
    magic_number="/9j/ww==",
    mime_type="image/jpg",
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
cyber_item2.append_facets(file1, file_content1, file_raster1, file_exif1)
bundle.append_to_uco_object(cyber_item2)

#######################################
# An investigative action on a device #
#######################################
inv_act = case.investigation.InvestigativeAction(
    name="annotated",
    end_time=datetime.now(timezone.utc),
    start_time=datetime.now(timezone.utc),
)
investigation_items.append(inv_act)  # NOTE: Appending whole object not just id
manufacturer_apple = uco.identity.Organization(name="Apple")
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
    end_time=datetime.now(timezone.utc),
    start_time=datetime.now(timezone.utc),
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
    source=cyber_item1,
    target=cyber_item2,
    kind_of_relationship="Contained_Within",
    directional=True,
)
path_rel1 = uco.observable.FacetPathRelation(path="/sdcard/IMG_0123.jpg")
cyber_rel1.append_facets(path_rel1)
bundle.append_to_uco_object(cyber_rel1)

##############################
#  Adding an Email Account   #  # NOTE: Changes here compared to previous version
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
    received_time=datetime.now(timezone.utc),
    sent_time=datetime.now(timezone.utc),
    message_id="<1234567890@example.com>",
)
cyber_item3.append_facets(email_msg)
bundle.append_to_uco_object(cyber_item3)


############################
#  Adding an SMS Account   #
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
#  Adding an SMS Message   #
############################
cyber_item4 = uco.observable.ObservableObject()
application_cyber_item = uco.observable.ObservableObject()
sms_application = uco.observable.FacetApplication(app_name="WhatsApp")
application_cyber_item.append_facets(sms_application)
sms_msg = uco.observable.FacetMessage(
    msg_to=[phone_account_object, phone_account_object2],
    msg_from=phone_account_object,
    message_text="Are you free this weekend?",
    sent_time=datetime.now(timezone.utc),
    application=application_cyber_item,
)
cyber_item4.append_facets(sms_msg)
bundle.append_to_uco_object(cyber_item4, application_cyber_item)

############################
#  Adding an Identity block#
############################
identity = uco.identity.Identity()
identity_name = uco.identity.FacetSimpleName(given_name="Davey", family_name="Jones")
identity_birth = uco.identity.FacetBirthInformation(
    birthdate=datetime.now(timezone.utc)
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

message_thread_object = uco.observable.MessageThread()

# 1st message
message_1 = uco.observable.Message(
    has_changed=True,
    state="some state",
)
facet_message_1 = uco.observable.FacetMessage()
message_1.append_facets(facet_message_1)
# 2nd message
message_2 = uco.observable.Message()
facet_message_2 = uco.observable.FacetMessage()
message_2.append_facets(facet_message_2)
# 3rd message
message_3 = uco.observable.Message()
facet_message_3 = uco.observable.FacetMessage()
message_3.append_facets(facet_message_3)

# 1st message is followed by 2nd and 3rd message.
# Create MessageThread
message_thread_facet = uco.observable.FacetMessagethread(
    display_name="some name",
    messages={
        message_1["@id"]: {
            message_2["@id"],
            message_3["@id"],
        }
    },
)

message_thread_object.append_facets(message_thread_facet)

# TODO Restore from list-style demo.
# Append more messages to MessageThread
# message_thread_facet.append_messages(messages=message_3)

# Add all objects to bundle
objs = (
    message_1,
    message_2,
    message_3,
    message_thread_object,
)
bundle.append_to_uco_object(objs)

##################
# Print the case #
##################

print(bundle)
