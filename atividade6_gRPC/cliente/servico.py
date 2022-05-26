import grpc
import faculdade_pb2
import faculdade_pb2_grpc
from functions import *


def inserirMatricula(stub):

    # Preenche a estrutura da matricula, porém com as notas e faltas com o valor padrao 0;
    matricula = faculdade_pb2.Matricula()
    matricula.ra = setRa()
    matricula.cod_disciplina = setCodDisciplina()
    matricula.ano = setAno()
    matricula.semestre = setSemestre()
    matricula.nota = 0
    matricula.faltas = 0

    resposta = stub.InserirMatricula(matricula)
    print(f"Mensagem: {resposta.mensagem}")


def alterarNotas(stub):
    pass


def alterarFaltas(stub):
    pass


def listarAlunosDaDisciplina(stub):
    pass


def boletimAluno(stub):
    pass


def main():

    channel = grpc.insecure_channel("localhost:7000")
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
