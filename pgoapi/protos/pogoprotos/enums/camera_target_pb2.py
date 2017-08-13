# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/camera_target.proto

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
    name='pogoprotos/enums/camera_target.proto',
    package='pogoprotos.enums',
    syntax='proto3',
    serialized_pb=_b(
        '\n$pogoprotos/enums/camera_target.proto\x12\x10pogoprotos.enums*\xfc\x03\n\x0c\x43\x61meraTarget\x12\x17\n\x13\x43\x41M_TARGET_ATTACKER\x10\x00\x12\x1c\n\x18\x43\x41M_TARGET_ATTACKER_EDGE\x10\x01\x12\x1e\n\x1a\x43\x41M_TARGET_ATTACKER_GROUND\x10\x02\x12\x17\n\x13\x43\x41M_TARGET_DEFENDER\x10\x03\x12\x1c\n\x18\x43\x41M_TARGET_DEFENDER_EDGE\x10\x04\x12\x1e\n\x1a\x43\x41M_TARGET_DEFENDER_GROUND\x10\x05\x12 \n\x1c\x43\x41M_TARGET_ATTACKER_DEFENDER\x10\x06\x12%\n!CAM_TARGET_ATTACKER_DEFENDER_EDGE\x10\x07\x12 \n\x1c\x43\x41M_TARGET_DEFENDER_ATTACKER\x10\x08\x12%\n!CAM_TARGET_DEFENDER_ATTACKER_EDGE\x10\t\x12\'\n#CAM_TARGET_ATTACKER_DEFENDER_MIRROR\x10\x0b\x12)\n%CAM_TARGET_SHOULDER_ATTACKER_DEFENDER\x10\x0c\x12\x30\n,CAM_TARGET_SHOULDER_ATTACKER_DEFENDER_MIRROR\x10\r\x12&\n\"CAM_TARGET_ATTACKER_DEFENDER_WORLD\x10\x0e\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CAMERATARGET = _descriptor.EnumDescriptor(
    name='CameraTarget',
    full_name='pogoprotos.enums.CameraTarget',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='CAM_TARGET_ATTACKER',
            index=0,
            number=0,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CAM_TARGET_ATTACKER_EDGE',
            index=1,
            number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CAM_TARGET_ATTACKER_GROUND',
            index=2,
            number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CAM_TARGET_DEFENDER',
            index=3,
            number=3,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CAM_TARGET_DEFENDER_EDGE',
            index=4,
            number=4,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CAM_TARGET_DEFENDER_GROUND',
            index=5,
            number=5,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CAM_TARGET_ATTACKER_DEFENDER',
            index=6,
            number=6,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CAM_TARGET_ATTACKER_DEFENDER_EDGE',
            index=7,
            number=7,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CAM_TARGET_DEFENDER_ATTACKER',
            index=8,
            number=8,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CAM_TARGET_DEFENDER_ATTACKER_EDGE',
            index=9,
            number=9,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CAM_TARGET_ATTACKER_DEFENDER_MIRROR',
            index=10,
            number=11,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CAM_TARGET_SHOULDER_ATTACKER_DEFENDER',
            index=11,
            number=12,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CAM_TARGET_SHOULDER_ATTACKER_DEFENDER_MIRROR',
            index=12,
            number=13,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CAM_TARGET_ATTACKER_DEFENDER_WORLD',
            index=13,
            number=14,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=59,
    serialized_end=567, )
_sym_db.RegisterEnumDescriptor(_CAMERATARGET)

CameraTarget = enum_type_wrapper.EnumTypeWrapper(_CAMERATARGET)
CAM_TARGET_ATTACKER = 0
CAM_TARGET_ATTACKER_EDGE = 1
CAM_TARGET_ATTACKER_GROUND = 2
CAM_TARGET_DEFENDER = 3
CAM_TARGET_DEFENDER_EDGE = 4
CAM_TARGET_DEFENDER_GROUND = 5
CAM_TARGET_ATTACKER_DEFENDER = 6
CAM_TARGET_ATTACKER_DEFENDER_EDGE = 7
CAM_TARGET_DEFENDER_ATTACKER = 8
CAM_TARGET_DEFENDER_ATTACKER_EDGE = 9
CAM_TARGET_ATTACKER_DEFENDER_MIRROR = 11
CAM_TARGET_SHOULDER_ATTACKER_DEFENDER = 12
CAM_TARGET_SHOULDER_ATTACKER_DEFENDER_MIRROR = 13
CAM_TARGET_ATTACKER_DEFENDER_WORLD = 14

DESCRIPTOR.enum_types_by_name['CameraTarget'] = _CAMERATARGET

# @@protoc_insertion_point(module_scope)
