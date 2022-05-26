import grpc from "grpc";
import protoLoader from "@grpc/proto-loader";
import path from "path";

function inserirMatricula(call, callback) {
  console.log(call.request);
  return callback(null, {mensagem: "Success"});
}

function atualizarNota(call, callback) {
  console.log(call)
}

function atualizarFaltas(call, callback) {
  console.log(call)
}

function listarAlunosDaDisciplina(call, callback) {
  console.log(call)
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