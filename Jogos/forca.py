def jogo():
    print("\n\n***********************************")
    print("***Bem Vindo ao Jogo de Forca!!!***")
    print("***********************************\n")

    palavra_secreta = "banana"
    letras_acertadas = ['_', '_', '_', '_', '_', '_']
    enforcou = False 
    acertou = False 

    print(letras_acertadas, "\n")

    while(not enforcou and not acertou):
        
        chute = input("Qual letra? ")
        chute = chute.strip()
        
        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra 
            posicao = posicao + 1

        print(letras_acertadas)
        letras_faltando = str(letras_acertadas.count('_'))
        print("Ainda faltam acertar {} letras.".format(letras_faltando))

    print("***********************************")
    print("**********Fim do jogo!!!***********")
    print("***********************************\n")

if (__name__ == "__main__"):
    jogo()