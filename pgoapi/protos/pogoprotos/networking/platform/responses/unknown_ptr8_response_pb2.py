# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/platform/responses/unknown_ptr8_response.proto

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
    name='pogoprotos/networking/platform/responses/unknown_ptr8_response.proto',
    package='pogoprotos.networking.platform.responses',
    syntax='proto3',
    serialized_pb=_b(
        '\nDpogoprotos/networking/platform/responses/unknown_ptr8_response.proto\x12(pogoprotos.networking.platform.responses\"&\n\x13UnknownPtr8Response\x12\x0f\n\x07message\x18\x02 \x01(\tb\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_UNKNOWNPTR8RESPONSE = _descriptor.Descriptor(
    name='UnknownPtr8Response',
    full_name='pogoprotos.networking.platform.responses.UnknownPtr8Response',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='message',
            full_name=
            'pogoprotos.networking.platform.responses.UnknownPtr8Response.message',
            index=0,
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
    serialized_start=114,
    serialized_end=152, )

DESCRIPTOR.message_types_by_name['UnknownPtr8Response'] = _UNKNOWNPTR8RESPONSE

UnknownPtr8Response = _reflection.GeneratedProtocolMessageType(
    'UnknownPtr8Response',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_UNKNOWNPTR8RESPONSE,
        __module__=
        'pogoprotos.networking.platform.responses.unknown_ptr8_response_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.networking.platform.responses.UnknownPtr8Response)
    ))
_sym_db.RegisterMessage(UnknownPtr8Response)

# @@protoc_insertion_point(module_scope)
