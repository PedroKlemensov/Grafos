import random

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

grafoEasy = {
    1: [[2,0],[7,0]],
    2: [[1,0],[3,0]],
    3: [[2,0],[4,0]],
    4: [[3,0],[5,0]],
    5: [[4,0],[6,0]],
    6: [[5,0],[7,0]],
    7: [[1,0],[6,0]]
}

peso=[8,9,10,11,12,13,14]
# print(Peso[0])


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
        for j in grafo_aux[i]:
            #print(i, j)
            if i!=j and j in grafo_aux[i] and i not in caminho:
                #print(i,j)
                #print(i,j,"connect")
                caminho.append(i)
                break
    caminho.append(1)
    print(caminho)


def Peso_caminho(grafo,peso):
    grafo_peso = grafo
    lista_chaves = list(grafo.keys())
    lista_valors = list(grafo.values())
    contador=0

    for i in lista_chaves:
        for j in lista_chaves:
            #print("i",i,"j",j)
            #print(grafo_peso[i][0][1],grafo_peso[i][1][1])
            contador = 0
            cont_aux = 0
            for x in grafo_peso[i]:
                #print(x[0])
                #print("contador",contador)
                # print(random.randint(0, 9))
                cont_aux += 1
                #print("auxiliar count fora", cont_aux)
                if j in x and cont_aux == 1:
                    print("entrou",i,"e",j,"recebem",peso[i-1])
                    print("auxiliar count dentro", cont_aux)

                    grafo_peso[i][cont_aux-1][1]=peso[i-1]
                    grafo_peso[j][cont_aux-1][1]=peso[i-1]
                    print(grafo_peso[i],grafo_peso[j])
                elif j in x and cont_aux == 2:
                    print("entrou",i,"e",j,"recebem",peso[i-1])
                    print("auxiliar count dentro", cont_aux)

                    grafo_peso[i][cont_aux-1][1]=peso[i-1]
                    grafo_peso[j][cont_aux-2][1]=peso[i-1]
                    print(grafo_peso[i],grafo_peso[j])
                contador=1


    for i in grafo_peso.keys():
        for j in grafo_peso[i]:
            print(i,j)





Peso_caminho(grafoEasy,peso)








# #grafo1
# if Eureler(grafo1) == "True":
#     print("È Eureliano")
#     Print_Caminho(grafo1)
# elif Eureler(grafo1) == "Semi":
#     print("È Semi-Eureliano")
#     Print_Caminho(grafo1)
# else:
#     print("Não é Eureliano")
# print()
# #grafo2
#
# if Eureler(grafo2) == "True":
#     print("È Eureliano")
#     Print_Caminho(grafo2)
# elif Eureler(grafo2) == "Semi":
#     print("È Semi-Eureliano")
#     Print_Caminho(grafo2)
# else:
#     print("Não é Eureliano")
# print()
#
# #grafo3
#
# if Eureler(grafo3) == "True":
#     print("È Eureliano")
#     Print_Caminho(grafo3)
# elif Eureler(grafo3) == "Semi":
#     print("È Semi-Eureliano")
#     Print_Caminho(grafo3)
# else:
#     print("Não é Eureliano")
# print()
#
# #grafo4
#
# if Eureler(grafo4) == "True":
#     print("È Eureliano")
#     Print_Caminho(grafo4)
# elif Eureler(grafo4) == "Semi":
#     print("È Semi-Eureliano")
#     Print_Caminho(grafo4)
# else:
#     print("Não é Eureliano")

