lista = [1,1]

numero_elementos = int(input("Digite aqui quantos número terá a sua sequência: "))

for numero in range(2,numero_elementos):
    n = lista[numero - 2] + (lista[numero -1])
    lista.append(n)
    print(lista)



