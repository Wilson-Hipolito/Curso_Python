import random


def jogo():

    print("***********************************")
    print("Bem Vindo ao Jogo de Adivinhação!!!")
    print("***********************************\n")

    numero_secreto = random.randrange(1, 51)
    tentativas = 0
    rodadas = 1
    pontos = 1000

    print("Escolha o nível de dificuldade, sendo: (1)Fácil (2)Médio (3)Difícil.")
    nivel = int(input("Defina o nível: "))
    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    elif nivel == 3:
        tentativas = 5
    else:
        print("Você digitou um nível inválido, tente novamente.\n")

    for rodadas in range(1, tentativas + 1):
        print("Tentativa {} de {}.".format(rodadas, tentativas))

        chute = input("Digite um número entre 1 e 50: ")
        print("Você digitou:", chute)
        chute = int(chute)

        if chute < 1 or chute > 50:
            print("Você digitou um número inválido!!!.")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Parabéns, você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou! Seu chute foi maior que o número secreto.")
            elif menor:
                print("Você errou! Seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("***********************************")
    print("Fim do jogo!!!")
    print("***********************************\n")


if __name__ == "__main__":
    jogo()
