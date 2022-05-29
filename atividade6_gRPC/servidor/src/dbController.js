import knex from "../database/connectDB.js"

export async function dbInsertMatricula(matricula) {
  const {ra, codDisciplina, ano, semestre} = matricula;

  const statement = await knex("Matricula")
    .insert({ ra, cod_disciplina: codDisciplina, ano, semestre, nota: 0, faltas: 0 });

  return Boolean(statement);
}
      
export async function dbUpdateNota(matricula) {
  const {ra, codDisciplina, ano, semestre, nota} = matricula;
  
  const statement = await knex("Matricula")
    .update({ nota })
    .where({ ra, cod_disciplina: codDisciplina, ano, semestre });

  return Boolean(statement);
}

export async function dbUpdateFaltas(matricula) {
  const {ra, codDisciplina, ano, semestre, faltas} = matricula;
  
  const statement = await knex("Matricula")
    .update({ faltas })
    .where({ ra, cod_disciplina: codDisciplina, ano, semestre });

  return Boolean(statement);
}

export async function dbListarAlunos(matricula) {
  const arrAlunos = [];

  const { codDisciplina, ano, semestre } = matricula;
  
  const statement = await knex("Aluno")
    .join("Matricula", {"Aluno.ra": "Matricula.ra"})
    .select("Aluno.ra", "Aluno.nome", "Aluno.periodo", "Aluno.cod_curso")
    .where({cod_disciplina: codDisciplina, ano, semestre});

  statement.map((res) => {
    const aluno = {
      ra: res.ra, 
      nome: res.nome, 
      periodo: res.periodo,
      cod_curso: res.cod_curso
    }

    arrAlunos.push(aluno);
  });

  return arrAlunos;
}


