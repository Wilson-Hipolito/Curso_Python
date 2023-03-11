
# Função input() - Função para receber dados do usuário.

"""
1° Forma de inserir e mostrar os dados do usuário:

print("Digite seu nome:")
nome = input()
print("Olá,"+ nome) - Pode ser usado a virgula ou o + na syntax.

2° Forma de inserir e mostrar os dados do usuário;

idade = input("Qual a sua idade? ")
print("Que legal vc tem, "+ idade, "anos.")

nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")

print("Seu nome é {0}, e sua idade é {1}.".format(nome, idade))
"""
#3° Forma de inserir e mostrar os dados do usuário.
nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")

print(f"Seu nome é {nome} e sua idade é {idade}")

