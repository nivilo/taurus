# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: collector.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='collector.proto',
  package='taurus',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0f\x63ollector.proto\x12\x06taurus\"T\n\x12\x43\x61ndlestickRequest\x12\x17\n\x0ftimestamp_start\x18\x01 \x01(\x03\x12\x15\n\rtimestamp_end\x18\x02 \x01(\x03\x12\x0e\n\x06symbol\x18\x03 \x01(\t\"x\n\x0b\x43\x61ndlestick\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x0c\n\x04open\x18\x02 \x01(\x01\x12\x0c\n\x04high\x18\x03 \x01(\x01\x12\x0b\n\x03low\x18\x04 \x01(\x01\x12\r\n\x05\x63lose\x18\x05 \x01(\x01\x12\x0e\n\x06volume\x18\x06 \x01(\x01\x12\x0e\n\x06symbol\x18\x07 \x01(\t\";\n\x0e\x43\x61ndlestickSet\x12)\n\x0c\x63\x61ndlesticks\x18\x01 \x03(\x0b\x32\x13.taurus.Candlestick\"h\n\x0cTradeRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0ftimestamp_start\x18\x02 \x01(\x03\x12\x15\n\rtimestamp_end\x18\x03 \x01(\x03\x12\x0e\n\x06symbol\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\"\xfe\x01\n\x05Trade\x12\x0c\n\x04info\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x10\n\x08\x64\x61tetime\x18\x04 \x01(\t\x12\x0e\n\x06symbol\x18\x05 \x01(\t\x12\r\n\x05order\x18\x06 \x01(\t\x12\x0c\n\x04type\x18\x07 \x01(\t\x12\x0c\n\x04side\x18\x08 \x01(\t\x12\x14\n\x0ctakerOrMaker\x18\t \x01(\t\x12\r\n\x05price\x18\n \x01(\x01\x12\x0e\n\x06\x61mount\x18\x0b \x01(\x01\x12\x0c\n\x04\x63ost\x18\x0c \x01(\x01\x12\x10\n\x08\x66\x65\x65_cost\x18\r \x01(\x01\x12\x14\n\x0c\x66\x65\x65_currency\x18\x0e \x01(\t\x12\x10\n\x08\x66\x65\x65_rate\x18\x0f \x01(\x01\")\n\x08TradeSet\x12\x1d\n\x06trades\x18\x01 \x03(\x0b\x32\r.taurus.Trade2\x83\x02\n\tCollector\x12\x43\n\x0eGetCandlestick\x12\x1a.taurus.CandlestickRequest\x1a\x13.taurus.Candlestick\"\x00\x12G\n\x0fGetCandlesticks\x12\x1a.taurus.CandlestickRequest\x1a\x16.taurus.CandlestickSet\"\x00\x12\x31\n\x08GetTrade\x12\x14.taurus.TradeRequest\x1a\r.taurus.Trade\"\x00\x12\x35\n\tGetTrades\x12\x14.taurus.TradeRequest\x1a\x10.taurus.TradeSet\"\x00\x62\x06proto3')
)




_CANDLESTICKREQUEST = _descriptor.Descriptor(
  name='CandlestickRequest',
  full_name='taurus.CandlestickRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_start', full_name='taurus.CandlestickRequest.timestamp_start', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_end', full_name='taurus.CandlestickRequest.timestamp_end', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='taurus.CandlestickRequest.symbol', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=27,
  serialized_end=111,
)


_CANDLESTICK = _descriptor.Descriptor(
  name='Candlestick',
  full_name='taurus.Candlestick',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='taurus.Candlestick.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='open', full_name='taurus.Candlestick.open', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='taurus.Candlestick.high', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low', full_name='taurus.Candlestick.low', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close', full_name='taurus.Candlestick.close', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='taurus.Candlestick.volume', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='taurus.Candlestick.symbol', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=113,
  serialized_end=233,
)


_CANDLESTICKSET = _descriptor.Descriptor(
  name='CandlestickSet',
  full_name='taurus.CandlestickSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='candlesticks', full_name='taurus.CandlestickSet.candlesticks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=235,
  serialized_end=294,
)


_TRADEREQUEST = _descriptor.Descriptor(
  name='TradeRequest',
  full_name='taurus.TradeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='taurus.TradeRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_start', full_name='taurus.TradeRequest.timestamp_start', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_end', full_name='taurus.TradeRequest.timestamp_end', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='taurus.TradeRequest.symbol', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='taurus.TradeRequest.type', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=296,
  serialized_end=400,
)


_TRADE = _descriptor.Descriptor(
  name='Trade',
  full_name='taurus.Trade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='taurus.Trade.info', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='taurus.Trade.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='taurus.Trade.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datetime', full_name='taurus.Trade.datetime', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='taurus.Trade.symbol', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order', full_name='taurus.Trade.order', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='taurus.Trade.type', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='side', full_name='taurus.Trade.side', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='takerOrMaker', full_name='taurus.Trade.takerOrMaker', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='taurus.Trade.price', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='taurus.Trade.amount', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost', full_name='taurus.Trade.cost', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_cost', full_name='taurus.Trade.fee_cost', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_currency', full_name='taurus.Trade.fee_currency', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_rate', full_name='taurus.Trade.fee_rate', index=14,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=403,
  serialized_end=657,
)


_TRADESET = _descriptor.Descriptor(
  name='TradeSet',
  full_name='taurus.TradeSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trades', full_name='taurus.TradeSet.trades', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=659,
  serialized_end=700,
)

_CANDLESTICKSET.fields_by_name['candlesticks'].message_type = _CANDLESTICK
_TRADESET.fields_by_name['trades'].message_type = _TRADE
DESCRIPTOR.message_types_by_name['CandlestickRequest'] = _CANDLESTICKREQUEST
DESCRIPTOR.message_types_by_name['Candlestick'] = _CANDLESTICK
DESCRIPTOR.message_types_by_name['CandlestickSet'] = _CANDLESTICKSET
DESCRIPTOR.message_types_by_name['TradeRequest'] = _TRADEREQUEST
DESCRIPTOR.message_types_by_name['Trade'] = _TRADE
DESCRIPTOR.message_types_by_name['TradeSet'] = _TRADESET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CandlestickRequest = _reflection.GeneratedProtocolMessageType('CandlestickRequest', (_message.Message,), dict(
  DESCRIPTOR = _CANDLESTICKREQUEST,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:taurus.CandlestickRequest)
  ))
_sym_db.RegisterMessage(CandlestickRequest)

Candlestick = _reflection.GeneratedProtocolMessageType('Candlestick', (_message.Message,), dict(
  DESCRIPTOR = _CANDLESTICK,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:taurus.Candlestick)
  ))
_sym_db.RegisterMessage(Candlestick)

CandlestickSet = _reflection.GeneratedProtocolMessageType('CandlestickSet', (_message.Message,), dict(
  DESCRIPTOR = _CANDLESTICKSET,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:taurus.CandlestickSet)
  ))
_sym_db.RegisterMessage(CandlestickSet)

TradeRequest = _reflection.GeneratedProtocolMessageType('TradeRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRADEREQUEST,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:taurus.TradeRequest)
  ))
_sym_db.RegisterMessage(TradeRequest)

Trade = _reflection.GeneratedProtocolMessageType('Trade', (_message.Message,), dict(
  DESCRIPTOR = _TRADE,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:taurus.Trade)
  ))
_sym_db.RegisterMessage(Trade)

TradeSet = _reflection.GeneratedProtocolMessageType('TradeSet', (_message.Message,), dict(
  DESCRIPTOR = _TRADESET,
  __module__ = 'collector_pb2'
  # @@protoc_insertion_point(class_scope:taurus.TradeSet)
  ))
_sym_db.RegisterMessage(TradeSet)



_COLLECTOR = _descriptor.ServiceDescriptor(
  name='Collector',
  full_name='taurus.Collector',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=703,
  serialized_end=962,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCandlestick',
    full_name='taurus.Collector.GetCandlestick',
    index=0,
    containing_service=None,
    input_type=_CANDLESTICKREQUEST,
    output_type=_CANDLESTICK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetCandlesticks',
    full_name='taurus.Collector.GetCandlesticks',
    index=1,
    containing_service=None,
    input_type=_CANDLESTICKREQUEST,
    output_type=_CANDLESTICKSET,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTrade',
    full_name='taurus.Collector.GetTrade',
    index=2,
    containing_service=None,
    input_type=_TRADEREQUEST,
    output_type=_TRADE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTrades',
    full_name='taurus.Collector.GetTrades',
    index=3,
    containing_service=None,
    input_type=_TRADEREQUEST,
    output_type=_TRADESET,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_COLLECTOR)

DESCRIPTOR.services_by_name['Collector'] = _COLLECTOR

# @@protoc_insertion_point(module_scope)