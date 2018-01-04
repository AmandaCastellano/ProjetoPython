"""
1 - Crie uma aplicação que rode infinitamente.
2 - A aplicação deverá perguntar ao usuário
se deseja realizar uma das seguintes ações
(independente se digitar maiúsculo ou minúsculo):
'C' ou 'Cadastrar' irá cadastrar uma nova
pessoa ao dicionário;
'L' ou 'Listar' irá listar as pessoas
cadastradas no dicionário;
'R' ou 'Remover' irá remover uma pessoa
(buscando pelo nome);
'E' ou 'Editar' irá editar uma pessoa
previamente cadastrada;
3 - A pessoa terá os seguintes dados: nome,
sobrenome, telefone e CPF.
4 - A cada ação realizada, o sistema deverá
informar uma mensagem de sucesso.
5 - Em caso de ações que procurem pessoas já
cadastradas no sistema (editar ou remover),
caso a pessoa não seja encontrada, exiba essa
mensagem para o usuário.
6 - Você deverá declarar uma função que recebe
 um nome de pessoa digitado pelo usuário e
 procure no dicionário por aquela pessoa.
 Caso encontre, retorne a pessoa encontrada.
 Caso contrário, exiba uma mensagem de que a
 pessoa não foi encontrada e pergunte
 novamente pelo nome da pessoa.
7 - A qualquer momento da aplicação, o usuário
 poderá cadastrar, listar, remover ou editar
 pessoas.
8 - Caso ele acesse alguma das opções acima e
 não queira prosseguir, digitar a palavra
 'cancelar' irá retornar ao menu principal.
"""
cadastros = []


while True:
    menu = print("Se você deseja: cadastrar uma nova pessoa, digite 'C' ou 'Cadastrar' ")
    print("Se você deseja: listar as pessoas cadastradas, digite 'L' ou 'Listar' ")
    print("Se você deseja: remover uma pessoa, digite 'R' ou 'Remover' ")
    print("Se você deseja: editar uma pessoa previamente cadastrada, digite 'E' ou 'Editar' ")
    resposta1 = input("O que você gostaria de fazer agora? ").upper()
    pessoas = {}
    if resposta1 == "CANCELAR":
        menu

    if resposta1 == "C" or resposta1 == "CADASTRAR":

        nome = input("Digite aqui o seu nome: ")
        pessoas["Nomes"] = nome
        sobrenome = input("Digite aqui o seu sobrenome: ")
        pessoas["Sobrenomes"] = sobrenome
        telefone = input("Digite aqui o seu telefone: ")
        pessoas["Telefones"] = telefone
        cpf = input("Digite aqui o seu CPF: ")
        pessoas["CPF"] = cpf
        print("Seu cadastro {}, {}, {}, {} foi realizado com sucesso!" . format(nome, sobrenome, telefone, cpf))
        cadastros.append(pessoas)
        print(cadastros)

    elif resposta1 == "L" or resposta1 == "LISTAR":
        for pessoa in cadastros:
            print(pessoa["Nomes"])

    elif resposta1 == "R" or resposta1 == "REMOVER":
        resposta2 = input("Quem você gostaria de remover? ")
        for pessoa in cadastros:
            if resposta2 == pessoa["Nomes"]:
                print(cadastros)
                cadastros.remove(pessoa)
                print(cadastros)
                print("consegui")
                print(" A pessoa {} foi removida com sucesso.". format(pessoa["Nomes"]))
            else:
                print("Pessoa não encontrada, tente novamente.")
    elif resposta1 == "E" or resposta1 == "EDITAR":
        resposta3 = input("Quem você gostaria de editar? ")
        for pessoa in cadastros:
            if resposta3 == pessoa["Nomes"]:
                indice = cadastros.index(pessoa)
                resposta4 = input("O que você gostaria de editar? Nome, sobrenome, telefone ou cpf?"). upper()
                if resposta4 == "NOME":
                    cadastros[indice]["Nomes"] = input("Qual será a alteração")
                    print("O seu cadastro foi alterado com sucesso.")
                elif resposta4 == "SOBRENOME":
                    cadastros[indice]["sobrenome"] = input("Qual será a alteração")
                    print("O seu cadastro foi alterado com sucesso.")
                elif resposta4 == "TELEFONE":
                    cadastros[indice]["TELEFONE"] = input("Qual será a alteração")
                    print("O seu cadastro foi alterado com sucesso.")
                elif resposta4 == "CPF":
                    cadastros[indice]["CPF"] = input("Qual será a alteração")
                    print("O seu cadastro foi alterado com sucesso.")
            else:
                    print("Pessoa não encontrada, tente novamente.")
    else:
        print("Desculpe, opção não encontrada, tente novamente.")

    print()
