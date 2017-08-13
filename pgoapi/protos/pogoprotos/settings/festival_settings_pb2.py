# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/festival_settings.proto

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
    name='pogoprotos/settings/festival_settings.proto',
    package='pogoprotos.settings',
    syntax='proto3',
    serialized_pb=_b(
        '\n+pogoprotos/settings/festival_settings.proto\x12\x13pogoprotos.settings\"\xb0\x01\n\x10\x46\x65stivalSettings\x12I\n\rfestival_type\x18\x01 \x01(\x0e\x32\x32.pogoprotos.settings.FestivalSettings.FestivalType\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0e\n\x06vector\x18\x03 \x01(\t\"4\n\x0c\x46\x65stivalType\x12\x08\n\x04NONE\x10\x00\x12\r\n\tHALLOWEEN\x10\x01\x12\x0b\n\x07HOLIDAY\x10\x02\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_FESTIVALSETTINGS_FESTIVALTYPE = _descriptor.EnumDescriptor(
    name='FestivalType',
    full_name='pogoprotos.settings.FestivalSettings.FestivalType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='NONE', index=0, number=0, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='HALLOWEEN', index=1, number=1, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='HOLIDAY', index=2, number=2, options=None, type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=193,
    serialized_end=245, )
_sym_db.RegisterEnumDescriptor(_FESTIVALSETTINGS_FESTIVALTYPE)

_FESTIVALSETTINGS = _descriptor.Descriptor(
    name='FestivalSettings',
    full_name='pogoprotos.settings.FestivalSettings',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='festival_type',
            full_name='pogoprotos.settings.FestivalSettings.festival_type',
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='key',
            full_name='pogoprotos.settings.FestivalSettings.key',
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
        _descriptor.FieldDescriptor(
            name='vector',
            full_name='pogoprotos.settings.FestivalSettings.vector',
            index=2,
            number=3,
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
    enum_types=[
        _FESTIVALSETTINGS_FESTIVALTYPE,
    ],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=69,
    serialized_end=245, )

_FESTIVALSETTINGS.fields_by_name[
    'festival_type'].enum_type = _FESTIVALSETTINGS_FESTIVALTYPE
_FESTIVALSETTINGS_FESTIVALTYPE.containing_type = _FESTIVALSETTINGS
DESCRIPTOR.message_types_by_name['FestivalSettings'] = _FESTIVALSETTINGS

FestivalSettings = _reflection.GeneratedProtocolMessageType(
    'FestivalSettings',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_FESTIVALSETTINGS,
        __module__='pogoprotos.settings.festival_settings_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.settings.FestivalSettings)
    ))
_sym_db.RegisterMessage(FestivalSettings)

# @@protoc_insertion_point(module_scope)
