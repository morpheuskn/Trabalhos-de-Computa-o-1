def lista_a2:
    arq=open(nome,"r")
    for linha in arq:
        linha=linha.strip()
        linha=linha.stlit(",")
        print(lista)

    arq.close()
    return

lista_a2('p:/alunos.txt')
