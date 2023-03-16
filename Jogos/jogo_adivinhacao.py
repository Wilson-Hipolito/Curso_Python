print("***********************************")
print("Bem Vindo ao Jogo de Adivinhação!!!")
print("***********************************\n")

numero_secreto = 42

chute = input("Digite o seu número: ")
print("Você digitou:", chute)

if numero_secreto == int(chute):
    print("Você acertou!")
else:
    print("Você errou!")
