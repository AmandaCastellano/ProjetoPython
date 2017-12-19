"""
1 - Crie um programa que receba um número digitado pelo usuário e execute um 'for' pelo exato número
de vezes do número digitado.
2 - Para cada vez que o 'for' rodar, cheque se o número principal que foi digitado é divisível por
aquele número que está no for em questão.
Para saber se um número é divisível pelo outro, saiba que o resto da divisão inteira deve resultar em 0 (zero).
Dica: Crie uma variável chamada 'contador' e para cada vez que um número for divisível pelo outro,
acrescente 1 (um) ao valor do contador, se ao final da execução do loop, o contador for igual a 2,
significa que o número é primo, caso contrário (3 ou mais) o número NÃO é primo.
Outra dica: Quando o range é utilizado, o for começa a ser executado a partir do índice 0, por tanto,
o número que você terá que começar a realizar a divisão é 1.
"""

"""
numeros_primos = int(input("Digite aqui um número: "))

for numeros in range(5):
    contador = numeros_primos % (numeros + 1)
    contador += 1
    if contador == 2:
        primos.append(numeros_primos)
    else:
        print(" Tente Novamente.")


print(primos)
"""

numero = int(input("Digite aqui um numero: "))
divisiveis = 0

for index in range(numero):
    # print(index)
    # print(numero)
    # print()
    divisivel = index + 1
    if numero % divisivel == 0:
        divisiveis += 1


if divisiveis == 2:
    print(" O número {} é primo.". format(divisiveis))
else:
    print("Tente Novamente")

