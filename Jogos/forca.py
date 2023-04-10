def jogo():
    print("***********************************")
    print("***Bem Vindo ao Jogo de Forca!!!***")
    print("***********************************\n")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False 

    while(not enforcou and not acertou):
        
        chute = input("Qual letra?")
        posicao = 0

        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei a letra {}, na posição {}.".format(letra, posicao))
            posicao = posicao + 1

        print("Jogando......")

    print("***********************************")
    print("**********Fim do jogo!!!***********")
    print("***********************************\n")

if (__name__ == "__main__"):
    jogo()