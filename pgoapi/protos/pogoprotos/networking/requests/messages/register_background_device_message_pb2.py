# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/register_background_device_message.proto

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
    name=
    'pogoprotos/networking/requests/messages/register_background_device_message.proto',
    package='pogoprotos.networking.requests.messages',
    syntax='proto3',
    serialized_pb=_b(
        '\nPpogoprotos/networking/requests/messages/register_background_device_message.proto\x12\'pogoprotos.networking.requests.messages\"I\n\x1fRegisterBackgroundDeviceMessage\x12\x13\n\x0b\x64\x65vice_type\x18\x01 \x01(\t\x12\x11\n\tdevice_id\x18\x02 \x01(\tb\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_REGISTERBACKGROUNDDEVICEMESSAGE = _descriptor.Descriptor(
    name='RegisterBackgroundDeviceMessage',
    full_name=
    'pogoprotos.networking.requests.messages.RegisterBackgroundDeviceMessage',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='device_type',
            full_name=
            'pogoprotos.networking.requests.messages.RegisterBackgroundDeviceMessage.device_type',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='device_id',
            full_name=
            'pogoprotos.networking.requests.messages.RegisterBackgroundDeviceMessage.device_id',
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
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
    serialized_start=125,
    serialized_end=198, )

DESCRIPTOR.message_types_by_name[
    'RegisterBackgroundDeviceMessage'] = _REGISTERBACKGROUNDDEVICEMESSAGE

RegisterBackgroundDeviceMessage = _reflection.GeneratedProtocolMessageType(
    'RegisterBackgroundDeviceMessage',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_REGISTERBACKGROUNDDEVICEMESSAGE,
        __module__=
        'pogoprotos.networking.requests.messages.register_background_device_message_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.RegisterBackgroundDeviceMessage)
    ))
_sym_db.RegisterMessage(RegisterBackgroundDeviceMessage)

# @@protoc_insertion_point(module_scope)
