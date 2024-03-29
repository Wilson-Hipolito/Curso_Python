import random


def jogo():
    imprime_msg_abertura()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 7

    print("Palavra Secreta:", letras_acertadas)

    while (not enforcou and not acertou):

        chute = pede_chute()

        if chute in palavra_secreta:
            print("Parabéns você acertou a letra !!!")
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            print("Você errou a letra !!!")
            erros += -1
            desenha_forca(erros)
        enforcou = erros == 0
        acertou = "_" not in letras_acertadas
        print("Palavra Secreta: ", letras_acertadas)
        letras_faltando = str(letras_acertadas.count('_'))
        print("Faltam acertar {} letras.".format(letras_faltando))
        print("Você possui {} tentativas.".format(erros))
    if acertou:
        imprime_vencedor()
    else:
        imprime_perdedor(palavra_secreta)


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_vencedor():
    print("\n VOCÊ GANHOU, PARABÉNS !!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_perdedor(palavra_secreta):
    print("\nVOCÊ PERDEU, TENTE NOVAMENTE !!!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[posicao] = letra
        posicao += 1


def pede_chute():
    chute = input("\nTente acertar, digite uma letra: ")
    chute = chute.strip().upper()
    return chute


def imprime_msg_abertura():
    print("\n***********************************")
    print("   BEM VINDO AO JOGO DA FORCA !!!  ")
    print("***********************************\n")


def carregar_palavra_secreta():
    arquivo = open('/media/wilson/HDD Secundário/Documentos/Cursos/TI/Python/Curso_Python/Jogos/palavras.txt', "r")
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
