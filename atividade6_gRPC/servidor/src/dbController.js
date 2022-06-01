/**
 * Descrição: As funcionalidades de insercao de matricula, alteracao de notas e faltas,
 * listagem de alunos dada uma disciplina e listagem do boletim de um aluno; que se 
 * comunica com o banco de dados, estao sendo gerenciadas neste controller.
 * 
 * @author Matheus Henrique Sechineli
 * @author Vinicius Kuwakino
 * 
 * Data de criação: 27/05/2022
 * Data de atualização: 01/06/2022
 * 
 */

import knex from '../database/connectDB.js';


/**
 * Funcao do banco de dados que realiza a insercao de matricula.
 * 
 * @param {Request} matricula - recebe os dados da matricula na requisicao do cliente
 * 
 * @returns {Boolean} retorna um boleano da operacao de inserir matricula
 */
export async function dbInsertMatricula(matricula) {
  const { ra, codDisciplina, ano, semestre } = matricula;

  const statement = await knex('Matricula').insert({
    ra,
    cod_disciplina: codDisciplina,
    ano,
    semestre,
    nota: 0,
    faltas: 0,
  });

  return Boolean(statement);
}


/**
 * Funcao do banco de dados que realiza a atualizacao da nota de uma matricula.
 * 
 * @param {Request} matricula - recebe os dados da matricula na requisicao do cliente
 * 
 * @returns {Boolean} retorna um boleano da operacao de atualizar nota.
 */
export async function dbUpdateNota(matricula) {
  const { ra, codDisciplina, ano, semestre, nota } = matricula;

  const statement = await knex('Matricula')
    .update({ nota })
    .where({ ra, cod_disciplina: codDisciplina, ano, semestre });

  return Boolean(statement);
}


/**
 * Funcao do banco de dados que realiza a atualizacao das faltas de uma matricula.
 * 
 * @param {Request} matricula - recebe os dados da matricula na requisicao do cliente
 * 
 * @returns {Boolean} retorna um boleano da operacao de atualizar faltas.
 */
export async function dbUpdateFaltas(matricula) {
  const { ra, codDisciplina, ano, semestre, faltas } = matricula;

  const statement = await knex('Matricula')
    .update({ faltas })
    .where({ ra, cod_disciplina: codDisciplina, ano, semestre });

  return Boolean(statement);
}


/**
 * Funcao do banco de dados que realiza a listagem de alunos de uma disciplina.
 * 
 * @param {Request} matricula - recebe os dados da matricula na requisicao do cliente
 * 
 * @returns {Array} retorna um array de alunos dada a disciplina.
 */
export async function dbListarAlunos(matricula) {
  const { codDisciplina, ano, semestre } = matricula;

  const statement = await knex('Aluno')
    .join('Matricula', { 'Aluno.ra': 'Matricula.ra' })
    .select('Aluno.ra', 'Aluno.nome', 'Aluno.periodo', 'Aluno.cod_curso')
    .where({ cod_disciplina: codDisciplina, ano, semestre });

  const arrAlunos = statement.map((res) => {
    return {
      ra: res.ra,
      nome: res.nome,
      periodo: res.periodo,
      cod_curso: res.cod_curso,
    };
  });

  return arrAlunos;
}


/**
 * Funcao do banco de dados que realiza a listagem do boletim dado um aluno.
 * 
 * @param {Request} matricula - recebe os dados da matricula na requisicao do cliente
 * 
 * @returns {Array} retorna um array de disciplinas e matriculas.
 */
export async function dbBoletimAlunos(matricula) {
  const arrMatricula = [];
  const arrDisciplina = [];

  const { ra, ano, semestre } = matricula;

  const statement = await knex('Matricula')
    .join('Disciplina', {
      'Matricula.cod_disciplina': 'Disciplina.codigo',
    })
    .where({ ra, ano, semestre });

  statement.forEach((statement) => {
    arrMatricula.push({
      ra: statement.ra,
      ano: statement.ano,
      semestre: statement.semestre,
      codDisciplina: statement.cod_disciplina,
      faltas: statement.faltas,
      nota: statement.nota,
    });
    arrDisciplina.push({
      codigo: statement.codigo,
      nome: statement.nome,
      professor: statement.professor,
      codCurso: statement.cod_curso,
    });
  });

  return [arrDisciplina, arrMatricula];
}
