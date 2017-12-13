"""def potencia(base, expoente):
    resultado = base ** expoente
    print("{} elevado a {} é {}.".format(base, expoente, resultado))
    potencia(10,2)
"""
"""
import math as m

n = int(input("Digite um número: "))
x = m.sqrt(n)
print("A raiz quadrada de {} é: {}".format(n,x))
"""
"""
def nome_funcao(*args):
    print("Args recebidos: {}". format(args))
    maior_numero = max(args)
    print("Maior numero: {}". format(maior_numero))

nome_funcao(1,2,3,4)
"""
"""
 if type(1.2) == float:
     print("o numero é um float")
"""
"""

def custo_hotel(noites):
    total1 = noites * 140
    #print(total1)
    return total1

# hotel = custo_hotel(int(input("Quantos dias de hotel? ")))

def custo_aviao(cidade):
    if cidade == "SP":
        return 312.00
    elif cidade == "POA":
        return 447.00
    elif cidade == "R":
        return 831.00
    elif cidade == "M":
        return 986.00


# aviao = custo_aviao(input("Qual é a cidade? "))
# print(aviao)


def custo_carro(dias):
    total2 = dias * 40.0
    if dias >= 7:
        total2 -= 50
    elif dias >= 3:
        total2 -= 20
    # print(total2)
    return total2

# carro = custo_carro(int(input("Quantos dias de carro? ")))


def custo_total(cidade, dias):
    return custo_hotel(dias) + custo_aviao(cidade) + custo_carro(dias)

cidade = input("Quantos é a cidade? ")
dias = int(input("Quantos dias de carro? "))


custo = custo_total(cidade, dias)
print("O custo total de uma viagem de {} dias para para a cidade de {} foi de {}".format(dias,cidade,custo))
"""
