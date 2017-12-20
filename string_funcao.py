"""
def checar_ocorrencias(texto, letra):
    numero_ocorrencias = 0
    for indice in range(len(texto)):
        letras = texto[indice]
        if letra == letras:
            numero_ocorrencias =+1
    return numero_ocorrencias


texto1 =  input(" Digite um texto: ")
letra1 =  input(" Digite uma letra: ")
ocorrencias = checar_ocorrencias(texto1,letra1)
print("A letra {} está presente {} vezes no texto {}.".format(letra1, ocorrencias, texto1))
"""


def contar_numero_pequenos(numeros):
    print(numeros)
    lista_vazia = []
    for numero in numeros:
        if numero < 10:
            lista_vazia.append(numero)
            print(lista_vazia)
    return sum(lista_vazia)


lista = [1, 7, 82, 8, 8, 65, 3]
contagem = contar_numero_pequenos(lista)
print(contagem)
