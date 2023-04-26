import random


def jogo():
    imprime_msg_abertura()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 6

    print("Palavra Secreta:", letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("\nTente acertar, digite uma letra: ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            print("Parabéns você acertou a letra !!!")
            posicao = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            print("Você errou a letra !!!")
            erros += -1
        enforcou = erros == 0
        acertou = "_" not in letras_acertadas
        print("Palavra Secreta: ", letras_acertadas)
        letras_faltando = str(letras_acertadas.count('_'))
        print("Faltam acertar {} letras.".format(letras_faltando))
        print("Você possui {} tentativas.".format(erros))
    if acertou:
        print("\n VOCÊ GANHOU, PARABÉNS !!!")
    else:
        print("\nVOCÊ PERDEU, TENTE NOVAMENTE !!!")
    print("\n***********************************")
    print("**********FIM DO JOGO !!!**********")
    print("***********************************\n")


def imprime_msg_abertura():
    print("\n***********************************")
    print("   BEM VINDO AO JOGO DA FORCA !!!  ")
    print("***********************************\n")


def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]


if __name__ == "__main__":
    jogo()
