"""
Adicione R$ 50,00 ao elemento ‘dinheiro’ do inventário.
Adicione um novo item à carteira.
Ordene os itens da bolsa por ordem alfabética.
Exiba na tela quantos itens a pessoa tem na carteira e na bolsa.
Adicione uma nova lista ao inventário
chamada ‘bolso’, e inclua alguns itens.
"""

inventario = {
    "dinheiro": 500,
    "carteira": ["joia", "cartao", "caderno"],
    "mochila": ["faca", "blusa", "guarda-chuva", "garrafa"]
}

inventario["dinheiro"] = inventario["dinheiro"] + 50
inventario["carteira"].append("RG")


inventario["mochila"].sort()

quantidade_carteira = len(inventario["carteira"])
quantidade_mochila = len(inventario["mochila"])

inventario["bolso"] = ["chave,""celular"]

print(inventario)

