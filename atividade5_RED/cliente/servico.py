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

    - Data de criação: 08/05/2022
    - Data de atualização: 25/05/2022
"""

import socket  # Utilizar socket TCP
import faculdade_pb2  # Funções de marshalling e unmarshalling
from functions import *  # Funções de setters ra, cod_disciplina, ano, semestre, nota e faltas


# Funcao que manda para o servidor o tipo da operacao que será realizada;
def tipoOP(num):

    # Preenche a estrutura da operacao;
    operacao = faculdade_pb2.Op()
    operacao.tipo = num

    # Marshalling
    op = operacao.SerializeToString()
    size = len(op)

    # Envia o tipo da operacao
    client_socket.send((str(size) + "\n").encode())
    client_socket.send(op)


# Funcao que recebe uma resposta do servidor: Success ou Fail, e retorna a mensagem;
def resposta():

    # Recebe a resposta do servidor
    res = faculdade_pb2.Resposta()
    res.ParseFromString(client_socket.recv(1024))

    return res.mensagem


# Funcao que recebe do servidor o numero de alunos e retorna a quantidade;
def getQuantidade():

    # Recebe a resposta do servidor
    tam = faculdade_pb2.Tamanho()
    tam.ParseFromString(client_socket.recv(1024))

    return tam


# Funcao de inserir matricula
def inserirMatricula():

    # Operacao de inserir matricula é do tipo 1;
    tipoOP(1)

    # Preenche a estrutura da matricula, porém com as notas e faltas com o valor padrao 0;
    matricula = faculdade_pb2.Matricula()
    matricula.ra = setRa()
    matricula.cod_disciplina = setCodDisciplina()
    matricula.ano = setAno()
    matricula.semestre = setSemestre()
    matricula.nota = 0
    matricula.faltas = 0

    # Marshalling
    msg = matricula.SerializeToString()
    size = len(msg)

    # Envia todos os dados da matricula
    client_socket.send((str(size) + "\n").encode())
    client_socket.send(msg)

    # Recebe a resposta do servidor
    print("MENSAGEM:" + resposta())


# Funcao de alterar notas de uma matrícula
def alterarNotas():

    # Operacao de alterar notas é do tipo 2;
    tipoOP(2)

    # Preenche a estrutura da matricula, porém, enviando tambem o campo "nota";
    matricula = faculdade_pb2.Matricula()
    matricula.ra = setRa()
    matricula.cod_disciplina = setCodDisciplina()
    matricula.ano = setAno()
    matricula.semestre = setSemestre()
    matricula.nota = setNota()

    # Marshalling
    msg = matricula.SerializeToString()
    size = len(msg)

    # Envia todos os dados da matricula com a nota;
    client_socket.send((str(size) + "\n").encode())
    client_socket.send(msg)

    # Recebe a resposta do servidor
    print("MENSAGEM:" + resposta())


# Funcao de alterar faltas de uma matrícula
def alterarFaltas():

    # Operacao de alterar faltas é do tipo 3;
    tipoOP(3)

    # Preenche a estrutura da matricula, porém, enviando tambem o campo "faltas";
    matricula = faculdade_pb2.Matricula()
    matricula.ra = setRa()
    matricula.cod_disciplina = setCodDisciplina()
    matricula.ano = setAno()
    matricula.semestre = setSemestre()
    matricula.faltas = setFalta()

    # Marshalling
    msg = matricula.SerializeToString()
    size = len(msg)

    # Envia todos os dados da matricula com as faltas;
    client_socket.send((str(size) + "\n").encode())
    client_socket.send(msg)

    # Recebe a resposta do servidor
    print("MENSAGEM:" + resposta())


# Funcao de listar alunos de uma disciplina
def listarAlunosDaDisciplina():

    # Operacao listar alunos da disciplina é do tipo 4;
    tipoOP(4)

    # Preenche a estrutura da matricula enviando apenas: codigo da disciplina, ano e semestre;
    matricula = faculdade_pb2.Matricula()
    matricula.cod_disciplina = setCodDisciplina()
    matricula.ano = setAno()
    matricula.semestre = setSemestre()

    # Marshalling
    msg = matricula.SerializeToString()
    size = len(msg)

    # Envia os dados da matricula;
    client_socket.send((str(size) + "\n").encode())
    client_socket.send(msg)

    # Recebe a resposta do servidor
    respostaServidor = resposta()
    if respostaServidor == "Fail":
        print("MENSAGEM:" + respostaServidor)
    else:
        print("MENSAGEM:" + respostaServidor)

        # Recebe a quantidade de alunos matriculados numa disciplina;
        qtd = getQuantidade()

        print("QUANTIDADE: " + str(qtd.quantidade))

        if qtd.quantidade > 0:
            for i in range(qtd.quantidade):

                # Recebe aluno do servidor e faz unmarshalling
                aluno = faculdade_pb2.Aluno()
                aluno.ParseFromString(client_socket.recv(1024))

                # Imprime os dados do aluno
                print("RA: " + str(aluno.ra))
                print("NOME: " + aluno.nome)
                print("PERIODO: " + str(aluno.periodo))


# Funcao de mostrar o boletim de um aluno
def boletimAluno():

    # Operacao de mostrar o boletim de um aluno é do tipo 5;
    tipoOP(5)

    # Preenche a estrutura da matricula enviando apenas: ra, ano e semestre;
    matricula = faculdade_pb2.Matricula()
    matricula.ra = setRa()
    matricula.ano = setAno()
    matricula.semestre = setSemestre()

    # Marshalling
    msg = matricula.SerializeToString()
    size = len(msg)

    # Envia os dados da matricula;
    client_socket.send((str(size) + "\n").encode())
    client_socket.send(msg)

    # Recebe a resposta do servidor
    respostaServidor = resposta()

    if respostaServidor == "Fail":
        print("MENSAGEM:" + respostaServidor)
    else:
        print("MENSAGEM:" + respostaServidor)

        # Recebe a quantidade de disciplinas que um aluno está matriculado;
        qtd = getQuantidade()

        print("QUANTIDADE: " + str(qtd.quantidade))

        print("-------- BOLETIM --------")
        print("RA: " + str(matricula.ra))
        print("SEMESTRE: " + str(matricula.semestre))
        print("ANO: " + str(matricula.ano))
        print("-------------------------")

        if qtd.quantidade > 0:
            for i in range(qtd.quantidade):
                # Recebe a matricula do servidor e faz unmarshalling
                matriculaResposta = faculdade_pb2.Matricula()
                matriculaResposta.ParseFromString(client_socket.recv(1024))

                # Recebe a disciplina do servidor e faz unmarshalling
                disciplina = faculdade_pb2.Disciplina()
                disciplina.ParseFromString(client_socket.recv(1024))

                # Imprime a disciplina, nota e faltas
                print("CODIGO_DISCIPLINA:" + str(disciplina.codigo))
                print("DISCIPLINA:" + disciplina.nome)
                print("PROFESSOR:" + disciplina.professor)
                print("NOTA: %.1f" % matriculaResposta.nota)
                print("FALTAS:" + str(matriculaResposta.faltas))
                print("-------------------------")


if __name__ == '__main__':

    # AF_INET é o protocolo de endereço IP
    # SOCK_STREAM utiliza o socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conexão do socket com o localhost e a porta
    client_socket.connect(("localhost", 7000))

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
            inserirMatricula()
        elif op == 2:
            alterarNotas()
        elif op == 3:
            alterarFaltas()
        elif op == 4:
            listarAlunosDaDisciplina()
        elif op == 5:
            boletimAluno()
        else:
            print("Operação inexistente!")
