"""
1 - Peça para o usuário digitar 3 números, envie-os para uma função
chamada 'pegar_maior_valor' utilizando o método '*args' e retorne o maior
deles utilizando a função max()
2 - Peça para o usuário digitar 3 números, envie-os para uma função
chamada 'pegar_menor_valor' utilizando o método '*args' e retorne o menor
deles utilizando a função min()
3 - Peça para o usuário digitar 3 números positivos e 3 números negativos,
 extraia o módulo (versão positiva) de cada número utilizando a função
 abs() e exiba na tela o maior e o menor número (utilize as funções
 criadas anteriormente no exercício 1 e 2).
4 - Declare uma função que recebe um número e o formata de acordo com o
tipo de sua variável (utilize a função type())
- Se a variável for um float, formate-a como moeda, exemplo:
- Entra a variável float 20.0 e exibe na tela R$ 20,00. Regra de
formatação: {:.2f}, onde 2 representa o número e casas decimais.
- Se a variável for um int, formate-a deixando com pelo menos 5 dígitos
(colocando zeros na frente). Regra de formatação: {:02d}, onde 2
representa o número de dígitos.
- Se a variável for uma string, formata-a para que utilize 10 espaços
adicionais à esquerda. Regra de formatação: {:>1}, onde 1 representa o
número de espaços que irá utilizar.
- Caso a variável não seja nenhuma dessas, exiba a mensagem "Esse tipo de
variável não está mapeado."
"""



def solicitar_int():
	return int(input("Digite um número inteiro: "))

def solicitar_int_negativo():
	return int(input("Digite um número inteiro negativo: "))

def solicitar_float():
	return float(input("Digite um número decimal: "))

def solicitar_string():
	return input("Digite uma string: ")


"""
def pegar_maior_valor(*args):
    print(args)
    maior_numero = max(args)
    print(" O maior número é o: {}".format(maior_numero))

def pegar_menor_valor(*args):
    print(args)
    menor_numero = min(args)
    print(" O menor número é o: {}".format(menor_numero))

def pegar_menor_maior_valor(*args):
    print(args)
    pegar_menor_maior_valor = max(args)
    print(" O maior número é o: {}".format(pegar_menor_maior_valor))
    pegar_menor_maior_valor = min(args)
    print(" O menor número é o: {}".format(pegar_menor_maior_valor))


n_1 = solicitar_int()
n_2 = solicitar_int()
n_3 = solicitar_int()
print(pegar_maior_valor(n_1,n_2,n_3))

n_4 = solicitar_int()
n_5 = solicitar_int()
n_6 = solicitar_int()
pegar_menor_valor(n_4, n_5, n_6)

n_7 = solicitar_int()
n_8 = solicitar_int()
n_9 = solicitar_int()
n_10 = solicitar_int_negativo()
n_11 = solicitar_int_negativo()
n_12 = solicitar_int_negativo()
pegar_menor_maior_valor(n_7, n_8, n_9, abs(n_10), abs(n_11), abs(n_12))
"""

def solicitar(numero):
    tipo = type(numero)
    print(tipo)
    if tipo == int:
        print("A formatação do INTEIRIO é:{:05d}".format(numero))
    elif tipo == float:
        print("A formatação do FLOAT é: R${:.2f}".format(numero))
    elif tipo == str:
        print("A formatação da STRING é: {:>10}".format(numero))
    else:
        print("Essa variavel não está mapeada")


numero1 = solicitar_int()
numero2 = solicitar_float()
numero3 = solicitar_string()
booleano = True

solicitar(numero1)
solicitar(numero2)
solicitar(numero3)

