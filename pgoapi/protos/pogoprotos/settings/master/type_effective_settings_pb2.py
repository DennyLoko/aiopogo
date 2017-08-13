# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/type_effective_settings.proto

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

from pogoprotos.enums import pokemon_type_pb2 as pogoprotos_dot_enums_dot_pokemon__type__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='pogoprotos/settings/master/type_effective_settings.proto',
    package='pogoprotos.settings.master',
    syntax='proto3',
    serialized_pb=_b(
        '\n8pogoprotos/settings/master/type_effective_settings.proto\x12\x1apogoprotos.settings.master\x1a#pogoprotos/enums/pokemon_type.proto\"b\n\x15TypeEffectiveSettings\x12\x15\n\rattack_scalar\x18\x01 \x03(\x02\x12\x32\n\x0b\x61ttack_type\x18\x02 \x01(\x0e\x32\x1d.pogoprotos.enums.PokemonTypeb\x06proto3'
    ),
    dependencies=[
        pogoprotos_dot_enums_dot_pokemon__type__pb2.DESCRIPTOR,
    ])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_TYPEEFFECTIVESETTINGS = _descriptor.Descriptor(
    name='TypeEffectiveSettings',
    full_name='pogoprotos.settings.master.TypeEffectiveSettings',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='attack_scalar',
            full_name=
            'pogoprotos.settings.master.TypeEffectiveSettings.attack_scalar',
            index=0,
            number=1,
            type=2,
            cpp_type=6,
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
            name='attack_type',
            full_name=
            'pogoprotos.settings.master.TypeEffectiveSettings.attack_type',
            index=1,
            number=2,
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
    serialized_end=223, )

_TYPEEFFECTIVESETTINGS.fields_by_name[
    'attack_type'].enum_type = pogoprotos_dot_enums_dot_pokemon__type__pb2._POKEMONTYPE
DESCRIPTOR.message_types_by_name[
    'TypeEffectiveSettings'] = _TYPEEFFECTIVESETTINGS

TypeEffectiveSettings = _reflection.GeneratedProtocolMessageType(
    'TypeEffectiveSettings',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_TYPEEFFECTIVESETTINGS,
        __module__='pogoprotos.settings.master.type_effective_settings_pb2'
        # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.TypeEffectiveSettings)
    ))
_sym_db.RegisterMessage(TypeEffectiveSettings)

# @@protoc_insertion_point(module_scope)
