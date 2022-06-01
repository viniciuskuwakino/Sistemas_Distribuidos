"""
    - Descrição: Parte do Cliente. Implementar um serviço de gerenciamento de notas, que deverá prover as seguintes
    funcionalidades:
        - Inserção na tabela Matricula (notas e faltas são inseridas com valor padrão 0).
        - Alteração notas na tabela Matricula.
        - Alteração faltas na tabela Matricula.
        - Listagem de alunos (RA, nome, período) de uma disciplina informado a disciplina, ano e semestre.
        - Listagem de disciplinas, faltas e notas (RA, nome, nota, faltas) de um aluno informado o ano e semestre.

    - Autores:
        Matheus Henrique Sechineli
        Vinicius Kuwakino

    - Data de criação: 27/05/2022
    - Data de atualização: 01/06/2022
"""

import grpc
import faculdade_pb2
import faculdade_pb2_grpc
from functions import *


# Funcao de inserir matricula
def inserirMatricula(stub):

    # Preenche a estrutura da matricula, porém com as notas e faltas com o valor padrao 0;
    matricula = faculdade_pb2.Matricula()
    matricula.ra = setRa()
    matricula.cod_disciplina = setCodDisciplina()
    matricula.ano = setAno()
    matricula.semestre = setSemestre()
    matricula.nota = 0
    matricula.faltas = 0

    # Realiza uma chamada na funcao de inserir matricula e recebe uma resposta do servidor;
    resposta = stub.InserirMatricula(matricula)
    
    # Imprime a mensagem da resposta do servidor;
    print(f"Mensagem: {resposta.mensagem}")


# Funcao de alterar notas de uma matrícula
def alterarNotas(stub):
    
    # Preenche a estrutura da matricula, porém, enviando tambem o campo "nota";
    matricula = faculdade_pb2.Matricula()
    matricula.ra = setRa()
    matricula.cod_disciplina = setCodDisciplina()
    matricula.ano = setAno()
    matricula.semestre = setSemestre()
    matricula.nota = setNota()

    # Realiza uma chamada na funcao de atualizar nota da matricula e recebe uma resposta do servidor;
    resposta = stub.AtualizarNota(matricula)
    
    # Imprime a mensagem da resposta do servidor;
    print(f"Mensagem: {resposta.mensagem}")


# Funcao de alterar faltas de uma matrícula
def alterarFaltas(stub):

    # Preenche a estrutura da matricula, porém, enviando tambem o campo "faltas";
    matricula = faculdade_pb2.Matricula()
    matricula.ra = setRa()
    matricula.cod_disciplina = setCodDisciplina()
    matricula.ano = setAno()
    matricula.semestre = setSemestre()
    matricula.faltas = setFalta()

    # Realiza uma chamada na funcao de atualizar faltas da matricula e recebe uma resposta do servidor;
    resposta = stub.AtualizarFaltas(matricula)
    
    # Imprime a mensagem da resposta do servidor;
    print(f"Mensagem: {resposta.mensagem}")


# Funcao de listar alunos de uma disciplina
def listarAlunosDaDisciplina(stub):

    # Preenche a estrutura da matricula, porém, enviando apenas os campos: "cod_disciplina", "ano" e "semestre";
    matricula = faculdade_pb2.Matricula()
    matricula.cod_disciplina = setCodDisciplina()
    matricula.ano = setAno()
    matricula.semestre = setSemestre()

    # Realiza uma chamada na funcao de listar alunos de uma disciplina e recebe uma resposta do servidor;
    resposta = stub.ListarAlunosDaDisciplina(matricula)
    
    # Quantidade de alunos
    qtdAlunos = len(resposta.alunos)

    if qtdAlunos == 0:
        print("Mensagem: Não há alunos!")
    else:
        print(f"Mensagem: {qtdAlunos} alunos encontrados")
        for aluno in resposta.alunos:
            print("------------------------")
            print(f"RA: {aluno.ra}")
            print(f"Nome: {aluno.nome}")
            print(f"Periodo: {aluno.periodo}")
        print("------------------------")


# Funcao de mostrar o boletim de um aluno
def boletimAluno(stub):
    
    # Preenche a estrutura da matricula, porém, enviando apenas os campos: "ra", "ano" e "semestre";
    matricula = faculdade_pb2.Matricula()
    matricula.ra = setRa()
    matricula.ano = setAno()
    matricula.semestre = setSemestre()

    # Realiza uma chamada na funcao de listar o boletim de um aluno e recebe uma resposta do servidor;
    resposta = stub.ListarBoletimDoAluno(matricula)

    if len(resposta.disciplina): 
        
        print("------------BOLETIM------------")
        print(f"RA: {resposta.matricula[0].ra}")
        print(f"Ano: {resposta.matricula[0].ano}")
        print(f"Semestre: {resposta.matricula[0].semestre}")
        print("----------DISCIPlINAS----------")
        
        for index, _ in enumerate(resposta.disciplina):
            print(f"Codigo: {resposta.disciplina[index].codigo}")
            print(f"Nome: {resposta.disciplina[index].nome}")
            print(f"Professor: {resposta.disciplina[index].professor}")
            print("Nota: %.1f" % resposta.matricula[index].nota)
            print(f"Faltas: {resposta.matricula[index].faltas}")
            print("-------------------------------")
            
        print("------------BOLETIM------------")
    else: print(f"Nenhuma matricula encontrada com RA:{matricula.ra}, ANO: {matricula.ano} e SEMESTRE:{matricula.semestre}")


def main():

    # Cria um canal de comunicacao
    channel = grpc.insecure_channel("localhost:7000")
    
    # Inicializacao do stub
    stub = faculdade_pb2_grpc.FaculdadeStub(channel)

    # Tabela de funcionalidades
    while True:
        print("1 - Inserir na tabela Matrícula;")
        print("2 - Alterar notas na tabela Matrícula;")
        print("3 - Alterar faltas na tabela Matrícula;")
        print("4 - Listagem de alunos;")
        print("5 - Boletim;")

        # Recebe o numero da funcionalidade
        op = int(input("Cliente:"))

        if op == 1:
            inserirMatricula(stub)
        elif op == 2:
            alterarNotas(stub)
        elif op == 3:
            alterarFaltas(stub)
        elif op == 4:
            listarAlunosDaDisciplina(stub)
        elif op == 5:
            boletimAluno(stub)
        else:
            print("Operação inexistente!")


if __name__ == '__main__':
    main()
