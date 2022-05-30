import protoLoader from '@grpc/proto-loader';
import grpc from 'grpc';
import path from 'path';
import {
  dbBoletimAlunos,
  dbInsertMatricula,
  dbListarAlunos,
  dbUpdateFaltas,
  dbUpdateNota,
} from './dbController.js';

async function inserirMatricula(call, callback) {
  const operacao = await dbInsertMatricula(call.request);

  if (operacao == true) return callback(null, { mensagem: 'Success' });
  else return callback(null, { mensagem: 'Fail' });
}

async function atualizarNota(call, callback) {
  const operacao = await dbUpdateNota(call.request);

  if (operacao == true) return callback(null, { mensagem: 'Success' });
  else return callback(null, { mensagem: 'Fail' });
}

async function atualizarFaltas(call, callback) {
  const operacao = await dbUpdateFaltas(call.request);

  if (operacao == true) return callback(null, { mensagem: 'Success' });
  else return callback(null, { mensagem: 'Fail' });
}

async function listarAlunosDaDisciplina(call, callback) {
  const operacao = await dbListarAlunos(call.request);

  return callback(null, { alunos: operacao });
}

async function listarBoletimDoAluno(call, callback) {
  const operacao = await dbBoletimAlunos(call.request);
  return callback(null, {
    disciplina: operacao[0],
    matricula: operacao[1],
  });
}

const proto = protoLoader.loadSync(path.resolve('../faculdade.proto'));
const FaculdadeProto = grpc.loadPackageDefinition(proto);
const server = new grpc.Server();

server.addService(FaculdadeProto.Faculdade.service, {
  inserirMatricula,
  atualizarNota,
  atualizarFaltas,
  listarAlunosDaDisciplina,
  listarBoletimDoAluno,
});

server.bind('localhost:7000', grpc.ServerCredentials.createInsecure());
console.log('Iniciando servidor!');
server.start();
