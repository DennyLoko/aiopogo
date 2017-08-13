# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/check_awarded_badges_response.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (
    lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from pogoprotos.enums import badge_type_pb2 as pogoprotos_dot_enums_dot_badge__type__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='pogoprotos/networking/responses/check_awarded_badges_response.proto',
    package='pogoprotos.networking.responses',
    syntax='proto3',
    serialized_pb=_b(
        '\nCpogoprotos/networking/responses/check_awarded_badges_response.proto\x12\x1fpogoprotos.networking.responses\x1a!pogoprotos/enums/badge_type.proto\"\x9d\x01\n\x1a\x43heckAwardedBadgesResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x33\n\x0e\x61warded_badges\x18\x02 \x03(\x0e\x32\x1b.pogoprotos.enums.BadgeType\x12\x1c\n\x14\x61warded_badge_levels\x18\x03 \x03(\x05\x12\x1b\n\x13\x61vatar_template_ids\x18\x04 \x03(\tb\x06proto3'
    ),
    dependencies=[
        pogoprotos_dot_enums_dot_badge__type__pb2.DESCRIPTOR,
    ])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CHECKAWARDEDBADGESRESPONSE = _descriptor.Descriptor(
    name='CheckAwardedBadgesResponse',
    full_name='pogoprotos.networking.responses.CheckAwardedBadgesResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='success',
            full_name=
            'pogoprotos.networking.responses.CheckAwardedBadgesResponse.success',
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='awarded_badges',
            full_name=
            'pogoprotos.networking.responses.CheckAwardedBadgesResponse.awarded_badges',
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='awarded_badge_levels',
            full_name=
            'pogoprotos.networking.responses.CheckAwardedBadgesResponse.awarded_badge_levels',
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='avatar_template_ids',
            full_name=
            'pogoprotos.networking.responses.CheckAwardedBadgesResponse.avatar_template_ids',
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=140,
    serialized_end=297, )

_CHECKAWARDEDBADGESRESPONSE.fields_by_name[
    'awarded_badges'].enum_type = pogoprotos_dot_enums_dot_badge__type__pb2._BADGETYPE
DESCRIPTOR.message_types_by_name[
    'CheckAwardedBadgesResponse'] = _CHECKAWARDEDBADGESRESPONSE

CheckAwardedBadgesResponse = _reflection.GeneratedProtocolMessageType(
    'CheckAwardedBadgesResponse',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_CHECKAWARDEDBADGESRESPONSE,
        __module__=
        'pogoprotos.networking.responses.check_awarded_badges_response_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.CheckAwardedBadgesResponse)
    ))
_sym_db.RegisterMessage(CheckAwardedBadgesResponse)

# @@protoc_insertion_point(module_scope)
