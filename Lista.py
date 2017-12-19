"""
lista = [1, 2, 3, 4, 5]
print(lista[3])
lista[0] = 8
print(lista)
lista_1 = vazia
print(lista_1)
lista = [1,2,5,7,9]
print(lista[2:4])
print(lista[2:5])
nome = "Amanda Castellano"
print(nome[:4])
print(nome[6:])
animais = "catdogfrog"
cat = print(animais[:3])
dog = print(animais[3:6])
frog = print(animais[6:])
animais = ["gato", "cachorro", "morcego"]
print(animais)
# print(animais.index("morcego")) # slide 121
animais.insert(1, "papagaio")
print(animais)
for animal in animais:
    print(animal)

lista1 = [1, 2, 3, 4, 5, 6]
for numeros in lista1:
     numeros_2 = (numeros) * 2
     numeros_3 = (numeros) * 3
     if numeros_3 % 2 == 0:
        print(numeros_3)

lista = []

for numeros in range(3):
    numeros_digitados = int(input("Digite aqui um número: "))
    lista.append(numeros_digitados)
print(lista)

animais = ["gato", "cachorro", "morcego"]
print(animais)
animais.sort()
print(animais)
numeros = [1, 2, 3 ,4 ,-7]
print(numeros)
numeros.sort(reverse=True)
print(numeros)

lista1 = [5, 6, 3, 2, 1]
lista2 = []

for numero in lista1:
    numero_2 = numero ** 2
    lista2.append(numero_2)
    lista2.sort()
print(lista2)

1 - Crie uma lista com alguns números inseridos manualmente (não há necessidade do usuário inserí-los).
2 - Crie um for que varra cada elemento da lista e exiba-o no console.
3 - Declare um novo for que exiba apenas os números maiores que 3.
4 - Declare um outro for que exiba apenas os números pares.
5 - Exiba na tela a soma de todos os elementos da lista sem a utilização de funções extras.
6 - Exiba a soma de todos os elementos utilizando a função sum().
7 - Crie uma nova lista a partir de números digitados pelo usuário, faça com que o usuário insira 10 números, porém, utilize o 'for' para isso, em vez de declarar 10 vezes o input de entrada de informação, declare apenas UMA vez e faça com que ele seja executado 10 vezes.
A cada atualização da lista, exiba a quantidade de elementos que ela possui.
8 - Exiba apenas os três primeiros elementos da lista no console.
9 - Exiba apenas os três últimos elementos da lista no console.
10 - Declare uma nova lista vazia chamada 'nomes' e armazene 3 nomes
digitados pelo usuário, ordene esses nomes por ordem alfabética e
exiba-os na tela, um de cada vez.

lista1 = [1, 2, 3, 4, 5, 6, 7]

# for numeros in lista1:
#    print(numeros)

# for numeros in lista1:
#    if numeros > 3:
#        print(numeros)

# for numeros in lista1:
#    if numeros % 2 == 0:
#        print(numeros)

total = 0
for numeros in lista1:
    total += numeros

# print(total)

resultado = sum(lista1)
# print(resultado)

lista2 = []
for numeros in range(10):
    #numeros_digitados = int(input("Digite aqui um número: "))
    lista2.append(numeros_digitados)
# print(lista2)
# print(lista2[:2])
# print(lista2[7:])

nomes = []
for nome in range(3):
    nome_digitados = input("Digite aqui um nome: ")
    nomes.append(nome_digitados)
    nomes.sort()

for n in nomes:
    print(n)
"""
