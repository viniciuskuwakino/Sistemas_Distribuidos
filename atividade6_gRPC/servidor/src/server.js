import grpc from "grpc";
import protoLoader from "@grpc/proto-loader";
import path from "path";
import { dbInsertMatricula, dbUpdateNota, dbUpdateFaltas, dbListarAlunos } from "./dbController.js";


function inserirMatricula(call, callback) {
  const operacao = dbInsertMatricula(call.request);
  
  operacao.then((res) => {
    if (res == true) return callback(null, { mensagem: "Success" });
    else return callback(null, { mensagem: "Fail" });
  });
}

function atualizarNota(call, callback) {
  const operacao = dbUpdateNota(call.request);

  operacao.then((res) => {
    if (res == true) return callback(null, { mensagem: "Success" });
    else return callback(null, { mensagem: "Fail" });
  });
}

function atualizarFaltas(call, callback) {
  const operacao = dbUpdateFaltas(call.request);

  operacao.then((res) => {
    if (res == true) return callback(null, { mensagem: "Success" });
    else return callback(null, { mensagem: "Fail" });
  });
}

function listarAlunosDaDisciplina(call, callback) {
  const operacao = dbListarAlunos(call.request);

  operacao.then((res) => {
    console.log(res)
    return callback(null, res)
  });
}

function listarBoletimDoAluno(call, callback) {
  console.log(call)
}
      
const proto = protoLoader.loadSync(path.resolve("../faculdade.proto"))
const FaculdadeProto = grpc.loadPackageDefinition(proto)
const server = new grpc.Server();

server.addService(FaculdadeProto.Faculdade.service, {
  inserirMatricula,
  atualizarNota,
  atualizarFaltas,
  listarAlunosDaDisciplina,
  listarBoletimDoAluno
});


server.bind("localhost:7000", grpc.ServerCredentials.createInsecure());
console.log("Iniciando servidor!");
server.start();