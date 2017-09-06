# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/list_avatar_customizations_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.avatar import avatar_customization_pb2 as pogoprotos_dot_data_dot_avatar_dot_avatar__customization__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/list_avatar_customizations_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nIpogoprotos/networking/responses/list_avatar_customizations_response.proto\x12\x1fpogoprotos.networking.responses\x1a\x31pogoprotos/data/avatar/avatar_customization.proto\"\xf7\x01\n ListAvatarCustomizationsResponse\x12X\n\x06result\x18\x01 \x01(\x0e\x32H.pogoprotos.networking.responses.ListAvatarCustomizationsResponse.Result\x12J\n\x15\x61vatar_customizations\x18\x02 \x01(\x0b\x32+.pogoprotos.data.avatar.AvatarCustomization\"-\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_avatar_dot_avatar__customization__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_LISTAVATARCUSTOMIZATIONSRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.ListAvatarCustomizationsResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=364,
  serialized_end=409,
)
_sym_db.RegisterEnumDescriptor(_LISTAVATARCUSTOMIZATIONSRESPONSE_RESULT)


_LISTAVATARCUSTOMIZATIONSRESPONSE = _descriptor.Descriptor(
  name='ListAvatarCustomizationsResponse',
  full_name='pogoprotos.networking.responses.ListAvatarCustomizationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.ListAvatarCustomizationsResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_customizations', full_name='pogoprotos.networking.responses.ListAvatarCustomizationsResponse.avatar_customizations', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LISTAVATARCUSTOMIZATIONSRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=409,
)

_LISTAVATARCUSTOMIZATIONSRESPONSE.fields_by_name['result'].enum_type = _LISTAVATARCUSTOMIZATIONSRESPONSE_RESULT
_LISTAVATARCUSTOMIZATIONSRESPONSE.fields_by_name['avatar_customizations'].message_type = pogoprotos_dot_data_dot_avatar_dot_avatar__customization__pb2._AVATARCUSTOMIZATION
_LISTAVATARCUSTOMIZATIONSRESPONSE_RESULT.containing_type = _LISTAVATARCUSTOMIZATIONSRESPONSE
DESCRIPTOR.message_types_by_name['ListAvatarCustomizationsResponse'] = _LISTAVATARCUSTOMIZATIONSRESPONSE

ListAvatarCustomizationsResponse = _reflection.GeneratedProtocolMessageType('ListAvatarCustomizationsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTAVATARCUSTOMIZATIONSRESPONSE,
  __module__ = 'pogoprotos.networking.responses.list_avatar_customizations_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.ListAvatarCustomizationsResponse)
  ))
_sym_db.RegisterMessage(ListAvatarCustomizationsResponse)


# @@protoc_insertion_point(module_scope)
