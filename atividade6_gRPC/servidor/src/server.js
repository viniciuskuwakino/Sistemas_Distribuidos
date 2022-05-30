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

function inserirMatricula(call, callback) {
  const operacao = dbInsertMatricula(call.request);

  operacao.then((res) => {
    if (res == true) return callback(null, { mensagem: 'Success' });
    else return callback(null, { mensagem: 'Fail' });
  });
}

function atualizarNota(call, callback) {
  const operacao = dbUpdateNota(call.request);

  operacao.then((res) => {
    if (res == true) return callback(null, { mensagem: 'Success' });
    else return callback(null, { mensagem: 'Fail' });
  });
}

function atualizarFaltas(call, callback) {
  const operacao = dbUpdateFaltas(call.request);

  operacao.then((res) => {
    if (res == true) return callback(null, { mensagem: 'Success' });
    else return callback(null, { mensagem: 'Fail' });
  });
}

function listarAlunosDaDisciplina(call, callback) {
  const operacao = dbListarAlunos(call.request);

  operacao.then((res) => {
    return callback(null, { alunos: res });
  });
}

function listarBoletimDoAluno(call, callback) {
  const operacao = dbBoletimAlunos(call.request);
  operacao.then((res) => {
    return callback(null, {
      disciplina: res[0],
      matricula: res[1],
    });
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
