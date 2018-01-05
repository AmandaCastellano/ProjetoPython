"""
def funcao(lista):
    sublista2 = []
    for sublista in lista:
        for numeros in sublista:
            sublista2.append(numeros)
    return sublista2
print()
n = [[1, 2, 3], [4, 5, 6, 7, 8]]
print(funcao(n))

"""

nova = []

n2 = [1, 2, 3, 4]
n4 = [5, 6, 7, 8]
n5 = [9, 10, 11, 12]

def multiplicar(lista):
    for sublista in lista:
        n3 = sublista * 2
        nova.append(n3)
        print(nova)


multiplicar(n5)


def exibir(lista):
    for numero in lista:
        print(numero)

exibir(nova)


print()
