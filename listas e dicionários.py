paulo = {
    "nome": "Paulo Salvatore",
    "atividades": [10.0, 8.0, 7.5],
    "quizess": [8.5, 9.0, 6.5],
    "testes": [5.0, 9.5, 6.0]
}

luisa = {
    "nome": "Luísa Oliveira",
    "atividades": [1.0, 6.0, 5.5],
    "quizess": [6.5, 4.0, 2.0],
    "testes": [1.5, 2.0, 3.0]
}

ana = {
    "nome": "Ana Azevedo ",
    "atividades": [7.5, 7.5, 6.0],
    "quizess": [10.0, 10.0, 4.0],
    "testes": [4.0, 8.5, 1.0]
}

estudantes = [paulo, luisa, ana]

def media(numeros):
    total = sum(numeros)
    # print(total)
    return total / len(numeros)

def pegar_media(aluno):
    atividades = (media(aluno["atividades"]))
    quizess = (media(aluno["quizess"]))
    testes = (media(aluno["testes"]))
    total = (atividades * 0.1) + (quizess * 0.3) + (testes *0.6)
    return total

def checar_aprovacao(aluno):
    nome = aluno["nome"]
    media_calculada = pegar_media(aluno)
    print("Aluno: {}\nMédia: {:.2f}".format(nome, media_calculada))

    if media_calculada < 4.0:
        print("\t{} foi Reprovado".format(nome))

    elif media_calculada <= 6.0:
        print("\t{} está de Exame".format(nome))

    else:
        print("\t{} está Aprovado".format(nome))
    print()


# checar_aprovacao(paulo)
# checar_aprovacao(ana)
# checar_aprovacao(luisa)

def pegar_media_classe(alunos_classe):

    medias_alunos_classe = []

    for aluno_classe in alunos_classe:
        media_calculada = pegar_media(aluno_classe)
        medias_alunos_classe.append(media_calculada)

    media_classe = media(medias_alunos_classe)
    return media_classe

for estudante in estudantes:
    checar_aprovacao(estudante)

media_classe_calculada = pegar_media_classe(estudantes)
print("Média da Classe: {:.2f}".format(media_classe_calculada))
