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
  const { codDisciplina, ano, semestre } = matricula;
  
  const statement = await knex("Aluno")
    .select("ra", "nome", "periodo")
    .where({ ra:
      knex("Matricula")
        .select("ra")
        .where({cod_disciplina: codDisciplina, ano, semestre})
    });

  return statement;
}


