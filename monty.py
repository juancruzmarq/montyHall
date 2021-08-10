import random as rm

lista  = [0,0,0]
mostrarLista = [lista]
a,b,c = 0,0,0
auto= 0


def llenarPuertas(lista):
    auto = rm.randint(0,2)
    for i in lista:
        if auto == 0:
            lista[0] = 1
        elif auto == 1:
            lista[1] = 1
        elif auto == 2:
            lista[2] = 1


def monty(a):
    ganados = 0
    for i in range(1000):
        lista = [0,0,0]
        llenarPuertas(lista)
        eleccion = rm.randint(0,2)
        print('puerta elegida ' + str(eleccion))
        print('numero de la lista ' + str(lista[eleccion]))
        if lista[eleccion]==1:
            if a==1:
                print('Perdiste')
            elif a==0:
                print('Ganaste')
                ganados +=1
        elif lista[eleccion] == 0:
            if a==1:
                ganados +=1 
                print('Ganaste')
            elif a==0:
                print('Perdiste')
    if a==1:
        print('Ganados '+ str(ganados))
    elif a==0:
        print('Ganados '+ str(ganados))



monty(1)