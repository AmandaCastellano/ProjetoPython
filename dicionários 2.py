"""
dicionario = {
    "Temer": "PMDB",
    "Lula": "PT",
    "Aécio": "PMDB"

}

for chave in dicionario:
    print(chave)
    valor = dicionario[chave]
    print(valor)
    print()
"""

partidos = {
    "PT": {
        "nome": "Partido dos Trabalhadores",
        "sede": "Brasília",
        "presidente": "Gleisi Hoffmann",
        "numero_eleitoral": 13,
        "candidato_proprio": True,
        "ideologias": [
            "Socialismo democrático",
            "Desenvolvimentismo",
            "Lulismo",
            "Trotskismo",
            "Democracia"
        ]
    },
    "PV": {
        "nome": "Partido Verde",
        "sede": "São Paulo",
        "presidente": "José Luiz Penna",
        "numero_eleitoral": 43,
        "candidato_proprio": False,
        "ideologias": [
            "Ambientalismo",
            "Ecologismo",
            "Liberalismo social",
            "Progressismo",
            "Social democracia",
            "Democracia"
        ]
    }
}

"""
pt = partidos["PT"]
print()

def pegar_ideologia_partidos(partidos):
    print(partidos)
    return partidos[partido]["ideologias"]

def pegar_campo_partidos(partido,campo):
    return partidos[partido][campo]

ideologia = pegar_campo_partidos("PV","ideologia")

def contar_iedeologias(partidos):
    return len(partidos)

print(partidos)
"""

def procurar_partidos_ideologias(ideologia):
    lista1 =[]
    for sigla in partidos:
        # print(sigla)
        # print(partidos)
        # print(ideologia)
        variavel = partidos[sigla]["ideologias"]
        #print(variavel)

        if variavel.count(ideologia)> 0:
            lista1.append(sigla)
            #print(lista1)
    return lista1


partidos_democracia = procurar_partidos_ideologias("Democracia")
print(partidos_democracia)

partidos_socialismo = procurar_partidos_ideologias("Socialismo democrático")
print(partidos_socialismo)
