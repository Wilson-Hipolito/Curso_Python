#Exercício n° 5 - Canversor de Real para Dólar.
#Formular para resolver o exercício: real * dólar

print("Exercício n°5 - Conversor de Real para Dólar.")

real = input("Quantos reais quer converter? ")
cotacao = 5.22
dolar = float(real) / float(cotacao)

print(f"O valor em Dólar é {dolar}.")
