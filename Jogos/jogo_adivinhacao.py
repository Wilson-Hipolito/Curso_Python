print("***********************************")
print("Bem Vindo ao Jogo de Adivinhação!!!")
print("***********************************\n")

numero_secreto = 42
tentativas = 3
rodadas = 1

for rodadas in range(1, tentativas + 1):
    print("Tentativa {} de {}.".format(rodadas, tentativas))
    chute = input("Digite um número entre 1 e 50: ")
    print("Você digitou:", chute)
    chute = int(chute)

    if(chute < 1 or chute > 50):
        print("\nVocê digitou um número inválido!!!.\n")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns, você acertou!\n")
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto.\n")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto.\n")

    print("***********************************")
    print("Fim do jogo!!!")
    print("***********************************\n")
