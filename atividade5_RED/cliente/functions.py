def setRa():
    while True:
        ra = int(input("Informe o RA:"))
        if ra is None: print("Campo \"RA\" está vazio!")
        else: break
    return ra


def setCodDisciplina():
    while True:
        cod = input("Informe o codigo da disciplina:")
        if cod is None: print("Campo \"cod_disciplina\" está vazio!")
        else: break
    return cod


def setAno():
    while True:
        ano = int(input("Informe o ano:"))
        if ano is None: print("Campo \"ano\" está vazio!")
        else: break
    return ano


def setSemestre():
    while True:
        semestre = int(input("Informe o semestre:"))
        if semestre is None: print("Campo \"semestre\" está vazio!")
        else: break
    return semestre


def setNota():
    while True:
        nota = float(input("Informa a nota:"))
        if nota is None: print("Campo \"nota\" está vazio!")
        else: break
    return nota


def setFalta():
    while True:
        falta = int(input("Informe as faltas:"))
        if falta is None: print("Campo \"faltas\" está vazio!")
        else: break
    return falta
