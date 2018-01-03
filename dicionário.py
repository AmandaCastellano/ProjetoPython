"""
pessoas = {
    "SP": 447,
    "RJ": 323,
    "MG": 121
}

print(pessoas)
print(pessoas["SP"])
print(pessoas.get("MG"))

refeicoes = {
    "cafe": 5,
    "bolo": 10
}
print(refeicoes)

for indice in refeicoes:
    print(indice)
    preco = refeicoes[indice]
    print(preco)
    print()

def pegarrefeicoes(indices):
    refeicao = refeicoes.get(indices)
    print(indices)
    print(refeicao)

    if refeicao == None:
        print("A refeição não existe")
    else:
        print("Refeição: {}".format(refeicao))
    return refeicao

custo1 = pegarrefeicoes("bolo")
custo2 = pegarrefeicoes("cafe")
conta = 0
conta = conta + custo1
conta = conta + custo2
print(conta)
print()

#del refeicoes["bolo"]
print(refeicoes)
"""

precos = {
    "banana":4,
    "maca":2,
    "laranja":1.5,
    "pera":3
}

# print(precos)
# print(precos["pera"])





estoques = {
    "banana":6,
    "maca":0,
    "laranja":32,
    "pera":15
}
# print(estoques)

mantimentos = ["banana", "laranja", "maca"]



def computar_compra(mantimento):
    total = 0
    total2 = 0
    print("A sua compra foi realizada com suceeso")
    #print(mantimento)
    for fruta in mantimento:
        preco = precos[fruta]
        #print(preco)
        estoque = estoques[fruta]
        if estoque > 0:
            # print(estoque)
            print("Você comprou a fruta: {} e pagou R${:.2f} por ela.". format(fruta, preco))

            # print("\tPreço: {}".format(preco))
            # print("\tEstoques: {}".format(estoque))
            #total += preco * estoque
            # print(total)
            #print()
            total2 += preco
            estoques[fruta] = estoques[fruta] - 1

    print("O valor total pago foi de: R${:.2f}".format(total2))
    return total

computar_compra(mantimentos)
print(estoques)

mantimentos2 = []
frutas_disponiveis = list(precos.keys())

print("Frutas disponiveis: \n".format("\n ". join(frutas_disponiveis)))
print("Digite 'comprar' para realizar a compra")

while True:
    comprar_frutas = input("Qual fruta você gostaria de comprar? ")

    if comprar_frutas == "comprar":
        computar_compra(mantimentos)
        break
    else:
        mantimentos2.append(comprar_frutas)
