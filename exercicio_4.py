#Exercício n° 4 - Calcular a area de um circulo.
#Formular para resolver o exercício: A área de um círculo é pi vezes o raio elevado ao quadrado (A = π r²).

print("Exercício n°4 - Calcular a area de um circulo.")

valorpi = 3.14159
raio = input("Qual o raio do circulo? ")
raioelevado = float(raio) * float(raio)
area = valorpi * raioelevado

print(f"A area do circulo é {area}.")

