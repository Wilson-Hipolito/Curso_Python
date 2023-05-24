import forca
import jogo_adivinhacao

def escolhe_jogo():

    print("***********************************")
    print("******Escolha o Seu Jogo!!!********")
    print("***********************************\n")

    print("Jogo da Forca (1) | Jogo De Adivinhação (2)")

    jogo = int(input("Qual Jogo Você Escolhe? "))

    if jogo == 1:
        print("Voce Escolheu o Jogo da Forca.")
        forca.jogo()
    elif jogo == 2:
        print("Você escolheu o Jogo de Adivinhação.")
        jogo_adivinhacao.jogo()
    else:
        print("Você Não Escolheu Uma Opção Valida.")


if __name__ == "__main__":
    escolhe_jogo()
