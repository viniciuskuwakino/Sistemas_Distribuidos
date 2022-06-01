/**
 * Descrição: O serviço será gerenciado em um servidor que receberá as informações via TCP.
 * O serviço deverá prover as seguintes funcionalidades remotas:
 * 1 - Inserção na tabela Matricula (notas e faltas são inseridas com valor padrão 0).
 * 2 - Alteração notas na tabela Matricula.
 * 3 - Alteração faltas na tabela Matricula.
 * 4 - Listagem de alunos (RA, nome, período) de uma disciplina informado a disciplina, ano e semestre.
 * 5 - Listagem de disciplinas, faltas e notas (RA, nome, nota, faltas) de um aluno informado o ano e semestre.
 * 
 * @author Matheus Henrique Sechineli
 * @author Vinicius Kuwakino
 * 
 * Data de criação: 27/05/2022
 * Data de atualização: 31/05/2022
 * 
 */

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


/**
 * Funcao que chama a funcao do banco de dados para inserir uma matricula.
 * 
 * @param {Request}   call      - parametro da requisicao feita pelo cliente
 * @param {Response}  callback  - parametro que envia uma resposta para o cliente
 * 
 * @returns {callback} retorna um callback, que possui os parametros de erro e 
 * o dado do mesmo tipo definido no arquivo proto, que seria uma mensagem
 * de "Success" ou "Fail". 
 */
async function inserirMatricula(call, callback) {
  const operacao = await dbInsertMatricula(call.request);

  if (operacao == true) return callback(null, { mensagem: 'Success' });
  else return callback(null, { mensagem: 'Fail' });
}


/**
 * Funcao que chama a funcao do banco de dados para atualizar a nota de uma matricula.
 * 
 * @param {Request}   call      - parametro da requisicao feita pelo cliente
 * @param {Response}  callback  - parametro que envia uma resposta para o cliente
 * 
 * @returns {callback} retorna um callback, que possui os parametros de erro e 
 * o dado do mesmo tipo definido no arquivo proto, que seria uma mensagem
 * de "Success" ou "Fail". 
 */
async function atualizarNota(call, callback) {
  const operacao = await dbUpdateNota(call.request);

  if (operacao == true) return callback(null, { mensagem: 'Success' });
  else return callback(null, { mensagem: 'Fail' });
}


/**
 * Funcao que chama a funcao do banco de dados para atualizar as faltas de uma matricula.
 * 
 * @param {Request}   call      - parametro da requisicao feita pelo cliente
 * @param {Response}  callback  - parametro que envia uma resposta para o cliente
 * 
 * @returns {callback} retorna um callback, que possui os parametros de erro e 
 * o dado do mesmo tipo definido no arquivo proto, que seria uma mensagem
 * de "Success" ou "Fail". 
 */
async function atualizarFaltas(call, callback) {
  const operacao = await dbUpdateFaltas(call.request);

  if (operacao == true) return callback(null, { mensagem: 'Success' });
  else return callback(null, { mensagem: 'Fail' });
}


/**
 * Funcao que chama a funcao do banco de dados para listar os alunos de uma disciplina.
 * 
 * @param {Request}   call      - parametro da requisicao feita pelo cliente
 * @param {Response}  callback  - parametro que envia uma resposta para o cliente
 * 
 * @returns {callback} retorna um callback, que possui os parametros de erro e 
 * o dado do mesmo tipo definido no arquivo proto, que seria um array de alunos. 
 */
async function listarAlunosDaDisciplina(call, callback) {
  const operacao = await dbListarAlunos(call.request);

  return callback(null, { alunos: operacao });
}


/**
 * Funcao que chama a funcao do banco de dados para listar o boletim de um aluno.
 * 
 * @param {Request}   call      - parametro da requisicao feita pelo cliente
 * @param {Response}  callback  - parametro que envia uma resposta para o cliente
 * 
 * @returns {callback} retorna um callback, que possui os parametros de erro e 
 * o dado do mesmo tipo definido no arquivo proto, que seria um array de 
 * disciplinas e matriculas. 
 */
async function listarBoletimDoAluno(call, callback) {
  const operacao = await dbBoletimAlunos(call.request);
  return callback(null, {
    disciplina: operacao[0],
    matricula: operacao[1],
  });
}


// Carrega o arquivo proto;
const proto = protoLoader.loadSync(path.resolve('../faculdade.proto'));

// FaculdadeProto recebe todo o pacote de hierarquia;
const FaculdadeProto = grpc.loadPackageDefinition(proto);

// Inicializacao do server;
const server = new grpc.Server();

// Adicao de servicos de cada acao definida no arquivo proto;
server.addService(FaculdadeProto.Faculdade.service, {
  inserirMatricula,
  atualizarNota,
  atualizarFaltas,
  listarAlunosDaDisciplina,
  listarBoletimDoAluno,
});

// Porta de comunicacao;
server.bind('localhost:7000', grpc.ServerCredentials.createInsecure());
console.log('Iniciando servidor!');

// Inicializacao do servidor;
server.start();
