# -*- coding: utf-8 -*-
# Copyright 2020 Ververica GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: entities.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='entities.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n)com.ververica.statefun.workshop.generatedP\001'),
  serialized_pb=_b('\n\x0e\x65ntities.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x1f\n\x0c\x43onfirmFraud\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\"o\n\x0bTransaction\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08merchant\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x05\"L\n\rFeatureVector\x12\x13\n\x0b\x66raud_count\x18\x01 \x01(\x05\x12\x16\n\x0emerchant_score\x18\x02 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x05\"\x1b\n\nFraudScore\x12\r\n\x05score\x18\x01 \x01(\x05\"\x1e\n\rReportedFraud\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"\r\n\x0b\x45xpireFraud\"\x0c\n\nQueryFraud\"-\n\rMerchantScore\x12\r\n\x05score\x18\x01 \x01(\x05\x12\r\n\x05\x65rror\x18\x02 \x01(\x08\"\x14\n\x12QueryMerchantScore\"\xd9\x01\n\x10MerchantMetadata\x12*\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x19.MerchantMetadata.Address\x12\x1a\n\x12remaining_attempts\x18\x02 \x01(\x05\x1a/\n\x0c\x46unctionType\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1aL\n\x07\x41\x64\x64ress\x12\n\n\x02id\x18\x01 \x01(\t\x12\x35\n\rfunction_type\x18\x02 \x01(\x0b\x32\x1e.MerchantMetadata.FunctionTypeB-\n)com.ververica.statefun.workshop.generatedP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_CONFIRMFRAUD = _descriptor.Descriptor(
  name='ConfirmFraud',
  full_name='ConfirmFraud',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='ConfirmFraud.account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=82,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='Transaction.account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Transaction.timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='merchant', full_name='Transaction.merchant', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='Transaction.amount', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=195,
)


_FEATUREVECTOR = _descriptor.Descriptor(
  name='FeatureVector',
  full_name='FeatureVector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fraud_count', full_name='FeatureVector.fraud_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='merchant_score', full_name='FeatureVector.merchant_score', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='FeatureVector.amount', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=273,
)


_FRAUDSCORE = _descriptor.Descriptor(
  name='FraudScore',
  full_name='FraudScore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='score', full_name='FraudScore.score', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=275,
  serialized_end=302,
)


_REPORTEDFRAUD = _descriptor.Descriptor(
  name='ReportedFraud',
  full_name='ReportedFraud',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='ReportedFraud.count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=304,
  serialized_end=334,
)


_EXPIREFRAUD = _descriptor.Descriptor(
  name='ExpireFraud',
  full_name='ExpireFraud',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=336,
  serialized_end=349,
)


_QUERYFRAUD = _descriptor.Descriptor(
  name='QueryFraud',
  full_name='QueryFraud',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=363,
)


_MERCHANTSCORE = _descriptor.Descriptor(
  name='MerchantScore',
  full_name='MerchantScore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='score', full_name='MerchantScore.score', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='MerchantScore.error', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=410,
)


_QUERYMERCHANTSCORE = _descriptor.Descriptor(
  name='QueryMerchantScore',
  full_name='QueryMerchantScore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=412,
  serialized_end=432,
)


_MERCHANTMETADATA_FUNCTIONTYPE = _descriptor.Descriptor(
  name='FunctionType',
  full_name='MerchantMetadata.FunctionType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='MerchantMetadata.FunctionType.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='MerchantMetadata.FunctionType.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=527,
  serialized_end=574,
)

_MERCHANTMETADATA_ADDRESS = _descriptor.Descriptor(
  name='Address',
  full_name='MerchantMetadata.Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='MerchantMetadata.Address.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='function_type', full_name='MerchantMetadata.Address.function_type', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=576,
  serialized_end=652,
)

_MERCHANTMETADATA = _descriptor.Descriptor(
  name='MerchantMetadata',
  full_name='MerchantMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='MerchantMetadata.address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remaining_attempts', full_name='MerchantMetadata.remaining_attempts', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MERCHANTMETADATA_FUNCTIONTYPE, _MERCHANTMETADATA_ADDRESS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=652,
)

_TRANSACTION.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MERCHANTMETADATA_FUNCTIONTYPE.containing_type = _MERCHANTMETADATA
_MERCHANTMETADATA_ADDRESS.fields_by_name['function_type'].message_type = _MERCHANTMETADATA_FUNCTIONTYPE
_MERCHANTMETADATA_ADDRESS.containing_type = _MERCHANTMETADATA
_MERCHANTMETADATA.fields_by_name['address'].message_type = _MERCHANTMETADATA_ADDRESS
DESCRIPTOR.message_types_by_name['ConfirmFraud'] = _CONFIRMFRAUD
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['FeatureVector'] = _FEATUREVECTOR
DESCRIPTOR.message_types_by_name['FraudScore'] = _FRAUDSCORE
DESCRIPTOR.message_types_by_name['ReportedFraud'] = _REPORTEDFRAUD
DESCRIPTOR.message_types_by_name['ExpireFraud'] = _EXPIREFRAUD
DESCRIPTOR.message_types_by_name['QueryFraud'] = _QUERYFRAUD
DESCRIPTOR.message_types_by_name['MerchantScore'] = _MERCHANTSCORE
DESCRIPTOR.message_types_by_name['QueryMerchantScore'] = _QUERYMERCHANTSCORE
DESCRIPTOR.message_types_by_name['MerchantMetadata'] = _MERCHANTMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfirmFraud = _reflection.GeneratedProtocolMessageType('ConfirmFraud', (_message.Message,), dict(
  DESCRIPTOR = _CONFIRMFRAUD,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:ConfirmFraud)
  ))
_sym_db.RegisterMessage(ConfirmFraud)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

FeatureVector = _reflection.GeneratedProtocolMessageType('FeatureVector', (_message.Message,), dict(
  DESCRIPTOR = _FEATUREVECTOR,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:FeatureVector)
  ))
_sym_db.RegisterMessage(FeatureVector)

FraudScore = _reflection.GeneratedProtocolMessageType('FraudScore', (_message.Message,), dict(
  DESCRIPTOR = _FRAUDSCORE,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:FraudScore)
  ))
_sym_db.RegisterMessage(FraudScore)

ReportedFraud = _reflection.GeneratedProtocolMessageType('ReportedFraud', (_message.Message,), dict(
  DESCRIPTOR = _REPORTEDFRAUD,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:ReportedFraud)
  ))
_sym_db.RegisterMessage(ReportedFraud)

ExpireFraud = _reflection.GeneratedProtocolMessageType('ExpireFraud', (_message.Message,), dict(
  DESCRIPTOR = _EXPIREFRAUD,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:ExpireFraud)
  ))
_sym_db.RegisterMessage(ExpireFraud)

QueryFraud = _reflection.GeneratedProtocolMessageType('QueryFraud', (_message.Message,), dict(
  DESCRIPTOR = _QUERYFRAUD,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:QueryFraud)
  ))
_sym_db.RegisterMessage(QueryFraud)

MerchantScore = _reflection.GeneratedProtocolMessageType('MerchantScore', (_message.Message,), dict(
  DESCRIPTOR = _MERCHANTSCORE,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:MerchantScore)
  ))
_sym_db.RegisterMessage(MerchantScore)

QueryMerchantScore = _reflection.GeneratedProtocolMessageType('QueryMerchantScore', (_message.Message,), dict(
  DESCRIPTOR = _QUERYMERCHANTSCORE,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:QueryMerchantScore)
  ))
_sym_db.RegisterMessage(QueryMerchantScore)

MerchantMetadata = _reflection.GeneratedProtocolMessageType('MerchantMetadata', (_message.Message,), dict(

  FunctionType = _reflection.GeneratedProtocolMessageType('FunctionType', (_message.Message,), dict(
    DESCRIPTOR = _MERCHANTMETADATA_FUNCTIONTYPE,
    __module__ = 'entities_pb2'
    # @@protoc_insertion_point(class_scope:MerchantMetadata.FunctionType)
    ))
  ,

  Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), dict(
    DESCRIPTOR = _MERCHANTMETADATA_ADDRESS,
    __module__ = 'entities_pb2'
    # @@protoc_insertion_point(class_scope:MerchantMetadata.Address)
    ))
  ,
  DESCRIPTOR = _MERCHANTMETADATA,
  __module__ = 'entities_pb2'
  # @@protoc_insertion_point(class_scope:MerchantMetadata)
  ))
_sym_db.RegisterMessage(MerchantMetadata)
_sym_db.RegisterMessage(MerchantMetadata.FunctionType)
_sym_db.RegisterMessage(MerchantMetadata.Address)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
