"""nome = "Amanda Castellano Rodrigues de Oliveira"
nome_split = nome.split(" ")
print(nome_split)

lista1 = input("Digite aqui 5 palavras de sua preferência: ",)
palavras = lista1.split(" ")

for palavras_digitadas in palavras:
    print(palavras_digitadas)

lista2 = []

for palavras in range(3):
    palavras_digitadas = input("Digite aqui uma palavra de sua preferência: ")
    lista2.append(palavras_digitadas)
    print(lista2)

lista2.reverse()
print(lista2)

lista3 = ["amanda", "castellano", "rodrigues"]
nome = "_".join(lista3)
print(nome)
"""

lista4 = input("Digite aqui seu nome completo: ")
print(lista4)

nome = lista4.split(" ")
print(nome)

nome.reverse()
print(nome)

nome2 = " ". join(nome)
print(nome2)
