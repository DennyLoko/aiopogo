# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/exclusive_ticket_info.proto

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
  name='pogoprotos/inventory/exclusive_ticket_info.proto',
  package='pogoprotos.inventory',
  syntax='proto3',
  serialized_pb=_b('\n0pogoprotos/inventory/exclusive_ticket_info.proto\x12\x14pogoprotos.inventory\"z\n\x13\x45xclusiveTicketInfo\x12\x11\n\traid_seed\x18\x01 \x01(\x03\x12\x0f\n\x07\x66ort_id\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x15\n\rstart_time_ms\x18\x04 \x01(\x03\x12\x13\n\x0b\x65nd_time_ms\x18\x05 \x01(\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EXCLUSIVETICKETINFO = _descriptor.Descriptor(
  name='ExclusiveTicketInfo',
  full_name='pogoprotos.inventory.ExclusiveTicketInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raid_seed', full_name='pogoprotos.inventory.ExclusiveTicketInfo.raid_seed', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='pogoprotos.inventory.ExclusiveTicketInfo.fort_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='pogoprotos.inventory.ExclusiveTicketInfo.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time_ms', full_name='pogoprotos.inventory.ExclusiveTicketInfo.start_time_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time_ms', full_name='pogoprotos.inventory.ExclusiveTicketInfo.end_time_ms', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=196,
)

DESCRIPTOR.message_types_by_name['ExclusiveTicketInfo'] = _EXCLUSIVETICKETINFO

ExclusiveTicketInfo = _reflection.GeneratedProtocolMessageType('ExclusiveTicketInfo', (_message.Message,), dict(
  DESCRIPTOR = _EXCLUSIVETICKETINFO,
  __module__ = 'pogoprotos.inventory.exclusive_ticket_info_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.inventory.ExclusiveTicketInfo)
  ))
_sym_db.RegisterMessage(ExclusiveTicketInfo)


# @@protoc_insertion_point(module_scope)
