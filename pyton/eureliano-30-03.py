

grafo1 = {
    1: [2,3,6,7],
    2: [1,3,4,5],
    3: [1,2,4,7],
    4: [2,3,5,6],
    5: [2,4,6,7],
    6: [1,4,5,7],
    7: [1,3,5,6],
}
#
grafo2 = {
    1: [2,3,7],
    2: [1,3,4,5],
    3: [1,2,4,7],
    4: [2,3,5,6],
    5: [2,4,6,7],
    6: [4,5,7],
    7: [1,3,5,6]
}

grafo3 = {
    1: [2,3,7],
    2: [1,3,4],
    3: [1,2,4],
    4: [2,3,5,6],
    5: [4,6],
    6: [4,5,7],
    7: [1,6]
}

grafo4 = {
    1: [2,7],
    2: [1,3,4],
    3: [2,4],
    4: [2,3,5,6],
    5: [4,6],
    6: [4,5,7],
    7: [1,6]
}

grafoTeste = {
    1: [[3,0.5],4,5],
    2: [3,4,5],
    3: [1,2],
    4: [1,2],
    5: [1,2],
}

grafoEasy = {
    1: [[2,0.0],[7,0.0]],
    2: [[1,0.0],[3,0.0]],
    3: [[2,0.0],[4,0.0]],
    4: [[3,0.0],[5,0.0]],
    5: [[4,0.0],[6,0.0]],
    6: [[5,0.0],[7,0.0]],
    7: [[1,0.0],[6,0.0]]
}

# print(grafoTeste[1][0][1])
# grafoTeste[1].append([3,0.8])
# print(grafoTeste[1][0][1])
# grafoTeste[1][0][1]=2.5
# print(grafoTeste[1][0][1])
# print(grafoTeste[1])
# print(len(grafoTeste[1]))
#
# print(grafoEasy)
# print(grafoEasy[1][0][1])




# caminho=[1]
# caminho.append(2)
# print(caminho)

def Eureler(grafo):
    contador=0
    grafo_aux=grafo
    failsafe="True"
    lista_chaves = list(grafo_aux.keys())
    lista_valors = list(grafo_aux.values())
    #print(len(grafo[1]))

    for i in grafo_aux.keys():
        if (len(grafo[i]) % 2)==0:
            ""
        else:
            contador += 1
            failsafe="False"
        if contador == 0:
            failsafe = "True"
        elif contador == 2:
            failsafe = "Semi"
        else:
            failsafe = "False"

    return failsafe


def Print_Caminho(grafo):
    caminho=[]
    grafo_aux=grafo
    failsafe=True
    lista_chaves = list(grafo_aux.keys())
    lista_valors = list(grafo_aux.values())

    for i in grafo_aux.keys():
        for j in grafo_aux.keys():
            if i!=j and j in grafo_aux[i] and i not in caminho:
                #print(i,j)
                #print(i,j,"connect")
                caminho.append(i)
                break

    print(caminho)

#grafo1
if Eureler(grafo1) == "True":
    print("È Eureliano")
    Print_Caminho(grafo1)
elif Eureler(grafo1) == "Semi":
    print("È Semi-Eureliano")
    Print_Caminho(grafo1)
else:
    print("Não é Eureliano")

#grafo2

if Eureler(grafo2) == "True":
    print("È Eureliano")
    Print_Caminho(grafo2)
elif Eureler(grafo2) == "Semi":
    print("È Semi-Eureliano")
    Print_Caminho(grafo2)
else:
    print("Não é Eureliano")

#grafo3

if Eureler(grafo3) == "True":
    print("È Eureliano")
    Print_Caminho(grafo3)
elif Eureler(grafo3) == "Semi":
    print("È Semi-Eureliano")
    Print_Caminho(grafo3)
else:
    print("Não é Eureliano")

#grafo4

if Eureler(grafo4) == "True":
    print("È Eureliano")
    Print_Caminho(grafo4)
elif Eureler(grafo4) == "Semi":
    print("È Semi-Eureliano")
    Print_Caminho(grafo4)
else:
    print("Não é Eureliano")

