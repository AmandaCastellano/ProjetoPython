# Crie uma função chamada 'numero_par(numero)' que receba um número como argumento e retorne True caso ele seja par ou False caso seja ímpar

def numero_par(numero):
    if numero % 2 == 0.0:
        return True

    else:
        return False


numero = int(input("Digite aqui um numero: "))

if numero_par(numero):
    print("Esse numero é par")

else:
    print("Esse numero é impar")

