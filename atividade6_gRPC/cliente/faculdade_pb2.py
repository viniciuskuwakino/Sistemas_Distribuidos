# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: faculdade.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x66\x61\x63uldade.proto\"\x17\n\x03Res\x12\x10\n\x08mensagem\x18\x01 \x01(\t\"\x1d\n\x07Tamanho\x12\x12\n\nquantidade\x18\x01 \x01(\t\"%\n\x0bListaAlunos\x12\x16\n\x06\x61lunos\x18\x01 \x03(\x0b\x32\x06.Aluno\"I\n\x07\x42oletim\x12\x1f\n\ndisciplina\x18\x01 \x03(\x0b\x32\x0b.Disciplina\x12\x1d\n\tmatricula\x18\x02 \x03(\x0b\x32\n.Matricula\"%\n\x05\x43urso\x12\x0e\n\x06\x63odigo\x18\x01 \x01(\x05\x12\x0c\n\x04nome\x18\x02 \x01(\t\"P\n\nDisciplina\x12\x0e\n\x06\x63odigo\x18\x01 \x01(\t\x12\x0c\n\x04nome\x18\x02 \x01(\t\x12\x11\n\tprofessor\x18\x03 \x01(\t\x12\x11\n\tcod_curso\x18\x04 \x01(\x05\"E\n\x05\x41luno\x12\n\n\x02ra\x18\x01 \x01(\x05\x12\x0c\n\x04nome\x18\x02 \x01(\t\x12\x0f\n\x07periodo\x18\x03 \x01(\x05\x12\x11\n\tcod_curso\x18\x04 \x01(\x05\"l\n\tMatricula\x12\n\n\x02ra\x18\x01 \x01(\x05\x12\x16\n\x0e\x63od_disciplina\x18\x02 \x01(\t\x12\x0b\n\x03\x61no\x18\x03 \x01(\x05\x12\x10\n\x08semestre\x18\x04 \x01(\x05\x12\x0c\n\x04nota\x18\x05 \x01(\x02\x12\x0e\n\x06\x66\x61ltas\x18\x06 \x01(\x05\x32\xe7\x01\n\tFaculdade\x12&\n\x10InserirMatricula\x12\n.Matricula\x1a\x04.Res\"\x00\x12#\n\rAtualizarNota\x12\n.Matricula\x1a\x04.Res\"\x00\x12%\n\x0f\x41tualizarFaltas\x12\n.Matricula\x1a\x04.Res\"\x00\x12\x36\n\x18ListarAlunosDaDisciplina\x12\n.Matricula\x1a\x0c.ListaAlunos\"\x00\x12.\n\x14ListarBoletimDoAluno\x12\n.Matricula\x1a\x08.Boletim\"\x00\x62\x06proto3')



_RES = DESCRIPTOR.message_types_by_name['Res']
_TAMANHO = DESCRIPTOR.message_types_by_name['Tamanho']
_LISTAALUNOS = DESCRIPTOR.message_types_by_name['ListaAlunos']
_BOLETIM = DESCRIPTOR.message_types_by_name['Boletim']
_CURSO = DESCRIPTOR.message_types_by_name['Curso']
_DISCIPLINA = DESCRIPTOR.message_types_by_name['Disciplina']
_ALUNO = DESCRIPTOR.message_types_by_name['Aluno']
_MATRICULA = DESCRIPTOR.message_types_by_name['Matricula']
Res = _reflection.GeneratedProtocolMessageType('Res', (_message.Message,), {
  'DESCRIPTOR' : _RES,
  '__module__' : 'faculdade_pb2'
  # @@protoc_insertion_point(class_scope:Res)
  })
_sym_db.RegisterMessage(Res)

Tamanho = _reflection.GeneratedProtocolMessageType('Tamanho', (_message.Message,), {
  'DESCRIPTOR' : _TAMANHO,
  '__module__' : 'faculdade_pb2'
  # @@protoc_insertion_point(class_scope:Tamanho)
  })
_sym_db.RegisterMessage(Tamanho)

ListaAlunos = _reflection.GeneratedProtocolMessageType('ListaAlunos', (_message.Message,), {
  'DESCRIPTOR' : _LISTAALUNOS,
  '__module__' : 'faculdade_pb2'
  # @@protoc_insertion_point(class_scope:ListaAlunos)
  })
_sym_db.RegisterMessage(ListaAlunos)

Boletim = _reflection.GeneratedProtocolMessageType('Boletim', (_message.Message,), {
  'DESCRIPTOR' : _BOLETIM,
  '__module__' : 'faculdade_pb2'
  # @@protoc_insertion_point(class_scope:Boletim)
  })
_sym_db.RegisterMessage(Boletim)

Curso = _reflection.GeneratedProtocolMessageType('Curso', (_message.Message,), {
  'DESCRIPTOR' : _CURSO,
  '__module__' : 'faculdade_pb2'
  # @@protoc_insertion_point(class_scope:Curso)
  })
_sym_db.RegisterMessage(Curso)

Disciplina = _reflection.GeneratedProtocolMessageType('Disciplina', (_message.Message,), {
  'DESCRIPTOR' : _DISCIPLINA,
  '__module__' : 'faculdade_pb2'
  # @@protoc_insertion_point(class_scope:Disciplina)
  })
_sym_db.RegisterMessage(Disciplina)

Aluno = _reflection.GeneratedProtocolMessageType('Aluno', (_message.Message,), {
  'DESCRIPTOR' : _ALUNO,
  '__module__' : 'faculdade_pb2'
  # @@protoc_insertion_point(class_scope:Aluno)
  })
_sym_db.RegisterMessage(Aluno)

Matricula = _reflection.GeneratedProtocolMessageType('Matricula', (_message.Message,), {
  'DESCRIPTOR' : _MATRICULA,
  '__module__' : 'faculdade_pb2'
  # @@protoc_insertion_point(class_scope:Matricula)
  })
_sym_db.RegisterMessage(Matricula)

_FACULDADE = DESCRIPTOR.services_by_name['Faculdade']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RES._serialized_start=19
  _RES._serialized_end=42
  _TAMANHO._serialized_start=44
  _TAMANHO._serialized_end=73
  _LISTAALUNOS._serialized_start=75
  _LISTAALUNOS._serialized_end=112
  _BOLETIM._serialized_start=114
  _BOLETIM._serialized_end=187
  _CURSO._serialized_start=189
  _CURSO._serialized_end=226
  _DISCIPLINA._serialized_start=228
  _DISCIPLINA._serialized_end=308
  _ALUNO._serialized_start=310
  _ALUNO._serialized_end=379
  _MATRICULA._serialized_start=381
  _MATRICULA._serialized_end=489
  _FACULDADE._serialized_start=492
  _FACULDADE._serialized_end=723
# @@protoc_insertion_point(module_scope)
