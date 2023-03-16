"""
Exercícios - Python

OBS: Todos os exercícios devem ser utilizar a função input,
de forma que o usuário possa determinar os dados de entrada.

01 - Área de um retângulo.
02 - Área de um quadrado.
03 - Se um produto que vc quer comprar custa (??) reais,
qual será o valor do mesmo com um desconto de (??)%.
04 - Área de um circulo.
05 - Conversão de reais para dólar.
06 - Conversão de dólar para real.

"""
#Exercício n° 1 - Área do Retângulo
#Formular para resolver o exercício: area = base * altura
print("Exercício 1° - Calculo da área de um retângulo.")

base = input("Qual o tamanho da base do seu retângulo? ")
altura = input("Qual o tamanho da altura do seu retângulo? ")
area = float(base) * float(altura)

print(f"O seu retângulo possui area de: {area} Unidades de medida")

