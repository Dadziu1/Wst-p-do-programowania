import random

def find(lista, wartosc):
    for x in range(0,len(lista)):
        if lista[x] == wartosc :
            lista.append()
        return lista

lista = [random.randint(0, 20) for x in range(10)]
print(lista)
userIn = int(input("Podaj szukana wartosc: "))
print(find(lista,userIn))