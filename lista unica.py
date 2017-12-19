lista = [1, 2, 3, 3, 5, 5, 6, 3, 6, 7]
"""print(lista)
lista_unica = set(lista)
print(lista_unica)
print(lista.count(5))
"""
lista_vazia = []
for numero in lista:
   # print(numero)
   # resp = lista.count(numero)
   # print("O número {} esta presente {} na lista.".format(numero,resp))
    if lista_vazia.count(numero) == 0:
        lista_vazia.append(numero)
        resp = lista.count(numero)
        if resp >= 0:
            print("O número {} esta presente {} na lista.".format(numero,resp))
        else:
            print("o número {} não é repetido.". format(numero))

