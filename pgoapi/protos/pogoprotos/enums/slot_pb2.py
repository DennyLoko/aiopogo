# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/slot.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (
    lambda x: x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='pogoprotos/enums/slot.proto',
    package='pogoprotos.enums',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x1bpogoprotos/enums/slot.proto\x12\x10pogoprotos.enums*\x9e\x01\n\x04Slot\x12\x0e\n\nUNSET_SLOT\x10\x00\x12\x08\n\x04HAIR\x10\x01\x12\t\n\x05SHIRT\x10\x02\x12\t\n\x05PANTS\x10\x03\x12\x07\n\x03HAT\x10\x04\x12\t\n\x05SHOES\x10\x05\x12\x08\n\x04\x45YES\x10\x06\x12\x0c\n\x08\x42\x41\x43KPACK\x10\x07\x12\n\n\x06GLOVES\x10\x08\x12\t\n\x05SOCKS\x10\t\x12\x08\n\x04\x42\x45LT\x10\n\x12\x0b\n\x07GLASSES\x10\x0b\x12\x0c\n\x08NECKLACE\x10\x0c\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_SLOT = _descriptor.EnumDescriptor(
    name='Slot',
    full_name='pogoprotos.enums.Slot',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='UNSET_SLOT', index=0, number=0, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='HAIR', index=1, number=1, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='SHIRT', index=2, number=2, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='PANTS', index=3, number=3, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='HAT', index=4, number=4, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='SHOES', index=5, number=5, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='EYES', index=6, number=6, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='BACKPACK', index=7, number=7, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='GLOVES', index=8, number=8, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='SOCKS', index=9, number=9, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='BELT', index=10, number=10, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='GLASSES', index=11, number=11, options=None, type=None),
        _descriptor.EnumValueDescriptor(
            name='NECKLACE', index=12, number=12, options=None, type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=50,
    serialized_end=208, )
_sym_db.RegisterEnumDescriptor(_SLOT)

Slot = enum_type_wrapper.EnumTypeWrapper(_SLOT)
UNSET_SLOT = 0
HAIR = 1
SHIRT = 2
PANTS = 3
HAT = 4
SHOES = 5
EYES = 6
BACKPACK = 7
GLOVES = 8
SOCKS = 9
BELT = 10
GLASSES = 11
NECKLACE = 12

DESCRIPTOR.enum_types_by_name['Slot'] = _SLOT

# @@protoc_insertion_point(module_scope)
