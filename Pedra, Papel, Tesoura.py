from random import randint

pontos_usuario = 0
pontos_pc = 0
empates = 0

while True:

    jogada_usuario = input("Qual é a sua jogada? (Pedra, papel ou tesoura) Ou digite 'Sair' para sair do jogo. ")
    jogada_pc = randint(0,3)

    if jogada_pc == 0:
        print("A jogada do PC é: Pedra")
    elif jogada_pc == 1:
        print("A jogada do PC é: Papel")
    elif jogada_pc == 2:
        print("A jogada do PC é: Tesoura")

    if jogada_usuario.upper() == "Pedra".upper():
        if jogada_pc == 1:
            print("Papel embrulha a pedra. Você perdeu!")
            pontos_pc += 1
        elif jogada_pc == 2:
            print("Pedra amassa tesoura.Você ganhou!")
            # vitoria = True
            pontos_usuario += 1
        else:
            print("Vocês empataram.Tente Novamente!")
            empates += 1
            # empate = True
    elif jogada_usuario.upper() == "Papel".upper():
        if jogada_pc == 0:
            print("Papel embrulha a pedra. Você ganhou!")
            # vitoria = True
            pontos_usuario += 1
        elif jogada_pc == 2:
            print("Pedra amassa tesoura.Você perdeu!")
            pontos_pc += 1
        else:
            print("Vocês empataram. Tente Novamente!")
            # empate = True
            empates += 1
    elif jogada_usuario.upper() == "Tesoura".upper():
        if jogada_pc == 1:
            print("Tesoura corta papel. Você ganhou!")
            # vitoria = True
            pontos_usuario += 1
        elif jogada_pc == 2:
            print("Pedra amassa tesoura.Você perdeu!")
            pontos_pc += 1
        else:
            print("Vocês empataram. Tente Novamente!")
            # empate = True
            empates += 1
    elif jogada_usuario.upper() == "Sair".upper():
        print("O Placar do Jogo é:")
        print("Pontos do Jogador: {}".format(pontos_usuario))
        print("Pontos do Computador: {}".format(pontos_pc))
        print("Empates: {}".format(empates))
        break

    else:
        print("Eu não entendi, tente novamente!")
    print()

