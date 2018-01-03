def contar_num_pequenos (numeros):
    total = 0
    for numero in numeros:
        if numero < 10:
            total += numero
    return total

lista = [1,2,3,4]
resultado = contar_num_pequenos(lista)
print("O resultado é {}.". format(resultado))

