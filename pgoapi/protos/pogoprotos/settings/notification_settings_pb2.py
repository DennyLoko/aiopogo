# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/notification_settings.proto

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

DESCRIPTOR = _descriptor.FileDescriptor(
    name='pogoprotos/settings/notification_settings.proto',
    package='pogoprotos.settings',
    syntax='proto3',
    serialized_pb=_b(
        '\n/pogoprotos/settings/notification_settings.proto\x12\x13pogoprotos.settings\"N\n\x14NotificationSettings\x12\x1a\n\x12pull_notifications\x18\x01 \x01(\x08\x12\x1a\n\x12show_notifications\x18\x02 \x01(\x08\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_NOTIFICATIONSETTINGS = _descriptor.Descriptor(
    name='NotificationSettings',
    full_name='pogoprotos.settings.NotificationSettings',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='pull_notifications',
            full_name=
            'pogoprotos.settings.NotificationSettings.pull_notifications',
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
            name='show_notifications',
            full_name=
            'pogoprotos.settings.NotificationSettings.show_notifications',
            index=1,
            number=2,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=72,
    serialized_end=150, )

DESCRIPTOR.message_types_by_name[
    'NotificationSettings'] = _NOTIFICATIONSETTINGS

NotificationSettings = _reflection.GeneratedProtocolMessageType(
    'NotificationSettings',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_NOTIFICATIONSETTINGS,
        __module__='pogoprotos.settings.notification_settings_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.settings.NotificationSettings)
    ))
_sym_db.RegisterMessage(NotificationSettings)

# @@protoc_insertion_point(module_scope)
