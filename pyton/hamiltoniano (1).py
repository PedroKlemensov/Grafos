grafo1 = {
    1: [2, 3, 6, 7],
    2: [1, 3, 4, 5],
    3: [1, 2, 4, 7],
    4: [2, 3, 5, 6],
    5: [2, 4, 6, 7],
    6: [1, 4, 5, 7],
    7: [1, 3, 5, 6],
}

grafo2 = {
    1: [2, 3, 7],
    2: [1, 3, 4, 5],
    3: [1, 2, 4, 7],
    4: [2, 3, 5, 6],
    5: [2, 4, 6, 7],
    6: [4, 5, 7],
    7: [1, 3, 5, 6]
}

grafo3 = {
    1: [2, 3, 7],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [2, 3, 5, 6],
    5: [4, 6],
    6: [4, 5, 7],
    7: [1, 6]
}

grafo4 = {
    1: [2, 7],
    2: [1, 3, 4],
    3: [2, 4],
    4: [2, 3, 5, 6],
    5: [4, 6],
    6: [4, 5, 7],
    7: [1, 6]
}

grafoTeste = {
    1: [3, 4, 5],
    2: [3, 4, 5],
    3: [1, 2],
    4: [1, 2],
    5: [1, 2],
}


def ciclo_hamiltoniano(grafo):
    vetor_X = []
    auxI = 0
    lista_chaves = list(grafo.keys())
    list(grafo.values())
    contador = 0

    for i in grafo.keys():
        vetor_X.append(grafo.get(i))
        # print(vetor_X[aux])

        auxJ = 0
        for _ in grafo[i]:

            # print(grafo[i][auxJ])
            if i + 1 == grafo[i][auxJ]:
                # print("possui proximo valor")
                # print(i+1)
                contador += 1

                # print("TESTES")
                # print(len(grafo))
            # print("TESTÃO")
            auxJ += 1

        auxI += 1

    print(" ")
    for o in grafo[len(grafo)]:
        if o == lista_chaves[0]:
            contador += 1

    if contador == len(grafo):
        print("O grafo Possui Ciclo Hamiltoniano")
    else:
        print("O grafo não Possui Ciclo Hamiltoniano")


def CheckDirac(grafo):
    # DIRAC
    # n = vertices
    # se Grafo = (V,A) com n vertices >= 3 vertices e d(x)(n° arestas no vertice) >= n/2 então G tem um ciclo hamiltoniano
    # ex (um vertice com 2 < 5 vertices totais/2)
    # "cada vertice esta ligado pelo menos a metade de todos os vertices"
    # "checagem de hamiltoniano, se o grafo tem >= 3 vertices E se cada vertice tem grau >= n/2
    # tem casos onde que a segunda regra n é comprida mas é hamiltoniano ex a-b-c-d-e-a.

    print(" ")
    print("Checkagem de Dirac: ")
    contador = 0
    cont_graus = 0
    cont_regra_dirac = 0
    limite_regra = len(grafo) / 2

    for i in grafo.keys():
        contador += 1

        for _ in grafo[i]:
            cont_graus += 1
        if cont_graus >= limite_regra:
            cont_regra_dirac += 1

        cont_graus = 0

    # Regra d(x)>=n/2 de dirac
    if cont_regra_dirac == len(grafo):
        print("Satisfaz a regra d(x) >= n/2 de Dirac")
    else:
        print("Não satisfaz a regra d(x) >= n/2 de Dirac")
    # ------------------------------------------------------------#
    # Regra N>=3 de dirac
    if contador < 3:
        print("Não satisfaz a regra N>=3 de Dirac")

    else:
        print("Satisfaz a regra N>=3 de Dirac")


def ORE(grafo):

    # ORE
    # seja um grafo n° vertice >=3 e que vertices n adjacentes sua soma de graus seja maior que o n° de vertic
    # d(x)+d(y)>= n° de vertic
    # tem casos onde que a segunda regra n é comprida mas é hamiltoniano ex a-b-c-d-e-a. bruh

    # bondy inserir mais vertices até descobrir e é hamiltoniano
    print(" ")
    print("Checkagem de ORE: ")
    cont_ORE = 1
    failSafe = False
    holder_aux = 0
    lista_chaves = list(grafo.keys())

    for i in grafo.keys():
        # print(i)
        for j in grafo[i]:
            # print(j)
            if lista_chaves[cont_ORE] == j:
                ""
            else:
                failSafe = True
                holder_aux = lista_chaves[cont_ORE]
                break
            cont_ORE += 1

        if failSafe:
            break
        else:
            ""

    # print("Adjacente: ")
    # print(holder_aux)

    qtdVdx = 0
    qtdVdy = 0
    for _ in grafo[1]:
        qtdVdx += 1
    for _ in grafo[holder_aux]:
        qtdVdy += 1
    soma_final = qtdVdx + qtdVdy

    if soma_final >= len(grafo):
        print("Satisfaz a regra d(x)+d(y) >= n")
    else:
        print("Não satisfaz a regra d(x)+d(y) >= n")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# chamando as funçoes pros grafos

def chamada():


    ORE(grafo2)





chamada()
