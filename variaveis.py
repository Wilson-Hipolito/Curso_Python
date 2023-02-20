x = 5 # x Recebe o valor de 5
y = 3.5 # Valor float
z = 1+4j # Valor Complexo

w = "Ana"
w = 'Ana' # No Python pode ser usado aspas simples, bem como aspas Duplas
 
# AS variáveis não podem começar com múmero, ou seja, elas podem ser de "A-z", "0-9" e "_"
# Além disso no Python existe case sensitive, ou seja, há diferença entre letras minúsculas e maiúsculas, EX: altura, Altura e ALTURA 

h, j, l = 1, 3, 5 # Podem ser criadas várias variáveis ao mesmo tempo e inserido valores nas mesmas 
print(h)
print(j)
print(l)

# Podemos atribuir a várias variáveis o mesmo valor, conforme abaixo 
a = b = c = " Faz o curso de Python"

print(a)
print(b)
print(c)

# Juntar variáveis 
h = w + a
print(h)

# Somar variáveis
l = x + j
print(l)

# Python é uma linguagem de tipagem forte e dinâmica, pois não é estática, pois as variáveis podem ter seus valores alterados depois de ser declarada
l = w + x
print(l) # Vai dar erro , pois o Python não pode concatenar uma string com um número
