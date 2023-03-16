"""Escopo das Variáveis
Escopo é o limite, o objetivo e o propósito no caso das variáveis.

Variáveis Globais - Declaradas fora dos blocos de uma função e podem ser usadas durante toda a execução do código.

Variáveis Locais - Declaradas dentro do bloco de uma função e não podem ser usadas por outras funções."""

x = 5

def funcao():
    x = 3
    print("Valor da variável local: ", x)

funcao()
print("Valor da variável global: ", x)

#Primeiro foi chamada a função com a variável local e depois a global


y = "Gabriel" #nome
z = 1,80 #altura
o = "000.000.000-00" #cpf
n = 38 #idade

print(y, z, o, n)

#Quando for declarar uma variável o correto é utilizar o nome para o qual a variável está sendo criada, para ficar mais fácil do código ser lido, conforme o exemplo abaixo. O exemplo acima deve ser evitado.


nome = "Gabriel"
altura = 1,80
cpf = "000.000.000-00"
idade = 38

print(nome, altura, cpf, idade)