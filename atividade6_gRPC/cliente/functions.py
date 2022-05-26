def setRa():
    while True:
        ra = int(input("Informe o RA:"))
        if not ra: print("Campo \"RA\" está vazio!")
        else: break
    return ra


def setCodDisciplina():
    while True:
        cod = input("Informe o codigo da disciplina:")
        if not cod: print("Campo \"cod_disciplina\" está vazio!")
        else: break
    return cod


def setAno():
    while True:
        ano = int(input("Informe o ano:"))
        if not ano: print("Campo \"ano\" está vazio!")
        else: break
    return ano


def setSemestre():
    while True:
        semestre = int(input("Informe o semestre:"))
        if not semestre: print("Campo \"semestre\" está vazio!")
        else: break
    return semestre


def setNota():
    while True:
        nota = float(input("Informa a nota:"))
        if not nota: print("Campo \"nota\" está vazio!")
        else: break
    return nota


def setFalta():
    while True:
        falta = int(input("Informe as faltas:"))
        if not falta: print("Campo \"faltas\" está vazio!")
        else: break
    return falta


def requestOperation():
    print("1 - Inserir matricula;\n")
    print("2 - Alterar nota;\n")
    print("3 - Alterar faltas;\n")
    print("4 - Listar alunos de uma disciplina;\n")
    print("5 - Listar boletim de um aluno;\n")
    op = int(input("Operacao:"))

    return op
