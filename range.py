parque = range(5, 100, 2)
parque_lista = list(parque)
#print(len(parque_lista)*10)

def exibir(a, b, exibir=False):
    total = a + b

    if exibir == True:
        #podemos usar tbm apenas 'exibir:' ou 'exibir is True'
        print(total)


n1 = 10
n2 = 20
exibir(n1, n2, exibir=True)


def exibir_lista(lista,exibir_chave=False):

    for chave in range(len(lista)):
        if exibir_chave == True:
            numero = lista[chave]
            print("Chave:{}, Valor:{}".format(chave, numero))
        else:
             print("Valor:{}".format(numero))

lista1 = [1, 2, 4, 5, 6, 2]
exibir_lista(lista1, exibir_chave=True)

