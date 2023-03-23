print("***********************************")
print("Bem Vindo ao Jogo de Adivinhação!!!")
print("***********************************\n")

numero_secreto = 42
tentativas = 3
rodadas = 1

while rodadas <= tentativas:
    print("Tentativa:", rodadas, "de", tentativas)
    chute = input("Digite o seu número: ")
    print("Você digitou:", chute)
    chute = int(chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns, você acertou!\n")
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto.\n")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto.\n")

    rodadas = rodadas + 1
    print("***********************************")
    print("Fim do jogo!!!")
    print("***********************************\n")
