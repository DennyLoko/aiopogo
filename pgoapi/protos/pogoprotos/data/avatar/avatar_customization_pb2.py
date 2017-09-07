# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/avatar/avatar_customization.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/avatar/avatar_customization.proto',
  package='pogoprotos.data.avatar',
  syntax='proto3',
  serialized_pb=_b('\n1pogoprotos/data/avatar/avatar_customization.proto\x12\x16pogoprotos.data.avatar\"\x8d\x02\n\x13\x41vatarCustomization\x12\x1a\n\x12\x61vatar_template_id\x18\x01 \x01(\t\x12\x41\n\x06labels\x18\x02 \x03(\x0e\x32\x31.pogoprotos.data.avatar.AvatarCustomization.Label\"\x96\x01\n\x05Label\x12\x0f\n\x0bUNSET_LABEL\x10\x00\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x01\x12\t\n\x05OWNED\x10\x02\x12\x0c\n\x08\x46\x45\x41TURED\x10\x03\x12\x07\n\x03NEW\x10\x04\x12\x08\n\x04SALE\x10\x05\x12\x0f\n\x0bPURCHASABLE\x10\x06\x12\x0e\n\nUNLOCKABLE\x10\x07\x12\n\n\x06VIEWED\x10\x08\x12\x16\n\x12LOCKED_PURCHASABLE\x10\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_AVATARCUSTOMIZATION_LABEL = _descriptor.EnumDescriptor(
  name='Label',
  full_name='pogoprotos.data.avatar.AvatarCustomization.Label',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_LABEL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OWNED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEATURED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SALE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PURCHASABLE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNLOCKABLE', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIEWED', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCKED_PURCHASABLE', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=197,
  serialized_end=347,
)
_sym_db.RegisterEnumDescriptor(_AVATARCUSTOMIZATION_LABEL)


_AVATARCUSTOMIZATION = _descriptor.Descriptor(
  name='AvatarCustomization',
  full_name='pogoprotos.data.avatar.AvatarCustomization',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='avatar_template_id', full_name='pogoprotos.data.avatar.AvatarCustomization.avatar_template_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='labels', full_name='pogoprotos.data.avatar.AvatarCustomization.labels', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AVATARCUSTOMIZATION_LABEL,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=347,
)

_AVATARCUSTOMIZATION.fields_by_name['labels'].enum_type = _AVATARCUSTOMIZATION_LABEL
_AVATARCUSTOMIZATION_LABEL.containing_type = _AVATARCUSTOMIZATION
DESCRIPTOR.message_types_by_name['AvatarCustomization'] = _AVATARCUSTOMIZATION

AvatarCustomization = _reflection.GeneratedProtocolMessageType('AvatarCustomization', (_message.Message,), dict(
  DESCRIPTOR = _AVATARCUSTOMIZATION,
  __module__ = 'pogoprotos.data.avatar.avatar_customization_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.avatar.AvatarCustomization)
  ))
_sym_db.RegisterMessage(AvatarCustomization)


# @@protoc_insertion_point(module_scope)
