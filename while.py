"""
n = ""
while n != 50:
    n = int(input("Digite aqui um numero inteiro: "))
    if n > 50:
        print(" Esse número é muito alto. Tente novamente: ")
"""
"""
# 1 - Crie uma lista com 20 números quaisquer (certifique-se de que alguns números são repetidos). 
Ordene a lista em ordem numérica com o método 'sort()' e exiba-a na tela.
# 2 - Exiba a quantidade de elementos que a lista possui.
# 3 - Varra todos os números da lista utilizando o for e exiba na tela apenas os números repetidos. 
Certifique-se de que cada número repetido apareça apenas uma vez.


lista = [1, 2, 4, 5, 6, 3, 7, 2, 7, 7, 4, 3, 8, 82, 97, 97, 75, 3, 86, 2]
# lista.sort()
lista1 = len(lista)
print("Existem {} números nessa lista. ".format(lista1))
lista_vazia = []

for numero in lista:
   # print(numero)
   # resp = lista.count(numero)
   # print("O número {} esta presente {} na lista.".format(numero,resp))
    if lista_vazia.count(numero) == 0:
        lista_vazia.append(numero)
        resp = lista.count(numero)
        if resp >= 2:
            print(numero)
            # print("O número {} esta presente {} vezes nessa lista.".format(numero,resp))
     
     
4 - Declare uma nova lista e insira 20 números (de 1 a 30) de forma aleatória utilizando a biblioteca 
random, com o método random.randint(inicio, limite). Ordene a lista em ordem numérica com o método 
'sort()' e exiba-a na tela. Consulte a documentação da biblioteca em caso de dúvidas.

lista3 = []

from random import randint

for numeros in range(20):
    lista3.append(randint(1, 30))
    lista3.sort()
    print(lista3)
    
5 - Pegue o código de varredura da lista com o for declarado no item 3 e coloque-o em uma função chamada 
'detectar_numeros_repetidos(lista)' que recebe um argumento referente a lista de números e retorna 
apenas os números repetidos. Execute a função para a lista de números criada no item 1 e exiba-a na tela.

def detectar_numeros_repetidos(lista4):
    lista_vazia2 = []

    for numero in lista4:
        #print(lista4)
        resp = lista4.count(numero)
        if resp >= 2:
            lista_vazia2.append(numero)

    print(lista_vazia2)


lista4 = [1, 2, 4, 5, 6, 3, 7, 2, 7, 7, 4, 3, 8, 82, 97, 97, 75, 3, 86, 2]
lista4.sort()
print(lista4)
lista4 = detectar_numeros_repetidos(lista4)

6 - Execute a função declarada no item 5 para a lista de números criada no item 4.

from random import randint

def detectar_numeros_repetidos(lista4):
    lista_vazia2 = []
    lista5 = []

    for numeros in range(20):
        lista5.append(randint(1, 30))
        lista5.sort()
        print(lista5)

    for numero in lista5:
        #print(lista4)
        resp = lista5.count(numero)
        if resp >= 2:
            lista_vazia2.append(numero)

    print(lista_vazia2)



lista4 = [1, 2, 4, 5, 6, 3, 7, 2, 7, 7, 4, 3, 8, 82, 97, 97, 75, 3, 86, 2]
lista4.sort()
print(lista4)
lista4 = detectar_numeros_repetidos(lista4)

7 - Crie uma função que receba uma lista de números e exiba na tela a quantidade de vezes que o número 
aparece repetido. Exiba a mensagem apenas para números repetidos e uma só vez por número. 
Dica: utilize o método 'lista.count(elemento)'.

def numeros_repetidos(lista5):
    lista_vazia3 = []

    for numeros in lista5:
        resp = lista5.count(numeros)
        print(resp)
        if resp >= 2:
            lista_vazia3.append(resp)
            print("O número {} esta presente {} vezes na lista.".format(numeros,resp))


lista5 = [1, 2, 3, 3, 4, 5, 5, 5]
lista5 = numeros_repetidos(lista5)


8 - Crie uma função que receba uma lista de números e retorne um dicionário para cada número, 
onde a chave do dicionário é o número em questão e o valor do dicionário é a quantidade de vezes que 
o número se repete. Utilize o método 'lista.count(elemento)'. Se o item não se repetir, exiba a 
mensagem "O número X não se repete.", caso contrário, exiba a mensagem "O número X se repete Y vezes.".
9 - Faça a mesma coisa que no item 9, porém, em vez de utilizar o método 'count()', faça a checagem para
 saber se o item em questão está no dicionário utilizando a checagem do método 'dicionário.get(chave)'.
  Caso a checagem seja negativa (o dicionário ainda não possui o numero) adicione-o no dicionário 
  utilizando 'dicionario[numero] = 1'. Caso a checagem seja positiva, atribua um valor adicional à 
  posição do dicionário utilizando: 'dicionario[numero] = dicionario[numero] + 1'.
10 - Crie uma função que insere 20 números aleatórios (de 1 a 30) em uma lista certificando de que 
NENHUM número é repetido. Ordene a lista em ordem numérica com o método 'sort()' e exiba-a na tela.
"""

from random import randint

def numeros_sem_repetir():
    lista6 = []

    while len(lista6) < 20:
        numero = randint(1,30)
        resp = lista6.count(numero)
        if resp == 0:
            lista6.append(numero)
           # print(lista6)
    return lista6

lista_aleatoria = numeros_sem_repetir()
lista_aleatoria.sort()
print(lista_aleatoria)


