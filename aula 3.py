def exibir_numero(numero):
     print("O numero exibido é: {}.".format(numero))
     resultado = (numero ** 2) + (numero * 1.1)
     print("O resultado é: {}".format(resultado))

numero = int(input(" Número: "))
exibir_numero(numero)


